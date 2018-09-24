#Dog class
class Dog:

    is_hungry = True

    def eat(self,val):
       is_hungry = val
    
       if is_hungry == "True":
           return True
       elif is_hungry == "False":
           return False

    def walk(self):
        print("Dog walking")
               


#pet class
class pet:

     def walk(self):
        print("pet Dog class")

if __name__ == "__main__":
   
    dog1 = Dog()
    dog2 = Dog()
    dog3 = Dog()

    print("I have 3 dogs")
    print("Tom is 6")
    print("Flectcher is 7")
    print("Larry is 9")
    print("And they're all mammals, of course")
    Dog_Qn = input("Are the dogs hungry ?  True or False : ")
    
    if Dog_Qn == "True":
        Eat_return = dog1.eat(Dog_Qn)
        Eat_return = dog2.eat(Dog_Qn)
        Eat_return = dog3.eat(Dog_Qn)
        print("--------------------")
        if Eat_return and Eat_return and Eat_return:
            print("My Dog are Hungry")

    elif Dog_Qn == "False":
        Eat_return = dog1.eat(Dog_Qn)
        Eat_return = dog2.eat(Dog_Qn)
        Eat_return = dog3.eat(Dog_Qn)
        
        print("--------------------")
        if not Eat_return  and not Eat_return and not Eat_return:
            print("My Dog are not Hungry")

