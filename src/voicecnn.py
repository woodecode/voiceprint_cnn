import tensorflow as tf


def create_model(input_shape, output_shape):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=input_shape))
    model.add(tf.keras.layers.Conv2D(name='Conv_0',filters=8,kernel_size=(2,3),activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(name='MaxPool_0'))
    model.add(tf.keras.layers.Conv2D(name='Conv_1',filters=32,kernel_size=(2,3),activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(name='MaxPool_1'))
    model.add(tf.keras.layers.Conv2D(name='Conv_2',filters=64,kernel_size=(2,3),activation='relu'))
    model.add(tf.keras.layers.MaxPool2D(name='MaxPool_2'))
    model.add(tf.keras.layers.Flatten(name='Flatten'))
    model.add(tf.keras.layers.Dense(units=32,name='Dense'))
    model.add(tf.keras.layers.Dense(units=output_shape,name='Output',activation='softmax'))
    return model


class VoiceVerificationCNN(tf.keras.Sequential):
    def __init__(self, input_shape, output_shape) -> None:
        super(VoiceVerificationCNN, self).__init__()
        # model structure
        self.add(tf.keras.layers.InputLayer(input_shape=input_shape))
        self.add(tf.keras.layers.Conv2D(name='Conv_0',filters=8,kernel_size=(2,3),activation='relu'))
        self.add(tf.keras.layers.MaxPool2D(name='MaxPool_0'))
        self.add(tf.keras.layers.Conv2D(name='Conv_1',filters=32,kernel_size=(2,3),activation='relu'))
        self.add(tf.keras.layers.MaxPool2D(name='MaxPool_1'))
        self.add(tf.keras.layers.Conv2D(name='Conv_2',filters=64,kernel_size=(2,3),activation='relu'))
        self.add(tf.keras.layers.MaxPool2D(name='MaxPool_2'))
        self.add(tf.keras.layers.Flatten(name='Flatten'))
        self.add(tf.keras.layers.Dense(units=32,name='Dense'))
        self.add(tf.keras.layers.Dense(units=output_shape,name='Output',activation='softmax'))


if __name__ == '__main__':
    # GPU support
    print(tf.config.list_physical_devices('GPU'))
    # create model
    model = VoiceVerificationCNN((26, 167, 1), 5)
    # save model
    model.save_weights('../model/model_test.h5')
    
    model.summary()
    