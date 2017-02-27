def computer_guess(num):
	low = 1
	high = 1000
	guess = 500
	while guess != num:
		guess = (low + high)//2
		print('Computer take a guess...', guess)
		if guess > num:
			high = guess
		elif guess < num:
			low = guess + 1

		print('The computer took a guess', guess , ' and it was correct!')

def main():
	num = int(input('Enter a number:  '))
	if num < 1 or num > 1000:
		print('Must be in range [1,1000]')
	else:
		computer_guess(num)

if __name__ == '__main__':
	main()


