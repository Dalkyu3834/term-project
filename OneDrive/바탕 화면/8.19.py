class TreeNode:
  def __init__(self,value) :              #초기값 설정. 노드 없
    self.value = value
    self.left = None
    self.right = None

  def is_complete_binary_tree(root):      #루트 검사 함수 생성
    if not root:                          #루트가 없다면 True 반환
      return True

    queue = [root]                        #queue로 루트 생성
    found_null = False                    #found_null변수는 트리 순회 중 None을 발견했는지 판단하는 여부

    while queue:
      current_node = queue.pop(0)         #맨앞에 있는 노드 추출, 끝날때까지

      if current_node:                    #레벨 순서로 순회, True인 경우 노드가 나오면 False 반환
        return False

        queue.append(current_node.left)   #현재 노드의 왼쪽에 추가
        queue.append(current_node.right)  #현재 노드의 오른쪽에 추가
      else:
        found_null = True                 #현재 노드가 None일 경우 True 반환

    return True                           #큐가 모두 돌았을 경우 완전 이진 트리를 뜻하므로 True 반환