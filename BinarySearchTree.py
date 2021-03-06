class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, insert_value):
        if insert_value < self.value:
            if self.left is None:
                self.left = Node(insert_value)
            else:
                self.left.insert(insert_value)
        else:
            if self.right is None:
                self.right = Node(insert_value)
            else:
                self.right.insert(insert_value)

    def min_value_node_delete(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, delete_value):
        if delete_value < self.value:
            self.left = self.left.delete(delete_value)
        elif delete_value > self.value:
            self.right = self.right.delete(delete_value)
        else:
            if self.left is None:
                temp = self.right
                return temp
            elif self.right is None:
                temp = self.left
                return temp
            temp = self.min_value_node_delete(self.right)
            self.value = temp.value
            self.right = self.right.delete(temp.value)
        return self

    def contains(self, contain_value):
        if contain_value == self.value:
            return True
        elif contain_value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(contain_value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(contain_value)

    def preorder(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value)
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)


child_nodes = []
def print_nodes_with_one_child(root):
    if not root:
        return

    if not root.left and root.right:
        child_nodes.append(root)
    elif root.left and not root.right:
        child_nodes.append(root)

    print_nodes_with_one_child(root.left)

    print_nodes_with_one_child(root.right)

    return

# Write to list every child node of the parameter root node.
def childs_tolist(actual_node, list):
    if not actual_node:
        return
    if actual_node.right:
        list.append(actual_node.right)
    if actual_node.left:
        list.append(actual_node.left)

    childs_tolist(actual_node.left, list)

    childs_tolist(actual_node.right, list)

    return

# Check the tree is contains the parameter node, and write every child of this node into a list.
def node_childs_tolist(root, contain_node):
    child_nodes_tolist = []
    if contain_node == root.value:
        childs_tolist(actual_node=root, list=child_nodes_tolist)
        return child_nodes_tolist
    elif contain_node < root.value:
        if root.left is None:
            return []
        else:
            return node_childs_tolist(root.left, contain_node)
    else:
        if root.right is None:
            return []
        else:
            return node_childs_tolist(root.right, contain_node)


def main():
    #      50
    #    /      \
    #   30     70
    #   / \    / \
    #  20 40  60 80

    node = Node(50)
    node.insert(30)
    node.insert(20)
    node.insert(40)
    node.insert(70)
    node.insert(60)
    # node.insert(80)

    print("Preorder: ---------")
    node.preorder()
    print("Inorder: ---------")
    node.inorder()
    print("Postorder: ---------")
    node.postorder()

    print("")
    print(node.contains(20))
    print(node.contains(90))
    print(node.contains(70))
    print("")
    # node.delete(20)
    # node.delete(30)
    # node.delete(50)
    print("Inorder after delete: ")
    node.inorder()

    print("")
    print("Has Only One Child:")
    print_nodes_with_one_child(node)
    for i in child_nodes:
        print(i.value, end=" ")
    print()

    print("")
    print("Childs of the node:")
    result = node_childs_tolist(node, 30)
    for i in result:
        print(i.value, end=" ")
    print()


if __name__ == "__main__":
    main()
