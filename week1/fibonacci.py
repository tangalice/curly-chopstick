# Program to display the Fibonacci sequence up to n-th term
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Formatting and printing of the Fibonacci
def fibonacci():
  nterms = int(input("How many terms? "))
  if nterms <= 0:
     print("Plese enter a positive integer")
  else:
     print("Fibonacci sequence:")
     for i in range(nterms):
         print(recur_fibo(i))

if __name__ == "__main__":
    fibonacci()