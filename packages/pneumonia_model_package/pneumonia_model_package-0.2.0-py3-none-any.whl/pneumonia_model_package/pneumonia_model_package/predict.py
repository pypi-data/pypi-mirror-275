import os,sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import typing as t
import pandas as pd
import numpy as np
from pathlib import Path
from loguru import logger


# modules necessary for our script
from pneumonia_model_package.pneumonia_model_package.data_processing import data_manager as dm
from pneumonia_model_package.pneumonia_model_package.config.core import config
from pneumonia_model_package.pneumonia_model_package import __version__
from pneumonia_model_package.pneumonia_model_package.config import core
from pneumonia_model_package.pneumonia_model_package.data_processing import dataset_preprocessor as dp

#LOAD THE KERAS TRAINED MODEL 
cnn_model = dm.load_pneumonia_model()


def make_single_prediction(*, image_name: str, image_dir: str):
    """ make a single predictiong using the saved model when give
    image name and directory path"""
    
    dataframe = dm.load_single_img(data_folder=image_dir, filename=image_name)

    updated_data = dataframe.drop(['label'], axis=1)
    
    logger.log(_Logger__message = updated_data, _Logger__level = 5)

    """ call the cnn model predict method"""
    preprocessed_data = dp.image_resizing_and_dataset_creation(
        data= updated_data,
        c_mode= None, 
        shufle= False,
        ylabelname= None
    )
    logger.info('Loaded data being preprocessed')

     # make prediction
    prediction = cnn_model.predict(preprocessed_data)
    # obtain the class with the highest probability
    predicted_class = np.argmax(prediction, axis=1)
    logger.info('Generating prediction on the data')

    results = ['NORMAL' if result == 0 else 'PNEUMONIA' for result in predicted_class]
    logger.log(_Logger__message = dict(image_class = results, version = __version__),  _Logger__level = 20)
    return dict(
        image_class = results,
        version = __version__
        )

def make_bulk_prediction(*, images_data: Path) -> dict:
    """" use this method to retrieve batch of predictions"""
    # Load the image files 
    loaded_images = dm.load_multiple_img_via_path(folder=images_data)

    updated_data = loaded_images.drop(['label'], axis=1)

    # convert images data to a dataset 
    dataset_of_images  = dp.image_resizing_and_dataset_creation(
        data= updated_data,
        c_mode= None,
        shufle= False,
        ylabelname= None)
    logger.info('Loaded data being preprocessed')

    # call the cnn model predict method
    pred = cnn_model.predict(dataset_of_images)
    logger.info('Generating prediction on the data')
    
    predicted_class = np.argmax(pred, axis=1)
    # this will be used to map the class names to the predicted class
    results = ['NORMAL' if result == 0 else 'PNEUMONIA' for result in predicted_class]
     
    logger.log(_Logger__message = dict(image_classes = results, version = __version__),  _Logger__level = 20)

    return dict(
        image_classes = results,
        version = __version__
    )

# if __name__ == '__main__':
#     make_single_prediction(image_name=config.modelConfig.sample_test_image, image_dir=core.VAL_FOLDER)
#     make_bulk_prediction(images_data=core.VAL_FOLDER)