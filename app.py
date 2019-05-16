import subprocess
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_commands = os.path.join(ROOT_DIR, 'commands.txt')


def return_exec(input):
    my_file = open(path_commands, "r")
    for line in my_file:
        data = line.split(",")
        if data[0] == input:
            my_file.close()
            return data[1].strip()
    my_file.close()


def return_all_commands():
    commands = []
    my_file = open(path_commands, "r")
    for line in my_file:
        data = line.split(",")
        commands.append(data[0])
    my_file.close()
    return commands


def add_command(input, existing_commands):
    data = input.split(" ")
    if len(data) < 3:
        print("Incorrecte syntax")
        print("De syntax is: " + "\'" + "add" + "\'" + " [commando] " + "[actie]")
        return
    if data[1] in existing_commands:
        print("Het commando" + "\'" + data[1] + "\'" + " bestaat al")
        return
    if data[2] != "python":
        print("Het command is geen python command")
        return

    my_file = open(path_commands, "a")
    my_file.write(data[1] + ", " + " ".join(data[2:len(data)]))
    my_file.write("\n")
    my_file.close()


def remove_command(input, existing_commands):
    data = input.split(" ")
    if len(data) != 2:
        print("Incorrecte syntax")
        print("De syntax is: " + "\'" + "remove" + "\'" + " [commando] ")
        return
    if data[1] not in existing_commands:
        print("Het commando" + "\'" + data[1] + "\'" + " bestaat niet")
        return

    with open(path_commands, "r") as f:
        lines = f.readlines()
    with open(path_commands, "w") as f:
        for line in lines:
            if data[1] not in line.strip("\n"):
                f.write(line)


all_commands = return_all_commands()
print("----------------------------------")
print("|Welkom bij de Python commandline|")
print("----------------------------------")
print("Typ " + "\'" + "help" + "\'" + " om alle commando's te zien")
print("Typ " + "\'" + "add" + "\'" + " [commando] " + "[actie] " + " om een commando toe te voegen")
print("Typ " + "\'" + "exit" + "\'" + " om te stoppen")

user_input = ""

while user_input != "exit":
    user_input = input().lower()
    if user_input == "help":
        print(all_commands)
    elif user_input == "exit":
        break
    elif "add" in user_input:
        add_command(user_input, all_commands)
        all_commands = return_all_commands()
    elif "remove" in user_input:
        remove_command(user_input, all_commands)
        all_commands = return_all_commands()
    elif user_input not in all_commands:
        print("\'" + user_input + "\'" + " is niet herkend als een commando")
    else:
        subprocess.call(return_exec(user_input))
