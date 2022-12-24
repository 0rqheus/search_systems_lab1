import time
from tests.mocks.docs import docs
from src.forward_index import ForwardIndex
from src.inverted_index import InvertedIndex

def main():
  target = input('Enter keyword to search: ')

  start = time.time()
  find_in_forward(target)
  end = time.time()
  print(f'forward indexing speed ${end-start}')

  start = time.time()
  find_in_inverted(target)
  end = time.time()
  print(f'inverted indexing speed ${end-start}')

def find_in_forward(target: str):
  forward_index = ForwardIndex(docs)
  forward_results = forward_index.run()
  for k, v in forward_results.items():
    if target in v:
      print('[forward]: success', k)
      return
  print('[forward] fail')

def find_in_inverted(target: str) :
  inverted_index = InvertedIndex(docs)
  inverted_results = inverted_index.run()
  if inverted_results[target]:
    print('[inverted]: success', inverted_results[target])
  else:
    print('[inverted]: failt')

main()