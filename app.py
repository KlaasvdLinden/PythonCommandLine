import subprocess

# commands = ["tweakers", "synoniemen"]

# def return_command(input):
#     command = "python "
#     command += {
#         commands[0]: " D:/Personal/Programming/Projects/Python/TweakersScraper/app.py",
#         commands[1]: " D:/Personal/Programming/Projects/Python/SynoniemenZoeker/app.py"
#     }[input]
#     return command


def return_exec(input):
    my_file = open("D:\Personal\Programming\Projects\Python\PythonCommandLine\commands.txt", "r")
    for line in my_file:
        data = line.split(",")
        if data[0] == input:
            my_file.close()
            return data[1].strip()
    my_file.close()


def return_all_commands():
    commands = []
    my_file = open("D:\Personal\Programming\Projects\Python\PythonCommandLine\commands.txt", "r")
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

    my_file = open("D:\Personal\Programming\Projects\Python\PythonCommandLine\commands.txt", "a")
    my_file.write(data[1] + ", " + " ".join(data[2:len(data)]))
    my_file.write("\n")
    my_file.close()


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
    elif user_input not in all_commands:
        print("\'" + user_input + "\'" + " is niet herkend als een commando")
    else:
        subprocess.call(return_exec(user_input))
