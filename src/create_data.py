import os
import numpy as np
import librosa
import matplotlib.pyplot as plt
import sklearn


def audio_trim(wav_wave, length, threshold=10):
    # split an audio signal into non-silent intervals.
    non_silence_parts = librosa.effects.split(wav, top_db=threshold)
    output = np.concatenate([wav_wave[s:e] for s, e in non_silence_parts])
    output = output[1:length + 1]
    return output


def mfcc_generator(wav_file, sr=44100, wav_length=32768, wav_db_threshold=30):
    # load wav file
    wave, _ = librosa.load(path=wav_file, sr=sr)
    wav = audio_trim(wav_wave=wave, length=wav_length, threshold=wav_db_threshold)
    # extract mfcc geature
    mfcc = librosa.feature.mfcc(y=wav, sr=sr,
                                window='hamming',
                                win_length=512,
                                hop_length=384,
                                n_fft=2048,
                                n_mels=32,
                                n_mfcc=32)
    scaler = sklearn.preprocessing.MinMaxScaler()
    normalize_mfcc = scaler.fit_transform(mfcc)
    return np.square(normalize_mfcc)


if __name__ == '__main__':
    # raw audio file folder path
    audio_folder_path = '../audio/'
    # mfcc data and labels files path
    dataset_file_path = 'dataset.npy'
    label_file_path = 'labels.npy'

    # get all speakers
    speakers = os.listdir(audio_folder_path)
    print("\nspeakers:", speakers, "\nlen:", len(speakers))

    dataset = []
    labels = []

    scaler = sklearn.preprocessing.MinMaxScaler()

    for speaker in speakers:
        cnt = 0
        wav_files = os.listdir(audio_folder_path + speaker + '/train_data/')
        for wav_file in wav_files:
            # print(speaker, 'wav file: ', wav_file)
            if '.wav' in wav_file:
                # load wav file
                wav, sr = librosa.load(path=audio_folder_path + speaker + '/train_data/' + wav_file, sr=16000)
                # The actual speaking time is about 20s
                wav = audio_trim(wav=wav, length=8192, threshold=30)
                # extract mfcc geature
                mfcc = librosa.feature.mfcc(y=wav, sr=sr,
                                            window='hamming',
                                            win_length=512,
                                            hop_length=384,
                                            n_fft=2048,
                                            n_mels=32,
                                            n_mfcc=32)
                # normalize the 2d-array
                normalize_mfcc = scaler.fit_transform(mfcc)
                # add to dataset and labels lists
                dataset.append(np.square(normalize_mfcc))
                labels.append(speaker)
                
                cnt += 1
                print(speaker, cnt, np.shape(mfcc))

    np.save(dataset_file_path, np.array(dataset))
    np.save(label_file_path, np.array(labels))
