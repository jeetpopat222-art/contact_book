import sys

print("1.check contact")
print("2.add contact")
print("3.search contact")
print("4.delet contact")
print("5.exit")



def check_contact():
        f = open("contact.txt","r")
        read = f.readlines()
        for line in read:
            print(line)
            f.close()

def add_contact():    
            with open("contact.txt","a") as a:
                ask_name = input("enter name: ").lower()
                ask_number = (input("enter nunmber: "))
                append = a.write(ask_name)
                append1 = a.write(f",{ask_number}\n")


def search_contact():
       with open("contact.txt")as f:
              number = f.readlines()
              name = input("enter name to find number: ")
              if name not in number:
                     print("invalid name !!")
              for line in number:
                      if name in line:
                             print(line)
              
                     
def delet_contact():
       with open("contact.txt", "r+") as f:
              read = f.readlines()
              
              name = input("enter name that you want to delete: ")
              if name not in read:
                     print("invalid name !!")
                     sys.exit()
              
              print("1.are you sure you want to delete:")
              print("2.no i dont want to delete")
              ask = int(input("enter your command: "))
              if ask == 2:
                     sys.exit()
              else:
                        lines = []
                        for line in read:
                            
                            
                            


                            if name not in line:
                                    lines.append(line)
                                    with open("contact.txt", "w") as f:                             
                                        f.writelines(lines)
                        else:
                               pass
                               
                     
              
            

ask = int(input("enter your mode: "))
if ask == 1:
      check_contact()

elif ask == 2:
        add_contact()
     
elif ask == 3:
       search_contact()

elif ask == 4:
       delet_contact()

elif ask == 5:
       sys.exit
       