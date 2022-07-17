from idlelib.pyshell import main as shell
import tkinter
import mysql.connector as SQL

def proj():
    mainWindow = tkinter.Tk()


    mainWindow.title("Python Tutorial")
    mainWindow.geometry('1280x720')
    mainWindow.resizable(width=True, height=True)
    mainWindow.configure(background='#36abcb')

    mainWindow.columnconfigure(0, weight=10)
    mainWindow.columnconfigure(2, weight=10)
    mainWindow.rowconfigure(0, weight=10)
    mainWindow.rowconfigure(2, weight=10)
    mainWindow.rowconfigure(4, weight=10)
    mainWindow.rowconfigure(6, weight=10)

    img = tkinter.PhotoImage(file="Python-Logo-PNG-Image.png")

    Logo_canvas = tkinter.Canvas(mainWindow, width=200, height=200, bg='#36abcb')
    Logo_canvas.grid(row=1, column=1)
    Logo_canvas.configure(border=10, relief='flat')
    Logo_canvas.create_image(115, 0, image=img, anchor='n')

    Scroll=tkinter.Button(mainWindow, text="Next", command=scroll)

    Try_it = tkinter.Button(mainWindow, text="Try it yourself!!", command=shell, bg='#13759c', bd=1, fg='white', font='roboto')
    Try_it.grid(row=5, column=1)
    Try_it.configure(relief='raised')

    textFrame = tkinter.Frame(mainWindow)
    textFrame.grid(row=3, column=1)

    instr = tkinter.Text(textFrame, width=100, height=20)
    instr.grid(row=0, column=0)

    with open("Tutorial.txt", 'r') as f:
        instr.insert(tkinter.INSERT, f.read())

    instr.config(state='disabled', font=("consolas", 12), bg='#2B2B2B', fg='white')

    textScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=instr.yview)
    textScroll.grid(row=3, column=2, sticky='nsw', rowspan=1)
    instr['yscrollcommand'] = textScroll.set


    mainWindow.mainloop()


def show_result():
    user_name = str(input("Enter user name for MySql: "))
    password = str(input("Enter password for MySql: "))

    mydb = SQL.connect(host="localhost", user=user_name, passwd=password)
    mycursor = mydb.cursor()

    if mydb.is_connected() == False:
        print("Can't establish connection")

    try:
        mycursor.execute("USE result")
        mycursor.execute("SELECT * FROM marksheet ORDER BY MarksOb DESC")
    except:
        print("Database does not exist")

    data = mycursor.fetchall()
    for i in data:
      print(i)



def inp():
    while True:
        user_input = str(input(""" Select any of the following:
        1. Tutorial
        2. Quiz
        3. Result
        4. Exit
        """))
        if user_input == '1':
            proj()
        elif user_input == '2':
            from Quiz import main_Program
        elif user_input == '3':
            show_result()
        elif user_input == "4":
            break
        else:
            print("Wrong input")
            inp()

inp()
