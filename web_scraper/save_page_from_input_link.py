import requests


def main():

    target_url = take_input_url()
    response = requests.get(target_url)
    response_code = response.status_code
    if response_code == 200:
        save_page_data(response)
    else:
        quit_with_error(response_code)


def take_input_url():
    return input("Input the URL:\n")


def get_request(url):
    return requests.get(url,
                        headers={'Accept-Language': 'en-US,en;q=0.5'})


def save_page_data(response):
    page_content = response.content
    with open('source.html', 'wb') as save_file:
        save_file.write(page_content)
    print('Content saved.')


def quit_with_error(code):
    print("The URL returned" + str(code))
    return None


def make_get_request(url):
    return requests.get(url)


if __name__ == '__main__':
    main()
