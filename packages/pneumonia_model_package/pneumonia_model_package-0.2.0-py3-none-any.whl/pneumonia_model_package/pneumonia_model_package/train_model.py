import os,sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import keras
from pneumonia_model_package.config import core
from pneumonia_model_package.config.core import config
from pneumonia_model_package.data_processing import data_manager
from pneumonia_model_package.data_processing.data_manager import *
import model as m
from pneumonia_model_package.data_processing import dataset_preprocessor as dp


filepath = "pneumonia_xception_model_val-acc_{val_accuracy:.3f}.keras"

checkpoint = keras.callbacks.ModelCheckpoint(
    f"{str(core.TRAINED_MODEL_DIR)}/{filepath}",
    save_best_only=True,
    monitor='val_accuracy',
    mode='max'
)

early_stopping_cb = keras.callbacks.EarlyStopping(
    patience=10, restore_best_weights=True
)

def run_training(save_results: bool =  True) -> None:
    """ train the model"""
    #load the image data
    train_data = data_manager.load_image_paths(data_folder=core.TRAIN_FOLDER)
    test_data = data_manager.load_image_paths(data_folder=core.TEST_FOLDER)
    logger.info('Data loaded successfully for both train and test')

    # convert the data to tf dataset processable by the model
    train_ds = dp.image_resizing_and_dataset_creation(
        data= train_data,
        c_mode= 'categorical',
        shufle=True,
        ylabelname= 'label'
    )
    test_ds = dp.image_resizing_and_dataset_creation(
        data= test_data,
        c_mode= 'categorical',
        shufle=False,
        ylabelname= 'label'
    )


    model = m.make_model(
        input_size= config.modelConfig.img_size,
        learning_rate= config.modelConfig.learning_rate,
        size_inner= config.modelConfig.dense_layer_first_inner_size,
        droprate= config.modelConfig.drop_rate
    )

    model.fit(train_ds, 
              epochs=config.modelConfig.epoch, 
              validation_data=test_ds,
              callbacks=[checkpoint, early_stopping_cb])
    logger.info(f'Saving model to {core.TRAINED_MODEL_DIR}')
    
    # call the method - retain best model
    retain_best_model(core.TRAINED_MODEL_DIR)

if __name__ == '__main__':
    run_training(save_results=True)
