from src.base_index import BaseIndex

class InvertedIndex(BaseIndex):
  def run(self):
    result = {}
    for k in self.docs.keys():
      l = self.get_keywords(k)
      for word in l:
        if word in result:
          result[word].append(k)
        else:
          result[word] = [k]
    return result