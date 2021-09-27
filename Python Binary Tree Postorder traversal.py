#Recursive method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__(self):
    self.a=[]
  def postOrderTraversal(self,root:TreeNode) -> List[int]:
    if root:
      self.postOrderTraversal(root.left)
      self.postOrderTraversal(root.right)  
      self.a.append(root.val)    
    return a
  
  
# 2 stack method
# take the root and append it to stack1, then run a loop till there are items in stack1,pop the item from stack1 and append it to stack2. 
# Check if poped item has left node and if it has then append it to stack1 and do same for right node.
# Now, pop items from stack2 and append them to solution list.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def postOrderTraversal(self,root:TreeNode) -> List[int]:
    stack1=[]
    stack2=[]
    a=[]
    stack1.append(root)
    while stack1:
      r=stack1.pop()
      stack2.append(r.val)
      
      if r.left is not None:
        stack1.append(r.left)
      if r.right is not None:
        stack1.append(r.right)
        
    while stack2:
      root=stack2.pop()
      a.append(root)
      
    return a
  

#  1 stack method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def peek(self,stack):
    if len(stack)>0:
      return stack[-1]
    return 
  
  def postOrderTraversal(self,root:TreeNode) -> List[int]:
    stack=[]
    a=[]
    while True:
      while root is not None:
        if root.right is not None:
          stack.append(root.right)
        
        stack.append(root)
        root=root.left
        
      root=stack.pop()
      if root.right is not None and self.peek(stack)==root.right:
        stack.pop()
        stack.append(root)
        root=root.right
      else:
        a.append(root)
        root=None
        
    return a
        
    
      
        
