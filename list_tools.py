import math

def mean(input):

  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))

def median(input):
  if len(input) == 0:
    return 0
  mid_index = math.floor(len(input) / 2)

  if len(input) % 2 == 0:
    return (input[mid_index - 1] + input[mid_index]) / 2
  else:
    return input[mid_index]

my_list = [1, 2, 3, 9, 4, 10]

print(median(my_list))
