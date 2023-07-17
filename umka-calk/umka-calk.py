while exit:
	number_1=int(input('введите первое чесло: '))
	number_2=int(input('введите второе чесло: '))
	sing=input('введите знак [+, -, *, /, **, %]: ')

	if sing == '+':
		r=number_1 + number_2
		p='сложение'
		t=p
	elif sing == '-':
		r=number_1 - number_2
		p='вичетание'
		t=p
	elif sing == '*':
		r=number_1 * number_2
		p='умножение'
		t=p
	elif sing == '/':
		r=number_1 / number_2
		p='деление'
		t=p
	elif sing == '**':
		r=number_1 ** number_2
		p='возведение в степень'
		t=p
	elif sing == '%':
		r=number_1 % number_2
		p='остаток от деление'
		t=p

	print("#===≠===#")
	print("{•••} результат", t, "=", r, p)
	print("#===≠===#")


	if exit:
		print("#===!===#")
		print("хотите продолжить работу? да, нет")
		ex=input("!> ")

		if ex == 'да':
			exit=True
			print("{•••} Дочтопочтенные кроты, пощитаем;)")
		elif ex == 'нет':
			exit=False
			print("{•••} Хорошего дня:)")
