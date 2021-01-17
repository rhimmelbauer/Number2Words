from egrep import egrep
 
Number2RegexLetter = {
    0: "(s|sh|c|ch|z)",
    1: "(t|d)",
    2: "n",
    3: "m",
    4: "r",
    5: "l",
    6: "(j|g)",
    7: "k",
    8: "(f|v)",
    9: "(b|p)"
}

def number2RegexLetters(number):
    letters = []
    for num in [ int(x) for x in str(number) ]:
        letters.append(Number2RegexLetter[num])
    return letters

def joinWildCards(letters):
    return "'[aeiouwhy]*" + "[aeiouwhy]*".join(letters) + "[aeiouwhy]*'"

def getWordsFromNumber(number):
    regexLetters = number2RegexLetters(number)
    fullRegex = joinWildCards(regexLetters)
    words = egrep("-w", fullRegex, "english_dictionary.txt")
    words.execute()
    return words.expressionFound