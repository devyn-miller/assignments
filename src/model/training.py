from config import EPOCHS, BATCH_SIZE, DATA_AUGMENTATION
from src.data_preprocessing.transformations import create_augmentation_pipeline

datagen = create_augmentation_pipeline()
def train_model(model, x_train, y_train, x_test, y_test):
    '''Trains the model.'''
    if not DATA_AUGMENTATION:
        print("Not using data augmentation.")
        history = model.fit(
            x_train,
            y_train,
            batch_size=BATCH_SIZE,
            epochs=EPOCHS,
            validation_data=(x_test, y_test),
            shuffle=True,
        )
    else:
        datagen.fit(x_train)
        # Fit the model on the batches generated by datagen.flow()
        history = model.fit(
            datagen.flow(x_train, y_train, batch_size=BATCH_SIZE),
            epochs=EPOCHS,
            validation_data=(x_test, y_test),
            workers=4,
        )

    return history
