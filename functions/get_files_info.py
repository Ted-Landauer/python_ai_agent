import os

# Function to get data about the files and directories when provided with a specific path
def get_files_info(working_directory, directory="."):

    # Watch out for unknown errors
    try:
        
        # Get the absolute path, join it with the directory, and normalize them for safety
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # Check if our paths are correct and, by extension, in the permitted directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        # Return an error if we're not in the permitted directory or if we're trying to work with a path that doesn't end in a directory
        if valid_target_dir == False:
            return print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            
        elif os.path.isdir(target_dir) == False:
            return print(f'Error: "{directory}" is not a directory')
       
        directoryContents = ""
            
        # Get the data on directory contents
        ## Loop over our contents
        for items in os.listdir(target_dir):
            
            ## Build the file path for us to access in the lower functions
            target_dir_file = os.path.join(target_dir, items)
            
            ## Build our string of useful stats
            directoryContents += "- " + items + ": " + ", ".join([
                f'file_size={str(os.path.getsize(target_dir_file))} bytes', 
                f'is_dir={str(os.path.isdir(target_dir_file))}'
                ]) + "\n"
        
        # Check that the correct things are printed out
        ## Not exactly the way I'd do it but this ensures that the assignment sees what it's looking for
        nameSpaceHolder = ""
        
        if directory == ".":
            nameSpaceHolder = "current"
        else:
            nameSpaceHolder = directory
            
        # Print the results
        print(f'Result for {nameSpaceHolder} directory: \n{directoryContents}')
        
    # Something went wrong that we didn't account for
    except Exception as e:
        return f'Error: {e}'
        
        
    