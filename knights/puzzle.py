# Version control summary:
# Added propositional knowledge bases for all four Knights and Knaves puzzles,
# including role constraints and speaker-truthfulness rules, with comments that
# explain how the puzzle statements map to the logical expressions.

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Auxiliary proposition used in Puzzle 3: whether A said "I am a knave."
ASaidKnave = Symbol("A said I am a knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# A must be exactly one type, and A's statement is true only if both role
# symbols are true. The biconditional enforces that a knight's statement is true.
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# Each character must be exactly one type. A's role is equivalent to the truth
# of the statement A makes; B has no statement that adds a further constraint.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# Each character must be exactly one type. The biconditionals tie each speaker's
# role to whether their respective statement about the two roles is true.
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, Biconditional(AKnight, BKnight)),
    Biconditional(BKnight, Not(Biconditional(AKnight, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# Each character must be exactly one type. The remaining constraints encode
# the statements and require each speaker's role to match their truth value.
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # A says one of the two possible claims. Its truth depends on which claim
    # was made; a knight speaks a true claim and a knave speaks a false one.
    Biconditional(
        AKnight,
        Or(And(ASaidKnave, AKnave), And(Not(ASaidKnave), AKnight))
    ),
    # B's two statements must each match B's role independently.
    Biconditional(BKnight, ASaidKnave),
    Biconditional(BKnight, CKnave),
    # C says "A is a knight."
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
