from functions.run_python import run_python_file


def main():
    #print(get_file_content("calculator", "lorem.txt"))
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    main()