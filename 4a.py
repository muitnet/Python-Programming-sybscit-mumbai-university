def list_function(a,b):
	for i in a:
		if i in b:
			print("True")
			break
			
list1=[1,2,3,4,5]
list2=[1,2,3,6,7,8]
list_function(list1,list2)
