#Program to display the Fibonacci sequence

nterms = int(input("How many terms?"))
# first two terms
n1,n2 =0,1
count=0
# check if the number of terms is valid
if nterms<=0:
    print("Please enter a positive integer")
# if there is only n terms then return n1
elif nterms==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
#Generate Fibonacci sequence
else :
    print("Fibonacci sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        #update value
        n1=n2
        n2=nth
        count+= 1
