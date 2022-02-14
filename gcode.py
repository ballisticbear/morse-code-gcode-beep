# String to Convert
inputString = "Hello World";

inputString = inputString.upper();
mcString = "";

# Frequency for beeps
frequency = "440";

# Set times for dots, dashes, and spaces (pause)
dot = 45;
dash = dot * 3;
pause = dash

# Morse Code Dictionary
mc = { 'A':'.-', 'B':'-...',
		'C':'-.-.', 'D':'-..', 'E':'.',
		'F':'..-.', 'G':'--.', 'H':'....',
		'I':'..', 'J':'.---', 'K':'-.-',
		'L':'.-..', 'M':'--', 'N':'-.',
		'O':'---', 'P':'.--.', 'Q':'--.-',
		'R':'.-.', 'S':'...', 'T':'-',
		'U':'..-', 'V':'...-', 'W':'.--',
		'X':'-..-', 'Y':'-.--', 'Z':'--..',
		'1':'.----', '2':'..---', '3':'...--',
		'4':'....-', '5':'.....', '6':'-....',
		'7':'--...', '8':'---..', '9':'----.',
		'0':'-----', ', ':'--..--', '.':'.-.-.-',
		'?':'..--..', '/':'-..-.', '-':'-....-',
		'(':'-.--.', ')':'-.--.-', ' ': ' '}

# Convert Input to Morse Code
for str in inputString:
	mcString+=mc[str]+" ";
# print((mcString));

# Output gcode
for char in mcString:
	if char == ".":
		print("M300 S% s" % frequency + " P"+"% s" % dot);
	if char == "-":
		print("M300 S% s" % frequency + " P"+"% s" % dash);
	else:
		print("M300 S0 P"+"% s" % dash);