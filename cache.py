# stores joint data as well as joint hierarches
from hierarchy import Hierarchy

class Cache:
    def __init__(self):
        self.data = {}
        self.hierarchy = Hierarchy("SCENE")

    def store(self, key, value, path):
        self.storeData(key, value)
        self.storeHierarchy(key, path)

    def storeData(self, key, val):
        self.data[key] = val

    def storeHierarchy(self, key, path):
        self.hierarchy.insert(key, path)

    #useful for calling a function on every node in the hierarchy
    def inorder(self, fn=print):
        for key in self.hierarchy.inorder():
            if key in self.data.keys():
                fn(self.data[key])





        