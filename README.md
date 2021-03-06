# FitnessDetection

### A project which aims to use computer vision and neural networks to give feedback on people's exercise routines. 

### Using `semi_automatic_multiple_sets.py` (found in main_projects/vedaant`)
This file will allow you to easily process large amounts of exercise data into squares of focus. The input will be composed of sets of folders of freeze-frames from an exercise routine that capture the complete range of motion. The sets must be named as per the convention "Set1", "Set2", "Set3" and so on. The images are ideally named "1.png", 2.png", and so on. The output will be a processed folder containing the squares of each image. The size will vary between sets, but this will be processed later. 

#### Step by Step Process
* Place all the sets in the images folder, ideally the ones assigned to you. All images should be named by convention
* Double-check to see if the current working directory is the root project directory. If not change it to that. (Check with `os.getcwd()`)
* The process should begin with an image close to the full range of motion in the exercise. Drag while left clicking to create a bounding box around the full person. Ensure that you start from the top left point.
* Press the E key on your keyboard if satisfied. If there are no errors, press F to continue to the next set. If you draw a box incorrectly, press R to restart
* Ensure all the processed files are in the proper folders

A sample input image:
![Input Sample](/images/Set1/1.png)


Sample Output: Image
![Output Sample](/images/Set1/Processed/1.png)

