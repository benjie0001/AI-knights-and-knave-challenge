from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    #from structure of the problem
    Or(AKnight, AKnave),
    Not(And(AKnight,AKnave)),
    # from A's statement
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave,Not(And(AKnight,AKnave)))
     )
    

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    #info from structure of the problem
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),
    
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # 
    #info from structure of the problem
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),

    #A "we are the same kind"
    Implication(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),
    Implication(AKnave,Not(Or(And(AKnight,BKnight), And(AKnave,BKnave)))),
    
    #B statement on they are of different kinds
    Implication(BKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),
    Implication(BKnave,Not(Or(And(AKnight,BKnave),And(AKnave,BKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #Info from Structure of the problem
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),
    Or(CKnight,CKnave),
    Not(And(CKnight,CKnave)),

    #A says either I am a knight or I am a knave but you dont know which
    Or(And(Implication(AKnight,AKnight),Implication(AKnave,Not(AKnight)))),
    And(Implication(AKnight,AKnave),Implication(AKnave,Not(AKnave))),
    
    #Bsays "A said 'I am a knave"
    Implication(BKnight,And(Implication(AKnight,AKnave),Implication(AKnave,Not(AKnave)))),
    Implication(BKnave,Not(And(Implication(AKnight,AKnave),Implication(AKnave,Not(AKnave))))),

    #Bsays "C is a knave"
    Implication(BKnight,CKnave),
    Implication(BKnave,Not(CKnave)),

    # C says "A is a knight"
    Implication(CKnight,AKnight),
    Implication(CKnave,Not(AKnight))
)

# Puzzle 4
# A says "B never lies."
# C says “A is a knave and I am a knave.”
# B says “Carol is a knave.”
knowledge4 = And(
    # TODO
)

# Puzzle 5
# B says “A is like me”
# A says “C always tells the truth.”
# C says “B lies.”
# B says “A is lying.”
knowledge5 = And(
    # TODO
)