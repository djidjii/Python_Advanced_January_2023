import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        file = open(f"{info[0]}", "w")
        file.close()

    elif command == "Add":
        with open(f"{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"{info[0]}", "r") as file:
                text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(info[1], info[2])

            with open(f"{info[0]}", "w") as file:
                file.write("".join(text))
        except FileExistsError:
            print(f"An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"{info[0]}")
        except FileExistsError:
            print("An error occurred!")

    if command == "End":
        break
