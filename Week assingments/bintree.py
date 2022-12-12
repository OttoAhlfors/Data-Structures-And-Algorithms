#Lähteenä kurssimateriaali
#https://moodle.lut.fi/mod/page/view.php?id=721075

class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = self.right = None
 

class BST:
    def __init__(self):
        self.root = None

    # insert the key into BST
    # Voidaan toteuttaa samoin kuin hakeminen
    def insert(self, key):
        # Asetetaan avain haluttuun paikkaan insert_help-funktiolla
        self.root = self.insert_help(self.root, key)
    
    def insert_help(self, node, key):
        # Jos node on None, palautetaan uusi node
        if not node:
            return Node(key)
        # Jos node on pienempi kuin avain, siirrytään oikealle
        elif node.key > key:
            node.left = self.insert_help(node.left, key)
        # Jos node on suurempi kuin avain, siirrytään vasemmalle
        elif node.key < key:
            node.right = self.insert_help(node.right, key)
        return node

    # search the key from BST #Lähteenä kurssimateriaalis
    def search(self, key):
        return self.search_help(self.root, key)

    # help function for 'search'.#Lähteenä kurssimateriaali
    def search_help(self, node, key):
        if not node:
            return False
        elif node.key > key:
            return self.search_help(node.left, key)
        elif node.key < key:
            return self.search_help(node.right, key)
        # None of the conditions were true. That
        # means the node stores the key.
        return True

    # order the BST #Lähteenä kurssimateriaali
    def preorder(self):
        stack = [self.root]     # start: stack with root only
        while stack != []:
            next = stack.pop(-1) # pop the node from the top of the stack
            # push right and left children of 'next' into the stack 
            if next.right != None:
                stack.append(next.right)
            if next.left != None:
                stack.append(next.left)
            print(next.key, end = " ")  # visit 'next'
        print()

    # find the minimum value in the BST, used for remove
    def min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current.key

    # remove the key from BST
    # https://moodle.lut.fi/mod/page/view.php?id=661713
    def remove(self, key):
        self.root = self.remove_help(self.root, key)
        Tree.preorder()

    def remove_help(self, node, key):
        # Etsitään avainta
        if not node:
            return None
        elif node.key > key:
            node.left = self.remove_help(node.left, key)
        elif node.key < key:
            node.right = self.remove_help(node.right, key)
        # Avain löytyi
        else:
            # Jos avaimella on vain yksi lapsi
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Jos avaimella on kaksi lasta
            else:
                node.key = self.min_value(node.right)
                node.right = self.remove_help(node.right, node.key)
        return node
    
if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()     # 5 1 3 2 4 9 7 6 
    Tree.remove(1)
    Tree.preorder()     # 5 3 2 4 9 7 6 
    Tree.remove(9)
    Tree.preorder()     # 5 3 2 4 7 6
    Tree.remove(3)
    Tree.preorder()     # 5 2 4 7 6