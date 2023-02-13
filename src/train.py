import numpy as np
import tensorflow as tf
import voicecnn

if __name__ == '__main__':
    # test whether this environment support GPU training
    print(tf.config.list_physical_devices('GPU'))
    # create model
    model = voicecnn.VoiceVerificationCNN((32, 22, 1), 4)

    dataset_file_path = 'dataset.npy'
    labels_file_path = 'labels.npy'

    # load dataset
    dataset = np.load(dataset_file_path,allow_pickle=True)
    dataset = tf.convert_to_tensor(dataset)
    print('dataset ', np.shape(dataset))

    # load labels and convert into one-hot encoded labels
    labels = np.load(labels_file_path,allow_pickle=True)
    # Convert the string labels into integer labels
    unique_labels = list(set(labels))
    label_to_int = {label: i for i, label in enumerate(unique_labels)}
    int_labels = [label_to_int[label] for label in labels]
    # Convert the integer labels into one-hot encoded labels
    one_hot_labels = tf.keras.utils.to_categorical(int_labels, len(unique_labels))
    print('labels ', np.shape(one_hot_labels))
    # np.set_printoptions(threshold=np.inf)
    print(one_hot_labels)

    model.compile(optimizer=tf.optimizers.SGD(learning_rate=0.003),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(x=dataset,y=one_hot_labels,epochs=500, batch_size=20)

    # save the model
    # model.save_weights('../model/model_20230209_0121.h5')
    tf.keras.models.save_model(model=model, filepath='../model/model_20230209_1533.h5')
