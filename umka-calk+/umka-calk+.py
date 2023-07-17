def speed():
	print("\n • 1 - км/год в миль/год")
	print(" • 2 - миль/год в км/год")
	print(" • 3 - км/с в м/с")
	print(" • 4 - м/с в км/с")
	print(" • 5 - км/год в км/с")
	print(" • 6 - км/с в км/год")
	print(" • 7 - миль/год в км/с")
	print(" • 8 - км/с в миль/год")
	
	spd = int(input("Виберіть, що ви хочете перетворити: "))
	
	if spd == 1:
		kmh = int(input("Введіть км/год: "))
		mph = kmh * 0.621371
		text_result = "Ваш результат перетворення км/год в миль/год:"
		rounded_result = round(mph, 1)
	elif spd == 2:
		mph = int(input("Введіть миль/год: "))
		kmh = mph * 1.60934
		text_result = "Ваш результат перетворення миль/год в км/год:"
		rounded_result = round(kmh, 1)
	elif spd == 3:
		kms = int(input("Введіть км/с: "))
		ms = kms * 1000
		text_result = "Ваш результат перетворення км/с в м/с:"
		rounded_result = round(ms, 1)
	elif spd == 4:
		ms = int(input("Введіть м/с: "))
		kms = ms / 1000
		text_result = "Ваш результат перетворення м/с в км/с:"
		rounded_result = round(kms, 1)
	elif spd == 5:
		kmh = int(input("Введіть км/год: "))
		kms = kmh / 3600
		text_result = "Ваш результат перетворення км/год в км/с:"
		rounded_result = round(kms, 4)
	elif spd == 6:
		kms = float(input("Введіть км/с: "))
		kmh = kms * 3600
		text_result = "Ваш результат перетворення км/с в км/год:"
		rounded_result = round(kmh, 1)
	elif spd == 7:
		mph = int(input("Введіть миль/год: "))
		kms = mph * 1.60934 * 0.000277777777778
		text_result = "Ваш результат перетворення миль/год в км/с:"
		rounded_result = round(kms, 7)
	elif spd == 8:
		kms = int(input("Введіть км/с: "))
		mph = kms * 0.621371 * 3600
		text_result = "Ваш результат перетворення км/с в миль/год:"
		rounded_result = round(mph, 1)

	print("\n{•••} " + text_result + " " + str(rounded_result) + "\n")


def imt():
	print("\nВітаємо у програмі розраховування вашої ідеальної ваги, просимо ознайомитись із значеннями")
	print("Показник ІМТ Відповідність маси тіла:")
	print("<18,5 - недостатня вага")
	print("18,5 – 24,9 - нормальна вага")
	print("25 – 29,9 наявність зайвої ваги")
	print(">30 - ожиріння")
	
	quit = True

	while quit:
		try:
			wei = int(input("Введіть свою вагу: "))
		except ValueError:
			print("\n{•••} Введіть цисло!\n")
		else:
			if wei > 250:
				print("\n{•••} Вага яку ви ввели перевищує ліміти, будь ласка, перевірте, чи правильно ввели\n")
				return wei
			elif wei < 20:
				print("\n{•••} Вага яку ви ввели недостатня, будь ласка перевірте, чи правильно ви ввели\n")
				return wei
			elif wei > 20 < 250:
				hei = int(input("Введіть свій зріст: "))

				if hei > 250:
					print("\n{•••} Зріст котрий ви ввели перевищує ліміт, будь ласка, перевірте чи правильно ви написали\n")
					return hei
				elif hei < 80:
					print("\n{•••} Зріст котрий ви ввели недостатній, будь ласка, перевірте, чи правильно ви написали\n")
					return hei

				quit = False
	
	hei2 = hei / 100
	res = hei2 * hei2
	res2 = wei / res
	rounded_result = round(res2, 1)
	
	print("\n{•••} Ваш IMT : " + str(rounded_result))
	
	if rounded_result < 18.5:
		print ("•> У вас недостатня вага\n")
	elif rounded_result > 30:
		print("•> У вас ожиріння\n")
	elif 18.5 <= rounded_result < 25:
		print("•> У вас нормальна вага\n")
	elif 25 <= rounded_result < 29.9:
		print("•> У вас наявніть зайвої ваги\n")


