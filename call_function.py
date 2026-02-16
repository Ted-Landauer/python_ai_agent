from google import genai
from google.genai import types

from config import WORKING_DIR
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_files import write_file, schema_write_files

# List of functions that the agent has access to
available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_files]
)


# A map of the specific functions and the actual calls to them
function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
}


# The function to call all functions
def call_function(function_call, verbose=False):
    
    # Check if we need to print out extra info
    if verbose is True:
        print(f'Calling function: {function_call.name}({function_call.args})')
        
    else:
        print(f' - Calling function: {function_call.name}')
        
        
    # Ensure that the function_name is a string
    function_name = function_call.name or ""
    
    
    # Check that the function_name being passed is a function that the agent would know about and return the name of the unknown function if it isn't
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )        
        
    # Create a dictionary for all the arguments in the function call or set it to an empty dictionary
    args = dict(function_call.args) if function_call.args else {}
    
    # Set our working directory path
    args["working_directory"] = WORKING_DIR
    
    # Call the requested function
    function_result = function_map[function_name](**args)
    
    # Return the results of the function calls
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            
            )
        
        ],
    
    )
    
    