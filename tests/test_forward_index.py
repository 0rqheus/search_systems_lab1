from src.forward_index import ForwardIndex
from mocks.docs import docs

def test_forward_indexing():
  forward_index = ForwardIndex(docs)
  results = forward_index.run()

  assert results["doc1"] == ['Come', 'God', "I'm", 'about', 'ahead', 'all', 'between', 'for', 'green', 'had', 'hands', 'head', 'in', 'it', "it's", 'light', 'looking', 'my', 'praying', 'straight', 'stuck', 'think', 'to']
  assert results["doc2"] == ['They', 'but', "don't", 'gun', "he'll", 'him', 'know', 'saw', 'say', 'stop', 'they', 'think', 'with']
  assert results["doc3"] == ['Death', 'God', "ain't", 'before', 'but', 'eyes', 'no', 'praying', 'response', 'to', 'you', 'your']