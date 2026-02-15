import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    
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
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        elif os.path.isfile(target_file) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
            
        elif file_path.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file'
            
        
        command = ["python", target_file]
        
        if args:
            command.extend(args)
        
        
        completed_process = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # print("subprocess output")
        # print(completed_process)
        
        # print("subprocess individual outputs")
        # print(completed_process.returncode)
        # print(completed_process.stdout)
        # print(completed_process.stderr)
        
        returnString = ""
        
        
        if completed_process.returncode != 0:
            returnString += f'Process exited with code {completed_process.returncode}\n'
            
        if completed_process.stdout is None:
            returnString += "No output produced\n"
        
        if completed_process.stderr is None:
            returnString += "No output produced\n"
            
        
        returnString += f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}'
            
        return returnString
        
        
        
        
        
    # Something went wrong that we didn't account for
    except Exception as e:
        return f'Error: executing Python file: {e}'