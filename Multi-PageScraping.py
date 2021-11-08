from selenium import webdriver
import csv
import re

csvfile=open('books_scraping.csv', 'w',encoding='utf-8')
csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(['Name','Genre','Price','Tax','Description','UPC','Available Copies','Rating (from Five)'])

driver = webdriver.Firefox()

for i in range(1,51):
    mainPage_link=f"http://books.toscrape.com/catalogue/page-{i}.html"
    driver.get(mainPage_link)
    page_books = driver.find_elements_by_xpath("//div[@class='image_container']")
    page_books_links = []
    for i in range(len(page_books)):
        book=page_books[i]
        book_link = book.find_element_by_tag_name("a").get_property("href")
        page_books_links.append(book_link)

    for book_link in page_books_links :
        driver.get(book_link)
        book_name = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/h1[1]").text
        book_genre = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[1]/ul[1]/li[3]/a[1]")[0].text
        book_price = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/p[1]").text
        book_tax = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/table[1]/tbody[1]/tr[5]/td[1]").text
        book_description = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/p[1]").text
        book_upc = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/table[1]/tbody[1]/tr[1]/td[1]").text
        copies_available = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/table[1]/tbody[1]/tr[6]/td[1]").text
        copies_available = re.findall("\d+",copies_available)[0]
        book_rating = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/p[3]").get_attribute("class")
        book_rating = book_rating.split()[1]
        csvwriter.writerow([book_name,book_genre,book_price,book_tax,book_description,book_upc,copies_available,book_rating])

csvfile.close()
