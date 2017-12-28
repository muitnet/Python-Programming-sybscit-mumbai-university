dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
print("dic1 :",dic1)
print("dic2 :",dic2)
print("dic3 :",dic3)
for i in (dic1,dic2,dic3):
	dic4.update(i)
print("after concatenate dic1,dic2,dic3 :")
print(dic4)
