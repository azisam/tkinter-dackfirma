import tkinter as tk
from tkinter import ttk

from booking_repositary import BookingRepositary


class App:
    def __init__(self, ):
        # Skapa huvud fönstret
        self.root = tk.Tk()

        # Titel, storlek
        self.root.title("Däckfirma")
        self.root.geometry("700x450")

        # Repo för bokning och...
        self.booking_repo = BookingRepositary("bookings.json")

        # Välj användare frame
        self.choose_user(self.root)

        # Börja loopet
        tk.mainloop()
    
    def choose_user(self, root):
        self.chooseuserframe = ttk.Frame(root)
        self.chooseuserframe.pack(pady=150)

        self.choose_user = ttk.Label(self.chooseuserframe,text="Vem är du?", font=("", 30))
        self.choose_user.pack()

        self.customer_button = ttk.Button(self.chooseuserframe, text="Kund", command=self.customer_frame)
        self.customer_button.pack(side="left")

        self.owner_button = ttk.Button(self.chooseuserframe, text="Ägare", command="")
        self.owner_button.pack(side="right")

    def customer_frame(self):
        # Glömmer den tidigare frame
        self.chooseuserframe.forget()

        # Huvud frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Boka tid frame
        self.booking_frame = ttk.Frame(self.main_frame)
        self.booking_frame.pack(side=tk.LEFT)

        # Tillgängliga tider frame
        self.available_bookings_frame = ttk.Frame(self.main_frame)
        self.available_bookings_frame.pack(side=tk.RIGHT, fill=None, padx=20)

        # Tillgängliga tider titel
        self.available_bookings_title = ttk.Label(self.available_bookings_frame, text="Tillgängliga tider", font=("", 25))
        self.available_bookings_title.pack(side=tk.TOP)

        # Tillgängliga tider table
        self.available_bookings_table = ttk.Treeview(self.available_bookings_frame)
        self.available_bookings_table.pack(fill=tk.BOTH, expand=True)

        # Körs när en selektion görs/ändras
        def onChange(event):
            ...
            table = event.widget

            selected_item = table.selection()

            print(table.item(selected_item[0], "values"))

        bookings = self.booking_repo.get_available_bookings()

        columns = ["Datum", "Tid", ""]

        self.available_bookings_table['columns'] = columns

        # Döljer den första kolumnen (#0)
        self.available_bookings_table.column("#0", width=0, stretch=False)
        self.available_bookings_table.heading("#0", text="")

        for col in columns:
            self.available_bookings_table.column(col, width=100, anchor="center")
            self.available_bookings_table.heading(col, text=col)

        for booking in bookings:
            row = [
                booking["date"],  # Map "Datum" to "date"
                booking["time"],  # Map "Tid" to "time"
                "Välj tid",       # Placeholder for "Knapp"
            ]
            self.available_bookings_table.insert("", "end", values=row)
        
        self.available_bookings_table.bind("<<TreeviewSelect>>", onChange)

        # Boka tid titel
        self.booking_title = ttk.Label(self.booking_frame, text="Boka tid", font=("", 25))
        self.booking_title.grid()

        # Välj datum
        self.choose_date_label = ttk.Label(self.booking_frame, text="Datum:")
        self.choose_date_label.grid(row=1, column=0)
        self.active_booking_date = tk.StringVar()
        self.active_booking_date.set("Tom")
        self.choose_date_entry = ttk.Entry(self.booking_frame, textvariable=self.active_booking_date, state=tk.DISABLED, foreground="white")
        self.choose_date_entry.grid(row=1, column=1)

        # Välj tid
        self.choose_time_label = ttk.Label(self.booking_frame, text="Tid:")
        self.choose_time_label.grid(row=2, column=0)
        self.active_booking_time = tk.StringVar()
        self.active_booking_time.set("20:00")
        self.choose_time_entry = ttk.Entry(self.booking_frame, textvariable=self.active_booking_time, state=tk.DISABLED, foreground="white")
        self.choose_time_entry.grid(row=2, column=1)

        # För och efternamn
        self.full_name_label = ttk.Label(self.booking_frame, text="För och efternamn:")
        self.full_name_label.grid(row=3, column=0)
        self.full_name_entry = ttk.Entry(self.booking_frame)
        self.full_name_entry.grid(row=3, column=1)

        # E-post
        self.choose_email_label = ttk.Label(self.booking_frame, text="E-post:")
        self.choose_email_label.grid(row=4, column=0)
        self.choose_email_input = ttk.Entry(self.booking_frame)
        self.choose_email_input.grid(row=4, column=1)

        # Välj typ av tjänst
        self.service_label = ttk.Label(self.booking_frame, text="Typ av tjänst:")
        self.service_label.grid(row=5, column=0)

        self.radio_choice = tk.IntVar()
        self.radio_choice.set(0)
        self.services = ("Däckbyte", "Balansering", "Däckreperation")

        for index, service in enumerate(self.services):
            ttk.Radiobutton(self.booking_frame, text=service, value=index, variable=self.radio_choice).grid(row=5, column=index+1)


if __name__ == "__main__":
    app = App()
