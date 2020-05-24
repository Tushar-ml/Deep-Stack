""" Using this File, we will be classifying Images using Predefined Models

and Scratch Models .

Author: Tushar Goel


Different Architectures:
    --> InceptionV3
    -->Xception
    --> VGG16
    --> VGG19
    --> Resnet50
    --> MobileNetV2

"""
from AutoDL import Deep_Stack
import cv2                          # Computer Vision Library
import  tensorflow as tf            # Powerful Framework for Deep Learning
import keras                        # A Deep Learning API 
import os                           # For Searching Folder within the system
from models import Models           # Script containing Different Models
from Preprocessing_Image import Preprocess_Image      #Preprocessing Image Script
 
class CNN(Deep_Stack):
    """
    This Class will have Following Properties:
        
    Attributes:
        --Training Directory
        -- Output Directory
        -- Image Folder Name
        
    Methods:
        --Create_Model
        --Train_Model
        --Predict_Model
        --Generate_Model
        --Visualize_Model
        --Deploy_Model
    """
    def __init__(self,working_directory,output_directory,Image_Folder_name,target_image_size,train=False):
        """
        In this function we will call Parent Function containing other Function
        
        and Define other variables.
        
        Arguments:
        ---------    
            working_directory --> Directory Containing Raw Data
            
            output_directory --> Output Sirectory to which Results will be posted
            
            Image_Folder_name --> Different Model Name for Different Models
            
            Train --> False Or True (For Prediction)
            
        Output:
        ------    
            None
        
        """
        Deep_Stack.__init__(self,working_directory,output_directory)
        self.epochs = 10                    #Initializing Epochs
        self.loss = 'sparse_categorical_crossentropy' 
        self.optimizer = 'adam'
        self.Image_Folder_name = Image_Folder_name
        self.train = train
        self.target_image_size = target_image_size
        
    """
    Defining Preprocess Function to Preprocess the Images with Different Flow Method
    
    """
    def Image_Preprocessing(self,model_name,num_classes,batch_size,method):
        """
        This function Will do image processing and return training Data Generator, Validation Data Generator
        
        and Test Data Generator on the Basis of Training Argument whether it is True Or False.
        
        Arguments:
            model_name --> Name for The Predefined Architecture
            num_classes --> Number of Classes
            batch_size --> Batch Size
            method --> Method by which Images will flow in the Function
            
        Outputs:
            It will Return the Data Generator for Train and Test
        
        """
        self.model_name = model_name
        self.num_classes = num_classes
        self.batch_size = batch_size
        self.method = method
        
        #Defining Variables for Preprocessing
        preprocessing = Preprocess_Image(self.model_name,self.num_classes,self.batch_size,self.target_image_size,self.train)
        
        if self.method == 'directory':
            
    
    
            
            
            
            
            
        
        
        
    
        
        

