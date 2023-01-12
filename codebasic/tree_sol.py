class TreeNode:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, everything):
        if everything == "both":
            spaces = ' '*self.get_level()*3
            prefix = spaces+"!__" if self.parent else ""
            print(prefix+self.name, "{}".format(self.position))
            if self.children:
                for child in self.children:
                    child.print_tree("both")
        elif everything == "designation":
            spaces = ' '*self.get_level()*3
            prefix = spaces+"!__" if self.parent else ""
            print(prefix+format(self.position))
            if self.children:
                for child in self.children:
                    child.print_tree("designation")

        elif everything == "name":
            spaces = ' '*self.get_level()*3
            prefix = spaces+"!__" if self.parent else ""
            print(prefix+format(self.name))
            if self.children:
                for child in self.children:
                    child.print_tree("name")

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_Tree():
    root = TreeNode("Nilpul", "CEO")

    laptop = TreeNode("CHINMAY", "cto")
    laptop.add_child(TreeNode("dhaval", "cloud manager"))
    laptop.add_child(TreeNode("abhijit", 'app manager'))
    laptop.add_child(TreeNode("aamir", 'application head'))

    cellphone = TreeNode("Gels", "hr head")
    cellphone.add_child(TreeNode("peter", 'recruitment manager'))
    cellphone.add_child(TreeNode("waqas", 'policy manager'))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root


if __name__ == "__main__":
    rn=build_product_Tree()
    rn.print_tree("both")
    rn.print_tree("name")
    rn.print_tree("designation")    
    
