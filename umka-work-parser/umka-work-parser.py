import requests
from bs4 import BeautifulSoup
import pandas as pd


regions = 'dnipro', 'kyiv', 'odesa', 'kharkiv', 'lviv', 'zaporizhia', 'vinnytsia', 'donetsk', 'ivano-frankivsk', 'sumy', 'poltava', 'ternopil', 'kharkiv', 'kherson', 'khmelnitsk', 'cherkasy', 'chernihiv'

def parser_job_sites():
	print("Ласкаво просимо до Umka - Work parser\n")

	print("Виберіть ваш регіон")
	for region in regions:
		print(region, end = " ")
	region = input("\n > ")

	num_page = int(input("Скільки сторінок зберегти? > "))

	jobs_data = []

	for page in range(1, num_page + 1):
		url = f"https://www.work.ua/jobs-{region}/?page={page}"

		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		jobs = soup.find_all("div", class_ = "card-hover")

		for job in jobs:
			title_element = job.find("h2")
			title = title_element.text.strip("\n") if title_element else "Назви не знайдено!"
			salary_element = job.find("b", class_ = "")
			salary = salary_element.text.strip().replace("\u202f","").replace("\xa0","").replace("\u2009","") if salary_element else "Заробітна плата не вказана!"
			company_element = job.find("span")
			company = company_element.text.strip() if company_element else "Компанію не вказано!"
			link_element = job.find("a")["href"]
			link = "https://www.work.ua" + link_element

			job_data = {
				"Посади": title,
				"Заробітна плата": salary,
				"Компанії": company,
				"Посилання": link
				}

			jobs_data.append(job_data)

		print(f"••• Umka обробляє дані з {page}-ї. сторінки, чикай!")

	df = pd.DataFrame(jobs_data)

	#  Фільтри
	if input("Хочете застосувати фільтри? 1 - так, 0 - ні ") == '1':
		search_keywodrs = list(map(str, input("Фільтрація за ключовими словами (Наприклад: водій, менеджер, і т.д.) > ").split(",")))
		exclude_keywrds = list(map(str, input("Виключення за ключовими словами (Наприклад: помічник, доставка, і т.д.) > ").split(",")))

		if search_keywodrs:
			df = df[df["Посади"].str.lower().str.contains("|".join(search_keywodrs), case = False, na = False)]

		if exclude_keywrds:
			df = df[~df["Посади"].str.lower().str.contains("|".join(exclude_keywrds), case = False, na = False)]

	print(df)

	if input("Зберегти дані у файл? 1 - так, 0 - ні ") == '1':
		df.to_excel("Вакансії.xlsx", index = False)
		print("{•••} Umka: Файл успішно збережено!")

	return df


parser_job_sites()
