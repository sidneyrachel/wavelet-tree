# Implementation of some algorithms on wavelet tree
## Introduction
We get the implementation of wavelet tree data structure from: [nectarios-ef/Wavelet-Tree](https://github.com/nectarios-ef/Wavelet-Tree).
We implement four algorithms on wavelet tree:
> S is the original input array.
1. `max_elem(sp, ep)`: Maximum value in `S[sp,ep]`.
2. `min_elem(sp, ep)`: Minimum value in `S[sp,ep]`.
3. `range_int(sp1, ep1, sp2, ep2)`: All the common value in `S[sp1,ep1]` and `S[sp2,ep2]`.
4. `max_range(sp, ep, l, h)`: The most frequently appearing value between at least `l` and at most `h` in `S[sp,ep]`.

## How To
1. Make sure you have Python 3.9.
2. Place the input inside `input.txt`.
3. Modify `main.py` to receive intended parameters for each algorithm.
4. Run `python main.py input.txt`.
