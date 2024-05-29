import transformers as t
from PIL import Image
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mb_utils.src import logging
from .get_weight import get_seg, get_final_mask, get_final_img, get_histogram, get_val
from urllib.parse import urlparse
from typing import List,Dict,Union

logger = logging.logger 
model_checkpoint = '/Users/test/test1/mit-segformer-s' 
model = t.TFSegformerForSemanticSegmentation.from_pretrained(model_checkpoint)

__all__ = ["load_color_values", "process_pipeline"]

def load_color_values(csv_path : str, logger: logging.Logger = None) -> Dict:
    """
    Function to load color values from a CSV file
    Args:
        csv_path (str): Path to the CSV file
        logger (Logger): Logger object
    Returns:
        dict: Dictionary containing color values
    """
    if logger:
        logger.info("Loading color values from CSV")
    color_dict = {}
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        taxcode = row['taxonomy_code']
        site = row['site_id']
        color = row['colors']
        if taxcode and site and color:
            composed_key = f"{site}_{taxcode}"
            color_list = eval(color)
            color_dict[composed_key] = color_list
    return color_dict

def process_pipeline(input_csv_path : str,gt_csv_path: str  ,val_color_csv_path : str,logger: logging.logger = None, **kwargs) -> Union[pd.DataFrame,List]:
    """
    Function to process the pipeline of Production Planning
    Args:
        input_csv_path (str): Path to the input CSV file
        gt_csv_path (str): Path to the groundtruth CSV file
        val_color_csv_path (str): Path to the color values CSV file
        logger (Logger): Logger object
    Returns:
        pd.DataFrame: Output dataframe
        List: List of results
    """

    color_dict = load_color_values(val_color_csv_path)
    groundtruth_df = pd.read_csv(gt_csv_path)
    
    input_df = pd.read_csv(input_csv_path)
    input_df['mask'] = ''
    input_df['final_image'] = ''
    input_df['pixel_count'] = 0
    input_df['histogram'] = ''
    input_df['pred_w2'] = 0.0
    input_df['error'] = 0.0
    input_df['success'] = False

    use_input_groundtruth = 'input_groundtruth' in input_df.columns

    entries = []
    for _, row in input_df.iterrows():
        s3_image_path = row['s3_image_path']
        site_id = row['site_id']
        taxonomy_code = row['taxonomy_code']
        input_groundtruth = row['input_groundtruth'] if use_input_groundtruth else 0
        if s3_image_path and site_id and taxonomy_code:
            composed_key = f"{site_id}_{taxonomy_code}"
            entries.append((site_id, s3_image_path, composed_key, taxonomy_code))
    
    if not entries:
        if logger:
            logger.error("No valid entries found in the CSV file")
        raise ValueError("No valid entries found in the CSV file")
    
    results = []
    for index, (site_id, s3_image_path, composed_key, taxonomy_code) in enumerate(entries):
        try:
            if composed_key not in color_dict:
                if logger:
                    logger.error(f"No color found for key {composed_key}. Skipping image {s3_image_path}.")
                input_df.at[index, 'success'] = False
                continue
            color = color_dict[composed_key]
        
            site_dir = os.path.join('/pp_images/images', site_id)
            os.makedirs(site_dir, exist_ok=True)
        
            parsed_url = urlparse(s3_image_path)
            original_filename = os.path.basename(parsed_url.path)
            download_path = os.path.join(site_dir, original_filename)
        
            if logger:
                logger.info(f"Processing image: {local_image_path}")
            local_image_path = download_image_from_s3(s3_image_path, download_path)
        
            a, b, c, d, e = get_seg(local_image_path, mask_val=0.08, resize=True, new_bg_removal=True, equalize=True)
        
            mask_vals = 50
            new_mask = get_final_mask(a, d, color=color, val=mask_vals)

            masks_dir = os.path.join('data/pp_images/masks')
            os.makedirs(masks_dir, exist_ok=True)
            mask_save_path = os.path.join(masks_dir, f"{original_filename}_mask_{mask_vals}.png")
            mask_image = Image.fromarray(new_mask.astype(np.uint8))
            mask_image.save(mask_save_path)
            input_df.at[index, 'mask'] = mask_save_path

            new_final_img = get_final_img(a, new_mask, mask_val=0.2)

            final_images_dir = os.path.join('data/pp_images/final_image')
            os.makedirs(final_images_dir, exist_ok=True)
            final_img_save_path = os.path.join(final_images_dir, f"{os.path.basename(local_image_path)}_final.png")
            final_image = Image.fromarray(new_final_img.astype(np.uint8))
            final_image.save(final_img_save_path)
            input_df.at[index, 'final_image'] = final_img_save_path
        
            new_histogram, bin_edges = get_histogram(new_final_img)

            pixel_count = new_histogram[-1]
            histograms_dir = os.path.join('data/pp_images/histograms')
            os.makedirs(histograms_dir, exist_ok=True)
            histogram_save_path = os.path.join(histograms_dir, f"{os.path.basename(local_image_path)}_{pixel_count}_hist.png")
            input_df.at[index, 'pixel_count'] = pixel_count
            input_df.at[index, 'histogram'] = histogram_save_path
        
            plt.figure()
            plt.hist(new_final_img.ravel(), bins=bin_edges)
            plt.title('Histogram')
            plt.xlabel('Pixel Value')
            plt.ylabel('Frequency')
            plt.savefig(histogram_save_path)
            plt.close()       

            reference_row = groundtruth_df[groundtruth_df['taxonomy_code'] == taxonomy_code]
            if not reference_row.empty:
                reference_pixel_count = reference_row.iloc[0]['reference_pixel_count']
                groundtruth_weight = reference_row.iloc[0]['groundtruth']

                weight2 = input_groundtruth if input_groundtruth else 0
                pred_w2, error = get_val(reference_pixel_count, pixel_count, groundtruth_weight, weight2)
            else:
                if logger:
                    logger.error(f"No groundtruth data found for taxonomy_code {taxonomy_code}.")

            input_df.at[index, 'pred_w2'] = pred_w2
            input_df.at[index, 'error'] = error
            input_df.at[index, 'success'] = True if pred_w2 is not None else False

            results.append((a, b, c, d, e, new_mask, new_final_img, new_histogram, pred_w2, error))
        except Exception as e:
            if logger:
                logger.error(f"Error processing image {s3_image_path}: {e}")
            input_df.at[index, 'success'] = False
            continue
    
    output_csv_path = "data/pp_images/csv/output_csv/output.csv"
    input_df.to_csv(output_csv_path, index=False)

    if logger:
        logger.info(f"Processing complete. Output saved to {output_csv_path}")
        
    return output_csv_path, results



# add logger
# error if there is not taxcode and skip that image - done
# column to output with failure or success -done
# new csv with refrence image and groundtruth, and histogram pixel inside segmentation, model-checkpoint - done
# download to GH2  particular location - done
# save everything mask(save the 50 val in the name of file as _50) histogram and final image - done 
# save everything locally - done
# save the plots locally only when input is given add plot boolean input to process_pipeline at images_plot folder 
# yaml file for inputs
# write the _mask after the name
# s3cmd ls s3://pp-image-capture-processed-useast1-prod/siteId=33263/mealService=b514a5da-2bcf-4330-8a3c-f17e7f85a922/
# get-repsonse -> get-image -> download image -> 
# aslo csv files