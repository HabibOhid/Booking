from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend import create_booking, create_user, isAvailable, get_bookings, update_room, search_booking_by_user

# MAIN ROOT SETUP
root = Tk()
root.title("BOOKINGS")


# FUNCTIONS


def quite():
    root.destroy()


def clear_entries():
    name_entry.delete(0, END)
    passport_entry.delete(0, END)
    country_entry.delete(0, END)
    fromDate_entry.delete(0, END)
    toDate_entry.delete(0, END)


def book_now():
    accomodationType = variable.get()
    userName = name_entry.get()
    userpassport = passport_entry.get()
    userCountry = country_entry.get()
    userGender = user_g.get()
    fromDate = fromDate_entry.get()
    toDate = toDate_entry.get()
    foundRoom = isAvailable(accomodationType)

    # print(foundRoom)
    if(foundRoom):
        newUser = {"name": userName, "country": userCountry,
                   "passport": userpassport, "gender": userGender}
        roomInfo = {"_id": foundRoom["_id"], "name": foundRoom["name"],
                    "roomType": foundRoom["roomType"]}
        print(roomInfo)
        newBooking = {"fromDate": fromDate, "toDate": toDate,
                      "roomBooked": roomInfo, "userInfo": newUser}
        bookingSuccess = create_booking(newBooking)

        if(bookingSuccess):
            update_room(foundRoom)
            create_user(newUser)
            messagebox.showinfo("Booking Completed",
                                "Booking was done successfully")
        clear_entries()
    else:
        messagebox.showwarning("Failed process",
                               "Room is already Fully Booked")


def search_entry():
    currentData = displaydata.get(ACTIVE)
    booking_found = search_booking_by_user(currentData)
    print(booking_found)
    print("SEARCH clicked")


def view_all_entries():
    booking_list = get_bookings()
    for item in booking_list:
        bookingInfo = "Room booked: {} - from {} to {} User: {} ".format(item["roomBooked"]["name"],
                                                                         item["fromDate"], item["toDate"], item["userInfo"]["name"])
        displaydata.insert(END, bookingInfo)
    print("VIEW ALL ENTRIES clicked")


def update_data():
    print("UPDATE clicked")


def view_entry():
    print("VIEW")


def gender_selected():
    filteredOPTIONS = OPTIONS.copy()
    print("GENDER SELECTED")
    user_gender = gender_entry.get()
    if(user_gender == 1):
        filteredOPTIONS.remove("Female Dorm")
        user_g.set("Male")
    else:
        filteredOPTIONS.remove("Male Dorm")
        user_g.set("Female")
    accomodation_type_list = OptionMenu(
        root, variable, *filteredOPTIONS).grid(row=3, column=1)
    print(filteredOPTIONS)
    print(OPTIONS)


# Creating label
name = Label(root, text="Name")
name.grid(row=0, column=0)
country = Label(root, text="Country")
passport = Label(root, text="Passport Number")
fromDate = Label(root, text="From >>format: year, month, day")
toDate = Label(root, text="To >>format: year, month, day")
gender = Label(root, text="Gender")
acco = Label(root, text="Accomodation Type")


# creating text area
booking_list = []


displaydata = Listbox(root, width=100)


displaydata.grid(row=5, columnspan=3)

# Creating entry
name_entry = Entry(root, width=50,)
passport_entry = Entry(root, width=50, )
country_entry = Entry(root, width=50, )
fromDate_entry = Entry(root, width=50, )
toDate_entry = Entry(root, width=50,)

user_g = StringVar()


# creating button
book_now = Button(root, text="Book Now", command=book_now, padx=50)
search_entry = Button(root, text="Search Entry", command=search_entry).grid(
    row=5, column=3, sticky=N)
update_entry = Button(root, text="Update Entry", command=update_data).grid(
    row=5, column=3, sticky=W)
view_entry = Button(root, text="View All Entries",
                    command=view_all_entries).grid(row=5, column=3, sticky=E)
delete_entry = Button(root, text="Delete selected entry",
                      command=lambda displaydata=displaydata: displaydata.delete(ANCHOR)).grid(row=5, column=3, sticky=S)
quit_application = Button(root, text="Quit Application", command=quite).grid(
    row=6, column=3, sticky=S)

gender_entry = IntVar()
# Radio button
male = Radiobutton(root, text="Male", variable=gender_entry,
                   value=1, command=gender_selected)
female = Radiobutton(root, text="Female",
                     variable=gender_entry, value=2, command=gender_selected)


name_entry.grid(row=0, column=1)
country.grid(row=0, column=2)
country_entry.grid(row=0, column=3)
passport.grid(row=1, column=0)
passport_entry.grid(row=1, column=1)
gender.grid(row=1, column=2)
male.grid(row=1, column=3)
female.grid(row=1, column=4)
fromDate.grid(row=2, column=0)
fromDate_entry.grid(row=2, column=1)
toDate.grid(row=2, column=2)
toDate_entry.grid(row=2, column=3)
acco.grid(row=3, column=0)
book_now.grid(row=3, column=3)

OPTIONS = [
    "Single Room",
    "Double Room",
    "Male Dorm",
    "Female Dorm",
]


variable = StringVar(root)
variable.set("Select Room Type")  # default value
filteredOPTIONS = ["", ]

accomodation_type_list = OptionMenu(
    root, variable, *filteredOPTIONS).grid(row=3, column=1)

root.mainloop()
