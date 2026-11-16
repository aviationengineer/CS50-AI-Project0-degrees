"""Parse English sentences and print their noun phrase chunks.

The terminal vocabulary is provided by the assignment; the grammar and
helper functions below describe how those words combine into sentences.
"""

import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
# S is the start symbol. A full clause has a subject NP and a predicate VP.
S -> NP VP
# Coordinated clauses allow examples such as "Holmes sat and he chuckled."
S -> S Conj S
# A noun phrase can be a bare noun, or a determiner plus a complete nominal.
NP -> N
NP -> Det Nominal
# Allow post-noun prepositional modifiers and coordinated noun phrases.
NP -> NP PP
NP -> NP Conj NP
# Every nominal has a noun at its center; adjectives can precede that noun.
Nominal -> N
Nominal -> Adj Nominal
# A prepositional phrase can also modify the noun: "the day before Thursday".
Nominal -> Nominal PP
# A verb alone handles intransitive predicates such as "Holmes sat".
VP -> V
# A verb may take a direct object, a prepositional phrase, or an adverb.
VP -> V NP
VP -> V PP
VP -> V Adv
# Objects may also be followed by a prepositional phrase.
VP -> V NP PP
# Adverbs and prepositional phrases can modify a larger verb phrase.
VP -> Adv VP
VP -> VP PP
VP -> VP Adv
# Coordinate predicates and complement clauses are allowed.
VP -> VP Conj VP
VP -> V S
# Prepositions take a noun phrase or, in this vocabulary, an adverb as object.
PP -> P NP
PP -> P Adv
"""

# Build the chart parser once from the grammar rules above.
grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    """Read a sentence, parse it, and display its parse and NP chunks."""

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Normalize and tokenize input before passing it to the grammar parser.
    s = preprocess(s)

    # The chart parser may raise ValueError for token sequences it cannot use.
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print every valid parse because a sentence can have multiple analyses.
    for tree in trees:
        tree.pretty_print()

        # Flatten each NP chunk to show its words in sentence order.
        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Tokenize first, then keep only tokens containing at least one letter.
    # Lowercasing makes the tokens match the lowercase terminal vocabulary.
    return [word.lower() for word in nltk.word_tokenize(sentence)
            if any(character.isalpha() for character in word)]


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Visit each NP in the tree and exclude any NP containing a smaller NP.
    # This leaves the smallest complete noun phrases as the requested chunks.
    chunks = []
    for subtree in tree.subtrees(lambda node: node.label() == "NP"):
        if not any(child.label() == "NP" for child in subtree.subtrees()
                   if child is not subtree):
            chunks.append(subtree)
    return chunks


if __name__ == "__main__":
    main()
