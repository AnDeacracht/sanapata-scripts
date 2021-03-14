# Generates the complete FontCreator OpenType code for the Osveraali script.

# TODOS:

# - substitute schwa-augmented letter if long vowel follows augmentable

# - substitute isolated letter for medial if ō is initial
# - substitute isolated letter for medial if ū is initial

from sanapatacode_generation_positionalsubs import *
from sanapatacode_generation_36_variants import *
from sanapatacode_generation_augmentables import *
from sanapatacode_generation_schwasubstitution import *

filename = "fullcodetest.txt"
mode = "w"

# properties of the writing system

letternames = "s rh th ts n sh tsh p zh dzh t j m f dh d gh b w g ng ch v z dz c q l lj r h a á i e o u schwa schwo A I E U O"
inputkeys = "s R T c n S C p J G t j m f D d H b w g N x v z Z k q l L r h a adieresis i e u o udieresis odieresis A I E U O"
consonants = "s rh th ts n sh tsh p zh dzh t j m f dh gh d b w g ng ch v z dz c q l lj h r"
vowels = "a á i e o u schwa schwo A I E U O"

inputkeyToLetternameMap = {
  "s" : "s",
  "R" : "rh",
  "T" : "th",
  "c" : "ts",
  "n" : "n",
  "S" : "sh",
  "C" : "tsh",
  "p" : "p",
  "J" : "zh",
  "G" : "dzh",
  "t" : "t",
  "j" : "j",
  "m" : "m",
  "f" : "f",
  "D" : "dh",
  "d" : "d",
  "H" : "gh",
  "b" : "b",
  "w" : "w",
  "g" : "g",
  "N" : "ng",
  "x" : "ch",
  "v" : "v",
  "z" : "z",
  "Z" : "dz",
  "k" : "c",
  "q" : "q",
  "l" : "l",
  "L" : "lj",
  "r" : "r",
  "h" : "h",
  "a" : "a",
  "adieresis": "á",
  "i" : "i",
  "e" : "e",
  "u" : "u",
  "o" : "o",
  "udieresis": "schwa",
  "odieresis": "schwo",
  "A" : "A",
  "I" : "I",
  "E" : "E",
  "U" : "U",
  "O" : "O"
}

augmentables = [
  "n", "sh", "tsh",
  "t", "j",
  "m", "f", "dh",
  "b", "w",
  "v", "z", "dz",
  "l", "lj"
]

nonaugmentables = [
  "s", "rh", "th", "ts",
  "p", "zh", "dzh",
  "d", "gh",
  "g", "ng", "ch",
  "c", "q",
  "r", "h"
]

nonconnectings = [
  "s", "rh", "th", "ts",
  "p", "zh", "dzh",
  "d", "gh",
  "g", "ng", "ch",
  "r", "h"
]

longVowels = [
  "A", "I", "U", "E", "O"
]

shortVowels = [
  "a", "i", "u", "e", "o"
]

positions = [
  "isol", "init", "med", "fin",
  "isol.gem", "init.gem", "med.gem", "fin.gem"
]

vowelPositions = [
  "isol", "init", "med", "fin"
]

taConnectives = "t j b w m f dh".split(" ")
afterTaSubs = "u o schwa schwo".split(" ")
variants = ".schwa .schwo .gem .gem.schwa .gem.schwo"

# lookup names

inputToIsol = "Positional Substitution - Input to Isolated"
isolToInit = "Positional Substitution - Isolated to Initial"
isolToFinal = "Positional Substitution - Isolated to Final"
finalToMedial = "Positional Substitution - Final to Medial"
initToMedial = "Positional Substitution - Initial to Medial"

tableInputToIsol = "Lookup Table - Input to Isolated"
tableIsolToInit = "Lookup Table - Isolated to Initial"
tableIsolToFinal = "Lookup Table - Isolated to Final"
tableFinalToMedial = "Lookup Table - Final to Medial"
tableInitToMedial = "Lookup Table - Initial to Medial"
tableConnToNonconn = "Lookup Table - Connecting to Nonconnecting"

doubleToGeminate = "Replacement - Double Letter to Geminate"
tableDoubleToGeminate = "Lookup Table - Double Letter to Geminate"

connectingToNonconnecting = "Replacement - Connecting to Nonconnecting"

longVowelToAugmented = "Replacement - Unaugmented to Augmented before Long Vowel"
tableLongVowelToAugmented = "Lookup Table - Unaugmented to Augmented before Long Vowel"

