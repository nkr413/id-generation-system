import random, time
from datetime import datetime
from random import randint

def main():
	symbols = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f","g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

	data = int(datetime.now().strftime('%Y%m%d%H%M%S'))
	data = hex(data)
	result = [i for i in data]
	result.append("-")

	yet = int(0)
	if len(data) < 29: yet = 29 - len(data)

	for i in range(0, yet):
		int_or_str = randint(0, 1)

		if int_or_str == 1:
			new_int = randint(0, 9)
			result.append(str(new_int))
		else: 
			rand_s = random.choice(symbols)
			high_or_low = randint(0, 1)

			if high_or_low == 1: rand_s = rand_s.upper()
			else: rand_s = rand_s.lower()

			result.append(rand_s)

	base = "".join(result)	
	print(base)

main()

