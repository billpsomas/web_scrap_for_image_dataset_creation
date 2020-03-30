# Create-Image-Dataset

## Description
This repository contains a naive but useful script for creating Image Datasets using the Yandex Images Search Engine. It can be useful for creating datasets for various Computer Vision tasks, such as image classification, object detection, instance or semantic segmentation etc.

## Required Libraries
In order to download the required libraries, use:

<b> pip3 install requirements.txt </b>

## How it works
In order to create your dataset, you first have to specify the classes about which you are interested in. Those are the classes for which images will be downloaded automatically from the Yandex Images Search Engine. Write them down in the classes.txt file and then run the script using:

<b> python create_dataset.py </b>

What this script exactly does is that it searches Yandex Images for the class you have specified and it downloads all the images. Of course it's up to you if you want to specify a limit concerning the number of photos you want to download.
