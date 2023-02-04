"""Here we attempt to make an organizational hierarchy with sub-organization,
which may have subsequent sub-organizations, such as:
GeneralManager								 [Composite]
	Manager1								 [Composite]
			Developer11					 [Leaf]
			Developer12					 [Leaf]
	Manager2								 [Composite]
			Developer21					 [Leaf]
			Developer22					 [Leaf]"""


class LeafElement:

    '''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)


class CompositeElement:

    def __init__(self, *args):

        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()


if __name__ == "__main__":

    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()
