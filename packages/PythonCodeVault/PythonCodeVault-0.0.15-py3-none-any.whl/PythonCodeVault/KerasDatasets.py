# https://medium.com/analytics-vidhya/write-your-own-custom-data-generator-for-tensorflow-keras-1252b64e41c3

import numpy as np
from keras.utils import Sequence

import os
import cv2
import random
import json

# TODO remove shuffle boolean
#       Übersicht nach dem alle bildee einglesen sind, Anzahl etc


class BinaryClassificationDataset(Sequence):
    """
    Creates Dataset for Training an Binary Classificatin Model in Keras.

    Parameters
    ----------
    base_dir: str
        Base directory containing the "fail_folder" and "pass_folder" directories

    fail_folder: str
        folder names of directories containing the data

    pass_folder: str
        folder names of directories containing the data

    augmentations: albumentations pipeline
    
    extension: str
        wanted file extension to be read in 

    tiff_layer: list
        of wanted tiff layers
    
    json_shape: tuple
        if extension == 'json': data has to be reshaped into this shape 
    
    dtype: numpy dtype
        dtype in which the array will be returned or given to the piplein

        
    Structure of given Base Folder should be like:

        Base
        │
        └─── Label0
        │    │   file01.txt
        │    │   ...
        │   
        └─── Label1
            │   file11.txt
            │   ...

    """

    def __init__(self, base_dir = './data', fail_folder = 'Fail', pass_folder = 'Pass', targets = [1,0], batch_size = 32, augmentations = None, extension = 'tiff', tiff_layer = [0], json_shape = (224,224,1), dtype = np.float32):
        self.fail_path = os.path.join(base_dir, fail_folder)
        self.pass_path = os.path.join(base_dir, pass_folder)
        
        self.extension = extension
        self.dtype = dtype

        self.fail_filepaths = [os.path.join(self.fail_path, filename) for filename in os.listdir(self.fail_path) if filename.endswith(self.extension)]    # Fail == 0
        self.pass_filepaths = [os.path.join(self.pass_path, filename) for filename in os.listdir(self.pass_path) if filename.endswith(self.extension)]    # Pass == 1

        self.json_shape = json_shape
        self.tiff_layer = tiff_layer

        self.read_images()

        self.fail_tuples = [(img, targets[0]) for img in self.fail_images]
        self.pass_tuples = [(img, targets[1]) for img in self.pass_images]

        self.data = self.fail_tuples + self.pass_tuples
        
        self.batch_size = batch_size
        self.augmentations = augmentations


    def __len__(self):
        return len(self.data) // self.batch_size

    def shuffle(self):
        random.shuffle(self.data)        

    def __getitem__(self, idx):
        data_tuples = self.data[idx * self.batch_size:(idx + 1) * self.batch_size]

        batch_x = [i[0] for i in data_tuples]
        batch_y = [i[1] for i in data_tuples]

        if self.augmentations: 
            return np.array([self.augmentations(image=x.astype(self.dtype))["image"] for x in batch_x]), np.array(batch_y).astype(self.dtype)
        else: 
            return np.array(batch_x).astype(self.dtype), np.array(batch_y).astype(self.dtype)
    
    def read_images(self):
        self.fail_images, self.pass_images = [], []
        
        if self.extension in ['json', '.json']:
            if not self.json_shape: raise Exception('Give wanted img shape (Height, Width (, Channels))')
            # Pass Images:
            for path in self.pass_filepaths:
                with open(path, 'r') as f:
                    data = json.load(f)
                img = np.array(data).reshape(self.json_shape)
                self.pass_images.append(img)
            # Fail Images:
            for path in self.fail_filepaths:
                with open(path, 'r') as f:
                    data = json.load(f)
                img = np.array(data).reshape(self.json_shape)
                self.fail_images.append(img)

        elif self.extension in ['tif', 'tiff', '.tif' '.tiff']:
            for path in self.fail_filepaths:
                imgs = cv2.imreadmulti(path)[1]
                for i in self.tiff_layer:
                    self.fail_images.append(imgs[i][:,:,0])           
            for path in self.pass_filepaths:
                imgs = cv2.imreadmulti(path)[1]
                for i in self.tiff_layer:
                    self.pass_images.append(imgs[i][:,:,0])



        else:
            self.fail_images = [cv2.imread(path, 0) for path in self.fail_filepaths]
            self.pass_images = [cv2.imread(path, 0) for path in self.pass_filepaths]


class BalancedBinaryClassificationDataset(Sequence):
    def __init__(self, base_dir = './data', fail_folder = 'Fail', pass_folder = 'Pass', 
                 targets = [1,0], batch_size = 32, augmentations = None, max_files = 100,
                 file_type = 'tiff', tiff_layers = None, json_shape = (1,17,363), dtype = np.float32):
        
        self.max_files = max_files
        self.batch_size = batch_size
        self.json_shape = json_shape
        self.targets = targets
        self.augmentations = augmentations
        self.dtype = dtype

        
        self.fail_dir = os.path.join(os.path.abspath(base_dir), fail_folder)
        self.pass_dir = os.path.join(os.path.abspath(base_dir), pass_folder)

        self.fail_paths = [os.path.join(self.fail_dir, filename) for filename in os.listdir(self.fail_dir) if filename.endswith(file_type)]
        self.pass_paths = [os.path.join(self.pass_dir, filename) for filename in os.listdir(self.pass_dir) if filename.endswith(file_type)]

        if file_type in ['.tiff', '.tif', 'tiff', 'tif']:
            self.fail_images, self.pass_images = self.read_images_tiff()
        elif file_type in ['.json', 'json']:
            self.fail_images, self.pass_images = self.read_images_json()
        else: raise Exception('Unknown file_type')

        self.batches = self.create_batches()
        
    def __len__(self):
        # return the number of batches
        return (self.max_files * 2) // self.batch_size

    def __getitem__(self, idx):
        batch = self.batches[idx]

        images, labels = [], []
        for image, label in batch:
            if self.augmentations:
                images.append(self.augmentations(image=image[0].astype(self.dtype))["image"])
            else: 
                images.append(image)

            labels.append(label)

        return np.array(images).astype(self.dtype), np.array(labels).astype(self.dtype)

    def on_epoch_end(self):
        self.batches = self.create_batches()

    def read_images_tiff(self):
        raise Exception('Not implemented yet')

    def read_images_json(self):
        channels, height, width = self.json_shape

        fail_images = []
        for path in self.fail_paths:
            with open(path, 'r') as f:
                data = np.array(json.load(f))
            fail_images.append(data.reshape((channels, height, width)))

        pass_images = []
        for path in self.pass_paths:
            with open(path, 'r') as f:
                data = np.array(json.load(f))
            pass_images.append(data.reshape((channels, height, width)))

        return fail_images, pass_images
    
    def create_batches(self):
        batches = []

        fail_idxs = np.random.choice(range(len(self.fail_paths)), self.max_files, replace=False)
        pass_idxs = np.random.choice(range(len(self.pass_paths)), self.max_files, replace=False)

        epoch_fail_images = [(self.fail_images[i], self.targets[0]) for i in fail_idxs]
        epoch_pass_images = [(self.pass_images[i], self.targets[1]) for i in pass_idxs]

        epoch_data = epoch_fail_images + epoch_pass_images
        random.shuffle(epoch_data)

        start, end = 0, self.batch_size
        for batch_idx in range(self.__len__()):
            batch_data = epoch_data[start : end]
            start += self.batch_size
            end += self.batch_size
            batches.append(batch_data)

        return batches

