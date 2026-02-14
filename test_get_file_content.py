from functions.get_file_content import get_file_content 

def main():
    
    result = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(result)}")
    print(f"End of content: ...{result[-100:]}")
    
    result1 = get_file_content("calculator", "main.py")
    print(result1)
    
    result2 = get_file_content("calculator", "pkg/calculator.py")
    print(result2)
    
    result3 = get_file_content("calculator", "/bin/cat")
    print(result3)
    
    result4 = get_file_content("calculator", "pkg/does_not_really_exist.py")
    print(result4)
    
main()