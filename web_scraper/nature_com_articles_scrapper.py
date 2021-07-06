import requests
import string
import os
from bs4 import BeautifulSoup

DOMAIN = "https://www.nature.com"
MAIN_URL = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) "
                  "Gecko/20100101 Firefox/89.0"
}


def main():

    pages_amount = take_pages_amount()
    article_type = take_article_type()

    for page_number in range(1, pages_amount + 1):
        url_to_parse = MAIN_URL + str(page_number)

        main_request = requests.get(url_to_parse, HEADERS)

        if is_url_accessible(main_request):
            page_dir_name = "Page_" + str(page_number)

            if os.path.exists(page_dir_name) is False:
                os.mkdir(page_dir_name)

            articles_soup = BeautifulSoup(main_request.content, 'html.parser')
            articles = articles_soup.find_all(
                "li", class_="app-article-list-row__item")

            article_links = scrap_articles_links(articles, article_type)
            scrap_articles_content(article_links, page_dir_name)
        else:
            print("The" + MAIN_URL + "returned "
                  + str(main_request.status_code) + "!")


def take_pages_amount():
    return int(input())


def take_article_type():
    return str(input())


def is_url_accessible(request):
    return request.status_code == 200


def scrap_articles_links(tags_to_scrap, target_article_type):
    links_container = {}
    for item in tags_to_scrap:
        article_type = item.find("span", class_="c-meta__type")
        if article_type.text != target_article_type:
            continue

        article_link = DOMAIN + item.find(
            "a", class_="c-card__link u-link-inherit").get("href")

        raw_article_name = item.find(
            "a", class_="c-card__link u-link-inherit").text

        pretty_article_name = raw_article_name.translate(
            str.maketrans(' ', '_', string.punctuation))

        links_container[pretty_article_name] = article_link
    return links_container


def scrap_articles_content(article_links, where_to_save):
    for article_name in article_links:
        link = article_links[article_name]
        article_request = requests.get(link, HEADERS)

        if is_url_accessible(article_request):
            article_soup = BeautifulSoup(
                article_request.content, 'html.parser')
            article_body = article_soup.find("div", {"class": ["c-article-body", "article-item__body"]})
            if article_body is not None:
                article_body_content = article_body.text.strip()
            else:
                continue
            article_body = "!Error!"

            save_article(article_body_content, article_name, where_to_save)
        else:
            print("The" + link + "returned " + str(
                article_request.status_code) + "!")


def save_article(content, file_name, where_to_save):
    with open(f"{where_to_save}/{file_name}.txt", "w", encoding='utf-8') as file:
        file.write(content)
    print(f"The article content was saved successfully in file: "
          f"{where_to_save}/{file_name}.txt\n")


if __name__ == '__main__':
    main()
