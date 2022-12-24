from src.inverted_index import InvertedIndex
from mocks.docs import docs

def test_inverted_indexing():
  inverted_index = InvertedIndex(docs)
  results = inverted_index.run()

  assert results["head"] == ["doc1"]
  assert results["think"] == ["doc1", "doc2"]
  assert results["praying"] == ["doc1", "doc3"]
  assert results["but"] == ["doc2", "doc3"]