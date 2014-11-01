def color():
	palette = {1: '04', 2: '07', 3: '08', 4: '09', 5: '11', 6: '12', 7: '06'};
	string = "And this is a very long, but not so complicated string.";
	sloop = len(string);
	stack = 0
	letters = list(string);	
	mod = "";

	for x in range(0, sloop):
		if stack == 7:
			stack = 0;
		stack += 1;
		mod += palette.get(stack) + letters[x];
	print mod;

color();
