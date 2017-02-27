import random

guessesTaken = 0

print('Hey man whats your name?')
myName = raw_input()

number = random.randint(1, 1000)
print('Well, ' + myName + ', I am thinking of a  Secret number between 1 and 1000. ')

while guessesTaken <15:
	print('Take a wild guess')
	guess = input()
	guess = int(guess)

	guessesTaken = guessesTaken + 1

	if guess < number:
 		print('Sorry thats too low')

	if guess > number:
		print('Sorry man thats too high')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Congrats big man,' + myName + '! You guessed my secret number in' +guessTaken+ ' guesses!')

	if guess !=number:
		number = str(number)
		print('Sorry your SOL and didnt guess my secret number. The number was' + number)
