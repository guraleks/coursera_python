class FileReader:

    def __init__(self, path, content=''):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                self.content = str(f.read())
        except IOError:
            return ''
        return self.content

# if __name__ == '__main__':
#     reader = FileReader('example.txt')
#     print(reader.read())