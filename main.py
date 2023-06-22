import tkinter
import sqlite3
from tkinter import ttk
from tkinter import messagebox

#Colors
blackColor = "#050505"  
whiteColor = "#feffff"   
tealColor = "#008080"  

def enterData():
    #User Info
    firstName = firstNameEntry.get()
    lastName = LastNameEntry.get()
    email = emailEntry.get()
    age = ageSpinbox.get()
    nationality = nationalityCombobox.get()
    
    #Course Info
    registrationStatus = regStatusVar.get()
    numCourses = numCourseSpinbox.get()
    numSemesters = numSemestersSpinbox.get()
    
    if firstName and lastName:
        print("------------------------------------------")
        print("First name: ", firstName, "Last name: ", lastName)
        print("Title: ", email, "Age: ", age, "Nationality: ", nationality)
        print("Courses: ", numCourses, "Semesters: ", numSemesters)
        print("Registration status: ", registrationStatus)
        print("------------------------------------------")
        tkinter.messagebox.showinfo(title="Success", message="Successfully registered.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")

    
window = tkinter.Tk()
window.title("Data Entry")
window.geometry('500x280')
window.minsize(500,280)
window.maxsize(500,280)

frame = tkinter.Frame(window)
frame.pack()

#First Row
userInfoFrame = tkinter.LabelFrame(frame, text="User Information")
userInfoFrame.grid(row=0, column=0,padx=20, pady=10)

firstNameLabel = tkinter.Label(userInfoFrame, text="First Name")
firstNameLabel.grid(row=0, column=0)

firstNameEntry = tkinter.Entry(userInfoFrame)
firstNameEntry.grid(row=1, column=0)

lastNameLabel = tkinter.Label(userInfoFrame, text="Last Name")
lastNameLabel.grid(row=0, column=1)

LastNameEntry = tkinter.Entry(userInfoFrame)
LastNameEntry.grid(row=1, column=1)

emailLabel = tkinter.Label(userInfoFrame, text="Email")
emailLabel.grid(row=0, column=2)

emailEntry = tkinter.Entry(userInfoFrame)
emailEntry.grid(row=1, column=2)

ageLabel = tkinter.Label(userInfoFrame, text="Age")
ageLabel.grid(row=2, column=0)

ageSpinbox = tkinter.Spinbox(userInfoFrame, from_=18, to=60)
ageSpinbox.grid(row=3, column=0)

nationalityLabel = tkinter.Label(userInfoFrame, text="Nationality")
nationalityLabel.grid(row=2, column=1)

nationalityCombobox = ttk.Combobox(userInfoFrame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationalityCombobox.grid(row=3, column=1)

for widget in userInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=2)
    
#Second Row
coursesFrame = tkinter.LabelFrame(frame, text="Registration Status")
coursesFrame.grid(row=1, column=0, padx=20, pady=10, sticky="news")

regStatusVar = tkinter.StringVar(value="Not Registered")
registeredCheck = tkinter.Checkbutton(coursesFrame, text="Currently Registered", variable=regStatusVar, onvalue="Registered", offvalue="Not Registered")
registeredCheck.grid(row=1, column=0)

numCoursesLabel = tkinter.Label(coursesFrame, text="Courses")
numCoursesLabel.grid(row=0, column=1)

numCourseSpinbox = tkinter.Spinbox(coursesFrame, from_="0", to="infinity")
numCourseSpinbox.grid(row=1, column=1)

numSemestersLabel = tkinter.Label(coursesFrame, text="Semesters")
numSemestersLabel.grid(row=0, column=2)

numSemestersSpinbox = tkinter.Spinbox(coursesFrame, from_=0, to="infinity")
numSemestersSpinbox.grid(row=1, column=2)

for widget in coursesFrame.winfo_children():
    widget.grid_configure(padx=10, pady=2)
    
#Third Row
button = tkinter.Button(frame, text="Enter Data", bg=tealColor, fg=whiteColor, command=enterData)
button.grid(row=2, column=0, sticky="news", padx=20, pady=10)
window.mainloop()