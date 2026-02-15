from functions.run_python_file import run_python_file

def main():
    
    result = run_python_file("calculator", "main.py")
    print(result)
    
    result1 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result1)
    
    result2 = run_python_file("calculator", "tests.py")
    print(result2)
    
    result3 = run_python_file("calculator", "../main.py")
    print(result3)
    
    result4 = run_python_file("calculator", "nonexistent.py")
    print(result4)
    
    result5 = run_python_file("calculator", "lorem.txt")
    print(result5)
    
main()