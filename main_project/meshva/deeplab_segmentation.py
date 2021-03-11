import torch
from PIL import Image
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import torchvision.transforms as T
import cv2 as cv

import time

#model = torchvision.models.segmentation.fcn_resnet101(pretrained=True).eval()
#torch.save(model, 'deeplab_entire')

model = torch.load('deeplab_entire')

image = Image.open('frames/yes/0.jpg')

def detect_obj(img):
    preprocess = T.Compose([T.ToTensor(),
                           T.Normalize(mean = [0.485, 0.456, 0.406], 
                                 std = [0.229, 0.224, 0.225])])
    input = preprocess(img).unsqueeze(0)
    
    output = model(input)['out'][0]
    output_predictions = output.argmax(0)

    col = np.zeros((output_predictions.shape[0], output_predictions.shape[1], 3))
    idx = output_predictions == 15
    col[idx] = (255, 255, 255)

    cv.imshow('new', col)

cap = cv.VideoCapture(0) # 5 frames / second
while True:
    ret, frame = cap.read()
    detect_obj(frame)
    print(end-start)
    cv.waitKey(10)
