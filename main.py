import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function



def main():
    
    # Parser Setup
    parser = argparse.ArgumentParser(description="Python AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # Parser Debug Statements
    #print("this is args: " + str(args.user_prompt))
    #print("this is args verbose check: " + str(args.verbose))
    
    # Load the .env and set the api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Check that we actually got the API key
    if api_key is None:
        raise RuntimeError("API Key was empty")
        
        
    # Set API key
    client = genai.Client(api_key=api_key)
    
    # Setup for back and forth conversations with the agent
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    # Check if we need to send extra info in the response
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    # Call the generate content function
    generate_content(client, messages, args.verbose)
    


# The call to the agent
def generate_content(client, messages, verbose):

    # Generate agent response
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages, 
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
            )
        )
        
    # Check that nothing failed in getting the response
    if response.usage_metadata is None:
        raise RuntimeError("There was a failed API Request")
    
    # Check for the verbose flag and output additional info if TRUE
    if verbose is True:
        
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    # Check if the function_calls property has any data
    if not response.function_calls:
        print("Response:")
        print(response.text)
        return
        
        
    # Create a list of function responses    
    function_responses = []
    
    # Loop over all the function responses
    for function_call in response.function_calls:
        
        # Get the call result
        function_call_result = call_function(function_call, verbose)
        
        
        # Check to see if the call results...
        ## has an overall empty parts list
        ## has an empty response
        ## has an empty response in the actual response data
        if function_call_result.parts is None:
            raise RuntimeError(f"Empty function response for {function_call.name}")
        
        elif function_call_result.parts[0].function_response is None:
            raise RuntimeError(f"Empty function response for {function_call.name}")
                
        elif function_call_result.parts[0].function_response.response is None:
            raise RuntimeError(f"Empty function response for {function_call.name}")
            
        # Check again for additional data printout requirement
        if verbose:
            print(f'-> {function_call_result.parts[0].function_response.response}')
            
        
        # Add all the responses to a list: Returning this value comes later
        function_responses.append(function_call_result.parts[0])
        
        
        #print(f"Calling function: {function_call.name}({function_call.args})")
        
    #else:
        
        # Print the agent's response
        #print(response.text)



if __name__ == "__main__":
    main()
