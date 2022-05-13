import sys
from models.file_reader import FileReader
from models.wavelet_tree import WaveletTree


def main():
    file_reader = FileReader(sys.argv)
    if (not file_reader.is_read()):
        sys.exit()
    wavelet_tree = WaveletTree(file_reader.get_characters())
    wavelet_tree.print_tree(bit=False)
    # print(wavelet_tree.track_symbol(1))
    # print(wavelet_tree.rank_query('5', 6))
    # print(wavelet_tree.select_query('e', 1))


if __name__ == '__main__':
    main()
