import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import tkinter.font as font
from functools import partial
import os
import json


class Library:
    d = dict()

    def first_window(self):
        global window
        window = tk.Tk()
        window.geometry('640x480')
        window.resizable(False, False)
        window.title('LIBRARY')
        window_l = ttk.Label(text='Library', font=('Brush Script MT', 20))
        frame = ttk.Frame(width=640, height=50, relief='sunken')
        label = ttk.Label(master=frame, text='Please choose an operation', font=('Edwardian Script ITC', 30))

        next_button = ttk.Button(text="Next", command=self.combo_value).place(x=275, y=200)

        global combobox
        combobox = ttk.Combobox()
        combobox["values"] = ("Add Book", "Change Price", "Show Price", "Exit")
        combobox["state"] = "readonly"
        combobox.current(0)
        combobox.place(x=250, y=125)

        window_l.pack()
        frame.pack()
        label.grid(row=10, column=3, sticky='n')

        window.mainloop()

    def combo_value(self):
        combo_value = combobox.get()
        if combo_value == "Add Book":
            self.add_book_window()

        elif combo_value == "Change Price":
            self.price_change_window()

        elif combo_value == "Show Price":
            self.show_price_window()

        else:
            window.destroy()

    def add_book_window(self):
        # A method to create a window to get name and price of a book

        window.destroy()
        a_windows = tk.Tk()
        a_windows.geometry('640x480')
        a_windows.resizable(False, False)
        a_windows.title('Adding Book')

        a_frame = tk.Frame(width=300, height=50, relief='sunken', borderwidth=3, bg='green')
        a_label = tk.Label(master=a_frame, text='Here You Can Add Any Book', fg='yellow', bg='green')
        a_label.config(font=('Harlow Solid Italic', 15))

        a_frame.place(x=160, y=50)
        a_label.place(x=10, y=5)

        global name_input
        name_input = tk.StringVar()
        name_entry = ttk.Entry(master=a_windows, textvariable=name_input)
        name_entry.place(x=225, y=200)
        name_label = tk.Label(a_windows, text='Please enter the name of the book: ')
        name_label.place(x=30, y=200)

        global price_input
        price_input = tk.IntVar()
        price_entry = ttk.Entry(a_windows, textvariable=price_input)
        price_entry.place(x=225, y=250)
        price_label = tk.Label(a_windows, text="How much it cost's: ")
        price_label.place(x=30, y=250)

        submit_button = ttk.Button(a_windows, text='Submit',
                                   command=partial(self.add_book)).place(x=450, y=220)

        return_b = ttk.Button(a_windows, text='Return', command=lambda: [a_windows.destroy(), self.first_window()],
                              cursor='pirate')
        return_b.place(x=550, y=430)
        a_windows.mainloop()

    def price_change_window(self):
        # Making the window to change price

        window.destroy()
        change_windows = tk.Tk()
        change_windows.geometry('640x480')
        change_windows.resizable(False, False)
        change_windows.title('Changing Price')



        global name_change
        name_change = tk.StringVar()
        name_entry = ttk.Entry(master=change_windows, textvariable=name_change)
        name_entry.place(x=250, y=150)

        name_label = tk.Label(change_windows, text="which book' price do you want to change? ")
        name_label.config(font=('Brush Script MT', 20))
        name_label.place(x=140, y=100)

        price_label = tk.Label(change_windows, text="How much it costs?")
        price_label.config(font=('Brush Script MT', 20))
        price_label.place(x=225, y=200)

        global price_change
        price_change = tk.IntVar()
        price_entry = ttk.Entry(master=change_windows, textvariable=price_change)
        price_entry.place(x=250, y=250)

        search_button = ttk.Button(text='Cahnge', command=self.change_price).place(x=275, y=300)
        return_button = ttk.Button(text='Return', command=lambda: [change_windows.destroy(), self.first_window()]).place(x=550, y=430)

    def show_price_window(self):
        # Making the window for price

        window.destroy()
        price_windows = tk.Tk()
        price_windows.geometry('640x480')
        price_windows.resizable(False, False)
        price_windows.title('Show Price')

        price_frame = tk.Frame(master=price_windows, width=400, height=50, relief='sunken',
                           borderwidth=3, bg='purple').place(x=125, y=50)
        price_label = tk.Label(master=price_frame, text="You Can Ask For Any Book's Price",
                           fg='yellow', bg='purple', font=('Brush Script MT', 20)).place(x=165, y=60)

        global name_show
        name_show = tk.StringVar()
        book_entry = ttk.Entry(master=price_windows, textvariable=name_show)
        book_entry.place(x=235, y=200)
        price_label = tk.Label(price_windows, text="Which book's price do you want")
        price_label.config(font=('Brush Script MT', 20))
        price_label.place(x=160, y=150)

        search_button = ttk.Button(text='Search', command=self.show_price).place(x=260, y=250)
        return_button = ttk.Button(text='Return', command=lambda: [price_windows.destroy(), self.first_window()]).place(x=550,
                                                                                                               y=430)

    def add_book(self):

        # A method to add book with it's price

        try:
            name = name_input.get()
            price = price_input.get()
            if name:
                if price:
                    if os.path.exists('seraj.txt'):
                        try:
                            my_file = open('seraj.txt')
                            line = my_file.read()
                            j_line = json.loads(line)
                            self.d[name] = price
                            j_line.update(self.d)
                            j = json.dumps(j_line)
                            my_file1 = open('seraj.txt', 'w')
                            my_file1.write(j)
                            my_file.close()
                            my_file1.close()
                            tk.messagebox.showinfo(title='Successes', message='The book has been added successfully')
                        except json.decoder.JSONDecodeError:
                            my_file = open('seraj.txt', 'w')
                            my_file.write('{}')
                    else:
                        my_file = open('seraj.txt', 'w')
                        self.d[name] = price
                        j = json.dumps(self.d)
                        my_file.write(j)
                        my_file.close()
                        tk.messagebox.showinfo(title='Successes', message='The book has been added successfully')
                else:
                    tk.messagebox.showinfo(title='Invalid', message='Please enter a proper price')

            else:
                tk.messagebox.showinfo(title='Invalid', message='Please enter the name of the book')

        except tk.TclError:
            messagebox.showerror('ERROR', 'Please enter a valid price')

    def change_price(self):

        # A method to change the price of books

        try:
            name = name_change.get()
            price = price_change.get()
            if name:
                if price:
                    if os.path.exists('seraj.txt'):
                        my_file = open('seraj.txt', 'r')
                        line = my_file.read()
                        j = json.loads(line)
                        for i in j.keys():
                            if i.lower() == name.lower():
                                j_line = json.loads(line)
                                self.d[name] = price
                                j_line.update(self.d)
                                j = json.dumps(j_line)
                                my_file1 = open('seraj.txt', 'w')
                                my_file1.write(j)
                                my_file.close()
                                my_file1.close()
                                messagebox.showinfo('Done', "The price has been changed")

                    else:
                        messagebox.showerror('ERROR', 'The library is empty, Please try and add a book first')
                else:
                    messagebox.showerror('ERROR', 'Please enter a valid price')
            else:
                messagebox.showerror('ERROR', 'Which book should i change???')
        except tk.TclError:
            messagebox.showerror('ERROR', 'Please enter a valid price')

    def show_price(self):

        # A method to show the price of books

        name = name_show.get()
        if os.path.exists('seraj.txt'):
            my_file = open('seraj.txt', 'r')
            line = my_file.read()
            j = json.loads(line)
            if name in j.keys():
                price = j[name]
                messagebox.showinfo('YES', f'Price is: {price}')

            else:
                messagebox.showerror('Sorry', "We don't have it")

        else:
            messagebox.showerror('ERROR', 'The library is empty, Please try and add a book first ')


x = Library()
x.first_window()
