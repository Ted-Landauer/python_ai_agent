import os

def write_file(working_directory, file_path, content):
    
    try:
        
        # Get the absolute path, join it with the directory, and normalize them for safety
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        #print(target_file)
        
        # Check if our paths are correct and, by extension, in the permitted directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        #valid_target_file = False
        
        # Return an error if we're not in the permitted directory or if we're trying to work with a file that doesn't exist or is not a regular file
        if valid_target_file == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        elif os.path.isdir(target_file) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
            
            
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        
        
        
        # Open a file, and write to it with the content value
        with open(target_file, "w") as file:
           file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    # Something went wrong that we didn't account for
    except Exception as e:
        return f'Error: {e}'