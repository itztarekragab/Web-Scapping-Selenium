from selenium import webdriver
import csv

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/gp/bestsellers/books/")
names = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncate-desktop-type2 p13n-sc-truncated']")
prices = driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")
for i in names:
    print(i.text)
for i in prices:
    print(i.text)

with open('amazon_products.csv', 'w',encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Product Name','Price'])
    for i in range(1,len(names)):
        csvwriter.writerow([names[i].text,prices[i].text])