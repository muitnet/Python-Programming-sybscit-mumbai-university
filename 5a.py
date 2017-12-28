import operator
x={1:10,3:15,4:20,2:21,2:30}
print("the orignal dict is :",x)
ascending_x = sorted(x.items(), key=operator.itemgetter(0))
print("dictonary in ascending order by value :",ascending_x)
descending_x=sorted(x.items(),key=operator.itemgetter(0),reverse=True)
print("dictonary in ascending order by value :",descending_x)
