consonants = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r".split(" ")
vowels = "a á i e o u schwa schwo A I E U O".split(" ")
diacritics = "schwa schwo gem gem.schwa gem.schwo".split(" ")
positions = "isol init med fin".split(" ")

def createConsonantVariants():
	with open("variants.txt", "a") as writer:
		for glyph in consonants:
			positionedGlyphs = map(lambda position: glyph + "." + position, positions)
			for posglyph in positionedGlyphs:
				writer.write(posglyph + "\n")
				qualifiedGlyphs = map(lambda diacritic: posglyph + "." + diacritic, diacritics)
				for finalGlyph in qualifiedGlyphs:
					writer.write(finalGlyph + "\n")

def createVowelVariants():
	with open("variants.txt", "a") as writer:
		for glyph in vowels:
			positionedGlyphs = map(lambda position: glyph + "." + position, positions)
			for posglyph in positionedGlyphs:
				writer.write(posglyph + "\n")

createConsonantVariants()
createVowelVariants()