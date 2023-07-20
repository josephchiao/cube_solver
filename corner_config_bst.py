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
        elif self.key > desired and self.l:
            return self.l.search(desired)
        elif self.key < desired and self.r:
            return self.r.search(desired)
        else: 
            return False

bst = BST(6, 1001, BST(4, 1100, False, False), False)
print(bst.search(4))
print(bst.search(3))