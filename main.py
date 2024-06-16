import tkinter
from tkinter import ttk
from tkinter import messagebox


def enterData():
    # User Info
    firstName = ImięOjcaEntry.get()
    lastName = ImięDrugieEntry.get()
    email = nazwiskoEntry.get()
    age = ageSpinbox.get()
    nationality = nationalityCombobox.get()

    # Course Info
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

        tkinter.messagebox.showinfo(
            title="Success", message="Successfully registered.")
    else:
        tkinter.messagebox.showwarning(
            title="Error", message="First name and last name are required.")


window = tkinter.Tk()
window.title("Data Entry")
window.geometry("580x400")
window.minsize(580, 350)


window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

frame = tkinter.Frame(window)
frame.pack()

# First Row
userInfoFrame = ttk.LabelFrame(frame, text="Dane Strony")
userInfoFrame.grid(row=0, column=0, padx=20, pady=10)

ImięLabel = ttk.Label(userInfoFrame, text="Imię Pierwsze")
ImięLabel.grid(row=0, column=0)

ImięEntry = ttk.Entry(userInfoFrame)
ImięEntry.grid(row=1, column=0)

ImięDrugieLabel = ttk.Label(userInfoFrame, text="Imię Drugie")
ImięDrugieLabel.grid(row=0, column=1)

ImięDrugieEntry = ttk.Entry(userInfoFrame)
ImięDrugieEntry.grid(row=1, column=1)

nazwiskoLabel = ttk.Label(userInfoFrame, text="Nazwisko")
nazwiskoLabel.grid(row=0, column=2)

nazwiskoEntry = ttk.Entry(userInfoFrame)
nazwiskoEntry.grid(row=1, column=2)


ImięOjcaLabel = ttk.Label(userInfoFrame, text="Imię Ojca")
ImięOjcaLabel.grid(row=2, column=0)

ImięOjcaEntry = ttk.Entry(userInfoFrame)
ImięOjcaEntry.grid(row=3, column=0)

ImięMatkiLabel = ttk.Label(userInfoFrame, text="Imię Matki")
ImięMatkiLabel.grid(row=2, column=1)

ImięMatkiEntry = ttk.Entry(userInfoFrame)
ImięMatkiEntry.grid(row=3, column=1)

PESELLabel = ttk.Label(userInfoFrame, text="PESEL")
PESELLabel.grid(row=2, column=2)

PESELEntry = ttk.Entry(userInfoFrame)
PESELEntry.grid(row=3, column=2)















dokumentRodzajLabel = ttk.Label(userInfoFrame, text="Dokument Tożsamości")
dokumentRodzajLabel.grid(row=4, column=0)

dokumentRodzajCombobox = ttk.Combobox(userInfoFrame, values=[
                                   "Dowód Osobisty", "Paszport"])
dokumentRodzajCombobox.grid(row=5, column=0)

nrDokumentuLabel = ttk.Label(userInfoFrame, text="Numer Dokumentu")
nrDokumentuLabel.grid(row=4, column=1)

nrDokumentuEntry = ttk.Entry(userInfoFrame)
nrDokumentuEntry.grid(row=5, column=1)

adresLabel = ttk.Label(userInfoFrame, text="Adres")
adresLabel.grid(row=4, column=2)

adresEntry = ttk.Entry(userInfoFrame)
adresEntry.grid(row=5, column=2)

for widget in userInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=3)

# Second Row
coursesFrame = ttk.LabelFrame(frame, text="Charakter Udziału")
coursesFrame.grid(row=1, column=0, padx=20, pady=10, sticky="news")

#obywatelstwoVar = tkinter.StringVar(value="Obywatel PL")
#obywatelstwoCheck = ttk.Checkbutton(coursesFrame, text="Obywatel Polski",
                                  #variable=obywatelstwoVar, onvalue="Obywatel PL", offvalue="Nie Obywatel PL")
#obywatelstwoCheck.grid(row=1, column=0)

udziałLicznikLabel = ttk.Label(coursesFrame, text="Udział Licznik")
udziałLicznikLabel.grid(row=0, column=0)

udziałLicznikSpinbox = ttk.Spinbox(coursesFrame, from_="0", to="infinity")
udziałLicznikSpinbox.insert(0, "0")
udziałLicznikSpinbox.grid(row=1, column=0)

udziałMianownikLabel = ttk.Label(coursesFrame, text="Udział Mianownik")
udziałMianownikLabel.grid(row=0, column=1)

udziałMianownikSpinbox = ttk.Spinbox(coursesFrame, from_=0, to="infinity")
udziałMianownikSpinbox.insert(0, "0")
udziałMianownikSpinbox.grid(row=1, column=1)

rodzajUdziałuLabel = ttk.Label(coursesFrame, text="Rodzaj Udziału")
rodzajUdziałuLabel.grid(row=0, column=2)

rodzajUdziałuCombobox = ttk.Combobox(coursesFrame, values=[
                                   "Zwykły", "Wspólność Małżeńśka",])
rodzajUdziałuCombobox.grid(row=1, column=2)

for widget in coursesFrame.winfo_children():
    widget.grid_configure(padx=10, pady=3)

# Third Row
button = ttk.Button(frame, text="Dodaj Stronę", command=enterData)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
