# Binary Search Tree

- #### 이진 탐색 트리란?

  지난 번에 했던 트리는 힙. 힙은 데이터 정렬 혹은, 우선순위 큐 라는 추상자료형을 만들 때 사용되었음. 

  이진탐색 트리는 주로, 세트나 딕셔너리 구현하는데 사용되어짐. 

  ![6_1](./resources/6_1.png)

  우선 이진탐색트리가 어떻게 동작하는지를 살펴보자. 

  이진탐색트리는 이진트리면서 동시에, 한가지 속성을 지켜야함. 

  어떤 노드를 기준으로 왼쪽에 있는 모든 노드는 그 노드보다 작아야 하고, 오른쪽에 있는 모든 노드는 그 노드보다 커야 함. 

  이런 속성을 바로 "**이진탐색트리 속성**"이라고 말한다. 

  ![6_1](./resources/6_2.png)

  이 특징이 이제, 루트노드 뿐만이 아닌 모든 노드에 들어가야 함. 

  ![6_1](./resources/6_3.png)

  이진탐색트리를 사용하면, 데이터를 찾는게 엄청 쉬움. 예를 들어 4를 찾고 싶다고 한다면, 작고 크고로 오른쪽 왼쪽으로 가면 돼. 각 왼쪽 오른쪽으로 가면서 데이터를 탐색해 갈 수 있음. 

  

- #### 이진탐색트리 노드 구현

  힙은 항상 완전이진트리였기 때문에 배열로 구현했음. 이진탐색트리는 이진트리이지만 완전이진트리라는 보장은 없다. 보통은 파이썬 리스트나 배열 등으로 구현하지 않는다. 

  ![6_1](./resources/6_4.png)

  부모 링크만 추가하면 됨. 각 노드는 자식들과 부모에 대한 레퍼런스를 모두 저장하고 있다. 

  ![6_1](./resources/6_5.png)

  ```python
  
  class Node:
      """이진 탐색 트리 노드 클래스"""
      def __init__(self, data):
          self.data = data
          self.parent = None
          self.left_child = None
          self.right_child = None
  
  # 노드 인스턴스 생성
  node_0 = Node(5)
  node_1 = Node(3)
  node_2 = Node(7)
  
  node_0.left_child = node_1
  node_0.right_child = node_2
  
  node_1.parent = node_0
  node_2.parent = node_0
  ```

  ![6_1](./resources/6_6.png)

  노드 클래스 뿐만이 아니라, 이진탐색트리 자체도 클래스로 만들면 조금 더 쉽다. 

  ```python
  
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
  ```

  아직은 생성하는 기능만 있고, 추가 등의 기능은 없음. 다음 레슨부터 어떻게 해야 되는지 알아볼 것. 



- #### 이진탐색트리 출력

  **in-order 순회**

  이진 탐색 트리에는 굉장히 재미있는 특성이 하나 더 있는데요. 전에 배웠던 in-order 순회, 기억나시나요?

  이런 트리를:

  ![6_7](./resources/6_7.png)

  in-order 순회하면서 노드의 값을 출력하면 A, B, C, D, E, F, G, H, I의 순서대로 출력됩니다.

  기억이 안 나는 분들을 위해 다시 정리하면 in-order 순회는

  1. 왼쪽 부분 트리를 in-order 순회한다
  2. 현재 노드의 데이터를 출력한다
  3. 오른쪽 부분 트리를 in-order 순회한다

  의 순서로 전체 트리를 순회합니다. 그래도 기억이 안 나시면 챕터 1을 복습하고 오세요.

  **in-order 순회와 이진 탐색 트리**

  이진 탐색 트리를 in-order 순회하면 저장된 데이터들을 정렬된 순서대로 출력할 수 있습니다. 아래와 같은 이진 탐색 트리가 있다고 했을 때

  ![6_1](./resources/6_8.png)

  트리의 root 노드(8이 있는 노드)를 in-order 순회 함수의 파라미터로 넘겨주면 트리 안에 있는 데이터를:

  1, 3, 4, 6, 7, 8, 10, 13, 14

  처럼 정렬된 순서대로 출력할 수 있는 거죠.

  **BinarySearchTree 클래스**

  이전에 구현해 본 in-order 순회 함수를 재활용해서 이진 탐색 트리를 나타내는 BinarySearchTree 클래스에 트리 속의 데이터를 순서대로 출력하는 메소드, `print_sorted_tree` 메소드를 작성할게요.

  ```python
  def print_inorder(node):
      """주어진 노드를 in-order로 출력해주는 함수"""
      if node is not None:
          print_inorder(node.left_child)
          print(node.data)
          print_inorder(node.right_child)
  
  
  class BinarySearchTree:
      """이진 탐색 트리 클래스"""
      def __init__(self):
          self.root = None
  
  
      def print_sorted_tree(self):
          """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
          print_inorder(self.root)  # root 노드를 in-order로 출력한다
  ```

  이제 트리를 출력할 때는 `print_sorted_tree` 메소드를 사용하겠습니다!



- #### 이진탐색트리 삽입

  당연하지만, 삽입한 뒤에도 이진탐색트리여야지. 

  ![6_1](./resources/6_9.png)

  13을 저장하는 새로운 노드를 만든다. 그리고, 어디에 저장해야 할지 위치를 알아내야 함. 

  ![6_1](./resources/6_10.png)

  루트 노드 부터 시작하는거지. 일단 18로 가. 그리고 18보다 작으니깐 15로 가. 그리고 15보다 작어. 거기에 노드가 없으면 추가하면서 가면 됨. 

  ![6_1](./resources/6_11.png)

  일반화 하자면 다음과 같다. 

  ![6_12](./resources/6_12.png)

  그러면 시간복잡도는 어떨까? 트리의 높이를 h라고 해보자. 

  최악의 경우는 트리의 높이만큼 비교하면서 내려와야 함. 예를 들어 아래에서 16을 넣는다고 하면 17을 아래까지 가지고 와야 함. 트리높이 보다 1만큼 더 비교해야 함. 

  ![6_12](./resources/6_13.png)

  즉, 시간복잡도는 **O(h)**가 걸린다는 뜻. 

  ![6_12](./resources/6_14.png)

  

- #### 이진탐색트리 탐색

  ![6_12](./resources/6_15.png)

  탐색은 왼쪽 오른쪽으로 오며가며 찾으면 끝. 

  ![6_12](./resources/6_16.png)

  ![6_12](./resources/6_17.png)

  **시간복잡도는?**

  ![6_12](./resources/6_18.png)

  ![6_12](./resources/6_19.png)



- #### 이진탐색트리 삭제 1

  삭제할때는 여러가지 경우를 고려해야 한다. 

  일단 그 데이터를 저장하고 있는 노드에 접근해야 한다. 이때는 그냥 이전에 했던 탐색연산을 사용하면 됨. 

  ![6_12](./resources/6_20.png)

  이제 찾았으면 경우의수가 있음. 

  **경우1. 지우려는 노드가 leaf 노드일때**

  ![6_12](./resources/6_21.png)

  이때는 그냥, 부모 6의 오른쪽 자식 레퍼런스를 None으로 지정해 주면 됨. 

  ![6_12](./resources/6_22.png)

  오른쪽, 왼쪽 자식인지만 확인하면 됨. 

  **경우2. 삭제하려는 노드가 하나의 자식 노드만 있을 때**

  ![6_12](./resources/6_23.png)

  이때는 그냥 자식이 부모의 자리 차지하게 하면 된다. 14를 8의 오른쪽 자식 노드로 지정하면 끝. 

  ![6_12](./resources/6_24.png)

