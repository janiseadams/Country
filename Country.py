

def mainmenu():
    print("COMMAND MENU")
    print("View - View country name")
    print("Add  - Add a country")
    print("Del  - Delete a country")
    print("Exit - Exit program")
    print()


def displaycodes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country Codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)


def view(countries):
    displaycodes(countries)
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country Name: {name}.\n")
    else:
        print("There Is No Country With That Code.\n")


def add(countries):
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} Is Already Using This Code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} Was Added.\n")


def delete(countries):
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} Was Deleted.\n")
    else:
        print("There Is No Country With That Code.\n")

def main():
    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico"}
    
    mainmenu()
    while True:        
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)   
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)  
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not A Valid Command. Please Try Again.\n")


if __name__ == "__main__":
    main()
