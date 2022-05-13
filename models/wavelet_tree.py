from models.node import Node


class WaveletTree(object):
    def __init__(self, data=None):
        if data is None:
            print('Please give correct parameters')
            return
        self.__root = Node(data)  # Create the parent node

    def rank_query(self, character=None, position=None):
        if character is None or position is None or position <= 0:
            print('Please give correct parameters')
            return -1
        return self.__root.get_rank_query(position, character)

    def select_query(self, character=None, position=None):
        if character is None or position is None or position <= 0:
            print('Please give correct parameters')
            return -1
        return self.__root.get_select_query(position, character)

    def track_symbol(self, position=None):
        if position is None or position <= 0:
            print('Please give correct parameters')
            return -1
        return self.__root.get_track_symbol(position)

    def __print_tree_util(self, current_node, space_num, bit):
        space = ''.join([' '] * space_num)
        if bit:
            print(space + ' '.join([str(int(bit_data)) for bit_data in current_node.bits_full_data]))
        else:
            print(space + ' '.join(current_node.full_data))

        new_space_num = space_num + 2

        for child in current_node.children:
            self.__print_tree_util(child, new_space_num, bit)

    def get_root(self):
        return self.__root

    def print_tree(self, bit=False):
        current_node = self.__root

        self.__print_tree_util(current_node, 0, bit)

    def is_contain_bit(self, curr_node, sp, ep, bit):
        rank_sp = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, bit)) + 1
        select_sp = curr_node.get_select_bit(rank_sp, bit)

        is_contain = sp <= select_sp <= ep

        if is_contain:
            select_ep = curr_node.get_select_bit(curr_node.get_rank_bit(ep, bit), bit)
            new_sp = curr_node.get_rank_bit(select_sp, bit)
            new_ep = curr_node.get_rank_bit(select_ep, bit)

            return is_contain, new_sp, new_ep
        else:
            return is_contain, None, None

    def max_elem_util(self, curr_node, sp, ep):
        if len(curr_node.children) == 0:
            return curr_node.full_data[0]

        is_contain_1, new_sp_1, new_ep_1 = self.is_contain_bit(curr_node, sp, ep, True)

        if is_contain_1:
            curr_node = curr_node.children[1]

            return self.max_elem_util(curr_node, new_sp_1, new_ep_1)
        else:
            is_contain_0, new_sp_0, new_sp_0 = self.is_contain_bit(curr_node, sp, ep, False)
            curr_node = curr_node.children[0]

            return self.max_elem_util(curr_node, new_sp_0, new_sp_0)

    def max_elem(self, sp, ep):
        return self.max_elem_util(self.__root, sp, ep)

    def min_elem_util(self, curr_node, sp, ep):
        if len(curr_node.children) == 0:
            return curr_node.full_data[0]

        is_contain_0, new_sp_0, new_ep_0 = self.is_contain_bit(curr_node, sp, ep, False)

        if is_contain_0:
            curr_node = curr_node.children[0]

            return self.min_elem_util(curr_node, new_sp_0, new_ep_0)
        else:
            is_contain_1, new_sp_1, new_ep_1 = self.is_contain_bit(curr_node, sp, ep, True)
            curr_node = curr_node.children[1]

            return self.min_elem_util(curr_node, new_sp_1, new_ep_1)

    def min_elem(self, sp, ep):
        return self.min_elem_util(self.__root, sp, ep)

    def range_int_util(self, curr_node, sp1, ep1, sp2, ep2):
        if len(curr_node.children) == 0:
            return [curr_node.full_data[0]]

        is_int1_contain_0, new_sp1_0, new_ep1_0 = self.is_contain_bit(curr_node, sp1, ep1, False)
        is_int2_contain_0, new_sp2_0, new_ep2_0 = self.is_contain_bit(curr_node, sp2, ep2, False)

        result = []

        if is_int1_contain_0 and is_int2_contain_0:
            result += self.range_int_util(curr_node.children[0], new_sp1_0, new_ep1_0, new_sp2_0, new_ep2_0)

        is_int1_contain_1, new_sp1_1, new_ep1_1 = self.is_contain_bit(curr_node, sp1, ep1, True)
        is_int2_contain_1, new_sp2_1, new_ep2_1 = self.is_contain_bit(curr_node, sp2, ep2, True)

        if is_int1_contain_1 and is_int2_contain_1:
            result += self.range_int_util(curr_node.children[1], new_sp1_1, new_ep1_1, new_sp2_1, new_ep2_1)

        return result

    def range_int(self, sp1, ep1, sp2, ep2):
        return self.range_int_util(self.__root, sp1, ep1, sp2, ep2)

    def is_overlap(self, l, h, part_l, part_h):
        return h >= part_l and l <= part_h

    def max_range_util(self, curr_node, sp, ep, l, h):
        if len(curr_node.children) == 0:
            return [curr_node.full_data[0]]

        left_l = curr_node.children[0].data[0]
        left_h = curr_node.children[0].data[-1]
        right_l = curr_node.children[1].data[0]
        right_h = curr_node.children[1].data[-1]

        is_left_overlap = self.is_overlap(l, h, left_l, left_h)
        is_right_overlap = self.is_overlap(l, h, right_l, right_h)

        is_contain_0, new_sp_0, new_ep_0 = self.is_contain_bit(curr_node, sp, ep, False)
        is_contain_1, new_sp_1, new_ep_1 = self.is_contain_bit(curr_node, sp, ep, True)

        print('is_left_overlap', is_left_overlap)
        print('is_right_overlap', is_right_overlap)
        print('is_contain_0 new_sp_0 new_ep_0', is_contain_0, new_sp_0, new_ep_0)
        print('is_contain_1 new_sp_1 new_ep_1', is_contain_1, new_sp_1, new_ep_1)

        if is_left_overlap and is_contain_0 and is_right_overlap and is_contain_1:
            rank_sp_0 = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, False))
            rank_ep_0 = curr_node.get_rank_bit(ep, False)
            rank_sp_1 = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, True))
            rank_ep_1 = curr_node.get_rank_bit(ep, True)

            num_0 = rank_ep_0 - rank_sp_0
            num_1 = rank_ep_1 - rank_sp_1

            print('num_0 num_1', num_0, num_1)

            if num_0 == num_1:
                return self.max_range_util(curr_node.children[0], new_sp_0, new_ep_0, l, h) + \
                         self.max_range_util(curr_node.children[1], new_sp_1, new_ep_1, l, h)
            elif num_0 > num_1:
                return self.max_range_util(curr_node.children[0], new_sp_0, new_ep_0, l, h)
            else:
                return self.max_range_util(curr_node.children[1], new_sp_1, new_ep_1, l, h)
        elif is_left_overlap and is_contain_0:
            return self.max_range_util(curr_node.children[0], new_sp_0, new_ep_0, l, h)
        elif is_right_overlap and is_contain_1:
            return self.max_range_util(curr_node.children[1], new_sp_1, new_ep_1, l, h)
        else:
            return []

    def max_range(self, sp, ep, l, h):
        return self.max_range_util(self.__root, sp, ep, l, h)
