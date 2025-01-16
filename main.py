import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from booking_repositary import BookingRepositary
from product_repositary import ProductRepositary

from product import Product
from booking import Booking


class App:
    def __init__(self, ):
        # Skapa huvud fönstret
        self.root = tk.Tk()

        # Titel på applikationsfönstret
        self.root.title("Däckfirma")
        #self.root.geometry("900x400")

        # Objekt/instanser för bokning och produkter Repositary
        self.booking_repo = BookingRepositary("bookings.json")
        self.product_repo = ProductRepositary("products.json")

        # Välj användare frame
        self.choose_user(self.root)

        # Börja loopet
        tk.mainloop()
    
    def choose_user(self, root):
        # Ändrar på geometry
        self.root.geometry("350x200")

        self.chooseuserframe = ttk.Frame(root)
        self.chooseuserframe.pack(expand=True)

        self.choose_user = ttk.Label(self.chooseuserframe,text="Välj användartyp", font=("", 30))
        self.choose_user.pack()

        frame_chooseuser_buttons = tk.Frame(self.chooseuserframe)
        frame_chooseuser_buttons.pack(ipadx=10, pady=10)

        self.customer_button = ttk.Button(frame_chooseuser_buttons, text="Kund", command=self.customer_frame)
        self.customer_button.pack(side=tk.LEFT)

        self.owner_button = ttk.Button(frame_chooseuser_buttons, text="Ägare", command=self.owner_frame)
        self.owner_button.pack(side=tk.RIGHT)

    def customer_frame(self):
        # Glömmer den tidigare frame
        self.chooseuserframe.forget()
        
        # Ändrar på geometry
        self.root.geometry("700x400")

        # Huvud frame
        self.frame_main_customer = ttk.Frame(self.root)
        self.frame_main_customer.pack(expand=True, fill=tk.Y, side=tk.TOP, ipadx=25)

        # Knapp för att växla till ägar vy
        button_switch_to_owner_view = ttk.Button(self.frame_main_customer, text="Växla till ägar vy", command=self.switch_to_owner_view)
        button_switch_to_owner_view.pack()

        # Boka tid frame
        self.booking_frame = ttk.Frame(self.frame_main_customer)
        self.booking_frame.pack(side=tk.LEFT)

        # Tillgängliga tider frame
        self.available_bookings_frame = ttk.Frame(self.frame_main_customer)
        self.available_bookings_frame.pack(side=tk.RIGHT)

        # Tillgängliga tider titel
        self.available_bookings_title = ttk.Label(self.available_bookings_frame, text="Tillgängliga tider", font=("", 25))
        self.available_bookings_title.pack(side=tk.TOP)

        # Tillgängliga tider table
        self.available_bookings_table = ttk.Treeview(self.available_bookings_frame)
        self.available_bookings_table.pack(fill=tk.BOTH, expand=True)

        # Boknings ID
        self.booking_id = tk.StringVar()

        # Körs när en treeview selektion görs/ändras
        def onChange(event):
            treeview = event.widget
            selected = treeview.selection()

            if selected:
                date, time, _ = treeview.item(selected, "values") # Delar upp den valda treeview raden (tupel med värden) till variabler

                id = treeview.focus() # Boknings ID för fokuserad treeview rad

                # Sätter in dem nya värderna
                self.booking_id.set(id)
                self.active_booking_date.set(date)
                self.active_booking_time.set(time)

        bookings = self.booking_repo.get_available_bookings()

        columns = ("Datum", "Tid", "")

        self.available_bookings_table['columns'] = columns

        # Döljer en första tom kolumn (#0)
        self.available_bookings_table.column("#0", width=0, stretch=False)

        for column in columns:
            self.available_bookings_table.column(column, width=100, anchor="center")
            self.available_bookings_table.heading(column, text=column)

        for booking in bookings:
            row = [
                booking["date"],  # Map "Datum" to "date"
                booking["time"],  # Map "Tid" to "time"
                "Välj tid",       # Placeholder for "Knapp"
            ]
            self.available_bookings_table.insert("", "end", values=row, iid=booking["id"])
        
        self.available_bookings_table.bind("<<TreeviewSelect>>", onChange)

        # Boka tid titel
        self.booking_title = ttk.Label(self.booking_frame, text="Boka tid", font=("", 25))
        self.booking_title.grid(columnspan=2, pady=(0, 10))

        # Välj datum
        self.choose_date_label = ttk.Label(self.booking_frame, text="Datum:")
        self.choose_date_label.grid(row=1, column=0, sticky="w")
        self.active_booking_date = tk.StringVar(value="Välj från tillgängliga tider...")
        self.choose_date_entry = ttk.Entry(self.booking_frame, textvariable=self.active_booking_date, state=tk.DISABLED)
        self.choose_date_entry.grid(row=1, column=1)

        # Välj tid
        self.choose_time_label = ttk.Label(self.booking_frame, text="Tid:")
        self.choose_time_label.grid(row=2, column=0, sticky="w")
        self.active_booking_time = tk.StringVar(value="Välj från tillgängliga tider...")
        self.choose_time_entry = ttk.Entry(self.booking_frame, textvariable=self.active_booking_time, state=tk.DISABLED)
        self.choose_time_entry.grid(row=2, column=1)

        # För och efternamn
        self.full_name_label = ttk.Label(self.booking_frame, text="För och efternamn:")
        self.full_name_label.grid(row=3, column=0, sticky="w")
        self.full_name_entry = ttk.Entry(self.booking_frame)
        self.full_name_entry.grid(row=3, column=1)

        # E-post
        self.choose_email_label = ttk.Label(self.booking_frame, text="E-post:")
        self.choose_email_label.grid(row=4, column=0, sticky="w")
        self.entry_email = ttk.Entry(self.booking_frame)
        self.entry_email.grid(row=4, column=1)


        # Välj typ av tjänst
        self.service_label = ttk.Label(self.booking_frame, text="Typ av tjänst:")
        self.service_label.grid(row=5, column=0, sticky="w")

        self.radio_choice = tk.IntVar()
        self.radio_choice.set(None)
        self.services = ("Däckbyte", "Balansering", "Däckreperation")

        for index, service in enumerate(self.services):
            ttk.Radiobutton(self.booking_frame, text=service, value=index, variable=self.radio_choice).grid(row=5+index, column=1, padx=(0, 10), pady=5, sticky="w")

        # Boka tid knapp
        self.book_time_button = ttk.Button(self.booking_frame, text="Boka", command=self.onClickBookingBtn)
        self.book_time_button.config(default="active")
        self.book_time_button.grid(row=8, columnspan=2, pady=(10, 0))

    def owner_frame(self):
        # Glömmer den tidigare frame
        self.chooseuserframe.forget()

        # Ändrar på geometry
        self.root.geometry("600x670")

        # Huvud frame
        self.frame_main_owner = ttk.Frame(self.root)
        self.frame_main_owner.pack()

        # Knapp för att växla till kund vy
        button_switch_to_customer_view = ttk.Button(self.frame_main_owner, text="Växla till kund vy", command=self.switch_to_customer_view)
        button_switch_to_customer_view.pack()

        # Bokade tider frame
        frame_bookings = ttk.Frame(self.frame_main_owner)
        frame_bookings.pack(pady=(20, 0))

        # Produkthantering frame
        frame_products = ttk.Frame(self.frame_main_owner)
        frame_products.pack(pady=(20, 0))

        # Bokade tider label
        label_bookings = ttk.Label(frame_bookings, text="Bokade tider", font=("", 25))
        label_bookings.pack()

        # Skapa ny tid knapp
        button_new_time = ttk.Button(frame_bookings, text="Skapa ny tid", command=self.add_booking)
        button_new_time.pack(pady=(0, 5))

        # Bokade tider treeview
        treeview_bookings = ttk.Treeview(frame_bookings)
        treeview_bookings.pack()

        # Treeview
        bookings = self.booking_repo.get_customer_bookings()

        columns = ("Datum", "Tid", "Kund", "E-post", "Tjänst")

        treeview_bookings['columns'] = columns

        # Döljer en första tom kolumn (#0)
        treeview_bookings.column("#0", width=0, stretch=False)

        for column in columns:
            treeview_bookings.column(column, width=100, anchor="center")
            treeview_bookings.heading(column, text=column)

        if bookings:
            for booking in bookings:
                row = [
                    booking["date"],
                    booking["time"],
                    booking["customer"]["fullName"],
                    booking["customer"]["email"],
                    booking["service"]
                ]
                treeview_bookings.insert("", "end", values=row, iid=booking["id"])

        # Produkthantering label
        label_products = ttk.Label(frame_products, text="Produkthantering", font=("", 25))
        label_products.grid(row=0)

        # Frame för CRUD knappar
        frame_crud_buttons = tk.Frame(frame_products)
        frame_crud_buttons.grid(row=1, pady=(0, 5))

        # Produkthantering buttons
        button_add_product = ttk.Button(frame_crud_buttons, text="Lägg till produkt", command=self.add_product)
        button_update_product = ttk.Button(frame_crud_buttons, text="Uppdatera produkt", command=self.update_product)
        button_remove_product = ttk.Button(frame_crud_buttons, text="Ta bort produkt", command=self.remove_product)
        buttons = [button_add_product, button_update_product, button_remove_product]
        for button in buttons:
            button.grid(row=0, column=buttons.index(button), padx=10)

        # Produkthantering treeview
        self.treeview_products = ttk.Treeview(frame_products)
        self.treeview_products.grid(row=2)

        products = self.product_repo.get_products()

        columns = ("Produkt ID", "Produkt namn", "Pris", "I lager", "Kategori")

        self.treeview_products['columns'] = columns

        # Döljer en första tom kolumn (#0)
        self.treeview_products.column("#0", width=0, stretch=False)

        for column in columns:
            self.treeview_products.column(column, width=100, anchor="center")
            self.treeview_products.heading(column, text=column)

        if products:
            for product in products:
                row = [
                    product["id"],
                    product["name"],
                    product["price"],
                    product["inStock"],
                    product["category"]
                ]
                self.treeview_products.insert("", "end", values=row, iid=product["id"])

    # Modal dialog för att lägga till en ny produkt (Ägare)
    def add_product(self):

        def onClick():
            id = entry_product_id.get()
            name = entry_product_name.get()
            price = int(entry_product_price.get())
            in_stock = int(entry_product_in_stock.get())
            category = entry_product_category.get()

            # Nytt produkt objekt
            new_product = Product(id, name, price, in_stock, category)

            # Lägger till den nya produkten i products JSON filen samt retunerar produkt dict:en om allt gått bra
            product = self.product_repo.add_product(new_product)

            # Om produkten lagts till korrekt i products JSON filen
            if product:
                row = [
                    product["id"],
                    product["name"],
                    product["price"],
                    product["inStock"],
                    product["category"]
                ]

                self.treeview_products.insert("", "end", values=row, iid=product["id"])
                dismiss()

        # Stänger dialog fönster
        def dismiss():
            dlg.grab_release()
            dlg.destroy()

        # Skapar dialog fönster
        dlg = tk.Toplevel(self.root, padx=15, pady=10)

        # Placerar översta dialogrutan ovanför root fönstret (https://stackoverflow.com/questions/36050192/how-to-position-toplevel-widget-relative-to-root-window)
        x= self.root.winfo_x()
        y = self.root.winfo_y()
        dlg.geometry("+%d+%d" % (x + 100, y + 200))

        ttk.Label(dlg, text="Produkt ID:").pack()
        entry_product_id = ttk.Entry(dlg)
        entry_product_id.pack(pady=(0, 10))

        ttk.Label(dlg, text="Produkt namn:").pack()
        entry_product_name = ttk.Entry(dlg)
        entry_product_name.pack(pady=(0, 10))

        ttk.Label(dlg, text="Pris:").pack()
        entry_product_price = ttk.Entry(dlg)
        entry_product_price.pack(pady=(0, 10))

        ttk.Label(dlg, text="I lager:").pack()
        entry_product_in_stock = ttk.Entry(dlg)
        entry_product_in_stock.pack(pady=(0, 10))

        ttk.Label(dlg, text="Kategori:").pack()
        entry_product_category = ttk.Entry(dlg)
        entry_product_category.pack()

        # Lägg till ny produkt knapp
        ttk.Button(dlg, text="Lägg till produkt", command=onClick).pack(pady=(20, 0))
        
        # Mer för att skapa dialog fönstret (https://tkdocs.com/tutorial/windows.html#dialogs)
        dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
        dlg.transient(self.root) # dialog window is related to main
        dlg.wait_visibility() # can't grab until window appears, so we wait
        dlg.grab_set() # ensure all input goes to our window
        dlg.wait_window() # block until window is destroyed

    def onClickBookingBtn(self):
        id = self.booking_id.get()
        full_name = self.full_name_entry.get()
        email = self.entry_email.get()
        service = self.services[self.radio_choice.get()]
        customer = { "fullName": full_name, "email": email }

        booking = self.booking_repo.book_time(id, service, customer)

        if booking:
            # Ta bort / rensa värden från alla input fält
            self.active_booking_date.set("Välj från tillgängliga tider...")
            self.active_booking_time.set("Välj från tillgängliga tider...")
            self.full_name_entry.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.radio_choice.set(None)

            # Tar bort bokningen från tillgängliga bokningar treeview:en
            self.available_bookings_table.delete(id)

    def remove_product(self):
        id = self.treeview_products.focus()

        # Om en produkt inte är vald från trädvyn
        if not id:
            messagebox.showerror(title="Välj en produkt", message="Du behöver välja en produkt från trädvyn!", icon=messagebox.ERROR)

        removed_product = self.product_repo.remove_product(id)

        if removed_product:
            self.treeview_products.delete(id)

    def update_product(self):
        # Om en rad inte är vald i treeview:en - hoppa ur metoden
        if not self.treeview_products.focus():
            messagebox.showerror(title="Välj en produkt", message="Du behöver välja en produkt från trädvyn!", icon=messagebox.ERROR)
            return

        selected = self.treeview_products.selection()
        selected_index = self.treeview_products.index(selected)
        # Delar upp tupel:en till variabler
        id, name, price, in_stock, category = (self.treeview_products.item(selected, "values"))

        def onClick():
            product = {
                "id": entry_id.get(),
                "name": entry_name.get(),
                "price": entry_price.get(),
                "inStock": entry_in_stock.get(),
                "category": entry_category.get()
            }

            updated_product = self.product_repo.update_product(id, product)

            if updated_product:
                row = (
                    updated_product["id"],
                    updated_product["name"],
                    updated_product["price"],
                    updated_product["inStock"],
                    updated_product["category"]
                )
                self.treeview_products.delete(id)
                self.treeview_products.insert("", index=selected_index, iid=updated_product["id"], values=row)
                dismiss()

        # Stänger dialog fönster
        def dismiss():
            dlg.grab_release()
            dlg.destroy()

        # Skapar dialog fönster
        dlg = tk.Toplevel(self.root, padx=15, pady=10)

        # Placerar översta dialogrutan ovanför root fönstret
        x= self.root.winfo_x()
        y = self.root.winfo_y()
        dlg.geometry("+%d+%d" % (x + 100, y + 200))

        ttk.Label(dlg, text="Produkt ID:").pack()
        entry_id = tk.StringVar(value=id)
        entry_product_id = ttk.Entry(dlg, textvariable=entry_id)
        entry_product_id.pack(pady=(0, 10))

        ttk.Label(dlg, text="Produkt namn:").pack()
        entry_name = tk.StringVar(value=name)
        entry_product_name = ttk.Entry(dlg, textvariable=entry_name)
        entry_product_name.pack(pady=(0, 10))

        ttk.Label(dlg, text="Pris:").pack()
        entry_price = tk.IntVar(value=price)
        entry_product_price = ttk.Entry(dlg, textvariable=entry_price)
        entry_product_price.pack(pady=(0, 10))

        ttk.Label(dlg, text="I lager:").pack()
        entry_in_stock = tk.IntVar(value=in_stock)
        entry_product_in_stock = ttk.Entry(dlg, textvariable=entry_in_stock)
        entry_product_in_stock.pack(pady=(0, 10))

        ttk.Label(dlg, text="Kategori:").pack()
        entry_category = tk.StringVar(value=category)
        entry_product_category = ttk.Entry(dlg, textvariable=entry_category)
        entry_product_category.pack()

        # Uppdatera produkt knapp
        ttk.Button(dlg, text="Uppdatera produkt", command=onClick).pack(pady=(20, 0))
        
        # Mer för att skapa dialog fönstret (https://tkdocs.com/tutorial/windows.html#dialogs)
        dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
        dlg.transient(self.root) # dialog window is related to main
        dlg.wait_visibility() # can't grab until window appears, so we wait
        dlg.grab_set() # ensure all input goes to our window
        dlg.wait_window() # block until window is destroyed

    def add_booking(self):
        
        def onSubmit():
            date = entry_date.get()
            time = entry_time.get()

            # Nytt boknings objekt
            new_booking = Booking(date, time)

            # Lägger till den nya bokningen i bookings JSON filen samt retunerar booking dict:en om allt gått bra
            booking = self.booking_repo.add_booking(new_booking)

            # Om bokningen lagts till korrekt i bookings JSON filen
            if booking:
                dismiss()

        # Stänger dialog fönster
        def dismiss():
            dlg.grab_release()
            dlg.destroy()

        # Skapar dialog fönster
        dlg = tk.Toplevel(self.root, padx=15, pady=10)

        # Placerar översta dialogrutan ovanför root fönstret
        x= self.root.winfo_x()
        y = self.root.winfo_y()
        dlg.geometry("+%d+%d" % (x + 100, y + 200))

        # Datum label + entry
        ttk.Label(dlg, text="Datum:").pack()
        entry_date = ttk.Entry(dlg)
        entry_date.pack(pady=(0, 10))

        # Tid label + entry
        ttk.Label(dlg, text="Tid:").pack()
        entry_time = ttk.Entry(dlg)
        entry_time.pack(pady=(0, 10))

        # Lägg till ny produkt knapp
        ttk.Button(dlg, text="Skapa ny tid", command=onSubmit).pack(pady=(20, 0))
        
        # Mer för att skapa dialog fönstret (https://tkdocs.com/tutorial/windows.html#dialogs)
        dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
        dlg.transient(self.root) # dialog window is related to main
        dlg.wait_visibility() # can't grab until window appears, so we wait
        dlg.grab_set() # ensure all input goes to our window
        dlg.wait_window() # block until window is destroyed

    def switch_to_customer_view(self):
        self.frame_main_owner.forget()
        self.customer_frame()

    def switch_to_owner_view(self):
        self.frame_main_customer.forget()
        self.owner_frame()

if __name__ == "__main__":
    app = App()
