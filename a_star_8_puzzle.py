# cs20b1063
# siddhardha

import copy
import itertools

initial_state = [[2,8,3],
                 [1,6,4],
                 [7,0,5]]

final_state = [[1,2,3],
               [8,0,4],
               [7,6,5]]

class StateNode:
    def __init__(self, current, depth , path):
        self.current_state = current
        self.heuristic = self.get_heuristic()
        self.blank_index = self.get_index()
        self.depth = depth
        self.cost = self.heuristic+ self.depth
        self.changeable_tiles = self.get_change_tiles(self.current_state)
        self.path = path
    
    def get_heuristic(self):
        return sum(
            self.current_state[i][j] not in [final_state[i][j], 0]
            for i, j in itertools.product(range(3), range(3))
        )
    
    def get_index(self):
        return next(
            (
                [i, j]
                for i, j in itertools.product(range(3), range(3))
                if self.current_state[i][j] == 0
            ),
            [-1, -1],
        )
        
    def is_final_state(self):
        return all(
            self.current_state[i][j] == final_state[i][j]
            for i, j in itertools.product(range(3), range(3))
        )
    
    def get_change_tiles(self,current_state):
        # [up , down , left , right]
        ch_list = []
        i = self.blank_index[0]
        j = self.blank_index[1]
        
        state_node = copy.deepcopy(current_state)
        
        # Check if the blank tile is not in the first row
        if self.blank_index[0] != 0:
            state_node[i][j], state_node[i-1][j] = current_state[i-1][j], current_state[i][j]
            ch_list.append(state_node)
            
        # Check if the blank tile is not in the last row
        if self.blank_index[0] != 2:
            state_node = copy.deepcopy(current_state)
            state_node[i][j], state_node[i+1][j] = current_state[i+1][j], current_state[i][j]
            ch_list.append(state_node)
        
        # Check if the blank tile is not in the first column
        if self.blank_index[1] != 0:
            state_node = copy.deepcopy(current_state)
            state_node[i][j], state_node[i][j-1] = current_state[i][j-1], current_state[i][j]
            ch_list.append(state_node)
        
        # Check if the blank tile is not in the last column
        if self.blank_index[1] != 2:
            state_node = copy.deepcopy(current_state)
            state_node[i][j], state_node[i][j+1] = current_state[i][j+1], current_state[i][j]
            ch_list.append(state_node)
        return ch_list

def print_list(list):
    for i in list:
        for j in i:
            print(j)
        print("\n    |\n    |\n    V\n")

def a_star_8_puzzle():
    queue = [StateNode(initial_state,0,[initial_state])]
    while queue:
        state = queue.pop(0)
        if state.is_final_state():
            return state.path
        queue.extend(
            StateNode(next_state, state.depth + 1, state.path + [next_state])
            for next_state in state.changeable_tiles
        )
        queue.sort(key=lambda x: x.cost)

print("(Initial State)")
print_list(a_star_8_puzzle())
print("Final State Reached!")