augmentableToSchwaAugmented = "Replacement - Augmentable to Schwa-Augmented"
tableAugmentableToSchwaAugmented = "Lookup Table - Augmentable to Schwa-Augmented"

augmentableToSchwoAugmented = "Replacement - Augmentable to Schwo-Augmented"
tableAugmentableToSchwoAugmented = "Lookup Table - Augmentable to Schwo-Augmented"

# These are the contexts where two glyphs may be substituted for a single one.
# This either means gemination or diacritic (schwa/schwo) substitution.
# For instance, medial T and medial T get substituted by geminate T,
# or initial T and final Schwa get substituted by isolated T.schwa.
# The exact substitution is listed sanapatacode_generation_schwasubstitution.substitutions.

substitutionContexts = [
  "@Initials @Isolates",
  "@Initials @Initials",
  "@Medials @Isolates",
  "@Medials @Initials",
  "@Initials @Medials",
  "@Medials @Medials",
  "@Medials @Finals",
  "@Initials @Finals"
]

### main method ###

def run():

  print("Generating Sanapata Font Creator code to " + filename + ".")

  with open(filename, mode) as writer:
    writer.write("script latn {\n\tfeature ContextualAlternates1;\n}\n\n")

    createPositionClass(writer, "Inputs", "", True)
    createPositionClass(writer, "Isolates", "isol")
    createPositionClass(writer, "Initials", "init")
    createPositionClass(writer, "Medials", "med")
    createPositionClass(writer, "Finals", "fin")

    createAugmentables(writer, augmentables, positions)
    createSchwaAugmenteds(writer, augmentables, positions)
    createNonconnectings(writer, augmentables, nonconnectings, positions)
    createNonaugmentables(writer, nonaugmentables, positions)
    createLongVowels(writer, longVowels, vowelPositions)
    createShortVowels(writer, shortVowels, vowelPositions)

    writer.write("feature ContextualAlternates1 calt {\n")
    
    writeSubstitutionRule(writer, inputToIsol)
    writeSubstitutionRule(writer, isolToInit)
    writeSubstitutionRule(writer, isolToFinal)
    writeSubstitutionRule(writer, finalToMedial)
    writeSubstitutionRule(writer, initToMedial)
    writeSubstitutionRule(writer, doubleToGeminate)
    writeSubstitutionRule(writer, augmentableToSchwaAugmented)
    writeSubstitutionRule(writer, augmentableToSchwoAugmented)
    writeSubstitutionRule(writer, connectingToNonconnecting)

   ### these are still a mess ###

    # writer.write("\tlookup \"Augmentable -> Schwa-augmented before Long Vowel\";\n")
    # writer.write("\tlookup \"schwa diacritic lookup\";\n")
    # writer.write("\tlookup \"schwo diacritic lookup\";\n")
    # writer.write("\tlookup \"change after nonconnecting\";\n")
    # writer.write("\tlookup \"long vowel to short vowel after schwa-augmented\";\n")
    # writer.write("\tlookup \"deadkey lookup\";\n")
    # writer.write("\tlookup AfterTaConnector;\n")
    writer.write("}\n\n")

    ### sub rules - cleaned up, looking good ###

    writePositionalSubstitutions(writer)
    writeGeminationSubstitutions(writer)
    writeSchwaSubstitutions(writer)
    writeSchwoSubstitutions(writer)
    
    # break out into method

    writer.write("lookup \"" + connectingToNonconnecting + "\" {\n")
    writer.write("\tcontext (@Nonconnecting) @Medials;\n")
    writer.write("\tsub 0 \"" + tableConnToNonconn + "\";\n")
    writer.write("\t context (@Nonconnecting) @Finals;\n")
    writer.write("\tsub 0 \"" + tableConnToNonconn + "\";\n")
    writer.write("}\n\n")

    # make this table explicit

    writer.write("lookup \"" + tableConnToNonconn + "\" {\n")
    writer.write("\tsub @Medials -> @Initials;\n")
    writer.write("\tsub @Finals -> @Isolates;\n")
    writer.write("}\n\n")

    ### mess starts here again ###

    # writer.write("lookup \"Augmentable -> Schwa-augmented before Long Vowel\" {\n")
    # writer.write("\tcontext (@Augmentable) @LongVowels;\n")
    # writer.write("\tsub 0 \"Long Vowel -> Schwa + Short Vowel\";\n")
    # writer.write("}\n\n")

    # writer.write("lookup \"schwa diacritic lookup\" {\n")
    # writer.write("\tcontext @Augmentable @Schwa;\n")
    # writer.write("\tsub 0 \"Augmentable to Schwa-Augmented\";\n")
    # writer.write("}\n\n")

    # writer.write("lookup \"schwo diacritic lookup\" {\n")
    # writer.write("\tcontext @Augmentable @Schwo;\n")
    # writer.write("\tsub 0 \"Augmentable to Schwo-Augmented\";\n")
    # writer.write("}\n\n")

    # writer.write("lookup \"long vowel to short vowel after schwa-augmented\" {\n")
    # writer.write("\tcontext (@SchwaAugmented) @LongVowels;\n")
    # writer.write("\tsub 0 \"Long Vowel to Short Vowel\";\n")
    # writer.write("}\n\n")

    # writer.write("lookup \"Long Vowel to Short Vowel\" {\n")
    # writer.write("\tsub @LongVowels -> @ShortVowels;\n")
    # writer.write("}\n\n")

    # writer.write("lookup \"deadkey lookup\" {\n")
    # writer.write("\tcontext (numbersign) @Isolates (numbersign);\n")
    # writer.write("\tsub 0 \"Isolated to Medial\";\n")
    # writer.write("\tcontext (numbersign) @Isolates;\n")
    # writer.write("\tsub 0 \"Isolated to Final\";\n")
    # writer.write("\tcontext @Isolates (numbersign);\n")
    # writer.write("\tsub 0 \"Isolated to Initial\";\n")
    # writer.write("}\n\n")

    # createSchwaOrSchwoSubstitutions(writer)
    # writer.write("\n")

    # createSchwaOrSchwoSubstitutions(writer, False)
    # writer.write("\n")

