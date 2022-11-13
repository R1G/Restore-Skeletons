from maya import cmds

class Joint:
    #TODO: Examine the artist's workflow to determine if more attributes are needed
    # adding pivots, offset matrices, etc. felt overkill based on the initial writeup
    def __init__(self, jointPath):
        self.path = jointPath.split('|')
        self.name = self.path.pop(-1)
        self.parent = self.getParent(self.name)
        self.pos = cmds.getAttr(self.name+".translate")[0]
        self.rot = cmds.getAttr(self.name+".rotate")[0]
        self.rotOrder = cmds.getAttr(self.name+".rotateOrder")
        self.scale = cmds.getAttr(self.name+".scale")[0]
        self.shear = cmds.getAttr(self.name+".shear")[0]
        self.rotAxis = cmds.getAttr(self.name+".rotateAxis")[0]
        self.inherits = cmds.getAttr(self.name+".inheritsTransform")
        self.orient = cmds.getAttr(self.name+".jointOrient")[0]

    def getParent(self, name):
        parent = cmds.listRelatives(name, parent=True)
        if parent is not None:
            parent = parent[0]
        return parent

    def restore(self):
        if self.name not in cmds.ls(type="joint"):
            print(self.name + " was deleted. rebuilding now...")
            new_joint = cmds.joint()
            cmds.rename(new_joint, self.name)
        
        parent = self.getParent(self.name)
        if parent != self.parent:
            print("{} was found under {}. reparenting to {}".format(self.name, parent, self.parent))
            cmds.parent(self.name, self.parent)

        #TODO: Could iterate over cmds.listAttr...save a few lines that way
        cmds.setAttr(self.name+".translate", *self.pos)
        cmds.setAttr(self.name+".rotate", *self.rot)
        cmds.setAttr(self.name+".rotateOrder", self.rotOrder)
        cmds.setAttr(self.name+".scale", *self.scale)
        cmds.setAttr(self.name+".shear", *self.shear)
        cmds.setAttr(self.name+".rotateAxis", *self.rotAxis)
        cmds.setAttr(self.name+".inheritsTransform", self.inherits)
        cmds.setAttr(self.name+".jointOrient", *self.orient)
