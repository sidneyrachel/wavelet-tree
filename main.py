import sys
from models.file_reader import FileReader
from models.wavelet_tree import WaveletTree


def main():
    file_reader = FileReader(sys.argv)

    if not file_reader.is_read():
        sys.exit()

    wavelet_tree = WaveletTree(file_reader.get_characters())
    print(wavelet_tree.max_elem(4, 8))


if __name__ == '__main__':
    main()
