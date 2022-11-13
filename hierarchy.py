# Binary tree structure that stores node names and their children
# Could be used for applications other than joint hierarchies
class Hierarchy:
    def __init__(self, name):
        self.name = name
        self.children = {}
        
    def insert(self, name, path):
        if self.name == name:
            return
        if path == []:
            if name not in self.children.keys():
                self.children[name] = Hierarchy(name)
        else:
            parent = path.pop(0)
            if parent not in self.children.keys():
                self.children[parent] = Hierarchy(parent) 
            self.children[parent].insert(name, path)

    def inorder(self):
        output = []
        output.append(self.name)
        for child in self.children.values():
            output += child.inorder()
        return output