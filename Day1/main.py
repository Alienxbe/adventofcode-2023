digits_str = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
]

# s[0] here is s[i] in find_digit()
def is_digit_str(s: str):
	for digit in digits_str:
		if (s[:len(digit)] == digit):
			return digits_str.index(digit)
	return None

def find_digits(s: str):
	first, second = 0, 0
	for i in range(len(s)):
		if (s[i].isdigit()):
			first = s[i]
			break
		elif (is_digit_str(s[i:])):
			first = is_digit_str(s[i:])
			break
	for i in range(len(s) - 1, -1, -1):
		if (s[i].isdigit()):
			second = s[i]
			break
		elif (is_digit_str(s[i:]) != None):
			second = is_digit_str(s[i:])
			break
	return (int(str(first) + str(second)))

if __name__ == '__main__':
	sum = 0
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			sum += find_digits(line)
	print(sum)