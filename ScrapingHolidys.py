from selenium import webdriver
import csv

driver = webdriver.Firefox()
driver.get("https://www.sos.ca.gov/state-holidays")
days = driver.find_elements_by_xpath("//td[1]")
holidays = driver.find_elements_by_xpath("//td[2]")
for i in days:
    print(i.text)
for i in holidays:
    print(i.text)

with open('Holidays.csv', 'w',encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Day','Holiday'])
    for i in range(1,len(days)):
        csvwriter.writerow([days[i].text,holidays[i].text])
