import sqlite3, time


ctl = []
total_quantity = []
total_price = []
cost = []

data = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())

class UMKA_PIZZA:
	def __init__(self, db, curs):
		self.db = db
		self.curs = curs


	def pizza_list(self):
		print("\nНайменування\n")
		pizza_list = self.curs.execute("SELECT rowid, * FROM umka_admin").fetchall()
		for el in pizza_list:
			print(" •> ID: " + str(el[0]) + " • " + str(el[1]) + ": " + str(el[2]) + " ціна")


	def checkout(self):
		name = input("Ведіть им'я: ")
		address = input("Ведіть адресу: ")
		phone = input("Ведіть телефон: ")
		self.curs.execute("INSERT INTO users (data, name, address, phone) VALUES(?,?,?,?)", (data, name, address, phone))
		user_id = curs.lastrowid

		quit = True

		while quit:
			UMKA_PIZZA(db, curs).pizza_list()
			
			pizza_number_id = input("Ведіть ID піци: ")
			quantity = input("Кіликість: ")
			total_quantity.extend([int(quantity)])

			pizza_number_id = self.curs.execute("SELECT rowid, * FROM umka_admin WHERE rowid = ?", (pizza_number_id, )).fetchall()

			for p in pizza_number_id:
				cl = f"{str(p[1])} {str(p[2])} ціна, {quantity} кількість"
				ctl.extend([cl])
				total_price.extend([int(p[2])])

			pizza = ", ".join(ctl)
			if input("Хочете додати ще піцу? 1 - так, 0 - ні ") == '0':
				quit = False

		total_amount = 0
		for amo in total_quantity:
			total_amount = total_amount + amo

		t = [x*y for x,y in zip(total_price, total_quantity)]
		cost.extend(t)

		total_cost = 0
		for price in cost:
			total_cost = total_cost + price

		self.curs.execute("INSERT INTO pizzas (pizza, total_amount, total_cost) VALUES(?,?,?)", (pizza, total_amount, total_cost))
		pizza_id = curs.lastrowid
		self.curs.execute("INSERT INTO user_pizza (user_id, pizza_id) VALUES(?,?)", (user_id, pizza_id))

		print("\n • Ваше замовлення\n •\n ••• Час замовлення: " + data + "\n •> Ваше ім'я: " + name + "\n •> Ваша адресса: " + address + "\n •> Ваш телефон: " + phone + "\n •\n •••> Замовлення: " + ", ".join(ctl) + "\n •\n ••> Загальна кіликість: " + str(total_amount) + " шт.\n ••> До сплати: " + str(total_cost) + " грн.")

	
db = sqlite3.connect('umka-pizza2.db')
curs = db.cursor()
print("{•••} Ласкаво просимо до UMKA - PIZZA, у нас найсвіжиша тай найсмачніша піца :)\n")
UMKA_PIZZA(db, curs).checkout()
print("\n{•••} Ваш замовлення успішно оформлено! Очикуйте доставку.\nПриємного дня! ;)")
db.commit()
db.close()