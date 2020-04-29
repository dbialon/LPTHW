from sys import argv, exit

if len(argv) != 4:
    print("Invalid input. Provide 3 variables.")
    exit(1)

script, first, second, third = argv

fourth = input("\nWhat is your fourth variable? ")
fifth = input("What is your fifth variable? ")
sixth = input("What is your fifth variable? ")

print(f"\nThe script is called {script} and your variables are in order:")
print(f"\t* {first} \n\t* {second} \n\t* {third} \n\t* {fourth} \n\t* {fifth} \n\t* {sixth}\n")

exit(0)