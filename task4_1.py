#reading a file and handling the error if file is not present
try:
    with open("sample.txt",'r')as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("The file 'sample.txt' not found.")
