# implementing a recursive function to calculate a factorial number of a given number. 
def fac_rec(a):
 if a==0 or a==1:
   return 1
 else:
   return a*fac_rec(a-1)

number=int(input("enter a value :"))
res=fac_rec(number)

print("factorial of {} is {}.".format(number,res))
