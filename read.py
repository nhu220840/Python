import tempfile

file_path = 'test.txt'

with open(file_path, 'r+') as f:
    print(f.read(19))
    # print(f.seek(0))
    # print(f.read())
    # print(f.readline())
    print(f.readlines())
    # f.write('Hello, World!\n')
