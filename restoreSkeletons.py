from maya import cmds
from cache import Cache
from joint import Joint
import pickle
import time

# A simple tool that analyzes a Maya scene and stores and restores all joint hierarchies
# Stores all hierarchies, bones, index order, and complete transform with joint orientation
class RestoreSkeletons(object):
    def __init__(self):
        self.name = "Restore Skeletons"
        self.cachePath = "/tmp/skeletons.spooky" # custom file type we will encode skeleton data into
        self.status = "No skeleton data currently stored"
        self.statusUI = None
        self.buildUI()

    def buildUI(self):
        if cmds.window(self.name, exists=True):
            cmds.deleteUI(self.name, window=True)
        window = cmds.window(self.name)
        cmds.columnLayout(adj=True)
        cmds.button("Store", w=200, command=self.onStoreClick, align='center')
        cmds.button("Restore", w=200, command=self.onRestoreClick, align='center')
        cmds.separator()
        self.statusUI = cmds.text(label = self.status, align='center')
        cmds.showWindow(window)


    def onStoreClick(self, _):
        cache = Cache()
        for path in cmds.ls(type="joint", long=True):
            joint = Joint(path)
            cache.store(joint.name, joint, joint.path) 
        with open(self.cachePath, 'wb') as f: # encode all skeletal data into external savefile
            pickle.dump(cache, f)
        
        self.status = "Last stored: {}".format(time.asctime(time.localtime(time.time())))
        cmds.text(self.statusUI, edit=True, label=self.status)
        
    def onRestoreClick(self, _):
        with open(self.cachePath, 'rb') as f: # read skeletal data
            cache = pickle.load(f)
        cache.inorder(lambda j: j.restore()) # see restore function of Joint class (joint.py)

        









        



    
        
            




        

                




        










