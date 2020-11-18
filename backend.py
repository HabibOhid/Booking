import pymongo

myclient = pymongo.MongoClient("mongodb://localhost/")
mydb = myclient["roomservices"]

# Uncomment and run these lines of code to create the mongoDb database Collections
# Create room collection
# mydb.create_collection("rooms")

# Create user collection
# mydb.create_collection("users")

# Create bookings collection
# mydb.create_collection("bookings")

# SEED
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

rooms = mydb.get_collection("rooms")
users = mydb.get_collection("users")
bookings = mydb.get_collection("bookings")


def isAvailable(name):
    roomAvailable = rooms.find_one({"name": name})
    if(roomAvailable and roomAvailable["quantity"] > 0):
        return roomAvailable
    return None


def create_booking(booking):
    return bookings.insert_one(booking)


def update_room(foundRoom):
    rooms.find_and_modify({"_id": foundRoom["_id"]}, {
        "$inc": {"quantity": -1}})


def create_user(newUser):
    users.insert_one(newUser)


def get_bookings():
    return bookings.find()


def search_booking_by_user(user):
    return bookings.find_one(user)
