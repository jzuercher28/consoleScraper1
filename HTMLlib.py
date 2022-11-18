from anytree import Node, RenderTree

root = Node(10)

level_1_child_1 = Node(34, parent=root)
level_1_child_2 = Node(89, parent=root)
level_2_child_1 = Node(45, parent=level_1_child_1)
level_2_child_2 = Node(50, parent=level_1_child_2)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

root2 = Node("https://google.com")
_level_1_child_1 = Node("/images/", parent=root2)
_level_1_child_2 = Node("/search/", parent=root2)
_level_2_child_1 = Node(f"/images/find/", parent=_level_1_child_1)
_level_2_child_2 = Node(f"/search/feelinglucky/", parent=_level_1_child_2)

for pre, fill, node in RenderTree(root2):
    print("%s%s" % (pre, node.name))


# Tree Structure
#          10
#        /    \
#       34      89
#     /    \
#    45    50

