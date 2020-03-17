substitutions = [
	("init","fin", "isol"),
	("init", "isol", "isol"),
	("init", "med", "init"),
	("init", "init", "init"),

	("med", "med", "med"),
	("med", "fin", "fin"),
	("med", "init", "med"),
	("med", "isol", "fin")
]

geminations = [

	("init", "isol", "isol"),
	("init", "init", "init"),
	("init", "med", "init"),
	("init", "fin", "isol"),

	("med", "isol", "fin"),
	("med", "init", "med"),
	("med", "med", "med"),
	("med", "fin", "fin")

]

#deprecated, use ligatures
def createAfterTaLookups():
	with open("aftertaSubs.txt", "w") as writer:
		writer.write("lookup AfterTaConnector {\n")
		for glyph in taConnectives:
			for sub in afterTaSubs:
				forms = [ sub + ".med", sub + ".fin"]
				for form in forms:
					writer.write("\tcontext (" + glyph + ".init) " + form + ";\n")
					writer.write("\tsub 0 AfterTaContextualForms;\n")
					writer.write("\tcontext (" + glyph + ".init.schwa) " + form + ";\n")
					writer.write("\tsub 0 AfterTaContextualForms;\n")
					writer.write("\tcontext (" + glyph + ".init.schwo) " + form + ";\n")
					writer.write("\tsub 0 AfterTaContextualForms;\n")
					writer.write("\tcontext (" + glyph + ".med) " + form + ";\n")
					writer.write("\tsub 0 AfterTaContextualForms;\n") 
					writer.write("\tcontext (" + glyph + ".med.schwa) " + form + ";\n")
					writer.write("\tsub 0 AfterTaContextualForms;\n")
					writer.write("\tcontext (" + glyph + ".med.schwo) " + form + ";\n")
					writer.write("\tsub 0 AfterTaContextualForms;\n")
		writer.write("}\n")

def createAfterTaSubstitutions(writer, description):
	writer.write("lookup \"" + description + "\" {\n")
	for glyph in afterTaSubs:
		writer.write("\t" + "sub " + glyph + ".med -> " + glyph + ".med.afterta;\n")
		writer.write("\t" + "sub " + glyph + ".fin -> " + glyph + ".fin.afterta;\n")
	writer.write("}\n")

def createGeminationSubstitutions(writer, description, consonants):
	writer.write("lookup \"" + description + "\" {\n")
	for glyph in consonants:
		for (firstQualifier, secondQualifier, substitutionQualifier) in substitutions:
			string = "sub " +  glyph + "." + firstQualifier + " " + glyph + "." + secondQualifier + " -> " + glyph + "." + substitutionQualifier + ".gem"
			writer.write("\t" + string + ";\n")
	writer.write("}\n")

def createSchwaOrSchwoSubstitutions(writer, description, useSchwa = True):
	diacritic = "schwa" if useSchwa else "schwo"
	writer.write("lookup \"" + description + "\" {\n")
	for glyph in augmentables:
		for (firstQualifier, schwaQualifier, substitutionQualifier) in substitutions:
			simpleString = "sub " + glyph + "." + firstQualifier + " " + diacritic + "." + schwaQualifier + " -> " + glyph + "." + substitutionQualifier + "." + diacritic 
			geminatedString = "sub " + glyph + "." + firstQualifier + ".gem " + diacritic + "." + schwaQualifier + " -> " + glyph + "." + substitutionQualifier + ".gem." +  diacritic
			writer.write("\t" + simpleString + ";\n")
			writer.write("\t" + geminatedString + ";\n")
	writer.write("}\n")
