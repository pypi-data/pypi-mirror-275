# processor-class
from __future__ import print_function, division

import sys
import os
head, tail = os.path.split(os.path.join(os.path.abspath(__file__)))

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import copy

import argparse
import cv2
import json

from PIL import Image
import torch.nn.functional as F


class Processor(object):
    def __init__(self):
        super(Processor, self).__init__()

        from _global_paths import __path_dict__
        self.__path_dict__ = __path_dict__

        ''' Paths '''
        self.CASE_PATH = None # The path to the case folder
        
        # DL-RELEVANT
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        self.dl_CLASSIFIER_HEMORRHAGE_CHECKPOINT_FILE =  os.path.join(__path_dict__['models'],'hemorrhage.pth')

        self.dl_DATATRANSFORMS_ICH = None
        self.dl_CLASSIFIER_ICH_MODEL = None
        
    def init_classifier_ich(self):  
        # Data augmentation and normalization for training
        # Just normalization for validation
        self.dl_DATATRANSFORMS_ICH = {
            'train': transforms.Compose([
                #transforms.RandomResizedCrop(224),
                #transforms.Resize((800,600)),
                transforms.Resize((256,256)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
            'val': transforms.Compose([
                # transforms.Resize((800,600)),
                transforms.Resize((256,256)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
        }
        
        self.dl_CLASSIFIER_ICH_MODEL = models.resnet18(weights=None)      
        
        num_ftrs = self.dl_CLASSIFIER_ICH_MODEL.fc.in_features
        # Here the size of each output sample is set to 2.
        # Alternatively, it can be generalized to nn.Linear(num_ftrs, len(class_names)).
        self.dl_CLASSIFIER_ICH_MODEL.fc = nn.Linear(num_ftrs, 2)
        self.dl_CLASSIFIER_ICH_MODEL = self.dl_CLASSIFIER_ICH_MODEL.to(self.device)
        try: self.dl_CLASSIFIER_ICH_MODEL.load_state_dict(torch.load(str(self.dl_CLASSIFIER_HEMORRHAGE_CHECKPOINT_FILE)))
        except RuntimeError: self.dl_CLASSIFIER_ICH_MODEL.load_state_dict(torch.load(str(self.dl_CLASSIFIER_HEMORRHAGE_CHECKPOINT_FILE), map_location=torch.device('cpu')))


    def inference_classifier_hemorrhage(self, input_image, *_):
        was_training = self.dl_CLASSIFIER_ICH_MODEL.training
        self.dl_CLASSIFIER_ICH_MODEL.eval()
        with torch.no_grad():
            input_image_trans = self.dl_DATATRANSFORMS_ICH['val'](input_image)
            input_image_device = input_image_trans.to(self.device)
            input_ready = torch.unsqueeze(input_image_device,0)
            output = self.dl_CLASSIFIER_ICH_MODEL(input_ready)
            _, preds = torch.max(output, 1)
        self.dl_CLASSIFIER_ICH_MODEL.train(mode=was_training)
        return output
