import sqlite3


class UMKA_ADMIN:
	def __init__(self, db, curs):
		self.db = db
		self.curs = curs


	def admin_user_list(self):
		print("\n • Список клієнтів\n")
		user_id = self.curs.execute("SELECT * FROM user_pizza").fetchall()
		user_client = self.curs.execute("SELECT * FROM users").fetchall()
		user_pizza_list = self.curs.execute("SELECT * FROM pizzas").fetchall()

		if len(user_client) == 0:
			print(" {•••} Немає жодного клієнту!\n")
		else:
			for uid in user_id: 
				for cl in user_client:
					if uid[0] == cl[0]:
						client = f" ••• Час замовлення: {str(cl[1])}\n •> Ім'я: {str(cl[2])}\n •> Адреса: {str(cl[3])}\n •> Телефон: {str(cl[4])}"
				for p in user_pizza_list:
					if uid[0] == p[0]:
						pizza = f" •••> Замовлення: {str(p[1])}\n •\n ••> Загальна кілкість: {str(p[2])} шт.\n ••> До сплати: {str(p[3])} грн."
				print(client + "\n •\n" + pizza + "\n ••••••••\n")


	def admin_pizza_list(self):
		print("\n • Найменування\n")
		pizza_list_db = self.curs.execute("SELECT rowid, * FROM umka_admin").fetchall()
		if len(pizza_list_db) == 0:
			print(" {•••} Немає жодного наіменювання!\n")
		else:
			for el in pizza_list_db:
				print(" •> ID: " + str(el[0]) + " • " + str(el[1]) + ": " + str(el[2]) + " ціна")


	def admin_pizza_add(self):
		name = input("Введить назву: ")
		price = input("Введить ціну: ")
		self.curs.execute("INSERT INTO umka_admin (name, price) VALUES(?,?)", (name,price))
		UMKA_ADMIN(db, curs).admin_pizza_list()


	def admin_search(self):
		def admin_search_list(search):
			user_pizza_list = self.curs.execute("SELECT * FROM pizzas").fetchall()

			for sear in search:
				client = f" ••• Час замовлення: {str(sear[1])}\n •> Ім'я: {str(sear[2])}\n •> Адреса: {str(sear[3])}\n •> Телефон: {str(sear[4])}"
				for p in user_pizza_list:
					if sear[0] == p[0]:
						pizza = f" •••> Замовлення: {str(p[1])}\n •\n ••> Загальна кілкість: {str(p[2])} шт.\n ••> До сплати: {str(p[3])} грн."
			print(client + "\n •\n" + pizza + "\n ••••••••\n")

		print("u - По імені | t - Телефону")
		search = input(" > ")
		if search == 'u':
			search_name = input("Введить ім'я клієнта: ")
			search = self.curs.execute("SELECT * FROM users WHERE name = ?", (search_name, )).fetchall()
			admin_search_list(search)
		elif search == 't':
			search_phone = input("Введить номер телефону: ")
			search = self.curs.execute("SELECT * FROM users WHERE phone = ?", (search_phone, )).fetchall()
			admin_search_list(search)


	def admin_delete(self):
		print("u - Клієнти | p - Піца")
		delete = input(" > ")
		if delete == 'u':
			UMKA_ADMIN(db, curs).admin_user_list()

			print("ud - По імені | all - Повне видалення")
			delete = input(" > ")
			if delete == 'ud':
				name_del = input("Введить ім'я клієнта: ")
				user_delete = self.curs.execute("SELECT * FROM users WHERE name = ?", (name_del,)).fetchall()

				user_id = self.curs.execute("SELECT * FROM user_pizza").fetchall()
				user_client = self.curs.execute("SELECT * FROM users").fetchall()
				user_pizza_list = self.curs.execute("SELECT * FROM pizzas").fetchall()

				for user in user_delete:
					for p in user_pizza_list:
						if user[0] == p[0]:
							self.curs.execute("DELETE FROM pizzas WHERE rowid = ?", (p[0],))
					for u in user_client:
						if user[0] == u[0]:
							self.curs.execute("DELETE FROM users WHERE rowid = ?", (u[0],))
					for uid in user_id:
						if user[0] == uid[0]:
							self.curs.execute("DELETE FROM user_pizza WHERE rowid = ?", (uid[0],))

				print(f"[•••] Клієнта {name_del}, успішно видалено!")
			elif delete == 'all':
				self.curs.execute("DELETE FROM pizzas")
				self.curs.execute("DELETE FROM users")
				self.curs.execute("DELETE FROM user_pizza")
				print("[•••] Усіх клієнтів, успішно видалені!")
		elif delete == 'p':
			UMKA_ADMIN(db, curs).admin_pizza_list()

			print("ip - По id | all - Повне видалення")
			delete = input(" > ")
			if delete == 'ip':
				id_pizza = input("Введить id піци: ")
				self.curs.execute("DELETE FROM umka_admin WHERE rowid = ?", (id_pizza,))
				print(f"[•••] Піцу з id {id_pizza}, успішно видалено!")
			elif delete == 'all':
				self.curs.execute("DELETE FROM umka_admin")
				print("[•••] Увесь список піц, успішно видалено!")


db = sqlite3.connect('umka-pizza2.db')
curs = db.cursor()
print("cl - Перелік замовлень | s - Пошук | pl - Перелік піц | add - Додати піццу | del - Видалення")
command = input(" > ")
if command == 'cl':
	UMKA_ADMIN(db, curs).admin_user_list()
if command == 's':
	UMKA_ADMIN(db, curs).admin_search()
elif command == 'pl':
	UMKA_ADMIN(db, curs).admin_pizza_list()
elif command == 'add':
	UMKA_ADMIN(db, curs).admin_pizza_add()
elif command == 'del':
	UMKA_ADMIN(db, curs).admin_delete()
db.commit()
db.close()