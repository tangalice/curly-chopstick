# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Common_Name": "Fennec Fox",  
               "Scientific_Name": "Vulpes Zerda",  
               "Conservation_Status": "Least Concern",    
               "Preferred_Foods":["Grasshoppers" , "Lizards" , "Birds" , "Eggs" , "Fruits" , "Leaves"]  
              })  

InfoDb.append({  
               "Common_Name": "Ground Squirrel",  
               "Scientific_Name": "Spermophilus Richardsonii",  
               "Conservation_Status": "Least Concern",    
               "Preferred_Foods":["Seeds" , "Nuts" , "Corn" , "Fruit" , "Leaves" , "Fungi" , "Bark"]   
              })  

InfoDb.append({  
               "Common_Name": "Alpine Ibex",  
               "Scientific_Name": "Capra Ibex",  
               "Conservation_Status": "Least Concern",    
               "Preferred_Foods":["Grasses", "Mosses" , "Flowers" , "Leaves" , "Twigs"]   
              })  

InfoDb.append({  
               "Common_Name": "Dormouse",  
               "Scientific_Name": "Gliridae",  
               "Conservation_Status": "Least Concern",    
               "Preferred_Foods":["Fruit" , "Hazelnuts" , "Acorns" , "Pine Seeds" , "Bark", "Eggs"]   
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Common_Name"]) 
    print(InfoDb[n]["Scientific_Name"]) 
    print("\t", "Conservation Status: ", end="") 
    print(InfoDb[n]["Conservation_Status"]) 
# using comma puts space between values
    print("\t", "Preferred Foods: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Preferred_Foods"]))  # join allows printing a string list with separator
    print()

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

def while_loop():
  while_loop0(0)

def recursive_loop():
  recursive_loop0(0)
  
if __name__ == "__main__":
    for_loop()
    while_loop()
    recursive_loop()