"""

@author: Ninad Mohite
"""
import tensorflow as tf
import pandas as pd
import random
import os
import shutil
from keras.preprocessing.image import ImageDataGenerator
from os import listdir
from os.path import isfile, join
from keras.preprocessing.image import ImageDataGenerator

file_names = []
dict_names = {}

# Make a list of all the labels

keys = ['air_conditioner','car_horn','children_playing','dog_bark','drilling','engine_idling','gun_shot','jackhammer','siren','street_music']

# Take file names from each folder named with labels and put it in a dictionary
# Where key is labels and value is list of files belonging to that label

for i in keys:
    name = i
    name = [f for f in listdir('/Volumes/Samsung_T5/UrbanSound8K/spectrograms3c/'+i) if isfile(join('/Volumes/Samsung_T5/UrbanSound8K/spectrograms3c/'+i, f))]

    dict_names[i] = name

# Create a list with file names

for each in keys:
    for file in dict_names[each]:
        file_names.append(file)

#print(len(file_names))

# Split data into training and testing
file_names.sort()
random.seed(230)
random.shuffle(file_names)

split_1 = int(0.8 * len(file_names))


train_file = file_names[:split_1]
test_file = file_names[split_1:]
print(len(train_file), len(test_file))


# Create train and test directories and labels as sub directories in each directory
# Copy all files into respective directories

def create_data(type,file):
    count = 0
    for k in keys:


        n = 0
        while n < len(file):

            if file[n] in dict_names[k]:
                if not os.path.exists('/Volumes/Samsung_T5/'+type+'/'+k):
                    os.mkdir('/Volumes/Samsung_T5/'+type+'/'+k)
                dest = shutil.copy('/Volumes/Samsung_T5/UrbanSound8K/spectrograms3c/'+k+'/'+file[n],'/Volumes/Samsung_T5/'+type+'/'+k)
                #print(dest)
                count+=1
            n+=1
    return count

print("Successfully copied"+" "+str(create_data("test",test_file))+" "+"test images")
print("Successfully copied"+" "+str(create_data("train",train_file))+" "+"training images")