def temp():
	print("\n • 1 - °F (Фаренгейт)")
	print(" • 2 - °C (Цельсій)")
	print(" • 3 - °R (Ранкін)")
	print(" • 4 - °Re (Реомюр)")
	print(" • 5 - K (Кельвін)")

	temp = int(input("Виберіть, з чого ви хочете перетворити: "))

	if temp == 1:
		print("\n • 1 - °C (Цельсій)")
		print(" • 2 - °R (Ранкін)")
		print(" • 3 - °Re (Реомюра)")
		print(" • 4 - K (Кельвін)")

		fare = int(input("Виберіть, в що ви хочете перетворити: "))

		if fare == 1:
			far = int(input("Введіть ваш °F: "))
			cel = (far - 32) * 5 / 9
			rounded_result = round(cel, 1)
			text_result = "°C"
		elif fare == 2:
			far = int(input("Введіть ваш °F: "))
			ran = far + 459.67
			rounded_result = round(ran, 1)
			text_result = "°R"
		elif fare == 3:
			far = int(input("Введіть ваш °F: "))
			reo = (far - 32) * 4 / 9
			rounded_result = round(reo, 1)
			text_result = "°Re"
		elif fare == 4:
			far = int(input("Введіть ваш °F: "))
			kel = (far + 459.67) * 5 / 9
			rounded_result = round(kel, 1)
			text_result = "K"

	elif temp == 2:
		print("\n • 1 - °F (Фаренгейти)")
		print(" • 2 - °R (Ранкіна)")
		print(" • 3 - °Re (Реомюра)")
		print(" • 4 - K (Кельвіна)")

		celc = int(input("Виберіть, в що ви хочете перетворити: "))

		if celc == 1:
			cel = int(input("Введіть ваш °C: "))
			far = (cel * 9 / 5) + 32
			rounded_result = round(far, 1)
			text_result = "°F"
		elif celc == 2: 
			cel = int(input("Введіть ваш °C: "))
			ran = (cel + 273.15) * 9 / 5
			rounded_result = round(ran, 1)
			text_result = "°R"
		elif celc == 3:
			cel = int(input("Введіть ваш °C: "))
			reo = cel * 4 / 5
			rounded_result = round(reo, 1)
			text_result = "°Re"
		elif celc == 4:
			cel = int(input("Введіть ваш °C: "))
			kel = cel + 273.15
			rounded_result = round(kel, 1)
			text_result = "K"

	elif temp == 3:
		print("\n • 1 - °F (Фаренгейти)")
		print(" • 2 - °C (Цельсій)")
		print(" • 3 - °Re (Реомюра)")
		print(" • 4 - K (Кельвіна)")
		
		rank = int(input("Виберіть, в що ви хочете перетворити: "))

		if rank == 1:
			ran = int(input("Введіть ваш °R: "))
			far = ran - 459.67
			rounded_result = round(far, 1)
			text_result = "°F"
		elif rank == 2: 
			ran = int(input("Введіть ваш °R: "))
			cel = (ran -491.67) * 5 / 9
			rounded_result = round(cel, 1)
			text_result = "°C"
		elif rank == 3:
			ran = int(input("Введіть ваш °R: "))
			reo = (ran - 491.67) * 4 / 9
			rounded_result = round(reo, 1)
			text_result = "°Re"
		elif rank == 4:
			ran = int(input("Введіть ваш °R: "))
			kel = (ran - 459.67) * 5 / 9 + 273.15
			rounded_result = round(kel, 1)
			text_result = "K"

	elif temp == 4:
		print("\n • 1 - °F (Фаренгейти)")
		print(" • 2 - °C (Цельсій)")
		print(" • 3 - °R (Ранкіна)")
		print(" • 4 - K (Кельвіна)")
		
		reom = int(input("Виберіть, в що ви хочете перетворити: "))

		if reom == 1:
			reo = int(input("Введіть ваш °Re: "))
			far = reo * 9 / 4 + 32
			rounded_result = round(far, 1)
			text_result = "°F"
		elif reom == 2:
			reo = int(input("Введіть ваш °Re: "))
			cel = reo * 5 / 4
			rounded_result = round(cel, 1)
			text_result = "°C"
		elif reom == 3:
			reo = int(input("Введіть ваш °Re: "))
			ran = (reo + 273.15) * 9 / 4
			rounded_result = round(ran, 1)
			text_result = "°R"
		elif reom == 4: 
			reo = int(input("Введіть ваш °Re: "))
			kel = reo * 5 / 4 + 273.15
			rounded_result = round(kel, 1)
			text_result = "K"

	elif temp == 5:
		print("\n • 1 - °F (Фаренгейти)")
		print(" • 2 - °C (Цельсій)")
		print(" • 3 - °R (Ранкіна)")
		print(" • 4 - °Re (Реомюра)")

		kelv = int(input("Виберіть, в що ви хочете перетворити: "))

		if kelv == 1:
			kel = int(input("Введіть ваш K: "))
			far = kel * 9 / 5 - 459.67
			rounded_result = round(far, 1)
			text_result = "°F"
		elif kelv == 2:
			kel = int(input("Введіть ваш K: "))
			cel = kel - 273.15
			rounded_result = round(cel, 1)
			text_result = "°C"
		elif kelv == 3:
			kel = int(input("Введіть ваш K: "))
			ran = kel * 9 / 5
			rounded_result = round(ran, 1)
			text_result = "°R"
		elif kelv == 4:
			kel = int(input("Введіть ваш K: "))
			reo = (kel - 273.15) * 4 / 5
			rounded_result = round(reo, 1)
			text_result = "°Re"

	print("\n{•••} " + str(rounded_result) + " " + text_result + "\n")


