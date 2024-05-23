import os
import csv
import numpy as np
from typing import Tuple
import datetime

import keras
from tensorflow.keras.layers import (
    Conv2D,
    Conv2DTranspose,
    Dropout,
    Input,
    MaxPooling2D,
    concatenate,
)
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard

import wandb
from wandb.integration.keras import WandbMetricsLogger, WandbModelCheckpoint

from utils import f1, iou, setup_logger


def create_model(
    input_shape: Tuple[int] = (256, 256, 1),
    output_classes: int = 1,
    optimizer: str = "adam",
    loss: str = "binary_crossentropy",
    output_activation: str = "sigmoid",
    dropout_1: int = 0.1,
    dropout_2: int = 0.2,
    dropout_3: int = 0.3,
    summary: bool = False,
) -> keras.models.Model:
    """
    Create a U-Net model for semantic segmentation.

    Parameters:
        - input_shape (Tuple[int]): Input shape for the model. Default is (256, 256, 1)
        - output_classes (int): Number of output classes. Default is 1.
        - optimizer (str/optimizer): Name of the optimizer to use or a custom optimizer. Default is 'adam'.
        - loss (str/loss function): Loss function to use during training. Default is 'binary_crossentropy'.
        - output_activation (str): Activation function for the output layer. Default is 'sigmoid'.
        - dropout_1 (float): Dropout rate for the first set of layers. Default is 0.1.
        - dropout_2 (float): Dropout rate for the second set of layers. Default is 0.2.
        - dropout_3 (float): Dropout rate for the third set of layers. Default is 0.3.
        - summary (bool): Whether to print the model summary. Default is False.

    Returns:
        - tensorflow.keras.models.Model: U-Net model for semantic segmentation.
    """
    # Define the logger
    logger = setup_logger()

    # Build the model
    inputs = Input(input_shape)
    s = inputs

    # Log input shape
    logger.debug(f"Input shape: {input_shape}")

    # Contraction path
    c1 = Conv2D(
        16, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(s)
    c1 = Dropout(dropout_1)(c1)
    c1 = Conv2D(
        16, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c1)
    p1 = MaxPooling2D((2, 2))(c1)

    c2 = Conv2D(
        32, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(p1)
    c2 = Dropout(dropout_1)(c2)
    c2 = Conv2D(
        32, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c2)
    p2 = MaxPooling2D((2, 2))(c2)

    c3 = Conv2D(
        64, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(p2)
    c3 = Dropout(dropout_2)(c3)
    c3 = Conv2D(
        64, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c3)
    p3 = MaxPooling2D((2, 2))(c3)

    c4 = Conv2D(
        128, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(p3)
    c4 = Dropout(dropout_2)(c4)
    c4 = Conv2D(
        128, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c4)
    p4 = MaxPooling2D(pool_size=(2, 2))(c4)

    c5 = Conv2D(
        256, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(p4)
    c5 = Dropout(dropout_3)(c5)
    c5 = Conv2D(
        256, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c5)

    # Expansive path
    u6 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding="same")(c5)
    u6 = concatenate([u6, c4])
    c6 = Conv2D(
        128, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(u6)
    c6 = Dropout(dropout_2)(c6)
    c6 = Conv2D(
        128, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c6)

    u7 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding="same")(c6)
    u7 = concatenate([u7, c3])
    c7 = Conv2D(
        64, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(u7)
    c7 = Dropout(dropout_2)(c7)
    c7 = Conv2D(
        64, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c7)

    u8 = Conv2DTranspose(32, (2, 2), strides=(2, 2), padding="same")(c7)
    u8 = concatenate([u8, c2])
    c8 = Conv2D(
        32, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(u8)
    c8 = Dropout(dropout_1)(c8)
    c8 = Conv2D(
        32, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c8)

    u9 = Conv2DTranspose(16, (2, 2), strides=(2, 2), padding="same")(c8)
    u9 = concatenate([u9, c1], axis=3)
    c9 = Conv2D(
        16, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(u9)
    c9 = Dropout(dropout_1)(c9)
    c9 = Conv2D(
        16, (3, 3), activation="relu", kernel_initializer="he_normal", padding="same"
    )(c9)

    outputs = Conv2D(output_classes, (1, 1), activation=output_activation)(c9)

    model = Model(inputs=[inputs], outputs=[outputs])

    # Compile the model
    model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy", f1, iou])

    # Show model summary
    if summary:
        logger.info(model.summary())

    return model


def load_pretrained_model(model_name: str) -> keras.models.Model:
    """
    Load a saved and pre-trained U-Net model from the specified directory.

    Parameters:
        - model_name (str): The name of the model file to load.

    Returns:
        - tensorflow.keras.models.Model: The loaded U-Net model.

    Raises:
        - FileNotFoundError: If the model file does not exist at the specified path.

    Notes:
        - The model file needs to be in the './models' directory.
    """

    # Define the logger
    logger = setup_logger()

    # Construct the model path
    model_path = os.path.join("models/", model_name + ".keras")

    # Check if the model file exists
    if not os.path.exists(model_path):
        logger.error(f"No model found at {model_path} with the name: {model_name}")
        raise FileNotFoundError(
            f"No model found at {model_path} with the name: {model_name}"
        )

    # Load the model
    model = load_model(model_path, custom_objects={"f1": f1, "iou": iou})

    # Log the model being loaded succesfully
    logger.info(f"Model loaded successfully from {model_path}")

    return model


def train_model(
    #model: keras.models.Model,
    model_name: str,
    train_generator,
    test_generator,
    steps_per_epoch: int,
    validation_steps: int,
    input_shape: Tuple[int] = (256, 256, 1),
    epochs: int = 20,
    model_suffix: str = "",
    summary: bool = False,
) -> None:
    """
    Trains and saves a convolutional neural network model using the specified architecture.

    Parameters:
        - model (keras.models.Model, optional):
        - model_name (str): Type of the neural network architecture to use.
        - train_generator: Training data generator.
        - test_generator: Testing data generator.
        - input_shape (int): Input shape used for the model.
        - steps_per_epoch (int): Number of steps to be taken per epoch.
        - validation_steps (int): Number of steps to be taken for validation.
        - epochs (int, optional): Number of training epochs (default is 20).
        - model_suffix (str, optional): Suffix to append to the model filename (default is '').
        - summary (bool, optional): Flag indicating whether to print the model summary (default is False).

    Returns:
        None

    Notes:
        - The function initializes a neural network model based on the specified architecture.
        - Training is performed using the provided data generators and hyperparameters.
        - Early stopping and model checkpoint callbacks are applied during training.
        - The best model is saved to a file with the specified suffix.
    """
    logger = setup_logger()
    # Check model availability, if not, create new one
    try:
        model = load_pretrained_model(model_name)
        logger.info(f"{model_name} loaded")
    except:
        model = create_model(input_shape)
        logger.info(f"{model_name} created")

    Now = datetime.datetime.now()
    time = Now.strftime("%Y%m%d-%H%M")

    # Start a run, tracking hyperparameters
    wandb.init(
        # Set the wandb project where this run will be logged
        project=model_name,
        # entity="220817",  # Maybe change
        # Track hyperparameters and run metadata with wandb.config
        sync_tensorboard=True,
        config={
            "metric": ["accuracy", f1, iou],
            "epoch": epochs,
            "steps_per_epoch": steps_per_epoch,
        },
    )

    tb = TensorBoard(log_dir="./logs/tensorboard/" + time, histogram_freq=1)
    logger.info(
        f'Tensorboard of {model_name} at location {"./logs/tensorboard/" + time}'
    )
    cb = EarlyStopping(
        monitor="val_loss", patience=5, restore_best_weights="True", mode="min"
    )

    save_model = ModelCheckpoint(
        # f"models/{model_name}{model_suffix}{epochs:02d}.h5",
        f"models/{model_name}.keras",
        save_best_only=True,
        monitor="val_loss",
        mode="min",
        #summary=summary,
    )
    wbml = WandbMetricsLogger(log_freq="epoch"),
    #wbmc = WandbModelCheckpoint(filepath = f"./models/wandb/{model_name}", save_best_only=True),

    history = model.fit(
        train_generator,
        steps_per_epoch=steps_per_epoch,
        epochs=epochs,
        validation_data=test_generator,
        validation_steps=validation_steps,
        callbacks=[
            cb,
            tb,
            save_model,
            wbml,
            #wbmc
        ],
    )
    wandb.finish()
    os.makedirs("./models/", exist_ok=True)
    model.save("./models/" + time + '.keras')
    logger.info(f'{model_name} saved at location {"./models/" + time}')
    logger.info(f"train_model - history - {history}")

    # Extracting patch_size and color_channels from input_shape
    patch_size = input_shape[0]
    color_channels = input_shape[2]
    best_val_loss = np.min(history.history["val_loss"])

    # Storing information in a CSV file
    os.makedirs(r"./log/", exist_ok=True)
    csv_file = "./log/model_info.csv"
    with open(csv_file, mode="a") as file:
        writer = csv.writer(file)
        writer.writerow(["Model_name", "patch_size", "color_channels", "val_loss"])
        writer.writerow([model_name, patch_size, color_channels, best_val_loss])
