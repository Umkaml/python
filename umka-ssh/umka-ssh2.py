import os, sqlite3


quit = True

db = sqlite3.connect('umka_ssh2.db')
c = db.cursor()
#c.execute("""CREATE TABLE umka_ssh(name text, user_name text, ip_addr text, password text)""")

def add():
	name = input("Введіть назву з'єднання: ")
	user_name = input("Введіть ім'я користувача: ")
	ip_addr = input("Введіть ip адресу: ")
	password = input("Введіть пароль: ")

	c.execute(
		"INSERT INTO umka_ssh(name, user_name, ip_addr, password)"
		"VALUES(?,?,?,?)",(name, user_name, ip_addr, password)
		)
	print("\nЗ'єднання успішно збереженно! Назва з'єднання: " + name + " •> ssh • " + user_name + "@" + ip_addr)

	if input("\nХочете приєднатись зараз 1 - так, 0 - ні ") == '1':
		os.system("ssh " + user_name + "@" + ip_addr)


def connect_list():
	print("Щоб повернутись до головного меню натисніть Enter\n")
	print("Список контактів")
	connect = c.execute("SELECT rowid, * FROM umka_ssh").fetchall()
	if len(connect) == 0:
		print(" {•••} Немає жодного контакту!")
	else:
		for con_list in connect:
			print(" id: " + str(con_list[0]) + " • " + str(con_list[1]) + " •> " + str(con_list[2]) + "@" + str(con_list[3]))


def connect():
	connect_list()

	connect_ssh = input("\nВведіть ID пітключення: ")
	connect = c.execute("SELECT rowid, * FROM umka_ssh WHERE rowid = ?", (connect_ssh, )).fetchall()
	for con_list in connect:
		print("\n •> " + str(con_list[1]) + ": ssh • " + str(con_list[2]) + "@" + str(con_list[3]) + "\n Пароль: " + str(con_list[4]) + "\n")
		os.system("ssh " + str(con_list[2]) + "@" + str(con_list[3]))


def delete():
	connect_list()

	print("\ndelid - видалення по id, delall - повне видалення")

	delete = input("•> ")
	if delete == 'delid':
		delete = input("Введіть ID: ")
		c.execute("DELETE FROM umka_ssh WHERE rowid = ?", (delete, ))
		print(" {•••} Контакт успішно видаленно!")
	elif delete == 'delall':
		c.execute("DELETE FROM umka_ssh")
		print(" {•••} Всі коннтакти видаленно!")


while quit:
	print("\nadd - додати з'єднання, con - приєднатись, del - видалення, q - вийти")
	g = input("Чого ви хочете: ")
	if g == 'add':
		add()
	if g == 'con':
		connect()
	if g == 'del':
		delete()
	if g == 'q':
		print("Приємного дня!")
		quit = False

db.commit()
db.close()