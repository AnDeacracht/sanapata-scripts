letternames = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r a á i e o u schwa schwo A I E U O"

nonaugmentables = "s rh th ts p zh dzh c q".split(" ")
augmentables = "n sh tsh t j m f dh gh d b w g ng ch v z dz l lj h r".split(" ")
nonconnectings = "s rh th ts p zh dzh gh d g ng ch h r".split(" ")
positions = "isol init med fin isol.gem init.gem med.gem fin.gem".split(" ")
schwxs = "schwa schwo A I E U O".split(" ")
longVowels = "A I E U O".split(" ")
shortVowels = "a i e u o".split(" ")

def createAugmentables(writer):
		writer.write("class @Augmentable [")
		for glyph in augmentables:
			qualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in qualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")


def createSchwaAugmenteds(writer):
		writer.write("class @SchwaAugmented [")
		for glyph in augmentables:
			qualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in qualifiedGlyphs:
				schwadGlyphs = map(lambda schwa: qualifiedGlyph + "." + schwa, ["schwa"])
				for schwadGlyph in schwadGlyphs:
					writer.write(schwadGlyph + " ")
		writer.write("];\n\n")

def createNonconnectings(writer):
		writer.write("class @Nonconnecting [")
		for glyph in nonconnectings:
			qualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in qualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
				schwxdGlyphs = map(lambda schwx: qualifiedGlyph + "." + schwx, schwxs)
				for schwxdGlyph in schwxdGlyphs:
					writer.write(schwxdGlyph + " ")
		writer.write("];\n\n")

def createNonaugmentables(writer):
		writer.write("class @Nonaugmentable [")
		for glyph in nonaugmentables:
			qualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in qualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")

def createLongVowels(writer):
		writer.write("class @LongVowels [")
		for glyph in longVowels:
			qualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in qualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")

def createShortVowels(writer):
		writer.write("class @ShortVowels [")
		for glyph in shortVowels:
			qualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in qualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")

#createShortVowels()
#createLongVowels()
#createNonaugmentables()
#createSchwaAugmenteds()
#createAugmentables()
#createNonconnectings()