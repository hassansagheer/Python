name = input("What's your name? ")

match name:
    case "Hassan" | "Sagheer":
        print("Wellcome", name)
    case "Saad":
        print("Wellcome", name)
    case _:
        print("Who?")