import webbrowser as wb

while True:
    search = str(input("Search: "))
    wb.open("https://www.bing.com/search?PC=U523&q={}&pglt=2083&FORM=ANNTA1".format(search))