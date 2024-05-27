from dataclasses import dataclass
@dataclass
class Group:
    """This is a basic group function to store the blocks, the get and set items have been added for backwards compatibility"""
    a:int
    b:int
    c:int
    d:int
    is_version_b: bool=False #should be none if theres no group set
    def to_list(self):
        return [self.a, self.b, self.c, self.d]
    def __iter__(self):
        return self.to_list()
    def __getitem__(self, key):
        return getattr(self, ["a","b","c","d"][key], None)
    def __setitem__(self, key, value):
        setattr(self, ["a","b","c","d"][key], value)