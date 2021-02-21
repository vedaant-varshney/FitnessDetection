# Use it for directory operations, making/moving/changing/deleting directories
import os

# Gets current working directory
curDir = os.getcwd()

# Makes a directory
os.mkdir("NonComputerVisionFiles")

# Renames a directory
os.rename("NonComputerVisionFiles", "NonCV_Files")

# Remove a directory
os.rmdir("dirName")