def massa():
	print("\n • 1 - Кілограм(кг)")
	print(" • 2 - Грам (г)")
	print(" • 3 - Міліграм (мг)")
	print(" • 4 - Тонна (т)")

	mas = int(input("Виберіть, що ви хочете перетворити: "))

	if mas == 1:
		print(" • 1 - Грам (г)")
		print(" • 2 - Міліграм (мг)")
		print(" • 3 - Тонна (т)")
	
		kgm = int(input("Виберіть, в що ви хочете перетворити: "))
		
		if kgm == 1:
			kgm1 = int(input("Введіть ваш Кг: "))
			grm = kgm1 * 1000
			rounded_result = round(grm, 1)
			text_result = "г"
		elif kgm == 2:
			kgm2 = int(input("Введіть ваш Кг: "))
			mgr = kgm2 * 1000000
			rounded_result = round(mgr, 1)
			text_result = "мг"
		elif kgm == 3:
			kgm3 = int(input("Введіть ваш Кг: "))
			ton = kgm3 / 1000
			rounded_result = round(ton, 1)
			text_result = "т"

	elif mas == 2:
		print("\n • 1 - Кілограм(кг)")
		print(" • 2 - Міліграм (мг)")
		print(" • 3 - Тонна (т)")

		grm = int(input("Виберіть, в що хочете перетворити: "))
    
		if grm == 1:
			grm1 = int(input("Введіть ваш Г: "))
			kgm1 = grm1 / 1000
			rounded_result = round(kgm1, 2)
			text_result = "кг"
		elif grm == 2:
			grm1 = int(input("Введіть ваш Г: "))
			mgr1 = grm1 * 1000
			rounded_result = round(mgr1, 1)
			text_result = "мг"
		elif grm == 3:
			grm1 = int(input("Введіть ваш Г: "))
			ton1 = grm1 / 1000000
			rounded_result = round(ton1, 1)
			text_result = "т"
    
	elif mas == 3:
		print("\n • 1 - Кілограм (кг)")
		print(" • 2 - Грам (г)")
		print(" • 3 - Тонна (т)")

		mgr = int(input("Виберіть, в що ви хочете перетворити: "))

		if mgr == 1:
			print()
			mgr1 = int(input("Введіть ваш Мг: "))
			kgm1 = mgr1 / 1000000
			rounded_result = round(kgm, 2)
			text_result = "кг"
		elif mgr == 2:
			mgr1 = int(input("Введіть ваш Мг: "))  
			grm1 = mgr1 / 1000
			rounded_result = round(grm1, 1)
			text_result = "г"
		elif mgr == 3:
			mgr1 = int(input("Введіть ваш Мг: "))
			ton1 = mgr1 / 1000000000
			rounded_result = round(ton1, 7)  
			text_result = "т"
	
	elif mas == 4:
		print("\n • 1 - Кілограм (кг)")
		print(" • 2 - Грам (г)")
		print(" • 3 - Міліграм (мг)")

		ton = int(input("Виберіть, в що ви хочете перетворити: "))

		if ton == 1:
			ton1 = int(input("Введіть ваш Т: "))
			kgm1 = ton1 * 1000
			rounded_result = round(kgm1, 2)
			text_result = "кг"
		elif ton == 2:
			ton1 = int(input("Введіть ваш Т: "))
			grm1 = ton1 * 1000000
			rounded_result = round(grm1, 1)
			text_result = "г"
		elif ton == 3:
			ton1 = int(input("Введіть ваш Т: "))
			mgr1 = ton1 * 1000000000
			rounded_result = round(mgr1, 1)
			text_result = "мг"

	print("\n{•••} " + str(rounded_result) + " " + text_result + "\n")


quit = True

while quit:
	print("Вітаємо у Umka - Calculator+\n")
	print(" • 1 - Швидкість")
	print(" • 2 - ІМТ")
	print(" • 3 - Температура")
	print(" • 4 - Маса")
	print("\n • 5 - Вихіт")

	enter = int(input("Виберіть, що вам потрібно: "))

	if enter == 1:
		speed()
	elif enter == 2:
		imt()
	elif enter == 3:
		temp()
	elif enter == 4:
		massa()
	elif enter == 5:
		print("Приємного дня... :)")
		quit = False