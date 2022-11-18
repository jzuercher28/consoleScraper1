from anytree import Node, RenderTree
from Scraper_class import Scraper


class HtmlTree:
    def __init__(self, root=None):
        self.root = root
        self.children = []

    def set_root(self, root):
        self.root = Node(root)

    def add_child(self, node):
        self.children.append(Node(node, parent=self.root))

    def branch(self, rootnode, newnode):
        htmltree = HtmlTree()
        htmltree.set_root(rootnode)
        htmltree.add_child(newnode)

    def preview_tree(self):
        for pre, fill, node in RenderTree(self.root):
            print(f"{pre}{node.name}")


def main():
    htmltree = HtmlTree()
    htmltree.set_root("https://google.com")
    l = ['/images', '/news', '/search']
    for branch in l:
        htmltree.add_child(branch)

    htmltree.preview_tree()


if __name__ == "__main__":
    main()