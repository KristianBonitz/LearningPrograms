END_VERSES = ["and a Partridge in a Pear Tree.",
				"two Turtle Doves, ",
				"three French Hens, ",
				"four Calling Birds, ",
				"five Gold Rings, ",
				"six Geese-a-Laying, ",
				"seven Swans-a-Swimming, ",
				"eight Maids-a-Milking, ",
				"nine Ladies Dancing, ",
				"ten Lords-a-Leaping, ",
				"eleven Pipers Piping, ",
				"twelve Drummers Drumming, "]

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
	song = []

	for v in range(start_verse-1, end_verse):
		line = f"On the {ORD_NUMBER[v]} day of Christmas my true love gave to me: "
		if v == 0:
			line += "a Partridge in a Pear Tree."
		else:
			line += "".join(END_VERSES[v::-1])
		song.append(line)

	return song