import os

directory = 'data'

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)  # Get full file path
    if os.path.isfile(file_path):  # Check if it's a file (not a directory)
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:\n{content}")
