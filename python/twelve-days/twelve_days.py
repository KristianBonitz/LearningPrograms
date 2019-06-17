END_VERSES = ["twelve Drummers Drumming, ",
                    "eleven Pipers Piping, ",
                    "ten Lords-a-Leaping, ",
                    "nine Ladies Dancing, ",
                    "eight Maids-a-Milking, ",
                    "seven Swans-a-Swimming, ",
                    "six Geese-a-Laying, ",
                    "five Gold Rings, ",
                    "four Calling Birds, ",
                    "three French Hens, ",
                    "two Turtle Doves, ",
                    "and a Partridge in a Pear Tree."]

ORD_NUMBER = ["first",
				"second",
				"third",
				"fourth",
				"fifth",
				"sixth",
				"seventh",
				"eighth",
				"ninth",
				"tenth",
				"eleventh",
				"twelfth"]

def recite(start_verse, end_verse):
	verse = ""
	for line in range(start_verse, end_verse+1):
		verse = f"On the {ORD_NUMBER[line-1]} day of Christmas my true love gave to me: "
		if line == 1:
			verse += "a Partridge in a Pear Tree."
		else:
			verse += "".join(END_VERSES[12-line:12])

	return [verse]