from operator import index


class HotelData():
    def __init__(self): 
        self.printz()
        self.idexUser=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0),(25,0)]
        self.data = []
        self.data1 = []
        self.RoomUse = []
        self.Room = []
        self.Roomcheck = []
        self.checkin = ['checkin','Check in','1','check in']
        self.checkout = ["checkout","Check out","2","check out","CHECK OUT","CHECKOUT"]
        self.checkroom = ['3',"Checkroom","check room","CheckRoom","CHECK ROOM","CHECKROOM"]
        self.checkuser = ['checkuser','Check user','Checkuser','4','check user']
        self.STOP = ['STOP','stop']
        self.Yy = ['Y','y','yes','Yes']
        
    def insertR2(self,addData,index=-1):
        if index == -1:
            self.Roomcheck.append(addData)
        else:
            print("add by index")
            data_last = self.Roomcheck[len(self.Roomcheck)-1]
            self.Roomcheck.append(data_last)

            for i in range(len(self.Roomcheck)-1,index,-1):
                self.Roomcheck[i] = self.Roomcheck[i-1]  
            self.Roomcheck[index] = addData

    def insert(self,addData,AddData,index=-1):
        if index == -1:
            self.data.append([addData,AddData])
        else:
            print("add by index")
            data_last = self.data[len(self.data)-1]
            self.data.append(data_last)

            for i in range(len(self.data)-1,index,-1):
                self.data[i] = self.data[i-1]  
            self.data[index] = addData         

    def search(self,data):
        for i, x in enumerate(self.data):
            if data in x:
                return i , x.index(data)
        return -1
      
    def delete(self,data,):
        for i in range(len(self.data)-1):
            if self.data[i] == data:
        
               self.data.pop(i)

#######################################################################################

    def insertD(self,adddata1,index=-1):
        if index == -1:
            self.data1.append(adddata1)
        else:
            print("add by index")
            data1_last = self.data1[len(self.data1)-1]
            self.data1.append(data1_last)

            for i in range(len(self.data1)-1,index,-1):
                self.data1[i] = self.data1[i-1]  
            self.data1[index] = adddata1

    def deleteD(self,data1):
        for i in range(len(self.data1)-1):
            if self.data1[i] == data1:
        
               self.data1.pop(i)  

    def insertU(self,addData,index=-1):
        if index == -1:
            self.RoomUse.append(addData)
        else:
            print("add by index")
            RoomUse_last = self.RoomUse[len(self.RoomUse)-1]
            self.RoomUse.append(RoomUse_last)

            for i in range(len(self.RoomUse)-1,index,-1):
                self.RoomUse[i] = self.RoomUse[i-1]  
            self.RoomUse[index] = addData

    def deleteU(self,data1):
        for i in range(len(self.RoomUse)-1):
            if self.RoomUse[i] == data1:
        
               self.RoomUse.pop(i) 

    def insertR(self,addRoom,index=-1):
        if index == -1:
            self.Room.append(addRoom)
        else:
            print("add by index")
            Room_last = self.Room[len(self.Room)-1]
            self.Room.append(Room_last)

            for i in range(len(self.Room)-1,index,-1):
                self.Room[i] = self.Room[i-1]  
            self.Room[index] = addRoom         
        
    def searchR(self,Room):
        for i in range(len(self.Room)-1):
            if self.Room[i] == Room:
                return i
        return -1

    def deleteR(self,Room):
        for i in range(len(self.Room)-1):
            if self.Room[i] == Room:
        
               self.Room.pop(i)
    
    def printz(self):
        print('\n')
        print("How to use A hotel's system.\nFirst : Ask customers if they want to check in or check out?\nThen If the customer check in.")
        print("1.Enter customer's name and Room Type Choose by Customer.\n - Enter 'A' means Standard room.\n - Enter 'B' means Superior room.\n - Enter 'C' means Deluxe room.")
        print("2. Ask the customer for sure? (y/n)")
        print("3. If the customer replies to sure, the system will display the name, price and room number to the customer, but if the customer is not sure, the system will return to the restart.")
        print("4. System displays the number of rooms available.\n")

        print("Check out\n\n1.Enter customer's name.\n2.System displays the number of rooms available update.\n\n* Only 1 room can be booked by 1 name.\n* Customers can choose only room type but cannot choose room.\n* Customer Name must be unique.\n")

        print("------------------------------------------------------------------------")

        print("Welcome to A hotel\nPlease read details before making a reservation.\n")

        print("Information\nA type room is standard room.\n- Price 500 bath for a day.\nB type room is superior room.\n- Price 1,500 bath for a day.\nC type room is deluxe room.\n- Price 2,500 bath for a day.\n")

        print("Benefits\n-Breakfast for all room types.\n-Buffet for superior rooms and deluxe room.\n\n")
        print("------------------------------------------------------------------------\n\n")   
    

