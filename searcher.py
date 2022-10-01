import webbrowser as wb


def choose():
    browser = input("Choose wich browser you want to use(yandex/google/bing)")
    if browser != "yandex" and browser != "google" and browser != "bing":
        print("Browser doesn't recognized, try again.")
        choose()
    elif browser == "yandex" or browser == "google" or browser == "bing":

        while True:
            search = str(input("Search: "))
            if browser == "bing":
                wb.open(
                    "https://www.bing.com/search?PC=U523&q={}&pglt=2083&FORM=ANNTA1".format(search))
            if browser == "yandex":
                wb.open(
                    "https://yandex.com/search/?text={}&lr=10262".format(search))
            if browser == "google":
                wb.open(
                    "https://www.google.com/search?q={}".format(search))


if __name__ == "__main__":
    choose()
