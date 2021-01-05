def remove_duplicates(arr):
  if len(arr) == 1:
    return 1
  i = 0
  j = 1
  num_distinct_elms = 1
  while not j>len(arr)-1:
    if arr[i] == arr[j]:
      j+=1
    else:
      arr[i+1] = arr[j]
      num_distinct_elms+=1
      i = j
      j = i+1
    print(arr)
  print(arr[0:num_distinct_elms])
  return num_distinct_elms

remove_duplicates([2, 3, 3, 3, 6, 9, 9])