import mysql.connector as myc
import os

mydb = myc.connect(
    host = "localhost",
    user = "root",
    password = "20020503",
    database = "hms"
)

c = mydb.cursor()

def welcome():
    pass
def roomChoose():
    pass

def showTable():
    os.system("clear")
    c.execute("select * from rooms")
    print("+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
    for x in c:
        if x[2] == 1:
            if x[4] == 1:
                print(f"| id:{x[0]} - xona:{x[1]} | luxe:✅| | band:✅ | narxi:{x[3]} so'm |")
            else:
                print(f"| id:{x[0]} - xona:{x[1]} | luxe:✅| | band:❎ | narxi:{x[3]} so'm |")
        else:
            if x[4] == 1:
                print(f"| id:{x[0]} - xona:{x[1]} | luxe:❎| | band:✅ | narxi:{x[3]} so'm |")
            else:
                print(f"| id:{x[0]} - xona:{x[1]} | luxe:❎| | band:❎ | narxi:{x[3]} so'm |")
    print("+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
    print("\n\nBosh menyuga qaytasizmi >> ")
    print("1.Ha")
    print("2.Yo'q")
    menu = int(input(">>"))
    if menu == 1:
        welcome()


def freeRooms():
    c.execute("select * from rooms where busy = 0")
    print("\n----------------Bo'sh xonalar------------------\n")
    for x in c:
        if x[2] == 1:
            print(f"{x[0]} idli {x[1]} xonali lyuks raqam bo'sh\n")
        else:
            print(f"{x[0]} idli {x[1]} xonali raqam bo'sh")
def busyRooms():
    c.execute("select * from rooms where busy = 1")
    print("\n----------------Band xonalar-------------------\n")
    for x in c:
        if x[2] == 1:
            print(f"{x[0]} idli {x[1]} xonali lyuks raqam band\n")
        else:
            print(f"{x[0]} idli {x[1]} xonali raqam band")


def showUsers():
    os.system("clear")
    print("-------------------Mehmonlar-----------------------\n\n")
    c.execute("select * from guest")
    for x in c:
        print(f"id:{x[0]} | ism:{x[1]} | familiya:{x[2]} | xona:{x[4]} |")

    print("\n\nBosh menyuga qaytasizmi?\n")
    print('''
    1.Ha\n
    2.Yoq
    ''')
    choose = int(input("Amalni tanlang >> "))
    if choose == 1:
        welcome()
    else:
        exit()

def newUser(room_choose):
    print("------------------------------Band qiluvchi malumotlari--------------------")
    guest_name = input("Ismi >> ")
    guest_surname = input("Familiyasi >> ")
    guest_passport = int(input("Passport idsi >> "))
    c.execute("insert into guest (name,surname,passport_id,xona_raqam) values (%s, %s, %s, %s)",(guest_name,guest_surname,guest_passport,room_choose))


def clearUser(room_choose):
    c.execute("delete from guest where xona_raqam = %s",(room_choose,))

def roomChoose():
    os.system("clear")
    print('''
    1.Xonani band qilish\n
    2.Band xonani bo'shatish
    ''')
    choose = int(input("Amalni tanlang >> "))
    isbusy = "0"
    question = ""
    if choose == 1:
        freeRooms()
        isbusy = "1"
        question = "Qaysi xonani band qilmoqchisiz(id) >> "
        
    elif choose == 2:
        busyRooms()
        isbusy = "0"
        question = "Qaysi xonani bo'shatmoqchisiz(id) >> "
    else:
        print("Bunday amal yo'q")
        welcome()
    room_choose = input(question)
    if choose == 1:
        newUser(room_choose)
    elif choose == 2:
        clearUser(room_choose)
    try:
        c.execute("update rooms set busy = %s where id = %s",(isbusy,room_choose))
        mydb.commit()
        welcome()
        print("YEss!!!!!")
    except:
        mydb.rollback()

def welcome():
    os.system("clear")
    print("--------------------XUSH KELIBSIZ-----------------------------")
    print("\n\n1.Jadvalni ko'rsatish")
    print("\n2.Jadvalni o'zgartirish\n")
    print("3.Mehmonlar ro'yhati\n")
    print("4.Chiqish")
    amal = int(input("Amalni tanlang >> "))
    if amal == 1:
        showTable()
    elif amal == 2:
        roomChoose()
    elif amal == 3:
        showUsers()
    else:
        exit()
welcome()
mydb.close()
