# For project mapping
class Room:
    def __init__(self, name, roomType, quantity):
        self.name = name
        self.roomType = roomType
        self.quantity = quantity

    def roomInfo(self):
        print("Room info Name:" + self.name + " Type: " + self.roomType)
