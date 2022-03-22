InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Name": "Luca",  
               "Nickname": "Fatty shat",  
               "Animal": "Domestic short hair cat",    
               "Likes":["Meowing" , "Sleeping" , "Treats" , "Cuddling", "Scratching"]  
              })  

InfoDb.append({  
               "Name": "Apollo",  
               "Nickname": "Binger shat",  
               "Animal": "Domestic short hair cat",    
               "Likes":["Staring" , "Sleeping" , "Sniffing"]    
              })  

InfoDb.append({  
               "Name": "Bella",  
               "Nickname": "Bug",  
               "Animal": "French Bulldog",    
               "Likes":["Barking" , "Chasing" , "Treats" , "Running"]   
              })  

InfoDb.append({  
               "Name": "Spotus",  
               "Nickname": "Spoot",  
               "Animal": "African Grey Parrot",    
               "Likes":["Flying" , "Talking" , "Toys" , "Nuts", "Dancing", "Music"]    
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Name"]) 
    print("\t", "Nickname: ", end="") 
    print(InfoDb[n]["Nickname"]) 
    print("\t", "Animal: ", end="") 
    print(InfoDb[n]["Animal"]) 
# using comma puts space between values
    print("\t", "Likes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Likes"]))  # join allows printing a string list with separator
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