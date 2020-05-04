

class Modifier:
    def __init__(self, pre_add=0, mult=1.0, post_add=0):
        self.pre_add = pre_add
        self.mult = mult
        self.post_add = post_add

    def __add__(self, other):
        return Modifier(pre_add=self.pre_add + other.pre_add,
                     mult=self.mult + other.mult - 1,
                     post_add=self.post_add + other.post_add)
