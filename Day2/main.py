def parse_set(set: str):
	parsed_set = {
		"red": 0,
		"green": 0,
		"blue": 0
	}
	for cubes in set.split(','):	# ["count", "color"]
		parsed_set[cubes[1:].split(" ")[1]] += int(cubes[1:].split(" ")[0])
	return parsed_set

def parse_file(file: str):
	game = []
	for line in file.split('\n'):	# Each game
		game_set = {
			"red": 0,
			"green": 0,
			"blue": 0
		}
		for set in line.split(":")[1].split(";"):	# Each set
			parsed_set = parse_set(set)
			for key in game_set.keys():
				if (parsed_set[key] > game_set[key]):
					game_set[key] = parsed_set[key]
		game.append(game_set)
	return game

def is_game_possible(game_set: dict, max_set: dict) -> bool:
	for key in game_set.keys():
		if (game_set[key] > max_set[key]):
			return False
	return True

def get_set_power(set: dict) -> int:
	power = 1
	for key in set.keys():
		power *= set[key]
	return power



if __name__ == '__main__':
	with open('input.txt', 'r') as file:
		games = parse_file(file.read())
		total = 0

		# Part 1:
		# max_set = {
		# 	"red": 12,
		# 	"green": 13,
		# 	"blue": 14
		# }
		# for i in range(len(games)):
		# 	if (is_game_possible(games[i], max_set)):
		# 		total += i + 1

		# Part 2:
		for game in games:
			total += get_set_power(game)

		print(total)
