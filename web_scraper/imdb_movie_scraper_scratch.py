import requests

from bs4 import BeautifulSoup


def main():

    target_url = take_input_url()

    if check_domain('www.imdb.com', target_url):
        response = get_request(target_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        if is_this_movie(soup):
            title = fetch_movie_title(soup)
            description = fetch_movie_description(soup)
            result = {'title': title, 'description': description}
            print(result)

        else:
            quit_with_error()
    else:
        quit_with_error()


def take_input_url():
    return input("Input the URL:\n")


def check_domain(domain, url):
    return domain in url


def get_request(url):
    return requests.get(url,
                        headers={'Accept-Language': 'en-US,en;q=0.5'})


def is_this_movie(soup):

    meta_type = soup.find('meta', {'property': 'og:type'})
    return 'video' in meta_type['content']


def fetch_movie_title(soup):
    title_tag = soup.find('meta', {'property': 'og:title'})
    title = title_tag['content']
    strip_start_index = title.index("(")
    title = title[0:strip_start_index - 1]
    return title


def fetch_movie_description(soup):
    description_tag = soup.find('div', {'class': 'summary_text'})
    content = description_tag.text
    content = content.strip()
    return content


def quit_with_error():
    print("Invalid movie page!")
    return None


def make_get_request(url):
    return requests.get(url)


if __name__ == '__main__':
    main()

