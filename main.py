from tkinter import *
import os.path
import sqlite3

# EDIT_ME
DBNAME = 'optics' + '.db' 
# TABLENAME and COLUMNS are used to create the tabel with
# 'CREATE TABLE TABLENAME (COLUMNS);'.
TABLENAME = 'optics'
# column_names, eventually this could be parsed from 'COLUMNS'. Currently it is
# used to insert the data. 
COLUMNS = [('type', 'TEXT'), ('manufacturer', 'TEXT'), 
		('focal_length', 'TEXT'), ('wavelength', 'TEXT'),
		('diameter', 'TEXT'), ('comment', 'TEXT')]

class entry_field:
	def __init__(self, parent, colName):

		self.frame = Frame(parent)
		self.frame.pack(side = TOP)
		
		self.label = Label(self.frame, text = colName)
		self.label.configure(width = 15)
		self.label.pack(side = LEFT)

		self.entry = Entry(self.frame)
		self.entry.pack(side = LEFT)
		self.value = lambda : self.entry.get()

		self.holdButton = Button(self.frame, command = self.hold)
		self.holdButton.configure(text = 'Hold')
		self.holdButton.pack(side = RIGHT)

	def hold(self):
		print('derp')


class App:
	def __init__(self, parent, columns, tablename, database):
		self.myParent = parent
		self.columns = columns
		#self.colNames = get_colNames(COLUMNS)
		self.tablename = tablename
		self.database = database

		self.Container = Frame(parent)
		self.Container.pack()

		self.check_connections(self.columns, self.tablename, self.database)
		
		self.entrycont = Frame(self.Container)
		self.entrycont.pack(side = TOP)
		self.make_buttons(self.myParent, self.columns)

		# Next/esc container
		self.next_esc = Frame(self.Container)
		self.next_esc.pack(side = BOTTOM)

		# Next button.
		self.nextButton = Button(self.next_esc, command = self.nextItem)
		self.nextButton.configure(text = 'Next')
		self.nextButton.pack(side = LEFT)

		# Escape the window.
		self.Container.bind('<Escape>', self.quit)

	def quit(self, event):
		self.myParent.destroy()


	
	# Check for database.
	def check_connections(self, columns, tablename, database):
		if not os.path.exists(database):
			link = sqlite3.connect(database)
			curs = link.cursor()
			tmplist = []
			for i in columns:
				tmplist.append(i[0] + ' ' +  i[1])
			column_names = ', '.join(tmplist)
			curs.execute("CREATE TABLE {0} (key INTEGER PRIMARY KEY ASC, {1})".format(tablename, column_names))
			link.commit()
			curs.close()

	# Make data entry buttons.
	def make_buttons(self, parent, column_names):
		#self.colName for colName in column_names
		self.factory = {}
		for i in column_names:
			colName = i[0]
			self.factory[colName] = entry_field(self.entrycont, colName)

	
	# Next button handeler.
	def nextItem(self):
		# get data from buttons
		data = []
		for i in self.columns:
			colName = i[0]
			data.append(self.factory[colName].value())
			curs.execute(
				'INSERT INTO {0} ({1}) VALUES ({2})'.format(
					self.tablename, self.colName, self.factory[colName].value()
					))




root = Tk()
app = App(root, COLUMNS, TABLENAME, DBNAME)
root.mainloop()