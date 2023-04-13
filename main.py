from termcolor import colored
import requests
from bs4 import BeautifulSoup

print("\nWellcome to Book Finder!")

is_running = True
while is_running:
    book = input(
        f"""\nSearch book in Google {colored("[-1] to exit: ", "yellow")}: """)

    if book == "-1":
        is_running = False
    else:
        URL = f"https://www.google.com/search?tbm=bks&q={book}"
        response = requests.get(URL)
        response_code = response.status_code
        html_code = response.text

        if response_code == 200:
            soup = BeautifulSoup(html_code, "html.parser")

            # registros etiquetas
            book_title_div_tags = soup.find_all(
                'div', {'class': 'BNeawe vvjwJb AP7Wnd'})

            print(colored("\nBooks found:", "yellow"))
            for i, div in enumerate(book_title_div_tags):
                print(colored(i+1, "red"), colored(div.string, "cyan"))

            is_running_2 = True
            while is_running_2:
                choice = input("\nDo you want to search other book? [y/n]: ")

                if choice == "n":
                    is_running = False
                    is_running_2 = False
                elif choice == "y":
                    is_running_2 = False
                else:
                    print("That's not an option...")

print("\nThanks for trying!")
