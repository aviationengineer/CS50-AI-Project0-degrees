# Analysis

The notes below describe possible patterns to look for in the generated attention maps. In each diagram, rows are the tokens doing the attending, columns are the tokens receiving attention, and lighter cells indicate higher attention. Check that the pattern is visible in your run before submitting these interpretations.

## Layer 1, Head 1

This head appears to connect determiners such as “the” and “a” to the noun that follows them. The pattern is clearest when the determiner and noun are separated by punctuation or other tokens: attention from the determiner still points toward the noun, rather than simply to the next token.

Remark: These examples vary the determiner and put extra words between it and the masked noun, making it easier to distinguish a determiner-to-noun link from attention to only the immediately following token.

Example Sentences:
- The old red [MASK] stood beside the gate.
- She placed a small, polished [MASK] on the desk.

## Layer 5, Head 8

This head appears to connect a pronoun to the earlier noun phrase that it refers to. In both examples, attention from the pronoun points back toward the person or animal introduced earlier in the sentence. The pattern is a useful clue about reference, though one head alone does not establish that this is its only role.

Remark: The examples use different antecedent types (a person and an animal) and place the pronoun later in the sentence, so the proposed pattern can be compared across contexts.

Example Sentences:
- Maria dropped her keys after [MASK] left the office.
- The dog chased the ball until [MASK] disappeared behind the fence.
