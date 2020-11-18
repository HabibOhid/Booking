# This file is also for mapping
from user import User
from rooms import Room
from booking import Booking
import datetime
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost/")

mydb = myclient["roomservices"]

# Create room collection
# mydb.create_collection("rooms")

# Create uer collection
# mydb.create_collection("users")

# Create bookings collection
# mydb.create_collection("bookings")

roomsCollection = mydb.get_collection("rooms")
userCollection = mydb.get_collection("users")
bookingCollection = mydb.get_collection("bookings")

fromDate = "2020, 10, 15"
toDate = "2020, 10, 25"

# USER
user1 = User("Habiba", "Thailand", "BB45ER", "FEMALE")

# ROOM
room1 = Room("Male Dorm", "MALE", 4)
room2 = Room("Female Dorm", "FEMALE", 4)
room3 = Room("Double Room", "DOUBLE", 1)
room4 = Room("Single Room", "SINGLE", 2)

# BOOKING
booking1 = Booking(fromDate, toDate, room1, user1)

# roomDb1 = {"name": room1.name, "roomType": room1.roomType,
#            "quantity": room1.quantity}
# roomDb2 = {"name": room2.name, "roomType": room2.roomType,
#            "quantity": room2.quantity}
# roomDb3 = {"name": room3.name, "roomType": room3.roomType,
#            "quantity": room3.quantity}
# roomDb4 = {"name": room4.name, "roomType": room4.roomType,
#            "quantity": room4.quantity}


# roomdbdat1 = mydb.get_collection("rooms").insert_many(
#     [roomDb4, roomDb3, roomDb2, roomDb1])


# print(roomdbdat1)
# print(booking1.roomBooked.roomInfo())


# rooms = mydb.get_collection("rooms").find()
# for room in rooms:
#     print(room)


# gender = "MALE"

# newRoomDocs = mydb.get_collection("rooms").find({"roomType": {"$ne": gender}})
# for room in newRoomDocs:
#     print(room)

gender = "MALE"


def filterRooms(gender):
    newRoomDocs = mydb.get_collection(
        "rooms").find({"roomType": {"$ne": gender}})
    return newRoomDocs


# User clicks male or female
availableRoomsForBooking = filterRooms(gender)
# for room in availableRoomsForBooking:
#     print(room)


# User sellects a room
# Get room ID
roomID = "5fa92ae8dc88193de298a307"

# Verify room availability


def isRoomAvailable(roomType):
    roomFound = roomsCollection.find_one(
        {"roomType": roomType})
    # Check quantity
    if(roomFound["quantity"] > 0):
        return True
    return False


isAvailable = isRoomAvailable(roomID)
if(isAvailable):
    # Room is available and now we do booking and save user info as well
    userInfo = user1.__dict__
    roomInfo = roomsCollection.find_and_modify(
        {"_id": ObjectId("5fa92ae8dc88193de298a307")}, {"$inc": {"quantity": -1}})

    if(roomInfo["quantity"] == 0):
        roomsCollection.find_and_modify(
            {"_id": ObjectId("5fa92ae8dc88193de298a307")}, {"$set": {"quantity": 0}})

    bookingInfo = {"fromDate": fromDate, "toDate": toDate,
                   "roomBooked": roomInfo, "userInfo": userInfo}
    userCollection.insert_one(userInfo)
    bookingCollection.insert_one(bookingInfo)
else:
    print("This room is already fullly booked")
