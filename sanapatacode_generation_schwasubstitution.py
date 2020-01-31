consonants = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r".split(" ")
augmentables = "n sh tsh t j m f dh gh d b w g ng ch v z dz l lj h r".split(" ")

taConnectives = "t j b w m f dh".split(" ")
afterTaSubs = "u o schwa schwo".split(" ")

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


#	 sub u.med -> u.med.afterta;
#  sub u.fin -> u.fin.afterta;
#  sub u.pau -> u.pau.afterta;

# lookup AfterTaConnector {
#   context (t.init) u.med;
#   sub 0 AfterTaContextualForms;
#   context (t.med) u.med;
#   sub 0 AfterTaContextualForms;
#   context (t.init) u.fin;
#   sub 0 AfterTaContextualForms;
#   context (t.med) u.fin;
#   sub 0 AfterTaContextualForms;
#   context (t.init) u.pau;
#   sub 0 AfterTaContextualForms;
#   context (t.med) u.pau;
#   sub 0 AfterTaContextualForms;
# }


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

def createAfterTaSubstitutions(writer):
	writer.write("lookup AfterTaContextualForms {\n")
	for glyph in afterTaSubs:
		writer.write("\t" + "sub " + glyph + ".med -> " + glyph + ".med.afterta;\n")
		writer.write("\t" + "sub " + glyph + ".fin -> " + glyph + ".fin.afterta;\n")
	writer.write("}\n")

def createGeminationSubstitutions(writer):
	writer.write("lookup \"Substitution - Double Letter to Geminate\" {\n")
	for glyph in consonants:
		for (firstQualifier, secondQualifier, substitutionQualifier) in substitutions:
			string = "sub " +  glyph + "." + firstQualifier + " " + glyph + "." + secondQualifier + " -> " + glyph + "." + substitutionQualifier + ".gem"
			writer.write("\t" + string + ";\n")
	writer.write("}\n")

def createSchwaOrSchwoSubstitutions(writer, useSchwa = True):
	diacritic = "schwa" if useSchwa else "schwo"
	if useSchwa:
		writer.write("lookup \"Substitution - Augmentable to Schwa-Augmented\" {\n")
	else:
		writer.write("lookup \"Substitution - Augmentable to Schwo-Augmented\" {\n")
	for glyph in augmentables:
		for (firstQualifier, schwaQualifier, substitutionQualifier) in substitutions:
			simpleString = "sub " + glyph + "." + firstQualifier + " " + diacritic + "." + schwaQualifier + " -> " + glyph + "." + substitutionQualifier + "." + diacritic 
			geminatedString = "sub " + glyph + "." + firstQualifier + ".gem " + diacritic + "." + schwaQualifier + " -> " + glyph + "." + substitutionQualifier + ".gem." +  diacritic
			writer.write("\t" + simpleString + ";\n")
			writer.write("\t" + geminatedString + ";\n")
	writer.write("}\n")

#createGeminationSubstitutions()
#createAfterTaSubstitutions()
#createAfterTaLookups()
#createSchwaSubstitutions()