def writeSubstitutionRule(writer, name):
  writer.write("\tlookup \"" + name + "\";\n")

def writeLookupTableName(writer, name):
  writer.write("lookup \"" + name + "\" {\n")

def writeActualSubstitution(writer, name):
  writer.write("\tsub 0 \"" + name + "\";\n")

def writeDiacriticSubstitutions(writer, subName, subTableName, contexts):
  writeLookupTableName(writer, subName)
  for context in contexts:
    writer.write("\tcontext " + context + ";\n")
    writeActualSubstitution(writer, subTableName)
  writer.write("}\n\n")

def writeGeminationSubstitutions(writer):
  writeDiacriticSubstitutions(writer, doubleToGeminate, tableDoubleToGeminate, substitutionContexts)
  createGeminationSubstitutions(writer, tableDoubleToGeminate, consonants.split())

def writeSchwaSubstitutions(writer):
	writeDiacriticSubstitutions(writer, augmentableToSchwaAugmented, tableAugmentableToSchwaAugmented, substitutionContexts)
	createSchwaOrSchwoSubstitutions(writer, tableAugmentableToSchwaAugmented, augmentables, useSchwa = True)

def writeSchwoSubstitutions(writer):
	writeDiacriticSubstitutions(writer, augmentableToSchwoAugmented, tableAugmentableToSchwoAugmented, substitutionContexts)
	createSchwaOrSchwoSubstitutions(writer, tableAugmentableToSchwoAugmented, augmentables, useSchwa = False)

def writePositionalSubstitutions(writer):
  writeLookupTableName(writer, inputToIsol)
  writer.write("\tcontext @Inputs;\n")
  writeActualSubstitution(writer, tableInputToIsol)
  writer.write("}\n\n")

  createInputToIsolSubs(writer, tableInputToIsol)

  writeLookupTableName(writer, isolToInit)
  writer.write("\tcontext @Isolates (@Isolates);\n")
  writeActualSubstitution(writer, tableIsolToInit)
  writer.write("}\n\n")

  createIsolToInitSubs(writer, tableIsolToInit)

  writeLookupTableName(writer, isolToFinal)
  writer.write("\tcontext (@Initials) @Isolates;\n")
  writeActualSubstitution(writer, tableIsolToFinal)
  writer.write("}\n\n")

  createIsolToFinalSubs(writer, tableIsolToFinal)

  writeLookupTableName(writer, finalToMedial)
  writer.write("\tcontext (@Medials) @Finals;\n")
  writeActualSubstitution(writer, tableFinalToMedial)
  writer.write("}\n\n")

  createFinalToMedialSubs(writer, tableFinalToMedial)

  writeLookupTableName(writer, initToMedial)
  writer.write("\tcontext (@Initials) @Initials;\n")
  writeActualSubstitution(writer, tableInitToMedial)
  writer.write("\tcontext (@Medials) @Initials;\n")
  writeActualSubstitution(writer, tableInitToMedial)
  writer.write("}\n\n")

  createInitToMedialSubs(writer, tableInitToMedial)

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

run()