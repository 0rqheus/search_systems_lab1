import re

class ForwardIndex:
  def __init__(self, docs):
    self.docs = docs

  def run(self):
    result = {}
    for k, v in self.docs.items():
      l = list(set(re.findall("\w+'?\w+", v)))
      l.sort()
      result[k] = l
    return result