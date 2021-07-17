import requests
print(""
    "\n______ ____________________ ______  _________" 
    "\n___  / __  __ \_  __ \__  //_/_  / / /__  __ \ "
    "\n__  /  _  / / /  / / /_  ,<  _  / / /__  /_/ /"
    "\n_  /___/ /_/ // /_/ /_  /| | / /_/ / _  ____/" 
    "\n/_____/\____/ \____/ /_/ |_| \____/  /_/            ")

print("LOOKUP v.1.0 - a free web scraper made with python.")
user_input1 = input("do you want to continue? y/n ")

if user_input1 == "n":
    print("Thanks for using the application! You can close the terminal.")

if user_input1 == "y":
    user_input2 = input("website:")
    print("1 - view the source code of the page")
    print("2 - view the headers of the page")
    print("3 - view the status code of the page")
    print("4 - save the picture")
    user_input3 = input("you can choose 4 options:")
    if user_input3 == "1":
        # getting text (source code of the page)
        r1 = requests.get(f'{user_input2}')
        print(r1.text)
    elif user_input3 == "2":
        # getting headers
        r2 = requests.get(f'{user_input2}')
        print(r2.headers)
    elif user_input3 == "3":
        r3 = requests.get(f'{user_input2}')
        # status code
        print(r3.status_code)
    elif user_input3 == ("4"):
        r4 = requests.get(user_input2)
        with open ("python.png","wb") as f:
            f.write(r4.content)
    else:
        print("ERROR:please enter the number from 1 to 4.")


