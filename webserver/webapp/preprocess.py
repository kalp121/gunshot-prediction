import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import librosa

class process():
	def create_image(name):

		y,sr=librosa.load("static/audio/"+name)
		mfccs = librosa.feature.mfcc(y, sr, n_mfcc=40)
		melspectrogram =librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000)
		chroma_stft=librosa.feature.chroma_stft(y=y, sr=sr,n_chroma=40)
		chroma_cq =librosa.feature.chroma_cqt(y=y, sr=sr,n_chroma=40)
		chroma_cens =librosa.feature.chroma_cens(y=y, sr=sr,n_chroma=40)
		spec_centroid=librosa.feature.spectral_centroid(y=y,sr=sr)
		melspectrogram.shape,chroma_stft.shape,chroma_cq.shape,chroma_cens.shape,mfccs.shape

		#mfcc
		plt.figure(figsize=(10,4))
		librosa.display.specshow(mfccs, x_axis='time')
		plt.colorbar()
		plt.title('MFCC')
		plt.tight_layout()
		plt.savefig("static/images/mfcc_"+name+".png")

		#Melspectrogram 
		plt.figure(figsize=(10,4))
		librosa.display.specshow(librosa.power_to_db(melspectrogram,ref=np.max),y_axis='mel', fmax=8000,x_axis='time')
		plt.colorbar(format='%+2.0f dB')
		plt.title('Mel spectrogram')
		plt.tight_layout()
		plt.savefig("static/images/spec_"+name+".png")

		#Chromagram
		plt.figure(figsize=(10,4))
		librosa.display.specshow(chroma_stft, y_axis='chroma', x_axis='time')
		plt.colorbar()
		plt.title('Chromagram')
		plt.tight_layout()
		plt.savefig("static/images/chroma_"+name+".png")

		#Chroma cqt of a dog bark
		plt.figure(figsize=(10,4))
		librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')
		plt.colorbar()
		plt.title('chroma_cqt')
		plt.tight_layout()
		plt.savefig("static/images/chroma_cq_"+name+".png")

		#Chroma cens of a dog bark
		plt.figure(figsize=(10,4))
		librosa.display.specshow(chroma_cens, y_axis='chroma', x_axis='time')
		plt.colorbar()
		plt.title('chroma_cens')
		plt.tight_layout()
		plt.savefig("static/images/chroma_cens_"+name+".png")

		return True
