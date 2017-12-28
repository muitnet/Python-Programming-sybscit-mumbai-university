def Armstrong_no(x):
	no=x 
	sum=0
	while no>0: 
	   R=no%10
	   sum=sum+(R*R*R)
	   no=no//10
	if num==sum:
	   print(num,"is an Armstrong number")
	else:
	   print(num,"is not an Armstrong number")
	   
def Palindrome(Number):
        n=Number
        Reverse=0
        while n>0:
            Reminder=n%10
            Reverse=(Reverse*10)+Reminder
            n=n//10
        if(Number==Reverse):
                print(Number,'is a palindrome number')
        else:
                print(Number,'is not a palindrome number')

num=int(input("Enter a number: "))
Armstrong_no(num)
Palindrome(num)
