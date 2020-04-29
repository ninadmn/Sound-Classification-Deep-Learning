"""

@author: Ninad Mohite
"""

import csv
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from PIL import Image

import time

# Read metadata and create required directory to save image files

count = -1
with open('/Users/ninadmohite/Downloads/UrbanSound8K.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        count += 1

        if count == 0:
            continue

        print(count)
        if not os.path.exists('/Volumes/Samsung_T5/UrbanSound8K/spectrograms/' + row[7]):
            os.makedirs('/Volumes/Samsung_T5/UrbanSound8K/spectrograms/' + row[7])

        y, sr = librosa.load("/Volumes/Samsung_T5/UrbanSound8K/audio/fold" + str(row[5]) + "/" + str(row[0]))

        # Make and display a mel-scaled power (energy-squared) spectrogram

        S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
        # S1 = np.abs(librosa.stft(y))

        # Convert to log scale (dB). We'll use the peak power as reference.
        log_S = librosa.core.power_to_db(S, ref=np.max)

        # Make a new figure

        fig = plt.figure(figsize=(12, 4))
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)

        # Display the spectrogram on a mel scale
        # sample rate and hop length parameters are used to render the time axis
        librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

        # Make the figure layout compact

        # plt.show()

        # Save plot as .png file

        plt.savefig('/Volumes/Samsung_T5/UrbanSound8K/spectrograms/' + row[7] + '/' + row[0] + '.png')
        # convert 4 channel image to 3 channel image

        image = Image.open('/Volumes/Samsung_T5/UrbanSound8K/spectrograms/' + row[7] + '/' + row[0] + '.png').convert(
            "RGB")
        #new_image = image.resize((150, 150))

        image.save('/Volumes/Samsung_T5/UrbanSound8K/spectrograms3c/' + row[7] + '/' + row[0] + '.png')
        plt.close()

