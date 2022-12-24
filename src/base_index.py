import re

class BaseIndex:
  def __init__(self, docs: dict[str, str]):
    self.docs = docs

  def get_keywords(self, doc_key):
    return list(set(re.findall("\w+'?\w+", self.docs[doc_key])))