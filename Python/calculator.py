import re
print("Magical Calculetar ")
print("type 'quit' to exit")



priv = 0
run = True

def primeth():
    global run
    global priv
    eq=''
    if priv == 0:
      
      eq=input("entar value :")
    else:
       eq=input(str(priv))  
    if eq == quit:
       run = False
    else:
       eq= re.sub('[a-zA-Z,:;()" "]','',eq)
       if priv == 0:
           priv = eval(eq)
       else:
            priv = eval(str(priv)+eq) #for add last ans 

            print("your ans is :",priv)

while run:
     primeth()

