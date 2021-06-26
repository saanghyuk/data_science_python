
class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    """이진탐색트리 클래스"""
    def __init__(self):
        self.root = None

bst = BinarySearchTree()

# 노드 인스턴스 생성
node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)

node_0.left_child = node_1
node_0.right_child = node_2

node_1.parent = node_0
node_2.parent = node_0