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

    def get_array_index(self, num):  # idx starts from 0
        return num - 1

    def get_original_index(self, num):  # idx starts from 1
        return num + 1

    def max_elem_util(self, curr_node, sp, ep):
        if len(curr_node.children) == 0:
            return curr_node.full_data[0]

        sp_idx = self.get_array_index(sp)
        ep_idx = self.get_array_index(ep)

        st_0 = -1
        end_0 = -1
        st_1 = -1
        end_1 = -1

        # TODO: Change this to be more efficient
        for idx in range(sp_idx, ep_idx + 1):
            if curr_node.bits_full_data[idx]:
                end_1 = idx

                if st_1 == -1:
                    st_1 = idx
            else:
                end_0 = idx

                if st_0 == -1:
                    st_0 = idx

        if st_1 != -1:
            new_sp = curr_node.get_rank(self.get_original_index(st_1), True)
            new_ep = curr_node.get_rank(self.get_original_index(end_1), True)
            curr_node = curr_node.children[1]

            return self.max_elem_util(curr_node, new_sp, new_ep)
        else:
            new_sp = curr_node.get_rank(self.get_original_index(st_0), False)
            new_ep = curr_node.get_rank(self.get_original_index(end_0), False)
            curr_node = curr_node.children[0]

            return self.max_elem_util(curr_node, new_sp, new_ep)

    def max_elem(self, sp, ep):
        return self.max_elem_util(self.__root, sp, ep)
