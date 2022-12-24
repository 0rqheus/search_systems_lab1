from src.base_index import BaseIndex

class ForwardIndex(BaseIndex):
  def run(self):
    result = {}
    for k in self.docs.keys():
      l = self.get_keywords(k)
      l.sort()
      result[k] = l
    return result