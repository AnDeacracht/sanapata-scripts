inputkeys = "s R T c n S C p J G t j m f D H d b w g N x v z Z k q l L h r a adieresis i e u o udieresis odieresis A I E U O"
consonants = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r"
vowels = "a á i e o u schwa schwo A I E U O"
variants = ".schwa .schwo .gem .gem.schwa .gem.schwo"

def createPositionClass(writer, className, qualifier, isInput = False):
	lettersToProcess = ""

	if isInput:
		lettersToProcess = inputkeys.split(" ")
	else:
		lettersToProcess = consonants.split(" ")
	
	writer.write("class @" + className + " [")
	if isInput:
		for glyph in lettersToProcess:
			writer.write(glyph + " ")
	else:
		for glyph in lettersToProcess:
			qualifiedGlyph = glyph + "." + qualifier
			forms = map(lambda x : qualifiedGlyph + x, [""] + variants.split(" "))
			formsString = " ".join(forms)
			writer.write(formsString)
			writer.write(" ")
		for glyph in vowels.split(" "):
			qualifiedGlyph = glyph + "." + qualifier
			writer.write(qualifiedGlyph)
			writer.write(" ")
	writer.write("];\n\n")

#createClass("Inputs", "", True)
#createClass("Isolates", "isol")
#createClass("Initials", "init")
#createClass("Medials", "med")
#createClass("Finals", "fin")
#createClass("Pausals", "pau")
#createClass("IsolatedPausals", "ispau")
#createClass("IsolatedFinals", "isfin")