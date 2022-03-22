# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with fav_color

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Alice",  
               "LastName": "Tang",  
               "DOB": "January 30",  
               "Residence": "San Diego",  
               "Email": "alicet46617@stu.powayusd.com",  
               "fav_color":["blue","white","purple"]  
              })  

InfoDb.append({  
               "FirstName": "Aliya",  
               "LastName": "Tang",  
               "DOB": "November 8",  
               "Residence": "San Diego",  
               "Email": "aliyat46616@stu.powayusd.com",  
               "fav_color":["blue","green","yellow"]  
              }) 
InfoDb.append({  
               "FirstName": "Alicia",  
               "LastName": "Ji",  
               "DOB": "December 11",  
               "Residence": "San Diego",  
               "Email": "aliciaj20384@stu.powayusd.com",  
               "fav_color":["orange","red","yellow"]  
              }) 
InfoDb.append({  
               "FirstName": "Aishani",  
               "LastName": "Vora",  
               "DOB": "November 7",  
               "Residence": "San Diego",  
               "Email": "aishaniv03957@stu.powayusd.com",  
               "fav_color":["black","brown","yellow"]  
              }) 

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Color: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["fav_color"]))  # join allows printing a string list with separator
    print()