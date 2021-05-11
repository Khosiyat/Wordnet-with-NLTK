                                                                    #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
#Wordnet with NLTK

#nltk packages are imported
from nltk.corpus import wordnet

#GET FINFORMATION ABOUT WORDS
example_word="dance"
def fullInfo_word(lexUnit_input):
    lexSet = wordnet.synsets(lexUnit_input)
    name=lexSet[0].name()
    lemmatized=lexSet[0].lemmas()[0].name()
    defination=lexSet[0].definition()
    example=lexSet[0].examples()
#print the result
fullInfo_word(example_word)


#PARSE ANTONYMUS AND SYNONYMUS OF THE WORDS
example_word2="honest"
def sort_AntonymsSynonyms(lexUnit_input):
    synonymUnits = []
    antonymUnits = []
    for lexSet in wordnet.synsets(lexUnit_input):
        for lematizedUnit in lexSet.lemmas():
            synonyms.append(lematizedUnit.name())
            if lematizedUnit.antonyms():
                antonyms.append(lematizedUnit.antonyms()[0].name())
    print(set(synonymUnits))
    print(set(antonymUnits))
    
#print the result
sort_AntonymsSynonyms(example_word2)


#CHECK OUT WORDS WETHER THEIR MEANING CLOSE TO EACH OTHER 
#Similar Meaning
exampleSimilar1A='book.n.01'
exampleSimilar1B='pen.n.01'
exampleSimilar2A='book.n.01'
exampleSimilar2B='journal.n.01'
exampleSimilar3A='book.n.01'
exampleSimilar3B='apple.n.01'

def wordSimilarity(lexUnit_input1, lexUnit_input2):
    lexUnit1 = wordnet.synset(lexUnit_input1)
    lexUnit2 = wordnet.synset(lexUnit_input2)
    print(lexUnit1.wup_similarity(lexUnit2))
    
#print the result
wordSimilarity(exampleSimilar1A,exampleSimilar1B)
wordSimilarity(exampleSimilar2A,exampleSimilar2B)
wordSimilarity(exampleSimilar3A,exampleSimilar3B)
