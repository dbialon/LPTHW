from sys import exit

## define a function beers_and_wines
def beers_and_wines(number_of_beers, number_of_wines):
	print(f"\nAltogether we have {number_of_beers} beers and {number_of_wines} wines.")
	print("Boy, we're gonna have a helluva party!\n")
	
## there are three people coming to a party
## each brings something
dave_b = 3
dave_w = 2
print(f"\nDave has {dave_b} beers and {dave_w} wines.")
joe_b = 2
joe_w = 2
print(f"Joe has {joe_b} beers and {joe_w} wines.")
eddie_b = 2
eddie_w = 4
print(f"Eddie has {eddie_b} beers and {eddie_w} wines.\n")

## now we ask if each one of them comes to the party
dave_comes = input("Is Dave coming to the party? (yes or no) ")
joe_comes = input("Is Joe comming to the party? ")
eddie_comes = input("Is Eddie comming to the party? ")

# check who's coming and who's not
if dave_comes == "no":
	dave_b = dave_w = 0
elif dave_comes != "yes":
	exit("\nI didn't understand your answers.\n")

if joe_comes == "no":
	joe_b = joe_w = 0
elif joe_comes != "yes":
	exit("\nI didn't understand your answers.\n")

if eddie_comes == "no":
	eddie_b = eddie_w = 0
elif eddie_comes != "yes":
	exit("\nI didn't understand your answers.\n")

if dave_comes == joe_comes == eddie_comes == "no":
		exit("\nNobody's coming so there is no party.\n")

beers_sum = dave_b + joe_b + eddie_b
wines_sum = dave_w + joe_w + eddie_w

beers_and_wines(beers_sum, wines_sum)