from src.forward_index import ForwardIndex
from mocks.docs import docs

def test_forward_indexing():
  forward_index = ForwardIndex(docs)
  results = forward_index.run()

  assert results["doc1"] == ["Come", "to", "think", "about", "it", "it's", "all", "in", "my", "head", "I'm", "praying", "for", "a", "green", "light", "looking", "straight", "ahead", "I", "had", "God", "stuck", "between", "hands"]
  assert results["doc2"] == ["They", "say", "they", "saw", "him", "with", "a", "gun", "think", "he'll", "stop", "but", "don't", "know"]
  assert results["doc3"] == ["Death", "before", "your", "eyes", "you", "praying", "to", "God", "but", "ain't", "no", "response"]