import sys
from models.file_reader import FileReader
from models.wavelet_tree import WaveletTree


def main():
    file_reader = FileReader(sys.argv)

    if not file_reader.is_read():
        sys.exit()

    wavelet_tree = WaveletTree(file_reader.get_characters())
    print('Original tree:')
    wavelet_tree.print_tree(is_bit=False)
    print()

    print('Bit tree:')
    wavelet_tree.print_tree(is_bit=True)
    print()

    print('max_elem(4,8):', wavelet_tree.max_elem(sp=4, ep=8))
    print('min_elem(4,8):', wavelet_tree.min_elem(sp=4, ep=8))
    print('range_int(5,7,9,12):', wavelet_tree.range_int(sp1=5, ep1=7, sp2=9, ep2=12))
    print('max_range(4,9,4,9):', wavelet_tree.max_range(sp=4, ep=9, l='4', h='9'))


if __name__ == '__main__':
    main()
