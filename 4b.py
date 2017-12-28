list1=[10,11,12,13,44,55,66,88,25,28]
list1=[x for (i,x) in enumerate(list1) if i not in (0,2,4,5)]
print("list after removing the 0th, 2nd, 4th and 5th elements")
print(list1)
