import tkinter
from tkinter import ttk
from tkinter import messagebox

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

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

frame = tkinter.Frame(window)
frame.pack()

#First Row
userInfoFrame = ttk.LabelFrame(frame, text="User Information")
userInfoFrame.grid(row=0, column=0,padx=20, pady=10)

firstNameLabel = ttk.Label(userInfoFrame, text="First Name")
firstNameLabel.grid(row=0, column=0)

firstNameEntry = ttk.Entry(userInfoFrame)
firstNameEntry.grid(row=1, column=0)

lastNameLabel = ttk.Label(userInfoFrame, text="Last Name")
lastNameLabel.grid(row=0, column=1)

LastNameEntry = ttk.Entry(userInfoFrame)
LastNameEntry.grid(row=1, column=1)

emailLabel = ttk.Label(userInfoFrame, text="Email")
emailLabel.grid(row=0, column=2)

emailEntry = ttk.Entry(userInfoFrame)
emailEntry.grid(row=1, column=2)

ageLabel = ttk.Label(userInfoFrame, text="Age")
ageLabel.grid(row=2, column=0)

ageSpinbox = ttk.Spinbox(userInfoFrame, from_=18, to=60)
ageSpinbox.insert(0,"18")
ageSpinbox.grid(row=3, column=0)

nationalityLabel = ttk.Label(userInfoFrame, text="Nationality")
nationalityLabel.grid(row=2, column=1)

nationalityCombobox = ttk.Combobox(userInfoFrame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationalityCombobox.grid(row=3, column=1)

for widget in userInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=3)
    
#Second Row
coursesFrame = ttk.LabelFrame(frame, text="Registration Status")
coursesFrame.grid(row=1, column=0, padx=20, pady=10, sticky="news")

regStatusVar = tkinter.StringVar(value="Not Registered")
registeredCheck = ttk.Checkbutton(coursesFrame, text="Currently Registered", variable=regStatusVar, onvalue="Registered", offvalue="Not Registered")
registeredCheck.grid(row=1, column=0)

numCoursesLabel = ttk.Label(coursesFrame, text="Courses")
numCoursesLabel.grid(row=0, column=1)

numCourseSpinbox = ttk.Spinbox(coursesFrame, from_="0", to="infinity")
numCourseSpinbox.grid(row=1, column=1)

numSemestersLabel = ttk.Label(coursesFrame, text="Semesters")
numSemestersLabel.grid(row=0, column=2)

numSemestersSpinbox = ttk.Spinbox(coursesFrame, from_=0, to="infinity")
numSemestersSpinbox.grid(row=1, column=2)

for widget in coursesFrame.winfo_children():
    widget.grid_configure(padx=10, pady=3)
    
#Third Row
button = ttk.Button(frame, text="Enter Data", command=enterData)
button.grid(row=2, column=0, sticky="news", padx=20, pady=10)
window.mainloop()