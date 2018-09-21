
print("----assesement----")
lis = ['a','b','c','d','e',0,1,0,0,'f','g','h',False,False,'i','j']

num = []
str_list = []
whole = 0
for i in range (lis.__len__()):
    
        #lis.pop(i)     

        if type(lis[i]) == int:
            int_lis = lis[i]
            num.insert(i, int_lis)
            #print("======")
            #print(num)
            #lis.pop(lis[i])

        if type(lis[i]) == str:
            str_lis =lis[i]
            #print("-------") 
            str_list.insert(i, str_lis)           
            #print( lis.__len__())
            #print(i + 1 == lis.__len__())
            whole = i + 1
            #print("oikn", whole)

        if type(lis[i]) == bool  :
            str_lis = lis[i]
            str_list.append(str_lis)
            #print(str_list)
            #print("=======")
            

        if whole == lis.__len__():
            str_list.append(num)
            print("sorted list")
            print(str_list)
        
        