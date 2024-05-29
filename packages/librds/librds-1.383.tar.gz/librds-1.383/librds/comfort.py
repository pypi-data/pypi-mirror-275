from enum import Enum, IntEnum

def get_from_list(input:list,index:int,default=None):
    """This is a simple function to remove index errors from the group generators"""
    try:
        return input[index]
    except IndexError:
        return default

class Groups(Enum):
    PS = 0
    PS_B = 1
    RT = 2
    RT_B = 3
    PTYN = 4
    ECC = 5
    LIC = 6
    TDA = 7
    TDA_B = 8
    IN_HOUSE = 9
    IN_HOUSE_B = 10

class GroupSequencer:
    """you can use this code to sequence though anything"""
    def __init__(self, sequence:list[IntEnum]) -> None:
        self.cur_idx = 1
        self.sequence = sequence
    def get_next(self):
        if len(self.sequence) == 0: return
        if self.cur_idx > len(self.sequence)-1: self.cur_idx = 1
        prev = self.sequence[self.cur_idx-1]
        self.cur_idx += 1
        return prev
    def change_sequence(self, sequence:list[IntEnum]):
       self.sequence = sequence
       self.cur_idx = 1
    def __len__(self):
        return len(self.sequence)
