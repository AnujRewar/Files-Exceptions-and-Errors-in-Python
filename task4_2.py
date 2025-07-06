try:
    file1=open('output.txt','w')
    writing_file=file1.write("Hello, Python!\n")
    file1.close()

    file1=open('output.txt','a')
    amending_file=file1.write("Learning file handling in python")
    file1.close()

    file1=open('output.txt','r+')
    print("Final content of output.txt: ")
    reading_file=file1.read()
    print(reading_file)
    file1.close()

except FileNotFoundError:
    print("The file 'output.txt' was not found")