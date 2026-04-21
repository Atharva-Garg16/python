n=int(input("enter number of terms\n"))
Sum=0
fibo=0
firstTerm=1
SecondTerm=1
print(1,1,end=" ")
for x in range(1,n):
    fibo=firstTerm+SecondTerm
    firstTerm=SecondTerm
    SecondTerm=fibo
    print(fibo,end=" ")
