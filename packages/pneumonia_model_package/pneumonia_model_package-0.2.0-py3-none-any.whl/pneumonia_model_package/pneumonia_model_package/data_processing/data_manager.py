import os
import logging
import re
import numpy as np
from typing import Union
import tensorflow as tf
import tensorflow_datasets as tfds
from PIL import Image
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import normalize
import pandas as pd 
from pathlib import Path
from loguru import logger
from tqdm import tqdm

from keras.models import load_model
from glob import glob

logging.basicConfig(level=logging.ERROR)

from pneumonia_model_package.pneumonia_model_package.config import core
from pneumonia_model_package.pneumonia_model_package.config.core import config, TRAINED_MODEL_DIR

AUTOTUNE = tf.data.AUTOTUNE
tfds.core.utils.gcs_utils._is_gcs_disabled = True
os.environ['NO_GCE_CHECK'] = 'true'

# FUNCTIONS SPECIFIC FOR A DIFFERENT DATASET APPLICABLE TO REAL IMAGE FORMATS LIKE JPEG, PNG ...
# ================== BEGIN =============== #
def load_single_img(data_folder: str, filename: str) -> pd.DataFrame:
    """ loads a single image and convert it to a dataframe"""
    image_list = []

    for image in glob(os.path.join(data_folder, f'{filename}')):
        # Create a DataFrame for each image and its target
        tmp = pd.DataFrame([[image, 'unknown']], columns=['image', 'label'])
        image_list.append(tmp)

    # Combine the list of DataFrames by concatenating them to form a new DataFrame
    final_df = pd.concat(image_list, ignore_index=True)
    
    return final_df

def load_multiple_img_via_path(folder: Path) -> Union[pd.DataFrame, pd.Series]:
    """ loads  multiple images and converts them to a dataframe"""
    image_names = []

    # Iterate through files in the folder
    for filename in os.listdir(folder):
        # Check if the file is an image
        if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
            # Read the image file
            image_path = os.path.join(folder, filename)
            
            # Append image name to lists
            image_names.append(image_path)
    # Create DataFrame from image data
    df = pd.DataFrame({"image": image_names, "label": 'unknown'})
    logger.log(_Logger__message = df.shape, _Logger__level = 5)
    return df


# Use this function for the training in the train model module
def load_image_paths(data_folder: str) -> pd.DataFrame:
    """Makes dataframe with image path and target."""

    images_df = []

    # navigate within each folder
    for class_folder_name in tqdm(os.listdir(data_folder)):
        class_folder_path = os.path.join(data_folder, class_folder_name)

        # collect every image path
        for image_path in glob(os.path.join(class_folder_path, "*.jpeg")):
            tmp = pd.DataFrame([image_path, class_folder_name]).T
            images_df.append(tmp)

    # concatenate the final df
    images_df = pd.concat(images_df, axis=0, ignore_index=True)
    images_df.columns = ['image', 'label']
    
    logger.log(_Logger__message = images_df.shape, _Logger__level = 20)

    return images_df

# def resize_and_create_dataset(df: pd.DataFrame , img_size:int):
#     """ resize and create a dataset"""

#     img_list =  []
#     for image in df['image']:
#         # loading and resizing
#         obj_img = load_img(image, target_size=(img_size, img_size))
#         # converting images to array
#         obj_arr = img_to_array(obj_img, dtype='float64')
#         img_list.append(obj_arr)

#     final_img_array = np.array(img_list)
#         # normalizing the dataset
#     dataset_norm = normalize( final_img_array, axis=-1, order=2)
#     return dataset_norm


def retain_best_model(path: Path) -> None:
    """" retains only best saved model after training"""
    # Define the folder path
    folder_path = path

    # Get all files in the folder
    files = os.listdir(folder_path)

    # Filter only the .keras files related to kitchenware_xception_model
    keras_files = [file for file in files if file.startswith('pneumonia_xception_model_val-acc_') and file.endswith('.keras')]

    if not keras_files:
        logger.info("No valid model files found in the directory.")

    # Extract the accuracy from filenames and identify the highest one
    max_accuracy = -1.0
    best_file = ""

    for file in keras_files:
        try:
            accuracy_str = file.split('_')[-1].replace('.keras', '')
            accuracy = float(accuracy_str)
            if accuracy > max_accuracy:
                max_accuracy = accuracy
                best_file = file
        except:
            logger.error(f"Error processing file: {file}")
            continue

    # Retain the file with the highest accuracy and remove the others
    for file in keras_files:
        if file != best_file:
            try:
                os.remove(os.path.join(folder_path, file))
                logger.info(f"Removed file: {file}")
            except:
                logger.error(f"Error removing file: {file}")

    logger.info(f"Retained file: {best_file}")

    # # Initialize dictionaries to store filenames and corresponding values
    # val_bin_acc_dict = {}
    # prec_dict = {}
    # recall_dict = {}

    # pattern = r"prec-(\d+\.\d+)_valprec-(\d+\.\d+)_recall-(\d+\.\d+)\.keras"

    # # Parse filenames and populate dictionaries
    # for file in files:
    #     match = re.search(pattern, file)
    #     if match:
    #         val_bin_acc, prec, recall = map(float, match.groups())
    #         val_bin_acc_dict[val_bin_acc] = file
    #         prec_dict[prec] = file
    #         recall_dict[recall] = file

    # # Get the filename with the highest value for each attribute
    # max_val_bin_acc_file = val_bin_acc_dict[max(val_bin_acc_dict)]
    # max_prec_file = prec_dict[max(prec_dict)]
    # max_recall_file = recall_dict[max(recall_dict)]

    # # Remove all files except the ones with the highest values
    # for file in files:
    #     if file != max_val_bin_acc_file and (file != max_prec_file or file != max_recall_file):
    #         os.remove(os.path.join(folder_path, file))

def load_pneumonia_model():
    """ Load a keras model from disk"""
    logger.info(f'Loading model from {TRAINED_MODEL_DIR}')
    for file in os.listdir(core.TRAINED_MODEL_DIR):
        if file.endswith(".keras"):
            model_file = os.path.join(core.TRAINED_MODEL_DIR, file)

    build_model = load_model(model_file)
    return build_model
# ================= END =================== #

