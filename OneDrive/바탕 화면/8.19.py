class treeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def is_complete_binary_tree(root):
    if not root:
      return True
    
    queue = [root]
    found_null = False

    while queue:
      current_node = queue.pop(0)

      if current_node:
        return False

        queue.append(current_node.left)
        queue.append(current_node.right)
      else:
        found_null = True
    
    return True