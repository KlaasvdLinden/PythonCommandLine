import subprocess

commands = ["tweakers", "synoniemen"]


def return_command(input):
    command = "python "
    command += {
        commands[0]: " D:/Personal/Programming/Projects/Python/TweakersScraper/app.py",
        commands[1]: " D:/Personal/Programming/Projects/Python/SynoniemenZoeker/app.py"
    }[input]
    return command


print("----------------------------------")
print("|Welkom bij de Python commandline|")
print("----------------------------------")
print("Typ " + "\'" + "help" + "\'" + " om alle commando's te zien")
print("Typ " + "\'" + "exit" + "\'" + " om te stoppen")

user_input = ""

while user_input != "exit":
    user_input = input().lower()
    if user_input == "help":
        print(commands)
    elif user_input == "exit":
        break
    elif user_input not in commands:
        print("\'" + user_input + "\'" + " is niet herkend als een commando")
    else:
        subprocess.call(return_command(user_input))
