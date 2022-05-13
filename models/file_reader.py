import sys


class FileReader(object):
    def __init__(self, params):
        self.character = []
        if len(params) < 2:
            print('Please give correct arguments')
            sys.exit()
        self.__read_file(params[1])

    # Read the txt file and create a list from character
    def __read_file(self, filename=None):
        if filename is None:
            return
        try:
            with open(filename) as f:
                while True:
                    c = f.read(1)
                    if not c:
                        print(f'Read {len(self.character)} character Successfully')
                        break
                    if ord(c) == 10:
                        continue
                    self.character.append(str(c))
        except IOError as e:
            print(f'I/O error({e.errno}): {e.strerror}')
            raise
        except:
            print(f'Unexpected error:{sys.exc_info()[0]}')
            raise

    def get_characters(self):
        if len(self.character) == 0:
            return None
        return self.character

    def is_read(self):
        if len(self.character) == 0:
            return False
        return True


if __name__ == '__main__':
    file_reader = FileReader(sys.argv)
    print(file_reader.get_characters())
