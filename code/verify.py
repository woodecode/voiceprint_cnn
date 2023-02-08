import tensorflow as tf
import numpy as np
import create_data
import voicecnn

if __name__ == '__main__':
    
    wav_file_path = ''

    # wav_file_path = "../audio/aaa/test_data/20170001P00001A0104.wav"
    # [[9.8473573e-01 4.9263886e-03 1.7453948e-04 1.0163375e-02]] -> 1000
    # wav_file_path = "../audio/bbb/test_data/20170001P00001I0108.wav"
    # [[2.0210398e-04 4.1069593e-03 1.4127867e-05 9.9567682e-01]] -> 0001
    # wav_file_path = "../audio/ccc/test_data/20170001P00283A0104.wav"
    # [[1.2693404e-09 5.8338312e-10 9.9991369e-01 8.6336484e-05]] -> 0010
    # wav_file_path = "../audio\ddd/test_data/20170001P00283I0102.wav"
    # [[1.6550887e-02 9.8104918e-01 8.9117008e-10 2.3999047e-03]] -> 0100

    # extract mfcc of this wav audio
    mfcc_data = create_data.mfcc_generator(wav_file=wav_file_path)
    mfcc_data = np.expand_dims(mfcc_data, axis=-1)
    mfcc_data = np.expand_dims(mfcc_data, axis=0)
    print('shape:', np.shape(mfcc_data))
    # load model
    model = tf.keras.models.load_model('../model/model_20230209_0138.h5')
    # model = voivecnn.VoiceVerificationCNN(input_shape=(32,171,1),output_shape=4)
    # model.load_weights('../model/model_20230209_0138.h5')

    print (model.predict(mfcc_data))



    