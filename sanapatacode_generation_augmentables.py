def createAugmentables(writer, augmentables, positions):
		writer.write("class @Augmentable [")
		for glyph in augmentables:
			positionallyQualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in positionallyQualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")


def createSchwaAugmenteds(writer, augmentables, positions):
		writer.write("class @SchwaAugmented [")
		for glyph in augmentables:
			positionallyQualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in positionallyQualifiedGlyphs:
				schwadGlyphs = map(lambda schwa: qualifiedGlyph + "." + schwa, ["schwa"])
				for schwadGlyph in schwadGlyphs:
					writer.write(schwadGlyph + " ")
		writer.write("];\n\n")

def createNonconnectings(writer, augmentables, nonconnectings, positions):
		writer.write("class @Nonconnecting [")
		for glyph in nonconnectings:
			positionallyQualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in positionallyQualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
				if glyph in augmentables:
					schwxs = "schwa schwo".split(" ")
					schwxdGlyphs = map(lambda schwx: qualifiedGlyph + "." + schwx, schwxs)
					for schwxdGlyph in schwxdGlyphs:
						writer.write(schwxdGlyph + " ")
		writer.write("];\n\n")

def createNonaugmentables(writer, nonaugmentables, positions):
		writer.write("class @Nonaugmentable [")
		for glyph in nonaugmentables:
			positionallyQualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in positionallyQualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")

def createLongVowels(writer, longVowels, positions):
		writer.write("class @LongVowels [")
		for glyph in longVowels:
			positionallyQualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in positionallyQualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")

def createShortVowels(writer, shortVowels, positions):
		writer.write("class @ShortVowels [")
		for glyph in shortVowels:
			positionallyQualifiedGlyphs = map(lambda pos: glyph + "." + pos, positions)
			for qualifiedGlyph in positionallyQualifiedGlyphs:
				writer.write(qualifiedGlyph + " ")
		writer.write("];\n\n")
