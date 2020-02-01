inputkeys = "s R T c n S C p J G t j m f D H d b w g N x v z Z k q l L h r a adieresis i e o u udieresis odieresis A I E U O".split(" ")
letternames = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r a á i e o u schwa schwo A I E U O".split(" ")
consonants = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r".split(" ")

def createSubs(writer, fromGlyph, toGlyph, lookupName, mapInputKeys = False):
		writer.write("lookup \"" + lookupName + "\" {\n\n")
		if mapInputKeys:
			mappings = zip(inputkeys, letternames)
			for (inputkey, lettername) in mappings:
				sub = "\tsub " + inputkey + " -> " + lettername + ".isol;\n"
				writer.write(sub)
		else:
			for glyph in letternames:
				subBasic = "\tsub " + glyph + "." + fromGlyph + " -> " + glyph + "." + toGlyph + ";\n"
				subGem = "\tsub " + glyph + "." + fromGlyph + ".gem -> " + glyph + "." + toGlyph + ".gem;\n"
				writer.write(subBasic)
				writer.write(subGem)
				if glyph in consonants:
					subGem = "\tsub " + glyph + "." + fromGlyph + ".gem -> " + glyph + "." + toGlyph + ".gem;\n"
					subSchwa = "\tsub " + glyph + "." + fromGlyph + ".schwa -> " + glyph + "." + toGlyph + ".schwa;\n"
					subSchwo = "\tsub " + glyph + "." + fromGlyph + ".schwo -> " + glyph + "." + toGlyph + ".schwo;\n"
					subGemSchwa = "\tsub " + glyph + "." + fromGlyph + ".gem.schwa -> " + glyph + "." + toGlyph + ".gem.schwa;\n"
					subGemSchwo = "\tsub " + glyph + "." + fromGlyph + ".gem.schwo -> " + glyph + "." + toGlyph + ".gem.schwo;\n"
					writer.write(subSchwa)
					writer.write(subSchwo)
					writer.write(subGemSchwa)
					writer.write(subGemSchwo)

		writer.write("\n}\n\n")	

def createInputToIsolSubs(writer, name):
	createSubs(writer, "", "", name, useZip = True)

def createIsolToInitSubs(writer, name):
	createSubs(writer, "isol", "init", name)

def createFinalToMedialSubs(writer, name):
	createSubs(writer, "fin", "med", name)

def createIsolToFinalSubs(writer, name):
	createSubs(writer, "isol", "fin", name)

def createInitToMedialSubs(writer, name):
	createSubs(writer, "init", "med", name)

def createIsolToMedialSubs(writer, name):
	createSubs(writer, "isol", "med", name)


# inputToIsol()
# isolToInit()
# finToMed()
# isolToFin()
# initToMed()
# isolToMed()
