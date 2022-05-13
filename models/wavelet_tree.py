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

    def max_elem_util(self, curr_node, sp, ep):
        if len(curr_node.children) == 0:
            return curr_node.full_data[0]

        rank_sp_1 = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, True)) + 1
        select_sp_1 = curr_node.get_select_bit(rank_sp_1, True)

        if sp <= select_sp_1 <= ep:  # contains 1
            select_ep_1 = curr_node.get_select_bit(curr_node.get_rank_bit(ep, True), True)
            new_sp = curr_node.get_rank_bit(select_sp_1, True)
            new_ep = curr_node.get_rank_bit(select_ep_1, True)
            curr_node = curr_node.children[1]

            return self.max_elem_util(curr_node, new_sp, new_ep)
        else:
            rank_sp_0 = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, False)) + 1
            select_sp_0 = curr_node.get_select_bit(rank_sp_0, False)
            select_ep_0 = curr_node.get_select_bit(curr_node.get_rank_bit(ep, False), False)
            new_sp = curr_node.get_rank_bit(select_sp_0, False)
            new_ep = curr_node.get_rank_bit(select_ep_0, False)
            curr_node = curr_node.children[0]

            return self.max_elem_util(curr_node, new_sp, new_ep)

    def max_elem(self, sp, ep):
        return self.max_elem_util(self.__root, sp, ep)

    def min_elem_util(self, curr_node, sp, ep):
        if len(curr_node.children) == 0:
            return curr_node.full_data[0]

        rank_sp_0 = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, False)) + 1
        select_sp_0 = curr_node.get_select_bit(rank_sp_0, False)

        if sp <= select_sp_0 <= ep:  # contains 0
            select_ep_0 = curr_node.get_select_bit(curr_node.get_rank_bit(ep, False), False)
            new_sp = curr_node.get_rank_bit(select_sp_0, False)
            new_ep = curr_node.get_rank_bit(select_ep_0, False)
            curr_node = curr_node.children[0]

            return self.min_elem_util(curr_node, new_sp, new_ep)
        else:
            rank_sp_1 = (0 if sp == 1 else curr_node.get_rank_bit(sp - 1, True)) + 1
            select_sp_1 = curr_node.get_select_bit(rank_sp_1, True)
            select_ep_1 = curr_node.get_select_bit(curr_node.get_rank_bit(ep, True), True)
            new_sp = curr_node.get_rank_bit(select_sp_1, True)
            new_ep = curr_node.get_rank_bit(select_ep_1, True)
            curr_node = curr_node.children[1]

            return self.min_elem_util(curr_node, new_sp, new_ep)

    def min_elem(self, sp, ep):
        return self.min_elem_util(self.__root, sp, ep)
