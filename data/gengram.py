from nltk import CFG
from nltk.parse.generate import generate, demo_grammar, _generate_all
from nltk import *
import sys
sys.setrecursionlimit(1000000)

grammar = CFG.fromstring("""
S -> NP | NP VP PUNCpoint | NPPRD | PPLOC COMMA NP VP PUNCpoint PUNCquotequote | VP | VP PUNCpoint	
PUNCpoint -> '.'	
VBG -> 'buying'	
SBAR -> RB IN S	
VBD -> 'observed' | 'saw'	
ADJP -> RB JJS | RB RB JJ	
VBN -> 'Given' | 'argued' | 'imported' | 'returned' | 'shown' | 'supported'	
VBP -> 'are' | 'lose' | 'wish'	
JJ -> 'Polish' | 'adjustable' | 'available' | 'congressional' | 'dependent' | 'happy' | 'healthcare' | 'legitimate' | 'likely' | 'magnetic' | 'serial' | 'stupid' | 'synthetic' | 'yearago'	
VBZ -> 'is' | 'manages' | 'recalls'	
DT -> 'The' | 'the'	
PP -> ADVP IN SNOM | IN | IN NP | RB IN NP | RB PP	
NN -> 'bank' | 'city' | 'comfort' | 'convention' | 'decade' | 'knowledge' | 'legislation' | 'management' | 'nomination' | 'notebook' | 'outcome' | 'platinum' | 'purchasing' | 'result' | 'scandal' | 'spite' | 'stock' | 'swing' | 'total' | 'war'	
ADVPTMP -> RBR NP	
PRN -> PUNCLRB NP PUNCRRB	
TO -> 'to'	
RB -> 'finally' | 'not' | 'very'	
NP -> DT ADJP NNS | DT NN | DT NNS | EX | NP | NP COMMA SBAR COMMA | NP NP | NP PP PRN | NP PPLOC PP PP | NPR | PRPdollar VBG NNS | QPMONEY | S	
NPPRD -> NP ADJP | NPR	
NNS -> 'assets' | 'companies' | 'instructions' | 'prisons' | 'properties' | 'relationships' | 'scenarios'	
NPLOC -> NP COMMA NP PUNCpoint	
NNP -> 'Campbell' | 'Dick' | 'French' | 'Ill' | 'Income' | 'Jefferies' | 'John' | 'McCaw' | 'Mitchell' | 'Northeast' | 'Party' | 'Robertson' | 'Superfund' | 'Sweden' | 'The'	
VB -> 'contribute' | 'go' | 'solve'	
QP -> RB RB QP	
CD -> '170' | '22' | '400' | '800'	
VP -> JJ | TO VP | VB NP PRT | VB NP VP | VB PP | VB PPLOCPRD | VBD NP NPTMP PPLOC | VBD NP PP | VBD NP PP PP COMMA SADV | VBD NP S | VBN PRT | VBP RB ADJPPRD | VBZ | VBZ ADJPPRD | VBZ ADJPPRD SBAR | VBZ PRT NP	
IN -> 'at' | 'under' | 'with'	
X -> IN	
MD -> 'Can'	
SBARADV -> X S	
NNPS -> 'Appeals' | 'Containers' | 'Dynamics'	
ADJPPRD -> JJ | JJ PPLOC | JJ S | PUNCbquotebquote JJ PUNCquotequote PP	
JJS -> 'biggest'	
SBARQ -> RB WHNP SQ PUNCpoint	
NPR -> NNP	
""")


for sentence in generate(grammar, n=1000, depth=50):
    print(' '.join(sentence))



#print(grammar.productions())



