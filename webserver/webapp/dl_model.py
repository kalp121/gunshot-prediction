from keras.models import load_model
import pandas as pd
import numpy as np
import librosa
import matplotlib.pyplot as plt

class audioModel():
	model=load_model('dl_models/model.h5')
	path="static/audio/"
	def audio_model(self,filename):
		test_data=[]
		y,sr=librosa.load(self.path+filename)
		mfccs = np.mean(librosa.feature.mfcc(y, sr, n_mfcc=40).T,axis=0)
		test_data.append(mfccs)
		test_data=np.array(test_data)
		test_data=np.reshape(test_data,(1, 40,1))
		test_data=np.reshape(test_data,(1, 40,1,1))
		return self.model.predict(test_data)

	def plot_graph(self,filename):

		y,sr=librosa.load(self.path+filename)
		mfccs = librosa.feature.mfcc(y, sr, n_mfcc=40)
		melspectrogram =librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000)
		chroma_stft=librosa.feature.chroma_stft(y=y, sr=sr,n_chroma=40)
		chroma_cq =librosa.feature.chroma_cqt(y=y, sr=sr,n_chroma=40)
		chroma_cens =librosa.feature.chroma_cens(y=y, sr=sr,n_chroma=40)
		spec_centroid=librosa.feature.spectral_centroid(y=y,sr=sr)
		melspectrogram.shape,chroma_stft.shape,chroma_cq.shape,chroma_cens.shape,mfccs.shape
		rms=librosa.feature.rms(y=y)


		#mfcc
		plt.figure(figsize=(10,4))
		librosa.display.specshow(mfccs, x_axis='time')
		plt.colorbar()
		plt.title('MFCC')
		plt.tight_layout()
		plt.savefig("mfcc.png")

		#Melspectrogram
		plt.figure(figsize=(10,4))
		librosa.display.specshow(librosa.power_to_db(melspectrogram,ref=np.max),y_axis='mel', fmax=8000,x_axis='time')
		plt.colorbar(format='%+2.0f dB')
		plt.title('Mel spectrogram')
		plt.tight_layout()
		plt.savefig("mel.png")


		#Chromagram of dog bark
		plt.figure(figsize=(10,4))
		librosa.display.specshow(chroma_stft, y_axis='chroma', x_axis='time')
		plt.colorbar()
		plt.title('Chromagram')
		plt.tight_layout()
		plt.savefig("chroma.png")

		#Chroma cqt of a dog bark
		plt.figure(figsize=(10,4))
		librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')
		plt.colorbar()
		plt.title('chroma_cqt')
		plt.tight_layout()
		plt.savefig("chromacqt.png")


		#spec_centroid
		S, phase = librosa.magphase(librosa.stft(y=y))
		plt.figure()
		plt.subplot(2, 1, 1)
		plt.semilogy(spec_centroid.T, label='Spectral centroid')
		plt.ylabel('Hz')
		plt.xticks([])
		plt.xlim([0, spec_centroid.shape[-1]])
		plt.legend()
		plt.subplot(2, 1, 2)
		librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),y_axis='log', x_axis='time')
		plt.title('log Power spectrogram')
		plt.tight_layout()
		plt.savefig('spec_centroid.png')

		#loudness
		S = librosa.magphase(librosa.stft(y, window=np.ones, center=False))[0]
		rms_1 = librosa.feature.rms(S=S)

		plt.figure()
		plt.subplot(2, 1, 1)
		plt.semilogy(rms.T, label='RMS Energy')
		plt.xticks([])
		plt.xlim([0, rms.shape[-1]])
		plt.legend()
		plt.subplot(2, 1, 2)
		librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),y_axis='log', x_axis='time')
		plt.title('log Power spectrogram')
		plt.tight_layout()
		plt.savefig('loudness.png')
		
