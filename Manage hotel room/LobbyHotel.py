
from hotel import HotelData

f = open('room.txt','r')
s = f.read()
Ls = s.split(',')

ar = HotelData()

for data in Ls:
    ar.insertR(str(data))
    ar.insertR2(str(data))    

while True  :
    
    print('\n')
    ans = str(input("1.Check in\n2.Check out\n3.Check Room\n4.Check user\n\nChoose the list you want : " ))

    if ans in ar.checkin :
        
        UserNamein = str(input("Please Enter your name to check in : "))
        
        print("\nWelcome , " + UserNamein )
        print('The room type is defined by the letters in front of the room number.\n')
        print(ar.Room)
        print('\n')

        while True :
            Roomchoose = str(input("Choose your room : "))
            if Roomchoose in ar.Room :
            
                usersure = str(input("Confirm selection?\nplease type 'Y' or 'N' : " ))

                if usersure in ar.Yy :
                        ar.deleteR(Roomchoose)
                        ar.insert(UserNamein,Roomchoose)
                        ar.insertD(UserNamein)
                        ar.insertU(Roomchoose)
                        print('\n')
                        print(ar.data)
                        print(ar.Room)
                        break
                
                else : 
                    print('If you want to confirm please type Y')
                    pass
                
            
            elif Roomchoose in ar.STOP :
                print('You stop working\nRetry again')
                break

            else :
                print('There is no room you selected.\nplease choose again\n')
                pass 
        
    
    
    elif ans in ar.checkout :
        
        while True :
            UserNameout = str(input("Enter user name : "))
            
            if UserNameout in ar.data1:
                IdexUserInRoom = ar.search(UserNameout)
                RoomUser = []
                #if SearchUserInRoom in ar.idexUser :
        
                if (0,0) == IdexUserInRoom:
                    RoomUser = (ar.data[0][1])
                
                if (1,0) == IdexUserInRoom:
                    RoomUser = (ar.data[1][1])

                if (2,0) == IdexUserInRoom:
                    RoomUser = (ar.data[2][1])

                if (3,0) == IdexUserInRoom:
                    RoomUser = (ar.data[3][1])

                if (4,0) == IdexUserInRoom:
                    RoomUser = (ar.data[4][1])

                if (5,0) == IdexUserInRoom:
                    RoomUser = (ar.data[5][1])

                if (6,0) == IdexUserInRoom:
                    RoomUser = (ar.data[6][1])

                if (7,0) == IdexUserInRoom:
                    RoomUser = (ar.data[7][1])

                if (8,0) == IdexUserInRoom:
                    RoomUser = (ar.data[2][1])

                if (3,0) == IdexUserInRoom:
                    RoomUser = (ar.data[8][1])

                if (9,0) == IdexUserInRoom:
                    RoomUser = (ar.data[9][1])

                if (10,0) == IdexUserInRoom:
                    RoomUser = (ar.data[10][1])

                if (11,0) == IdexUserInRoom:
                    RoomUser = (ar.data[11][1])

                if (12,0) == IdexUserInRoom:
                    RoomUser = (ar.data[12][1])

                if (13,0) == IdexUserInRoom:
                    RoomUser = (ar.data[13][1])

                if (14,0) == IdexUserInRoom:
                    RoomUser = (ar.data[14][1])

                if (15,0) == IdexUserInRoom:
                    RoomUser = (ar.data[15][1])

                if (16,0) == IdexUserInRoom:
                    RoomUser = (ar.data[16][1])

                if (17,0) == IdexUserInRoom:
                    RoomUser = (ar.data[17][1])

                if (18,0) == IdexUserInRoom:
                    RoomUser = (ar.data[18][1])

                if (19,0) == IdexUserInRoom:
                    RoomUser = (ar.data[19][1])

                if (20,0) == IdexUserInRoom:
                    RoomUser = (ar.data[20][1])

                if (21,0) == IdexUserInRoom:
                    RoomUser = (ar.data[21][1])

                if (22,0) == IdexUserInRoom:
                    RoomUser = (ar.data[22][1])

                if (23,0) == IdexUserInRoom:
                    RoomUser = (ar.data[23][1])

                if (24,0) == IdexUserInRoom:
                    RoomUser = (ar.data[24][1])

                if (25,0) == IdexUserInRoom:
                    RoomUser = (ar.data[25][1])
                # UserRoom = str(input("Enter your number room : ")) 
                #if UserRoom in ar.RoomUse :

                ar.insertR(RoomUser)
                ar.delete([UserNameout,RoomUser])
                ar.deleteD(UserNameout)
                ar.deleteU(RoomUser)
                print(ar.data)
                print('\n')
                print(ar.Room)
                print('\n\n')
                break
            
            elif UserNameout in ar.STOP:
                    break          

            else : 
                print('not found user name\nPlease try again')
                pass

    elif ans in ar.checkroom :
        print('\n')
        print(ar.Room)
        print("\nIt's a room that's still available.")

    
    elif ans in ar.checkuser :
        
        SearchUserInRoom = ar.search(str(input('searchUser : ')))

        if SearchUserInRoom in ar.idexUser :
        
            if (0,0) == SearchUserInRoom:
                print(ar.data[0][1])
            

            if (1,0) == SearchUserInRoom:
                print(ar.data[1][1])

            if (2,0) == SearchUserInRoom:
                print(ar.data[2][1])

            if (3,0) == SearchUserInRoom:
                print(ar.data[3][1])

            if (4,0) == SearchUserInRoom:
                print(ar.data[4][1])

            if (5,0) == SearchUserInRoom:
                print(ar.data[5][1])

            if (6,0) == SearchUserInRoom:
                print(ar.data[6][1])

            if (7,0) == SearchUserInRoom:
                print(ar.data[7][1])

            if (8,0) == SearchUserInRoom:
                print(ar.data[2][1])

            if (3,0) == SearchUserInRoom:
                print(ar.data[8][1])

            if (9,0) == SearchUserInRoom:
                print(ar.data[9][1])

            if (10,0) == SearchUserInRoom:
                print(ar.data[10][1])

            if (11,0) == SearchUserInRoom:
                print(ar.data[11][1])

            if (12,0) == SearchUserInRoom:
                print(ar.data[12][1])

            if (13,0) == SearchUserInRoom:
                print(ar.data[13][1])

            if (14,0) == SearchUserInRoom:
                print(ar.data[14][1])

            if (15,0) == SearchUserInRoom:
                print(ar.data[15][1])

            if (16,0) == SearchUserInRoom:
                print(ar.data[16][1])

            if (17,0) == SearchUserInRoom:
                print(ar.data[17][1])

            if (18,0) == SearchUserInRoom:
                print(ar.data[18][1])

            if (19,0) == SearchUserInRoom:
                print(ar.data[19][1])

            if (20,0) == SearchUserInRoom:
                print(ar.data[20][1])

            if (21,0) == SearchUserInRoom:
                print(ar.data[21][1])

            if (22,0) == SearchUserInRoom:
                print(ar.data[22][1])

            if (23,0) == SearchUserInRoom:
                print(ar.data[23][1])

            if (24,0) == SearchUserInRoom:
                print(ar.data[24][1])

            if (25,0) == SearchUserInRoom:
                print(ar.data[25][1])
        
        else : 
            print('not found user name')

        

    elif ans in ar.STOP : 
        print('Stop working')
        break

    else : 
        print('invalid input\nPlease try again \n///////////////////\n\n')
        continue

