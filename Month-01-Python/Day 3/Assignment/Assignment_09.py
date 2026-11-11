my_list = [10, 66, 54, 99]

if my_list:
  largest = my_list[0]

  for num in my_list:
    if num > largest:
      largest = num

  print(largest) 

print(max(my_list)) #Using Max Function