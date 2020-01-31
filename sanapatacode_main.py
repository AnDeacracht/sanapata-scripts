# Generates the complete FontCreator OpenType code for the Osveraali script.

from sanapatacode_generation import *
from sanapatacode_generation_36_variants import *
from sanapatacode_generation_augmentables import *
from sanapatacode_generation_classes import *
from sanapatacode_generation_schwasubstitution import *

filename = "fullcodetest.txt"
mode = "w"

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

doubleToGeminate = "Replacement - Double Letter to Geminate"
longVowelToAugmented = "Replacement - Unaugmented to Augmented before Long Vowel"
augmentableToSchwaAugmented = "Replacement - Augmentable to Schwa-Augmented"
augmentableToSchwoAugmented = "Replacement - Augmentable to Schwo-Augmented"

### main method ###

def run():

  with open(filename, mode) as writer:
    writer.write("script latn {\n\tfeature ContextualAlternates1;\n}\n\n")

    createPositionClass(writer, "Inputs", "", True)
    createPositionClass(writer, "Isolates", "isol")
    createPositionClass(writer, "Initials", "init")
    createPositionClass(writer, "Medials", "med")
    createPositionClass(writer, "Finals", "fin")

    createAugmentables(writer)
    createSchwaAugmenteds(writer)
    createNonconnectings(writer)
    createNonaugmentables(writer)
    createLongVowels(writer)
    createShortVowels(writer)

    writer.write("feature ContextualAlternates1 calt {\n")
    
    writeSubstitutionRule(writer, inputToIsol)
    writeSubstitutionRule(writer, isolToInit)
    writeSubstitutionRule(writer, isolToFinal)
    writeSubstitutionRule(writer, finalToMedial)
    writeSubstitutionRule(writer, initToMedial)

    ### these are still a mess ###

    writer.write("\tlookup \"double letter to geminate lookup\";\n") 
    writer.write("\tlookup \"Augmentable -> Schwa-augmented before Long Vowel\";\n")
    writer.write("\tlookup \"schwa diacritic lookup\";\n")
    writer.write("\tlookup \"schwo diacritic lookup\";\n")
    writer.write("\tlookup \"change after nonconnecting\";\n")
    writer.write("\tlookup \"long vowel to short vowel after schwa-augmented\";\n")
    writer.write("\tlookup \"deadkey lookup\";\n")
    writer.write("\tlookup AfterTaConnector;\n")
    writer.write("}\n\n")

    ### positional sub rules - cleaned up, looking good ###

    writePositionalSubstitutions(writer)
    
    ### mess starts here again ###

    writer.write("lookup \"change after nonconnecting\" {\n")
    writer.write("\tcontext (@Nonconnecting) @Medials;\n")
    writer.write("\tsub 0 \"sub after nonconnecting\";\n")
    writer.write("\t context (@Nonconnecting) @Finals;\n")
    writer.write("\tsub 0 \"sub after nonconnecting\";\n")
    writer.write("}\n\n")

    writer.write("lookup \"sub after nonconnecting\" {\n")
    writer.write("\tsub @Medials -> @Initials;\n")
    writer.write("\tsub @Finals -> @IsolatedFinals;\n")
    writer.write("}\n\n")

    writer.write("lookup \"double letter to geminate lookup\" {\n")
    writer.write("\tcontext @Initials @Isolates;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Initials @Initials;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Medials @Isolates;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Medials @Initials;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Initials @Medials;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Medials @Medials;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Medials @Finals;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("\tcontext @Initials @Finals;\n")
    writer.write("\tsub 0 \"double letter to geminate letter\";\n")
    writer.write("}\n\n")

    writer.write("lookup \"Augmentable -> Schwa-augmented before Long Vowel\" {\n")
    writer.write("\tcontext (@Augmentable) @LongVowels;\n")
    writer.write("\tsub 0 \"Long Vowel -> Schwa + Short Vowel\";\n")
    writer.write("}\n\n")

    writer.write("lookup \"schwa diacritic lookup\" {\n")
    writer.write("\tcontext @Augmentable @Schwa;\n")
    writer.write("\tsub 0 \"Augmentable to Schwa-Augmented\";\n")
    writer.write("}\n\n")

    writer.write("lookup \"schwo diacritic lookup\" {\n")
    writer.write("\tcontext @Augmentable @Schwo;\n")
    writer.write("\tsub 0 \"Augmentable to Schwo-Augmented\";\n")
    writer.write("}\n\n")

    writer.write("lookup \"long vowel to short vowel after schwa-augmented\" {\n")
    writer.write("\tcontext (@SchwaAugmented) @LongVowels;\n")
    writer.write("\tsub 0 \"Long Vowel to Short Vowel\";\n")
    writer.write("}\n\n")

    writer.write("lookup \"Long Vowel to Short Vowel\" {\n")
    writer.write("\tsub @LongVowels -> @ShortVowels;\n")
    writer.write("}\n\n")

    writer.write("lookup \"deadkey lookup\" {\n")
    writer.write("\tcontext (numbersign) @Isolates (numbersign);\n")
    writer.write("\tsub 0 \"Isolated to Medial\";\n")
    writer.write("\tcontext (numbersign) @Isolates;\n")
    writer.write("\tsub 0 \"Isolated to Final\";\n")
    writer.write("\tcontext @Isolates (numbersign);\n")
    writer.write("\tsub 0 \"Isolated to Initial\";\n")
    writer.write("}\n\n")

    createGeminationSubstitutions(writer)
    writer.write("\n")

    createSchwaOrSchwoSubstitutions(writer)
    writer.write("\n")

    createSchwaOrSchwoSubstitutions(writer, False)
    writer.write("\n")

def writeSubstitutionRule(writer, name):
  writer.write("\tlookup \"" + name + "\";\n")

def writeLookupTableName(writer, name):
  writer.write("lookup \"" + name + "\" {\n")

def writeActualSubstitution(writer, name):
  writer.write("\tsub 0 \"" + name + "\";\n")

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
  writer.write("\tcontext @Initials (@Isolates);\n")
  writeActualSubstitution(writer, tableIsolToFinal)
  writer.write("}\n\n")

  createIsolToFinalSubs(writer, tableIsolToFinal)

  writeLookupTableName(writer, finalToMedial)
  writer.write("\tcontext @Medials (@Finals);\n")
  writeActualSubstitution(writer, tableFinalToMedial)
  writer.write("}\n\n")

  createFinalToMedialSubs(writer, tableFinalToMedial)

  writeLookupTableName(writer, initToMedial)
  writer.write("\tcontext @Initials (@Initials);\n")
  writeActualSubstitution(writer, tableInitToMedial)
  writer.write("\tcontext @Medials (@Initials);\n")
  writeActualSubstitution(writer, tableInitToMedial)
  writer.write("}\n\n")

  createInitToMedialSubs(writer, tableInitToMedial)


run()