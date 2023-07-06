import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb 
root=Tk()
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="Hasini@123")
cursor = mydb.cursor()
connector = mydb
root.geometry("2000x2000")
root.title("Animal Info")
heading_label= Label(root, text = "Animal Info", font = ("Rockwell", 15, "bold"), bg = "Black", fg = "White")
heading_label.pack()
l_frame = Frame(root, bg="light blue")
c_frame = Frame(root, bg = "dark blue" )
r_frame = Frame(root, bg = "royal blue")
#name, scienticific name, species, color, habitat, endangered, extinct
search_strvar= StringVar()
name_strvar = StringVar()
scientificname_strvar = StringVar()
species_strvar = StringVar()
color_strvar = StringVar()
habitat_strvar = StringVar()
endangered_strvar= StringVar()
extinct_strvar = StringVar()
search_entry = Entry(r_frame, width = 20, font = ("Verdana", 11), textvariable = search_strvar)
search_entry.place(x=100, y = 20)

def search():  
	global connector 
	query = str(search_strvar.get())
	if query !='':
		listbox.delete(0, END)
		cursor.execute('SELECT * FROM ANIMALS_BOOK.ANIMALINFO WHERE NAME LIKE %s', ("%"+query+ "%",))
		check = cursor.fetchall()
		for data in check:
			listbox.insert(END, data[0])

def submit(): 
	global search_strvar, name_strvar, scientificname_strvar, species_strvar, color_strvar, habitat_strvar, endangered_strvar, extinct_strvar, search_entry
	global cursor
	name, scientificname, species, color, habitat, endangered, extinct = name_strvar.get(), scientificname_strvar.get(), species_strvar.get(), color_strvar.get(), habitat_strvar.get(), endangered_strvar.get(), extinct_strvar.get()
	print(name, scientificname, species, color, habitat, endangered, extinct)
	print(name)
	if name == '' or scientificname == '' or species== '' or color == "" or habitat== "" or endangered== "" or extinct == "": 
		mb.showerror("Error!", "Please fill all the fields")
	else: 
		cursor.execute(
			"INSERT INTO ANIMALS_BOOK.ANIMALINFO (NAME, SCIENTIFICNAME, SPECIES, COLOR, HABITAT, ENDANGERED, EXTINCT) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, scientificname, species, color, habitat, endangered, extinct))
		connector.commit()
		mb.showinfo("Info added", "We have stored the information sucessfully")	
		listbox.delete(0, END)
		list_animals()
		clear_fields()

def view_record(): 
	global search_strvar, name_strvar, scientificname_strvar, species_strvar, color_strvar, habitat_strvar, endangered_strvar, extinct_strvar, search_entry
	x=listbox.get(ACTIVE)
	print(x)
	cursor.execute("SELECT * FROM ANIMALS_BOOK.ANIMALINFO WHERE NAME='"+x+"';")
	values = cursor.fetchall()[0]
	#print(values)
	name_strvar.set(values[0]); scientificname_strvar.set(values[1]);species_strvar.set(values[2]);color_strvar.set(values[3]);habitat_strvar.set(values[4]);endangered_strvar.set(values[5]);extinct_strvar.set(values[6]);




def clear_fields(): 
	global search_strvar, name_strvar, scientificname_strvar, species_strvar, color_strvar, habitat_strvar, endangered_strvar, extinct_strvar, search_entry
	listbox.selection_clear(0, END)
	name_strvar.set('')
	scientificname_strvar.set('')
	species_strvar.set('')
	color_strvar.set('')
	habitat_strvar.set('')
	endangered_strvar.set('')
	extinct_strvar.set('')
	search_strvar.set('')

def list_animals(): 
	global cursor 
	cursor.execute('SELECT NAME FROM ANIMALS_BOOK.ANIMALINFO')
	fetch = cursor.fetchall()
	for data in fetch: 
		listbox.insert(END, data)
	name_strvar.set('')
	search_strvar.set('')
	scientificname_strvar.set('')
	species_strvar.set('')
	color_strvar.set('')
	habitat_strvar.set('')
	endangered_strvar.set('')
	extinct_strvar.set('')

l_frame.place(relx =0, y = 30, relheight = 1, relwidth = 0.3)
c_frame.place(relx = 0.6, y = 30, relheight = 1, relwidth = 0.4)
r_frame.place(relx = 0.3, y = 30, relheight = 1, relwidth = 0.4)
Button(r_frame, text = "Search", font=("Rockwell"), width=15, command=search).place(x=100, rely=0.1)
Button(r_frame, text = "Add Record", font=("Rockwell"), width=15, command=submit).place(x=100, rely=0.2)
Button(r_frame, text = "View Record", font=("Rockwell"), width=15, command=view_record).place(x=100, rely=0.3)
Button(r_frame, text = "Clear Fields", font=("Rockwell"), width=15, command=clear_fields).place(x=100, rely=0.4)

Label(c_frame, text="Name", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.05)
name_entry = Entry(c_frame, width = 15, font =("Rockwell ", 11), textvariable=name_strvar)
name_entry.place(relx = 0.3, rely = 0.1)

Label(c_frame, text="Scientific Name", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.18)
scientificname_entry = Entry(c_frame, width = 15, font =("Rockwell ", 11), textvariable=scientificname_strvar)
scientificname_entry.place(relx = 0.3, rely = 0.23)

Label(c_frame, text="Species", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.31)
species_entry = Entry(c_frame, width = 15, font =("Rockwell", 11), textvariable=species_strvar)
species_entry.place(relx = 0.3, rely = 0.36)

Label(c_frame, text="Color", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.45)
color_entry = Entry(c_frame, width = 15, font =("Rockwell", 11), textvariable=color_strvar)
color_entry.place(relx = 0.3, rely = 0.50)

Label(c_frame, text="Habitat", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.6)
habitat_entry = Entry(c_frame, width = 15, font =("Rockwell", 11), textvariable=habitat_strvar)
habitat_entry.place(relx = 0.3, rely = 0.65)

Label(c_frame, text="Endangered?", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.72)
endangered_entry = Entry(c_frame, width = 15, font =("Rockwell", 11), textvariable=endangered_strvar)
endangered_entry.place(relx = 0.3, rely = 0.77)

Label(c_frame, text="Extinct?", bg="royal blue", fg ="black", font = ("Rockwell")).place(relx=0.3, rely = 0.85)
extinct_entry = Entry(c_frame, width = 15, font =("Rockwell", 11), textvariable=extinct_strvar)
extinct_entry.place(relx = 0.3, rely = 0.9)



Label(l_frame, text="List of Animals", font =("Rockwell", 14), bg="light blue").place(relx=0.25, rely=0.05)
listbox=Listbox(l_frame, selectbackground = "light blue", bg="light blue", font=("Rockwell", 12), height = 20, width=25)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand = scroller.set)
listbox.place(x=50, y=50)
root.mainloop()