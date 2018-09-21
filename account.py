accounts = {}

def add_account(Name,Password):

    accounts[Password] = Name     
        

def login(name,password):
    for k,v in accounts.items():
        #print(k,v)
        #print(accounts.__contains__(k))
        if k == password and v == name  :
            return True
        
#add_account("Ochom","Isaac")
#print(login("Ochom","Isaac"))
