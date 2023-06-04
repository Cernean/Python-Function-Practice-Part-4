def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(75,5,90))
print(max_num(14,69,7))


def mult_list(lst):
  if len(lst) == 0:
    return 0

  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i
  return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([20]))


def rev_string(my_str):
  return my_str[::-1]

print(rev_string(""))
print(rev_string("cloud"))
print(rev_string("mt string"))



def num_within(a, b, c):
  return a in range(b,c+1)
     
print(num_within(1,2,3))     
print(num_within(3,2,1))     
print(num_within(6,7,8))



triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(2)
pascal(5)