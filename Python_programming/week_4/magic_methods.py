import os
import tempfile

class File:

    def __init__(self, path):
        self.path = path
        self.current_position = 0

    def write(self, string):
        with open(self.path, 'w') as f:
            f.write(string)

    def read(self):
        with open(self.path, 'r') as f:
           return f.read()

    def __add__(self, other):
        new_file = File(os.path.join(tempfile.gettempdir(), 'new_file.txt'))
        with open(new_file.path, 'w+') as f:
            f.write(self.read())
            f.write(other.read())
        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)
            line = f.readline()
            if line:
                self.current_position = f.tell()
                return line
            else:
                self.current_position = 0
                raise StopIteration



if __name__ == '__main__':
    first_file = File('example.txt')
    second_file = File('second.txt')
    first_plus_second = first_file.__add__(second_file)

    with open('example.txt', 'r') as f:
        print(f.read())

    with open('second.txt', 'r') as f:
        print(f.read())

    # не понятно, почему не работает
    with open(first_plus_second.path, 'w+') as f:
        print(f.read())

