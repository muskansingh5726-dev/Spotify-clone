import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime
import json
import os

FILE_NAME = "cal.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        reminders = json.load(file)
else:

    reminders = {}
def save_reminders():
    with open(FILE_NAME, "w") as file:
        json.dump(reminders, file, indent=4)
class CalendarApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Calendar & Reminder App")
        self.root.geometry("750x650")
        self.root.configure(bg="#EAF6FF")

        today = datetime.today()

        self.month = today.month
        self.year = today.year

        title = tk.Label(
            root,
            text="Calendar & Reminder",
            font=("Arial", 22, "bold"),
            bg="#0A74DA",
            fg="white",
            pady=10
        )
        title.pack(fill="x")

        nav = tk.Frame(root, bg="#EAF6FF")
        nav.pack(pady=10)

        tk.Button(nav, text="<< Previous",
                  command=self.prev_month).grid(row=0,column=0,padx=10)

        self.month_label = tk.Label(
            nav,
            font=("Arial",16,"bold"),
            bg="#EAF6FF"
        )
        self.month_label.grid(row=0,column=1,padx=20)

        tk.Button(nav,text="Next >>",
                  command=self.next_month).grid(row=0,column=2,padx=10)

        self.calendar_text = tk.Text(
            root,
            width=25,
            height=10,
            font=("Courier",14),
            bg="white"
        )
        self.calendar_text.pack()

        frame = tk.Frame(root,bg="#EAF6FF")
        frame.pack(pady=20)

        tk.Label(frame,text="Date (YYYY-MM-DD)",
                 bg="#EAF6FF").grid(row=0,column=0)

        self.date_entry = tk.Entry(frame,width=18)
        self.date_entry.grid(row=0,column=1,padx=10)

        tk.Label(frame,text="Reminder",
                 bg="#EAF6FF").grid(row=1,column=0,pady=10)

        self.reminder_entry = tk.Entry(frame,width=40)
        self.reminder_entry.grid(row=1,column=1)

        tk.Button(
            frame,
            text="Add Reminder",
            bg="#4CAF50",
            fg="white",
            command=self.add_reminder
        ).grid(row=2,column=0,pady=15)

        tk.Button(
            frame,
            text="View Reminder",
            bg="#2196F3",
            fg="white",
            command=self.view_reminder
        ).grid(row=2,column=1)

        tk.Button(
            frame,
            text="Delete Reminder",
            bg="red",
            fg="white",
            command=self.delete_reminder
        ).grid(row=3,column=0,columnspan=2,pady=10)

        self.display_calendar()

    # --------------------

    def display_calendar(self):

        self.calendar_text.delete("1.0",tk.END)

        cal = calendar.month(self.year,self.month)

        self.calendar_text.insert(tk.END,cal)

        self.month_label.config(
            text=f"{calendar.month_name[self.month]} {self.year}"
        )

    # --------------------

    def prev_month(self):

        self.month -= 1

        if self.month == 0:
            self.month = 12
            self.year -= 1

        self.display_calendar()

    # --------------------

    def next_month(self):

        self.month += 1

        if self.month == 13:
            self.month = 1
            self.year += 1

        self.display_calendar()

    # --------------------

    def add_reminder(self):

        date = self.date_entry.get()
        text = self.reminder_entry.get()

        if date == "" or text == "":
            messagebox.showerror("Error","Fill all fields")
            return

        reminders[date] = text

        save_reminders()

        messagebox.showinfo("Success","Reminder Saved")

        self.date_entry.delete(0,tk.END)
        self.reminder_entry.delete(0,tk.END)

    # --------------------

    def view_reminder(self):

        date = self.date_entry.get()

        if date in reminders:
            messagebox.showinfo(
                "Reminder",
                reminders[date]
            )
        else:
            messagebox.showinfo(
                "Reminder",
                "No Reminder Found."
            )

    # --------------------

    def delete_reminder(self):

        date = self.date_entry.get()

        if date in reminders:

            del reminders[date]

            save_reminders()

            messagebox.showinfo(
                "Deleted",
                "Reminder Deleted"
            )

        else:

            messagebox.showinfo(
                "Reminder",
                "No Reminder Found"
            )

# -------------------------

root = tk.Tk()

app = CalendarApp(root)

root.mainloop()