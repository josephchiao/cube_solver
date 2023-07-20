from dataclasses import dataclass

@dataclass
class BST:
    key : int
    info: int
    l: False
    r: False

    def search(self, desired):
        if self.key == desired:
            return self.info
        elif not (self.l or self.r):
            return False
        elif self.l.search(desired):
            return self.l.search(desired)
        else:
            return self.r.search(desired)

bst = BST(6, 1001, BST(4, 1100, False, False), False)
print(bst.search(4))