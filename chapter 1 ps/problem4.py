import os

# Function to list contents of a directory
def list_directory_contents(path):
    try:
        # Get list of files and directories in the specified path
        contents = os.listdir(path)
        return contents
    except FileNotFoundError:
        return "The specified directory does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

# Specify the directory you want to list (current directory in this case)
directory_path = '/New folder'

# Get directory contents
contents = list_directory_contents(directory_path)
print(contents)
