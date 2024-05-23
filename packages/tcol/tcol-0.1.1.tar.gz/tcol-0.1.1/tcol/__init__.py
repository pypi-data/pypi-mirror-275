ITALICS = 3
UNDERLINE = 4
FLASH = 5
INVERT = 7
STRIKETHROUGH = 9
DOUBLEUNDERLINE = 21

BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
PINK = 35
CYAN = 36
WHITE = 37

BBLACK = 40
BRED = 41
BGREEN = 42
BYELLOW = 43
BBLUE = 44
BPINK = 45
BCYAN = 46
BWHITE = 47

LBLACK = 90
LRED = 91
LGREEN = 92
LYELLOW = 93
LBLUE = 94
LPINK = 95
LCYAN = 96
LWHITE = 97

BLBLACK = 100
BLRED = 101
BLGREEN = 102
BLYELLOW = 103
BLBLUE = 104
BLPINK = 105
BLCYAN = 106
BLWHITE = 107

def tc(ansi_colour: int):
	print(f"\u001b[{ansi_colour}m", end="")

def tcd():
	print("\u001b[0m", end="")

def pc(ansi_colour: int, *text, sep=" ", end="\n"):
	tc(ansi_colour)
	print(*text, sep=sep, end="")
	tcd()
	print(end=end)
