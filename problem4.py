# Import the os module
import os

# Specify the directory path
path = "."

# Get the list of files and folders in the directory
contents = os.listdir(path)

# Print the contents of the directory
for item in contents:
    print(item)