import os
from config import MAX_CHARS

# Function to get read the data of a specific file
def get_file_content(working_directory, file_path):


    # Watch out for unknown errors
    try:
        
        # Get the absolute path, join it with the directory, and normalize them for safety
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Check if our paths are correct and, by extension, in the permitted directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        #valid_target_file = False
        
        # Return an error if we're not in the permitted directory or if we're trying to work with a file that doesn't exist or is not a regular file
        if valid_target_file == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        elif os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        
        # Open a file, read it out of the MAX_CHARS value (10000 at default), and check if we've truncated things
        fileContents = ""
        trunTest = False
        
        with open(target_file, "r") as file:
            fileContents = file.read(MAX_CHARS)
            
            if file.read(1):
                fileContents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                trunTest = True
        
        
        return fileContents
        
    # Something went wrong that we didn't account for
    except Exception as e:
        return f'Error: {e}'
        
        
    