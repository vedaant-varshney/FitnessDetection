import torch
from torch import nn
import os
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms
import os

if __name__ == "__main__":

    print(os.getcwd())
    model = torch.hub.load('pytorch/vision:v0.6.0', 'deeplabv3_resnet101', pretrained=True)
    model.eval()

    os.chdir('/Users/udiram/Documents/GitHub/FitnessDetection')
    os.getcwd()

    curDir = os.getcwd()

    processed_sets_path = os.path.join(curDir, 'images', "ProcessedSets")
    new_extracted_path = os.path.join(curDir, 'images', 'BackgroundExtractedSets')
    image_list = os.listdir(processed_sets_path)

    for image in image_list:
        img_filename = os.path.join(processed_sets_path, image)

        input_image = Image.open(img_filename)
        preprocess = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

        # move the input and model to GPU for speed if available
        if torch.cuda.is_available():
            # print('Cuda is available')
            input_batch = input_batch.to('cuda')
            model.to('cuda')

        with torch.no_grad():
            output = model(input_batch)['out'][0]
        output_predictions = output.argmax(0)

        palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
        colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
        colors = (colors % 255).numpy().astype("uint8")

        # plot the semantic segmentation predictions of 21 classes in each color
        r = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(input_image.size)
        r.putpalette(colors)

        r = r.save(os.path.join(new_extracted_path, image))