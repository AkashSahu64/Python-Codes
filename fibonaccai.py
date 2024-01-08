def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
t = int(input("Enter number of terms of fibonaccai series : "))   
if t <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(t):  
       print(recur_fibo(i),end=' ')  