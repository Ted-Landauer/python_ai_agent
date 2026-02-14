import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

# if api_key is None:
    # raise RuntimeError("API Key was empty")

# client = genai.Client(api_key=api_key)


# response = client.models.generate_content(
    # model='gemini-2.5-flash',
    # contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    # )
    
# print(response.text)


def main():
    #print("Hello from python-ai-agent!")
    
    
    parser = argparse.ArgumentParser(description="Python AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    #print("this is args: " + str(args.user_prompt))
    
    
    if api_key is None:
        raise RuntimeError("API Key was empty")

    client = genai.Client(api_key=api_key)


    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=args.user_prompt
        )
        
        #contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        
    if response.usage_metadata is None:
        raise RuntimeError("There was a failed API Request")
        
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
        
    print(response.text)


if __name__ == "__main__":
    main()
