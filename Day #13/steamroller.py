## Test cases:  
## [1, {}, [3, [[4]]]]
## [[["a"]], [["b"]]]
## [1, [], [3, [[4]]]]
## [1, [2], [3, [[4]]]]

def main():
  arr = [1, {}, [3, [[4]]]]
  final_arr = []
  flatten(arr, final_arr)
  print(final_arr)

def flatten(arr, final_arr):
  for e in arr:
    if not isinstance(e, list):
      print(e)
      final_arr.append(e)
    else:
      print(e)
      flatten(e,final_arr)
  

if __name__ == '__main__':
  main()