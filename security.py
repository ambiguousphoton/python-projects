#                         o     ----------------------------------
#                    d__/'H'\__b   |  hi this program is by Vyoam |                                      
#                         V        -------------------------------
#                        / \
#                       /   |
#                     ""    ""
class secure_list:
    def __init__(self,data =None):
        self.__allowed_users = {"Ram":["mahadev",'RW'],
                                "hanuman": ["shri ram","R"],
                                "laxman":["bhrata","W"],
                                "Vyoam":["Mata","RW"]}
        self.__data = data

    def read(self,user,password):
        if user in self.__allowed_users: 
            if self.__allowed_users[user][0] == password:
                if 'R' in self.__allowed_users[user][1]:
                    print(self.__data)
                else:
                    print("no read permission !")
            else:
                print("passoword not correct !")
        else:
            print("Not authentic user !")
    
    def write(self,user,password):
        if user in self.__allowed_users:
            if self.__allowed_users[user][0] == password:  
                if "W" in self.__allowed_users[user][1]:
                    print("textmessage , list")
                    x = input("what do want to store ?")
                    if x == "textmessage":
                        s = input(" -> ",)
                        self.__data = s
                    else: 
                        print("Enter elements of list, end by -> END")
                        list1 = []
                        while True:
                            y = input()
                            if y == "END":
                                break
                            else:
                                list1.append(y)
                        
                        self.__data = list1
                else:
                    print("no write permission !")
            else:
                print("passoword not correct !")
        else:
            print("Not authentic user !") 

s = secure_list(None)

while True:
    print("<<s secured list>>")
    x = input()
    if x == "read":
        user = input("username :")
        password = input("password :")
        s.read(user,password)
    elif x=="write":
        user = input("username :")
        password = input("password :")
        s.write(user,password)
    elif x=="END":
        break




