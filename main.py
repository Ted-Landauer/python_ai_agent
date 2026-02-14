import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")



def main():
    
    # Parser Setup
    parser = argparse.ArgumentParser(description="Python AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # Parser Debug Statements
    #print("this is args: " + str(args.user_prompt))
    #print("this is args verbose check: " + str(args.verbose))
    
    # Setup for back and forth conversations with the agent
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    
    # Check that we actually got the API key
    if api_key is None:
        raise RuntimeError("API Key was empty")
        
    # Set API key
    client = genai.Client(api_key=api_key)

    # Generate agent response
    response = client.models.generate_content(model='gemini-2.5-flash', contents=messages)
        
    # Check that nothing failed in getting the response
    if response.usage_metadata is None:
        raise RuntimeError("There was a failed API Request")
    
    # Check for the verbose flag and output additional info if TRUE
    if args.verbose is True:
        
        print("User prompt:" + args.user_prompt)
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
    
    # Print the agent's response
    print(response.text)



if __name__ == "__main__":
    main()
