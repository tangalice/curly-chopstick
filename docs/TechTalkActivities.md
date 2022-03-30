{% include navigation.html %}

## Tech Talk Activites

### Week 2 Activites
Key Learning: I learned about classes and OOP method in coding. More specifically, I learned how to code a program that finds the factors of any number.

We made a factorial function using classes
```
class Factorial:
    def findFact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

def factorial():
  print("Enter a Number: ", end="")
  num = int(input())
  ob = Factorial()
  print("\nFactorial of", num, "=", ob.findFact(num))

if __name__ == "__main__":
    factorial()
   
   ```
 The last line of code calls the function.

### Week 1 Activites
Key Learning: I learned about lists and using loops to print the information inside of lists. Using loops is a more effecient way to print everything espeically if you have a lot of information where there are lists inside of lists. I also learned how to troubleshoot a replit page after a week of it not running. I had to reclone my github repo and make sure that I had the language set to python3 before making a new repl.

We learned how to make loops in 3 ways (for, while and recursive) when accessing an InfoDB with a list within a list.
- A recursive loop calls itself multiple times until the return or exit condition is reached.

```
def for_loop():
  for n in range(len(InfoDb)):
    print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop0(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop0(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop0(n + 1)
  return # exit condition
  ```

### Week 0 Activites
Key Learning: I learned how to "animate something" with the use of funcation, variables and print statements. I also learned how to make a menu <br>

[Replit](https://replit.com/@alicet1/alice-individual#main.py) <br>
<iframe height="900px" width="700px" src="https://replit.com/@alicet1/curly-chopstick?lite=true#main.py"></iframe>


