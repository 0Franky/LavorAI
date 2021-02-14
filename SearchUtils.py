import numpy as np

def ida_star(root):
  bound = h(root)
  path = [root]
  while True:
    t = search(path, 0, bound)
    if t == "FOUND":
      return (path, bound)
    if t == np.Inf:
      return "NOT_FOUND"
    bound = t


def search(path, g, bound):
  node = path.last
  f = g + h(node)
  if f > bound:
    return f
  if is_goal(node):
    return "FOUND"
  min = np.Inf
  for succ in successors(node):
    if succ not in path:
      path.append(succ)
      t = search(path, g + cost(node, succ), bound)
      if t == "FOUND":
        return "FOUND"
      if t < min:
        min = t
      path.pop()
  return min





  
















  

def h(node):
  return "stub"

def is_goal(node):
  return False

def successors(node):
  return node

def cost(node, succ):
  return 5