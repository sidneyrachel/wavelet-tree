import sys
from models.file_reader import FileReader
from models.wavelet_tree import WaveletTree


def main():
    file_reader = FileReader(sys.argv)

    if not file_reader.is_read():
        sys.exit()

    wavelet_tree = WaveletTree(file_reader.get_characters())
    # wavelet_tree.print_tree(False)
    print('max_elem(5,8):', wavelet_tree.max_elem(5, 8))
    print('min_elem(5,8):', wavelet_tree.min_elem(5, 8))
    print('range_int(5,7,9,12)', wavelet_tree.range_int(5, 7, 9, 12))


if __name__ == '__main__':
    main()
