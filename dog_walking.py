#Dog class
class Dog:
    
    def walk(self,Dog_name):
        print("%s is walking" % Dog_name)

    def sleep(self,Dog_name):
        print("%s is sleeping" % Dog_name)
         
               


#pet class
class pet:
    
    def walk(self):

        Dog_List = ['Tom','Fletcher','Larry']

        for dog_name in Dog_List:
            print(Dog().walk(dog_name))
         
    def sleep(self):

        Dog_List = ['Tom','Fletcher','Larry']

        for dog_name in Dog_List:
            print(Dog().sleep(dog_name))
         

if __name__ == "__main__":
   
    pet_ins = pet()
    print(pet_ins.walk())
    print("-----------------")
    print(pet_ins.sleep())
   