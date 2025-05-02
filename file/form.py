from tkinter import *
from tkinter import messagebox 


def save_data():
    name = name_entry.get()
    mobile = mobile_entry.get()
    
    with open("UserData.xlsx","a") as file:
        file.write(f"Name : {name} \t Mobile : {mobile}\n")
    
    name_entry.delete(0,END)
    mobile_entry.delete(0,END)
    messagebox.showinfo("Success", "Data saved successfully!")
    
    
app = Tk()
app.geometry("400x300")
app.title("Simple Form")


Label(app, text="Form", font="Arial 20 bold").grid(row=0, column=1, pady=20)


Label(app, text="Name").grid(row=1, column=0)
name_entry = Entry(app)
name_entry.grid(row=1, column=1, padx=10)

Label(app, text="Mobile Num").grid(row=2, column=0)
mobile_entry = Entry(app)
mobile_entry.grid(row=2, column=1, padx=10)


button = Button(app, text="Submit", bg="blue", fg="white",command=save_data).grid(row=3, column=1, pady=20)



app.mainloop()


