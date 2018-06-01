from nltk import CFG, ChartParser
from random import choice
import sys
sys.setrecursionlimit(1000000)

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    production = []
    if productions:
        production = choice(productions)
        for sym in production.rhs():
            if isinstance(sym, str):
                words.append(sym)
            elif not sym:
                print(sym)
            else:
                words.extend(produce(grammar, sym))
    else:
        #words.append("")
        print(symbol);
    return words

grammar = CFG.fromstring('''
S -> ADJPPRD
S -> ADVP VP
S -> ADVPPRD
S -> ADVPTMP VP
S -> NPPRD
S -> NPTMP VP
S -> PP VP
S -> PPPRD
S -> PPTMP VP
S -> PRN VP
S -> RB VP
S -> VP
S -> VP PUNCpoint
S -> VP PUNCcolon
S -> PUNCbquotebquote NPPRD
S -> NP
S -> NP ADJPPRD
S -> NP ADVPPRD
S -> NP NPPRD
S -> NP PPLOCPRD
S -> NP PPPRD
S -> NP VP
S -> NPdollar VP
S -> SNOM VP
S -> SBARNOM VP
PDT -> 'all'
PDT -> 'half'
PDT -> 'such'
SNOM -> ADVP VP
SNOM -> ADVPTMP VP
SNOM -> RB VP
SNOM -> VP
SNOM -> NP VP
SNOM -> NPdollar VP
PUNCRRB -> 'RCB'
PUNCRRB -> 'RRB'
NAC -> NN PP
NAC -> NPR PP
ADJPPRD -> ADJP
ADJPPRD -> ADJP PP
ADJPPRD -> ADJP SBAR
ADJPPRD -> ADVP JJ
ADJPPRD -> JJ
ADJPPRD -> JJ NP
ADJPPRD -> JJ NPTMP
ADJPPRD -> JJ PP
ADJPPRD -> JJ PPLOC
ADJPPRD -> JJ S
ADJPPRD -> JJ SBAR
ADJPPRD -> JJR
ADJPPRD -> JJR PP
ADJPPRD -> NN
ADJPPRD -> NP JJ
ADJPPRD -> NP JJR
ADJPPRD -> NPADV JJR
ADJPPRD -> RB JJ
ADJPPRD -> RB JJR
ADJPPRD -> RB VBN
ADJPPRD -> RBR
ADJPPRD -> RBR JJ
ADJPPRD -> RBS JJ
ADJPPRD -> RP
ADJPPRD -> VBG
ADJPPRD -> VBN
ADJPPRD -> VBN PP
ADJPPRD -> VBN S
ADJPPRD -> VBN SBAR
RBR -> 'better'
RBR -> 'closer'
RBR -> 'earlier'
RBR -> 'faster'
RBR -> 'further'
RBR -> 'harder'
RBR -> 'higher'
RBR -> 'later'
RBR -> 'less'
RBR -> 'longer'
RBR -> 'lower'
RBR -> 'more'
RBR -> 'worse'
CD -> '1'
CD -> '1,'
CD -> '1,200'
CD -> '1,500'
CD -> '1point'
CD -> '1point1'
CD -> '1point125'
CD -> '1point15'
CD -> '1point17'
CD -> '1point18'
CD -> '1point2'
CD -> '1point20'
CD -> '1point25'
CD -> '1point26'
CD -> '1point3'
CD -> '1point375'
CD -> '1point39'
CD -> '1point4'
CD -> '1point5'
CD -> '1point50'
CD -> '1point55'
CD -> '1point6'
CD -> '1point7'
CD -> '1point71'
CD -> '1point75'
CD -> '1point8'
CD -> '1point875'
CD -> '1point9'
CD -> '10'
CD -> '10,'
CD -> '10point2'
CD -> '10point5'
CD -> '10point77'
CD -> '100'
CD -> '100,'
CD -> '101'
CD -> '102'
CD -> '103'
CD -> '104'
CD -> '105'
CD -> '106'
CD -> '107'
CD -> '109'
CD -> '11'
CD -> '11point8'
CD -> '110'
CD -> '111'
CD -> '114'
CD -> '115'
CD -> '119'
CD -> '11:slash:16'
CD -> '12'
CD -> '12point5'
CD -> '12point6'
CD -> '12point8'
CD -> '120'
CD -> '120,'
CD -> '125'
CD -> '12:slash:32'
CD -> '13'
CD -> '13point50'
CD -> '13point625'
CD -> '13point8'
CD -> '130'
CD -> '13:slash:16'
CD -> '14'
CD -> '14point5'
CD -> '140'
CD -> '145'
CD -> '149'
CD -> '15'
CD -> '15,'
CD -> '15point6'
CD -> '150'
CD -> '150,'
CD -> '155'
CD -> '16'
CD -> '16,'
CD -> '160'
CD -> '17'
CD -> '170'
CD -> '179'
CD -> '18'
CD -> '18,'
CD -> '18point65'
CD -> '180'
CD -> '185'
CD -> '19'
CD -> '19point7'
CD -> '190'
CD -> '1906'
CD -> '1929'
CD -> '1950s'
CD -> '1959'
CD -> '1960'
CD -> '1962'
CD -> '1967'
CD -> '1969'
CD -> '1970'
CD -> '1970s'
CD -> '1971'
CD -> '1972'
CD -> '1973'
CD -> '1974'
CD -> '1975'
CD -> '1976'
CD -> '1977'
CD -> '1978'
CD -> '1979'
CD -> '198'
CD -> '1980'
CD -> '1980s'
CD -> '1981'
CD -> '1982'
CD -> '1983'
CD -> '1984'
CD -> '1985'
CD -> '1986'
CD -> '1987'
CD -> '1988'
CD -> '1989'
CD -> '1990'
CD -> '1990s'
CD -> '1991'
CD -> '1992'
CD -> '1993'
CD -> '1994'
CD -> '1995'
CD -> '1996'
CD -> '1997'
CD -> '1998'
CD -> '1999'
CD -> '19:slash:32'
CD -> '1:slash:2'
CD -> '1:slash:4'
CD -> '1:slash:8'
CD -> '2'
CD -> '2,'
CD -> '2point1'
CD -> '2point2'
CD -> '2point25'
CD -> '2point3'
CD -> '2point4'
CD -> '2point5'
CD -> '2point50'
CD -> '2point58'
CD -> '2point6'
CD -> '2point625'
CD -> '2point7'
CD -> '2point75'
CD -> '2point8'
CD -> '2point9'
CD -> '20'
CD -> '20,'
CD -> '200'
CD -> '200,'
CD -> '2000'
CD -> '2001'
CD -> '2003:slash:2007'
CD -> '2004'
CD -> '2009'
CD -> '2018'
CD -> '2019'
CD -> '21'
CD -> '22'
CD -> '22point6'
CD -> '220'
CD -> '225'
CD -> '23'
CD -> '230'
CD -> '24'
CD -> '25'
CD -> '25,'
CD -> '250'
CD -> '250,'
CD -> '26'
CD -> '26point23'
CD -> '260'
CD -> '2638point73'
CD -> '2659point22'
CD -> '2662point91'
CD -> '2683point20'
CD -> '27'
CD -> '270'
CD -> '275'
CD -> '28'
CD -> '280'
CD -> '29'
CD -> '2:slash:32'
CD -> '3'
CD -> '3,'
CD -> '3point1'
CD -> '3point16'
CD -> '3point2'
CD -> '3point3'
CD -> '3point35'
CD -> '3point4'
CD -> '3point5'
CD -> '3point6'
CD -> '3point69'
CD -> '3point7'
CD -> '3point8'
CD -> '3point9'
CD -> '30'
CD -> '30,'
CD -> '300'
CD -> '300,'
CD -> '31'
CD -> '32'
CD -> '33'
CD -> '34'
CD -> '35'
CD -> '350'
CD -> '350,'
CD -> '36'
CD -> '37'
CD -> '37point5'
CD -> '38'
CD -> '380'
CD -> '39'
CD -> '39point55'
CD -> '3:slash:32'
CD -> '3:slash:4'
CD -> '3:slash:8'
CD -> '4'
CD -> '4,'
CD -> '4point1'
CD -> '4point2'
CD -> '4point25'
CD -> '4point3'
CD -> '4point4'
CD -> '4point5'
CD -> '4point6'
CD -> '4point7'
CD -> '4point75'
CD -> '4point8'
CD -> '4point875'
CD -> '4point9'
CD -> '40'
CD -> '40,'
CD -> '400'
CD -> '400,'
CD -> '41'
CD -> '42'
CD -> '43'
CD -> '44'
CD -> '45'
CD -> '450'
CD -> '46'
CD -> '47'
CD -> '48'
CD -> '486'
CD -> '49'
CD -> '5'
CD -> '5,'
CD -> '5point1'
CD -> '5point2'
CD -> '5point3'
CD -> '5point4'
CD -> '5point5'
CD -> '5point6'
CD -> '5point8'
CD -> '5point9'
CD -> '50'
CD -> '50,'
CD -> '500'
CD -> '500,'
CD -> '51'
CD -> '52'
CD -> '53'
CD -> '54'
CD -> '55'
CD -> '550'
CD -> '550,'
CD -> '56'
CD -> '57'
CD -> '58'
CD -> '59'
CD -> '5:slash:16'
CD -> '5:slash:8'
CD -> '6'
CD -> '6,'
CD -> '6point2'
CD -> '6point25'
CD -> '6point3'
CD -> '6point4'
CD -> '6point5'
CD -> '6point6'
CD -> '6point7'
CD -> '6point79'
CD -> '6point8'
CD -> '6point9'
CD -> '60'
CD -> '600'
CD -> '600,'
CD -> '61'
CD -> '62'
CD -> '62point5'
CD -> '63'
CD -> '63point52'
CD -> '64'
CD -> '65'
CD -> '650'
CD -> '66'
CD -> '66point7'
CD -> '67'
CD -> '68'
CD -> '69'
CD -> '6:slash:2'
CD -> '7'
CD -> '7point10'
CD -> '7point2'
CD -> '7point20'
CD -> '7point3'
CD -> '7point37'
CD -> '7point42'
CD -> '7point5'
CD -> '7point50'
CD -> '7point52'
CD -> '7point6'
CD -> '7point60'
CD -> '7point7'
CD -> '7point75'
CD -> '7point80'
CD -> '7point82'
CD -> '7point875'
CD -> '7point88'
CD -> '7point9'
CD -> '7point90'
CD -> '7point92'
CD -> '7point93'
CD -> '7point95'
CD -> '7point96'
CD -> '7point98'
CD -> '70'
CD -> '70,'
CD -> '700'
CD -> '700,'
CD -> '71'
CD -> '72'
CD -> '73'
CD -> '74'
CD -> '75'
CD -> '750'
CD -> '76'
CD -> '77'
CD -> '78'
CD -> '79'
CD -> '7:slash:16'
CD -> '7:slash:8'
CD -> '8'
CD -> '8,'
CD -> '8point'
CD -> '8point1'
CD -> '8point15'
CD -> '8point2'
CD -> '8point20'
CD -> '8point25'
CD -> '8point3'
CD -> '8point30'
CD -> '8point32'
CD -> '8point33'
CD -> '8point35'
CD -> '8point375'
CD -> '8point4'
CD -> '8point40'
CD -> '8point45'
CD -> '8point47'
CD -> '8point5'
CD -> '8point50'
CD -> '8point55'
CD -> '8point60'
CD -> '8point65'
CD -> '8point70'
CD -> '8point75'
CD -> '8point8'
CD -> '8point9'
CD -> '80'
CD -> '800'
CD -> '800,'
CD -> '85'
CD -> '86'
CD -> '87'
CD -> '87point5'
CD -> '88'
CD -> '89'
CD -> '9'
CD -> '9point1'
CD -> '9point2'
CD -> '9point4'
CD -> '9point5'
CD -> '9point6'
CD -> '9point7'
CD -> '9point75'
CD -> '90'
CD -> '900'
CD -> '92'
CD -> '93'
CD -> '95'
CD -> '96'
CD -> '97'
CD -> '98'
CD -> '99'
CD -> '9:slash:16'
CD -> 'One'
CD -> 'Ten'
CD -> 'Three'
CD -> 'billion'
CD -> 'eight'
CD -> 'five'
CD -> 'four'
CD -> 'hundred'
CD -> 'million'
CD -> 'nine'
CD -> 'one'
CD -> 'seven'
CD -> 'six'
CD -> 'thousand'
CD -> 'three'
CD -> 'trillion'
CD -> 'two'
RP -> 'about'
RP -> 'along'
RP -> 'around'
RP -> 'aside'
RP -> 'away'
RP -> 'back'
RP -> 'by'
RP -> 'down'
RP -> 'in'
RP -> 'off'
RP -> 'on'
RP -> 'out'
RP -> 'over'
RP -> 'through'
RP -> 'together'
RP -> 'up'
SBARTMP -> IN S
SBARTMP -> IN SNOM
SBARTMP -> RB S
SBARTMP -> WHADVP S
NPLOC -> NP PP
NPLOC -> NPR
NPLOC -> NPR PUNCpoint
NPLOC -> RB
POUND -> '#'
WHADJP -> WRB JJ
PRP -> "'s"
PRP -> 'He'
PRP -> 'It'
PRP -> 'She'
PRP -> 'They'
PRP -> 'We'
PRP -> 'You'
PRP -> 'he'
PRP -> 'her'
PRP -> 'herself'
PRP -> 'him'
PRP -> 'himself'
PRP -> 'i'
PRP -> 'it'
PRP -> 'itself'
PRP -> 'me'
PRP -> 'myself'
PRP -> 'one'
PRP -> 'she'
PRP -> 'them'
PRP -> 'themselves'
PRP -> 'they'
PRP -> 'us'
PRP -> 'we'
PRP -> 'you'
PRP -> 'yourself'
LST -> LS
LST -> LS PUNCpoint
VP -> ADVP VBN
VP -> ADVPTMP VBN
VP -> IN NP
VP -> IN S
VP -> JJ
VP -> JJ PP
VP -> JJ NP
VP -> MD
VP -> MD S
VP -> MD VP
VP -> NN
VP -> TO
VP -> TO VP
VP -> VB
VP -> VB ADVP
VP -> VB NPTMP
VP -> VB PP
VP -> VB PPLOC
VP -> VB PPTMP
VP -> VB SPRP
VP -> VB SBARTMP
VP -> VB ADJP
VP -> VB ADJPPRD
VP -> VB ADVPLOC
VP -> VB ADVPPRD
VP -> VB ADVPTMP
VP -> VB NP
VP -> VB NPPRD
VP -> VB PPLOCPRD
VP -> VB PPPRD
VP -> VB PRT
VP -> VB S
VP -> VB SPRD
VP -> VB SBAR
VP -> VB SBARADV
VP -> VB SBARNOM
VP -> VB SBARPRD
VP -> VB VP
VP -> VBD
VP -> VBD ADVPTMP
VP -> VBD NPTMP
VP -> VBD PP
VP -> VBD PPLOC
VP -> VBD PPTMP
VP -> VBD SPRP
VP -> VBD ADJP
VP -> VBD ADJPPRD
VP -> VBD ADVP
VP -> VBD ADVPLOCPRD
VP -> VBD ADVPPRD
VP -> VBD NP
VP -> VBD NPPRD
VP -> VBD PPLOCPRD
VP -> VBD PPPRD
VP -> VBD PPTMPPRD
VP -> VBD PRT
VP -> VBD S
VP -> VBD SADV
VP -> VBD SPRD
VP -> VBD SBAR
VP -> VBD SBARADV
VP -> VBD SBARNOM
VP -> VBD SBARPRD
VP -> VBD SBARTMP
VP -> VBD VP
VP -> VBG
VP -> VBG PP
VP -> VBG ADJPPRD
VP -> VBG ADVP
VP -> VBG ADVPLOC
VP -> VBG ADVPTMP
VP -> VBG NP
VP -> VBG NPPRD
VP -> VBG NPTMP
VP -> VBG PPLOC
VP -> VBG PPTMP
VP -> VBG PRT
VP -> VBG S
VP -> VBG SPRP
VP -> VBG SBAR
VP -> VBG SBARNOM
VP -> VBG SBARTMP
VP -> VBG VP
VP -> VBN
VP -> VBN ADVP
VP -> VBN ADVPLOC
VP -> VBN ADVPTMP
VP -> VBN NP
VP -> VBN NPTMP
VP -> VBN PP
VP -> VBN PPLOC
VP -> VBN PPTMP
VP -> VBN PRT
VP -> VBN S
VP -> VBN SPRP
VP -> VBN SBAR
VP -> VBN SBARADV
VP -> VBN SBARPRP
VP -> VBN SBARTMP
VP -> VBN ADJPPRD
VP -> VBN ADVPPRD
VP -> VBN NPPRD
VP -> VBN PPLOCPRD
VP -> VBN PPPRD
VP -> VBN SPRD
VP -> VBN VP
VP -> VBP
VP -> VBP PP
VP -> VBP PPLOC
VP -> VBP ADJPPRD
VP -> VBP ADVP
VP -> VBP ADVPLOC
VP -> VBP ADVPPRD
VP -> VBP NP
VP -> VBP NPPRD
VP -> VBP NPTMP
VP -> VBP PPLOCPRD
VP -> VBP PPPRD
VP -> VBP RB
VP -> VBP S
VP -> VBP SBAR
VP -> VBP SBARNOM
VP -> VBP VP
VP -> VBZ
VP -> VBZ PP
VP -> VBZ PPLOC
VP -> VBZ S
VP -> VBZ ADJP
VP -> VBZ ADJPPRD
VP -> VBZ ADVP
VP -> VBZ ADVPLOC
VP -> VBZ ADVPLOCPRD
VP -> VBZ ADVPPRD
VP -> VBZ ADVPTMP
VP -> VBZ NP
VP -> VBZ NPPRD
VP -> VBZ NPTMP
VP -> VBZ PPLOCPRD
VP -> VBZ PPPRD
VP -> VBZ PPTMP
VP -> VBZ PPTMPPRD
VP -> VBZ PRT
VP -> VBZ RB
VP -> VBZ SNOMPRD
VP -> VBZ SPRD
VP -> VBZ SBAR
VP -> VBZ SBARADV
VP -> VBZ SBARLOCPRD
VP -> VBZ SBARNOM
VP -> VBZ SBARNOMPRD
VP -> VBZ SBARPRD
VP -> VBZ SBARPRPPRD
VP -> VBZ SBARTMP
VP -> VBZ VP
ADVPPRD -> IN
ADVPPRD -> IN NP
ADVPPRD -> IN PP
ADVPPRD -> JJ
ADVPPRD -> RB
ADVPPRD -> RB NP
ADVPPRD -> RB PP
ADVPPRD -> RB RB
ADVPPRD -> RP
EX -> 'There'
EX -> 'there'
PUNCbquotebquote -> '`'
PUNCbquotebquote -> '``'
RB -> 'Even'
RB -> 'Just'
RB -> 'Maybe'
RB -> 'Never'
RB -> 'Not'
RB -> 'Now'
RB -> 'Obviously'
RB -> 'Once'
RB -> 'So'
RB -> 'Sometimes'
RB -> 'Then'
RB -> 'apointm'
RB -> 'apointmpoint'
RB -> 'about'
RB -> 'abroad'
RB -> 'abruptly'
RB -> 'absolutely'
RB -> 'actively'
RB -> 'actually'
RB -> 'adequately'
RB -> 'after'
RB -> 'afterward'
RB -> 'again'
RB -> 'aggressively'
RB -> 'ago'
RB -> 'ahead'
RB -> 'all'
RB -> 'allegedly'
RB -> 'almost'
RB -> 'alone'
RB -> 'along'
RB -> 'already'
RB -> 'also'
RB -> 'altogether'
RB -> 'always'
RB -> 'annually'
RB -> 'anymore'
RB -> 'anytime'
RB -> 'anyway'
RB -> 'anywhere'
RB -> 'apart'
RB -> 'apiece'
RB -> 'apparently'
RB -> 'approximately'
RB -> 'around'
RB -> 'as'
RB -> 'aside'
RB -> 'automatically'
RB -> 'away'
RB -> 'back'
RB -> 'badly'
RB -> 'barely'
RB -> 'basically'
RB -> 'because'
RB -> 'before'
RB -> 'behind'
RB -> 'below'
RB -> 'best'
RB -> 'better'
RB -> 'bitterly'
RB -> 'broadly'
RB -> 'carefully'
RB -> 'certainly'
RB -> 'clearly'
RB -> 'close'
RB -> 'closely'
RB -> 'commonly'
RB -> 'completely'
RB -> 'consequently'
RB -> 'considerably'
RB -> 'consistently'
RB -> 'constantly'
RB -> 'currently'
RB -> 'daily'
RB -> 'deeply'
RB -> 'definitely'
RB -> 'deliberately'
RB -> 'directly'
RB -> 'double'
RB -> 'down'
RB -> 'downward'
RB -> 'due'
RB -> 'earlier'
RB -> 'early'
RB -> 'easily'
RB -> 'easy'
RB -> 'effectively'
RB -> 'either'
RB -> 'else'
RB -> 'elsewhere'
RB -> 'enough'
RB -> 'entirely'
RB -> 'environmentally'
RB -> 'equally'
RB -> 'especially'
RB -> 'essentially'
RB -> 'even'
RB -> 'eventually'
RB -> 'ever'
RB -> 'everywhere'
RB -> 'exactly'
RB -> 'exceptionally'
RB -> 'exclusively'
RB -> 'extremely'
RB -> 'fairly'
RB -> 'far'
RB -> 'fast'
RB -> 'federally'
RB -> 'finally'
RB -> 'financially'
RB -> 'first'
RB -> 'forever'
RB -> 'formally'
RB -> 'formerly'
RB -> 'forward'
RB -> 'fractionally'
RB -> 'freely'
RB -> 'frequently'
RB -> 'fully'
RB -> 'further'
RB -> 'furthermore'
RB -> 'generally'
RB -> 'gradually'
RB -> 'greatly'
RB -> 'hard'
RB -> 'hardly'
RB -> 'heavily'
RB -> 'here'
RB -> 'high'
RB -> 'highly'
RB -> 'historically'
RB -> 'hopefully'
RB -> 'however'
RB -> 'illegally'
RB -> 'immediately'
RB -> 'in'
RB -> 'incorrectly'
RB -> 'increasingly'
RB -> 'indeed'
RB -> 'indirectly'
RB -> 'inevitably'
RB -> 'initially'
RB -> 'instead'
RB -> 'jointly'
RB -> 'just'
RB -> 'largely'
RB -> 'last'
RB -> 'late'
RB -> 'lately'
RB -> 'later'
RB -> 'likely'
RB -> 'likewise'
RB -> 'literally'
RB -> 'little'
RB -> 'long'
RB -> 'longer'
RB -> 'mainly'
RB -> 'maybe'
RB -> 'meanwhile'
RB -> 'merely'
RB -> 'moderately'
RB -> 'modestly'
RB -> 'monthly'
RB -> 'moreover'
RB -> 'mostly'
RB -> 'much'
RB -> "n't"
RB -> 'narrowly'
RB -> 'nationally'
RB -> 'naturally'
RB -> 'nearby'
RB -> 'nearly'
RB -> 'necessarily'
RB -> 'nervously'
RB -> 'never'
RB -> 'nevertheless'
RB -> 'newly'
RB -> 'next'
RB -> 'no'
RB -> 'nonetheless'
RB -> 'normally'
RB -> 'not'
RB -> 'notably'
RB -> 'now'
RB -> 'obviously'
RB -> 'occasionally'
RB -> 'off'
RB -> 'officially'
RB -> 'often'
RB -> 'on'
RB -> 'once'
RB -> 'only'
RB -> 'openly'
RB -> 'ordinarily'
RB -> 'originally'
RB -> 'otherwise'
RB -> 'out'
RB -> 'over'
RB -> 'overall'
RB -> 'overly'
RB -> 'overseas'
RB -> 'ppointm'
RB -> 'ppointmpoint'
RB -> 'partially'
RB -> 'particularly'
RB -> 'partly'
RB -> 'perfectly'
RB -> 'perhaps'
RB -> 'politically'
RB -> 'possibly'
RB -> 'potentially'
RB -> 'precisely'
RB -> 'presumably'
RB -> 'pretty'
RB -> 'previously'
RB -> 'primarily'
RB -> 'prior'
RB -> 'privately'
RB -> 'probably'
RB -> 'promptly'
RB -> 'properly'
RB -> 'publicly'
RB -> 'quickly'
RB -> 'quietly'
RB -> 'quite'
RB -> 'rapidly'
RB -> 'rarely'
RB -> 'rather'
RB -> 'real'
RB -> 'really'
RB -> 'reasonably'
RB -> 'recently'
RB -> 'regardless'
RB -> 'relatively'
RB -> 'repeatedly'
RB -> 'reportedly'
RB -> 'right'
RB -> 'roughly'
RB -> 'routinely'
RB -> 'safely'
RB -> 'seasonally'
RB -> 'separately'
RB -> 'seriously'
RB -> 'sharply'
RB -> 'short'
RB -> 'shortly'
RB -> 'significantly'
RB -> 'similarly'
RB -> 'simply'
RB -> 'slightly'
RB -> 'slowly'
RB -> 'so'
RB -> 'solely'
RB -> 'some'
RB -> 'somehow'
RB -> 'sometime'
RB -> 'sometimes'
RB -> 'somewhat'
RB -> 'somewhere'
RB -> 'soon'
RB -> 'south'
RB -> 'specifically'
RB -> 'steadily'
RB -> 'still'
RB -> 'strongly'
RB -> 'subsequently'
RB -> 'substantially'
RB -> 'successfully'
RB -> 'suddenly'
RB -> 'supposedly'
RB -> 'sure'
RB -> 'surely'
RB -> 'surprisingly'
RB -> 'temporarily'
RB -> 'tenfold'
RB -> 'tentatively'
RB -> 'that'
RB -> 'then'
RB -> 'there'
RB -> 'thereafter'
RB -> 'therefore'
RB -> 'though'
RB -> 'through'
RB -> 'thus'
RB -> 'tight'
RB -> 'together'
RB -> 'too'
RB -> 'totally'
RB -> 'traditionally'
RB -> 'twice'
RB -> 'typically'
RB -> 'ultimately'
RB -> 'unanimously'
RB -> 'unexpectedly'
RB -> 'unfairly'
RB -> 'unfortunately'
RB -> 'unsuccessfully'
RB -> 'unusually'
RB -> 'up'
RB -> 'upward'
RB -> 'usually'
RB -> 'very'
RB -> 'virtually'
RB -> 'voluntarily'
RB -> 'well'
RB -> 'widely'
RB -> 'wildly'
RB -> 'worldwide'
RB -> 'yesterday'
RB -> 'yet'
FW -> 'de'
FW -> 'glasnost'
FW -> 'naczelnik'
FW -> 'perestroika'
FW -> 'pro'
FW -> 'vspoint'
PUNCLRB -> 'LCB'
PUNCLRB -> 'LRB'
VBP -> "'m"
VBP -> "'re"
VBP -> "'ve"
VBP -> 'Are'
VBP -> 'Do'
VBP -> 'account'
VBP -> 'add'
VBP -> 'agree'
VBP -> 'ai'
VBP -> 'allow'
VBP -> 'am'
VBP -> 'appear'
VBP -> 'approve'
VBP -> 'are'
VBP -> 'argue'
VBP -> 'become'
VBP -> 'believe'
VBP -> 'build'
VBP -> 'buy'
VBP -> 'call'
VBP -> 'carry'
VBP -> 'change'
VBP -> 'charge'
VBP -> 'cite'
VBP -> 'claim'
VBP -> 'come'
VBP -> 'complain'
VBP -> 'concede'
VBP -> 'consider'
VBP -> 'contend'
VBP -> 'continue'
VBP -> 'decline'
VBP -> 'disagree'
VBP -> 'do'
VBP -> 'estimate'
VBP -> 'exist'
VBP -> 'expect'
VBP -> 'face'
VBP -> 'fall'
VBP -> 'fare'
VBP -> 'favor'
VBP -> 'fear'
VBP -> 'feel'
VBP -> 'find'
VBP -> 'get'
VBP -> 'give'
VBP -> 'go'
VBP -> 'hate'
VBP -> 'have'
VBP -> 'help'
VBP -> 'hit'
VBP -> 'hold'
VBP -> 'hope'
VBP -> 'illustrate'
VBP -> 'include'
VBP -> 'indicate'
VBP -> 'insist'
VBP -> 'intend'
VBP -> 'keep'
VBP -> 'know'
VBP -> 'lead'
VBP -> 'leave'
VBP -> 'like'
VBP -> 'live'
VBP -> 'look'
VBP -> 'lose'
VBP -> 'love'
VBP -> 'maintain'
VBP -> 'make'
VBP -> 'mean'
VBP -> 'meet'
VBP -> 'move'
VBP -> 'need'
VBP -> 'note'
VBP -> 'offer'
VBP -> 'oppose'
VBP -> 'own'
VBP -> 'pay'
VBP -> 'plan'
VBP -> 'play'
VBP -> 'point'
VBP -> 'predict'
VBP -> 'prefer'
VBP -> 'provide'
VBP -> 'put'
VBP -> 'question'
VBP -> 'raise'
VBP -> 'range'
VBP -> 'reach'
VBP -> 'read'
VBP -> 'realize'
VBP -> 'receive'
VBP -> 'reflect'
VBP -> 'remain'
VBP -> 'report'
VBP -> 'represent'
VBP -> 'require'
VBP -> 'rise'
VBP -> 'run'
VBP -> 'say'
VBP -> 'see'
VBP -> 'seek'
VBP -> 'seem'
VBP -> 'sell'
VBP -> 'show'
VBP -> 'spend'
VBP -> 'stand'
VBP -> 'start'
VBP -> 'stay'
VBP -> 'suggest'
VBP -> 'support'
VBP -> 'suspect'
VBP -> 'take'
VBP -> 'tell'
VBP -> 'tend'
VBP -> 'think'
VBP -> 'total'
VBP -> 'trade'
VBP -> 'try'
VBP -> 'understand'
VBP -> 'use'
VBP -> 'vary'
VBP -> 'view'
VBP -> 'want'
VBP -> 'wish'
VBP -> 'wonder'
VBP -> 'work'
VBP -> 'worry'
SBARNOM -> IN S
SBARNOM -> WHADVP S
SBARNOM -> WHNP S
PRPdollar -> 'My'
PRPdollar -> 'Our'
PRPdollar -> 'Their'
PRPdollar -> 'her'
PRPdollar -> 'his'
PRPdollar -> 'its'
PRPdollar -> 'my'
PRPdollar -> 'our'
PRPdollar -> 'their'
PRPdollar -> 'your'
JJR -> 'better'
JJR -> 'bigger'
JJR -> 'broader'
JJR -> 'cheaper'
JJR -> 'cleaner'
JJR -> 'closer'
JJR -> 'deeper'
JJR -> 'earlier'
JJR -> 'easier'
JJR -> 'faster'
JJR -> 'fewer'
JJR -> 'greater'
JJR -> 'harder'
JJR -> 'higher'
JJR -> 'larger'
JJR -> 'less'
JJR -> 'longer'
JJR -> 'lower'
JJR -> 'more'
JJR -> 'older'
JJR -> 'riskier'
JJR -> 'slower'
JJR -> 'smaller'
JJR -> 'softer'
JJR -> 'steeper'
JJR -> 'stronger'
JJR -> 'tighter'
JJR -> 'tougher'
JJR -> 'weaker'
JJR -> 'wider'
JJR -> 'worse'
JJR -> 'younger'
ADVP -> ADVP
ADVP -> ADVP PP
ADVP -> ADVP SBAR
ADVP -> DT
ADVP -> IN
ADVP -> IN DT
ADVP -> IN JJS
ADVP -> IN NN
ADVP -> IN NP
ADVP -> IN PP
ADVP -> IN RB
ADVP -> JJ
ADVP -> JJ PP
ADVP -> JJR
ADVP -> JJR IN
ADVP -> LS
ADVP -> NN
ADVP -> NN IN
ADVP -> NP JJR
ADVP -> NP RB
ADVP -> NP RBR
ADVP -> NPADV RBR
ADVP -> NPR
ADVP -> QP
ADVP -> RB
ADVP -> RB IN
ADVP -> RB JJ
ADVP -> RB JJR
ADVP -> RB NP
ADVP -> RB PP
ADVP -> RB RB
ADVP -> RB RBR
ADVP -> RB S
ADVP -> RBR
ADVP -> RBR IN
ADVP -> RBR PP
ADVP -> RBR RB
ADVP -> RBS
ADVP -> RBS RB
NNPS -> 'Affairs'
NNPS -> 'Airlines'
NNPS -> 'Airways'
NNPS -> 'Americans'
NNPS -> 'Appeals'
NNPS -> 'Appropriations'
NNPS -> 'Associates'
NNPS -> 'Bankers'
NNPS -> 'Beebes'
NNPS -> 'Brothers'
NNPS -> 'CDs'
NNPS -> 'Communications'
NNPS -> 'Communists'
NNPS -> 'Containers'
NNPS -> 'Contras'
NNPS -> 'Cowboys'
NNPS -> 'Crusaders'
NNPS -> 'Dealers'
NNPS -> 'Democrats'
NNPS -> 'Dynamics'
NNPS -> 'Enterprises'
NNPS -> 'Facilities'
NNPS -> 'Farmers'
NNPS -> 'Fujis'
NNPS -> 'Futures'
NNPS -> 'Gardens'
NNPS -> 'Germans'
NNPS -> 'Giants'
NNPS -> 'Harbors'
NNPS -> 'Hills'
NNPS -> 'Holdings'
NNPS -> 'Industries'
NNPS -> 'Investments'
NNPS -> 'Investors'
NNPS -> 'Issues'
NNPS -> 'Japanese'
NNPS -> 'Laboratories'
NNPS -> 'Lines'
NNPS -> 'Machines'
NNPS -> 'Manufacturers'
NNPS -> 'Markets'
NNPS -> 'Motors'
NNPS -> 'Netherlands'
NNPS -> 'Options'
NNPS -> 'Partners'
NNPS -> 'Philippines'
NNPS -> 'Pictures'
NNPS -> 'Poles'
NNPS -> 'Products'
NNPS -> 'Republicans'
NNPS -> 'Resources'
NNPS -> 'Rights'
NNPS -> 'Rothschilds'
NNPS -> 'Savings'
NNPS -> 'Sciences'
NNPS -> 'Securities'
NNPS -> 'Services'
NNPS -> 'Soviets'
NNPS -> 'States'
NNPS -> 'Statistics'
NNPS -> 'Stores'
NNPS -> 'Systems'
NNPS -> 'Technologies'
NNPS -> 'Texans'
NNPS -> 'Times'
NNPS -> 'Treasurys'
NNPS -> 'Utilities'
NNPS -> 'Workers'
NNPS -> 'assets'
NNPS -> 'rates'
ADVPLOC -> IN
ADVPLOC -> IN NP
ADVPLOC -> IN PP
ADVPLOC -> JJ
ADVPLOC -> NP RB
ADVPLOC -> RB
ADVPLOC -> RB PP
ADVPLOC -> RB RB
UH -> 'no'
UH -> 'quack'
UH -> 'yes'
NPTMP -> DT NN
NPTMP -> DT NNS
NPTMP -> IN NN
NPTMP -> IN NPR
NPTMP -> JJ NN
NPTMP -> JJ NNS
NPTMP -> JJ NPR
NPTMP -> NN
NPTMP -> NN NN
NPTMP -> NP ADVP
NPTMP -> NP NPADV
NPTMP -> NP PP
NPTMP -> NP SBAR
NPTMP -> NPR
NPTMP -> NPR NP
NPTMP -> NPR QP
NPTMP -> QP
NPTMP -> QP NN
NPTMP -> QP NNS
NPTMP -> RB
NPTMP -> RB NN
NPTMP -> RB NPR
WHADVP -> IN
WHADVP -> RB WRB
WHADVP -> WRB
WHADVP -> WRB JJ
WHADVP -> WRB RB
NX -> NPR
ADVPLOCPRD -> RB
ADVPLOCPRD -> RB PP
JJS -> 'Most'
JJS -> 'best'
JJS -> 'biggest'
JJS -> 'busiest'
JJS -> 'greatest'
JJS -> 'highest'
JJS -> 'hottest'
JJS -> 'largest'
JJS -> 'latest'
JJS -> 'least'
JJS -> 'lowest'
JJS -> 'most'
JJS -> 'smallest'
JJS -> 'strongest'
JJS -> 'worst'
LS -> '3'
SINV -> VBD NP
SINV -> VP NP
SPRD -> VP
SPRD -> NP VP
PUNCquotequote -> "'"
PUNCquotequote -> "''"
VB -> 'Be'
VB -> 'Call'
VB -> 'Consider'
VB -> 'Do'
VB -> 'Give'
VB -> 'Let'
VB -> 'Take'
VB -> 'abandon'
VB -> 'absorb'
VB -> 'accept'
VB -> 'accommodate'
VB -> 'account'
VB -> 'achieve'
VB -> 'acquire'
VB -> 'act'
VB -> 'add'
VB -> 'address'
VB -> 'adjust'
VB -> 'adopt'
VB -> 'advise'
VB -> 'affect'
VB -> 'afford'
VB -> 'agree'
VB -> 'allow'
VB -> 'alter'
VB -> 'announce'
VB -> 'answer'
VB -> 'anticipate'
VB -> 'appeal'
VB -> 'appear'
VB -> 'apply'
VB -> 'approve'
VB -> 'argue'
VB -> 'arrange'
VB -> 'arrive'
VB -> 'ask'
VB -> 'assess'
VB -> 'assist'
VB -> 'assume'
VB -> 'assure'
VB -> 'attempt'
VB -> 'attract'
VB -> 'auction'
VB -> 'avoid'
VB -> 'back'
VB -> 'be'
VB -> 'bear'
VB -> 'beat'
VB -> 'become'
VB -> 'begin'
VB -> 'believe'
VB -> 'benefit'
VB -> 'bid'
VB -> 'blame'
VB -> 'block'
VB -> 'bolster'
VB -> 'boost'
VB -> 'borrow'
VB -> 'break'
VB -> 'bring'
VB -> 'build'
VB -> 'buy'
VB -> 'call'
VB -> 'cancel'
VB -> 'care'
VB -> 'carry'
VB -> 'catch'
VB -> 'cause'
VB -> 'challenge'
VB -> 'change'
VB -> 'check'
VB -> 'choose'
VB -> 'clear'
VB -> 'close'
VB -> 'collapse'
VB -> 'combine'
VB -> 'come'
VB -> 'comment'
VB -> 'compare'
VB -> 'compensate'
VB -> 'compete'
VB -> 'complete'
VB -> 'comply'
VB -> 'concentrate'
VB -> 'conduct'
VB -> 'consider'
VB -> 'continue'
VB -> 'contribute'
VB -> 'control'
VB -> 'convert'
VB -> 'cope'
VB -> 'correct'
VB -> 'cost'
VB -> 'count'
VB -> 'cover'
VB -> 'crack'
VB -> 'create'
VB -> 'curb'
VB -> 'curtail'
VB -> 'cut'
VB -> 'deal'
VB -> 'decide'
VB -> 'decline'
VB -> 'decrease'
VB -> 'defend'
VB -> 'delay'
VB -> 'deliver'
VB -> 'demand'
VB -> 'deny'
VB -> 'depend'
VB -> 'describe'
VB -> 'design'
VB -> 'destroy'
VB -> 'determine'
VB -> 'develop'
VB -> 'die'
VB -> 'differ'
VB -> 'disclose'
VB -> 'discover'
VB -> 'discuss'
VB -> 'distribute'
VB -> 'divest'
VB -> 'do'
VB -> 'double'
VB -> 'draw'
VB -> 'drive'
VB -> 'drop'
VB -> 'dump'
VB -> 'earn'
VB -> 'ease'
VB -> 'eat'
VB -> 'elaborate'
VB -> 'eliminate'
VB -> 'emerge'
VB -> 'enable'
VB -> 'enact'
VB -> 'encourage'
VB -> 'end'
VB -> 'engage'
VB -> 'enhance'
VB -> 'ensure'
VB -> 'enter'
VB -> 'erode'
VB -> 'establish'
VB -> 'estimate'
VB -> 'evaluate'
VB -> 'examine'
VB -> 'exceed'
VB -> 'exchange'
VB -> 'execute'
VB -> 'exercise'
VB -> 'exist'
VB -> 'expand'
VB -> 'expect'
VB -> 'expire'
VB -> 'explain'
VB -> 'explore'
VB -> 'export'
VB -> 'express'
VB -> 'extend'
VB -> 'face'
VB -> 'fall'
VB -> 'favor'
VB -> 'feel'
VB -> 'fend'
VB -> 'fight'
VB -> 'file'
VB -> 'fill'
VB -> 'finance'
VB -> 'find'
VB -> 'finish'
VB -> 'fit'
VB -> 'flee'
VB -> 'float'
VB -> 'fly'
VB -> 'focus'
VB -> 'follow'
VB -> 'force'
VB -> 'forget'
VB -> 'form'
VB -> 'fund'
VB -> 'gain'
VB -> 'generate'
VB -> 'get'
VB -> 'give'
VB -> 'go'
VB -> 'grow'
VB -> 'guarantee'
VB -> 'guess'
VB -> 'halt'
VB -> 'handle'
VB -> 'happen'
VB -> 'have'
VB -> 'head'
VB -> 'hear'
VB -> 'hedge'
VB -> 'help'
VB -> 'hide'
VB -> 'hire'
VB -> 'hit'
VB -> 'hold'
VB -> 'honor'
VB -> 'hurt'
VB -> 'identify'
VB -> 'imagine'
VB -> 'impose'
VB -> 'improve'
VB -> 'include'
VB -> 'increase'
VB -> 'indicate'
VB -> 'induce'
VB -> 'insist'
VB -> 'insure'
VB -> 'intend'
VB -> 'intensify'
VB -> 'intervene'
VB -> 'introduce'
VB -> 'invest'
VB -> 'investigate'
VB -> 'involve'
VB -> 'issue'
VB -> 'join'
VB -> 'judge'
VB -> 'jump'
VB -> 'justify'
VB -> 'keep'
VB -> 'kill'
VB -> 'know'
VB -> 'last'
VB -> 'launch'
VB -> 'lead'
VB -> 'learn'
VB -> 'leave'
VB -> 'lend'
VB -> 'let'
VB -> 'lift'
VB -> 'like'
VB -> 'limit'
VB -> 'listen'
VB -> 'live'
VB -> 'look'
VB -> 'lose'
VB -> 'lower'
VB -> 'maintain'
VB -> 'make'
VB -> 'manage'
VB -> 'market'
VB -> 'match'
VB -> 'maximize'
VB -> 'mean'
VB -> 'measure'
VB -> 'meet'
VB -> 'merge'
VB -> 'mind'
VB -> 'miss'
VB -> 'monitor'
VB -> 'move'
VB -> 'name'
VB -> 'need'
VB -> 'negotiate'
VB -> 'note'
VB -> 'notify'
VB -> 'obtain'
VB -> 'occur'
VB -> 'offer'
VB -> 'offset'
VB -> 'open'
VB -> 'operate'
VB -> 'oppose'
VB -> 'order'
VB -> 'oust'
VB -> 'overcome'
VB -> 'override'
VB -> 'own'
VB -> 'participate'
VB -> 'pass'
VB -> 'pay'
VB -> 'perform'
VB -> 'permit'
VB -> 'persuade'
VB -> 'pick'
VB -> 'place'
VB -> 'plan'
VB -> 'play'
VB -> 'point'
VB -> 'pose'
VB -> 'post'
VB -> 'postpone'
VB -> 'predict'
VB -> 'press'
VB -> 'pressure'
VB -> 'prevent'
VB -> 'proceed'
VB -> 'produce'
VB -> 'profit'
VB -> 'promote'
VB -> 'propose'
VB -> 'protect'
VB -> 'prove'
VB -> 'provide'
VB -> 'publish'
VB -> 'pull'
VB -> 'purchase'
VB -> 'pursue'
VB -> 'push'
VB -> 'put'
VB -> 'quit'
VB -> 'raise'
VB -> 'rally'
VB -> 'reach'
VB -> 'read'
VB -> 'realize'
VB -> 'receive'
VB -> 'recognize'
VB -> 'recommend'
VB -> 'record'
VB -> 'recover'
VB -> 'redeem'
VB -> 'reduce'
VB -> 'reflect'
VB -> 'reinforce'
VB -> 'reject'
VB -> 'remain'
VB -> 'remember'
VB -> 'remove'
VB -> 'reopen'
VB -> 'repay'
VB -> 'replace'
VB -> 'report'
VB -> 'represent'
VB -> 'require'
VB -> 'rescue'
VB -> 'reset'
VB -> 'resolve'
VB -> 'respond'
VB -> 'restore'
VB -> 'restrict'
VB -> 'restructure'
VB -> 'result'
VB -> 'resume'
VB -> 'retain'
VB -> 'retire'
VB -> 'return'
VB -> 'reveal'
VB -> 'review'
VB -> 'revive'
VB -> 'rewrite'
VB -> 'rise'
VB -> 'risk'
VB -> 'roll'
VB -> 'rule'
VB -> 'run'
VB -> 'satisfy'
VB -> 'save'
VB -> 'say'
VB -> 'scuttle'
VB -> 'see'
VB -> 'seek'
VB -> 'seem'
VB -> 'seize'
VB -> 'select'
VB -> 'sell'
VB -> 'send'
VB -> 'serve'
VB -> 'set'
VB -> 'settle'
VB -> 'share'
VB -> 'shift'
VB -> 'ship'
VB -> 'shore'
VB -> 'show'
VB -> 'shrink'
VB -> 'shut'
VB -> 'sign'
VB -> 'signal'
VB -> 'sit'
VB -> 'slash'
VB -> 'slow'
VB -> 'soar'
VB -> 'solve'
VB -> 'sort'
VB -> 'sound'
VB -> 'spark'
VB -> 'speak'
VB -> 'specify'
VB -> 'speculate'
VB -> 'speed'
VB -> 'spend'
VB -> 'spin'
VB -> 'spread'
VB -> 'spur'
VB -> 'stabilize'
VB -> 'stand'
VB -> 'start'
VB -> 'stay'
VB -> 'steal'
VB -> 'stem'
VB -> 'step'
VB -> 'stick'
VB -> 'stock'
VB -> 'stop'
VB -> 'strengthen'
VB -> 'strike'
VB -> 'study'
VB -> 'submit'
VB -> 'succeed'
VB -> 'suffer'
VB -> 'suggest'
VB -> 'supply'
VB -> 'support'
VB -> 'survive'
VB -> 'suspend'
VB -> 'switch'
VB -> 'take'
VB -> 'talk'
VB -> 'tap'
VB -> 'tell'
VB -> 'test'
VB -> 'testify'
VB -> 'think'
VB -> 'throw'
VB -> 'top'
VB -> 'total'
VB -> 'trade'
VB -> 'transfer'
VB -> 'transform'
VB -> 'travel'
VB -> 'treat'
VB -> 'trim'
VB -> 'trust'
VB -> 'try'
VB -> 'tumble'
VB -> 'turn'
VB -> 'understand'
VB -> 'underwrite'
VB -> 'unveil'
VB -> 'use'
VB -> 'veto'
VB -> 'violate'
VB -> 'visit'
VB -> 'vote'
VB -> 'wait'
VB -> 'walk'
VB -> 'want'
VB -> 'watch'
VB -> 'wear'
VB -> 'welcome'
VB -> 'win'
VB -> 'withdraw'
VB -> 'withstand'
VB -> 'woo'
VB -> 'work'
VB -> 'worry'
VB -> 'write'
VB -> 'yield'
SBAR -> S
SBAR -> PUNCbquotebquote S
SBAR -> IN S
SBAR -> DT S
SBAR -> IN SINV
SBAR -> RB S
SBAR -> WDT S
SBAR -> WHADJP S
SBAR -> WHADVP S
SBAR -> WHNP S
SBAR -> WHPP S
MD -> "'d"
MD -> "'ll"
MD -> 'Can'
MD -> 'ca'
MD -> 'can'
MD -> 'could'
MD -> 'may'
MD -> 'might'
MD -> 'must'
MD -> 'ought'
MD -> 'should'
MD -> 'will'
MD -> 'wo'
MD -> 'would'
SBARPRD -> S
SBARPRD -> IN S
SBARPRD -> WHADVP S
SBARPRD -> WHNP S
SBARADV -> IN S
SBARADV -> IN SINV
SBARADV -> RB S
SBARADV -> SINV
SBARADV -> WHADVP S
SBARADV -> WHNP S
SBARADV -> X S
NNS -> '1960s'
NNS -> '1970s'
NNS -> '1980s'
NNS -> '1990s'
NNS -> 'Americans'
NNS -> 'Bonds'
NNS -> 'CDs'
NNS -> 'CFCs'
NNS -> 'Democrats'
NNS -> 'EURODOLLARS'
NNS -> 'East'
NNS -> 'Germans'
NNS -> 'Investors'
NNS -> 'Issues'
NNS -> 'Japanese'
NNS -> 'LBOs'
NNS -> 'Notes'
NNS -> 'People'
NNS -> 'Republicans'
NNS -> 'Results'
NNS -> 'Securities'
NNS -> 'Soviets'
NNS -> 'Things'
NNS -> 'abortionrights'
NNS -> 'abortions'
NNS -> 'abuses'
NNS -> 'acceptances'
NNS -> 'accounts'
NNS -> 'accusations'
NNS -> 'acquisitions'
NNS -> 'acres'
NNS -> 'actions'
NNS -> 'activists'
NNS -> 'activities'
NNS -> 'adjusters'
NNS -> 'adjustments'
NNS -> 'ads'
NNS -> 'adults'
NNS -> 'advancers'
NNS -> 'advances'
NNS -> 'advertisers'
NNS -> 'advisers'
NNS -> 'advocates'
NNS -> 'affairs'
NNS -> 'affiliates'
NNS -> 'aftershocks'
NNS -> 'agencies'
NNS -> 'agents'
NNS -> 'agreements'
NNS -> 'aides'
NNS -> 'airlines'
NNS -> 'allegations'
NNS -> 'alliances'
NNS -> 'allies'
NNS -> 'alternatives'
NNS -> 'amounts'
NNS -> 'analysts'
NNS -> 'animals'
NNS -> 'announcements'
NNS -> 'answers'
NNS -> 'appeals'
NNS -> 'apples'
NNS -> 'applicants'
NNS -> 'applications'
NNS -> 'appointments'
NNS -> 'appropriations'
NNS -> 'arbitragers'
NNS -> 'areas'
NNS -> 'arguments'
NNS -> 'arms'
NNS -> 'arrangements'
NNS -> 'articles'
NNS -> 'aspects'
NNS -> 'assets'
NNS -> 'associates'
NNS -> 'attacks'
NNS -> 'attempts'
NNS -> 'attendants'
NNS -> 'attorneys'
NNS -> 'auctions'
NNS -> 'authorities'
NNS -> 'authors'
NNS -> 'averages'
NNS -> 'backers'
NNS -> 'bacteria'
NNS -> 'bankers'
NNS -> 'banks'
NNS -> 'bargains'
NNS -> 'barrels'
NNS -> 'barriers'
NNS -> 'bases'
NNS -> 'bells'
NNS -> 'beneficiaries'
NNS -> 'benefits'
NNS -> 'bidders'
NNS -> 'bids'
NNS -> 'bikes'
NNS -> 'billings'
NNS -> 'billions'
NNS -> 'bills'
NNS -> 'blacks'
NNS -> 'blocks'
NNS -> 'boards'
NNS -> 'bonds'
NNS -> 'books'
NNS -> 'borrowers'
NNS -> 'borrowings'
NNS -> 'bosses'
NNS -> 'boxes'
NNS -> 'branches'
NNS -> 'brands'
NNS -> 'breakers'
NNS -> 'briefs'
NNS -> 'broadcasts'
NNS -> 'brokers'
NNS -> 'brothers'
NNS -> 'budgets'
NNS -> 'bugs'
NNS -> 'builders'
NNS -> 'buildings'
NNS -> 'bureaucrats'
NNS -> 'bushels'
NNS -> 'businesses'
NNS -> 'businessmen'
NNS -> 'buyouts'
NNS -> 'buyers'
NNS -> 'calculations'
NNS -> 'calls'
NNS -> 'campaigns'
NNS -> 'camps'
NNS -> 'candidates'
NNS -> 'cans'
NNS -> 'capitalgains'
NNS -> 'cards'
NNS -> 'careers'
NNS -> 'carriers'
NNS -> 'cars'
NNS -> 'cases'
NNS -> 'categories'
NNS -> 'cattle'
NNS -> 'causes'
NNS -> 'cells'
NNS -> 'centers'
NNS -> 'cents'
NNS -> 'certificates'
NNS -> 'chains'
NNS -> 'challenges'
NNS -> 'chances'
NNS -> 'changes'
NNS -> 'channels'
NNS -> 'characters'
NNS -> 'charges'
NNS -> 'charities'
NNS -> 'charts'
NNS -> 'checks'
NNS -> 'chemicals'
NNS -> 'children'
NNS -> 'chips'
NNS -> 'choices'
NNS -> 'cigarettes'
NNS -> 'circuits'
NNS -> 'circumstances'
NNS -> 'cities'
NNS -> 'citizens'
NNS -> 'claimants'
NNS -> 'claims'
NNS -> 'classes'
NNS -> 'clients'
NNS -> 'clothes'
NNS -> 'colleagues'
NNS -> 'colors'
NNS -> 'comments'
NNS -> 'commercials'
NNS -> 'commissions'
NNS -> 'commitments'
NNS -> 'committees'
NNS -> 'commodities'
NNS -> 'communications'
NNS -> 'communities'
NNS -> 'commuters'
NNS -> 'companies'
NNS -> 'comparisons'
NNS -> 'competitors'
NNS -> 'complaints'
NNS -> 'components'
NNS -> 'computers'
NNS -> 'concerns'
NNS -> 'concessions'
NNS -> 'conditions'
NNS -> 'conferees'
NNS -> 'consequences'
NNS -> 'conservatives'
NNS -> 'considerations'
NNS -> 'constituents'
NNS -> 'consultants'
NNS -> 'consumers'
NNS -> 'contractors'
NNS -> 'contracts'
NNS -> 'contributions'
NNS -> 'controls'
NNS -> 'conversations'
NNS -> 'copies'
NNS -> 'corporations'
NNS -> 'cosmetics'
NNS -> 'costs'
NNS -> 'countries'
NNS -> 'couples'
NNS -> 'courses'
NNS -> 'courts'
NNS -> 'credentials'
NNS -> 'creditors'
NNS -> 'credits'
NNS -> 'crimes'
NNS -> 'criminals'
NNS -> 'critics'
NNS -> 'crops'
NNS -> 'curbs'
NNS -> 'currencies'
NNS -> 'customers'
NNS -> 'cutbacks'
NNS -> 'cuts'
NNS -> 'cycles'
NNS -> 'damages'
NNS -> 'data'
NNS -> 'days'
NNS -> 'dealers'
NNS -> 'dealings'
NNS -> 'deals'
NNS -> 'deaths'
NNS -> 'debentures'
NNS -> 'debts'
NNS -> 'decades'
NNS -> 'decisions'
NNS -> 'decliners'
NNS -> 'declines'
NNS -> 'defaults'
NNS -> 'defects'
NNS -> 'defendants'
NNS -> 'defenses'
NNS -> 'delays'
NNS -> 'deliveries'
NNS -> 'demands'
NNS -> 'demonstrators'
NNS -> 'deposits'
NNS -> 'designs'
NNS -> 'desks'
NNS -> 'details'
NNS -> 'developers'
NNS -> 'developments'
NNS -> 'devices'
NNS -> 'diabetics'
NNS -> 'differences'
NNS -> 'difficulties'
NNS -> 'directors'
NNS -> 'disasters'
NNS -> 'discounts'
NNS -> 'discussions'
NNS -> 'diseases'
NNS -> 'displays'
NNS -> 'dissidents'
NNS -> 'districts'
NNS -> 'dividends'
NNS -> 'divisions'
NNS -> 'doctors'
NNS -> 'documents'
NNS -> 'dollars'
NNS -> 'donations'
NNS -> 'doors'
NNS -> 'dozens'
NNS -> 'drives'
NNS -> 'drops'
NNS -> 'drugs'
NNS -> 'duties'
NNS -> 'earnings'
NNS -> 'earthquakes'
NNS -> 'economics'
NNS -> 'economies'
NNS -> 'economists'
NNS -> 'editions'
NNS -> 'editors'
NNS -> 'effects'
NNS -> 'efforts'
NNS -> 'eggs'
NNS -> 'elections'
NNS -> 'electronics'
NNS -> 'elevators'
NNS -> 'emissions'
NNS -> 'employees'
NNS -> 'employers'
NNS -> 'engineers'
NNS -> 'enterprises'
NNS -> 'entities'
NNS -> 'entrepreneurs'
NNS -> 'environmentalists'
NNS -> 'environments'
NNS -> 'equities'
NNS -> 'errors'
NNS -> 'estimates'
NNS -> 'ethics'
NNS -> 'events'
NNS -> 'exchanges'
NNS -> 'executives'
NNS -> 'expectations'
NNS -> 'expenditures'
NNS -> 'expenses'
NNS -> 'experiments'
NNS -> 'experts'
NNS -> 'exporters'
NNS -> 'exports'
NNS -> 'exposures'
NNS -> 'eyes'
NNS -> 'facilities'
NNS -> 'factories'
NNS -> 'factors'
NNS -> 'facts'
NNS -> 'failures'
NNS -> 'families'
NNS -> 'fans'
NNS -> 'fares'
NNS -> 'farmers'
NNS -> 'farms'
NNS -> 'fears'
NNS -> 'features'
NNS -> 'feedlots'
NNS -> 'feelings'
NNS -> 'fees'
NNS -> 'feet'
NNS -> 'fibers'
NNS -> 'fields'
NNS -> 'figures'
NNS -> 'filings'
NNS -> 'films'
NNS -> 'finances'
NNS -> 'financialservices'
NNS -> 'financings'
NNS -> 'findings'
NNS -> 'firms'
NNS -> 'flights'
NNS -> 'fluctuations'
NNS -> 'foes'
NNS -> 'folks'
NNS -> 'forces'
NNS -> 'forecasts'
NNS -> 'foreigners'
NNS -> 'forms'
NNS -> 'fortunes'
NNS -> 'franchisees'
NNS -> 'francs'
NNS -> 'freedoms'
NNS -> 'friends'
NNS -> 'fuels'
NNS -> 'functions'
NNS -> 'fundamentals'
NNS -> 'funds'
NNS -> 'furriers'
NNS -> 'futures'
NNS -> 'gainers'
NNS -> 'gains'
NNS -> 'gallons'
NNS -> 'games'
NNS -> 'generations'
NNS -> 'genes'
NNS -> 'giants'
NNS -> 'goals'
NNS -> 'goods'
NNS -> 'governments'
NNS -> 'governors'
NNS -> 'graphics'
NNS -> 'grounds'
NNS -> 'groups'
NNS -> 'guarantees'
NNS -> 'guests'
NNS -> 'guidelines'
NNS -> 'guilders'
NNS -> 'guns'
NNS -> 'guys'
NNS -> 'gyrations'
NNS -> 'hands'
NNS -> 'hats'
NNS -> 'headquarters'
NNS -> 'hearings'
NNS -> 'heels'
NNS -> 'highs'
NNS -> 'hits'
NNS -> 'holders'
NNS -> 'holdings'
NNS -> 'homes'
NNS -> 'hopes'
NNS -> 'hospitals'
NNS -> 'hotels'
NNS -> 'hours'
NNS -> 'households'
NNS -> 'houses'
NNS -> 'hundreds'
NNS -> 'hunters'
NNS -> 'hurdles'
NNS -> 'ideas'
NNS -> 'imbalances'
NNS -> 'implications'
NNS -> 'imports'
NNS -> 'improvements'
NNS -> 'incentives'
NNS -> 'inches'
NNS -> 'increases'
NNS -> 'indexes'
NNS -> 'indications'
NNS -> 'indicators'
NNS -> 'individuals'
NNS -> 'industrials'
NNS -> 'industries'
NNS -> 'initiatives'
NNS -> 'injuries'
NNS -> 'inquiries'
NNS -> 'insiders'
NNS -> 'installations'
NNS -> 'institutions'
NNS -> 'instructions'
NNS -> 'instruments'
NNS -> 'insurers'
NNS -> 'interests'
NNS -> 'interviews'
NNS -> 'inventories'
NNS -> 'investigations'
NNS -> 'investigators'
NNS -> 'investments'
NNS -> 'investors'
NNS -> 'issuers'
NNS -> 'issues'
NNS -> 'items'
NNS -> 'jackets'
NNS -> 'jobs'
NNS -> 'journalists'
NNS -> 'judges'
NNS -> 'jurors'
NNS -> 'justices'
NNS -> 'kids'
NNS -> 'kinds'
NNS -> 'kronor'
NNS -> 'lawmakers'
NNS -> 'laws'
NNS -> 'lawsuits'
NNS -> 'lawyers'
NNS -> 'leaders'
NNS -> 'legislators'
NNS -> 'lenders'
NNS -> 'letters'
NNS -> 'levels'
NNS -> 'liabilities'
NNS -> 'liberals'
NNS -> 'licenses'
NNS -> 'lights'
NNS -> 'limits'
NNS -> 'lines'
NNS -> 'links'
NNS -> 'lire'
NNS -> 'lists'
NNS -> 'lives'
NNS -> 'loans'
NNS -> 'locations'
NNS -> 'losers'
NNS -> 'losses'
NNS -> 'lots'
NNS -> 'lows'
NNS -> 'machines'
NNS -> 'machinists'
NNS -> 'magazines'
NNS -> 'mainframes'
NNS -> 'makers'
NNS -> 'managers'
NNS -> 'manufacturers'
NNS -> 'margins'
NNS -> 'marketmakers'
NNS -> 'marketers'
NNS -> 'markets'
NNS -> 'marks'
NNS -> 'masters'
NNS -> 'materials'
NNS -> 'matters'
NNS -> 'maturities'
NNS -> 'means'
NNS -> 'measures'
NNS -> 'media'
NNS -> 'meetings'
NNS -> 'members'
NNS -> 'men'
NNS -> 'merchants'
NNS -> 'messages'
NNS -> 'metals'
NNS -> 'microprocessors'
NNS -> 'middlemen'
NNS -> 'miles'
NNS -> 'milestones'
NNS -> 'millions'
NNS -> 'mines'
NNS -> 'ministers'
NNS -> 'minutes'
NNS -> 'models'
NNS -> 'moments'
NNS -> 'months'
NNS -> 'mortgages'
NNS -> 'moves'
NNS -> 'movies'
NNS -> 'multiples'
NNS -> 'municipalities'
NNS -> 'municipals'
NNS -> 'names'
NNS -> 'nations'
NNS -> 'needs'
NNS -> 'negotiations'
NNS -> 'negotiators'
NNS -> 'neighborhoods'
NNS -> 'neighbors'
NNS -> 'networks'
NNS -> 'newcomers'
NNS -> 'newspapers'
NNS -> 'notes'
NNS -> 'numbers'
NNS -> 'objections'
NNS -> 'objectives'
NNS -> 'obligations'
NNS -> 'observers'
NNS -> 'occasions'
NNS -> 'odds'
NNS -> 'offerings'
NNS -> 'offers'
NNS -> 'officers'
NNS -> 'offices'
NNS -> 'officials'
NNS -> 'ones'
NNS -> 'operations'
NNS -> 'operators'
NNS -> 'opinions'
NNS -> 'opponents'
NNS -> 'opportunities'
NNS -> 'options'
NNS -> 'orders'
NNS -> 'organizations'
NNS -> 'others'
NNS -> 'ounces'
NNS -> 'outflows'
NNS -> 'outlays'
NNS -> 'outlets'
NNS -> 'outsiders'
NNS -> 'owners'
NNS -> 'packagedgoods'
NNS -> 'packages'
NNS -> 'pages'
NNS -> 'paintings'
NNS -> 'panels'
NNS -> 'papers'
NNS -> 'parents'
NNS -> 'participants'
NNS -> 'parties'
NNS -> 'partners'
NNS -> 'partnerships'
NNS -> 'parts'
NNS -> 'passengers'
NNS -> 'patients'
NNS -> 'patterns'
NNS -> 'payments'
NNS -> 'pence'
NNS -> 'pencils'
NNS -> 'people'
NNS -> 'periods'
NNS -> 'permits'
NNS -> 'personnel'
NNS -> 'pharmaceuticals'
NNS -> 'phones'
NNS -> 'pickers'
NNS -> 'pictures'
NNS -> 'pieces'
NNS -> 'pigs'
NNS -> 'pilots'
NNS -> 'places'
NNS -> 'plaintiffs'
NNS -> 'planes'
NNS -> 'planners'
NNS -> 'plans'
NNS -> 'plants'
NNS -> 'plastics'
NNS -> 'players'
NNS -> 'pockets'
NNS -> 'points'
NNS -> 'police'
NNS -> 'policies'
NNS -> 'policyholders'
NNS -> 'politicians'
NNS -> 'politics'
NNS -> 'polls'
NNS -> 'portfolios'
NNS -> 'portions'
NNS -> 'positions'
NNS -> 'posts'
NNS -> 'pounds'
NNS -> 'powers'
NNS -> 'practices'
NNS -> 'predictions'
NNS -> 'preferences'
NNS -> 'premiums'
NNS -> 'pressures'
NNS -> 'prices'
NNS -> 'priorities'
NNS -> 'prisons'
NNS -> 'problems'
NNS -> 'procedures'
NNS -> 'proceedings'
NNS -> 'proceeds'
NNS -> 'processors'
NNS -> 'producers'
NNS -> 'products'
NNS -> 'professionals'
NNS -> 'profits'
NNS -> 'programs'
NNS -> 'projections'
NNS -> 'projects'
NNS -> 'promises'
NNS -> 'promotions'
NNS -> 'properties'
NNS -> 'proponents'
NNS -> 'proposals'
NNS -> 'pros'
NNS -> 'prosecutions'
NNS -> 'prosecutors'
NNS -> 'prospects'
NNS -> 'proteins'
NNS -> 'protesters'
NNS -> 'protests'
NNS -> 'provisions'
NNS -> 'publications'
NNS -> 'publishers'
NNS -> 'punts'
NNS -> 'purchasers'
NNS -> 'purchases'
NNS -> 'purposes'
NNS -> 'puts'
NNS -> 'quantities'
NNS -> 'quarters'
NNS -> 'questions'
NNS -> 'quotas'
NNS -> 'quotations'
NNS -> 'raiders'
NNS -> 'rallies'
NNS -> 'ranks'
NNS -> 'rates'
NNS -> 'ratings'
NNS -> 'ratios'
NNS -> 'reactions'
NNS -> 'readers'
NNS -> 'reasons'
NNS -> 'rebates'
NNS -> 'rebels'
NNS -> 'receipts'
NNS -> 'recommendations'
NNS -> 'records'
NNS -> 'redemptions'
NNS -> 'reductions'
NNS -> 'reformers'
NNS -> 'reforms'
NNS -> 'refugees'
NNS -> 'refunds'
NNS -> 'regions'
NNS -> 'regulations'
NNS -> 'regulators'
NNS -> 'relations'
NNS -> 'relationships'
NNS -> 'releases'
NNS -> 'remarks'
NNS -> 'rents'
NNS -> 'repairs'
NNS -> 'reporters'
NNS -> 'reports'
NNS -> 'representatives'
NNS -> 'requests'
NNS -> 'requirements'
NNS -> 'researchers'
NNS -> 'reserves'
NNS -> 'residents'
NNS -> 'resignations'
NNS -> 'resources'
NNS -> 'respondents'
NNS -> 'responses'
NNS -> 'responsibilities'
NNS -> 'restaurants'
NNS -> 'restraints'
NNS -> 'restrictions'
NNS -> 'results'
NNS -> 'retailers'
NNS -> 'returns'
NNS -> 'revenues'
NNS -> 'rights'
NNS -> 'ringers'
NNS -> 'risks'
NNS -> 'rivals'
NNS -> 'roads'
NNS -> 'rocks'
NNS -> 'rooms'
NNS -> 'routes'
NNS -> 'rules'
NNS -> 'rumors'
NNS -> 'salaries'
NNS -> 'sales'
NNS -> 'salesmen'
NNS -> 'salespeople'
NNS -> 'sanctions'
NNS -> 'savings'
NNS -> 'scandals'
NNS -> 'scenarios'
NNS -> 'scenes'
NNS -> 'schedules'
NNS -> 'schools'
NNS -> 'scientists'
NNS -> 'scores'
NNS -> 'screens'
NNS -> 'seats'
NNS -> 'seconds'
NNS -> 'secrets'
NNS -> 'sections'
NNS -> 'sectors'
NNS -> 'securities'
NNS -> 'seeds'
NNS -> 'segments'
NNS -> 'sellers'
NNS -> 'senators'
NNS -> 'sentences'
NNS -> 'services'
NNS -> 'sessions'
NNS -> 'setbacks'
NNS -> 'sets'
NNS -> 'settlements'
NNS -> 'shareholders'
NNS -> 'shares'
NNS -> 'sheets'
NNS -> 'shipments'
NNS -> 'shippers'
NNS -> 'ships'
NNS -> 'shocks'
NNS -> 'shops'
NNS -> 'shows'
NNS -> 'sidelines'
NNS -> 'sides'
NNS -> 'signals'
NNS -> 'signs'
NNS -> 'sites'
NNS -> 'skills'
NNS -> 'soldiers'
NNS -> 'solutions'
NNS -> 'sorts'
NNS -> 'sources'
NNS -> 'specialists'
NNS -> 'speculators'
NNS -> 'spirits'
NNS -> 'sports'
NNS -> 'spots'
NNS -> 'staffers'
NNS -> 'stages'
NNS -> 'stakes'
NNS -> 'standards'
NNS -> 'starts'
NNS -> 'statements'
NNS -> 'states'
NNS -> 'stations'
NNS -> 'statistics'
NNS -> 'statutes'
NNS -> 'steelmakers'
NNS -> 'steps'
NNS -> 'stockholders'
NNS -> 'stocks'
NNS -> 'stones'
NNS -> 'stores'
NNS -> 'stories'
NNS -> 'strategies'
NNS -> 'strategists'
NNS -> 'streets'
NNS -> 'structures'
NNS -> 'students'
NNS -> 'studies'
NNS -> 'studios'
NNS -> 'styles'
NNS -> 'subjects'
NNS -> 'subscribers'
NNS -> 'subsidiaries'
NNS -> 'subsidies'
NNS -> 'suggestions'
NNS -> 'suits'
NNS -> 'superconductors'
NNS -> 'suppliers'
NNS -> 'supplies'
NNS -> 'supporters'
NNS -> 'surpluses'
NNS -> 'surveys'
NNS -> 'swings'
NNS -> 'symptoms'
NNS -> 'syndicates'
NNS -> 'systems'
NNS -> 'tables'
NNS -> 'tactics'
NNS -> 'takeovers'
NNS -> 'talks'
NNS -> 'tanks'
NNS -> 'targets'
NNS -> 'tariffs'
NNS -> 'tasks'
NNS -> 'taxes'
NNS -> 'taxpayers'
NNS -> 'teachers'
NNS -> 'teams'
NNS -> 'technologies'
NNS -> 'telecommunications'
NNS -> 'temperatures'
NNS -> 'terms'
NNS -> 'tests'
NNS -> 'thanks'
NNS -> 'thieves'
NNS -> 'things'
NNS -> 'thousands'
NNS -> 'thrifts'
NNS -> 'tickets'
NNS -> 'ties'
NNS -> 'times'
NNS -> 'tons'
NNS -> 'tools'
NNS -> 'tourists'
NNS -> 'toys'
NNS -> 'traders'
NNS -> 'trades'
NNS -> 'traffickers'
NNS -> 'transactions'
NNS -> 'transplants'
NNS -> 'travelers'
NNS -> 'tremors'
NNS -> 'trends'
NNS -> 'trials'
NNS -> 'troops'
NNS -> 'troubles'
NNS -> 'trucks'
NNS -> 'twothirds'
NNS -> 'types'
NNS -> 'underwriters'
NNS -> 'unions'
NNS -> 'units'
NNS -> 'universities'
NNS -> 'users'
NNS -> 'uses'
NNS -> 'utilities'
NNS -> 'values'
NNS -> 'vehicles'
NNS -> 'ventures'
NNS -> 'versions'
NNS -> 'vessels'
NNS -> 'victims'
NNS -> 'viewers'
NNS -> 'views'
NNS -> 'violations'
NNS -> 'visitors'
NNS -> 'voters'
NNS -> 'votes'
NNS -> 'wages'
NNS -> 'walls'
NNS -> 'warnings'
NNS -> 'warrants'
NNS -> 'wars'
NNS -> 'watchers'
NNS -> 'waves'
NNS -> 'ways'
NNS -> 'weapons'
NNS -> 'weeks'
NNS -> 'whites'
NNS -> 'windows'
NNS -> 'wines'
NNS -> 'winners'
NNS -> 'withdrawals'
NNS -> 'witnesses'
NNS -> 'woes'
NNS -> 'women'
NNS -> 'words'
NNS -> 'workers'
NNS -> 'works'
NNS -> 'workstations'
NNS -> 'worries'
NNS -> 'years'
NNS -> 'yen'
NNS -> 'yields'
NPADV -> DT
NPADV -> DT JJ
NPADV -> DT NN
NPADV -> DT RB
NPADV -> NP PP
NPADV -> NP SBAR
NPADV -> NP VP
NPADV -> PRP
NPADV -> QP
NPADV -> QP NN
NPADV -> QP NNS
NPADV -> QPMONEY
PUNCpoint -> '!'
PUNCpoint -> '.'
PUNCpoint -> '?'
WHNP -> DT
WHNP -> IN
WHNP -> NP PP
WHNP -> NP WHPP
WHNP -> RB WP
WHNP -> WDT
WHNP -> WDT NN
WHNP -> WDT NNS
WHNP -> WHADJP NN
WHNP -> WHNP PP
WHNP -> WHNP WHPP
WHNP -> WP
WHNP -> WP NN
WHNP -> WPdollar NN
WHNP -> WPdollar NNS
WHNP -> WRB JJ
SSBJ -> VP
X -> DT JJR
X -> IN
X -> PP
X -> SYM
X -> X NP
PPPRDLOC -> IN NP
PPTMPPRD -> IN NP
RBS -> 'best'
RBS -> 'most'
NP -> ADJP NN
NP -> ADJP NNS
NP -> ADJP NPR
NP -> ADJP NPRS
NP -> DT
NP -> DT ADJP
NP -> DT DT
NP -> DT FW
NP -> DT JJ
NP -> DT JJR
NP -> DT JJS
NP -> DT NN
NP -> DT NNS
NP -> DT NPR
NP -> DT NPRS
NP -> DT PRP
NP -> DT QP
NP -> DT QPMONEY
NP -> EX
NP -> FW
NP -> IN
NP -> IN NN
NP -> IN QP
NP -> JJ
NP -> JJ NN
NP -> JJ NNS
NP -> JJ NPR
NP -> JJ NPRS
NP -> JJ QP
NP -> JJ VBG
NP -> JJR
NP -> JJR NN
NP -> JJR NNS
NP -> JJS
NP -> JJS NNS
NP -> NAC NNS
NP -> NAC NPR
NP -> NN
NP -> NN PUNCpoint
NP -> NN PUNCcolon
NP -> NN JJ
NP -> NN NN
NP -> NN NNS
NP -> NN NPR
NP -> NN QP
NP -> NN RB
NP -> NN S
NP -> NN SBAR
NP -> NN VBG
NP -> NNS
NP -> NNS PUNCcolon
NP -> NNS NN
NP -> NNS NNS
NP -> NNS S
NP -> NNS SBAR
NP -> NP
NP -> NP PUNCcolon
NP -> NP ADJP
NP -> NP ADVP
NP -> NP ADVPLOC
NP -> NP ADVPTMP
NP -> NP NNS
NP -> NP NP
NP -> NP NPADV
NP -> NP NPLOC
NP -> NP NPTMP
NP -> NP PP
NP -> NP PPLOC
NP -> NP PPTMP
NP -> NP PRN
NP -> NP RRC
NP -> NP S
NP -> NP SNOM
NP -> NP SBAR
NP -> NP SBARLOC
NP -> NP SBARPRP
NP -> NP SBARTMP
NP -> NP VP
NP -> NPdollar NN
NP -> NPdollar NNS
NP -> NPdollar NP
NP -> NPdollar NPR
NP -> NPdollar NPRS
NP -> NPdollar QPMONEY
NP -> NPR
NP -> NPR COMMA
NP -> NPR PUNCpoint
NP -> NPR PUNCcolon
NP -> NPR JJ
NP -> NPR NP
NP -> NPR PP
NP -> NPR QP
NP -> NPR VBZ
NP -> NPRS
NP -> NPRS PUNCcolon
NP -> NPRS NP
NP -> PRP
NP -> PRP NN
NP -> PRP NP
NP -> PRPdollar
NP -> PRPdollar JJ
NP -> PRPdollar NN
NP -> PRPdollar NNS
NP -> PRPdollar NPR
NP -> PRPdollar QPMONEY
NP -> QP
NP -> QP JJ
NP -> QP NN
NP -> QP NNS
NP -> QP NP
NP -> QP NPR
NP -> QP NPRS
NP -> QP PP
NP -> QP RB
NP -> QPMONEY
NP -> RB
NP -> RB DT
NP -> RB JJ
NP -> RB JJR
NP -> RB NN
NP -> RB NNS
NP -> RB NPR
NP -> RB QP
NP -> RB RB
NP -> RBR
NP -> RBS
NP -> S
NP -> SYM
NP -> VB
NP -> VB NN
NP -> VBG
NP -> VBG NN
NP -> VBG NNS
NP -> VBN
NP -> VBN NN
NP -> VBN NNS
NP -> WDT
PP -> FW NP
PP -> IN
PP -> IN ADJP
PP -> IN ADVP
PP -> IN ADVPTMP
PP -> IN NP
PP -> IN NPdollar
PP -> IN NPLOC
PP -> IN NPTMP
PP -> IN PP
PP -> IN PPLOC
PP -> IN PPTMP
PP -> IN SNOM
PP -> IN SBAR
PP -> IN SBARNOM
PP -> NPR NP
PP -> PP PP
PP -> RB
PP -> RB ADJP
PP -> RB PP
PP -> RP
PP -> RP NP
PP -> TO
PP -> TO ADJP
PP -> TO NP
PP -> TO NPdollar
PP -> TO SNOM
PP -> TO SBARNOM
PP -> VBG NP
PP -> VBG PP
PP -> VBG SNOM
PP -> VBN NP
PP -> VBN PP
PP -> VBN SBAR
INTJ -> RB
INTJ -> UH
INTJ -> UH PUNCpoint
INTJ -> VB
PRT -> IN
PRT -> RB
PRT -> RP
VBG -> 'Excluding'
VBG -> 'Having'
VBG -> 'Looking'
VBG -> 'Noting'
VBG -> 'Reflecting'
VBG -> 'Using'
VBG -> 'accepting'
VBG -> 'accompanying'
VBG -> 'according'
VBG -> 'acquiring'
VBG -> 'acting'
VBG -> 'adding'
VBG -> 'adjusting'
VBG -> 'adopting'
VBG -> 'advancing'
VBG -> 'advertising'
VBG -> 'advising'
VBG -> 'affecting'
VBG -> 'agreeing'
VBG -> 'alleging'
VBG -> 'allowing'
VBG -> 'announcing'
VBG -> 'arguing'
VBG -> 'arranging'
VBG -> 'asking'
VBG -> 'assuming'
VBG -> 'attempting'
VBG -> 'attending'
VBG -> 'attracting'
VBG -> 'avoiding'
VBG -> 'awaiting'
VBG -> 'backing'
VBG -> 'banking'
VBG -> 'banning'
VBG -> 'becoming'
VBG -> 'beginning'
VBG -> 'being'
VBG -> 'believing'
VBG -> 'betting'
VBG -> 'bidding'
VBG -> 'blocking'
VBG -> 'boosting'
VBG -> 'breaking'
VBG -> 'bringing'
VBG -> 'building'
VBG -> 'buying'
VBG -> 'calling'
VBG -> 'carrying'
VBG -> 'catching'
VBG -> 'causing'
VBG -> 'challenging'
VBG -> 'changing'
VBG -> 'charging'
VBG -> 'circulating'
VBG -> 'citing'
VBG -> 'claiming'
VBG -> 'climbing'
VBG -> 'closing'
VBG -> 'collecting'
VBG -> 'coming'
VBG -> 'competing'
VBG -> 'complaining'
VBG -> 'concerning'
VBG -> 'conducting'
VBG -> 'confirming'
VBG -> 'considering'
VBG -> 'consisting'
VBG -> 'consulting'
VBG -> 'containing'
VBG -> 'continuing'
VBG -> 'contributing'
VBG -> 'controlling'
VBG -> 'coping'
VBG -> 'counting'
VBG -> 'covering'
VBG -> 'creating'
VBG -> 'cutting'
VBG -> 'dealing'
VBG -> 'deciding'
VBG -> 'declaring'
VBG -> 'declining'
VBG -> 'defending'
VBG -> 'delivering'
VBG -> 'demanding'
VBG -> 'denouncing'
VBG -> 'depending'
VBG -> 'designing'
VBG -> 'developing'
VBG -> 'discounting'
VBG -> 'discouraging'
VBG -> 'discussing'
VBG -> 'doing'
VBG -> 'doubling'
VBG -> 'driving'
VBG -> 'dropping'
VBG -> 'earning'
VBG -> 'easing'
VBG -> 'eating'
VBG -> 'eliminating'
VBG -> 'emerging'
VBG -> 'encouraging'
VBG -> 'ending'
VBG -> 'entering'
VBG -> 'equaling'
VBG -> 'establishing'
VBG -> 'exceeding'
VBG -> 'excluding'
VBG -> 'existing'
VBG -> 'expanding'
VBG -> 'expecting'
VBG -> 'experiencing'
VBG -> 'explaining'
VBG -> 'exploring'
VBG -> 'extending'
VBG -> 'facing'
VBG -> 'failing'
VBG -> 'falling'
VBG -> 'featuring'
VBG -> 'feeling'
VBG -> 'fighting'
VBG -> 'filing'
VBG -> 'filling'
VBG -> 'financing'
VBG -> 'finding'
VBG -> 'floating'
VBG -> 'flying'
VBG -> 'focusing'
VBG -> 'following'
VBG -> 'forcing'
VBG -> 'gaining'
VBG -> 'getting'
VBG -> 'giving'
VBG -> 'going'
VBG -> 'granting'
VBG -> 'growing'
VBG -> 'handling'
VBG -> 'happening'
VBG -> 'having'
VBG -> 'heading'
VBG -> 'helping'
VBG -> 'hiring'
VBG -> 'hitting'
VBG -> 'holding'
VBG -> 'hoping'
VBG -> 'hurting'
VBG -> 'ignoring'
VBG -> 'imposing'
VBG -> 'improving'
VBG -> 'including'
VBG -> 'increasing'
VBG -> 'indicating'
VBG -> 'installing'
VBG -> 'intensifying'
VBG -> 'introducing'
VBG -> 'investigating'
VBG -> 'investing'
VBG -> 'involving'
VBG -> 'issuing'
VBG -> 'joining'
VBG -> 'keeping'
VBG -> 'killing'
VBG -> 'lagging'
VBG -> 'launching'
VBG -> 'laying'
VBG -> 'leading'
VBG -> 'learning'
VBG -> 'leaving'
VBG -> 'lending'
VBG -> 'letting'
VBG -> 'limiting'
VBG -> 'listening'
VBG -> 'living'
VBG -> 'lobbying'
VBG -> 'looking'
VBG -> 'losing'
VBG -> 'lowering'
VBG -> 'lying'
VBG -> 'maintaining'
VBG -> 'making'
VBG -> 'managing'
VBG -> 'manufacturing'
VBG -> 'marketing'
VBG -> 'marking'
VBG -> 'matching'
VBG -> 'maturing'
VBG -> 'meaning'
VBG -> 'meeting'
VBG -> 'missing'
VBG -> 'mounting'
VBG -> 'moving'
VBG -> 'mulling'
VBG -> 'negotiating'
VBG -> 'noting'
VBG -> 'obtaining'
VBG -> 'offering'
VBG -> 'offsetting'
VBG -> 'opening'
VBG -> 'operating'
VBG -> 'ordering'
VBG -> 'overseeing'
VBG -> 'owning'
VBG -> 'participating'
VBG -> 'passing'
VBG -> 'paying'
VBG -> 'pending'
VBG -> 'performing'
VBG -> 'picking'
VBG -> 'planning'
VBG -> 'playing'
VBG -> 'plunging'
VBG -> 'posting'
VBG -> 'pouring'
VBG -> 'predicting'
VBG -> 'preparing'
VBG -> 'preserving'
VBG -> 'preventing'
VBG -> 'processing'
VBG -> 'producing'
VBG -> 'projecting'
VBG -> 'promoting'
VBG -> 'prompting'
VBG -> 'proposing'
VBG -> 'protecting'
VBG -> 'providing'
VBG -> 'publishing'
VBG -> 'pulling'
VBG -> 'purchasing'
VBG -> 'pursuing'
VBG -> 'pushing'
VBG -> 'putting'
VBG -> 'raising'
VBG -> 'ranging'
VBG -> 'reaching'
VBG -> 'reacting'
VBG -> 'reading'
VBG -> 'receiving'
VBG -> 'recovering'
VBG -> 'reducing'
VBG -> 'referring'
VBG -> 'reflecting'
VBG -> 'regarding'
VBG -> 'relating'
VBG -> 'remaining'
VBG -> 'removing'
VBG -> 'replacing'
VBG -> 'reporting'
VBG -> 'representing'
VBG -> 'requiring'
VBG -> 'resigning'
VBG -> 'resisting'
VBG -> 'responding'
VBG -> 'resulting'
VBG -> 'retaining'
VBG -> 'retiring'
VBG -> 'returning'
VBG -> 'reversing'
VBG -> 'reviewing'
VBG -> 'riding'
VBG -> 'rising'
VBG -> 'ruling'
VBG -> 'running'
VBG -> 'rushing'
VBG -> 'sacrificing'
VBG -> 'saying'
VBG -> 'scrambling'
VBG -> 'searching'
VBG -> 'seeing'
VBG -> 'seeking'
VBG -> 'selling'
VBG -> 'sending'
VBG -> 'serving'
VBG -> 'setting'
VBG -> 'settling'
VBG -> 'shifting'
VBG -> 'shipping'
VBG -> 'showing'
VBG -> 'shrinking'
VBG -> 'signing'
VBG -> 'sitting'
VBG -> 'sliding'
VBG -> 'slipping'
VBG -> 'slowing'
VBG -> 'soaring'
VBG -> 'soliciting'
VBG -> 'spending'
VBG -> 'stabilizing'
VBG -> 'standing'
VBG -> 'starting'
VBG -> 'stemming'
VBG -> 'sticking'
VBG -> 'struggling'
VBG -> 'studying'
VBG -> 'succeeding'
VBG -> 'suggesting'
VBG -> 'supporting'
VBG -> 'surrounding'
VBG -> 'surviving'
VBG -> 'taking'
VBG -> 'talking'
VBG -> 'targeting'
VBG -> 'telling'
VBG -> 'testing'
VBG -> 'thinking'
VBG -> 'throwing'
VBG -> 'totaling'
VBG -> 'trading'
VBG -> 'traveling'
VBG -> 'trying'
VBG -> 'tumbling'
VBG -> 'turning'
VBG -> 'underlying'
VBG -> 'urging'
VBG -> 'using'
VBG -> 'violating'
VBG -> 'voting'
VBG -> 'waiting'
VBG -> 'warning'
VBG -> 'watching'
VBG -> 'weakening'
VBG -> 'wearing'
VBG -> 'winning'
VBG -> 'wondering'
VBG -> 'working'
VBG -> 'worrying'
VBG -> 'worsening'
VBG -> 'writing'
VBG -> 'yielding'
PUNCcolon -> '-'
PUNCcolon -> '--'
PUNCcolon -> '...'
PUNCcolon -> ':'
PUNCcolon -> ';'
WHPP -> IN WHNP
WHPP -> TO WHNP
SQ -> VP
SQ -> MD VP
SPRP -> VP
SPRP -> ADVP VP
ADJP -> PUNCdollar JJ
ADJP -> ADJP PP
ADJP -> ADJP PRN
ADJP -> ADJP SBAR
ADJP -> ADVP JJ
ADJP -> ADVP VBN
ADJP -> IN JJ
ADJP -> IN NN
ADJP -> JJ
ADJP -> JJ JJ
ADJP -> JJ JJR
ADJP -> JJ JJS
ADJP -> JJ NN
ADJP -> JJ NP
ADJP -> JJ NPTMP
ADJP -> JJ PP
ADJP -> JJ PPTMP
ADJP -> JJ S
ADJP -> JJ SBAR
ADJP -> JJR
ADJP -> JJR JJ
ADJP -> JJR PP
ADJP -> JJS
ADJP -> JJS JJ
ADJP -> NN VBN
ADJP -> NP JJ
ADJP -> NP JJR
ADJP -> NPADV JJR
ADJP -> NPR JJ
ADJP -> QP
ADJP -> QP JJ
ADJP -> QP JJR
ADJP -> QP NN
ADJP -> QPMONEY
ADJP -> RB
ADJP -> RB DT
ADJP -> RB JJ
ADJP -> RB JJR
ADJP -> RB JJS
ADJP -> RB VBG
ADJP -> RB VBN
ADJP -> RBR
ADJP -> RBR JJ
ADJP -> RBS JJ
ADJP -> VBN
ADJP -> VBN NP
ADJP -> VBN PP
PPLOCPRD -> IN NP
SADV -> ADJPPRD
SADV -> ADVP VP
SADV -> ADVPPRD
SADV -> ADVPTMP VP
SADV -> NPPRD
SADV -> PPPRD
SADV -> VP
SADV -> NP VP
NNP -> "'s"
NNP -> 'Apoint'
NNP -> 'ApointPpoint'
NNP -> 'AB'
NNP -> 'ABB'
NNP -> 'ABC'
NNP -> 'ABM'
NNP -> 'AG'
NNP -> 'AMR'
NNP -> 'ANC'
NNP -> 'ASKO'
NNP -> 'AT&T'
NNP -> 'AZT'
NNP -> 'Abramson'
NNP -> 'Acceptance'
NNP -> 'Accounting'
NNP -> 'Achenbaum'
NNP -> 'Acquisition'
NNP -> 'Act'
NNP -> 'Admpoint'
NNP -> 'Administration'
NNP -> 'Advanced'
NNP -> 'Advertising'
NNP -> 'Aer'
NNP -> 'Aeroflot'
NNP -> 'Aerospace'
NNP -> 'Aetna'
NNP -> 'Africa'
NNP -> 'African'
NNP -> 'Agency'
NNP -> 'Agnos'
NNP -> 'Agricole'
NNP -> 'Agriculture'
NNP -> 'Air'
NNP -> 'Aircraft'
NNP -> 'Airlines'
NNP -> 'Airport'
NNP -> 'Airways'
NNP -> 'Akzo'
NNP -> 'Alan'
NNP -> 'Albert'
NNP -> 'Alex'
NNP -> 'Alexander'
NNP -> 'Alfred'
NNP -> 'Allen'
NNP -> 'Alliance'
NNP -> 'Allianz'
NNP -> 'Alto'
NNP -> 'Alvin'
NNP -> 'Ambrosiano'
NNP -> 'Amendment'
NNP -> 'America'
NNP -> 'American'
NNP -> 'Amex'
NNP -> 'Amoco'
NNP -> 'Analytical'
NNP -> 'Anchor'
NNP -> 'Anderson'
NNP -> 'Andersson'
NNP -> 'Andrew'
NNP -> 'Andy'
NNP -> 'Angeles'
NNP -> 'Anheuser'
NNP -> 'Anne'
NNP -> 'Antar'
NNP -> 'Anthony'
NNP -> 'Antonio'
NNP -> 'Apogee'
NNP -> 'Apple'
NNP -> 'Applied'
NNP -> 'April'
NNP -> 'Aquino'
NNP -> 'Arabia'
NNP -> 'Arafat'
NNP -> 'Arbel'
NNP -> 'Arby'
NNP -> 'Arco'
NNP -> 'Area'
NNP -> 'Arizpoint'
NNP -> 'Arizona'
NNP -> 'Arkansas'
NNP -> 'Armonk'
NNP -> 'Armstrong'
NNP -> 'Army'
NNP -> 'Arnold'
NNP -> 'Arrow'
NNP -> 'Art'
NNP -> 'Arthur'
NNP -> 'Artist'
NNP -> 'Ashland'
NNP -> 'Asia'
NNP -> 'Assembly'
NNP -> 'Asset'
NNP -> 'Assistant'
NNP -> 'Associates'
NNP -> 'Association'
NNP -> 'Atlanta'
NNP -> 'Atlantic'
NNP -> 'Atlantis'
NNP -> 'Attorney'
NNP -> 'Augpoint'
NNP -> 'August'
NNP -> 'Austin'
NNP -> 'Australia'
NNP -> 'Authority'
NNP -> 'Avenue'
NNP -> 'Average'
NNP -> 'Aviation'
NNP -> 'Axa'
NNP -> 'Bpoint'
NNP -> 'BpointApointT'
NNP -> 'BNL'
NNP -> 'BSN'
NNP -> 'Baker'
NNP -> 'Ball'
NNP -> 'Bally'
NNP -> 'Baltimore'
NNP -> 'Banc'
NNP -> 'Banco'
NNP -> 'Bancorp'
NNP -> 'Bank'
NNP -> 'BankAmerica'
NNP -> 'Bankers'
NNP -> 'Banking'
NNP -> 'Bankruptcy'
NNP -> 'Banks'
NNP -> 'Banque'
NNP -> 'Banxquote'
NNP -> 'Barbara'
NNP -> 'Barney'
NNP -> 'Barre'
NNP -> 'Barry'
NNP -> 'Bartlett'
NNP -> 'Bass'
NNP -> 'Bates'
NNP -> 'Batibot'
NNP -> 'Bay'
NNP -> 'Beach'
NNP -> 'Bear'
NNP -> 'Beatrice'
NNP -> 'Beers'
NNP -> 'Beijing'
NNP -> 'Belgium'
NNP -> 'Bell'
NNP -> 'BellSouth'
NNP -> 'Bennett'
NNP -> 'Benson'
NNP -> 'Bergsma'
NNP -> 'Berkeley'
NNP -> 'Berlin'
NNP -> 'Berlitz'
NNP -> 'Bernard'
NNP -> 'Bernstein'
NNP -> 'Berry'
NNP -> 'Bethlehem'
NNP -> 'Beverly'
NNP -> 'Big'
NNP -> 'Bill'
NNP -> 'Birmingham'
NNP -> 'Black'
NNP -> 'Bloc'
NNP -> 'Block'
NNP -> 'Bloomingdale'
NNP -> 'Blue'
NNP -> 'Blumenfeld'
NNP -> 'Board'
NNP -> 'Bob'
NNP -> 'Bobby'
NNP -> 'Boeing'
NNP -> 'Boesel'
NNP -> 'Bofors'
NNP -> 'Bogart'
NNP -> 'Bolar'
NNP -> 'Bombay'
NNP -> 'Bond'
NNP -> 'Boren'
NNP -> 'Bork'
NNP -> 'Boston'
NNP -> 'Boyd'
NNP -> 'Bozell'
NNP -> 'Bradford'
NNP -> 'Bradley'
NNP -> 'Brady'
NNP -> 'Brands'
NNP -> 'Brawer'
NNP -> 'Brazil'
NNP -> 'Breeden'
NNP -> 'Brewing'
NNP -> 'Brian'
NNP -> 'Bridge'
NNP -> 'BristolMyers'
NNP -> 'Britain'
NNP -> 'British'
NNP -> 'Broadcasting'
NNP -> 'Bronx'
NNP -> 'Brooklyn'
NNP -> 'Brooks'
NNP -> 'Brothers'
NNP -> 'Brown'
NNP -> 'Brussels'
NNP -> 'Budapest'
NNP -> 'Budget'
NNP -> 'Buffett'
NNP -> 'Buick'
NNP -> 'Building'
NNP -> 'Bureau'
NNP -> 'Burgess'
NNP -> 'Burlington'
NNP -> 'Burmah'
NNP -> 'Burnham'
NNP -> 'Burt'
NNP -> 'Bush'
NNP -> 'Business'
NNP -> 'Businessland'
NNP -> 'Butler'
NNP -> 'Byrd'
NNP -> 'Cpoint'
NNP -> 'CBOE'
NNP -> 'CBS'
NNP -> CD
NNP -> 'CFCs'
NNP -> 'CFTC'
NNP -> 'CIA'
NNP -> 'CMS'
NNP -> 'CNN'
NNP -> 'CS'
NNP -> 'Cable'
NNP -> 'Cabrera'
NNP -> 'Cadillac'
NNP -> 'Calif'
NNP -> 'Califpoint'
NNP -> 'California'
NNP -> 'Caltrans'
NNP -> 'Cambria'
NNP -> 'Cambridge'
NNP -> 'Campbell'
NNP -> 'Campeau'
NNP -> 'Canaan'
NNP -> 'Canada'
NNP -> 'Canadian'
NNP -> 'Cancer'
NNP -> 'Candlestick'
NNP -> 'Capital'
NNP -> 'Capitol'
NNP -> 'Care'
NNP -> 'Carl'
NNP -> 'Carlos'
NNP -> 'Carnival'
NNP -> 'Carol'
NNP -> 'Carolina'
NNP -> 'Carpenter'
NNP -> 'Carson'
NNP -> 'Carter'
NNP -> 'Cathay'
NNP -> 'Cathcart'
NNP -> 'Catholic'
NNP -> 'Cellular'
NNP -> 'CenTrust'
NNP -> 'Census'
NNP -> 'Center'
NNP -> 'Central'
NNP -> 'Chairman'
NNP -> 'Chamber'
NNP -> 'Chan'
NNP -> 'Chancellor'
NNP -> 'Chancery'
NNP -> 'Chandler'
NNP -> 'Channel'
NNP -> 'Chapter'
NNP -> 'Charles'
NNP -> 'Charleston'
NNP -> 'Charlotte'
NNP -> 'Chase'
NNP -> 'Cheer'
NNP -> 'Chemical'
NNP -> 'Cheney'
NNP -> 'Chevrolet'
NNP -> 'Chevron'
NNP -> 'Chicago'
NNP -> 'Chief'
NNP -> 'China'
NNP -> 'Chinese'
NNP -> 'Christian'
NNP -> 'Christie'
NNP -> 'Christmas'
NNP -> 'Christopher'
NNP -> 'Chrysler'
NNP -> 'Church'
NNP -> 'Ciepoint'
NNP -> 'Cincinnati'
NNP -> 'Cineplex'
NNP -> 'Circuit'
NNP -> 'Citicorp'
NNP -> 'City'
NNP -> 'CityFed'
NNP -> 'Clara'
NNP -> 'Clark'
NNP -> 'Class'
NNP -> 'Clean'
NNP -> 'Cleveland'
NNP -> 'Club'
NNP -> 'Co'
NNP -> 'Copoint'
NNP -> 'Coast'
NNP -> 'CocaCola'
NNP -> 'Cocom'
NNP -> 'Code'
NNP -> 'Cohen'
NNP -> 'Coke'
NNP -> 'Coleman'
NNP -> 'Colgate'
NNP -> 'College'
NNP -> 'Colopoint'
NNP -> 'Colombia'
NNP -> 'Color'
NNP -> 'Colorado'
NNP -> 'Columbia'
NNP -> 'Commerce'
NNP -> 'Commerciale'
NNP -> 'Commission'
NNP -> 'Committee'
NNP -> 'Commodity'
NNP -> 'Commodore'
NNP -> 'Commonwealth'
NNP -> 'Communications'
NNP -> 'Communist'
NNP -> 'Community'
NNP -> 'Company'
NNP -> 'Compaq'
NNP -> 'Composite'
NNP -> 'Comprehensive'
NNP -> 'Computer'
NNP -> 'Conference'
NNP -> 'Congress'
NNP -> 'Coniston'
NNP -> 'Conn'
NNP -> 'Connpoint'
NNP -> 'Connaught'
NNP -> 'Connecticut'
NNP -> 'Conner'
NNP -> 'Consolidated'
NNP -> 'Constitution'
NNP -> 'Container'
NNP -> 'Continental'
NNP -> 'Contra'
NNP -> 'Control'
NNP -> 'Coors'
NNP -> 'Cornell'
NNP -> 'Corning'
NNP -> 'Corp'
NNP -> 'Corppoint'
NNP -> 'Corporate'
NNP -> 'Corr'
NNP -> 'Corry'
NNP -> 'Cospoint'
NNP -> 'Costa'
NNP -> 'Council'
NNP -> 'County'
NNP -> 'Court'
NNP -> 'Courtaulds'
NNP -> 'Courter'
NNP -> 'Craig'
NNP -> 'Cray'
NNP -> 'Credit'
NNP -> 'Creek'
NNP -> 'Cross'
NNP -> 'Cruise'
NNP -> 'Cuba'
NNP -> 'Cup'
NNP -> 'Cypress'
NNP -> 'Czechoslovakia'
NNP -> 'Dpoint'
NNP -> 'DpointCpoint'
NNP -> 'DpointTpoint'
NNP -> 'DAX'
NNP -> 'DD'
NNP -> 'DPC'
NNP -> 'DWG'
NNP -> 'Daily'
NNP -> 'DaimlerBenz'
NNP -> 'Daiwa'
NNP -> 'Dalkon'
NNP -> 'Dallas'
NNP -> 'Dan'
NNP -> 'Daniel'
NNP -> 'Danny'
NNP -> 'Darman'
NNP -> 'Data'
NNP -> 'Datapoint'
NNP -> 'Dataproducts'
NNP -> 'Dave'
NNP -> 'David'
NNP -> 'Davis'
NNP -> 'Day'
NNP -> 'De'
NNP -> 'Dean'
NNP -> 'Deaver'
NNP -> 'Dec'
NNP -> 'Decpoint'
NNP -> 'December'
NNP -> 'Defense'
NNP -> 'Del'
NNP -> 'Delaware'
NNP -> 'Delicious'
NNP -> 'Dell'
NNP -> 'Della'
NNP -> 'Delmed'
NNP -> 'Deloitte'
NNP -> 'Delta'
NNP -> 'Democrat'
NNP -> 'Democratic'
NNP -> 'Dennis'
NNP -> 'Dentsu'
NNP -> 'Denver'
NNP -> 'Department'
NNP -> 'Deposit'
NNP -> 'Detrex'
NNP -> 'Detroit'
NNP -> 'Deukmejian'
NNP -> 'Deutsche'
NNP -> 'Development'
NNP -> 'Di'
NNP -> 'Dick'
NNP -> 'Diego'
NNP -> 'Digest'
NNP -> 'Digital'
NNP -> 'Dingell'
NNP -> 'Dinkins'
NNP -> 'Director'
NNP -> 'Disney'
NNP -> 'District'
NNP -> 'Division'
NNP -> 'Dole'
NNP -> 'Dollar'
NNP -> 'Doman'
NNP -> 'Don'
NNP -> 'Donald'
NNP -> 'Donaldson'
NNP -> 'Donoghue'
NNP -> 'Donuts'
NNP -> 'Dorrance'
NNP -> 'Douglas'
NNP -> 'Dow'
NNP -> 'Dozen'
NNP -> 'Drpoint'
NNP -> 'Dresdner'
NNP -> 'Drexel'
NNP -> 'Dreyfus'
NNP -> 'Du'
NNP -> 'Dunkin'
NNP -> 'Dutch'
NNP -> 'Dynamics'
NNP -> 'Epoint'
NNP -> 'EC'
NNP -> 'EDT'
NNP -> 'EPA'
NNP -> 'EPO'
NNP -> 'Eagle'
NNP -> 'Earth'
NNP -> 'East'
NNP -> 'Eastern'
NNP -> 'Eastman'
NNP -> 'Economic'
NNP -> 'Economics'
NNP -> 'Edelman'
NNP -> 'Edison'
NNP -> 'Edisto'
NNP -> 'Education'
NNP -> 'Edward'
NNP -> 'Edwards'
NNP -> 'Egg'
NNP -> 'El'
NNP -> 'Electric'
NNP -> 'Elizabeth'
NNP -> 'Energy'
NNP -> 'Enfield'
NNP -> 'Engelken'
NNP -> 'Engineering'
NNP -> 'England'
NNP -> 'English'
NNP -> 'Enron'
NNP -> 'Entertainment'
NNP -> 'Environmental'
NNP -> 'Equipment'
NNP -> 'Equity'
NNP -> 'Erbamont'
NNP -> 'Erich'
NNP -> 'Estate'
NNP -> 'Eugene'
NNP -> 'Eurocom'
NNP -> 'Europe'
NNP -> 'European'
NNP -> 'Evans'
NNP -> 'Exchange'
NNP -> 'Exchequer'
NNP -> 'Executive'
NNP -> 'Express'
NNP -> 'Exterior'
NNP -> 'Exxon'
NNP -> 'Fpoint'
NNP -> 'FASB'
NNP -> 'FBI'
NNP -> 'FCC'
NNP -> 'FDA'
NNP -> 'FEMA'
NNP -> 'FHA'
NNP -> 'FTSE'
NNP -> 'FTC'
NNP -> 'Fair'
NNP -> 'Falcon'
NNP -> 'Family'
NNP -> 'Fannie'
NNP -> 'Fantasy'
NNP -> 'Far'
NNP -> 'Farmers'
NNP -> 'Fe'
NNP -> 'Febpoint'
NNP -> 'February'
NNP -> 'Fed'
NNP -> 'Federal'
NNP -> 'Federated'
NNP -> 'Federation'
NNP -> 'Femina'
NNP -> 'Ferranti'
NNP -> 'Fiat'
NNP -> 'Fidelity'
NNP -> 'Field'
NNP -> 'Fifth'
NNP -> 'Filipino'
NNP -> 'Finance'
NNP -> 'Financial'
NNP -> 'Financiere'
NNP -> 'Financing'
NNP -> 'Finland'
NNP -> 'Fireman'
NNP -> 'First'
NNP -> 'Fitzwater'
NNP -> 'Fla'
NNP -> 'Flapoint'
NNP -> 'Florida'
NNP -> 'Florio'
NNP -> 'Fluor'
NNP -> 'Foods'
NNP -> 'Football'
NNP -> 'Force'
NNP -> 'Ford'
NNP -> 'Foreign'
NNP -> 'Forest'
NNP -> 'Fort'
NNP -> 'Foster'
NNP -> 'Foundation'
NNP -> 'Fournier'
NNP -> 'Fox'
NNP -> 'France'
NNP -> 'Francisco'
NNP -> 'Frank'
NNP -> 'Frankfurt'
NNP -> 'Franklin'
NNP -> 'Freddie'
NNP -> 'Frederick'
NNP -> 'Free'
NNP -> 'Freeman'
NNP -> 'FreeportMcMoRan'
NNP -> 'French'
NNP -> 'Fresenius'
NNP -> 'Friday'
NNP -> 'Friedman'
NNP -> 'Friend'
NNP -> 'Fromstein'
NNP -> 'Fuji'
NNP -> 'Fujitsu'
NNP -> 'Fulton'
NNP -> 'Fund'
NNP -> 'Funding'
NNP -> 'Futures'
NNP -> 'Gpoint'
NNP -> 'Gpointmpointb'
NNP -> 'GAF'
NNP -> 'GE'
NNP -> 'GM'
NNP -> 'GMAC'
NNP -> 'GNP'
NNP -> 'GOP'
NNP -> 'GTE'
NNP -> 'Gapoint'
NNP -> 'Gabelli'
NNP -> 'Galileo'
NNP -> 'Gandhi'
NNP -> 'Garcia'
NNP -> 'Garratt'
NNP -> 'Gary'
NNP -> 'Gas'
NNP -> 'GenProbe'
NNP -> 'Genpoint'
NNP -> 'General'
NNP -> 'Generale'
NNP -> 'Genetics'
NNP -> 'Geneva'
NNP -> 'George'
NNP -> 'Georgia'
NNP -> 'GeorgiaPacific'
NNP -> 'Gerald'
NNP -> 'German'
NNP -> 'Germany'
NNP -> 'Giant'
NNP -> 'Giants'
NNP -> 'Ginnie'
NNP -> 'Giuliani'
NNP -> 'Glass'
NNP -> 'Glenn'
NNP -> 'Global'
NNP -> 'God'
NNP -> 'Gold'
NNP -> 'Goldberg'
NNP -> 'Golden'
NNP -> 'Goldman'
NNP -> 'Goldsmith'
NNP -> 'Gonzalez'
NNP -> 'Goodson'
NNP -> 'Gorbachev'
NNP -> 'Gould'
NNP -> 'Goupil'
NNP -> 'Govpoint'
NNP -> 'Government'
NNP -> 'GrammRudman'
NNP -> 'Grand'
NNP -> 'Graphics'
NNP -> 'Gray'
NNP -> 'Great'
NNP -> 'Greece'
NNP -> 'Green'
NNP -> 'Greenberg'
NNP -> 'Greenspan'
NNP -> 'Greenville'
NNP -> 'Greenwich'
NNP -> 'Gregory'
NNP -> 'Grenfell'
NNP -> 'Group'
NNP -> 'Grumman'
NNP -> 'Guard'
NNP -> 'Guber'
NNP -> 'Guinness'
NNP -> 'Gulf'
NNP -> 'Guzman'
NNP -> 'H&R'
NNP -> 'Hpoint'
NNP -> 'HBO'
NNP -> 'HUD'
NNP -> 'Hahn'
NNP -> 'Hall'
NNP -> 'Hammond'
NNP -> 'Hampshire'
NNP -> 'Hanover'
NNP -> 'Harold'
NNP -> 'Harris'
NNP -> 'Harry'
NNP -> 'Hartford'
NNP -> 'Harvard'
NNP -> 'Hastings'
NNP -> 'Hatch'
NNP -> 'Haven'
NNP -> 'Health'
NNP -> 'HealthVest'
NNP -> 'Hearst'
NNP -> 'Helmsley'
NNP -> 'Helmut'
NNP -> 'Henderson'
NNP -> 'Henry'
NNP -> 'Herald'
NNP -> 'Herbert'
NNP -> 'Heritage'
NNP -> 'Hertz'
NNP -> 'Hess'
NNP -> 'HewlettPackard'
NNP -> 'High'
NNP -> 'Hill'
NNP -> 'Hills'
NNP -> 'Hilton'
NNP -> 'Hiroshima'
NNP -> 'Hitachi'
NNP -> 'Hoechst'
NNP -> 'Hoffman'
NNP -> 'Holding'
NNP -> 'Holdings'
NNP -> 'Holiday'
NNP -> 'Hollander'
NNP -> 'Hollywood'
NNP -> 'Home'
NNP -> 'HomeFed'
NNP -> 'Honda'
NNP -> 'Honecker'
NNP -> 'Honeywell'
NNP -> 'Hong'
NNP -> 'Hooker'
NNP -> 'Hospital'
NNP -> 'House'
NNP -> 'HouseSenate'
NNP -> 'Housing'
NNP -> 'Houston'
NNP -> 'Howard'
NNP -> 'Hoylake'
NNP -> 'Hudson'
NNP -> 'Hughes'
NNP -> 'Hugo'
NNP -> 'Humana'
NNP -> 'Hungary'
NNP -> 'Hunt'
NNP -> 'Hunter'
NNP -> 'Hurricane'
NNP -> 'Hutchinson'
NNP -> 'Hutton'
NNP -> 'HydroQuebec'
NNP -> 'IBM'
NNP -> 'II'
NNP -> 'III'
NNP -> 'IMF'
NNP -> 'IRS'
NNP -> 'ISI'
NNP -> 'ITT'
NNP -> 'Icahn'
NNP -> 'Ill'
NNP -> 'Illpoint'
NNP -> 'Illinois'
NNP -> 'Illuminating'
NNP -> 'Imperial'
NNP -> 'Inc'
NNP -> 'Incpoint'
NNP -> 'Inco'
NNP -> 'Income'
NNP -> 'Indpoint'
NNP -> 'Independent'
NNP -> 'Index'
NNP -> 'India'
NNP -> 'Indianapolis'
NNP -> 'Individual'
NNP -> 'Industrial'
NNP -> 'Industries'
NNP -> 'Industry'
NNP -> 'Infiniti'
NNP -> 'Information'
NNP -> 'Ingersoll'
NNP -> 'Institute'
NNP -> 'Insurance'
NNP -> 'Integrated'
NNP -> 'Intel'
NNP -> 'Intelligence'
NNP -> 'Intelogic'
NNP -> 'Intergroup'
NNP -> 'Intermediate'
NNP -> 'Internal'
NNP -> 'International'
NNP -> 'Interpublic'
NNP -> 'Interstate'
NNP -> 'Investment'
NNP -> 'Investments'
NNP -> 'Investor'
NNP -> 'Investors'
NNP -> 'Iowa'
NNP -> 'Ira'
NNP -> 'Iran'
NNP -> 'IranContra'
NNP -> 'Ireland'
NNP -> 'Irving'
NNP -> 'Island'
NNP -> 'Israel'
NNP -> 'Italy'
NNP -> 'Iverson'
NNP -> 'Jpoint'
NNP -> 'JpointCpoint'
NNP -> 'Jack'
NNP -> 'Jackson'
NNP -> 'Jacobson'
NNP -> 'Jaguar'
NNP -> 'James'
NNP -> 'Janpoint'
NNP -> 'January'
NNP -> 'Japan'
NNP -> 'Japanese'
NNP -> 'Jay'
NNP -> 'Jefferies'
NNP -> 'Jeffrey'
NNP -> 'Jerry'
NNP -> 'Jersey'
NNP -> 'Jim'
NNP -> 'Joe'
NNP -> 'John'
NNP -> 'Johnson'
NNP -> 'Jonathan'
NNP -> 'Jones'
NNP -> 'Jose'
NNP -> 'Joseph'
NNP -> 'Journal'
NNP -> 'Jr'
NNP -> 'Jrpoint'
NNP -> 'Judge'
NNP -> 'Judiciary'
NNP -> 'July'
NNP -> 'June'
NNP -> 'Jupiter'
NNP -> 'Justice'
NNP -> 'Justin'
NNP -> 'Kpoint'
NNP -> 'KKR'
NNP -> 'Kabul'
NNP -> 'Kaiser'
NNP -> 'Kangyo'
NNP -> 'Kansas'
NNP -> 'Kao'
NNP -> 'Kasparov'
NNP -> 'Katz'
NNP -> 'Kaye'
NNP -> 'Kean'
NNP -> 'Keating'
NNP -> 'Kellogg'
NNP -> 'Kemper'
NNP -> 'Kennedy'
NNP -> 'Kenneth'
NNP -> 'Kent'
NNP -> 'Kentucky'
NNP -> 'Khmer'
NNP -> 'Kidder'
NNP -> 'KinderCare'
NNP -> 'King'
NNP -> 'Kingdom'
NNP -> 'Kleinwort'
NNP -> 'KnightRidder'
NNP -> 'Kodak'
NNP -> 'Kohl'
NNP -> 'Kong'
NNP -> 'Korea'
NNP -> 'Korotich'
NNP -> 'Kraft'
NNP -> 'Krasnoyarsk'
NNP -> 'Kremlin'
NNP -> 'Krenz'
NNP -> 'Kuala'
NNP -> 'Kume'
NNP -> 'Kypoint'
NNP -> 'Lpoint'
NNP -> 'LpointJpoint'
NNP -> 'LDP'
NNP -> 'LTV'
NNP -> 'La'
NNP -> 'Laband'
NNP -> 'Labor'
NNP -> 'Laff'
NNP -> 'Lake'
NNP -> 'Lambert'
NNP -> 'Land'
NNP -> 'Lane'
NNP -> 'Lang'
NNP -> 'Lantos'
NNP -> 'Larry'
NNP -> 'Las'
NNP -> 'Latin'
NNP -> 'Laurel'
NNP -> 'Law'
NNP -> 'Lawrence'
NNP -> 'Lawson'
NNP -> 'Leader'
NNP -> 'League'
NNP -> 'Learning'
NNP -> 'Lebanon'
NNP -> 'Lee'
NNP -> 'Legal'
NNP -> 'Lehman'
NNP -> 'LeighPemberton'
NNP -> 'Leipzig'
NNP -> 'Leonard'
NNP -> 'Lesko'
NNP -> 'Levine'
NNP -> 'Levy'
NNP -> 'Lewis'
NNP -> 'Lexington'
NNP -> 'Lexus'
NNP -> 'Libor'
NNP -> 'Libya'
NNP -> 'Life'
NNP -> 'Lilly'
NNP -> 'Limited'
NNP -> 'Lin'
NNP -> 'Lincoln'
NNP -> 'Line'
NNP -> 'Lines'
NNP -> 'Lipper'
NNP -> 'Litigation'
NNP -> 'Little'
NNP -> 'Lloyd'
NNP -> 'Loan'
NNP -> 'Lockheed'
NNP -> 'London'
NNP -> 'Lone'
NNP -> 'Loral'
NNP -> 'Lorenzo'
NNP -> 'Lorin'
NNP -> 'Los'
NNP -> 'Lotus'
NNP -> 'Louis'
NNP -> 'Louisville'
NNP -> 'Ltd'
NNP -> 'Ltdpoint'
NNP -> 'Lumpur'
NNP -> 'Luzon'
NNP -> 'Lynch'
NNP -> 'Lynn'
NNP -> 'Mpoint'
NNP -> 'MCA'
NNP -> 'MCI'
NNP -> 'MGM'
NNP -> 'MGM:slash:UA'
NNP -> 'MTM'
NNP -> 'Mac'
NNP -> 'Machines'
NNP -> 'Mack'
NNP -> 'Macmillan'
NNP -> 'Madison'
NNP -> 'Mae'
NNP -> 'Magazine'
NNP -> 'Maidenform'
NNP -> 'Maine'
NNP -> 'Major'
NNP -> 'Majority'
NNP -> 'Malaysia'
NNP -> 'Malcolm'
NNP -> 'Management'
NNP -> 'Mancuso'
NNP -> 'Manhattan'
NNP -> 'Manuel'
NNP -> 'Manufacturers'
NNP -> 'Manufacturing'
NNP -> 'Manville'
NNP -> 'March'
NNP -> 'Marcos'
NNP -> 'Marina'
NNP -> 'Marine'
NNP -> 'Mario'
NNP -> 'Mark'
NNP -> 'Market'
NNP -> 'Marketing'
NNP -> 'Markets'
NNP -> 'Markey'
NNP -> 'Marlin'
NNP -> 'Marshall'
NNP -> 'Martin'
NNP -> 'Marvin'
NNP -> 'Mary'
NNP -> 'Maryland'
NNP -> 'Mason'
NNP -> 'Mass'
NNP -> 'Masspoint'
NNP -> 'Massachusetts'
NNP -> 'Matra'
NNP -> 'Max'
NNP -> 'Maxwell'
NNP -> 'May'
NNP -> 'Maynard'
NNP -> 'Mayor'
NNP -> 'McCaw'
NNP -> 'McDonald'
NNP -> 'McDonough'
NNP -> 'McDuffie'
NNP -> 'McGovern'
NNP -> 'McGrawHill'
NNP -> 'McNamee'
NNP -> 'Mdpoint'
NNP -> 'MedChem'
NNP -> 'Media'
NNP -> 'Medical'
NNP -> 'Medicare'
NNP -> 'Medicine'
NNP -> 'Mehl'
NNP -> 'Mellon'
NNP -> 'Menlo'
NNP -> 'Merc'
NNP -> 'Mercantile'
NNP -> 'Meredith'
NNP -> 'Meridian'
NNP -> 'Merieux'
NNP -> 'Merksamer'
NNP -> 'Merkur'
NNP -> 'Merrill'
NNP -> 'Mesa'
NNP -> 'Metromedia'
NNP -> 'Metropolitan'
NNP -> 'Mexico'
NNP -> 'Miami'
NNP -> 'Michpoint'
NNP -> 'Michael'
NNP -> 'Michigan'
NNP -> 'Microsoft'
NNP -> 'Middle'
NNP -> 'Midland'
NNP -> 'Midwest'
NNP -> 'Mike'
NNP -> 'Mikhail'
NNP -> 'Milan'
NNP -> 'Miller'
NNP -> 'Mills'
NNP -> 'Milton'
NNP -> 'Milunovich'
NNP -> 'Minister'
NNP -> 'Ministry'
NNP -> 'Minnpoint'
NNP -> 'Minneapolis'
NNP -> 'Minnesota'
NNP -> 'Minpeco'
NNP -> 'Mips'
NNP -> 'Miss'
NNP -> 'Mississippi'
NNP -> 'Missouri'
NNP -> 'Mitchell'
NNP -> 'Mitsubishi'
NNP -> 'Mitsui'
NNP -> 'Mixte'
NNP -> 'Mobil'
NNP -> 'Monday'
NNP -> 'Money'
NNP -> 'Montedison'
NNP -> 'Montgomery'
NNP -> 'Montreal'
NNP -> 'Moody'
NNP -> 'Moon'
NNP -> 'Moore'
NNP -> 'Morgan'
NNP -> 'Morishita'
NNP -> 'Morris'
NNP -> 'Mortgage'
NNP -> 'Mosbacher'
NNP -> 'Moscow'
NNP -> 'Motor'
NNP -> 'Motorola'
NNP -> 'Motors'
NNP -> 'Mrpoint'
NNP -> 'Mrspoint'
NNP -> 'Mspoint'
NNP -> 'Mullins'
NNP -> 'Municipal'
NNP -> 'Murdoch'
NNP -> 'Murray'
NNP -> 'NpointC'
NNP -> 'NpointCpoint'
NNP -> 'NpointJ'
NNP -> 'NpointJpoint'
NNP -> 'NpointVpoint'
NNP -> 'NpointY'
NNP -> 'NpointYpoint'
NNP -> 'NAHB'
NNP -> 'NASA'
NNP -> 'NATO'
NNP -> 'NBC'
NNP -> 'NCNB'
NNP -> 'NEC'
NNP -> 'NFL'
NNP -> 'NIH'
NNP -> 'NL'
NNP -> 'NRM'
NNP -> 'NYSE'
NNP -> 'Nabisco'
NNP -> 'Nadeau'
NNP -> 'Namibia'
NNP -> 'Nasdaq'
NNP -> 'Nashua'
NNP -> 'National'
NNP -> 'Navigation'
NNP -> 'Navy'
NNP -> 'Neal'
NNP -> 'Nebpoint'
NNP -> 'Needham'
NNP -> 'Neil'
NNP -> 'Nekoosa'
NNP -> 'Nelson'
NNP -> 'Nestle'
NNP -> 'Netherlands'
NNP -> 'Network'
NNP -> 'New'
NNP -> 'Newport'
NNP -> 'News'
NNP -> 'Newsweek'
NNP -> 'Next'
NNP -> 'Nicaragua'
NNP -> 'Nicholas'
NNP -> 'Nielsen'
NNP -> 'Nigel'
NNP -> 'Nikkei'
NNP -> 'Nippon'
NNP -> 'Nissan'
NNP -> 'Nixon'
NNP -> 'Nobel'
NNP -> 'Nomura'
NNP -> 'Norfolk'
NNP -> 'Noriega'
NNP -> 'Norman'
NNP -> 'North'
NNP -> 'Northeast'
NNP -> 'Northern'
NNP -> 'Northwest'
NNP -> 'Novpoint'
NNP -> 'November'
NNP -> 'Nuovo'
NNP -> 'Nynex'
NNP -> "O'Brien"
NNP -> "O'Kicki"
NNP -> 'Opoint'
NNP -> 'OPEC'
NNP -> 'OTC'
NNP -> 'Oakland'
NNP -> 'Octpoint'
NNP -> 'Octel'
NNP -> 'October'
NNP -> 'Odeon'
NNP -> 'Office'
NNP -> 'Ogilvy'
NNP -> 'Ohio'
NNP -> 'Oil'
NNP -> 'Oklapoint'
NNP -> 'Oklahoma'
NNP -> 'Old'
NNP -> 'Oliver'
NNP -> 'Olivetti'
NNP -> 'Omni'
NNP -> 'Options'
NNP -> 'Orange'
NNP -> 'Order'
NNP -> 'Orepoint'
NNP -> 'Oregon'
NNP -> 'Organization'
NNP -> 'Orkem'
NNP -> 'Orleans'
NNP -> 'Ortega'
NNP -> 'Otto'
NNP -> 'Owen'
NNP -> 'P&G'
NNP -> 'Ppoint'
NNP -> 'PASOK'
NNP -> 'PLC'
NNP -> 'PLO'
NNP -> 'PS'
NNP -> 'Papoint'
NNP -> 'Pace'
NNP -> 'Pacific'
NNP -> 'Packwood'
NNP -> 'PackwoodRoth'
NNP -> 'PaineWebber'
NNP -> 'Palo'
NNP -> 'Pan'
NNP -> 'Panama'
NNP -> 'Paper'
NNP -> 'Paramount'
NNP -> 'Paribas'
NNP -> 'Paris'
NNP -> 'Park'
NNP -> 'Parker'
NNP -> 'Parks'
NNP -> 'Parliament'
NNP -> 'Part'
NNP -> 'Partners'
NNP -> 'Partnership'
NNP -> 'Party'
NNP -> 'Pat'
NNP -> 'Patrick'
NNP -> 'Patterson'
NNP -> 'Paul'
NNP -> 'Peabody'
NNP -> 'Peck'
NNP -> 'Peladeau'
NNP -> 'Pemex'
NNP -> 'Penney'
NNP -> 'Pennsylvania'
NNP -> 'Pennzoil'
NNP -> 'Pentagon'
NNP -> 'Perspective'
NNP -> 'Peter'
NNP -> 'Peters'
NNP -> 'Peterson'
NNP -> 'Petrie'
NNP -> 'Petroleum'
NNP -> 'Peugeot'
NNP -> 'Pfizer'
NNP -> 'Pharmaceutical'
NNP -> 'Pharmacia'
NNP -> 'Phelan'
NNP -> 'Philadelphia'
NNP -> 'Philip'
NNP -> 'Phillips'
NNP -> 'Phoenix'
NNP -> 'Pickens'
NNP -> 'Picop'
NNP -> 'Pictures'
NNP -> 'Pilson'
NNP -> 'Pinkerton'
NNP -> 'Pinnacle'
NNP -> 'Pioneer'
NNP -> 'Pittsburgh'
NNP -> 'Pizza'
NNP -> 'Plan'
NNP -> 'Plant'
NNP -> 'Plaza'
NNP -> 'Poland'
NNP -> 'Polaroid'
NNP -> 'Policy'
NNP -> 'Politburo'
NNP -> 'Polly'
NNP -> 'Pont'
NNP -> 'Portfolio'
NNP -> 'Posner'
NNP -> 'Postal'
NNP -> 'Power'
NNP -> 'Prebon'
NNP -> 'President'
NNP -> 'Press'
NNP -> 'Price'
NNP -> 'Prime'
NNP -> 'Prince'
NNP -> 'Profpoint'
NNP -> 'Professional'
NNP -> 'Program'
NNP -> 'Protection'
NNP -> 'Prudential'
NNP -> 'PrudentialBache'
NNP -> 'Public'
NNP -> 'Publishing'
NNP -> 'Puerto'
NNP -> 'Qintex'
NNP -> 'Quantum'
NNP -> 'Quayle'
NNP -> 'Quebecor'
NNP -> 'Quotron'
NNP -> 'Rpoint'
NNP -> 'RJR'
NNP -> 'RTC'
NNP -> 'RU486'
NNP -> 'Radio'
NNP -> 'Rally'
NNP -> 'Ralph'
NNP -> 'Ratners'
NNP -> 'Raymond'
NNP -> 'Reagan'
NNP -> 'Realty'
NNP -> 'Recognition'
NNP -> 'Red'
NNP -> 'Redford'
NNP -> 'Reebok'
NNP -> 'Reed'
NNP -> 'Regulatory'
NNP -> 'Reinvestment'
NNP -> 'Reliance'
NNP -> 'Remic'
NNP -> 'Renaissance'
NNP -> 'Reppoint'
NNP -> 'Report'
NNP -> 'Republic'
NNP -> 'Republican'
NNP -> 'Research'
NNP -> 'Reserve'
NNP -> 'Resolution'
NNP -> 'Resources'
NNP -> 'Reuters'
NNP -> 'Revpoint'
NNP -> 'Revco'
NNP -> 'Revenue'
NNP -> 'Review'
NNP -> 'Rey'
NNP -> 'Reynolds'
NNP -> 'Rica'
NNP -> 'Rich'
NNP -> 'Richard'
NNP -> 'Richmond'
NNP -> 'Richter'
NNP -> 'Rick'
NNP -> 'Rico'
NNP -> 'Ridley'
NNP -> 'Right'
NNP -> 'Rights'
NNP -> 'River'
NNP -> 'Robert'
NNP -> 'Roberts'
NNP -> 'Robertson'
NNP -> 'Robins'
NNP -> 'Rochester'
NNP -> 'Rock'
NNP -> 'Rockefeller'
NNP -> 'Rockwell'
NNP -> 'Roderick'
NNP -> 'Roe'
NNP -> 'Roger'
NNP -> 'Rogers'
NNP -> 'Roh'
NNP -> 'Roman'
NNP -> 'Ron'
NNP -> 'Ronald'
NNP -> 'Rose'
NNP -> 'Rosen'
NNP -> 'Ross'
NNP -> 'Rouge'
NNP -> 'Rowe'
NNP -> 'Roy'
NNP -> 'Royal'
NNP -> 'Rubens'
NNP -> 'Runkel'
NNP -> 'Russell'
NNP -> 'Ruth'
NNP -> 'Ryder'
NNP -> 'S&L'
NNP -> 'S&P'
NNP -> 'Spoint'
NNP -> 'SpointApoint'
NNP -> 'Spointp'
NNP -> 'SCI'
NNP -> 'SEC'
NNP -> 'Saab'
NNP -> 'SaabScania'
NNP -> 'Saatchi'
NNP -> 'Sachs'
NNP -> 'Sacramento'
NNP -> 'Salinas'
NNP -> 'Salinger'
NNP -> 'Salomon'
NNP -> 'Salvador'
NNP -> 'Sam'
NNP -> 'Samuel'
NNP -> 'San'
NNP -> 'Sanford'
NNP -> 'Sansui'
NNP -> 'Santa'
NNP -> 'Satellite'
NNP -> 'Saturday'
NNP -> 'Saudi'
NNP -> 'Savaiko'
NNP -> 'Savings'
NNP -> 'Schaeffer'
NNP -> 'ScheringPlough'
NNP -> 'School'
NNP -> 'Schwab'
NNP -> 'Schwartz'
NNP -> 'Schwarz'
NNP -> 'Scott'
NNP -> 'Sea'
NNP -> 'Seagate'
NNP -> 'Sears'
NNP -> 'Seattle'
NNP -> 'Secretary'
NNP -> 'Section'
NNP -> 'Securities'
NNP -> 'Security'
NNP -> 'Seidman'
NNP -> 'Senpoint'
NNP -> 'Senate'
NNP -> 'Senator'
NNP -> 'Seoul'
NNP -> 'Septpoint'
NNP -> 'September'
NNP -> 'Series'
NNP -> 'Service'
NNP -> 'Services'
NNP -> 'Shack'
NNP -> 'Shannon'
NNP -> 'Shaw'
NNP -> 'Shearson'
NNP -> 'Sherman'
NNP -> 'Shevardnadze'
NNP -> 'Show'
NNP -> 'Showtime'
NNP -> 'Sierra'
NNP -> 'Silicon'
NNP -> 'Sim'
NNP -> 'Simmons'
NNP -> 'Simon'
NNP -> 'Singapore'
NNP -> 'Sinyard'
NNP -> 'Sir'
NNP -> 'Sisulu'
NNP -> 'Skase'
NNP -> 'Skinner'
NNP -> 'Sloan'
NNP -> 'Smith'
NNP -> 'SmithKline'
NNP -> 'Social'
NNP -> 'Socialist'
NNP -> 'Societe'
NNP -> 'Society'
NNP -> 'Solidarity'
NNP -> 'Sony'
NNP -> 'Soo'
NNP -> 'Sotheby'
NNP -> 'Soup'
NNP -> 'South'
NNP -> 'Southam'
NNP -> 'Southeast'
NNP -> 'Southern'
NNP -> 'Soviet'
NNP -> 'Spain'
NNP -> 'Speaker'
NNP -> 'Specialized'
NNP -> 'Sperry'
NNP -> 'Spiegel'
NNP -> 'Spielvogel'
NNP -> 'Springs'
NNP -> 'Squibb'
NNP -> 'Stpoint'
NNP -> 'Stamford'
NNP -> 'Stanford'
NNP -> 'Stanley'
NNP -> 'Star'
NNP -> 'State'
NNP -> 'States'
NNP -> 'StatesWest'
NNP -> 'Stateswest'
NNP -> 'Statistics'
NNP -> 'Stearns'
NNP -> 'Steel'
NNP -> 'Stein'
NNP -> 'Steinberg'
NNP -> 'Steinhardt'
NNP -> 'Stephen'
NNP -> 'Sterling'
NNP -> 'Steve'
NNP -> 'Steven'
NNP -> 'Stevens'
NNP -> 'Stewart'
NNP -> 'Stock'
NNP -> 'Stoll'
NNP -> 'Stone'
NNP -> 'Store'
NNP -> 'Straszheim'
NNP -> 'Street'
NNP -> 'Suisse'
NNP -> 'Sullivan'
NNP -> 'Sun'
NNP -> 'Sunday'
NNP -> 'Superfund'
NNP -> 'Supervision'
NNP -> 'Supreme'
NNP -> 'Susan'
NNP -> 'Sweden'
NNP -> 'Swedish'
NNP -> 'Sweig'
NNP -> 'Switzerland'
NNP -> 'Sydney'
NNP -> 'System'
NNP -> 'Systems'
NNP -> 'Tpoint'
NNP -> 'TVA'
NNP -> 'TVS'
NNP -> 'TW'
NNP -> 'Taipei'
NNP -> 'Taiwan'
NNP -> 'Tandy'
NNP -> 'Task'
NNP -> 'Tax'
NNP -> 'Taylor'
NNP -> 'Technologies'
NNP -> 'Technology'
NNP -> 'Ted'
NNP -> 'Teddy'
NNP -> 'TeleCommunications'
NNP -> 'Telecommunications'
NNP -> 'Telephone'
NNP -> 'Telerate'
NNP -> 'Telesis'
NNP -> 'Temple'
NNP -> 'Tennpoint'
NNP -> 'Tenneco'
NNP -> 'Tennessee'
NNP -> 'Terry'
NNP -> 'Tesoro'
NNP -> 'Texaco'
NNP -> 'Texas'
NNP -> 'Thatcher'
NNP -> 'The'
NNP -> 'Theater'
NNP -> 'Thi'
NNP -> 'Third'
NNP -> 'Thomas'
NNP -> 'Thompson'
NNP -> 'Thomson'
NNP -> 'Three'
NNP -> 'Thrift'
NNP -> 'Thurmond'
NNP -> 'Thursday'
NNP -> 'Tiger'
NNP -> 'Timbers'
NNP -> 'Time'
NNP -> 'Times'
NNP -> 'TimesStock'
NNP -> 'Timothy'
NNP -> 'Today'
NNP -> 'Tokyo'
NNP -> 'Tokyu'
NNP -> 'Tom'
NNP -> 'Tony'
NNP -> 'Toronto'
NNP -> 'Torrijos'
NNP -> 'Toseland'
NNP -> 'Toshiba'
NNP -> 'Tower'
NNP -> 'Toyota'
NNP -> 'Trade'
NNP -> 'Trading'
NNP -> 'Trans'
NNP -> 'TransCanada'
NNP -> 'Transportation'
NNP -> 'Travel'
NNP -> 'Treasury'
NNP -> 'Treaty'
NNP -> 'Trelleborg'
NNP -> 'Trinity'
NNP -> 'Trump'
NNP -> 'Trust'
NNP -> 'Tucson'
NNP -> 'Tuesday'
NNP -> 'Tulsa'
NNP -> 'Turkey'
NNP -> 'Turner'
NNP -> 'Turnpike'
NNP -> 'UpointKpoint'
NNP -> 'UpointNpoint'
NNP -> 'UpointSpoint'
NNP -> 'UpointSpointA'
NNP -> 'UpointSpointApoint'
NNP -> 'UpointSpointSpointRpoint'
NNP -> 'UAL'
NNP -> 'UAW'
NNP -> 'UNESCO'
NNP -> 'USA'
NNP -> 'USAir'
NNP -> 'USX'
NNP -> 'Unilever'
NNP -> 'Union'
NNP -> 'Unisys'
NNP -> 'United'
NNP -> 'University'
NNP -> 'Unix'
NNP -> 'Upjohn'
NNP -> 'Urban'
NNP -> 'Utah'
NNP -> 'Utsumi'
NNP -> 'Va'
NNP -> 'Vapoint'
NNP -> 'Valley'
NNP -> 'Value'
NNP -> 'Van'
NNP -> 'Vancouver'
NNP -> 'Vax'
NNP -> 'Vegas'
NNP -> 'Venice'
NNP -> 'Vermont'
NNP -> 'Viacom'
NNP -> 'Vice'
NNP -> 'Victor'
NNP -> 'Vietnam'
NNP -> 'View'
NNP -> 'Vila'
NNP -> 'Vincent'
NNP -> 'Virginia'
NNP -> 'Volokh'
NNP -> 'Wpoint'
NNP -> 'WCRS'
NNP -> 'WPP'
NNP -> 'WSJ'
NNP -> 'Wade'
NNP -> 'Waertsilae'
NNP -> 'Wall'
NNP -> 'Walter'
NNP -> 'Wang'
NNP -> 'War'
NNP -> 'Ward'
NNP -> 'Warner'
NNP -> 'Warren'
NNP -> 'Warsaw'
NNP -> 'Washpoint'
NNP -> 'Washington'
NNP -> 'Wathen'
NNP -> 'Wayne'
NNP -> 'Webster'
NNP -> 'Wednesday'
NNP -> 'Wedtech'
NNP -> 'Weisfield'
NNP -> 'Weisman'
NNP -> 'Weiss'
NNP -> 'Wells'
NNP -> 'West'
NNP -> 'Western'
NNP -> 'Westinghouse'
NNP -> 'Westmoreland'
NNP -> 'Whitbread'
NNP -> 'White'
NNP -> 'Whittle'
NNP -> 'William'
NNP -> 'Williams'
NNP -> 'Wilson'
NNP -> 'Windsor'
NNP -> 'Wisconsin'
NNP -> 'Witter'
NNP -> 'Wolf'
NNP -> 'World'
NNP -> 'Wright'
NNP -> 'Wyss'
NNP -> 'Xerox'
NNP -> 'Yale'
NNP -> 'Yamaichi'
NNP -> 'Yeargin'
NNP -> 'York'
NNP -> 'Young'
NNP -> 'Zealand'
NNP -> 'a'
NNP -> 'aids'
NNP -> 'apple'
NNP -> 'assets'
NNP -> 'association'
NNP -> 'b'
NNP -> 'baker'
NNP -> 'bank'
NNP -> 'bell'
NNP -> 'big'
NNP -> 'blockbuster'
NNP -> 'c'
NNP -> 'carnival'
NNP -> 'chairman'
NNP -> 'chase'
NNP -> 'chicago'
NNP -> 'china'
NNP -> 'coke'
NNP -> 'commercial'
NNP -> 'computer'
NNP -> 'congress'
NNP -> 'continental'
NNP -> 'control'
NNP -> 'de'
NNP -> 'des'
NNP -> 'dig'
NNP -> 'digital'
NNP -> 'du'
NNP -> 'east'
NNP -> 'eastern'
NNP -> 'energy'
NNP -> 'fed'
NNP -> 'federal'
NNP -> 'first'
NNP -> 'foreign'
NNP -> 'frank'
NNP -> 'general'
NNP -> 'giant'
NNP -> 'government'
NNP -> 'great'
NNP -> 'gulf'
NNP -> 'home'
NNP -> 'house'
NNP -> 'integrated'
NNP -> 'interbank'
NNP -> 'international'
NNP -> 'judge'
NNP -> 'k'
NNP -> 'loan'
NNP -> 'mart'
NNP -> 'midOctober'
NNP -> 'money'
NNP -> 'mortgage'
NNP -> 'national'
NNP -> 'new'
NNP -> 'northeast'
NNP -> 'paper'
NNP -> 'pop'
NNP -> 'president'
NNP -> 'prime'
NNP -> 'quantum'
NNP -> 'rally'
NNP -> 'rate'
NNP -> 'ready'
NNP -> 'royal'
NNP -> 'secretary'
NNP -> 'security'
NNP -> 'senate'
NNP -> 'senator'
NNP -> 'separately'
NNP -> 'silicon'
NNP -> 'south'
NNP -> 'sun'
NNP -> 'time'
NNP -> 'treasury'
NNP -> 'trust'
NNP -> 'tv'
NNP -> 'union'
NNP -> 'united'
NNP -> 'us'
NNP -> 'valley'
NNP -> 'van'
NNP -> 'wall'
NNP -> 'west'
NNP -> 'white'
SBARPRP -> S
SBARPRP -> IN S
VBN -> 'Asked'
VBN -> 'Given'
VBN -> 'Guaranteed'
VBN -> 'Posted'
VBN -> 'abandoned'
VBN -> 'accepted'
VBN -> 'accompanied'
VBN -> 'accrued'
VBN -> 'accused'
VBN -> 'achieved'
VBN -> 'acquired'
VBN -> 'adapted'
VBN -> 'added'
VBN -> 'adjusted'
VBN -> 'admitted'
VBN -> 'adopted'
VBN -> 'advanced'
VBN -> 'advised'
VBN -> 'affected'
VBN -> 'aged'
VBN -> 'agreed'
VBN -> 'aimed'
VBN -> 'alleged'
VBN -> 'allowed'
VBN -> 'amended'
VBN -> 'announced'
VBN -> 'annualized'
VBN -> 'anticipated'
VBN -> 'applied'
VBN -> 'appointed'
VBN -> 'approached'
VBN -> 'approved'
VBN -> 'argued'
VBN -> 'arrested'
VBN -> 'arrived'
VBN -> 'asked'
VBN -> 'assigned'
VBN -> 'associated'
VBN -> 'assumed'
VBN -> 'assured'
VBN -> 'attached'
VBN -> 'attributed'
VBN -> 'authorized'
VBN -> 'avoided'
VBN -> 'awarded'
VBN -> 'backed'
VBN -> 'barred'
VBN -> 'based'
VBN -> 'become'
VBN -> 'been'
VBN -> 'begun'
VBN -> 'believed'
VBN -> 'benefited'
VBN -> 'bid'
VBN -> 'blamed'
VBN -> 'bolstered'
VBN -> 'boosted'
VBN -> 'born'
VBN -> 'borrowed'
VBN -> 'bought'
VBN -> 'bound'
VBN -> 'broken'
VBN -> 'brought'
VBN -> 'built'
VBN -> 'buoyed'
VBN -> 'calculated'
VBN -> 'called'
VBN -> 'canceled'
VBN -> 'capitalized'
VBN -> 'capped'
VBN -> 'captured'
VBN -> 'carried'
VBN -> 'caught'
VBN -> 'caused'
VBN -> 'challenged'
VBN -> 'changed'
VBN -> 'charged'
VBN -> 'chosen'
VBN -> 'cited'
VBN -> 'claimed'
VBN -> 'closed'
VBN -> 'collapsed'
VBN -> 'combined'
VBN -> 'come'
VBN -> 'committed'
VBN -> 'compared'
VBN -> 'complained'
VBN -> 'completed'
VBN -> 'complicated'
VBN -> 'concerned'
VBN -> 'concluded'
VBN -> 'conducted'
VBN -> 'confirmed'
VBN -> 'connected'
VBN -> 'considered'
VBN -> 'continued'
VBN -> 'contributed'
VBN -> 'controlled'
VBN -> 'converted'
VBN -> 'convicted'
VBN -> 'convinced'
VBN -> 'cost'
VBN -> 'counted'
VBN -> 'coupled'
VBN -> 'covered'
VBN -> 'created'
VBN -> 'criticized'
VBN -> 'cut'
VBN -> 'damaged'
VBN -> 'dated'
VBN -> 'decided'
VBN -> 'declined'
VBN -> 'defined'
VBN -> 'delayed'
VBN -> 'delivered'
VBN -> 'denied'
VBN -> 'depressed'
VBN -> 'described'
VBN -> 'designed'
VBN -> 'determined'
VBN -> 'developed'
VBN -> 'devoted'
VBN -> 'died'
VBN -> 'diluted'
VBN -> 'diminished'
VBN -> 'disappointed'
VBN -> 'disclosed'
VBN -> 'discontinued'
VBN -> 'discounted'
VBN -> 'discovered'
VBN -> 'discussed'
VBN -> 'distributed'
VBN -> 'divided'
VBN -> 'dominated'
VBN -> 'donated'
VBN -> 'done'
VBN -> 'doubled'
VBN -> 'drawn'
VBN -> 'driven'
VBN -> 'dropped'
VBN -> 'dubbed'
VBN -> 'earned'
VBN -> 'elected'
VBN -> 'eliminated'
VBN -> 'employed'
VBN -> 'enacted'
VBN -> 'encouraged'
VBN -> 'ended'
VBN -> 'engaged'
VBN -> 'engineered'
VBN -> 'enhanced'
VBN -> 'entered'
VBN -> 'entitled'
VBN -> 'established'
VBN -> 'estimated'
VBN -> 'exercised'
VBN -> 'expanded'
VBN -> 'expected'
VBN -> 'experienced'
VBN -> 'exposed'
VBN -> 'expressed'
VBN -> 'extended'
VBN -> 'faced'
VBN -> 'failed'
VBN -> 'fallen'
VBN -> 'fed'
VBN -> 'felt'
VBN -> 'filed'
VBN -> 'filled'
VBN -> 'financed'
VBN -> 'finished'
VBN -> 'fired'
VBN -> 'fixed'
VBN -> 'focused'
VBN -> 'followed'
VBN -> 'forced'
VBN -> 'forecast'
VBN -> 'formed'
VBN -> 'found'
VBN -> 'fueled'
VBN -> 'funded'
VBN -> 'gained'
VBN -> 'generated'
VBN -> 'given'
VBN -> 'gone'
VBN -> 'got'
VBN -> 'gotten'
VBN -> 'grown'
VBN -> 'guaranteed'
VBN -> 'had'
VBN -> 'halted'
VBN -> 'hampered'
VBN -> 'handed'
VBN -> 'handled'
VBN -> 'happened'
VBN -> 'headed'
VBN -> 'heard'
VBN -> 'held'
VBN -> 'helped'
VBN -> 'hidden'
VBN -> 'hired'
VBN -> 'hit'
VBN -> 'hoped'
VBN -> 'hurt'
VBN -> 'identified'
VBN -> 'ignored'
VBN -> 'imported'
VBN -> 'imposed'
VBN -> 'improved'
VBN -> 'included'
VBN -> 'increased'
VBN -> 'incurred'
VBN -> 'indicated'
VBN -> 'initiated'
VBN -> 'injured'
VBN -> 'installed'
VBN -> 'insured'
VBN -> 'integrated'
VBN -> 'intended'
VBN -> 'interpreted'
VBN -> 'interviewed'
VBN -> 'introduced'
VBN -> 'invested'
VBN -> 'invited'
VBN -> 'involved'
VBN -> 'issued'
VBN -> 'justified'
VBN -> 'kept'
VBN -> 'killed'
VBN -> 'known'
VBN -> 'labeled'
VBN -> 'launched'
VBN -> 'learned'
VBN -> 'led'
VBN -> 'left'
VBN -> 'leveraged'
VBN -> 'lifted'
VBN -> 'limited'
VBN -> 'linked'
VBN -> 'liquidated'
VBN -> 'listed'
VBN -> 'located'
VBN -> 'locked'
VBN -> 'looked'
VBN -> 'lost'
VBN -> 'made'
VBN -> 'managed'
VBN -> 'manufactured'
VBN -> 'matched'
VBN -> 'meant'
VBN -> 'measured'
VBN -> 'mentioned'
VBN -> 'met'
VBN -> 'misstated'
VBN -> 'mixed'
VBN -> 'moved'
VBN -> 'named'
VBN -> 'narrowed'
VBN -> 'needed'
VBN -> 'negotiated'
VBN -> 'noted'
VBN -> 'notified'
VBN -> 'obtained'
VBN -> 'offered'
VBN -> 'offset'
VBN -> 'opened'
VBN -> 'opposed'
VBN -> 'ordered'
VBN -> 'organized'
VBN -> 'ousted'
VBN -> 'owed'
VBN -> 'owned'
VBN -> 'paid'
VBN -> 'painted'
VBN -> 'passed'
VBN -> 'performed'
VBN -> 'permitted'
VBN -> 'phased'
VBN -> 'placed'
VBN -> 'planned'
VBN -> 'played'
VBN -> 'pleased'
VBN -> 'plummeted'
VBN -> 'polled'
VBN -> 'posted'
VBN -> 'predicted'
VBN -> 'preferred'
VBN -> 'prepared'
VBN -> 'presented'
VBN -> 'prevented'
VBN -> 'priced'
VBN -> 'printed'
VBN -> 'processed'
VBN -> 'produced'
VBN -> 'projected'
VBN -> 'promised'
VBN -> 'prompted'
VBN -> 'proposed'
VBN -> 'protected'
VBN -> 'proved'
VBN -> 'provided'
VBN -> 'publicized'
VBN -> 'published'
VBN -> 'pulled'
VBN -> 'purchased'
VBN -> 'pushed'
VBN -> 'put'
VBN -> 'quoted'
VBN -> 'raised'
VBN -> 'rated'
VBN -> 'reached'
VBN -> 'read'
VBN -> 'received'
VBN -> 'recognized'
VBN -> 'recommended'
VBN -> 'recorded'
VBN -> 'redeemed'
VBN -> 'reduced'
VBN -> 'reflected'
VBN -> 'refused'
VBN -> 'regarded'
VBN -> 'registered'
VBN -> 'rejected'
VBN -> 'related'
VBN -> 'released'
VBN -> 'relieved'
VBN -> 'remained'
VBN -> 'renewed'
VBN -> 'repaid'
VBN -> 'repeated'
VBN -> 'replaced'
VBN -> 'reported'
VBN -> 'represented'
VBN -> 'requested'
VBN -> 'required'
VBN -> 'resolved'
VBN -> 'restated'
VBN -> 'restored'
VBN -> 'restricted'
VBN -> 'restructured'
VBN -> 'resulted'
VBN -> 'retained'
VBN -> 'retired'
VBN -> 'returned'
VBN -> 'revised'
VBN -> 'revived'
VBN -> 'risen'
VBN -> 'rolled'
VBN -> 'ruled'
VBN -> 'rumored'
VBN -> 'run'
VBN -> 'said'
VBN -> 'scheduled'
VBN -> 'secured'
VBN -> 'seen'
VBN -> 'selected'
VBN -> 'sent'
VBN -> 'sentenced'
VBN -> 'served'
VBN -> 'set'
VBN -> 'settled'
VBN -> 'shared'
VBN -> 'shipped'
VBN -> 'shown'
VBN -> 'shut'
VBN -> 'signed'
VBN -> 'slated'
VBN -> 'slowed'
VBN -> 'soared'
VBN -> 'sold'
VBN -> 'sought'
VBN -> 'specified'
VBN -> 'spent'
VBN -> 'spoken'
VBN -> 'spooked'
VBN -> 'spread'
VBN -> 'spun'
VBN -> 'squeezed'
VBN -> 'stalled'
VBN -> 'started'
VBN -> 'stated'
VBN -> 'stolen'
VBN -> 'stopped'
VBN -> 'struck'
VBN -> 'stuck'
VBN -> 'studied'
VBN -> 'submitted'
VBN -> 'subordinated'
VBN -> 'succeeded'
VBN -> 'sued'
VBN -> 'suffered'
VBN -> 'suggested'
VBN -> 'supplied'
VBN -> 'supported'
VBN -> 'supposed'
VBN -> 'surprised'
VBN -> 'surveyed'
VBN -> 'suspended'
VBN -> 'sustained'
VBN -> 'sweetened'
VBN -> 'switched'
VBN -> 'taken'
VBN -> 'taped'
VBN -> 'targeted'
VBN -> 'tendered'
VBN -> 'tested'
VBN -> 'thought'
VBN -> 'threatened'
VBN -> 'thrown'
VBN -> 'tied'
VBN -> 'titled'
VBN -> 'told'
VBN -> 'tracked'
VBN -> 'traded'
VBN -> 'transferred'
VBN -> 'treated'
VBN -> 'tried'
VBN -> 'triggered'
VBN -> 'tripled'
VBN -> 'troubled'
VBN -> 'turned'
VBN -> 'undervalued'
VBN -> 'used'
VBN -> 'valued'
VBN -> 'viewed'
VBN -> 'watched'
VBN -> 'withdrawn'
VBN -> 'won'
VBN -> 'worked'
VBN -> 'worried'
VBN -> 'written'
WP -> 'What'
WP -> 'Who'
WP -> 'what'
WP -> 'who'
WP -> 'whom'
SBARNOMPRD -> WHNP S
JJ -> '10year'
JJ -> '100share'
JJ -> '12year'
JJ -> '13th'
JJ -> '190point'
JJ -> '190point58point'
JJ -> '2for1'
JJ -> '20year'
JJ -> '20th'
JJ -> '30day'
JJ -> '30share'
JJ -> '30year'
JJ -> '300ashare'
JJ -> '300day'
JJ -> '52week'
JJ -> 'African'
JJ -> 'American'
JJ -> 'Angelesbased'
JJ -> 'Arab'
JJ -> 'Asian'
JJ -> 'Australian'
JJ -> 'Big'
JJ -> 'Brazilian'
JJ -> 'British'
JJ -> 'Califpointbased'
JJ -> 'Canadian'
JJ -> 'Chicagobased'
JJ -> 'Chinese'
JJ -> 'Christian'
JJ -> 'Colombian'
JJ -> 'Communist'
JJ -> 'Democratic'
JJ -> 'Denverbased'
JJ -> 'Dutch'
JJ -> 'East'
JJ -> 'Egyptian'
JJ -> 'English'
JJ -> 'European'
JJ -> 'Finnish'
JJ -> 'First'
JJ -> 'French'
JJ -> 'German'
JJ -> 'Great'
JJ -> 'Highgrade'
JJ -> 'Hispanic'
JJ -> 'Housepassed'
JJ -> 'Hungarian'
JJ -> 'Indian'
JJ -> 'Irish'
JJ -> 'Israeli'
JJ -> 'Italian'
JJ -> 'Japanese'
JJ -> 'Jewish'
JJ -> 'Korean'
JJ -> 'Latin'
JJ -> 'Londonbased'
JJ -> 'Mexican'
JJ -> 'Miamibased'
JJ -> 'Nicaraguan'
JJ -> 'North'
JJ -> 'Northern'
JJ -> 'Panamanian'
JJ -> 'Philippine'
JJ -> 'Polish'
JJ -> 'Republican'
JJ -> 'Russian'
JJ -> 'South'
JJ -> 'Soviet'
JJ -> 'Spanish'
JJ -> 'Swedish'
JJ -> 'Swiss'
JJ -> 'Taiwanese'
JJ -> 'Vietnamese'
JJ -> 'Washingtonbased'
JJ -> 'West'
JJ -> 'Western'
JJ -> 'Yorkbased'
JJ -> 'able'
JJ -> 'abrupt'
JJ -> 'academic'
JJ -> 'acceptable'
JJ -> 'accepted'
JJ -> 'accurate'
JJ -> 'acrosstheboard'
JJ -> 'active'
JJ -> 'actual'
JJ -> 'added'
JJ -> 'additional'
JJ -> 'adequate'
JJ -> 'adjustable'
JJ -> 'adjusted'
JJ -> 'administrative'
JJ -> 'advanced'
JJ -> 'adverse'
JJ -> 'affluent'
JJ -> 'afraid'
JJ -> 'aftertax'
JJ -> 'aggressive'
JJ -> 'agricultural'
JJ -> 'alive'
JJ -> 'alleged'
JJ -> 'alternative'
JJ -> 'ambitious'
JJ -> 'ample'
JJ -> 'angry'
JJ -> 'annual'
JJ -> 'annualized'
JJ -> 'antiabortion'
JJ -> 'antitakeover'
JJ -> 'anticipated'
JJ -> 'antitrust'
JJ -> 'anxious'
JJ -> 'apparent'
JJ -> 'applicable'
JJ -> 'appropriate'
JJ -> 'architectural'
JJ -> 'assetbacked'
JJ -> 'assistant'
JJ -> 'associate'
JJ -> 'atmospheric'
JJ -> 'attractive'
JJ -> 'automatic'
JJ -> 'automotive'
JJ -> 'available'
JJ -> 'average'
JJ -> 'aware'
JJ -> 'back'
JJ -> 'bad'
JJ -> 'bankbacked'
JJ -> 'base'
JJ -> 'basic'
JJ -> 'bearish'
JJ -> 'benchmark'
JJ -> 'big'
JJ -> 'bitter'
JJ -> 'black'
JJ -> 'blackandwhite'
JJ -> 'bleak'
JJ -> 'blue'
JJ -> 'bluechip'
JJ -> 'bold'
JJ -> 'bondequivalent'
JJ -> 'bottom'
JJ -> 'brief'
JJ -> 'bright'
JJ -> 'brisk'
JJ -> 'broad'
JJ -> 'budgetary'
JJ -> 'bullish'
JJ -> 'busy'
JJ -> 'buy'
JJ -> 'buyback'
JJ -> 'buyout'
JJ -> 'call'
JJ -> 'capable'
JJ -> 'capitalgains'
JJ -> 'capped'
JJ -> 'careful'
JJ -> 'catastrophic'
JJ -> 'cautious'
JJ -> 'cellular'
JJ -> 'central'
JJ -> 'certain'
JJ -> 'changed'
JJ -> 'chaotic'
JJ -> 'characteristic'
JJ -> 'charitable'
JJ -> 'cheap'
JJ -> 'chemical'
JJ -> 'chief'
JJ -> 'civil'
JJ -> 'classaction'
JJ -> 'classic'
JJ -> 'clear'
JJ -> 'clinical'
JJ -> 'close'
JJ -> 'closed'
JJ -> 'closedend'
JJ -> 'cold'
JJ -> 'collective'
JJ -> 'combined'
JJ -> 'comfortable'
JJ -> 'comic'
JJ -> 'coming'
JJ -> 'commercial'
JJ -> 'committed'
JJ -> 'common'
JJ -> 'communist'
JJ -> 'comparable'
JJ -> 'compelling'
JJ -> 'competitive'
JJ -> 'complete'
JJ -> 'complex'
JJ -> 'composite'
JJ -> 'comprehensive'
JJ -> 'computerdriven'
JJ -> 'computerguided'
JJ -> 'computerized'
JJ -> 'concentrated'
JJ -> 'concerned'
JJ -> 'concrete'
JJ -> 'confident'
JJ -> 'confidential'
JJ -> 'congressional'
JJ -> 'consecutive'
JJ -> 'conservative'
JJ -> 'considerable'
JJ -> 'consistent'
JJ -> 'consolidated'
JJ -> 'constant'
JJ -> 'constitutional'
JJ -> 'continued'
JJ -> 'continuing'
JJ -> 'contrary'
JJ -> 'controversial'
JJ -> 'conventional'
JJ -> 'convertible'
JJ -> 'convinced'
JJ -> 'cool'
JJ -> 'cooperative'
JJ -> 'core'
JJ -> 'corporate'
JJ -> 'costly'
JJ -> 'covert'
JJ -> 'crazy'
JJ -> 'creative'
JJ -> 'credible'
JJ -> 'criminal'
JJ -> 'critical'
JJ -> 'crowded'
JJ -> 'crucial'
JJ -> 'crude'
JJ -> 'cubic'
JJ -> 'cultural'
JJ -> 'cumulative'
JJ -> 'current'
JJ -> 'cyclical'
JJ -> 'daily'
JJ -> 'damaged'
JJ -> 'dangerous'
JJ -> 'daytoday'
JJ -> 'dead'
JJ -> 'decent'
JJ -> 'deductible'
JJ -> 'deep'
JJ -> 'defensive'
JJ -> 'definitive'
JJ -> 'defunct'
JJ -> 'democratic'
JJ -> 'dependent'
JJ -> 'depositary'
JJ -> 'depository'
JJ -> 'deputy'
JJ -> 'derivative'
JJ -> 'desirable'
JJ -> 'desperate'
JJ -> 'different'
JJ -> 'difficult'
JJ -> 'diplomatic'
JJ -> 'direct'
JJ -> 'disappointed'
JJ -> 'disappointing'
JJ -> 'disciplinary'
JJ -> 'discount'
JJ -> 'discretionary'
JJ -> 'dismal'
JJ -> 'disposable'
JJ -> 'dissident'
JJ -> 'diversified'
JJ -> 'dizzying'
JJ -> 'domestic'
JJ -> 'dominant'
JJ -> 'double'
JJ -> 'doubledigit'
JJ -> 'doubtful'
JJ -> 'down'
JJ -> 'downward'
JJ -> 'dramatic'
JJ -> 'dry'
JJ -> 'dual'
JJ -> 'dubious'
JJ -> 'due'
JJ -> 'durable'
JJ -> 'dutyfree'
JJ -> 'eager'
JJ -> 'early'
JJ -> 'east'
JJ -> 'easy'
JJ -> 'economic'
JJ -> 'educational'
JJ -> 'effective'
JJ -> 'efficient'
JJ -> 'elderly'
JJ -> 'electric'
JJ -> 'electrical'
JJ -> 'electronic'
JJ -> 'eligible'
JJ -> 'else'
JJ -> 'emotional'
JJ -> 'empty'
JJ -> 'enormous'
JJ -> 'enough'
JJ -> 'entire'
JJ -> 'environmental'
JJ -> 'equal'
JJ -> 'equitypurchase'
JJ -> 'equivalent'
JJ -> 'essential'
JJ -> 'estimated'
JJ -> 'ethnic'
JJ -> 'evident'
JJ -> 'exact'
JJ -> 'excellent'
JJ -> 'excess'
JJ -> 'excessive'
JJ -> 'exciting'
JJ -> 'exclusive'
JJ -> 'executive'
JJ -> 'exercisable'
JJ -> 'existing'
JJ -> 'expected'
JJ -> 'expensive'
JJ -> 'extensive'
JJ -> 'external'
JJ -> 'extra'
JJ -> 'extraordinary'
JJ -> 'fair'
JJ -> 'false'
JJ -> 'familiar'
JJ -> 'famous'
JJ -> 'fastestgrowing'
JJ -> 'fat'
JJ -> 'favorable'
JJ -> 'favorite'
JJ -> 'federal'
JJ -> 'female'
JJ -> 'few'
JJ -> 'fierce'
JJ -> 'fifth'
JJ -> 'final'
JJ -> 'financial'
JJ -> 'fine'
JJ -> 'firm'
JJ -> 'first'
JJ -> 'fiscal'
JJ -> 'fiveyear'
JJ -> 'fixed'
JJ -> 'fixedincome'
JJ -> 'fixedrate'
JJ -> 'flat'
JJ -> 'flexible'
JJ -> 'floatingrate'
JJ -> 'following'
JJ -> 'foreign'
JJ -> 'formal'
JJ -> 'former'
JJ -> 'fouryear'
JJ -> 'fouryearold'
JJ -> 'fourth'
JJ -> 'fourthquarter'
JJ -> 'free'
JJ -> 'freelance'
JJ -> 'frequent'
JJ -> 'fresh'
JJ -> 'friendly'
JJ -> 'front'
JJ -> 'full'
JJ -> 'fullyear'
JJ -> 'fundamental'
JJ -> 'further'
JJ -> 'future'
JJ -> 'general'
JJ -> 'generous'
JJ -> 'genetic'
JJ -> 'genuine'
JJ -> 'giant'
JJ -> 'global'
JJ -> 'gold'
JJ -> 'golden'
JJ -> 'good'
JJ -> 'grand'
JJ -> 'gray'
JJ -> 'great'
JJ -> 'green'
JJ -> 'grim'
JJ -> 'gross'
JJ -> 'guilty'
JJ -> 'half'
JJ -> 'handy'
JJ -> 'happy'
JJ -> 'hard'
JJ -> 'healthcare'
JJ -> 'healthy'
JJ -> 'heavy'
JJ -> 'hefty'
JJ -> 'held'
JJ -> 'helpful'
JJ -> 'high'
JJ -> 'highdefinition'
JJ -> 'highend'
JJ -> 'highpriced'
JJ -> 'highquality'
JJ -> 'highrisk'
JJ -> 'hightech'
JJ -> 'highyield'
JJ -> 'historical'
JJ -> 'horrible'
JJ -> 'hostile'
JJ -> 'hot'
JJ -> 'hotdipped'
JJ -> 'huge'
JJ -> 'human'
JJ -> 'hybrid'
JJ -> 'identical'
JJ -> 'idle'
JJ -> 'illegal'
JJ -> 'immediate'
JJ -> 'imminent'
JJ -> 'immune'
JJ -> 'impending'
JJ -> 'important'
JJ -> 'impossible'
JJ -> 'improved'
JJ -> 'incomplete'
JJ -> 'increased'
JJ -> 'independent'
JJ -> 'indicated'
JJ -> 'indirect'
JJ -> 'individual'
JJ -> 'industrial'
JJ -> 'industrywide'
JJ -> 'inevitable'
JJ -> 'inflationadjusted'
JJ -> 'influential'
JJ -> 'informal'
JJ -> 'inherent'
JJ -> 'initial'
JJ -> 'innovative'
JJ -> 'institutional'
JJ -> 'insufficient'
JJ -> 'insured'
JJ -> 'intense'
JJ -> 'interbank'
JJ -> 'interested'
JJ -> 'interesting'
JJ -> 'interim'
JJ -> 'internal'
JJ -> 'international'
JJ -> 'interstate'
JJ -> 'investmentgrade'
JJ -> 'involved'
JJ -> 'ironic'
JJ -> 'irresponsible'
JJ -> 'joint'
JJ -> 'judicial'
JJ -> 'jumbo'
JJ -> 'junkbond'
JJ -> 'key'
JJ -> 'labormanagement'
JJ -> 'lackluster'
JJ -> 'large'
JJ -> 'last'
JJ -> 'lastminute'
JJ -> 'late'
JJ -> 'later'
JJ -> 'lead'
JJ -> 'leading'
JJ -> 'leftist'
JJ -> 'legal'
JJ -> 'legislative'
JJ -> 'legitimate'
JJ -> 'leveraged'
JJ -> 'liable'
JJ -> 'liberal'
JJ -> 'light'
JJ -> 'like'
JJ -> 'likely'
JJ -> 'limited'
JJ -> 'lineitem'
JJ -> 'liquid'
JJ -> 'little'
JJ -> 'loanloss'
JJ -> 'local'
JJ -> 'long'
JJ -> 'longterm'
JJ -> 'longstanding'
JJ -> 'longtime'
JJ -> 'low'
JJ -> 'lowincome'
JJ -> 'loyal'
JJ -> 'lucky'
JJ -> 'lucrative'
JJ -> 'magnetic'
JJ -> 'main'
JJ -> 'major'
JJ -> 'male'
JJ -> 'mandatory'
JJ -> 'many'
JJ -> 'massmarket'
JJ -> 'massive'
JJ -> 'maximum'
JJ -> 'meaningful'
JJ -> 'mechanical'
JJ -> 'medical'
JJ -> 'mere'
JJ -> 'metric'
JJ -> 'metropolitan'
JJ -> 'middle'
JJ -> 'mild'
JJ -> 'military'
JJ -> 'minimal'
JJ -> 'minimum'
JJ -> 'minor'
JJ -> 'mixed'
JJ -> 'moderate'
JJ -> 'modern'
JJ -> 'modest'
JJ -> 'monetary'
JJ -> 'moneymarket'
JJ -> 'monthly'
JJ -> 'moral'
JJ -> 'mortgagebacked'
JJ -> 'much'
JJ -> 'multiple'
JJ -> 'municipal'
JJ -> 'mutual'
JJ -> 'narrow'
JJ -> 'nasty'
JJ -> 'national'
JJ -> 'nationwide'
JJ -> 'natural'
JJ -> 'near'
JJ -> 'nearterm'
JJ -> 'nearby'
JJ -> 'necessary'
JJ -> 'negative'
JJ -> 'negotiable'
JJ -> 'nervous'
JJ -> 'net'
JJ -> 'new'
JJ -> 'newissue'
JJ -> 'next'
JJ -> 'nice'
JJ -> 'ninemonth'
JJ -> 'nonfinancial'
JJ -> 'nonfood'
JJ -> 'noninterest'
JJ -> 'noncallable'
JJ -> 'nonexecutive'
JJ -> 'normal'
JJ -> 'northern'
JJ -> 'nuclear'
JJ -> 'numerous'
JJ -> 'obvious'
JJ -> 'odd'
JJ -> 'off'
JJ -> 'official'
JJ -> 'old'
JJ -> 'oldfashioned'
JJ -> 'onsite'
JJ -> 'oneday'
JJ -> 'onethird'
JJ -> 'onetime'
JJ -> 'oneyear'
JJ -> 'ongoing'
JJ -> 'only'
JJ -> 'open'
JJ -> 'operational'
JJ -> 'optical'
JJ -> 'optimistic'
JJ -> 'orderly'
JJ -> 'ordinary'
JJ -> 'organized'
JJ -> 'original'
JJ -> 'other'
JJ -> 'outside'
JJ -> 'outstanding'
JJ -> 'overthecounter'
JJ -> 'overall'
JJ -> 'overdue'
JJ -> 'overnight'
JJ -> 'overseas'
JJ -> 'overwhelming'
JJ -> 'own'
JJ -> 'painful'
JJ -> 'par'
JJ -> 'partial'
JJ -> 'particular'
JJ -> 'passive'
JJ -> 'past'
JJ -> 'payable'
JJ -> 'peaceful'
JJ -> 'pershare'
JJ -> 'periodic'
JJ -> 'permanent'
JJ -> 'persistent'
JJ -> 'personal'
JJ -> 'pessimistic'
JJ -> 'pharmaceutical'
JJ -> 'photographic'
JJ -> 'planned'
JJ -> 'plastic'
JJ -> 'pleased'
JJ -> 'political'
JJ -> 'poor'
JJ -> 'popular'
JJ -> 'portable'
JJ -> 'positive'
JJ -> 'possible'
JJ -> 'postcrash'
JJ -> 'postwar'
JJ -> 'potential'
JJ -> 'powerful'
JJ -> 'practical'
JJ -> 'pretrial'
JJ -> 'precious'
JJ -> 'preferred'
JJ -> 'pregnant'
JJ -> 'preliminary'
JJ -> 'prepared'
JJ -> 'present'
JJ -> 'presidential'
JJ -> 'prestigious'
JJ -> 'pretax'
JJ -> 'previous'
JJ -> 'primary'
JJ -> 'prime'
JJ -> 'principal'
JJ -> 'prior'
JJ -> 'private'
JJ -> 'privatesector'
JJ -> 'prochoice'
JJ -> 'prodemocracy'
JJ -> 'procedural'
JJ -> 'productive'
JJ -> 'professional'
JJ -> 'profitable'
JJ -> 'programtrading'
JJ -> 'prominent'
JJ -> 'proper'
JJ -> 'proposed'
JJ -> 'prospective'
JJ -> 'provisional'
JJ -> 'prudent'
JJ -> 'public'
JJ -> 'punishable'
JJ -> 'punitive'
JJ -> 'quarterly'
JJ -> 'questionable'
JJ -> 'quick'
JJ -> 'quiet'
JJ -> 'racial'
JJ -> 'radical'
JJ -> 'random'
JJ -> 'rapid'
JJ -> 'rare'
JJ -> 'raw'
JJ -> 'ready'
JJ -> 'real'
JJ -> 'reasonable'
JJ -> 'recent'
JJ -> 'record'
JJ -> 'red'
JJ -> 'reduced'
JJ -> 'regional'
JJ -> 'regular'
JJ -> 'regulatory'
JJ -> 'related'
JJ -> 'relative'
JJ -> 'reluctant'
JJ -> 'remaining'
JJ -> 'remarkable'
JJ -> 'rental'
JJ -> 'required'
JJ -> 'residential'
JJ -> 'responsible'
JJ -> 'restrictive'
JJ -> 'retail'
JJ -> 'revised'
JJ -> 'rich'
JJ -> 'rid'
JJ -> 'right'
JJ -> 'rigid'
JJ -> 'risky'
JJ -> 'rival'
JJ -> 'robust'
JJ -> 'rough'
JJ -> 'routine'
JJ -> 'rural'
JJ -> 'sad'
JJ -> 'safe'
JJ -> 'sales'
JJ -> 'same'
JJ -> 'savingsandloan'
JJ -> 'scarce'
JJ -> 'scary'
JJ -> 'scheduled'
JJ -> 'scientific'
JJ -> 'seasonal'
JJ -> 'second'
JJ -> 'secondlargest'
JJ -> 'secondquarter'
JJ -> 'secondary'
JJ -> 'secret'
JJ -> 'secured'
JJ -> 'seismic'
JJ -> 'senior'
JJ -> 'sensitive'
JJ -> 'separate'
JJ -> 'serial'
JJ -> 'serious'
JJ -> 'sevenday'
JJ -> 'sevenyear'
JJ -> 'seventh'
JJ -> 'several'
JJ -> 'severe'
JJ -> 'shaky'
JJ -> 'sharp'
JJ -> 'short'
JJ -> 'shortterm'
JJ -> 'sick'
JJ -> 'significant'
JJ -> 'similar'
JJ -> 'simple'
JJ -> 'single'
JJ -> 'sixmonth'
JJ -> 'sixth'
JJ -> 'sizable'
JJ -> 'skeptical'
JJ -> 'slight'
JJ -> 'slim'
JJ -> 'slow'
JJ -> 'sluggish'
JJ -> 'small'
JJ -> 'smooth'
JJ -> 'socalled'
JJ -> 'social'
JJ -> 'socialist'
JJ -> 'soft'
JJ -> 'sole'
JJ -> 'solid'
JJ -> 'sophisticated'
JJ -> 'sorry'
JJ -> 'sound'
JJ -> 'sour'
JJ -> 'south'
JJ -> 'southern'
JJ -> 'special'
JJ -> 'specific'
JJ -> 'spectacular'
JJ -> 'square'
JJ -> 'stable'
JJ -> 'standard'
JJ -> 'standardized'
JJ -> 'startup'
JJ -> 'stateowned'
JJ -> 'statistical'
JJ -> 'steady'
JJ -> 'steep'
JJ -> 'stiff'
JJ -> 'stockindex'
JJ -> 'straight'
JJ -> 'strange'
JJ -> 'strategic'
JJ -> 'strict'
JJ -> 'striking'
JJ -> 'strong'
JJ -> 'structural'
JJ -> 'stupid'
JJ -> 'subject'
JJ -> 'subordinated'
JJ -> 'substantial'
JJ -> 'suburban'
JJ -> 'successful'
JJ -> 'such'
JJ -> 'sudden'
JJ -> 'sufficient'
JJ -> 'superior'
JJ -> 'sure'
JJ -> 'surprising'
JJ -> 'sweeping'
JJ -> 'sweet'
JJ -> 'sympathetic'
JJ -> 'synthetic'
JJ -> 'tall'
JJ -> 'taxexempt'
JJ -> 'taxfree'
JJ -> 'taxable'
JJ -> 'technical'
JJ -> 'temporary'
JJ -> 'tentative'
JJ -> 'thin'
JJ -> 'third'
JJ -> 'thirdquarter'
JJ -> 'threemonth'
JJ -> 'threeyear'
JJ -> 'tight'
JJ -> 'tiny'
JJ -> 'tony'
JJ -> 'top'
JJ -> 'total'
JJ -> 'tough'
JJ -> 'traditional'
JJ -> 'tremendous'
JJ -> 'tricky'
JJ -> 'troubled'
JJ -> 'troublesome'
JJ -> 'troubling'
JJ -> 'true'
JJ -> 'twoday'
JJ -> 'twoyear'
JJ -> 'typical'
JJ -> 'ultimate'
JJ -> 'unable'
JJ -> 'unavailable'
JJ -> 'uncertain'
JJ -> 'unchanged'
JJ -> 'unclear'
JJ -> 'unconstitutional'
JJ -> 'undemocratic'
JJ -> 'underlying'
JJ -> 'undisclosed'
JJ -> 'unexpected'
JJ -> 'unfair'
JJ -> 'unfilled'
JJ -> 'unfortunate'
JJ -> 'unhappy'
JJ -> 'unlikely'
JJ -> 'unnecessary'
JJ -> 'unprecedented'
JJ -> 'unrelated'
JJ -> 'unsecured'
JJ -> 'unsettled'
JJ -> 'unsolicited'
JJ -> 'unspecified'
JJ -> 'unsuccessful'
JJ -> 'unusual'
JJ -> 'unwanted'
JJ -> 'unwelcome'
JJ -> 'upper'
JJ -> 'upscale'
JJ -> 'upward'
JJ -> 'urban'
JJ -> 'used'
JJ -> 'useful'
JJ -> 'usual'
JJ -> 'vacant'
JJ -> 'valid'
JJ -> 'valuable'
JJ -> 'various'
JJ -> 'vast'
JJ -> 'very'
JJ -> 'vicious'
JJ -> 'vigorous'
JJ -> 'visible'
JJ -> 'volatile'
JJ -> 'voluntary'
JJ -> 'vulnerable'
JJ -> 'wary'
JJ -> 'weak'
JJ -> 'weekly'
JJ -> 'weird'
JJ -> 'welcome'
JJ -> 'west'
JJ -> 'western'
JJ -> 'whenissued'
JJ -> 'white'
JJ -> 'whitecollar'
JJ -> 'whole'
JJ -> 'wholesale'
JJ -> 'wide'
JJ -> 'widespread'
JJ -> 'wild'
JJ -> 'willing'
JJ -> 'worldwide'
JJ -> 'worried'
JJ -> 'worth'
JJ -> 'wouldbe'
JJ -> 'wrong'
JJ -> 'yearago'
JJ -> 'yearearlier'
JJ -> 'yearend'
JJ -> 'yearly'
JJ -> 'yellow'
JJ -> 'young'
JJ -> 'zerocoupon'
TO -> 'To'
TO -> 'to'
PPPRD -> IN NP
PPPRD -> IN PP
PPPRD -> IN SNOM
PPPRD -> JJ NP
PPPRD -> TO NP
QPMONEY -> PUNCdollar QP
QPMONEY -> DT QPMONEY
QPMONEY -> IN QPMONEY
QPMONEY -> QPMONEY PP
QPMONEY -> RB QPMONEY
WRB -> 'How'
WRB -> 'When'
WRB -> 'Where'
WRB -> 'Why'
WRB -> 'how'
WRB -> 'when'
WRB -> 'whenever'
WRB -> 'where'
WRB -> 'why'
PRN -> COMMA S
PRN -> PUNCcolon NP
PRN -> S
PRN -> S COMMA
PRN -> SINV
SBARPRPPRD -> IN S
WDT -> 'that'
WDT -> 'what'
WDT -> 'whatever'
WDT -> 'which'
QP -> CD
QP -> CD CD
QP -> DT QP
QP -> IN QP
QP -> JJ QP
QP -> QP JJR
QP -> QP NNS
QP -> QP PP
QP -> RB DT
QP -> RB NN
QP -> RB PDT
QP -> RB QP
QP -> RB RB
QP -> TO QP
VBZ -> "'s"
VBZ -> 'Is'
VBZ -> 'accounts'
VBZ -> 'acknowledges'
VBZ -> 'acts'
VBZ -> 'adds'
VBZ -> 'admits'
VBZ -> 'advises'
VBZ -> 'agrees'
VBZ -> 'alleges'
VBZ -> 'allows'
VBZ -> 'amounts'
VBZ -> 'anticipates'
VBZ -> 'appears'
VBZ -> 'argues'
VBZ -> 'asks'
VBZ -> 'asserts'
VBZ -> 'assumes'
VBZ -> 'attracts'
VBZ -> 'bears'
VBZ -> 'becomes'
VBZ -> 'begins'
VBZ -> 'believes'
VBZ -> 'belongs'
VBZ -> 'blames'
VBZ -> 'boasts'
VBZ -> 'boosts'
VBZ -> 'breaks'
VBZ -> 'brings'
VBZ -> 'buys'
VBZ -> 'calls'
VBZ -> 'carries'
VBZ -> 'causes'
VBZ -> 'changes'
VBZ -> 'charges'
VBZ -> 'claims'
VBZ -> 'comes'
VBZ -> 'compares'
VBZ -> 'complains'
VBZ -> 'concedes'
VBZ -> 'concerns'
VBZ -> 'concludes'
VBZ -> 'confirms'
VBZ -> 'considers'
VBZ -> 'contains'
VBZ -> 'contends'
VBZ -> 'continues'
VBZ -> 'controls'
VBZ -> 'costs'
VBZ -> 'counts'
VBZ -> 'covers'
VBZ -> 'cuts'
VBZ -> 'declares'
VBZ -> 'declines'
VBZ -> 'demonstrates'
VBZ -> 'denies'
VBZ -> 'depends'
VBZ -> 'describes'
VBZ -> 'does'
VBZ -> 'doubts'
VBZ -> 'draws'
VBZ -> 'drops'
VBZ -> 'emerges'
VBZ -> 'employs'
VBZ -> 'ends'
VBZ -> 'estimates'
VBZ -> 'exceeds'
VBZ -> 'exists'
VBZ -> 'expects'
VBZ -> 'expires'
VBZ -> 'explains'
VBZ -> 'faces'
VBZ -> 'fails'
VBZ -> 'falls'
VBZ -> 'feels'
VBZ -> 'figures'
VBZ -> 'finds'
VBZ -> 'follows'
VBZ -> 'forces'
VBZ -> 'generates'
VBZ -> 'gets'
VBZ -> 'gives'
VBZ -> 'goes'
VBZ -> 'grows'
VBZ -> 'guarantees'
VBZ -> 'happens'
VBZ -> 'has'
VBZ -> 'heads'
VBZ -> 'helps'
VBZ -> 'holds'
VBZ -> 'hopes'
VBZ -> 'includes'
VBZ -> 'increases'
VBZ -> 'indicates'
VBZ -> 'insists'
VBZ -> 'intends'
VBZ -> 'involves'
VBZ -> 'is'
VBZ -> 'joins'
VBZ -> 'keeps'
VBZ -> 'knows'
VBZ -> 'lacks'
VBZ -> 'leads'
VBZ -> 'leaves'
VBZ -> 'lies'
VBZ -> 'likes'
VBZ -> 'lives'
VBZ -> 'looks'
VBZ -> 'maintains'
VBZ -> 'makes'
VBZ -> 'manages'
VBZ -> 'marks'
VBZ -> 'matches'
VBZ -> 'means'
VBZ -> 'meets'
VBZ -> 'misses'
VBZ -> 'moves'
VBZ -> 'narrows'
VBZ -> 'needs'
VBZ -> 'notes'
VBZ -> 'occurs'
VBZ -> 'offers'
VBZ -> 'operates'
VBZ -> 'opposes'
VBZ -> 'oversees'
VBZ -> 'owes'
VBZ -> 'owns'
VBZ -> 'pays'
VBZ -> 'permits'
VBZ -> 'places'
VBZ -> 'plans'
VBZ -> 'plays'
VBZ -> 'points'
VBZ -> 'predicts'
VBZ -> 'presents'
VBZ -> 'prevails'
VBZ -> 'prevents'
VBZ -> 'produces'
VBZ -> 'prohibits'
VBZ -> 'promises'
VBZ -> 'provides'
VBZ -> 'puts'
VBZ -> 'quotes'
VBZ -> 'raises'
VBZ -> 'reaches'
VBZ -> 'recalls'
VBZ -> 'receives'
VBZ -> 'reduces'
VBZ -> 'reflects'
VBZ -> 'refuses'
VBZ -> 'regains'
VBZ -> 'relies'
VBZ -> 'remains'
VBZ -> 'replies'
VBZ -> 'reports'
VBZ -> 'represents'
VBZ -> 'requires'
VBZ -> 'results'
VBZ -> 'retains'
VBZ -> 'returns'
VBZ -> 'runs'
VBZ -> 'says'
VBZ -> 'seeks'
VBZ -> 'seems'
VBZ -> 'sees'
VBZ -> 'sells'
VBZ -> 'serves'
VBZ -> 'sets'
VBZ -> 'shares'
VBZ -> 'shows'
VBZ -> 'sounds'
VBZ -> 'specializes'
VBZ -> 'spends'
VBZ -> 'stands'
VBZ -> 'starts'
VBZ -> 'states'
VBZ -> 'stems'
VBZ -> 'succeeds'
VBZ -> 'suggests'
VBZ -> 'suspects'
VBZ -> 'takes'
VBZ -> 'talks'
VBZ -> 'tells'
VBZ -> 'thinks'
VBZ -> 'throws'
VBZ -> 'tracks'
VBZ -> 'trades'
VBZ -> 'tries'
VBZ -> 'turns'
VBZ -> 'understands'
VBZ -> 'uses'
VBZ -> 'values'
VBZ -> 'wants'
VBZ -> 'widens'
VBZ -> 'wins'
VBZ -> 'works'
VBZ -> 'writes'
STAR -> '*'
SNOMPRD -> VP
POS -> "'"
POS -> "'s"
SBARSBJ -> IN S
NPdollar -> NP POS
SBARQ -> WHNP SQ
NPR -> DT NPR
NPR -> NNP
NPR -> NNP NNP
NPR -> NNPS NNP
NPR -> NP PP
NPR -> NPRS
NPRS -> NNP NNPS
NPRS -> NNPS
NPRS -> NNPS NNPS
NPPRD -> ADJP NN
NPPRD -> DT
NPPRD -> DT ADJP
NPPRD -> DT JJ
NPPRD -> DT NN
NPPRD -> DT NNS
NPPRD -> DT NPR
NPPRD -> JJ
NPPRD -> JJ NN
NPPRD -> JJ NNS
NPPRD -> JJR
NPPRD -> NN
NPPRD -> NN NN
NPPRD -> NN NNS
NPPRD -> NNS
NPPRD -> NNS SBAR
NPPRD -> NP ADJP
NPPRD -> NP ADVP
NPPRD -> NP NP
NPPRD -> NP NPADV
NPPRD -> NP PP
NPPRD -> NP PPLOC
NPPRD -> NP PPTMP
NPPRD -> NP PRN
NPPRD -> NP SBAR
NPPRD -> NP SBARTMP
NPPRD -> NP VP
NPPRD -> NPdollar NN
NPPRD -> NPR
NPPRD -> NPRS
NPPRD -> PRPdollar NN
NPPRD -> QP
NPPRD -> QP NN
NPPRD -> QP NNS
NPPRD -> QPMONEY
PPTMP -> IN ADJP
PPTMP -> IN ADVP
PPTMP -> IN NP
PPTMP -> IN PP
PPTMP -> IN SNOM
PPTMP -> IN SBAR
PPTMP -> PP PP
PPTMP -> RB PP
PPTMP -> RB SNOM
PPTMP -> TO NP
PPTMP -> VBG NP
PPTMP -> VBG PP
PUNCdollar -> '$'
PUNCdollar -> 'Adollar'
PUNCdollar -> 'Cdollar'
PUNCdollar -> 'HKdollar'
PUNCdollar -> 'USdollar'
SBARLOC -> WHADVP S
STPC -> VP
STPC -> NP VP
STPC -> SNOM VP
STPC -> SBARNOM VP
NN -> '%'
NN -> 'Apoint'
NN -> 'Activity'
NN -> CD
NN -> 'Chapter'
NN -> 'Class'
NN -> 'Everybody'
NN -> 'Everyone'
NN -> 'HDTV'
NN -> 'House'
NN -> 'IPO'
NN -> 'Incpoint'
NN -> 'LBO'
NN -> 'Man'
NN -> 'Market'
NN -> 'Nopoint'
NN -> 'Nobody'
NN -> 'Nothing'
NN -> 'PC'
NN -> 'S&L'
NN -> 'Section'
NN -> 'Series'
NN -> 'Treasury'
NN -> 'Volume'
NN -> 'West'
NN -> 'a'
NN -> 'apointmpoint'
NN -> 'ability'
NN -> 'abortion'
NN -> 'absence'
NN -> 'abuse'
NN -> 'acceleration'
NN -> 'acceptance'
NN -> 'access'
NN -> 'accident'
NN -> 'accord'
NN -> 'account'
NN -> 'accounting'
NN -> 'achievement'
NN -> 'acquisition'
NN -> 'act'
NN -> 'action'
NN -> 'activity'
NN -> 'actor'
NN -> 'ad'
NN -> 'addition'
NN -> 'address'
NN -> 'adjustment'
NN -> 'administration'
NN -> 'administrator'
NN -> 'admission'
NN -> 'adult'
NN -> 'advance'
NN -> 'advantage'
NN -> 'advertising'
NN -> 'advice'
NN -> 'adviser'
NN -> 'affair'
NN -> 'affiliate'
NN -> 'aftermath'
NN -> 'afternoon'
NN -> 'age'
NN -> 'agency'
NN -> 'agenda'
NN -> 'agent'
NN -> 'agreement'
NN -> 'aid'
NN -> 'aide'
NN -> 'aim'
NN -> 'air'
NN -> 'aircraft'
NN -> 'airline'
NN -> 'airport'
NN -> 'alarm'
NN -> 'alliance'
NN -> 'ally'
NN -> 'alternative'
NN -> 'aluminum'
NN -> 'ambassador'
NN -> 'amendment'
NN -> 'amount'
NN -> 'analysis'
NN -> 'analyst'
NN -> 'animal'
NN -> 'announcement'
NN -> 'answer'
NN -> 'antibody'
NN -> 'anticipation'
NN -> 'anxiety'
NN -> 'anybody'
NN -> 'anyone'
NN -> 'anything'
NN -> 'apartheid'
NN -> 'apartment'
NN -> 'apparel'
NN -> 'appeal'
NN -> 'appearance'
NN -> 'appetite'
NN -> 'apple'
NN -> 'application'
NN -> 'appointment'
NN -> 'appreciation'
NN -> 'approach'
NN -> 'approval'
NN -> 'arbitrage'
NN -> 'architecture'
NN -> 'area'
NN -> 'argument'
NN -> 'arm'
NN -> 'army'
NN -> 'arrangement'
NN -> 'array'
NN -> 'arrest'
NN -> 'art'
NN -> 'article'
NN -> 'artist'
NN -> 'asbestos'
NN -> 'aspect'
NN -> 'assassination'
NN -> 'assault'
NN -> 'assembly'
NN -> 'asset'
NN -> 'assistance'
NN -> 'assistant'
NN -> 'associate'
NN -> 'association'
NN -> 'assumption'
NN -> 'assurance'
NN -> 'atmosphere'
NN -> 'attack'
NN -> 'attempt'
NN -> 'attendance'
NN -> 'attention'
NN -> 'attitude'
NN -> 'attorney'
NN -> 'auction'
NN -> 'audience'
NN -> 'audit'
NN -> 'author'
NN -> 'authority'
NN -> 'authorization'
NN -> 'auto'
NN -> 'automobile'
NN -> 'autumn'
NN -> 'availability'
NN -> 'average'
NN -> 'award'
NN -> 'baby'
NN -> 'back'
NN -> 'backdrop'
NN -> 'background'
NN -> 'backing'
NN -> 'backlog'
NN -> 'bacterium'
NN -> 'bailout'
NN -> 'balance'
NN -> 'ball'
NN -> 'balloon'
NN -> 'ballot'
NN -> 'ban'
NN -> 'band'
NN -> 'bang'
NN -> 'bank'
NN -> 'banker'
NN -> 'banking'
NN -> 'bankruptcy'
NN -> 'bankruptcylaw'
NN -> 'bar'
NN -> 'bargain'
NN -> 'bargaining'
NN -> 'barometer'
NN -> 'barrel'
NN -> 'barrier'
NN -> 'base'
NN -> 'baseball'
NN -> 'basis'
NN -> 'basket'
NN -> 'basketball'
NN -> 'battery'
NN -> 'battle'
NN -> 'bay'
NN -> 'bear'
NN -> 'bearing'
NN -> 'bed'
NN -> 'beef'
NN -> 'beer'
NN -> 'beginning'
NN -> 'behalf'
NN -> 'behavior'
NN -> 'belief'
NN -> 'bell'
NN -> 'bellwether'
NN -> 'bench'
NN -> 'benchmark'
NN -> 'benefit'
NN -> 'bet'
NN -> 'bias'
NN -> 'bid'
NN -> 'bidder'
NN -> 'bidding'
NN -> 'bike'
NN -> 'bill'
NN -> 'binge'
NN -> 'biotechnology'
NN -> 'birth'
NN -> 'bit'
NN -> 'blame'
NN -> 'bloc'
NN -> 'block'
NN -> 'blood'
NN -> 'blow'
NN -> 'board'
NN -> 'boat'
NN -> 'body'
NN -> 'boiler'
NN -> 'bond'
NN -> 'bonus'
NN -> 'book'
NN -> 'boom'
NN -> 'boost'
NN -> 'border'
NN -> 'borough'
NN -> 'borrowing'
NN -> 'boss'
NN -> 'bottle'
NN -> 'bottom'
NN -> 'bourbon'
NN -> 'box'
NN -> 'boy'
NN -> 'brain'
NN -> 'branch'
NN -> 'brand'
NN -> 'break'
NN -> 'breakdown'
NN -> 'breaker'
NN -> 'breakfast'
NN -> 'brewer'
NN -> 'brewing'
NN -> 'bridge'
NN -> 'brief'
NN -> 'broadcast'
NN -> 'broadcasting'
NN -> 'broker'
NN -> 'brokerage'
NN -> 'budget'
NN -> 'building'
NN -> 'bulk'
NN -> 'bull'
NN -> 'bullet'
NN -> 'burden'
NN -> 'bureau'
NN -> 'bureaucracy'
NN -> 'bus'
NN -> 'bushel'
NN -> 'business'
NN -> 'businessman'
NN -> 'buy'
NN -> 'buyback'
NN -> 'buyout'
NN -> 'buyer'
NN -> 'buying'
NN -> 'cabinet'
NN -> 'cable'
NN -> 'cableTV'
NN -> 'calendar'
NN -> 'call'
NN -> 'camera'
NN -> 'campaign'
NN -> 'cancer'
NN -> 'candidate'
NN -> 'candy'
NN -> 'cap'
NN -> 'capability'
NN -> 'capacity'
NN -> 'capita'
NN -> 'capital'
NN -> 'capitalism'
NN -> 'car'
NN -> 'carbon'
NN -> 'card'
NN -> 'care'
NN -> 'career'
NN -> 'cargo'
NN -> 'carpet'
NN -> 'carpeting'
NN -> 'carrier'
NN -> 'case'
NN -> 'cash'
NN -> 'casino'
NN -> 'catalog'
NN -> 'catalyst'
NN -> 'catastrophe'
NN -> 'category'
NN -> 'cause'
NN -> 'caution'
NN -> 'ceasefire'
NN -> 'ceiling'
NN -> 'cell'
NN -> 'cement'
NN -> 'cent'
NN -> 'centennial'
NN -> 'center'
NN -> 'centerpiece'
NN -> 'century'
NN -> 'cereal'
NN -> 'chain'
NN -> 'chair'
NN -> 'chairman'
NN -> 'challenge'
NN -> 'chamber'
NN -> 'champion'
NN -> 'chance'
NN -> 'change'
NN -> 'character'
NN -> 'charge'
NN -> 'charity'
NN -> 'charter'
NN -> 'check'
NN -> 'chemical'
NN -> 'chief'
NN -> 'child'
NN -> 'chip'
NN -> 'choice'
NN -> 'cholesterol'
NN -> 'chromosome'
NN -> 'chunk'
NN -> 'church'
NN -> 'cigarette'
NN -> 'circle'
NN -> 'circuit'
NN -> 'circulation'
NN -> 'city'
NN -> 'claim'
NN -> 'class'
NN -> 'clause'
NN -> 'cleanup'
NN -> 'clearance'
NN -> 'clearing'
NN -> 'client'
NN -> 'climate'
NN -> 'climb'
NN -> 'close'
NN -> 'closing'
NN -> 'club'
NN -> 'coal'
NN -> 'coalition'
NN -> 'coast'
NN -> 'cocoa'
NN -> 'code'
NN -> 'coffee'
NN -> 'collaboration'
NN -> 'collapse'
NN -> 'collateral'
NN -> 'collection'
NN -> 'college'
NN -> 'colon'
NN -> 'colony'
NN -> 'color'
NN -> 'column'
NN -> 'combat'
NN -> 'combination'
NN -> 'comeback'
NN -> 'comedy'
NN -> 'comfort'
NN -> 'command'
NN -> 'comment'
NN -> 'commentary'
NN -> 'commercial'
NN -> 'commission'
NN -> 'commissioner'
NN -> 'commitment'
NN -> 'committee'
NN -> 'commodity'
NN -> 'common'
NN -> 'community'
NN -> 'company'
NN -> 'comparison'
NN -> 'compensation'
NN -> 'competition'
NN -> 'competitor'
NN -> 'complaint'
NN -> 'completion'
NN -> 'complex'
NN -> 'compliance'
NN -> 'component'
NN -> 'composite'
NN -> 'compound'
NN -> 'compromise'
NN -> 'comptroller'
NN -> 'computer'
NN -> 'computing'
NN -> 'concept'
NN -> 'concern'
NN -> 'conclusion'
NN -> 'condition'
NN -> 'conference'
NN -> 'confidence'
NN -> 'confirmation'
NN -> 'confusion'
NN -> 'conglomerate'
NN -> 'congress'
NN -> 'congressman'
NN -> 'connection'
NN -> 'consensus'
NN -> 'consent'
NN -> 'conservation'
NN -> 'consideration'
NN -> 'consolidation'
NN -> 'consortium'
NN -> 'conspiracy'
NN -> 'construction'
NN -> 'consultant'
NN -> 'consulting'
NN -> 'consumer'
NN -> 'consumption'
NN -> 'contest'
NN -> 'context'
NN -> 'contract'
NN -> 'contractor'
NN -> 'contrast'
NN -> 'contribution'
NN -> 'control'
NN -> 'controversy'
NN -> 'convenience'
NN -> 'convention'
NN -> 'conversation'
NN -> 'conversion'
NN -> 'conviction'
NN -> 'cooperation'
NN -> 'copper'
NN -> 'copy'
NN -> 'core'
NN -> 'corn'
NN -> 'corner'
NN -> 'corporation'
NN -> 'correction'
NN -> 'corruption'
NN -> 'cost'
NN -> 'cotton'
NN -> 'council'
NN -> 'counsel'
NN -> 'count'
NN -> 'counterpart'
NN -> 'country'
NN -> 'county'
NN -> 'coup'
NN -> 'couple'
NN -> 'coupon'
NN -> 'course'
NN -> 'court'
NN -> 'coverage'
NN -> 'crack'
NN -> 'crash'
NN -> 'creation'
NN -> 'credibility'
NN -> 'credit'
NN -> 'creditcard'
NN -> 'creditor'
NN -> 'crime'
NN -> 'crisis'
NN -> 'criticism'
NN -> 'crop'
NN -> 'crowd'
NN -> 'crude'
NN -> 'cruise'
NN -> 'crunch'
NN -> 'culture'
NN -> 'currency'
NN -> 'cushion'
NN -> 'customer'
NN -> 'cut'
NN -> 'cycle'
NN -> 'dam'
NN -> 'damage'
NN -> 'danger'
NN -> 'data'
NN -> 'date'
NN -> 'day'
NN -> 'deadline'
NN -> 'deal'
NN -> 'dealer'
NN -> 'dealership'
NN -> 'death'
NN -> 'debacle'
NN -> 'debate'
NN -> 'debenture'
NN -> 'debt'
NN -> 'debut'
NN -> 'decade'
NN -> 'decision'
NN -> 'declaration'
NN -> 'decline'
NN -> 'default'
NN -> 'defendant'
NN -> 'defense'
NN -> 'deficiency'
NN -> 'deficit'
NN -> 'deficitreduction'
NN -> 'definition'
NN -> 'deflator'
NN -> 'degree'
NN -> 'delay'
NN -> 'delegation'
NN -> 'delivery'
NN -> 'demand'
NN -> 'demise'
NN -> 'democracy'
NN -> 'demonstration'
NN -> 'department'
NN -> 'departure'
NN -> 'dependence'
NN -> 'deposit'
NN -> 'depositary'
NN -> 'depository'
NN -> 'deputy'
NN -> 'deregulation'
NN -> 'design'
NN -> 'designer'
NN -> 'desire'
NN -> 'desk'
NN -> 'destruction'
NN -> 'detective'
NN -> 'detergent'
NN -> 'deterioration'
NN -> 'devaluation'
NN -> 'developer'
NN -> 'development'
NN -> 'device'
NN -> 'dialogue'
NN -> 'dictator'
NN -> 'difference'
NN -> 'difficulty'
NN -> 'dignity'
NN -> 'dinner'
NN -> 'dioxide'
NN -> 'direction'
NN -> 'director'
NN -> 'disappointment'
NN -> 'disaster'
NN -> 'discipline'
NN -> 'disclosure'
NN -> 'discount'
NN -> 'discounting'
NN -> 'discovery'
NN -> 'discrepancy'
NN -> 'discrimination'
NN -> 'discussion'
NN -> 'disease'
NN -> 'disk'
NN -> 'dismissal'
NN -> 'disobedience'
NN -> 'display'
NN -> 'disposal'
NN -> 'dispute'
NN -> 'distance'
NN -> 'distribution'
NN -> 'distributor'
NN -> 'district'
NN -> 'dive'
NN -> 'diversification'
NN -> 'dividend'
NN -> 'division'
NN -> 'doctor'
NN -> 'document'
NN -> 'dog'
NN -> 'dollar'
NN -> 'door'
NN -> 'doubt'
NN -> 'downgrade'
NN -> 'downtown'
NN -> 'downturn'
NN -> 'dozen'
NN -> 'draft'
NN -> 'drag'
NN -> 'drain'
NN -> 'dream'
NN -> 'dress'
NN -> 'drilling'
NN -> 'drive'
NN -> 'drop'
NN -> 'drought'
NN -> 'drug'
NN -> 'duty'
NN -> 'earning'
NN -> 'earth'
NN -> 'earthquake'
NN -> 'easing'
NN -> 'economist'
NN -> 'economy'
NN -> 'edge'
NN -> 'edition'
NN -> 'editor'
NN -> 'editorial'
NN -> 'education'
NN -> 'effect'
NN -> 'effectiveness'
NN -> 'efficiency'
NN -> 'effort'
NN -> 'egg'
NN -> 'election'
NN -> 'electricity'
NN -> 'electronics'
NN -> 'element'
NN -> 'elephant'
NN -> 'elimination'
NN -> 'embarrassment'
NN -> 'embryo'
NN -> 'emergency'
NN -> 'emphasis'
NN -> 'empire'
NN -> 'employee'
NN -> 'employer'
NN -> 'employment'
NN -> 'enactment'
NN -> 'encouragement'
NN -> 'end'
NN -> 'energy'
NN -> 'enforcement'
NN -> 'engine'
NN -> 'engineer'
NN -> 'engineering'
NN -> 'enough'
NN -> 'entertainment'
NN -> 'enthusiasm'
NN -> 'entity'
NN -> 'entrepreneur'
NN -> 'entry'
NN -> 'environment'
NN -> 'envy'
NN -> 'epicenter'
NN -> 'episode'
NN -> 'equipment'
NN -> 'equity'
NN -> 'equivalent'
NN -> 'era'
NN -> 'error'
NN -> 'establishment'
NN -> 'estate'
NN -> 'estimate'
NN -> 'ethylene'
NN -> 'euphoria'
NN -> 'evaluation'
NN -> 'evening'
NN -> 'event'
NN -> 'everybody'
NN -> 'everyone'
NN -> 'everything'
NN -> 'evidence'
NN -> 'evolution'
NN -> 'examination'
NN -> 'example'
NN -> 'exception'
NN -> 'excess'
NN -> 'exchange'
NN -> 'exclusion'
NN -> 'excuse'
NN -> 'execution'
NN -> 'executive'
NN -> 'exercise'
NN -> 'exhibit'
NN -> 'exhibition'
NN -> 'existence'
NN -> 'exodus'
NN -> 'expansion'
NN -> 'expectation'
NN -> 'expense'
NN -> 'experience'
NN -> 'experiment'
NN -> 'expert'
NN -> 'expiration'
NN -> 'explanation'
NN -> 'exploration'
NN -> 'explosion'
NN -> 'export'
NN -> 'exposure'
NN -> 'expression'
NN -> 'extension'
NN -> 'extent'
NN -> 'extradition'
NN -> 'eye'
NN -> 'face'
NN -> 'facility'
NN -> 'fact'
NN -> 'factor'
NN -> 'factory'
NN -> 'failure'
NN -> 'fairness'
NN -> 'faith'
NN -> 'fall'
NN -> 'fallout'
NN -> 'family'
NN -> 'fan'
NN -> 'fare'
NN -> 'farm'
NN -> 'farmer'
NN -> 'fashion'
NN -> 'fastfood'
NN -> 'fate'
NN -> 'father'
NN -> 'fault'
NN -> 'favor'
NN -> 'fear'
NN -> 'fee'
NN -> 'feeling'
NN -> 'fellow'
NN -> 'felony'
NN -> 'fence'
NN -> 'fever'
NN -> 'field'
NN -> 'fight'
NN -> 'figure'
NN -> 'filing'
NN -> 'film'
NN -> 'finance'
NN -> 'financier'
NN -> 'financing'
NN -> 'finding'
NN -> 'fine'
NN -> 'fire'
NN -> 'firm'
NN -> 'fishing'
NN -> 'fit'
NN -> 'flag'
NN -> 'flagship'
NN -> 'flavor'
NN -> 'fleet'
NN -> 'flexibility'
NN -> 'flight'
NN -> 'flood'
NN -> 'floor'
NN -> 'flow'
NN -> 'focus'
NN -> 'following'
NN -> 'food'
NN -> 'foot'
NN -> 'football'
NN -> 'force'
NN -> 'forecast'
NN -> 'forecasting'
NN -> 'foreignexchange'
NN -> 'forest'
NN -> 'forfeiture'
NN -> 'form'
NN -> 'format'
NN -> 'formation'
NN -> 'formula'
NN -> 'foundation'
NN -> 'founder'
NN -> 'fraction'
NN -> 'frame'
NN -> 'franc'
NN -> 'franchise'
NN -> 'fraud'
NN -> 'freedom'
NN -> 'freeway'
NN -> 'freight'
NN -> 'friend'
NN -> 'friendship'
NN -> 'front'
NN -> 'fuel'
NN -> 'fun'
NN -> 'fund'
NN -> 'funding'
NN -> 'furor'
NN -> 'fusion'
NN -> 'future'
NN -> 'gain'
NN -> 'gallery'
NN -> 'gamble'
NN -> 'game'
NN -> 'gap'
NN -> 'garden'
NN -> 'gas'
NN -> 'gasoline'
NN -> 'gene'
NN -> 'general'
NN -> 'generation'
NN -> 'ghost'
NN -> 'giant'
NN -> 'girl'
NN -> 'glass'
NN -> 'goal'
NN -> 'gold'
NN -> 'golf'
NN -> 'good'
NN -> 'government'
NN -> 'governor'
NN -> 'grain'
NN -> 'greenhouse'
NN -> 'gridlock'
NN -> 'grip'
NN -> 'ground'
NN -> 'group'
NN -> 'growth'
NN -> 'guarantee'
NN -> 'guard'
NN -> 'guerrilla'
NN -> 'guide'
NN -> 'guy'
NN -> 'habit'
NN -> 'half'
NN -> 'halfhour'
NN -> 'halt'
NN -> 'hand'
NN -> 'handful'
NN -> 'handling'
NN -> 'hardware'
NN -> 'harvest'
NN -> 'head'
NN -> 'headline'
NN -> 'headquarters'
NN -> 'health'
NN -> 'healthcare'
NN -> 'hearing'
NN -> 'heart'
NN -> 'heat'
NN -> 'heavy'
NN -> 'helicopter'
NN -> 'hell'
NN -> 'help'
NN -> 'high'
NN -> 'highway'
NN -> 'history'
NN -> 'hit'
NN -> 'hold'
NN -> 'holder'
NN -> 'holding'
NN -> 'holiday'
NN -> 'home'
NN -> 'honor'
NN -> 'hook'
NN -> 'hope'
NN -> 'horizon'
NN -> 'horse'
NN -> 'hospital'
NN -> 'host'
NN -> 'hotel'
NN -> 'hotelcasino'
NN -> 'hour'
NN -> 'house'
NN -> 'household'
NN -> 'housing'
NN -> 'humor'
NN -> 'hurricane'
NN -> 'husband'
NN -> 'hypoglycemia'
NN -> 'i'
NN -> 'ice'
NN -> 'idea'
NN -> 'identity'
NN -> 'illustration'
NN -> 'image'
NN -> 'impact'
NN -> 'impeachment'
NN -> 'import'
NN -> 'importance'
NN -> 'impression'
NN -> 'improvement'
NN -> 'incentive'
NN -> 'incident'
NN -> 'incinerator'
NN -> 'inclination'
NN -> 'income'
NN -> 'increase'
NN -> 'independence'
NN -> 'index'
NN -> 'indexarbitrage'
NN -> 'indication'
NN -> 'indicator'
NN -> 'indictment'
NN -> 'individual'
NN -> 'industry'
NN -> 'inflation'
NN -> 'influence'
NN -> 'information'
NN -> 'initiative'
NN -> 'injection'
NN -> 'injunction'
NN -> 'inquiry'
NN -> 'insider'
NN -> 'insistence'
NN -> 'inspector'
NN -> 'instance'
NN -> 'institute'
NN -> 'institution'
NN -> 'instrument'
NN -> 'insulin'
NN -> 'insurance'
NN -> 'insurer'
NN -> 'integration'
NN -> 'intelligence'
NN -> 'intent'
NN -> 'intention'
NN -> 'interbank'
NN -> 'interest'
NN -> 'interestrate'
NN -> 'interpretation'
NN -> 'intervention'
NN -> 'interview'
NN -> 'intraday'
NN -> 'introduction'
NN -> 'inventory'
NN -> 'investigation'
NN -> 'investing'
NN -> 'investment'
NN -> 'investmentbanking'
NN -> 'investor'
NN -> 'involvement'
NN -> 'island'
NN -> 'issuance'
NN -> 'issue'
NN -> 'issuer'
NN -> 'item'
NN -> 'jail'
NN -> 'jet'
NN -> 'jewelry'
NN -> 'job'
NN -> 'joint'
NN -> 'joke'
NN -> 'jolt'
NN -> 'journal'
NN -> 'journalist'
NN -> 'judge'
NN -> 'judgment'
NN -> 'jump'
NN -> 'junk'
NN -> 'junkbond'
NN -> 'jurisdiction'
NN -> 'jury'
NN -> 'justice'
NN -> 'key'
NN -> 'kind'
NN -> 'king'
NN -> 'knowledge'
NN -> 'label'
NN -> 'labor'
NN -> 'labormanagement'
NN -> 'laboratory'
NN -> 'lack'
NN -> 'lady'
NN -> 'land'
NN -> 'landing'
NN -> 'landscape'
NN -> 'language'
NN -> 'launch'
NN -> 'law'
NN -> 'lawsuit'
NN -> 'lawyer'
NN -> 'lead'
NN -> 'leader'
NN -> 'leadership'
NN -> 'league'
NN -> 'lease'
NN -> 'leasing'
NN -> 'leg'
NN -> 'legislation'
NN -> 'legislature'
NN -> 'leisure'
NN -> 'lending'
NN -> 'lesson'
NN -> 'letter'
NN -> 'level'
NN -> 'leverage'
NN -> 'liability'
NN -> 'libel'
NN -> 'library'
NN -> 'license'
NN -> 'life'
NN -> 'lifetime'
NN -> 'light'
NN -> 'likelihood'
NN -> 'limit'
NN -> 'linage'
NN -> 'line'
NN -> 'link'
NN -> 'liquidity'
NN -> 'liquor'
NN -> 'list'
NN -> 'listing'
NN -> 'literature'
NN -> 'litigation'
NN -> 'living'
NN -> 'load'
NN -> 'loan'
NN -> 'loanloss'
NN -> 'lobby'
NN -> 'lobbyist'
NN -> 'location'
NN -> 'logic'
NN -> 'longtime'
NN -> 'look'
NN -> 'loss'
NN -> 'lot'
NN -> 'love'
NN -> 'low'
NN -> 'loyalty'
NN -> 'luck'
NN -> 'lunch'
NN -> 'lung'
NN -> 'luxury'
NN -> 'luxurycar'
NN -> 'machine'
NN -> 'machinery'
NN -> 'magazine'
NN -> 'magnitude'
NN -> 'mail'
NN -> 'mainframe'
NN -> 'mainstream'
NN -> 'maintenance'
NN -> 'majority'
NN -> 'maker'
NN -> 'making'
NN -> 'mall'
NN -> 'man'
NN -> 'management'
NN -> 'manager'
NN -> 'managing'
NN -> 'mandate'
NN -> 'maneuver'
NN -> 'manner'
NN -> 'manufacturer'
NN -> 'manufacturing'
NN -> 'march'
NN -> 'margin'
NN -> 'mark'
NN -> 'market'
NN -> 'marketing'
NN -> 'marketplace'
NN -> 'mart'
NN -> 'massacre'
NN -> 'massage'
NN -> 'master'
NN -> 'material'
NN -> 'matter'
NN -> 'maturity'
NN -> 'maximum'
NN -> 'mayor'
NN -> 'meantime'
NN -> 'measure'
NN -> 'meat'
NN -> 'mechanism'
NN -> 'medicine'
NN -> 'meeting'
NN -> 'member'
NN -> 'membership'
NN -> 'memo'
NN -> 'memory'
NN -> 'merchandise'
NN -> 'merchant'
NN -> 'merger'
NN -> 'merit'
NN -> 'mess'
NN -> 'message'
NN -> 'metal'
NN -> 'method'
NN -> 'microprocessor'
NN -> 'midday'
NN -> 'middle'
NN -> 'midnight'
NN -> 'midst'
NN -> 'milk'
NN -> 'mill'
NN -> 'mind'
NN -> 'mine'
NN -> 'minimum'
NN -> 'mining'
NN -> 'minister'
NN -> 'ministry'
NN -> 'minority'
NN -> 'minute'
NN -> 'missile'
NN -> 'mission'
NN -> 'mistake'
NN -> 'mix'
NN -> 'model'
NN -> 'moment'
NN -> 'momentum'
NN -> 'money'
NN -> 'monitoring'
NN -> 'month'
NN -> 'mood'
NN -> 'morning'
NN -> 'mortality'
NN -> 'mortgage'
NN -> 'mother'
NN -> 'motion'
NN -> 'motor'
NN -> 'mountain'
NN -> 'mountainbike'
NN -> 'move'
NN -> 'movement'
NN -> 'movie'
NN -> 'mural'
NN -> 'murder'
NN -> 'music'
NN -> 'mystery'
NN -> 'name'
NN -> 'nation'
NN -> 'nature'
NN -> 'navy'
NN -> 'need'
NN -> 'negotiation'
NN -> 'neighborhood'
NN -> 'nervousness'
NN -> 'net'
NN -> 'network'
NN -> 'news'
NN -> 'newsletter'
NN -> 'newspaper'
NN -> 'niche'
NN -> 'night'
NN -> 'nobody'
NN -> 'nomination'
NN -> 'none'
NN -> 'north'
NN -> 'nose'
NN -> 'note'
NN -> 'notebook'
NN -> 'nothing'
NN -> 'notice'
NN -> 'notion'
NN -> 'novel'
NN -> 'number'
NN -> 'objective'
NN -> 'obligation'
NN -> 'obstacle'
NN -> 'offer'
NN -> 'offering'
NN -> 'office'
NN -> 'officer'
NN -> 'official'
NN -> 'oil'
NN -> 'one'
NN -> 'onethird'
NN -> 'opening'
NN -> 'operating'
NN -> 'operation'
NN -> 'operator'
NN -> 'opinion'
NN -> 'opponent'
NN -> 'opportunity'
NN -> 'opposition'
NN -> 'optimism'
NN -> 'option'
NN -> 'order'
NN -> 'ordinance'
NN -> 'organization'
NN -> 'ounce'
NN -> 'outcome'
NN -> 'outcry'
NN -> 'outlook'
NN -> 'output'
NN -> 'outside'
NN -> 'overcapacity'
NN -> 'overhaul'
NN -> 'overtime'
NN -> 'owner'
NN -> 'ownership'
NN -> 'ozone'
NN -> 'ppointmpoint'
NN -> 'p53'
NN -> 'pace'
NN -> 'pachinko'
NN -> 'package'
NN -> 'packaging'
NN -> 'pact'
NN -> 'page'
NN -> 'pageone'
NN -> 'painting'
NN -> 'panel'
NN -> 'panic'
NN -> 'paper'
NN -> 'par'
NN -> 'parent'
NN -> 'park'
NN -> 'parking'
NN -> 'parliament'
NN -> 'part'
NN -> 'participation'
NN -> 'partner'
NN -> 'partnership'
NN -> 'party'
NN -> 'passage'
NN -> 'passenger'
NN -> 'past'
NN -> 'pasta'
NN -> 'patent'
NN -> 'path'
NN -> 'patient'
NN -> 'pattern'
NN -> 'pawn'
NN -> 'pay'
NN -> 'payment'
NN -> 'payout'
NN -> 'payroll'
NN -> 'peace'
NN -> 'peak'
NN -> 'penalty'
NN -> 'pence'
NN -> 'penny'
NN -> 'pension'
NN -> 'percent'
NN -> 'percentage'
NN -> 'perception'
NN -> 'performance'
NN -> 'period'
NN -> 'permission'
NN -> 'person'
NN -> 'personalcomputer'
NN -> 'perspective'
NN -> 'pertussis'
NN -> 'pesticide'
NN -> 'petrochemical'
NN -> 'petroleum'
NN -> 'phase'
NN -> 'phenomenon'
NN -> 'philosophy'
NN -> 'phone'
NN -> 'picture'
NN -> 'piece'
NN -> 'pill'
NN -> 'pilot'
NN -> 'pipeline'
NN -> 'pit'
NN -> 'pitch'
NN -> 'place'
NN -> 'placement'
NN -> 'plan'
NN -> 'plane'
NN -> 'planner'
NN -> 'planning'
NN -> 'plant'
NN -> 'plastic'
NN -> 'plate'
NN -> 'platform'
NN -> 'platinum'
NN -> 'play'
NN -> 'player'
NN -> 'playing'
NN -> 'plea'
NN -> 'pledge'
NN -> 'plenty'
NN -> 'plot'
NN -> 'plunge'
NN -> 'point'
NN -> 'poison'
NN -> 'police'
NN -> 'policy'
NN -> 'poll'
NN -> 'pollution'
NN -> 'polyethylene'
NN -> 'pool'
NN -> 'popularity'
NN -> 'population'
NN -> 'portfolio'
NN -> 'portion'
NN -> 'portrait'
NN -> 'position'
NN -> 'possibility'
NN -> 'post'
NN -> 'potential'
NN -> 'pound'
NN -> 'poverty'
NN -> 'power'
NN -> 'practice'
NN -> 'preamble'
NN -> 'predecessor'
NN -> 'preference'
NN -> 'prelude'
NN -> 'premium'
NN -> 'prescription'
NN -> 'presence'
NN -> 'presidency'
NN -> 'president'
NN -> 'press'
NN -> 'pressure'
NN -> 'pretax'
NN -> 'price'
NN -> 'pricing'
NN -> 'pride'
NN -> 'primetime'
NN -> 'principal'
NN -> 'principle'
NN -> 'print'
NN -> 'printer'
NN -> 'printing'
NN -> 'priority'
NN -> 'prison'
NN -> 'privatization'
NN -> 'privilege'
NN -> 'probe'
NN -> 'problem'
NN -> 'procedure'
NN -> 'process'
NN -> 'processing'
NN -> 'producer'
NN -> 'product'
NN -> 'production'
NN -> 'productivity'
NN -> 'professor'
NN -> 'profit'
NN -> 'profittaking'
NN -> 'profitability'
NN -> 'program'
NN -> 'programtrading'
NN -> 'programming'
NN -> 'progress'
NN -> 'project'
NN -> 'projection'
NN -> 'promise'
NN -> 'promotion'
NN -> 'proof'
NN -> 'property'
NN -> 'proportion'
NN -> 'proposal'
NN -> 'prosecution'
NN -> 'prosecutor'
NN -> 'prospect'
NN -> 'prospectus'
NN -> 'prosperity'
NN -> 'protection'
NN -> 'protein'
NN -> 'protest'
NN -> 'province'
NN -> 'provision'
NN -> 'proxy'
NN -> 'psychology'
NN -> 'psyllium'
NN -> 'public'
NN -> 'publication'
NN -> 'publicity'
NN -> 'publisher'
NN -> 'publishing'
NN -> 'pulp'
NN -> 'purchase'
NN -> 'purchasing'
NN -> 'purpose'
NN -> 'push'
NN -> 'put'
NN -> 'quake'
NN -> 'quality'
NN -> 'quarter'
NN -> 'quarterly'
NN -> 'question'
NN -> 'quota'
NN -> 'race'
NN -> 'racketeering'
NN -> 'radar'
NN -> 'radio'
NN -> 'raider'
NN -> 'rail'
NN -> 'railroad'
NN -> 'rain'
NN -> 'raise'
NN -> 'rally'
NN -> 'ranch'
NN -> 'range'
NN -> 'rash'
NN -> 'rate'
NN -> 'rating'
NN -> 'ratio'
NN -> 'reelection'
NN -> 'reaction'
NN -> 'reader'
NN -> 'reading'
NN -> 'realestate'
NN -> 'reality'
NN -> 'reason'
NN -> 'rebound'
NN -> 'recapitalization'
NN -> 'recession'
NN -> 'recognition'
NN -> 'recommendation'
NN -> 'reconciliation'
NN -> 'record'
NN -> 'recording'
NN -> 'recovery'
NN -> 'red'
NN -> 'redemption'
NN -> 'reduction'
NN -> 'reference'
NN -> 'refinery'
NN -> 'reform'
NN -> 'refund'
NN -> 'regime'
NN -> 'region'
NN -> 'registration'
NN -> 'regulation'
NN -> 'regulator'
NN -> 'reinforcement'
NN -> 'reinsurance'
NN -> 'rejection'
NN -> 'relationship'
NN -> 'release'
NN -> 'reliance'
NN -> 'relief'
NN -> 'reluctance'
NN -> 'remainder'
NN -> 'reminder'
NN -> 'removal'
NN -> 'renewal'
NN -> 'rent'
NN -> 'reorganization'
NN -> 'repair'
NN -> 'repeal'
NN -> 'replacement'
NN -> 'report'
NN -> 'reporter'
NN -> 'reporting'
NN -> 'representative'
NN -> 'repurchase'
NN -> 'reputation'
NN -> 'request'
NN -> 'requirement'
NN -> 'rescue'
NN -> 'research'
NN -> 'researcher'
NN -> 'reserve'
NN -> 'resignation'
NN -> 'resistance'
NN -> 'resolution'
NN -> 'resort'
NN -> 'respect'
NN -> 'response'
NN -> 'responsibility'
NN -> 'rest'
NN -> 'restaurant'
NN -> 'restraint'
NN -> 'restructuring'
NN -> 'result'
NN -> 'retailer'
NN -> 'retailing'
NN -> 'retirement'
NN -> 'retreat'
NN -> 'return'
NN -> 'revenue'
NN -> 'reversal'
NN -> 'review'
NN -> 'revision'
NN -> 'revival'
NN -> 'revolution'
NN -> 'rhetoric'
NN -> 'ride'
NN -> 'right'
NN -> 'ring'
NN -> 'rise'
NN -> 'risk'
NN -> 'rival'
NN -> 'road'
NN -> 'role'
NN -> 'roll'
NN -> 'room'
NN -> 'round'
NN -> 'rout'
NN -> 'route'
NN -> 'row'
NN -> 'rubble'
NN -> 'ruble'
NN -> 'rule'
NN -> 'ruling'
NN -> 'run'
NN -> 'runup'
NN -> 'rush'
NN -> 'safety'
NN -> 'salary'
NN -> 'sale'
NN -> 'salesman'
NN -> 'salmonella'
NN -> 'sand'
NN -> 'satellite'
NN -> 'satisfaction'
NN -> 'scale'
NN -> 'scandal'
NN -> 'scenario'
NN -> 'scene'
NN -> 'schedule'
NN -> 'scheme'
NN -> 'school'
NN -> 'science'
NN -> 'scientist'
NN -> 'screen'
NN -> 'sea'
NN -> 'search'
NN -> 'season'
NN -> 'seat'
NN -> 'second'
NN -> 'secretary'
NN -> 'section'
NN -> 'sector'
NN -> 'security'
NN -> 'sedan'
NN -> 'seed'
NN -> 'segment'
NN -> 'selfincrimination'
NN -> 'sell'
NN -> 'selloff'
NN -> 'seller'
NN -> 'selling'
NN -> 'semiconductor'
NN -> 'senator'
NN -> 'sense'
NN -> 'sentence'
NN -> 'sentiment'
NN -> 'series'
NN -> 'service'
NN -> 'session'
NN -> 'set'
NN -> 'setback'
NN -> 'settlement'
NN -> 'sex'
NN -> 'shadow'
NN -> 'shame'
NN -> 'shape'
NN -> 'share'
NN -> 'shareholder'
NN -> 'sheet'
NN -> 'shelf'
NN -> 'shield'
NN -> 'shift'
NN -> 'ship'
NN -> 'shipping'
NN -> 'shipyard'
NN -> 'shock'
NN -> 'shop'
NN -> 'shopping'
NN -> 'shortage'
NN -> 'shot'
NN -> 'shoulder'
NN -> 'show'
NN -> 'showing'
NN -> 'shuttle'
NN -> 'side'
NN -> 'sight'
NN -> 'sign'
NN -> 'signal'
NN -> 'significance'
NN -> 'silver'
NN -> 'singer'
NN -> 'site'
NN -> 'situation'
NN -> 'size'
NN -> 'ski'
NN -> 'slate'
NN -> 'slide'
NN -> 'slowdown'
NN -> 'slowing'
NN -> 'slump'
NN -> 'smallbusiness'
NN -> 'smoking'
NN -> 'socialism'
NN -> 'society'
NN -> 'softdrink'
NN -> 'software'
NN -> 'soil'
NN -> 'solution'
NN -> 'somebody'
NN -> 'someone'
NN -> 'something'
NN -> 'son'
NN -> 'sort'
NN -> 'source'
NN -> 'soybean'
NN -> 'space'
NN -> 'spacecraft'
NN -> 'speaker'
NN -> 'specialist'
NN -> 'specialty'
NN -> 'speculation'
NN -> 'speech'
NN -> 'speed'
NN -> 'spending'
NN -> 'spill'
NN -> 'spinoff'
NN -> 'spirit'
NN -> 'spite'
NN -> 'split'
NN -> 'spokesman'
NN -> 'spokeswoman'
NN -> 'sponsor'
NN -> 'sport'
NN -> 'spot'
NN -> 'spread'
NN -> 'spree'
NN -> 'spring'
NN -> 'spy'
NN -> 'square'
NN -> 'squeeze'
NN -> 'stability'
NN -> 'stadium'
NN -> 'staff'
NN -> 'stage'
NN -> 'stake'
NN -> 'stance'
NN -> 'stand'
NN -> 'standard'
NN -> 'standing'
NN -> 'standpoint'
NN -> 'star'
NN -> 'start'
NN -> 'state'
NN -> 'statement'
NN -> 'station'
NN -> 'status'
NN -> 'statute'
NN -> 'steel'
NN -> 'steelmaker'
NN -> 'step'
NN -> 'sterling'
NN -> 'stock'
NN -> 'stockindex'
NN -> 'stockmarket'
NN -> 'stop'
NN -> 'storage'
NN -> 'store'
NN -> 'storm'
NN -> 'story'
NN -> 'strain'
NN -> 'strategist'
NN -> 'strategy'
NN -> 'stream'
NN -> 'street'
NN -> 'strength'
NN -> 'stress'
NN -> 'stretch'
NN -> 'strike'
NN -> 'string'
NN -> 'strip'
NN -> 'structure'
NN -> 'struggle'
NN -> 'student'
NN -> 'studio'
NN -> 'study'
NN -> 'stuff'
NN -> 'style'
NN -> 'subcommittee'
NN -> 'subject'
NN -> 'subsidiary'
NN -> 'substance'
NN -> 'substitute'
NN -> 'suburb'
NN -> 'success'
NN -> 'successor'
NN -> 'sugar'
NN -> 'suggestion'
NN -> 'suit'
NN -> 'suitor'
NN -> 'sum'
NN -> 'summer'
NN -> 'summit'
NN -> 'sun'
NN -> 'supercomputer'
NN -> 'supermarket'
NN -> 'supplier'
NN -> 'supply'
NN -> 'support'
NN -> 'surface'
NN -> 'surge'
NN -> 'surgery'
NN -> 'surplus'
NN -> 'surprise'
NN -> 'survey'
NN -> 'survival'
NN -> 'suspension'
NN -> 'swap'
NN -> 'sweep'
NN -> 'swing'
NN -> 'symbol'
NN -> 'syndicate'
NN -> 'syndrome'
NN -> 'system'
NN -> 'table'
NN -> 'takeover'
NN -> 'talent'
NN -> 'talk'
NN -> 'tape'
NN -> 'target'
NN -> 'tariff'
NN -> 'task'
NN -> 'taste'
NN -> 'tax'
NN -> 'tea'
NN -> 'teacher'
NN -> 'team'
NN -> 'technique'
NN -> 'technology'
NN -> 'telecommunications'
NN -> 'telephone'
NN -> 'television'
NN -> 'temptation'
NN -> 'tendency'
NN -> 'tender'
NN -> 'tension'
NN -> 'tenure'
NN -> 'term'
NN -> 'terminal'
NN -> 'territory'
NN -> 'terrorism'
NN -> 'test'
NN -> 'testimony'
NN -> 'testing'
NN -> 'textile'
NN -> 'theater'
NN -> 'theft'
NN -> 'theme'
NN -> 'theory'
NN -> 'therapy'
NN -> 'thing'
NN -> 'third'
NN -> 'thirdquarter'
NN -> 'thought'
NN -> 'threat'
NN -> 'thrift'
NN -> 'thumb'
NN -> 'ticket'
NN -> 'time'
NN -> 'timetable'
NN -> 'timing'
NN -> 'tip'
NN -> 'title'
NN -> 'tobacco'
NN -> 'today'
NN -> 'tolerance'
NN -> 'toll'
NN -> 'tomorrow'
NN -> 'ton'
NN -> 'tone'
NN -> 'tonight'
NN -> 'tool'
NN -> 'top'
NN -> 'topic'
NN -> 'total'
NN -> 'touch'
NN -> 'tour'
NN -> 'tourism'
NN -> 'tourist'
NN -> 'tower'
NN -> 'town'
NN -> 'toxin'
NN -> 'toy'
NN -> 'track'
NN -> 'trade'
NN -> 'trader'
NN -> 'trading'
NN -> 'tradition'
NN -> 'traffic'
NN -> 'trail'
NN -> 'train'
NN -> 'training'
NN -> 'transaction'
NN -> 'transfer'
NN -> 'transition'
NN -> 'transport'
NN -> 'transportation'
NN -> 'travel'
NN -> 'treasurer'
NN -> 'treasury'
NN -> 'treatment'
NN -> 'treaty'
NN -> 'tree'
NN -> 'trend'
NN -> 'trial'
NN -> 'trip'
NN -> 'troop'
NN -> 'trouble'
NN -> 'trough'
NN -> 'truck'
NN -> 'trust'
NN -> 'trustee'
NN -> 'truth'
NN -> 'tube'
NN -> 'turmoil'
NN -> 'turn'
NN -> 'turnaround'
NN -> 'turnover'
NN -> 'tv'
NN -> 'type'
NN -> 'uncertainty'
NN -> 'underwriter'
NN -> 'underwriting'
NN -> 'unemployment'
NN -> 'union'
NN -> 'unit'
NN -> 'university'
NN -> 'upscale'
NN -> 'uptick'
NN -> 'use'
NN -> 'user'
NN -> 'utility'
NN -> 'utilization'
NN -> 'vacancy'
NN -> 'vaccine'
NN -> 'valuation'
NN -> 'value'
NN -> 'variety'
NN -> 'vehicle'
NN -> 'venture'
NN -> 'verdict'
NN -> 'version'
NN -> 'veteran'
NN -> 'veto'
NN -> 'vice'
NN -> 'victim'
NN -> 'victory'
NN -> 'video'
NN -> 'view'
NN -> 'violation'
NN -> 'virus'
NN -> 'vision'
NN -> 'visit'
NN -> 'voice'
NN -> 'volatility'
NN -> 'volume'
NN -> 'vote'
NN -> 'voting'
NN -> 'wage'
NN -> 'waiver'
NN -> 'wake'
NN -> 'wall'
NN -> 'war'
NN -> 'warming'
NN -> 'warning'
NN -> 'warrant'
NN -> 'waste'
NN -> 'watch'
NN -> 'water'
NN -> 'waterworks'
NN -> 'wave'
NN -> 'way'
NN -> 'weakness'
NN -> 'wealth'
NN -> 'weapon'
NN -> 'weather'
NN -> 'week'
NN -> 'weekend'
NN -> 'weight'
NN -> 'well'
NN -> 'wheat'
NN -> 'while'
NN -> 'whole'
NN -> 'wife'
NN -> 'will'
NN -> 'willingness'
NN -> 'wind'
NN -> 'window'
NN -> 'wine'
NN -> 'winner'
NN -> 'winter'
NN -> 'wire'
NN -> 'wisdom'
NN -> 'withdrawal'
NN -> 'witness'
NN -> 'woman'
NN -> 'word'
NN -> 'work'
NN -> 'worker'
NN -> 'world'
NN -> 'worm'
NN -> 'worth'
NN -> 'writedown'
NN -> 'writeoff'
NN -> 'writer'
NN -> 'year'
NN -> 'yearend'
NN -> 'yeast'
NN -> 'yen'
NN -> 'yesterday'
NN -> 'yield'
NN -> 'youth'
VBD -> "'d"
VBD -> 'abandoned'
VBD -> 'accepted'
VBD -> 'accounted'
VBD -> 'accused'
VBD -> 'acknowledged'
VBD -> 'acquired'
VBD -> 'acted'
VBD -> 'added'
VBD -> 'adopted'
VBD -> 'advanced'
VBD -> 'affected'
VBD -> 'agreed'
VBD -> 'alleged'
VBD -> 'allowed'
VBD -> 'amended'
VBD -> 'amounted'
VBD -> 'announced'
VBD -> 'appealed'
VBD -> 'appeared'
VBD -> 'approved'
VBD -> 'argued'
VBD -> 'arose'
VBD -> 'arrived'
VBD -> 'asked'
VBD -> 'asserted'
VBD -> 'assumed'
VBD -> 'attended'
VBD -> 'attracted'
VBD -> 'attributed'
VBD -> 'authorized'
VBD -> 'averaged'
VBD -> 'awarded'
VBD -> 'backed'
VBD -> 'became'
VBD -> 'began'
VBD -> 'believed'
VBD -> 'blamed'
VBD -> 'boosted'
VBD -> 'bought'
VBD -> 'broke'
VBD -> 'brought'
VBD -> 'built'
VBD -> 'called'
VBD -> 'came'
VBD -> 'capped'
VBD -> 'carried'
VBD -> 'caught'
VBD -> 'caused'
VBD -> 'changed'
VBD -> 'charged'
VBD -> 'chose'
VBD -> 'cited'
VBD -> 'claimed'
VBD -> 'cleared'
VBD -> 'climbed'
VBD -> 'closed'
VBD -> 'collapsed'
VBD -> 'compared'
VBD -> 'complained'
VBD -> 'completed'
VBD -> 'conceded'
VBD -> 'concluded'
VBD -> 'confirmed'
VBD -> 'considered'
VBD -> 'contained'
VBD -> 'contended'
VBD -> 'continued'
VBD -> 'contracted'
VBD -> 'contributed'
VBD -> 'convicted'
VBD -> 'cost'
VBD -> 'created'
VBD -> 'cut'
VBD -> 'decided'
VBD -> 'declared'
VBD -> 'declined'
VBD -> 'defended'
VBD -> 'demanded'
VBD -> 'denied'
VBD -> 'described'
VBD -> 'determined'
VBD -> 'developed'
VBD -> 'did'
VBD -> 'died'
VBD -> 'disclosed'
VBD -> 'discovered'
VBD -> 'dismissed'
VBD -> 'dominated'
VBD -> 'doubled'
VBD -> 'drew'
VBD -> 'dropped'
VBD -> 'drove'
VBD -> 'dumped'
VBD -> 'earned'
VBD -> 'eased'
VBD -> 'edged'
VBD -> 'elected'
VBD -> 'emerged'
VBD -> 'ended'
VBD -> 'endorsed'
VBD -> 'entered'
VBD -> 'estimated'
VBD -> 'exceeded'
VBD -> 'expected'
VBD -> 'expired'
VBD -> 'explained'
VBD -> 'exploded'
VBD -> 'expressed'
VBD -> 'extended'
VBD -> 'failed'
VBD -> 'fared'
VBD -> 'feared'
VBD -> 'fell'
VBD -> 'felt'
VBD -> 'figured'
VBD -> 'filed'
VBD -> 'finished'
VBD -> 'fired'
VBD -> 'fled'
VBD -> 'flew'
VBD -> 'followed'
VBD -> 'forced'
VBD -> 'found'
VBD -> 'fueled'
VBD -> 'gained'
VBD -> 'gave'
VBD -> 'generated'
VBD -> 'got'
VBD -> 'grew'
VBD -> 'had'
VBD -> 'halted'
VBD -> 'handled'
VBD -> 'happened'
VBD -> 'heard'
VBD -> 'held'
VBD -> 'helped'
VBD -> 'hinted'
VBD -> 'hired'
VBD -> 'hit'
VBD -> 'hoped'
VBD -> 'hurt'
VBD -> 'imposed'
VBD -> 'improved'
VBD -> 'inched'
VBD -> 'included'
VBD -> 'increased'
VBD -> 'indicated'
VBD -> 'insisted'
VBD -> 'intended'
VBD -> 'introduced'
VBD -> 'invested'
VBD -> 'issued'
VBD -> 'joined'
VBD -> 'jumped'
VBD -> 'kept'
VBD -> 'kicked'
VBD -> 'killed'
VBD -> 'knew'
VBD -> 'landed'
VBD -> 'launched'
VBD -> 'learned'
VBD -> 'led'
VBD -> 'left'
VBD -> 'let'
VBD -> 'lived'
VBD -> 'looked'
VBD -> 'lost'
VBD -> 'loved'
VBD -> 'lowered'
VBD -> 'made'
VBD -> 'managed'
VBD -> 'marked'
VBD -> 'meant'
VBD -> 'met'
VBD -> 'missed'
VBD -> 'moved'
VBD -> 'named'
VBD -> 'narrowed'
VBD -> 'needed'
VBD -> 'noted'
VBD -> 'observed'
VBD -> 'occurred'
VBD -> 'offered'
VBD -> 'opened'
VBD -> 'opposed'
VBD -> 'ordered'
VBD -> 'outnumbered'
VBD -> 'outpaced'
VBD -> 'owned'
VBD -> 'paid'
VBD -> 'passed'
VBD -> 'picked'
VBD -> 'placed'
VBD -> 'planned'
VBD -> 'played'
VBD -> 'pleaded'
VBD -> 'pledged'
VBD -> 'plummeted'
VBD -> 'plunged'
VBD -> 'pointed'
VBD -> 'posted'
VBD -> 'postponed'
VBD -> 'praised'
VBD -> 'predicted'
VBD -> 'preferred'
VBD -> 'presented'
VBD -> 'prevailed'
VBD -> 'prevented'
VBD -> 'produced'
VBD -> 'projected'
VBD -> 'promised'
VBD -> 'prompted'
VBD -> 'proposed'
VBD -> 'proved'
VBD -> 'provided'
VBD -> 'pulled'
VBD -> 'purchased'
VBD -> 'pushed'
VBD -> 'put'
VBD -> 'questioned'
VBD -> 'quit'
VBD -> 'raised'
VBD -> 'rallied'
VBD -> 'ran'
VBD -> 'ranged'
VBD -> 'reached'
VBD -> 'reacted'
VBD -> 'read'
VBD -> 'realized'
VBD -> 'rebounded'
VBD -> 'recalled'
VBD -> 'received'
VBD -> 'recommended'
VBD -> 'recorded'
VBD -> 'recovered'
VBD -> 'reduced'
VBD -> 'referred'
VBD -> 'reflected'
VBD -> 'refused'
VBD -> 'rejected'
VBD -> 'released'
VBD -> 'remained'
VBD -> 'replaced'
VBD -> 'replied'
VBD -> 'reported'
VBD -> 'represented'
VBD -> 'requested'
VBD -> 'required'
VBD -> 'resigned'
VBD -> 'responded'
VBD -> 'resulted'
VBD -> 'retained'
VBD -> 'retired'
VBD -> 'returned'
VBD -> 'rolled'
VBD -> 'rose'
VBD -> 'ruled'
VBD -> 'rushed'
VBD -> 'said'
VBD -> 'sank'
VBD -> 'sat'
VBD -> 'saw'
VBD -> 'scrambled'
VBD -> 'seemed'
VBD -> 'sent'
VBD -> 'served'
VBD -> 'set'
VBD -> 'settled'
VBD -> 'shed'
VBD -> 'shot'
VBD -> 'shouted'
VBD -> 'showed'
VBD -> 'signaled'
VBD -> 'signed'
VBD -> 'skidded'
VBD -> 'slid'
VBD -> 'slipped'
VBD -> 'snapped'
VBD -> 'soared'
VBD -> 'sold'
VBD -> 'sought'
VBD -> 'sparked'
VBD -> 'speculated'
VBD -> 'spent'
VBD -> 'spread'
VBD -> 'staged'
VBD -> 'started'
VBD -> 'stated'
VBD -> 'stayed'
VBD -> 'stemmed'
VBD -> 'stepped'
VBD -> 'stood'
VBD -> 'stopped'
VBD -> 'stressed'
VBD -> 'struck'
VBD -> 'stuck'
VBD -> 'succeeded'
VBD -> 'sued'
VBD -> 'suffered'
VBD -> 'suggested'
VBD -> 'supported'
VBD -> 'surfaced'
VBD -> 'surged'
VBD -> 'surprised'
VBD -> 'suspended'
VBD -> 'sustained'
VBD -> 'switched'
VBD -> 'talked'
VBD -> 'taught'
VBD -> 'termed'
VBD -> 'terminated'
VBD -> 'testified'
VBD -> 'thought'
VBD -> 'threatened'
VBD -> 'threw'
VBD -> 'told'
VBD -> 'took'
VBD -> 'topped'
VBD -> 'totaled'
VBD -> 'traded'
VBD -> 'tried'
VBD -> 'triggered'
VBD -> 'trimmed'
VBD -> 'tumbled'
VBD -> 'turned'
VBD -> 'unveiled'
VBD -> 'upheld'
VBD -> 'urged'
VBD -> 'used'
VBD -> 'valued'
VBD -> 'viewed'
VBD -> 'violated'
VBD -> 'visited'
VBD -> 'voted'
VBD -> 'vowed'
VBD -> 'waited'
VBD -> 'wanted'
VBD -> 'warned'
VBD -> 'was'
VBD -> 'watched'
VBD -> 'weakened'
VBD -> 'weighed'
VBD -> 'welcomed'
VBD -> 'went'
VBD -> 'were'
VBD -> 'withdrew'
VBD -> 'won'
VBD -> 'worked'
VBD -> 'wrote'
DT -> 'All'
DT -> 'An'
DT -> 'Every'
DT -> 'No'
DT -> 'Some'
DT -> 'That'
DT -> 'The'
DT -> 'These'
DT -> 'This'
DT -> 'Those'
DT -> 'a'
DT -> 'all'
DT -> 'an'
DT -> 'another'
DT -> 'any'
DT -> 'both'
DT -> 'each'
DT -> 'either'
DT -> 'every'
DT -> 'half'
DT -> 'many'
DT -> 'neither'
DT -> 'no'
DT -> 'some'
DT -> 'that'
DT -> 'the'
DT -> 'these'
DT -> 'this'
DT -> 'those'
ADVPTMP -> ADVP PP
ADVPTMP -> ADVP SBAR
ADVPTMP -> DT RB
ADVPTMP -> DT RBR
ADVPTMP -> IN
ADVPTMP -> IN RB
ADVPTMP -> JJ
ADVPTMP -> NP IN
ADVPTMP -> NP JJR
ADVPTMP -> NP RB
ADVPTMP -> NP RBR
ADVPTMP -> RB
ADVPTMP -> RB NP
ADVPTMP -> RB PP
ADVPTMP -> RB RB
ADVPTMP -> RB RBR
ADVPTMP -> RB SBAR
ADVPTMP -> RBR
ADVPTMP -> RBR NP
ADVPTMP -> RBR PP
ADVPTMP -> RBR RB
SBARLOCPRD -> WHADVP S
COMMA -> ','
IN -> 'After'
IN -> 'As'
IN -> 'At'
IN -> 'Before'
IN -> 'By'
IN -> 'During'
IN -> 'For'
IN -> 'From'
IN -> 'If'
IN -> 'In'
IN -> 'Of'
IN -> 'On'
IN -> 'Unless'
IN -> 'While'
IN -> 'With'
IN -> 'Without'
IN -> 'aboard'
IN -> 'about'
IN -> 'above'
IN -> 'across'
IN -> 'after'
IN -> 'against'
IN -> 'ago'
IN -> 'along'
IN -> 'although'
IN -> 'amid'
IN -> 'among'
IN -> 'around'
IN -> 'as'
IN -> 'at'
IN -> 'because'
IN -> 'before'
IN -> 'behind'
IN -> 'below'
IN -> 'beneath'
IN -> 'besides'
IN -> 'between'
IN -> 'beyond'
IN -> 'by'
IN -> 'de'
IN -> 'despite'
IN -> 'down'
IN -> 'during'
IN -> 'except'
IN -> 'for'
IN -> 'from'
IN -> 'if'
IN -> 'in'
IN -> 'inside'
IN -> 'into'
IN -> 'like'
IN -> 'near'
IN -> 'next'
IN -> 'of'
IN -> 'off'
IN -> 'on'
IN -> 'once'
IN -> 'onto'
IN -> 'out'
IN -> 'outside'
IN -> 'over'
IN -> 'past'
IN -> 'per'
IN -> 'plus'
IN -> 'since'
IN -> 'so'
IN -> 'than'
IN -> 'that'
IN -> 'though'
IN -> 'through'
IN -> 'throughout'
IN -> 'toward'
IN -> 'under'
IN -> 'unless'
IN -> 'unlike'
IN -> 'until'
IN -> 'up'
IN -> 'upon'
IN -> 'via'
IN -> 'vspoint'
IN -> 'whether'
IN -> 'while'
IN -> 'with'
IN -> 'within'
IN -> 'without'
PPLOC -> IN NP
PPLOC -> IN NPdollar
PPLOC -> IN PP
PPLOC -> IN SNOM
PPLOC -> IN SBARNOM
PPLOC -> TO NP
ROOT -> S
WPdollar -> 'whose'
SYM -> STAR
SYM -> 'STARSTAR'
SYM -> 'a'
SYM -> 'b'
RRC -> ADVPTMP NP
RRC -> ADVPTMP PPLOC
S0 -> PUNCLRB NP
S1 -> S0 PUNCRRB
S -> S1 VP
S2 -> PUNCLRB NP
S3 -> S2 VP
S -> S3 PUNCpoint
S4 -> PUNCLRB NP
S5 -> S4 VP
S6 -> S5 PUNCpoint
S -> S6 PUNCRRB
S7 -> PUNCLRB PPTMP
S8 -> S7 COMMA
S9 -> S8 NP
S10 -> S9 VP
S11 -> S10 PUNCpoint
S -> S11 PUNCRRB
S12 -> COMMA PP
S13 -> S12 COMMA
S -> S13 VP
S14 -> PUNCbquotebquote NPPRD
S -> S14 PUNCquotequote
S15 -> PUNCcolon NP
S16 -> S15 VP
S -> S16 PUNCpoint
S17 -> PUNCcolon SBARADV
S18 -> S17 COMMA
S19 -> S18 NP
S20 -> S19 VP
S -> S20 PUNCpoint
S21 -> ADJP COMMA
S22 -> S21 NP
S23 -> S22 VP
S -> S23 PUNCpoint
S24 -> ADVP COMMA
S25 -> S24 NP
S26 -> S25 ADVP
S27 -> S26 VP
S -> S27 PUNCpoint
S28 -> ADVP COMMA
S29 -> S28 NP
S30 -> S29 ADVPTMP
S31 -> S30 VP
S -> S31 PUNCpoint
S32 -> ADVP COMMA
S33 -> S32 NP
S -> S33 VP
S34 -> ADVP COMMA
S35 -> S34 NP
S36 -> S35 VP
S -> S36 PUNCpoint
S37 -> ADVP COMMA
S38 -> S37 NP
S39 -> S38 VP
S40 -> S39 PUNCpoint
S -> S40 PUNCquotequote
S41 -> ADVP COMMA
S42 -> S41 PP
S43 -> S42 COMMA
S44 -> S43 NP
S45 -> S44 VP
S -> S45 PUNCpoint
S46 -> ADVP COMMA
S47 -> S46 PPLOC
S48 -> S47 COMMA
S49 -> S48 NP
S50 -> S49 VP
S -> S50 PUNCpoint
S51 -> ADVP COMMA
S52 -> S51 SBARTMP
S53 -> S52 COMMA
S54 -> S53 NP
S55 -> S54 VP
S -> S55 PUNCpoint
S56 -> ADVP NP
S -> S56 VP
S57 -> ADVP NP
S58 -> S57 VP
S -> S58 PUNCpoint
S59 -> ADVP PRN
S60 -> S59 NP
S61 -> S60 VP
S -> S61 PUNCpoint
S62 -> ADVPLOC COMMA
S63 -> S62 NP
S64 -> S63 VP
S -> S64 PUNCpoint
S65 -> ADVPLOC NP
S66 -> S65 VP
S -> S66 PUNCpoint
S67 -> ADVPTMP COMMA
S68 -> S67 ADVP
S69 -> S68 COMMA
S70 -> S69 NP
S71 -> S70 VP
S -> S71 PUNCpoint
S72 -> ADVPTMP COMMA
S73 -> S72 NP
S74 -> S73 ADVP
S75 -> S74 VP
S -> S75 PUNCpoint
S76 -> ADVPTMP COMMA
S77 -> S76 NP
S -> S77 VP
S78 -> ADVPTMP COMMA
S79 -> S78 NP
S80 -> S79 VP
S -> S80 PUNCpoint
S81 -> ADVPTMP COMMA
S82 -> S81 NP
S83 -> S82 VP
S84 -> S83 PUNCpoint
S -> S84 PUNCquotequote
S85 -> ADVPTMP COMMA
S86 -> S85 PP
S87 -> S86 COMMA
S88 -> S87 NP
S89 -> S88 VP
S -> S89 PUNCpoint
S90 -> ADVPTMP COMMA
S91 -> S90 PPTMP
S92 -> S91 COMMA
S93 -> S92 NP
S94 -> S93 VP
S -> S94 PUNCpoint
S95 -> ADVPTMP NP
S -> S95 VP
S96 -> ADVPTMP NP
S97 -> S96 VP
S -> S97 PUNCpoint
S98 -> ADVPTMP NP
S99 -> S98 VP
S100 -> S99 PUNCpoint
S -> S100 PUNCquotequote
S101 -> ADVPTMP PRN
S102 -> S101 NP
S103 -> S102 VP
S -> S103 PUNCpoint
S104 -> IN NP
S105 -> S104 VP
S -> S105 PUNCpoint
S106 -> INTJ COMMA
S107 -> S106 NP
S108 -> S107 VP
S -> S108 PUNCpoint
S109 -> LST VP
S -> S109 PUNCpoint
S110 -> NP COMMA
S111 -> S110 ADVP
S112 -> S111 COMMA
S -> S112 VP
S113 -> NP COMMA
S114 -> S113 ADVP
S115 -> S114 COMMA
S116 -> S115 VP
S -> S116 PUNCpoint
S117 -> NP COMMA
S118 -> S117 ADVPTMP
S119 -> S118 COMMA
S120 -> S119 VP
S -> S120 PUNCpoint
S121 -> NP COMMA
S122 -> S121 NP
S123 -> S122 VP
S -> S123 PUNCpoint
S124 -> NP COMMA
S125 -> S124 PP
S126 -> S125 COMMA
S -> S126 VP
S127 -> NP COMMA
S128 -> S127 PP
S129 -> S128 COMMA
S130 -> S129 VP
S -> S130 PUNCpoint
S131 -> NP COMMA
S132 -> S131 PPLOC
S133 -> S132 COMMA
S134 -> S133 VP
S -> S134 PUNCpoint
S135 -> NP COMMA
S136 -> S135 PPTMP
S137 -> S136 COMMA
S138 -> S137 VP
S -> S138 PUNCpoint
S139 -> NP COMMA
S140 -> S139 SADV
S141 -> S140 COMMA
S -> S141 VP
S142 -> NP COMMA
S143 -> S142 SADV
S144 -> S143 COMMA
S145 -> S144 VP
S -> S145 PUNCpoint
S146 -> NP COMMA
S147 -> S146 SBARADV
S148 -> S147 COMMA
S -> S148 VP
S149 -> NP COMMA
S150 -> S149 SBARADV
S151 -> S150 COMMA
S152 -> S151 VP
S -> S152 PUNCpoint
S153 -> NP COMMA
S -> S153 VP
S154 -> NP COMMA
S155 -> S154 VP
S -> S155 PUNCpoint
S156 -> NP ADJPPRD
S -> S156 S
S157 -> NP ADJPPRD
S -> S157 SBAR
S158 -> NP ADVP
S -> S158 VP
S159 -> NP ADVP
S160 -> S159 VP
S -> S160 PUNCpoint
S161 -> NP ADVP
S162 -> S161 VP
S163 -> S162 PUNCpoint
S -> S163 PUNCquotequote
S164 -> NP ADVPTMP
S -> S164 VP
S165 -> NP ADVPTMP
S166 -> S165 VP
S -> S166 PUNCpoint
S167 -> NP ADVPTMP
S168 -> S167 VP
S169 -> S168 PUNCpoint
S -> S169 PUNCquotequote
S170 -> NP NP
S171 -> S170 VP
S -> S171 PUNCpoint
S172 -> NP NPTMP
S -> S172 VP
S173 -> NP NPTMP
S174 -> S173 VP
S -> S174 PUNCpoint
S175 -> NP PP
S176 -> S175 VP
S -> S176 PUNCpoint
S177 -> NP PPLOC
S178 -> S177 VP
S -> S178 PUNCpoint
S179 -> NP PPTMP
S -> S179 VP
S180 -> NP PPTMP
S181 -> S180 VP
S -> S181 PUNCpoint
S182 -> NP PRN
S -> S182 VP
S183 -> NP PRN
S184 -> S183 VP
S -> S184 PUNCpoint
S185 -> NP PRN
S186 -> S185 VP
S187 -> S186 PUNCpoint
S -> S187 PUNCquotequote
S188 -> NP PRN
S189 -> S188 PUNCbquotebquote
S190 -> S189 VP
S -> S190 PUNCpoint
S191 -> NP PRN
S192 -> S191 PUNCbquotebquote
S193 -> S192 VP
S194 -> S193 PUNCpoint
S -> S194 PUNCquotequote
S195 -> NP VP
S -> S195 PUNCpoint
S196 -> NP VP
S197 -> S196 PUNCpoint
S -> S197 PUNCquotequote
S198 -> NP VP
S199 -> S198 PUNCpoint
S200 -> S199 PUNCquotequote
S -> S200 PUNCquotequote
S201 -> NP VP
S202 -> S201 PUNCpoint
S -> S202 PUNCRRB
S203 -> NP VP
S -> S203 PUNCcolon
S204 -> NP VP
S205 -> S204 PUNCcolon
S -> S205 PUNCpoint
S206 -> NP VP
S -> S206 PP
S207 -> NP PUNCbquotebquote
S -> S207 ADJPPRD
S208 -> NP PUNCbquotebquote
S -> S208 NPPRD
S209 -> NP PUNCbquotebquote
S -> S209 VP
S210 -> NP PUNCbquotebquote
S211 -> S210 VP
S -> S211 PUNCpoint
S212 -> NPdollar VP
S -> S212 PUNCpoint
S213 -> NPADV COMMA
S214 -> S213 NP
S215 -> S214 VP
S -> S215 PUNCpoint
S216 -> NPTMP COMMA
S217 -> S216 NP
S -> S217 VP
S218 -> NPTMP COMMA
S219 -> S218 NP
S220 -> S219 VP
S -> S220 PUNCpoint
S221 -> NPTMP COMMA
S222 -> S221 NP
S223 -> S222 VP
S224 -> S223 PUNCpoint
S -> S224 PUNCquotequote
S225 -> NPTMP COMMA
S226 -> S225 PPLOC
S227 -> S226 COMMA
S228 -> S227 NP
S229 -> S228 VP
S -> S229 PUNCpoint
S230 -> NPTMP COMMA
S231 -> S230 SBARTMP
S232 -> S231 COMMA
S233 -> S232 NP
S234 -> S233 VP
S -> S234 PUNCpoint
S235 -> NPTMP NP
S -> S235 VP
S236 -> NPTMP NP
S237 -> S236 VP
S -> S237 PUNCpoint
S238 -> NPR VP
S -> S238 PUNCpoint
S239 -> PP COMMA
S -> S239 VP
S240 -> PP COMMA
S241 -> S240 ADVP
S242 -> S241 COMMA
S243 -> S242 NP
S244 -> S243 VP
S -> S244 PUNCpoint
S245 -> PP COMMA
S246 -> S245 NP
S247 -> S246 ADVP
S248 -> S247 VP
S -> S248 PUNCpoint
S249 -> PP COMMA
S250 -> S249 NP
S251 -> S250 ADVPTMP
S252 -> S251 VP
S -> S252 PUNCpoint
S253 -> PP COMMA
S254 -> S253 NP
S255 -> S254 NPTMP
S256 -> S255 VP
S -> S256 PUNCpoint
S257 -> PP COMMA
S258 -> S257 NP
S -> S258 VP
S259 -> PP COMMA
S260 -> S259 NP
S261 -> S260 VP
S -> S261 PUNCpoint
S262 -> PP COMMA
S263 -> S262 NP
S264 -> S263 VP
S265 -> S264 PUNCpoint
S -> S265 PUNCquotequote
S266 -> PP COMMA
S267 -> S266 PP
S268 -> S267 COMMA
S269 -> S268 NP
S270 -> S269 VP
S -> S270 PUNCpoint
S271 -> PP COMMA
S272 -> S271 SBARADV
S273 -> S272 COMMA
S274 -> S273 NP
S275 -> S274 VP
S -> S275 PUNCpoint
S276 -> PP NP
S -> S276 VP
S277 -> PP NP
S278 -> S277 VP
S -> S278 PUNCpoint
S279 -> PP PRN
S280 -> S279 NP
S281 -> S280 VP
S -> S281 PUNCpoint
S282 -> PPLOC COMMA
S283 -> S282 ADVP
S284 -> S283 COMMA
S285 -> S284 NP
S286 -> S285 VP
S -> S286 PUNCpoint
S287 -> PPLOC COMMA
S288 -> S287 NP
S289 -> S288 ADVP
S290 -> S289 VP
S -> S290 PUNCpoint
S291 -> PPLOC COMMA
S292 -> S291 NP
S293 -> S292 ADVPTMP
S294 -> S293 VP
S -> S294 PUNCpoint
S295 -> PPLOC COMMA
S296 -> S295 NP
S -> S296 VP
S297 -> PPLOC COMMA
S298 -> S297 NP
S299 -> S298 VP
S -> S299 PUNCpoint
S300 -> PPLOC COMMA
S301 -> S300 NP
S302 -> S301 VP
S303 -> S302 PUNCpoint
S -> S303 PUNCquotequote
S304 -> PPLOC COMMA
S305 -> S304 PP
S306 -> S305 COMMA
S307 -> S306 NP
S308 -> S307 VP
S -> S308 PUNCpoint
S309 -> PPLOC PUNCcolon
S310 -> S309 NP
S311 -> S310 VP
S -> S311 PUNCpoint
S312 -> PPLOC NP
S -> S312 VP
S313 -> PPLOC NP
S314 -> S313 VP
S -> S314 PUNCpoint
S315 -> PPLOC NPTMP
S316 -> S315 COMMA
S317 -> S316 NP
S318 -> S317 VP
S -> S318 PUNCpoint
S319 -> PPLOC NPTMP
S320 -> S319 PPLOC
S321 -> S320 COMMA
S322 -> S321 NP
S323 -> S322 VP
S -> S323 PUNCpoint
S324 -> PPLOC PPLOC
S325 -> S324 COMMA
S326 -> S325 NP
S327 -> S326 VP
S -> S327 PUNCpoint
S328 -> PPLOC PPLOC
S329 -> S328 NPTMP
S330 -> S329 COMMA
S331 -> S330 NP
S332 -> S331 VP
S -> S332 PUNCpoint
S333 -> PPLOC PRN
S334 -> S333 NP
S335 -> S334 VP
S -> S335 PUNCpoint
S336 -> PPTMP COMMA
S337 -> S336 ADVP
S338 -> S337 COMMA
S339 -> S338 NP
S340 -> S339 VP
S -> S340 PUNCpoint
S341 -> PPTMP COMMA
S342 -> S341 NP
S343 -> S342 ADVP
S344 -> S343 VP
S -> S344 PUNCpoint
S345 -> PPTMP COMMA
S346 -> S345 NP
S347 -> S346 ADVPTMP
S348 -> S347 VP
S -> S348 PUNCpoint
S349 -> PPTMP COMMA
S350 -> S349 NP
S -> S350 VP
S351 -> PPTMP COMMA
S352 -> S351 NP
S353 -> S352 VP
S -> S353 PUNCpoint
S354 -> PPTMP COMMA
S355 -> S354 NP
S356 -> S355 VP
S357 -> S356 PUNCpoint
S -> S357 PUNCquotequote
S358 -> PPTMP COMMA
S359 -> S358 PP
S360 -> S359 COMMA
S361 -> S360 NP
S362 -> S361 VP
S -> S362 PUNCpoint
S363 -> PPTMP COMMA
S364 -> S363 PPTMP
S365 -> S364 COMMA
S366 -> S365 NP
S367 -> S366 VP
S -> S367 PUNCpoint
S368 -> PPTMP COMMA
S369 -> S368 SBARTMP
S370 -> S369 COMMA
S371 -> S370 NP
S372 -> S371 VP
S -> S372 PUNCpoint
S373 -> PPTMP NP
S -> S373 VP
S374 -> PPTMP NP
S375 -> S374 VP
S -> S375 PUNCpoint
S376 -> PPTMP NPTMP
S377 -> S376 COMMA
S378 -> S377 NP
S379 -> S378 VP
S -> S379 PUNCpoint
S380 -> PPTMP PRN
S381 -> S380 NP
S382 -> S381 VP
S -> S382 PUNCpoint
S383 -> RB NP
S384 -> S383 VP
S -> S384 PUNCpoint
S385 -> S COMMA
S386 -> S385 IN
S -> S386 S
S387 -> S COMMA
S388 -> S387 IN
S389 -> S388 S
S -> S389 PUNCpoint
S390 -> S COMMA
S391 -> S390 NP
S392 -> S391 VP
S -> S392 PUNCpoint
S393 -> S COMMA
S394 -> S393 S
S -> S394 PUNCpoint
S395 -> S PUNCcolon
S -> S395 S
S396 -> S PUNCcolon
S397 -> S396 S
S -> S397 PUNCpoint
S398 -> S PUNCcolon
S399 -> S398 S
S400 -> S399 PUNCpoint
S -> S400 PUNCquotequote
S401 -> S PUNCcolon
S402 -> S401 S
S403 -> S402 PUNCcolon
S404 -> S403 S
S -> S404 PUNCpoint
S405 -> S PUNCcolon
S406 -> S405 PUNCbquotebquote
S407 -> S406 S
S408 -> S407 PUNCpoint
S -> S408 PUNCquotequote
S409 -> SADV COMMA
S410 -> S409 NP
S411 -> S410 ADVP
S412 -> S411 VP
S -> S412 PUNCpoint
S413 -> SADV COMMA
S414 -> S413 NP
S415 -> S414 ADVPTMP
S416 -> S415 VP
S -> S416 PUNCpoint
S417 -> SADV COMMA
S418 -> S417 NP
S419 -> S418 VP
S -> S419 PUNCpoint
S420 -> SADV COMMA
S421 -> S420 NP
S422 -> S421 VP
S423 -> S422 PUNCpoint
S -> S423 PUNCquotequote
S424 -> SNOM VP
S -> S424 PUNCpoint
S425 -> SPRP COMMA
S426 -> S425 NP
S427 -> S426 VP
S -> S427 PUNCpoint
S428 -> STPC COMMA
S429 -> S428 PUNCquotequote
S430 -> S429 NP
S431 -> S430 VP
S -> S431 PUNCpoint
S432 -> STPC COMMA
S433 -> S432 NP
S -> S433 VP
S434 -> STPC COMMA
S435 -> S434 NP
S436 -> S435 VP
S -> S436 PUNCpoint
S437 -> STPC NP
S438 -> S437 VP
S -> S438 PUNCpoint
S439 -> SBAR COMMA
S440 -> S439 NP
S -> S440 VP
S441 -> SBAR COMMA
S442 -> S441 NP
S443 -> S442 VP
S -> S443 PUNCpoint
S444 -> SBARADV COMMA
S445 -> S444 PUNCquotequote
S446 -> S445 NP
S447 -> S446 VP
S -> S447 PUNCpoint
S448 -> SBARADV COMMA
S449 -> S448 VP
S -> S449 PUNCpoint
S450 -> SBARADV COMMA
S451 -> S450 NP
S452 -> S451 ADVP
S453 -> S452 VP
S -> S453 PUNCpoint
S454 -> SBARADV COMMA
S455 -> S454 NP
S456 -> S455 ADVPTMP
S457 -> S456 VP
S -> S457 PUNCpoint
S458 -> SBARADV COMMA
S459 -> S458 NP
S -> S459 VP
S460 -> SBARADV COMMA
S461 -> S460 NP
S462 -> S461 VP
S -> S462 PUNCpoint
S463 -> SBARADV COMMA
S464 -> S463 NP
S465 -> S464 VP
S466 -> S465 PUNCpoint
S -> S466 PUNCquotequote
S467 -> SBARADV NP
S -> S467 VP
S468 -> SBARADV NP
S469 -> S468 VP
S -> S469 PUNCpoint
S470 -> SBARADV PRN
S471 -> S470 NP
S472 -> S471 VP
S -> S472 PUNCpoint
S473 -> SBARNOM VP
S -> S473 PUNCpoint
S474 -> SBARPRP COMMA
S475 -> S474 NP
S -> S475 VP
S476 -> SBARPRP COMMA
S477 -> S476 NP
S478 -> S477 VP
S -> S478 PUNCpoint
S479 -> SBARSBJ VP
S -> S479 PUNCpoint
S480 -> SBARTMP COMMA
S481 -> S480 NP
S482 -> S481 ADVPTMP
S483 -> S482 VP
S -> S483 PUNCpoint
S484 -> SBARTMP COMMA
S485 -> S484 NP
S -> S485 VP
S486 -> SBARTMP COMMA
S487 -> S486 NP
S488 -> S487 VP
S -> S488 PUNCpoint
S489 -> SBARTMP COMMA
S490 -> S489 NP
S491 -> S490 VP
S492 -> S491 PUNCpoint
S -> S492 PUNCquotequote
S493 -> SBARTMP NP
S494 -> S493 VP
S -> S494 PUNCpoint
S495 -> PUNCbquotebquote ADVP
S496 -> S495 COMMA
S497 -> S496 NP
S498 -> S497 VP
S499 -> S498 PUNCpoint
S -> S499 PUNCquotequote
S500 -> PUNCbquotebquote ADVP
S501 -> S500 NP
S502 -> S501 VP
S503 -> S502 PUNCpoint
S -> S503 PUNCquotequote
S504 -> PUNCbquotebquote NP
S505 -> S504 PUNCquotequote
S -> S505 VP
S506 -> PUNCbquotebquote NP
S507 -> S506 PUNCquotequote
S508 -> S507 VP
S -> S508 PUNCpoint
S509 -> PUNCbquotebquote NP
S510 -> S509 COMMA
S511 -> S510 PUNCquotequote
S512 -> S511 NP
S513 -> S512 VP
S -> S513 PUNCpoint
S514 -> PUNCbquotebquote NP
S515 -> S514 ADVP
S516 -> S515 VP
S517 -> S516 PUNCpoint
S -> S517 PUNCquotequote
S518 -> PUNCbquotebquote NP
S519 -> S518 PRN
S520 -> S519 VP
S521 -> S520 PUNCpoint
S -> S521 PUNCquotequote
S522 -> PUNCbquotebquote NP
S -> S522 VP
S523 -> PUNCbquotebquote NP
S524 -> S523 VP
S -> S524 PUNCpoint
S525 -> PUNCbquotebquote NP
S526 -> S525 VP
S527 -> S526 PUNCpoint
S -> S527 PUNCquotequote
S528 -> PUNCbquotebquote NP
S529 -> S528 VP
S -> S529 PUNCcolon
S530 -> PUNCbquotebquote NPR
S531 -> S530 PUNCquotequote
S -> S531 VP
S532 -> PUNCbquotebquote NPR
S533 -> S532 PUNCquotequote
S534 -> S533 VP
S -> S534 PUNCpoint
S535 -> PUNCbquotebquote PP
S536 -> S535 COMMA
S537 -> S536 NP
S538 -> S537 VP
S -> S538 PUNCpoint
S539 -> PUNCbquotebquote PP
S540 -> S539 COMMA
S541 -> S540 NP
S542 -> S541 VP
S543 -> S542 PUNCpoint
S -> S543 PUNCquotequote
S544 -> PUNCbquotebquote PPTMP
S545 -> S544 COMMA
S546 -> S545 NP
S547 -> S546 VP
S -> S547 PUNCpoint
S548 -> PUNCbquotebquote S
S549 -> S548 COMMA
S550 -> S549 PUNCquotequote
S551 -> S550 NP
S552 -> S551 VP
S -> S552 PUNCpoint
S553 -> PUNCbquotebquote S
S554 -> S553 PUNCcolon
S555 -> S554 S
S556 -> S555 PUNCpoint
S -> S556 PUNCquotequote
S557 -> PUNCbquotebquote STPC
S558 -> S557 COMMA
S559 -> S558 PUNCquotequote
S560 -> S559 NP
S561 -> S560 VP
S -> S561 PUNCpoint
S562 -> PUNCbquotebquote STPC
S563 -> S562 COMMA
S564 -> S563 PUNCquotequote
S565 -> S564 VP
S566 -> S565 NP
S -> S566 PUNCpoint
S567 -> PUNCbquotebquote STPC
S568 -> S567 COMMA
S569 -> S568 NP
S570 -> S569 VP
S -> S570 PUNCpoint
S571 -> PUNCbquotebquote SBARADV
S572 -> S571 COMMA
S573 -> S572 NP
S574 -> S573 VP
S -> S574 PUNCpoint
S575 -> PUNCbquotebquote SBARADV
S576 -> S575 COMMA
S577 -> S576 NP
S578 -> S577 VP
S579 -> S578 PUNCpoint
S -> S579 PUNCquotequote
S580 -> PUNCbquotebquote SBARTMP
S581 -> S580 COMMA
S582 -> S581 NP
S583 -> S582 VP
S584 -> S583 PUNCpoint
S -> S584 PUNCquotequote
ADJPPRD585 -> ADJP COMMA
ADJPPRD -> ADJPPRD585 ADJP
ADJPPRD586 -> ADJP PP
ADJPPRD -> ADJPPRD586 PP
ADJPPRD587 -> ADVP JJ
ADJPPRD -> ADJPPRD587 PP
ADJPPRD588 -> JJ NPTMP
ADJPPRD -> ADJPPRD588 PP
ADJPPRD589 -> JJ PP
ADJPPRD -> ADJPPRD589 PP
ADJPPRD590 -> JJ RB
ADJPPRD -> ADJPPRD590 S
ADJPPRD591 -> RB JJ
ADJPPRD -> ADJPPRD591 PP
ADJPPRD592 -> RB JJ
ADJPPRD -> ADJPPRD592 S
ADJPPRD593 -> RB JJ
ADJPPRD -> ADJPPRD593 SBAR
ADJPPRD594 -> RB RB
ADJPPRD -> ADJPPRD594 JJ
ADJPPRD595 -> RB RBR
ADJPPRD -> ADJPPRD595 JJ
ADJPPRD596 -> RB VBN
ADJPPRD -> ADJPPRD596 PP
ADJPPRD597 -> RBR JJ
ADJPPRD -> ADJPPRD597 PP
ADJPPRD598 -> RBR JJ
ADJPPRD -> ADJPPRD598 S
ADJPPRD599 -> PUNCbquotebquote JJ
ADJPPRD600 -> ADJPPRD599 PUNCquotequote
ADJPPRD -> ADJPPRD600 PP
SBARTMP601 -> ADVP IN
SBARTMP -> SBARTMP601 S
SBARTMP602 -> NP IN
SBARTMP -> SBARTMP602 S
SBARTMP603 -> NPADV IN
SBARTMP -> SBARTMP603 S
SBARTMP604 -> RB IN
SBARTMP -> SBARTMP604 S
NPLOC605 -> NP COMMA
NPLOC -> NPLOC605 NP
NPLOC606 -> NP COMMA
NPLOC607 -> NPLOC606 NP
NPLOC -> NPLOC607 COMMA
NPLOC608 -> NP COMMA
NPLOC609 -> NPLOC608 NP
NPLOC -> NPLOC609 PUNCpoint
NPLOC610 -> NPR COMMA
NPLOC -> NPLOC610 NPR
VP611 -> ADVP VB
VP -> VP611 NP
VP612 -> ADVP VB
VP613 -> VP612 NP
VP -> VP613 PP
VP614 -> ADVP VB
VP -> VP614 S
VP615 -> ADVP VBD
VP -> VP615 NP
VP616 -> ADVP VBD
VP617 -> VP616 NP
VP -> VP617 PP
VP618 -> ADVP VBD
VP619 -> VP618 PP
VP -> VP619 PP
VP620 -> ADVP VBD
VP -> VP620 S
VP621 -> ADVP VBD
VP -> VP621 SBAR
VP622 -> ADVP VBG
VP -> VP622 NP
VP623 -> ADVP VBG
VP624 -> VP623 NP
VP -> VP624 PP
VP625 -> ADVP VBG
VP -> VP625 PP
VP626 -> ADVP VBG
VP -> VP626 S
VP627 -> ADVP VBN
VP -> VP627 PP
VP628 -> ADVP VBN
VP -> VP628 PPLOC
VP629 -> ADVP VBN
VP -> VP629 PPTMP
VP630 -> ADVP VBN
VP -> VP630 NP
VP631 -> ADVP VBN
VP -> VP631 S
VP632 -> ADVP VBP
VP -> VP632 NP
VP633 -> ADVP VBP
VP -> VP633 SBAR
VP634 -> ADVP VBZ
VP -> VP634 NP
VP635 -> ADVPTMP VBG
VP -> VP635 NP
VP636 -> ADVPTMP VBG
VP -> VP636 VP
VP637 -> ADVPTMP VBN
VP -> VP637 PP
VP638 -> ADVPTMP VBN
VP -> VP638 PPLOC
VP639 -> MD ADVP
VP -> VP639 VP
VP640 -> MD ADVPTMP
VP -> VP640 VP
VP641 -> MD RB
VP642 -> VP641 ADVP
VP -> VP642 VP
VP643 -> MD RB
VP644 -> VP643 ADVPTMP
VP -> VP644 VP
VP645 -> MD RB
VP -> VP645 VP
VP646 -> MD PUNCbquotebquote
VP -> VP646 VP
VP647 -> RB VBG
VP -> VP647 NP
VP648 -> TO ADVP
VP -> VP648 VP
VP649 -> TO ADVPTMP
VP -> VP649 VP
VP650 -> TO PUNCbquotebquote
VP -> VP650 VP
VP651 -> VB PUNCquotequote
VP -> VP651 NP
VP652 -> VB ADJPPRD
VP -> VP652 ADVP
VP653 -> VB ADJPPRD
VP -> VP653 ADVPTMP
VP654 -> VB ADJPPRD
VP -> VP654 NPTMP
VP655 -> VB ADJPPRD
VP -> VP655 PP
VP656 -> VB ADJPPRD
VP -> VP656 PPLOC
VP657 -> VB ADJPPRD
VP -> VP657 PPTMP
VP658 -> VB ADJPPRD
VP -> VP658 S
VP659 -> VB ADJPPRD
VP -> VP659 SBAR
VP660 -> VB ADJPPRD
VP -> VP660 SBARADV
VP661 -> VB ADJPPRD
VP -> VP661 SBARPRP
VP662 -> VB ADJPPRD
VP -> VP662 SBARTMP
VP663 -> VB ADVP
VP -> VP663 NP
VP664 -> VB ADVP
VP -> VP664 PP
VP665 -> VB ADVP
VP -> VP665 PPLOC
VP666 -> VB ADVP
VP -> VP666 PPTMP
VP667 -> VB ADVP
VP -> VP667 SBAR
VP668 -> VB ADVP
VP -> VP668 VP
VP669 -> VB ADVPTMP
VP -> VP669 PP
VP670 -> VB NP
VP671 -> VP670 COMMA
VP -> VP671 ADVP
VP672 -> VB NP
VP673 -> VP672 COMMA
VP -> VP673 PP
VP674 -> VB NP
VP675 -> VP674 COMMA
VP -> VP675 SADV
VP676 -> VB NP
VP677 -> VP676 COMMA
VP -> VP677 SBARADV
VP678 -> VB NP
VP -> VP678 ADVP
VP679 -> VB NP
VP680 -> VP679 ADVP
VP -> VP680 PP
VP681 -> VB NP
VP -> VP681 ADVPLOC
VP682 -> VB NP
VP -> VP682 ADVPTMP
VP683 -> VB NP
VP -> VP683 NP
VP684 -> VB NP
VP685 -> VP684 NP
VP -> VP685 PP
VP686 -> VB NP
VP687 -> VP686 NP
VP -> VP687 PPTMP
VP688 -> VB NP
VP -> VP688 NPTMP
VP689 -> VB NP
VP690 -> VP689 NPTMP
VP691 -> VP690 COMMA
VP -> VP691 PP
VP692 -> VB NP
VP693 -> VP692 NPTMP
VP -> VP693 PP
VP694 -> VB NP
VP695 -> VP694 NPTMP
VP -> VP695 PPLOC
VP696 -> VB NP
VP -> VP696 PP
VP697 -> VB NP
VP698 -> VP697 PP
VP699 -> VP698 COMMA
VP -> VP699 PP
VP700 -> VB NP
VP701 -> VP700 PP
VP702 -> VP701 COMMA
VP -> VP702 SADV
VP703 -> VB NP
VP704 -> VP703 PP
VP705 -> VP704 COMMA
VP -> VP705 SBARADV
VP706 -> VB NP
VP707 -> VP706 PP
VP708 -> VP707 COMMA
VP -> VP708 SBARPRP
VP709 -> VB NP
VP710 -> VP709 PP
VP -> VP710 ADVPTMP
VP711 -> VB NP
VP712 -> VP711 PP
VP -> VP712 NPTMP
VP713 -> VB NP
VP714 -> VP713 PP
VP -> VP714 PP
VP715 -> VB NP
VP716 -> VP715 PP
VP -> VP716 PPLOC
VP717 -> VB NP
VP718 -> VP717 PP
VP -> VP718 PPTMP
VP719 -> VB NP
VP720 -> VP719 PP
VP -> VP720 SPRP
VP721 -> VB NP
VP722 -> VP721 PP
VP -> VP722 SBARADV
VP723 -> VB NP
VP724 -> VP723 PP
VP -> VP724 SBARPRP
VP725 -> VB NP
VP726 -> VP725 PP
VP -> VP726 SBARTMP
VP727 -> VB NP
VP -> VP727 PPLOC
VP728 -> VB NP
VP729 -> VP728 PPLOC
VP -> VP729 PP
VP730 -> VB NP
VP731 -> VP730 PPLOC
VP -> VP731 PPTMP
VP732 -> VB NP
VP -> VP732 PPTMP
VP733 -> VB NP
VP734 -> VP733 PPTMP
VP735 -> VP734 COMMA
VP -> VP735 PP
VP736 -> VB NP
VP737 -> VP736 PPTMP
VP -> VP737 PP
VP738 -> VB NP
VP739 -> VP738 PPTMP
VP -> VP739 SBARTMP
VP740 -> VB NP
VP -> VP740 PRT
VP741 -> VB NP
VP -> VP741 S
VP742 -> VB NP
VP -> VP742 SPRP
VP743 -> VB NP
VP -> VP743 SBAR
VP744 -> VB NP
VP -> VP744 SBARADV
VP745 -> VB NP
VP -> VP745 SBARPRP
VP746 -> VB NP
VP -> VP746 SBARTMP
VP747 -> VB NP
VP -> VP747 VP
VP748 -> VB NPPRD
VP -> VP748 NPTMP
VP749 -> VB NPPRD
VP -> VP749 PP
VP750 -> VB NPPRD
VP -> VP750 PPLOC
VP751 -> VB NPPRD
VP -> VP751 PPTMP
VP752 -> VB NPPRD
VP -> VP752 SBARTMP
VP753 -> VB NPTMP
VP -> VP753 NP
VP754 -> VB PP
VP755 -> VP754 COMMA
VP -> VP755 ADVP
VP756 -> VB PP
VP -> VP756 ADVP
VP757 -> VB PP
VP -> VP757 ADVPTMP
VP758 -> VB PP
VP -> VP758 NP
VP759 -> VB PP
VP -> VP759 NPTMP
VP760 -> VB PP
VP -> VP760 PP
VP761 -> VB PP
VP -> VP761 PPLOC
VP762 -> VB PP
VP -> VP762 PPTMP
VP763 -> VB PP
VP -> VP763 SPRP
VP764 -> VB PP
VP -> VP764 SBAR
VP765 -> VB PP
VP -> VP765 SBARADV
VP766 -> VB PP
VP -> VP766 SBARPRP
VP767 -> VB PP
VP -> VP767 SBARTMP
VP768 -> VB PPLOC
VP -> VP768 PPTMP
VP769 -> VB PPLOC
VP -> VP769 SBARTMP
VP770 -> VB PPPRD
VP -> VP770 PP
VP771 -> VB PPPRD
VP -> VP771 PPTMP
VP772 -> VB PPTMP
VP -> VP772 NP
VP773 -> VB PPTMP
VP -> VP773 PP
VP774 -> VB PPTMP
VP -> VP774 SPRP
VP775 -> VB PPTMP
VP -> VP775 SBAR
VP776 -> VB PRT
VP -> VP776 NP
VP777 -> VB PRT
VP778 -> VP777 NP
VP -> VP778 PP
VP779 -> VB PRT
VP780 -> VP779 NP
VP -> VP780 PPTMP
VP781 -> VB PRT
VP782 -> VP781 NP
VP -> VP782 SPRP
VP783 -> VB PRT
VP -> VP783 PP
VP784 -> VB PRT
VP -> VP784 PPLOC
VP785 -> VB PRT
VP -> VP785 S
VP786 -> VB PRT
VP -> VP786 SBAR
VP787 -> VB RB
VP -> VP787 VP
VP788 -> VB S
VP789 -> VP788 COMMA
VP -> VP789 SBARADV
VP790 -> VB S
VP -> VP790 PP
VP791 -> VB S
VP -> VP791 PPTMP
VP792 -> VB S
VP -> VP792 SPRP
VP793 -> VB S
VP -> VP793 SBARADV
VP794 -> VB S
VP -> VP794 SBARPRP
VP795 -> VB S
VP -> VP795 SBARTMP
VP796 -> VB PUNCbquotebquote
VP -> VP796 ADJPPRD
VP797 -> VB PUNCbquotebquote
VP -> VP797 NP
VP798 -> VBD COMMA
VP799 -> VP798 ADVP
VP800 -> VP799 COMMA
VP -> VP800 SBAR
VP801 -> VBD COMMA
VP -> VP801 S
VP802 -> VBD COMMA
VP -> VP802 SADV
VP803 -> VBD COMMA
VP -> VP803 SBAR
VP804 -> VBD COMMA
VP805 -> VP804 PUNCbquotebquote
VP -> VP805 S
VP806 -> VBD PP
VP -> VP806 PP
VP807 -> VBD PP
VP -> VP807 PPTMP
VP808 -> VBD PRT
VP -> VP808 PP
VP809 -> VBD PUNCcolon
VP810 -> VP809 PUNCbquotebquote
VP -> VP810 S
VP811 -> VBD ADJPPRD
VP812 -> VP811 COMMA
VP -> VP812 PP
VP813 -> VBD ADJPPRD
VP814 -> VP813 COMMA
VP -> VP814 SADV
VP815 -> VBD ADJPPRD
VP -> VP815 NPTMP
VP816 -> VBD ADJPPRD
VP -> VP816 PP
VP817 -> VBD ADJPPRD
VP -> VP817 PPLOC
VP818 -> VBD ADJPPRD
VP -> VP818 PPTMP
VP819 -> VBD ADJPPRD
VP -> VP819 SBAR
VP820 -> VBD ADJPPRD
VP -> VP820 SBARADV
VP821 -> VBD ADJPPRD
VP -> VP821 SBARTMP
VP822 -> VBD ADVP
VP823 -> VP822 COMMA
VP -> VP823 PP
VP824 -> VBD ADVP
VP825 -> VP824 COMMA
VP -> VP825 SADV
VP826 -> VBD ADVP
VP -> VP826 ADJPPRD
VP827 -> VBD ADVP
VP -> VP827 NP
VP828 -> VBD ADVP
VP -> VP828 NPPRD
VP829 -> VBD ADVP
VP -> VP829 NPTMP
VP830 -> VBD ADVP
VP -> VP830 PP
VP831 -> VBD ADVP
VP832 -> VP831 PP
VP833 -> VP832 COMMA
VP -> VP833 SADV
VP834 -> VBD ADVP
VP835 -> VP834 PP
VP -> VP835 PP
VP836 -> VBD ADVP
VP -> VP836 PPLOC
VP837 -> VBD ADVP
VP -> VP837 PPPRD
VP838 -> VBD ADVP
VP -> VP838 PPTMP
VP839 -> VBD ADVP
VP -> VP839 SBAR
VP840 -> VBD ADVP
VP -> VP840 SBARTMP
VP841 -> VBD ADVP
VP -> VP841 VP
VP842 -> VBD ADVPPRD
VP -> VP842 PP
VP843 -> VBD ADVPTMP
VP -> VP843 ADJPPRD
VP844 -> VBD ADVPTMP
VP -> VP844 NPPRD
VP845 -> VBD ADVPTMP
VP -> VP845 SBAR
VP846 -> VBD ADVPTMP
VP -> VP846 VP
VP847 -> VBD NP
VP848 -> VP847 COMMA
VP -> VP848 ADVP
VP849 -> VBD NP
VP850 -> VP849 COMMA
VP -> VP850 PP
VP851 -> VBD NP
VP852 -> VP851 COMMA
VP853 -> VP852 PP
VP854 -> VP853 COMMA
VP -> VP854 PP
VP855 -> VBD NP
VP856 -> VP855 COMMA
VP857 -> VP856 PP
VP -> VP857 PP
VP858 -> VBD NP
VP859 -> VP858 COMMA
VP -> VP859 PPLOC
VP860 -> VBD NP
VP861 -> VP860 COMMA
VP -> VP861 SADV
VP862 -> VBD NP
VP863 -> VP862 COMMA
VP -> VP863 SBARADV
VP864 -> VBD NP
VP865 -> VP864 COMMA
VP -> VP865 SBARTMP
VP866 -> VBD NP
VP -> VP866 ADVP
VP867 -> VBD NP
VP868 -> VP867 ADVP
VP -> VP868 PP
VP869 -> VBD NP
VP -> VP869 ADVPLOC
VP870 -> VBD NP
VP -> VP870 ADVPTMP
VP871 -> VBD NP
VP872 -> VP871 ADVPTMP
VP -> VP872 PP
VP873 -> VBD NP
VP -> VP873 NP
VP874 -> VBD NP
VP875 -> VP874 NP
VP -> VP875 PPTMP
VP876 -> VBD NP
VP -> VP876 NPTMP
VP877 -> VBD NP
VP878 -> VP877 NPTMP
VP879 -> VP878 COMMA
VP -> VP879 PP
VP880 -> VBD NP
VP881 -> VP880 NPTMP
VP -> VP881 PP
VP882 -> VBD NP
VP883 -> VP882 NPTMP
VP -> VP883 PPLOC
VP884 -> VBD NP
VP885 -> VP884 NPTMP
VP -> VP885 S
VP886 -> VBD NP
VP887 -> VP886 NPTMP
VP -> VP887 SBAR
VP888 -> VBD NP
VP889 -> VP888 NPTMP
VP -> VP889 SBARTMP
VP890 -> VBD NP
VP -> VP890 PP
VP891 -> VBD NP
VP892 -> VP891 PP
VP893 -> VP892 COMMA
VP -> VP893 NP
VP894 -> VBD NP
VP895 -> VP894 PP
VP896 -> VP895 COMMA
VP -> VP896 PP
VP897 -> VBD NP
VP898 -> VP897 PP
VP899 -> VP898 COMMA
VP -> VP899 SADV
VP900 -> VBD NP
VP901 -> VP900 PP
VP902 -> VP901 COMMA
VP -> VP902 SBARADV
VP903 -> VBD NP
VP904 -> VP903 PP
VP -> VP904 ADVPTMP
VP905 -> VBD NP
VP906 -> VP905 PP
VP -> VP906 NPTMP
VP907 -> VBD NP
VP908 -> VP907 PP
VP -> VP908 PP
VP909 -> VBD NP
VP910 -> VP909 PP
VP911 -> VP910 PP
VP912 -> VP911 COMMA
VP -> VP912 SADV
VP913 -> VBD NP
VP914 -> VP913 PP
VP915 -> VP914 PP
VP916 -> VP915 COMMA
VP -> VP916 SBARADV
VP917 -> VBD NP
VP918 -> VP917 PP
VP919 -> VP918 PP
VP -> VP919 PP
VP920 -> VBD NP
VP921 -> VP920 PP
VP922 -> VP921 PP
VP -> VP922 PPTMP
VP923 -> VBD NP
VP924 -> VP923 PP
VP -> VP924 PPLOC
VP925 -> VBD NP
VP926 -> VP925 PP
VP -> VP926 PPTMP
VP927 -> VBD NP
VP928 -> VP927 PP
VP -> VP928 S
VP929 -> VBD NP
VP930 -> VP929 PP
VP -> VP930 SADV
VP931 -> VBD NP
VP932 -> VP931 PP
VP -> VP932 SPRP
VP933 -> VBD NP
VP934 -> VP933 PP
VP -> VP934 SBARADV
VP935 -> VBD NP
VP936 -> VP935 PP
VP -> VP936 SBARTMP
VP937 -> VBD NP
VP -> VP937 PPLOC
VP938 -> VBD NP
VP939 -> VP938 PPLOC
VP940 -> VP939 COMMA
VP -> VP940 PP
VP941 -> VBD NP
VP942 -> VP941 PPLOC
VP943 -> VP942 COMMA
VP -> VP943 SADV
VP944 -> VBD NP
VP945 -> VP944 PPLOC
VP -> VP945 NPTMP
VP946 -> VBD NP
VP947 -> VP946 PPLOC
VP -> VP947 PP
VP948 -> VBD NP
VP949 -> VP948 PPLOC
VP -> VP949 PPTMP
VP950 -> VBD NP
VP -> VP950 PPTMP
VP951 -> VBD NP
VP952 -> VP951 PPTMP
VP953 -> VP952 COMMA
VP -> VP953 ADVP
VP954 -> VBD NP
VP955 -> VP954 PPTMP
VP956 -> VP955 COMMA
VP -> VP956 NP
VP957 -> VBD NP
VP958 -> VP957 PPTMP
VP959 -> VP958 COMMA
VP -> VP959 PP
VP960 -> VBD NP
VP961 -> VP960 PPTMP
VP962 -> VP961 COMMA
VP -> VP962 SADV
VP963 -> VBD NP
VP964 -> VP963 PPTMP
VP965 -> VP964 COMMA
VP -> VP965 SBARADV
VP966 -> VBD NP
VP967 -> VP966 PPTMP
VP -> VP967 PP
VP968 -> VBD NP
VP969 -> VP968 PPTMP
VP970 -> VP969 PP
VP -> VP970 PP
VP971 -> VBD NP
VP972 -> VP971 PPTMP
VP -> VP972 PPTMP
VP973 -> VBD NP
VP974 -> VP973 PPTMP
VP -> VP974 SBAR
VP975 -> VBD NP
VP -> VP975 S
VP976 -> VBD NP
VP -> VP976 SADV
VP977 -> VBD NP
VP -> VP977 SPRP
VP978 -> VBD NP
VP -> VP978 SBAR
VP979 -> VBD NP
VP -> VP979 SBARADV
VP980 -> VBD NP
VP -> VP980 SBARPRP
VP981 -> VBD NP
VP -> VP981 SBARTMP
VP982 -> VBD NPADV
VP -> VP982 PP
VP983 -> VBD NPADV
VP984 -> VP983 PP
VP -> VP984 PP
VP985 -> VBD NPPRD
VP986 -> VP985 COMMA
VP -> VP986 ADVP
VP987 -> VBD NPPRD
VP988 -> VP987 COMMA
VP -> VP988 PP
VP989 -> VBD NPPRD
VP990 -> VP989 COMMA
VP -> VP990 SADV
VP991 -> VBD NPPRD
VP992 -> VP991 COMMA
VP -> VP992 SBARADV
VP993 -> VBD NPPRD
VP -> VP993 PP
VP994 -> VBD NPPRD
VP -> VP994 PPLOC
VP995 -> VBD NPPRD
VP -> VP995 PPTMP
VP996 -> VBD NPPRD
VP -> VP996 SBAR
VP997 -> VBD NPTMP
VP -> VP997 PP
VP998 -> VBD NPTMP
VP999 -> VP998 PP
VP1000 -> VP999 COMMA
VP -> VP1000 ADVP
VP1001 -> VBD NPTMP
VP1002 -> VP1001 PP
VP1003 -> VP1002 COMMA
VP1004 -> VP1003 ADVP
VP1005 -> VP1004 COMMA
VP -> VP1005 PPLOC
VP1006 -> VBD NPTMP
VP -> VP1006 PPLOC
VP1007 -> VBD NPTMP
VP -> VP1007 S
VP1008 -> VBD NPTMP
VP -> VP1008 SBAR
VP1009 -> VBD PP
VP1010 -> VP1009 COMMA
VP -> VP1010 ADVP
VP1011 -> VBD PP
VP1012 -> VP1011 COMMA
VP1013 -> VP1012 ADVP
VP1014 -> VP1013 COMMA
VP -> VP1014 PPLOC
VP1015 -> VBD PP
VP1016 -> VP1015 COMMA
VP -> VP1016 PP
VP1017 -> VBD PP
VP1018 -> VP1017 COMMA
VP -> VP1018 SADV
VP1019 -> VBD PP
VP1020 -> VP1019 COMMA
VP -> VP1020 SBARADV
VP1021 -> VBD PP
VP -> VP1021 ADVP
VP1022 -> VBD PP
VP -> VP1022 ADVPTMP
VP1023 -> VBD PP
VP -> VP1023 NP
VP1024 -> VBD PP
VP -> VP1024 NPTMP
VP1025 -> VBD PP
VP1026 -> VP1025 NPTMP
VP -> VP1026 PP
VP1027 -> VBD PP
VP1028 -> VP1027 PP
VP1029 -> VP1028 COMMA
VP -> VP1029 ADVP
VP1030 -> VBD PP
VP1031 -> VP1030 PP
VP1032 -> VP1031 COMMA
VP -> VP1032 PP
VP1033 -> VBD PP
VP1034 -> VP1033 PP
VP -> VP1034 PPTMP
VP1035 -> VBD PP
VP -> VP1035 PPLOC
VP1036 -> VBD PP
VP1037 -> VP1036 PPTMP
VP -> VP1037 PP
VP1038 -> VBD PP
VP -> VP1038 S
VP1039 -> VBD PP
VP -> VP1039 SPRP
VP1040 -> VBD PP
VP -> VP1040 SBAR
VP1041 -> VBD PP
VP -> VP1041 SBARPRP
VP1042 -> VBD PP
VP -> VP1042 SBARTMP
VP1043 -> VBD PPLOC
VP1044 -> VP1043 COMMA
VP -> VP1044 ADVP
VP1045 -> VBD PPLOC
VP -> VP1045 PP
VP1046 -> VBD PPLOC
VP -> VP1046 PPTMP
VP1047 -> VBD PPLOC
VP -> VP1047 SPRP
VP1048 -> VBD PPLOC
VP -> VP1048 SBAR
VP1049 -> VBD PPLOCPRD
VP -> VP1049 SBARTMP
VP1050 -> VBD PPTMP
VP -> VP1050 PP
VP1051 -> VBD PPTMP
VP -> VP1051 SBAR
VP1052 -> VBD PRT
VP -> VP1052 NP
VP1053 -> VBD PRT
VP1054 -> VP1053 NP
VP1055 -> VP1054 COMMA
VP -> VP1055 SADV
VP1056 -> VBD PRT
VP1057 -> VP1056 NP
VP -> VP1057 PP
VP1058 -> VBD PRT
VP1059 -> VP1058 NP
VP -> VP1059 PPTMP
VP1060 -> VBD PRT
VP1061 -> VP1060 NP
VP -> VP1061 SPRP
VP1062 -> VBD PRT
VP -> VP1062 PPLOC
VP1063 -> VBD PRT
VP -> VP1063 S
VP1064 -> VBD PRT
VP -> VP1064 SBAR
VP1065 -> VBD RB
VP -> VP1065 ADJPPRD
VP1066 -> VBD RB
VP1067 -> VP1066 ADVP
VP -> VP1067 VP
VP1068 -> VBD RB
VP -> VP1068 NPPRD
VP1069 -> VBD RB
VP -> VP1069 VP
VP1070 -> VBD S
VP1071 -> VP1070 COMMA
VP -> VP1071 PP
VP1072 -> VBD S
VP1073 -> VP1072 COMMA
VP -> VP1073 SADV
VP1074 -> VBD S
VP1075 -> VP1074 COMMA
VP -> VP1075 SBARADV
VP1076 -> VBD S
VP -> VP1076 NPTMP
VP1077 -> VBD S
VP -> VP1077 PP
VP1078 -> VBD S
VP -> VP1078 PPLOC
VP1079 -> VBD S
VP -> VP1079 PPTMP
VP1080 -> VBD S
VP -> VP1080 SBARTMP
VP1081 -> VBD SBAR
VP1082 -> VP1081 COMMA
VP -> VP1082 SADV
VP1083 -> VBD SBAR
VP1084 -> VP1083 COMMA
VP -> VP1084 SBARADV
VP1085 -> VBD PUNCbquotebquote
VP -> VP1085 ADJPPRD
VP1086 -> VBD PUNCbquotebquote
VP -> VP1086 NPPRD
VP1087 -> VBD PUNCbquotebquote
VP -> VP1087 S
VP1088 -> VBD PUNCbquotebquote
VP -> VP1088 VP
VP1089 -> VBG COMMA
VP1090 -> VP1089 PUNCbquotebquote
VP -> VP1090 S
VP1091 -> VBG PUNCcolon
VP1092 -> VP1091 PUNCbquotebquote
VP -> VP1092 S
VP1093 -> VBG ADVP
VP -> VP1093 NP
VP1094 -> VBG ADVP
VP -> VP1094 PP
VP1095 -> VBG ADVP
VP -> VP1095 PPLOC
VP1096 -> VBG ADVP
VP -> VP1096 PPTMP
VP1097 -> VBG ADVP
VP -> VP1097 SBARTMP
VP1098 -> VBG ADVP
VP -> VP1098 VP
VP1099 -> VBG NP
VP1100 -> VP1099 COMMA
VP -> VP1100 PP
VP1101 -> VBG NP
VP1102 -> VP1101 COMMA
VP -> VP1102 SADV
VP1103 -> VBG NP
VP -> VP1103 ADVP
VP1104 -> VBG NP
VP1105 -> VP1104 ADVP
VP -> VP1105 PP
VP1106 -> VBG NP
VP -> VP1106 ADVPLOC
VP1107 -> VBG NP
VP -> VP1107 ADVPTMP
VP1108 -> VBG NP
VP -> VP1108 NP
VP1109 -> VBG NP
VP -> VP1109 NPTMP
VP1110 -> VBG NP
VP -> VP1110 PP
VP1111 -> VBG NP
VP1112 -> VP1111 PP
VP1113 -> VP1112 COMMA
VP -> VP1113 SBARADV
VP1114 -> VBG NP
VP1115 -> VP1114 PP
VP -> VP1115 PP
VP1116 -> VBG NP
VP1117 -> VP1116 PP
VP -> VP1117 PPTMP
VP1118 -> VBG NP
VP1119 -> VP1118 PP
VP -> VP1119 SPRP
VP1120 -> VBG NP
VP1121 -> VP1120 PP
VP -> VP1121 SBARTMP
VP1122 -> VBG NP
VP -> VP1122 PPLOC
VP1123 -> VBG NP
VP -> VP1123 PPTMP
VP1124 -> VBG NP
VP1125 -> VP1124 PPTMP
VP -> VP1125 PP
VP1126 -> VBG NP
VP -> VP1126 PRT
VP1127 -> VBG NP
VP -> VP1127 S
VP1128 -> VBG NP
VP -> VP1128 SPRP
VP1129 -> VBG NP
VP -> VP1129 SBAR
VP1130 -> VBG NP
VP -> VP1130 SBARADV
VP1131 -> VBG NP
VP -> VP1131 SBARPRP
VP1132 -> VBG NP
VP -> VP1132 SBARTMP
VP1133 -> VBG PP
VP1134 -> VP1133 COMMA
VP -> VP1134 SADV
VP1135 -> VBG PP
VP -> VP1135 ADVP
VP1136 -> VBG PP
VP -> VP1136 ADVPTMP
VP1137 -> VBG PP
VP -> VP1137 NP
VP1138 -> VBG PP
VP -> VP1138 NPTMP
VP1139 -> VBG PP
VP -> VP1139 PP
VP1140 -> VBG PP
VP -> VP1140 PPLOC
VP1141 -> VBG PP
VP -> VP1141 PPTMP
VP1142 -> VBG PP
VP -> VP1142 S
VP1143 -> VBG PP
VP -> VP1143 SPRP
VP1144 -> VBG PP
VP -> VP1144 SBAR
VP1145 -> VBG PPLOC
VP -> VP1145 NPTMP
VP1146 -> VBG PPLOC
VP -> VP1146 PPTMP
VP1147 -> VBG PPTMP
VP -> VP1147 SBAR
VP1148 -> VBG PRT
VP -> VP1148 NP
VP1149 -> VBG PRT
VP1150 -> VP1149 NP
VP -> VP1150 PP
VP1151 -> VBG PRT
VP1152 -> VP1151 NP
VP -> VP1152 PPTMP
VP1153 -> VBG PRT
VP1154 -> VP1153 NP
VP -> VP1154 SPRP
VP1155 -> VBG PRT
VP -> VP1155 PP
VP1156 -> VBG PRT
VP -> VP1156 S
VP1157 -> VBG S
VP -> VP1157 PPTMP
VP1158 -> VBG PUNCbquotebquote
VP -> VP1158 NP
VP1159 -> VBN COMMA
VP -> VP1159 PP
VP1160 -> VBN COMMA
VP -> VP1160 SBARADV
VP1161 -> VBN ADVP
VP -> VP1161 PP
VP1162 -> VBN ADVP
VP -> VP1162 PPLOC
VP1163 -> VBN ADVP
VP -> VP1163 PPTMP
VP1164 -> VBN ADVPTMP
VP -> VP1164 PP
VP1165 -> VBN NP
VP -> VP1165 PP
VP1166 -> VBN NPTMP
VP -> VP1166 PP
VP1167 -> VBN NPTMP
VP -> VP1167 PPLOC
VP1168 -> VBN PP
VP1169 -> VP1168 COMMA
VP -> VP1169 ADVP
VP1170 -> VBN PP
VP1171 -> VP1170 COMMA
VP -> VP1171 PP
VP1172 -> VBN PP
VP1173 -> VP1172 COMMA
VP -> VP1173 SADV
VP1174 -> VBN PP
VP1175 -> VP1174 COMMA
VP -> VP1175 SBARADV
VP1176 -> VBN PP
VP -> VP1176 ADVPTMP
VP1177 -> VBN PP
VP -> VP1177 NPTMP
VP1178 -> VBN PP
VP -> VP1178 PP
VP1179 -> VBN PP
VP1180 -> VP1179 PP
VP -> VP1180 PP
VP1181 -> VBN PP
VP -> VP1181 PPLOC
VP1182 -> VBN PP
VP -> VP1182 PPTMP
VP1183 -> VBN PP
VP1184 -> VP1183 PPTMP
VP -> VP1184 PP
VP1185 -> VBN PP
VP -> VP1185 S
VP1186 -> VBN PP
VP -> VP1186 SPRP
VP1187 -> VBN PP
VP -> VP1187 SBARPRP
VP1188 -> VBN PP
VP -> VP1188 SBARTMP
VP1189 -> VBN PPLOC
VP1190 -> VP1189 COMMA
VP -> VP1190 SADV
VP1191 -> VBN PPLOC
VP -> VP1191 NPTMP
VP1192 -> VBN PPLOC
VP1193 -> VP1192 NPTMP
VP -> VP1193 PP
VP1194 -> VBN PPLOC
VP -> VP1194 PP
VP1195 -> VBN PPLOC
VP -> VP1195 PPLOC
VP1196 -> VBN PPLOC
VP -> VP1196 PPTMP
VP1197 -> VBN PPTMP
VP -> VP1197 PP
VP1198 -> VBN PPTMP
VP -> VP1198 PPLOC
VP1199 -> VBN PPTMP
VP -> VP1199 SPRP
VP1200 -> VBN PRT
VP -> VP1200 PP
VP1201 -> VBN PRT
VP -> VP1201 PPLOC
VP1202 -> VBN PRT
VP -> VP1202 PPTMP
VP1203 -> VBN ADJPPRD
VP1204 -> VP1203 COMMA
VP -> VP1204 SADV
VP1205 -> VBN ADJPPRD
VP -> VP1205 PP
VP1206 -> VBN ADJPPRD
VP -> VP1206 PPTMP
VP1207 -> VBN ADJPPRD
VP -> VP1207 SBARTMP
VP1208 -> VBN ADVP
VP -> VP1208 NPTMP
VP1209 -> VBN ADVP
VP -> VP1209 VP
VP1210 -> VBN NP
VP1211 -> VP1210 COMMA
VP -> VP1211 PP
VP1212 -> VBN NP
VP1213 -> VP1212 COMMA
VP -> VP1213 SADV
VP1214 -> VBN NP
VP1215 -> VP1214 COMMA
VP -> VP1215 SBARADV
VP1216 -> VBN NP
VP -> VP1216 ADVP
VP1217 -> VBN NP
VP1218 -> VP1217 ADVP
VP -> VP1218 PP
VP1219 -> VBN NP
VP -> VP1219 ADVPTMP
VP1220 -> VBN NP
VP -> VP1220 NP
VP1221 -> VBN NP
VP -> VP1221 NPTMP
VP1222 -> VBN NP
VP1223 -> VP1222 PP
VP -> VP1223 PP
VP1224 -> VBN NP
VP1225 -> VP1224 PP
VP -> VP1225 PPTMP
VP1226 -> VBN NP
VP -> VP1226 PPLOC
VP1227 -> VBN NP
VP -> VP1227 PPTMP
VP1228 -> VBN NP
VP1229 -> VP1228 PPTMP
VP1230 -> VP1229 COMMA
VP -> VP1230 PP
VP1231 -> VBN NP
VP -> VP1231 S
VP1232 -> VBN NP
VP -> VP1232 SPRP
VP1233 -> VBN NP
VP -> VP1233 SBAR
VP1234 -> VBN NP
VP -> VP1234 SBARADV
VP1235 -> VBN NP
VP -> VP1235 SBARPRP
VP1236 -> VBN NP
VP -> VP1236 SBARTMP
VP1237 -> VBN NPPRD
VP -> VP1237 PP
VP1238 -> VBN NPPRD
VP -> VP1238 PPTMP
VP1239 -> VBN PPLOCPRD
VP -> VP1239 PPTMP
VP1240 -> VBN PPPRD
VP -> VP1240 PPTMP
VP1241 -> VBN PPTMP
VP -> VP1241 S
VP1242 -> VBN PRT
VP -> VP1242 NP
VP1243 -> VBN PRT
VP1244 -> VP1243 NP
VP -> VP1244 PP
VP1245 -> VBN S
VP1246 -> VP1245 COMMA
VP -> VP1246 PP
VP1247 -> VBN S
VP1248 -> VP1247 COMMA
VP -> VP1248 SADV
VP1249 -> VBN S
VP1250 -> VP1249 COMMA
VP -> VP1250 SBARADV
VP1251 -> VBN S
VP -> VP1251 PP
VP1252 -> VBN S
VP -> VP1252 PPLOC
VP1253 -> VBN S
VP -> VP1253 PPTMP
VP1254 -> VBN S
VP -> VP1254 SBARADV
VP1255 -> VBN S
VP -> VP1255 SBARPRP
VP1256 -> VBN S
VP -> VP1256 SBARTMP
VP1257 -> VBP ADJPPRD
VP1258 -> VP1257 COMMA
VP -> VP1258 SADV
VP1259 -> VBP ADJPPRD
VP -> VP1259 NPTMP
VP1260 -> VBP ADJPPRD
VP -> VP1260 PP
VP1261 -> VBP ADJPPRD
VP -> VP1261 PPLOC
VP1262 -> VBP ADJPPRD
VP -> VP1262 SBARADV
VP1263 -> VBP ADJPPRD
VP -> VP1263 SBARPRP
VP1264 -> VBP ADVP
VP -> VP1264 ADJPPRD
VP1265 -> VBP ADVP
VP -> VP1265 NP
VP1266 -> VBP ADVP
VP -> VP1266 NPPRD
VP1267 -> VBP ADVP
VP -> VP1267 PP
VP1268 -> VBP ADVP
VP -> VP1268 VP
VP1269 -> VBP ADVPTMP
VP -> VP1269 ADJPPRD
VP1270 -> VBP ADVPTMP
VP -> VP1270 NPPRD
VP1271 -> VBP ADVPTMP
VP -> VP1271 PPLOCPRD
VP1272 -> VBP ADVPTMP
VP -> VP1272 VP
VP1273 -> VBP DT
VP -> VP1273 VP
VP1274 -> VBP NP
VP1275 -> VP1274 COMMA
VP -> VP1275 ADVP
VP1276 -> VBP NP
VP1277 -> VP1276 COMMA
VP -> VP1277 PP
VP1278 -> VBP NP
VP1279 -> VP1278 COMMA
VP -> VP1279 SADV
VP1280 -> VBP NP
VP1281 -> VP1280 COMMA
VP -> VP1281 SBARADV
VP1282 -> VBP NP
VP -> VP1282 ADVP
VP1283 -> VBP NP
VP -> VP1283 ADVPTMP
VP1284 -> VBP NP
VP -> VP1284 NP
VP1285 -> VBP NP
VP -> VP1285 NPTMP
VP1286 -> VBP NP
VP -> VP1286 PP
VP1287 -> VBP NP
VP1288 -> VP1287 PP
VP -> VP1288 PP
VP1289 -> VBP NP
VP1290 -> VP1289 PP
VP -> VP1290 SBARTMP
VP1291 -> VBP NP
VP -> VP1291 PPLOC
VP1292 -> VBP NP
VP -> VP1292 PPTMP
VP1293 -> VBP NP
VP -> VP1293 S
VP1294 -> VBP NP
VP -> VP1294 SPRP
VP1295 -> VBP NP
VP -> VP1295 SBAR
VP1296 -> VBP NP
VP -> VP1296 SBARPRP
VP1297 -> VBP NPPRD
VP1298 -> VP1297 COMMA
VP -> VP1298 PP
VP1299 -> VBP PP
VP -> VP1299 PP
VP1300 -> VBP PPTMP
VP -> VP1300 VP
VP1301 -> VBP PRT
VP -> VP1301 NP
VP1302 -> VBP PRT
VP -> VP1302 PP
VP1303 -> VBP RB
VP -> VP1303 ADJPPRD
VP1304 -> VBP RB
VP1305 -> VP1304 ADVP
VP -> VP1305 VP
VP1306 -> VBP RB
VP1307 -> VP1306 ADVPTMP
VP -> VP1307 VP
VP1308 -> VBP RB
VP -> VP1308 NPPRD
VP1309 -> VBP RB
VP -> VP1309 VP
VP1310 -> VBP SBAR
VP1311 -> VP1310 COMMA
VP -> VP1311 SBARADV
VP1312 -> VBP PUNCbquotebquote
VP -> VP1312 NP
VP1313 -> VBZ COMMA
VP -> VP1313 SBARPRD
VP1314 -> VBZ COMMA
VP1315 -> VP1314 PUNCbquotebquote
VP -> VP1315 S
VP1316 -> VBZ COMMA
VP -> VP1316 SADV
VP1317 -> VBZ PUNCcolon
VP1318 -> VP1317 PUNCbquotebquote
VP -> VP1318 S
VP1319 -> VBZ ADJPPRD
VP1320 -> VP1319 COMMA
VP -> VP1320 PP
VP1321 -> VBZ ADJPPRD
VP -> VP1321 PP
VP1322 -> VBZ ADJPPRD
VP -> VP1322 PPLOC
VP1323 -> VBZ ADJPPRD
VP -> VP1323 PPTMP
VP1324 -> VBZ ADJPPRD
VP -> VP1324 S
VP1325 -> VBZ ADJPPRD
VP -> VP1325 SBAR
VP1326 -> VBZ ADJPPRD
VP -> VP1326 SBARADV
VP1327 -> VBZ ADJPPRD
VP -> VP1327 SBARPRP
VP1328 -> VBZ ADVP
VP -> VP1328 ADJPPRD
VP1329 -> VBZ ADVP
VP -> VP1329 NP
VP1330 -> VBZ ADVP
VP -> VP1330 NPPRD
VP1331 -> VBZ ADVP
VP -> VP1331 PP
VP1332 -> VBZ ADVP
VP -> VP1332 PPPRD
VP1333 -> VBZ ADVP
VP -> VP1333 VP
VP1334 -> VBZ ADVPTMP
VP -> VP1334 ADJPPRD
VP1335 -> VBZ ADVPTMP
VP -> VP1335 NPPRD
VP1336 -> VBZ ADVPTMP
VP -> VP1336 S
VP1337 -> VBZ ADVPTMP
VP -> VP1337 VP
VP1338 -> VBZ NP
VP1339 -> VP1338 COMMA
VP -> VP1339 ADVP
VP1340 -> VBZ NP
VP1341 -> VP1340 COMMA
VP -> VP1341 PP
VP1342 -> VBZ NP
VP1343 -> VP1342 COMMA
VP -> VP1343 SADV
VP1344 -> VBZ NP
VP1345 -> VP1344 COMMA
VP -> VP1345 SBARADV
VP1346 -> VBZ NP
VP -> VP1346 ADVP
VP1347 -> VBZ NP
VP -> VP1347 ADVPTMP
VP1348 -> VBZ NP
VP -> VP1348 NP
VP1349 -> VBZ NP
VP -> VP1349 NPTMP
VP1350 -> VBZ NP
VP -> VP1350 PP
VP1351 -> VBZ NP
VP1352 -> VP1351 PP
VP -> VP1352 PP
VP1353 -> VBZ NP
VP -> VP1353 PPLOC
VP1354 -> VBZ NP
VP -> VP1354 PPTMP
VP1355 -> VBZ NP
VP -> VP1355 S
VP1356 -> VBZ NP
VP -> VP1356 SPRP
VP1357 -> VBZ NP
VP -> VP1357 SBAR
VP1358 -> VBZ NP
VP -> VP1358 SBARADV
VP1359 -> VBZ NP
VP -> VP1359 SBARPRP
VP1360 -> VBZ NP
VP -> VP1360 SBARTMP
VP1361 -> VBZ NPPRD
VP1362 -> VP1361 COMMA
VP -> VP1362 PP
VP1363 -> VBZ NPPRD
VP1364 -> VP1363 COMMA
VP -> VP1364 SADV
VP1365 -> VBZ NPPRD
VP1366 -> VP1365 COMMA
VP -> VP1366 SBARADV
VP1367 -> VBZ NPPRD
VP -> VP1367 ADVPTMP
VP1368 -> VBZ NPPRD
VP -> VP1368 PP
VP1369 -> VBZ NPPRD
VP -> VP1369 PPLOC
VP1370 -> VBZ NPPRD
VP -> VP1370 PPTMP
VP1371 -> VBZ NPPRD
VP -> VP1371 S
VP1372 -> VBZ NPPRD
VP -> VP1372 SBAR
VP1373 -> VBZ NPPRD
VP -> VP1373 SBARADV
VP1374 -> VBZ NPPRD
VP -> VP1374 SBARTMP
VP1375 -> VBZ PP
VP1376 -> VP1375 COMMA
VP -> VP1376 SBARADV
VP1377 -> VBZ PP
VP -> VP1377 PP
VP1378 -> VBZ PP
VP -> VP1378 PPLOC
VP1379 -> VBZ PP
VP -> VP1379 SBARTMP
VP1380 -> VBZ PPPRD
VP -> VP1380 PP
VP1381 -> VBZ PPPRD
VP -> VP1381 S
VP1382 -> VBZ PPTMP
VP -> VP1382 VP
VP1383 -> VBZ PRT
VP -> VP1383 NP
VP1384 -> VBZ PRT
VP -> VP1384 PP
VP1385 -> VBZ PRT
VP -> VP1385 SBAR
VP1386 -> VBZ RB
VP -> VP1386 ADJPPRD
VP1387 -> VBZ RB
VP1388 -> VP1387 ADJPPRD
VP -> VP1388 SBAR
VP1389 -> VBZ RB
VP1390 -> VP1389 ADVP
VP -> VP1390 VP
VP1391 -> VBZ RB
VP1392 -> VP1391 ADVPTMP
VP -> VP1392 VP
VP1393 -> VBZ RB
VP -> VP1393 NPPRD
VP1394 -> VBZ RB
VP -> VP1394 PPPRD
VP1395 -> VBZ RB
VP -> VP1395 VP
VP1396 -> VBZ S
VP1397 -> VP1396 COMMA
VP -> VP1397 SADV
VP1398 -> VBZ S
VP1399 -> VP1398 COMMA
VP -> VP1399 SBARADV
VP1400 -> VBZ S
VP -> VP1400 PP
VP1401 -> VBZ S
VP -> VP1401 PPLOC
VP1402 -> VBZ PUNCbquotebquote
VP -> VP1402 ADJPPRD
VP1403 -> VBZ PUNCbquotebquote
VP -> VP1403 NP
VP1404 -> VBZ PUNCbquotebquote
VP -> VP1404 NPPRD
VP1405 -> VBZ PUNCbquotebquote
VP -> VP1405 VP
VP1406 -> VP COMMA
VP1407 -> VP1406 ADVP
VP -> VP1407 VP
VP1408 -> VP COMMA
VP -> VP1408 NP
VP1409 -> VP COMMA
VP -> VP1409 NPADV
VP1410 -> VP COMMA
VP1411 -> VP1410 RB
VP -> VP1411 VP
VP1412 -> VP COMMA
VP -> VP1412 SBAR
VP1413 -> VP COMMA
VP -> VP1413 SBARADV
VP1414 -> VP COMMA
VP -> VP1414 VP
VP1415 -> VP COMMA
VP1416 -> VP1415 VP
VP1417 -> VP1416 COMMA
VP -> VP1417 VP
VP1418 -> VP PUNCcolon
VP -> VP1418 NP
VP1419 -> PUNCbquotebquote VB
VP1420 -> VP1419 PUNCquotequote
VP -> VP1420 NP
ADVPPRD1421 -> RB NP
ADVPPRD -> ADVPPRD1421 PP
ADVP1422 -> IN NP
ADVP -> ADVP1422 PP
ADVP1423 -> QP TO
ADVP -> ADVP1423 QP
ADVP1424 -> RB NP
ADVP -> ADVP1424 PP
ADVP1425 -> RB NP
ADVP -> ADVP1425 PPTMP
ADVP1426 -> RB RB
ADVP -> ADVP1426 RB
ADVPLOC1427 -> NP RB
ADVPLOC -> ADVPLOC1427 PP
NPTMP1428 -> ADVP DT
NPTMP -> NPTMP1428 NN
NPTMP1429 -> DT JJ
NPTMP -> NPTMP1429 NN
NPTMP1430 -> DT NN
NPTMP -> NPTMP1430 NN
NPTMP1431 -> JJ JJ
NPTMP -> NPTMP1431 NN
NPTMP1432 -> JJ NPR
NPTMP -> NPTMP1432 QP
NPTMP1433 -> NP COMMA
NPTMP -> NPTMP1433 NP
NPTMP1434 -> NP COMMA
NPTMP -> NPTMP1434 SBAR
NPTMP1435 -> NPR QP
NPTMP1436 -> NPTMP1435 COMMA
NPTMP -> NPTMP1436 QP
NPTMP1437 -> NPR QP
NPTMP1438 -> NPTMP1437 COMMA
NPTMP1439 -> NPTMP1438 QP
NPTMP -> NPTMP1439 COMMA
NPTMP1440 -> NPR QP
NPTMP1441 -> NPTMP1440 COMMA
NPTMP1442 -> NPTMP1441 QP
NPTMP -> NPTMP1442 PUNCcolon
NPTMP1443 -> RB DT
NPTMP -> NPTMP1443 NN
NPTMP1444 -> RB JJ
NPTMP -> NPTMP1444 NN
NPTMP1445 -> RBR DT
NPTMP -> NPTMP1445 NN
NACLOC1446 -> NPR COMMA
NACLOC -> NACLOC1446 NPR
NACLOC1447 -> NPR COMMA
NACLOC1448 -> NACLOC1447 NPR
NACLOC -> NACLOC1448 COMMA
SINV1449 -> ADJPPRD VP
SINV1450 -> SINV1449 NP
SINV -> SINV1450 PUNCpoint
SINV1451 -> ADVP VP
SINV1452 -> SINV1451 VP
SINV1453 -> SINV1452 NP
SINV -> SINV1453 PUNCpoint
SINV1454 -> ADVPLOCPRD VP
SINV1455 -> SINV1454 NP
SINV -> SINV1455 PUNCpoint
SINV1456 -> ADVPLOCPRD VP
SINV1457 -> SINV1456 NP
SINV -> SINV1457 PUNCcolon
SINV1458 -> MD NP
SINV -> SINV1458 VP
SINV1459 -> PPLOC VP
SINV1460 -> SINV1459 NP
SINV -> SINV1460 PUNCpoint
SINV1461 -> PPLOCPRD VP
SINV1462 -> SINV1461 NP
SINV -> SINV1462 PUNCpoint
SINV1463 -> PPPRD VP
SINV1464 -> SINV1463 NP
SINV -> SINV1464 PUNCpoint
SINV1465 -> S COMMA
SINV1466 -> SINV1465 VP
SINV1467 -> SINV1466 NP
SINV -> SINV1467 PUNCpoint
SINV1468 -> STPC COMMA
SINV1469 -> SINV1468 PUNCquotequote
SINV1470 -> SINV1469 VP
SINV1471 -> SINV1470 NP
SINV -> SINV1471 PUNCpoint
SINV1472 -> STPC COMMA
SINV1473 -> SINV1472 VP
SINV1474 -> SINV1473 NP
SINV -> SINV1474 PUNCpoint
SINV1475 -> STPC VP
SINV1476 -> SINV1475 NP
SINV -> SINV1476 PUNCpoint
SINV1477 -> VBD NP
SINV -> SINV1477 VP
SINV1478 -> VP NP
SINV1479 -> SINV1478 COMMA
SINV1480 -> SINV1479 PUNCbquotebquote
SINV1481 -> SINV1480 S
SINV1482 -> SINV1481 PUNCpoint
SINV -> SINV1482 PUNCquotequote
SINV1483 -> VP NP
SINV1484 -> SINV1483 PUNCcolon
SINV1485 -> SINV1484 PUNCbquotebquote
SINV1486 -> SINV1485 S
SINV -> SINV1486 PUNCpoint
SINV1487 -> VP NP
SINV1488 -> SINV1487 PUNCcolon
SINV1489 -> SINV1488 PUNCbquotebquote
SINV1490 -> SINV1489 S
SINV1491 -> SINV1490 PUNCpoint
SINV -> SINV1491 PUNCquotequote
SINV1492 -> VP VP
SINV1493 -> SINV1492 NP
SINV -> SINV1493 PUNCpoint
SINV1494 -> PUNCbquotebquote S
SINV1495 -> SINV1494 COMMA
SINV1496 -> SINV1495 PUNCquotequote
SINV1497 -> SINV1496 VP
SINV1498 -> SINV1497 NP
SINV -> SINV1498 PUNCpoint
SINV1499 -> PUNCbquotebquote STPC
SINV1500 -> SINV1499 COMMA
SINV1501 -> SINV1500 PUNCquotequote
SINV1502 -> SINV1501 VP
SINV -> SINV1502 NP
SINV1503 -> PUNCbquotebquote STPC
SINV1504 -> SINV1503 COMMA
SINV1505 -> SINV1504 PUNCquotequote
SINV1506 -> SINV1505 VP
SINV1507 -> SINV1506 NP
SINV1508 -> SINV1507 COMMA
SINV1509 -> SINV1508 SADV
SINV -> SINV1509 PUNCpoint
SINV1510 -> PUNCbquotebquote STPC
SINV1511 -> SINV1510 COMMA
SINV1512 -> SINV1511 PUNCquotequote
SINV1513 -> SINV1512 VP
SINV1514 -> SINV1513 NP
SINV -> SINV1514 PUNCpoint
SINV1515 -> PUNCbquotebquote STPC
SINV1516 -> SINV1515 COMMA
SINV1517 -> SINV1516 VP
SINV1518 -> SINV1517 NP
SINV -> SINV1518 PUNCpoint
SBAR1519 -> IN COMMA
SBAR -> SBAR1519 S
SBAR1520 -> IN IN
SBAR -> SBAR1520 S
SBAR1521 -> IN PUNCbquotebquote
SBAR -> SBAR1521 S
SBAR1522 -> RB IN
SBAR -> SBAR1522 S
SBAR1523 -> SBAR COMMA
SBAR -> SBAR1523 SBAR
SBAR1524 -> WHNP COMMA
SBAR -> SBAR1524 S
SBARADV1525 -> ADVP IN
SBARADV -> SBARADV1525 S
SBARADV1526 -> IN COMMA
SBARADV -> SBARADV1526 S
SBARADV1527 -> IN IN
SBARADV -> SBARADV1527 S
SBARADV1528 -> RB IN
SBARADV -> SBARADV1528 S
NPADV1529 -> DT JJ
NPADV -> NPADV1529 NN
WHNP1530 -> WPdollar JJ
WHNP -> WHNP1530 NN
NP1531 -> PUNCcolon NN
NP1532 -> NP1531 NN
NP1533 -> NP1532 NN
NP -> NP1533 PUNCpoint
NP1534 -> PUNCcolon NPR
NP -> NP1534 PUNCpoint
NP1535 -> ADJP ADJP
NP1536 -> NP1535 JJ
NP1537 -> NP1536 JJ
NP1538 -> NP1537 NN
NP -> NP1538 NNS
NP1539 -> ADJP DT
NP -> NP1539 NN
NP1540 -> ADJP JJ
NP -> NP1540 NN
NP1541 -> ADJP JJ
NP1542 -> NP1541 NN
NP -> NP1542 NNS
NP1543 -> ADJP JJ
NP -> NP1543 NNS
NP1544 -> ADJP NN
NP -> NP1544 NN
NP1545 -> ADJP NN
NP -> NP1545 NNS
NP1546 -> DT ADJP
NP1547 -> NP1546 COMMA
NP1548 -> NP1547 JJ
NP -> NP1548 NN
NP1549 -> DT ADJP
NP1550 -> NP1549 ADJP
NP -> NP1550 NN
NP1551 -> DT ADJP
NP1552 -> NP1551 JJ
NP1553 -> NP1552 JJ
NP -> NP1553 NN
NP1554 -> DT ADJP
NP1555 -> NP1554 JJ
NP -> NP1555 NN
NP1556 -> DT ADJP
NP1557 -> NP1556 JJ
NP1558 -> NP1557 NN
NP -> NP1558 NN
NP1559 -> DT ADJP
NP1560 -> NP1559 JJ
NP -> NP1560 NNS
NP1561 -> DT ADJP
NP -> NP1561 NN
NP1562 -> DT ADJP
NP1563 -> NP1562 NN
NP -> NP1563 NN
NP1564 -> DT ADJP
NP1565 -> NP1564 NN
NP1566 -> NP1565 NN
NP -> NP1566 NN
NP1567 -> DT ADJP
NP1568 -> NP1567 NN
NP -> NP1568 NNS
NP1569 -> DT ADJP
NP -> NP1569 NNS
NP1570 -> DT ADJP
NP1571 -> NP1570 NNS
NP -> NP1571 NN
NP1572 -> DT ADJP
NP -> NP1572 NPR
NP1573 -> DT ADJP
NP1574 -> NP1573 NPR
NP -> NP1574 NP
NP1575 -> DT ADJP
NP1576 -> NP1575 QP
NP -> NP1576 NN
NP1577 -> DT ADJP
NP -> NP1577 QPMONEY
NP1578 -> DT ADVP
NP -> NP1578 NN
NP1579 -> DT DT
NP1580 -> NP1579 JJ
NP -> NP1580 NNS
NP1581 -> DT DT
NP -> NP1581 NN
NP1582 -> DT DT
NP -> NP1582 NNS
NP1583 -> DT JJ
NP1584 -> NP1583 COMMA
NP1585 -> NP1584 JJ
NP1586 -> NP1585 JJ
NP -> NP1586 NN
NP1587 -> DT JJ
NP1588 -> NP1587 COMMA
NP1589 -> NP1588 JJ
NP -> NP1589 NN
NP1590 -> DT JJ
NP1591 -> NP1590 COMMA
NP1592 -> NP1591 JJ
NP -> NP1592 NNS
NP1593 -> DT JJ
NP1594 -> NP1593 COMMA
NP1595 -> NP1594 JJ
NP1596 -> NP1595 NPR
NP -> NP1596 NP
NP1597 -> DT JJ
NP1598 -> NP1597 ADJP
NP1599 -> NP1598 JJ
NP -> NP1599 NN
NP1600 -> DT JJ
NP1601 -> NP1600 ADJP
NP -> NP1601 NN
NP1602 -> DT JJ
NP1603 -> NP1602 ADJP
NP1604 -> NP1603 NN
NP -> NP1604 NN
NP1605 -> DT JJ
NP -> NP1605 DT
NP1606 -> DT JJ
NP -> NP1606 JJ
NP1607 -> DT JJ
NP1608 -> NP1607 JJ
NP1609 -> NP1608 JJ
NP -> NP1609 NN
NP1610 -> DT JJ
NP1611 -> NP1610 JJ
NP1612 -> NP1611 JJ
NP1613 -> NP1612 NN
NP -> NP1613 NN
NP1614 -> DT JJ
NP1615 -> NP1614 JJ
NP -> NP1615 NN
NP1616 -> DT JJ
NP1617 -> NP1616 JJ
NP1618 -> NP1617 NN
NP -> NP1618 NN
NP1619 -> DT JJ
NP1620 -> NP1619 JJ
NP1621 -> NP1620 NN
NP1622 -> NP1621 NN
NP -> NP1622 NN
NP1623 -> DT JJ
NP1624 -> NP1623 JJ
NP1625 -> NP1624 NN
NP -> NP1625 NNS
NP1626 -> DT JJ
NP1627 -> NP1626 JJ
NP -> NP1627 NNS
NP1628 -> DT JJ
NP1629 -> NP1628 JJ
NP1630 -> NP1629 NNS
NP -> NP1630 NN
NP1631 -> DT JJ
NP1632 -> NP1631 JJ
NP -> NP1632 NPR
NP1633 -> DT JJ
NP1634 -> NP1633 JJ
NP1635 -> NP1634 NPR
NP -> NP1635 NP
NP1636 -> DT JJ
NP -> NP1636 NN
NP1637 -> DT JJ
NP1638 -> NP1637 NN
NP1639 -> NP1638 JJ
NP -> NP1639 NN
NP1640 -> DT JJ
NP1641 -> NP1640 NN
NP -> NP1641 NN
NP1642 -> DT JJ
NP1643 -> NP1642 NN
NP1644 -> NP1643 NN
NP -> NP1644 NN
NP1645 -> DT JJ
NP1646 -> NP1645 NN
NP1647 -> NP1646 NN
NP -> NP1647 NNS
NP1648 -> DT JJ
NP1649 -> NP1648 NN
NP -> NP1649 NNS
NP1650 -> DT JJ
NP1651 -> NP1650 NN
NP1652 -> NP1651 NNS
NP -> NP1652 NN
NP1653 -> DT JJ
NP1654 -> NP1653 NN
NP -> NP1654 NPR
NP1655 -> DT JJ
NP1656 -> NP1655 NN
NP -> NP1656 S
NP1657 -> DT JJ
NP1658 -> NP1657 NN
NP -> NP1658 SBAR
NP1659 -> DT JJ
NP -> NP1659 NNS
NP1660 -> DT JJ
NP1661 -> NP1660 NNS
NP -> NP1661 NN
NP1662 -> DT JJ
NP1663 -> NP1662 NNS
NP1664 -> NP1663 NN
NP -> NP1664 NN
NP1665 -> DT JJ
NP1666 -> NP1665 NNS
NP -> NP1666 NNS
NP1667 -> DT JJ
NP -> NP1667 NPR
NP1668 -> DT JJ
NP1669 -> NP1668 NPR
NP1670 -> NP1669 JJ
NP -> NP1670 NN
NP1671 -> DT JJ
NP1672 -> NP1671 NPR
NP -> NP1672 NP
NP1673 -> DT JJ
NP -> NP1673 NPRS
NP1674 -> DT JJ
NP -> NP1674 QP
NP1675 -> DT JJ
NP1676 -> NP1675 QP
NP1677 -> NP1676 JJ
NP -> NP1677 NNS
NP1678 -> DT JJ
NP1679 -> NP1678 QP
NP -> NP1679 NN
NP1680 -> DT JJ
NP1681 -> NP1680 QP
NP1682 -> NP1681 NN
NP -> NP1682 NN
NP1683 -> DT JJ
NP1684 -> NP1683 QP
NP -> NP1684 NNS
NP1685 -> DT JJ
NP -> NP1685 QPMONEY
NP1686 -> DT JJ
NP1687 -> NP1686 VBG
NP -> NP1687 NN
NP1688 -> DT JJ
NP1689 -> NP1688 VBN
NP -> NP1689 NN
NP1690 -> DT JJR
NP1691 -> NP1690 JJ
NP -> NP1691 NN
NP1692 -> DT JJR
NP -> NP1692 NN
NP1693 -> DT JJR
NP1694 -> NP1693 NN
NP -> NP1694 NN
NP1695 -> DT JJR
NP -> NP1695 NNS
NP1696 -> DT JJS
NP1697 -> NP1696 JJ
NP -> NP1697 NN
NP1698 -> DT JJS
NP1699 -> NP1698 JJ
NP -> NP1699 NNS
NP1700 -> DT JJS
NP -> NP1700 NN
NP1701 -> DT JJS
NP1702 -> NP1701 NN
NP -> NP1702 NN
NP1703 -> DT JJS
NP1704 -> NP1703 NN
NP -> NP1704 NNS
NP1705 -> DT JJS
NP -> NP1705 NNS
NP1706 -> DT JJS
NP1707 -> NP1706 QP
NP -> NP1707 NNS
NP1708 -> DT NAC
NP -> NP1708 NN
NP1709 -> DT NAC
NP -> NP1709 NPR
NP1710 -> DT NACLOC
NP1711 -> NP1710 JJ
NP -> NP1711 NN
NP1712 -> DT NACLOC
NP -> NP1712 NN
NP1713 -> DT NACLOC
NP1714 -> NP1713 NN
NP -> NP1714 NN
NP1715 -> DT NACTMP
NP -> NP1715 NN
NP1716 -> DT NN
NP -> NP1716 JJ
NP1717 -> DT NN
NP -> NP1717 NN
NP1718 -> DT NN
NP1719 -> NP1718 NN
NP -> NP1719 NN
NP1720 -> DT NN
NP1721 -> NP1720 NN
NP1722 -> NP1721 NN
NP -> NP1722 NN
NP1723 -> DT NN
NP1724 -> NP1723 NN
NP -> NP1724 NNS
NP1725 -> DT NN
NP1726 -> NP1725 NN
NP -> NP1726 NPR
NP1727 -> DT NN
NP1728 -> NP1727 NN
NP -> NP1728 S
NP1729 -> DT NN
NP -> NP1729 NNS
NP1730 -> DT NN
NP1731 -> NP1730 NNS
NP -> NP1731 NN
NP1732 -> DT NN
NP -> NP1732 NPR
NP1733 -> DT NN
NP1734 -> NP1733 NPR
NP -> NP1734 NP
NP1735 -> DT NN
NP -> NP1735 QP
NP1736 -> DT NN
NP1737 -> NP1736 QP
NP -> NP1737 NN
NP1738 -> DT NN
NP -> NP1738 QPMONEY
NP1739 -> DT NN
NP -> NP1739 RB
NP1740 -> DT NN
NP -> NP1740 S
NP1741 -> DT NN
NP -> NP1741 SBAR
NP1742 -> DT NN
NP1743 -> NP1742 VBG
NP -> NP1743 NN
NP1744 -> DT NN
NP -> NP1744 VBZ
NP1745 -> DT NNS
NP -> NP1745 NN
NP1746 -> DT NNS
NP1747 -> NP1746 NN
NP -> NP1747 NN
NP1748 -> DT NNS
NP -> NP1748 NNS
NP1749 -> DT NNS
NP -> NP1749 S
NP1750 -> DT NNS
NP -> NP1750 SBAR
NP1751 -> DT NP
NP -> NP1751 NN
NP1752 -> DT NPdollar
NP -> NP1752 NN
NP1753 -> DT NPR
NP1754 -> NP1753 JJ
NP -> NP1754 NN
NP1755 -> DT NPR
NP1756 -> NP1755 JJ
NP1757 -> NP1756 NN
NP -> NP1757 NN
NP1758 -> DT NPR
NP1759 -> NP1758 JJ
NP1760 -> NP1759 NN
NP1761 -> NP1760 NN
NP -> NP1761 NN
NP1762 -> DT NPR
NP1763 -> NP1762 JJ
NP -> NP1763 NNS
NP1764 -> DT NPR
NP -> NP1764 NP
NP1765 -> DT NPR
NP1766 -> NP1765 NP
NP -> NP1766 S
NP1767 -> DT NPR
NP -> NP1767 QP
NP1768 -> DT NPR
NP1769 -> NP1768 QP
NP -> NP1769 NN
NP1770 -> DT NPR
NP1771 -> NP1770 QP
NP -> NP1771 NNS
NP1772 -> DT NPR
NP1773 -> NP1772 QP
NP -> NP1773 NPR
NP1774 -> DT NPR
NP1775 -> NP1774 VBG
NP -> NP1775 NN
NP1776 -> DT NPRS
NP -> NP1776 NP
NP1777 -> DT QP
NP1778 -> NP1777 JJ
NP -> NP1778 NN
NP1779 -> DT QP
NP1780 -> NP1779 JJ
NP1781 -> NP1780 NN
NP -> NP1781 NN
NP1782 -> DT QP
NP1783 -> NP1782 JJ
NP1784 -> NP1783 NN
NP -> NP1784 NNS
NP1785 -> DT QP
NP1786 -> NP1785 JJ
NP -> NP1786 NNS
NP1787 -> DT QP
NP -> NP1787 NN
NP1788 -> DT QP
NP1789 -> NP1788 NN
NP -> NP1789 NN
NP1790 -> DT QP
NP1791 -> NP1790 NN
NP -> NP1791 NNS
NP1792 -> DT QP
NP -> NP1792 NNS
NP1793 -> DT QP
NP -> NP1793 NPR
NP1794 -> DT QP
NP1795 -> NP1794 NPR
NP -> NP1795 NP
NP1796 -> DT QP
NP -> NP1796 NPRS
NP1797 -> DT RB
NP1798 -> NP1797 JJ
NP -> NP1798 NN
NP1799 -> DT RB
NP1800 -> NP1799 JJ
NP1801 -> NP1800 NN
NP -> NP1801 NN
NP1802 -> DT RBR
NP1803 -> NP1802 JJ
NP -> NP1803 NN
NP1804 -> DT RBS
NP1805 -> NP1804 JJ
NP -> NP1805 NN
NP1806 -> DT RBS
NP1807 -> NP1806 JJ
NP -> NP1807 NNS
NP1808 -> DT VBG
NP1809 -> NP1808 JJ
NP -> NP1809 NN
NP1810 -> DT VBG
NP -> NP1810 NN
NP1811 -> DT VBG
NP1812 -> NP1811 NN
NP -> NP1812 NN
NP1813 -> DT VBG
NP -> NP1813 NNS
NP1814 -> DT VBG
NP -> NP1814 NPR
NP1815 -> DT VBG
NP1816 -> NP1815 NPR
NP -> NP1816 NP
NP1817 -> DT VBN
NP1818 -> NP1817 JJ
NP -> NP1818 NN
NP1819 -> DT VBN
NP1820 -> NP1819 JJ
NP1821 -> NP1820 NN
NP -> NP1821 NN
NP1822 -> DT VBN
NP -> NP1822 NN
NP1823 -> DT VBN
NP1824 -> NP1823 NN
NP -> NP1824 NN
NP1825 -> DT VBN
NP -> NP1825 NNS
NP1826 -> DT VBN
NP -> NP1826 NPR
NP1827 -> DT VBN
NP1828 -> NP1827 NPR
NP -> NP1828 NP
NP1829 -> DT VBN
NP -> NP1829 QP
NP1830 -> DT VBN
NP1831 -> NP1830 QP
NP -> NP1831 NN
NP1832 -> DT VBN
NP1833 -> NP1832 QP
NP -> NP1833 NNS
NP1834 -> DT VBN
NP -> NP1834 QPMONEY
NP1835 -> DT PUNCbquotebquote
NP1836 -> NP1835 JJ
NP1837 -> NP1836 PUNCquotequote
NP -> NP1837 NN
NP1838 -> DT PUNCbquotebquote
NP1839 -> NP1838 JJ
NP -> NP1839 NN
NP1840 -> DT PUNCbquotebquote
NP1841 -> NP1840 JJ
NP1842 -> NP1841 NN
NP -> NP1842 PUNCquotequote
NP1843 -> DT PUNCbquotebquote
NP1844 -> NP1843 JJ
NP1845 -> NP1844 NN
NP1846 -> NP1845 NN
NP -> NP1846 PUNCquotequote
NP1847 -> DT PUNCbquotebquote
NP -> NP1847 NN
NP1848 -> DT PUNCbquotebquote
NP1849 -> NP1848 NN
NP -> NP1849 PUNCquotequote
NP1850 -> DT PUNCbquotebquote
NP1851 -> NP1850 NN
NP1852 -> NP1851 PUNCquotequote
NP -> NP1852 NN
NP1853 -> DT PUNCbquotebquote
NP1854 -> NP1853 NN
NP1855 -> NP1854 NN
NP -> NP1855 PUNCquotequote
NP1856 -> DT PUNCbquotebquote
NP -> NP1856 NPR
NP1857 -> IN QP
NP -> NP1857 NNS
NP1858 -> JJ COMMA
NP1859 -> NP1858 JJ
NP -> NP1859 NN
NP1860 -> JJ COMMA
NP1861 -> NP1860 JJ
NP1862 -> NP1861 NN
NP1863 -> NP1862 NN
NP -> NP1863 NNS
NP1864 -> JJ COMMA
NP1865 -> NP1864 JJ
NP -> NP1865 NNS
NP1866 -> JJ ADJP
NP -> NP1866 NNS
NP1867 -> JJ DT
NP1868 -> NP1867 JJ
NP -> NP1868 NN
NP1869 -> JJ DT
NP -> NP1869 NN
NP1870 -> JJ JJ
NP1871 -> NP1870 JJ
NP -> NP1871 NN
NP1872 -> JJ JJ
NP1873 -> NP1872 JJ
NP1874 -> NP1873 NN
NP -> NP1874 NNS
NP1875 -> JJ JJ
NP1876 -> NP1875 JJ
NP -> NP1876 NNS
NP1877 -> JJ JJ
NP -> NP1877 NN
NP1878 -> JJ JJ
NP1879 -> NP1878 NN
NP -> NP1879 NN
NP1880 -> JJ JJ
NP1881 -> NP1880 NN
NP -> NP1881 NNS
NP1882 -> JJ JJ
NP1883 -> NP1882 NN
NP -> NP1883 NPR
NP1884 -> JJ JJ
NP -> NP1884 NNS
NP1885 -> JJ JJ
NP1886 -> NP1885 NNS
NP -> NP1886 NNS
NP1887 -> JJ JJ
NP1888 -> NP1887 NPR
NP -> NP1888 NP
NP1889 -> JJ NN
NP -> NP1889 PUNCcolon
NP1890 -> JJ NN
NP -> NP1890 NN
NP1891 -> JJ NN
NP1892 -> NP1891 NN
NP -> NP1892 NN
NP1893 -> JJ NN
NP1894 -> NP1893 NN
NP -> NP1894 NNS
NP1895 -> JJ NN
NP1896 -> NP1895 NN
NP -> NP1896 NPR
NP1897 -> JJ NN
NP -> NP1897 NNS
NP1898 -> JJ NN
NP -> NP1898 NPR
NP1899 -> JJ NN
NP -> NP1899 S
NP1900 -> JJ NN
NP -> NP1900 SBAR
NP1901 -> JJ NNS
NP -> NP1901 PUNCcolon
NP1902 -> JJ NNS
NP -> NP1902 NN
NP1903 -> JJ NNS
NP -> NP1903 NNS
NP1904 -> JJ NNS
NP -> NP1904 S
NP1905 -> JJ NNS
NP -> NP1905 SBAR
NP1906 -> JJ NPR
NP -> NP1906 NP
NP1907 -> JJ NPR
NP1908 -> NP1907 NP
NP1909 -> NP1908 JJ
NP -> NP1909 NNS
NP1910 -> JJ QP
NP -> NP1910 NNS
NP1911 -> JJ VBG
NP -> NP1911 NNS
NP1912 -> JJ VBN
NP -> NP1912 NNS
NP1913 -> JJR JJ
NP -> NP1913 NN
NP1914 -> JJR JJ
NP -> NP1914 NNS
NP1915 -> JJR NN
NP -> NP1915 NN
NP1916 -> JJR NN
NP -> NP1916 NNS
NP1917 -> JJR NPR
NP -> NP1917 NP
NP1918 -> JJS JJ
NP -> NP1918 NNS
NP1919 -> JJS NN
NP -> NP1919 NNS
NP1920 -> JJS NPR
NP -> NP1920 NP
NP1921 -> NN JJ
NP -> NP1921 NN
NP1922 -> NN JJ
NP -> NP1922 NNS
NP1923 -> NN NN
NP -> NP1923 NN
NP1924 -> NN NN
NP1925 -> NP1924 NN
NP -> NP1925 NN
NP1926 -> NN NN
NP1927 -> NP1926 NN
NP -> NP1927 NNS
NP1928 -> NN NN
NP -> NP1928 NNS
NP1929 -> NN NN
NP -> NP1929 NPR
NP1930 -> NN NNS
NP -> NP1930 PUNCcolon
NP1931 -> NN NNS
NP1932 -> NP1931 PUNCcolon
NP -> NP1932 PUNCpoint
NP1933 -> NN NNS
NP -> NP1933 NN
NP1934 -> NN NNS
NP -> NP1934 NNS
NP1935 -> NN VBN
NP -> NP1935 NNS
NP1936 -> NNS QP
NP -> NP1936 PUNCpoint
NP1937 -> NP PUNCquotequote
NP -> NP1937 PP
NP1938 -> NP PUNCquotequote
NP -> NP1938 PPLOC
NP1939 -> NP PUNCquotequote
NP -> NP1939 SBAR
NP1940 -> NP COMMA
NP1941 -> NP1940 PUNCquotequote
NP -> NP1941 NP
NP1942 -> NP COMMA
NP1943 -> NP1942 PUNCquotequote
NP -> NP1943 SBAR
NP1944 -> NP COMMA
NP -> NP1944 ADJP
NP1945 -> NP COMMA
NP1946 -> NP1945 ADJP
NP -> NP1946 COMMA
NP1947 -> NP COMMA
NP1948 -> NP1947 ADJP
NP1949 -> NP1948 COMMA
NP -> NP1949 S
NP1950 -> NP COMMA
NP -> NP1950 ADVP
NP1951 -> NP COMMA
NP1952 -> NP1951 ADVP
NP -> NP1952 COMMA
NP1953 -> NP COMMA
NP1954 -> NP1953 ADVP
NP -> NP1954 NP
NP1955 -> NP COMMA
NP1956 -> NP1955 ADVP
NP1957 -> NP1956 NP
NP -> NP1957 COMMA
NP1958 -> NP COMMA
NP -> NP1958 ADVPLOC
NP1959 -> NP COMMA
NP1960 -> NP1959 ADVPTMP
NP -> NP1960 NP
NP1961 -> NP COMMA
NP -> NP1961 NP
NP1962 -> NP COMMA
NP1963 -> NP1962 NP
NP -> NP1963 COMMA
NP1964 -> NP COMMA
NP1965 -> NP1964 NP
NP1966 -> NP1965 COMMA
NP -> NP1966 PUNCquotequote
NP1967 -> NP COMMA
NP1968 -> NP1967 NP
NP1969 -> NP1968 COMMA
NP -> NP1969 NP
NP1970 -> NP COMMA
NP1971 -> NP1970 NP
NP1972 -> NP1971 COMMA
NP1973 -> NP1972 NP
NP -> NP1973 COMMA
NP1974 -> NP COMMA
NP1975 -> NP1974 NP
NP1976 -> NP1975 COMMA
NP1977 -> NP1976 NP
NP1978 -> NP1977 COMMA
NP -> NP1978 NP
NP1979 -> NP COMMA
NP1980 -> NP1979 NP
NP1981 -> NP1980 COMMA
NP -> NP1981 PP
NP1982 -> NP COMMA
NP1983 -> NP1982 NP
NP1984 -> NP1983 COMMA
NP1985 -> NP1984 PP
NP -> NP1985 PUNCpoint
NP1986 -> NP COMMA
NP1987 -> NP1986 NP
NP1988 -> NP1987 COMMA
NP -> NP1988 SBAR
NP1989 -> NP COMMA
NP1990 -> NP1989 NP
NP -> NP1990 PUNCpoint
NP1991 -> NP COMMA
NP1992 -> NP1991 NP
NP -> NP1992 PUNCcolon
NP1993 -> NP COMMA
NP1994 -> NP1993 NP
NP -> NP1994 SBAR
NP1995 -> NP COMMA
NP -> NP1995 NPLOC
NP1996 -> NP COMMA
NP1997 -> NP1996 NPLOC
NP -> NP1997 COMMA
NP1998 -> NP COMMA
NP1999 -> NP1998 NPLOC
NP2000 -> NP1999 COMMA
NP2001 -> NP2000 NP
NP2002 -> NP2001 COMMA
NP2003 -> NP2002 NP
NP2004 -> NP2003 COMMA
NP2005 -> NP2004 NP
NP -> NP2005 COMMA
NP2006 -> NP COMMA
NP2007 -> NP2006 NPLOC
NP2008 -> NP2007 COMMA
NP -> NP2008 SBAR
NP2009 -> NP COMMA
NP2010 -> NP2009 NPLOC
NP -> NP2010 SBAR
NP2011 -> NP COMMA
NP -> NP2011 PP
NP2012 -> NP COMMA
NP2013 -> NP2012 PP
NP -> NP2013 COMMA
NP2014 -> NP COMMA
NP2015 -> NP2014 PP
NP2016 -> NP2015 COMMA
NP -> NP2016 SBAR
NP2017 -> NP COMMA
NP2018 -> NP2017 PP
NP -> NP2018 PUNCpoint
NP2019 -> NP COMMA
NP -> NP2019 PPLOC
NP2020 -> NP COMMA
NP2021 -> NP2020 PPLOC
NP -> NP2021 COMMA
NP2022 -> NP COMMA
NP -> NP2022 PPTMP
NP2023 -> NP COMMA
NP2024 -> NP2023 RB
NP -> NP2024 NP
NP2025 -> NP COMMA
NP2026 -> NP2025 RB
NP2027 -> NP2026 NP
NP -> NP2027 COMMA
NP2028 -> NP COMMA
NP -> NP2028 RRC
NP2029 -> NP COMMA
NP2030 -> NP2029 RRC
NP -> NP2030 COMMA
NP2031 -> NP COMMA
NP -> NP2031 SBAR
NP2032 -> NP COMMA
NP2033 -> NP2032 SBAR
NP -> NP2033 COMMA
NP2034 -> NP COMMA
NP -> NP2034 SBARLOC
NP2035 -> NP COMMA
NP -> NP2035 SBARTMP
NP2036 -> NP COMMA
NP -> NP2036 VP
NP2037 -> NP COMMA
NP2038 -> NP2037 VP
NP -> NP2038 COMMA
NP2039 -> NP COMMA
NP2040 -> NP2039 VP
NP2041 -> NP2040 COMMA
NP -> NP2041 PUNCquotequote
NP2042 -> NP COMMA
NP2043 -> NP2042 VP
NP2044 -> NP2043 COMMA
NP -> NP2044 SBAR
NP2045 -> NP COMMA
NP2046 -> NP2045 PUNCbquotebquote
NP -> NP2046 S
NP2047 -> NP PUNCLRB
NP2048 -> NP2047 NP
NP -> NP2048 PUNCRRB
NP2049 -> NP PUNCLRB
NP2050 -> NP2049 PP
NP -> NP2050 PUNCRRB
NP2051 -> NP PUNCcolon
NP -> NP2051 NP
NP2052 -> NP PUNCcolon
NP2053 -> NP2052 NP
NP2054 -> NP2053 COMMA
NP2055 -> NP2054 PP
NP -> NP2055 PUNCpoint
NP2056 -> NP PUNCcolon
NP2057 -> NP2056 NP
NP -> NP2057 PUNCpoint
NP2058 -> NP PUNCcolon
NP2059 -> NP2058 NP
NP -> NP2059 PUNCcolon
NP2060 -> NP PUNCcolon
NP2061 -> NP2060 NP
NP2062 -> NP2061 PUNCcolon
NP -> NP2062 NP
NP2063 -> NP PUNCcolon
NP2064 -> NP2063 NP
NP2065 -> NP2064 PUNCcolon
NP2066 -> NP2065 NP
NP -> NP2066 PUNCpoint
NP2067 -> NP PUNCcolon
NP2068 -> NP2067 NP
NP2069 -> NP2068 PUNCcolon
NP2070 -> NP2069 NP
NP2071 -> NP2070 PUNCcolon
NP -> NP2071 NP
NP2072 -> NP PUNCcolon
NP2073 -> NP2072 NP
NP2074 -> NP2073 PUNCcolon
NP2075 -> NP2074 NP
NP2076 -> NP2075 PUNCcolon
NP2077 -> NP2076 NP
NP2078 -> NP2077 PUNCcolon
NP -> NP2078 NP
NP2079 -> NP PUNCcolon
NP2080 -> NP2079 NP
NP2081 -> NP2080 PUNCcolon
NP2082 -> NP2081 NP
NP2083 -> NP2082 PUNCcolon
NP2084 -> NP2083 NP
NP2085 -> NP2084 PUNCcolon
NP2086 -> NP2085 NP
NP2087 -> NP2086 PUNCcolon
NP -> NP2087 NP
NP2088 -> NP PUNCcolon
NP2089 -> NP2088 NP
NP2090 -> NP2089 PUNCcolon
NP2091 -> NP2090 NP
NP2092 -> NP2091 PUNCcolon
NP2093 -> NP2092 NP
NP2094 -> NP2093 PUNCcolon
NP2095 -> NP2094 NP
NP2096 -> NP2095 PUNCcolon
NP2097 -> NP2096 NP
NP2098 -> NP2097 PUNCcolon
NP -> NP2098 NP
NP2099 -> NP PUNCcolon
NP2100 -> NP2099 RB
NP2101 -> NP2100 NP
NP -> NP2101 PUNCpoint
NP2102 -> NP PUNCcolon
NP -> NP2102 S
NP2103 -> NP PUNCcolon
NP2104 -> NP2103 S
NP -> NP2104 PUNCpoint
NP2105 -> NP PUNCcolon
NP -> NP2105 SBAR
NP2106 -> NP PUNCcolon
NP2107 -> NP2106 SBAR
NP -> NP2107 PUNCcolon
NP2108 -> NP ADJP
NP2109 -> NP2108 COMMA
NP -> NP2109 PP
NP2110 -> NP ADJP
NP2111 -> NP2110 COMMA
NP -> NP2111 VP
NP2112 -> NP ADJP
NP -> NP2112 PUNCpoint
NP2113 -> NP ADJP
NP -> NP2113 PP
NP2114 -> NP ADVPTMP
NP -> NP2114 PP
NP2115 -> NP NP
NP2116 -> NP2115 COMMA
NP -> NP2116 ADVP
NP2117 -> NP NP
NP -> NP2117 PUNCpoint
NP2118 -> NP NPADV
NP -> NP2118 PP
NP2119 -> NP NPLOC
NP -> NP2119 PUNCpoint
NP2120 -> NP NPTMP
NP -> NP2120 PP
NP2121 -> NP NPTMP
NP2122 -> NP2121 PP
NP -> NP2122 PP
NP2123 -> NP NPTMP
NP -> NP2123 PPLOC
NP2124 -> NP NPTMP
NP -> NP2124 SBAR
NP2125 -> NP PP
NP -> NP2125 PUNCquotequote
NP2126 -> NP PP
NP2127 -> NP2126 COMMA
NP -> NP2127 ADJP
NP2128 -> NP PP
NP2129 -> NP2128 COMMA
NP2130 -> NP2129 ADJP
NP -> NP2130 COMMA
NP2131 -> NP PP
NP2132 -> NP2131 COMMA
NP -> NP2132 ADVP
NP2133 -> NP PP
NP2134 -> NP2133 COMMA
NP -> NP2134 NP
NP2135 -> NP PP
NP2136 -> NP2135 COMMA
NP -> NP2136 PP
NP2137 -> NP PP
NP2138 -> NP2137 COMMA
NP2139 -> NP2138 PP
NP -> NP2139 COMMA
NP2140 -> NP PP
NP2141 -> NP2140 COMMA
NP -> NP2141 PPLOC
NP2142 -> NP PP
NP2143 -> NP2142 COMMA
NP -> NP2143 SBAR
NP2144 -> NP PP
NP2145 -> NP2144 COMMA
NP2146 -> NP2145 SBAR
NP -> NP2146 COMMA
NP2147 -> NP PP
NP2148 -> NP2147 COMMA
NP -> NP2148 VP
NP2149 -> NP PP
NP2150 -> NP2149 COMMA
NP2151 -> NP2150 VP
NP -> NP2151 COMMA
NP2152 -> NP PP
NP -> NP2152 PUNCpoint
NP2153 -> NP PP
NP -> NP2153 ADJP
NP2154 -> NP PP
NP -> NP2154 ADVP
NP2155 -> NP PP
NP -> NP2155 ADVPLOC
NP2156 -> NP PP
NP -> NP2156 ADVPTMP
NP2157 -> NP PP
NP -> NP2157 NPADV
NP2158 -> NP PP
NP -> NP2158 NPTMP
NP2159 -> NP PP
NP -> NP2159 PP
NP2160 -> NP PP
NP2161 -> NP2160 PP
NP -> NP2161 PUNCpoint
NP2162 -> NP PP
NP2163 -> NP2162 PP
NP -> NP2163 PP
NP2164 -> NP PP
NP2165 -> NP2164 PP
NP -> NP2165 PPTMP
NP2166 -> NP PP
NP -> NP2166 PPLOC
NP2167 -> NP PP
NP2168 -> NP2167 PPLOC
NP -> NP2168 PUNCpoint
NP2169 -> NP PP
NP -> NP2169 PPTMP
NP2170 -> NP PP
NP2171 -> NP2170 PPTMP
NP -> NP2171 PP
NP2172 -> NP PP
NP2173 -> NP2172 PPTMP
NP -> NP2173 PPTMP
NP2174 -> NP PP
NP -> NP2174 PRN
NP2175 -> NP PP
NP -> NP2175 S
NP2176 -> NP PP
NP -> NP2176 SBAR
NP2177 -> NP PP
NP -> NP2177 SBARTMP
NP2178 -> NP PP
NP -> NP2178 VP
NP2179 -> NP PPLOC
NP2180 -> NP2179 COMMA
NP -> NP2180 PP
NP2181 -> NP PPLOC
NP2182 -> NP2181 COMMA
NP -> NP2182 SBAR
NP2183 -> NP PPLOC
NP2184 -> NP2183 COMMA
NP2185 -> NP2184 SBAR
NP -> NP2185 COMMA
NP2186 -> NP PPLOC
NP -> NP2186 NPTMP
NP2187 -> NP PPLOC
NP -> NP2187 PP
NP2188 -> NP PPLOC
NP2189 -> NP2188 PP
NP -> NP2189 PP
NP2190 -> NP PPLOC
NP -> NP2190 PPLOC
NP2191 -> NP PPLOC
NP -> NP2191 PPTMP
NP2192 -> NP PPLOC
NP -> NP2192 SBAR
NP2193 -> NP PPLOC
NP -> NP2193 SBARTMP
NP2194 -> NP PPLOC
NP -> NP2194 VP
NP2195 -> NP PPTMP
NP -> NP2195 PP
NP2196 -> NP PPTMP
NP -> NP2196 SBAR
NP2197 -> NP PRN
NP2198 -> NP2197 COMMA
NP2199 -> NP2198 NP
NP -> NP2199 COMMA
NP2200 -> NP PRN
NP2201 -> NP2200 COMMA
NP -> NP2201 SBAR
NP2202 -> NP PRN
NP -> NP2202 PUNCcolon
NP2203 -> NP PRN
NP2204 -> NP2203 PUNCcolon
NP2205 -> NP2204 NP
NP -> NP2205 PUNCpoint
NP2206 -> NP PRN
NP -> NP2206 PP
NP2207 -> NP PRN
NP -> NP2207 SBAR
NP2208 -> NP PRN
NP -> NP2208 VP
NP2209 -> NP QP
NP -> NP2209 PUNCpoint
NP2210 -> NP SBAR
NP2211 -> NP2210 COMMA
NP -> NP2211 PP
NP2212 -> NP SBAR
NP -> NP2212 PP
NP2213 -> NP SBAR
NP -> NP2213 SBAR
NP2214 -> NP VP
NP2215 -> NP2214 COMMA
NP -> NP2215 PP
NP2216 -> NP VP
NP2217 -> NP2216 COMMA
NP -> NP2217 SBAR
NP2218 -> NP VP
NP -> NP2218 PUNCpoint
NP2219 -> NP VP
NP -> NP2219 PUNCcolon
NP2220 -> NP VP
NP -> NP2220 SBAR
NP2221 -> NP PUNCbquotebquote
NP -> NP2221 NP
NP2222 -> NP PUNCbquotebquote
NP2223 -> NP2222 NPR
NP -> NP2223 PUNCquotequote
NP2224 -> NP PUNCbquotebquote
NP2225 -> NP2224 S
NP -> NP2225 PUNCquotequote
NP2226 -> NP PUNCbquotebquote
NP -> NP2226 SBAR
NP2227 -> NPdollar ADJP
NP2228 -> NP2227 JJ
NP -> NP2228 NN
NP2229 -> NPdollar ADJP
NP -> NP2229 NN
NP2230 -> NPdollar ADJP
NP2231 -> NP2230 NN
NP -> NP2231 NN
NP2232 -> NPdollar ADJP
NP -> NP2232 NNS
NP2233 -> NPdollar JJ
NP2234 -> NP2233 ADJP
NP -> NP2234 NN
NP2235 -> NPdollar JJ
NP2236 -> NP2235 JJ
NP2237 -> NP2236 JJ
NP -> NP2237 NN
NP2238 -> NPdollar JJ
NP2239 -> NP2238 JJ
NP -> NP2239 NN
NP2240 -> NPdollar JJ
NP2241 -> NP2240 JJ
NP2242 -> NP2241 NN
NP -> NP2242 NN
NP2243 -> NPdollar JJ
NP2244 -> NP2243 JJ
NP -> NP2244 NNS
NP2245 -> NPdollar JJ
NP -> NP2245 NN
NP2246 -> NPdollar JJ
NP2247 -> NP2246 NN
NP -> NP2247 NN
NP2248 -> NPdollar JJ
NP2249 -> NP2248 NN
NP -> NP2249 NNS
NP2250 -> NPdollar JJ
NP2251 -> NP2250 NN
NP -> NP2251 S
NP2252 -> NPdollar JJ
NP -> NP2252 NNS
NP2253 -> NPdollar JJ
NP2254 -> NP2253 NNS
NP -> NP2254 NN
NP2255 -> NPdollar JJ
NP -> NP2255 NPR
NP2256 -> NPdollar JJ
NP2257 -> NP2256 NPR
NP -> NP2257 NP
NP2258 -> NPdollar JJ
NP2259 -> NP2258 QP
NP -> NP2259 NNS
NP2260 -> NPdollar JJR
NP -> NP2260 NN
NP2261 -> NPdollar JJS
NP2262 -> NP2261 JJ
NP -> NP2262 NN
NP2263 -> NPdollar JJS
NP -> NP2263 NN
NP2264 -> NPdollar JJS
NP2265 -> NP2264 NN
NP -> NP2265 NN
NP2266 -> NPdollar JJS
NP2267 -> NP2266 NN
NP -> NP2267 NNS
NP2268 -> NPdollar JJS
NP -> NP2268 NNS
NP2269 -> NPdollar NACLOC
NP -> NP2269 NN
NP2270 -> NPdollar NN
NP2271 -> NP2270 JJ
NP -> NP2271 NN
NP2272 -> NPdollar NN
NP -> NP2272 NN
NP2273 -> NPdollar NN
NP2274 -> NP2273 NN
NP -> NP2274 NN
NP2275 -> NPdollar NN
NP2276 -> NP2275 NN
NP -> NP2276 NNS
NP2277 -> NPdollar NN
NP -> NP2277 NNS
NP2278 -> NPdollar NN
NP2279 -> NP2278 NNS
NP -> NP2279 NN
NP2280 -> NPdollar NN
NP -> NP2280 NPR
NP2281 -> NPdollar NN
NP -> NP2281 S
NP2282 -> NPdollar NN
NP -> NP2282 SBAR
NP2283 -> NPdollar NNS
NP -> NP2283 NN
NP2284 -> NPdollar NNS
NP -> NP2284 NNS
NP2285 -> NPdollar NNS
NP -> NP2285 S
NP2286 -> NPdollar NNS
NP -> NP2286 SBAR
NP2287 -> NPdollar NPR
NP -> NP2287 NP
NP2288 -> NPdollar NPRS
NP -> NP2288 NP
NP2289 -> NPdollar QP
NP2290 -> NP2289 JJ
NP -> NP2290 NNS
NP2291 -> NPdollar QP
NP -> NP2291 NN
NP2292 -> NPdollar QP
NP2293 -> NP2292 NN
NP -> NP2293 NN
NP2294 -> NPdollar QP
NP2295 -> NP2294 NN
NP -> NP2295 NNS
NP2296 -> NPdollar QP
NP -> NP2296 NNS
NP2297 -> NPdollar VBG
NP -> NP2297 NN
NP2298 -> NPdollar VBG
NP2299 -> NP2298 NN
NP -> NP2299 NN
NP2300 -> NPdollar VBG
NP -> NP2300 NNS
NP2301 -> NPdollar VBN
NP -> NP2301 NN
NP2302 -> NPdollar VBN
NP2303 -> NP2302 NN
NP -> NP2303 NN
NP2304 -> NPdollar VBN
NP -> NP2304 NNS
NP2305 -> NPdollar PUNCbquotebquote
NP2306 -> NP2305 NX
NP -> NP2306 PUNCquotequote
NP2307 -> NPR PUNCquotequote
NP -> NP2307 NPR
NP2308 -> NPR COMMA
NP -> NP2308 NPR
NP2309 -> NPR COMMA
NP -> NP2309 NPRS
NP2310 -> NPR PUNCpoint
NP -> NP2310 NPR
NP2311 -> NPR ADJP
NP -> NP2311 NNS
NP2312 -> NPR FW
NP -> NP2312 NPR
NP2313 -> NPR JJ
NP -> NP2313 NN
NP2314 -> NPR JJ
NP2315 -> NP2314 NN
NP2316 -> NP2315 NN
NP -> NP2316 NPR
NP2317 -> NPR JJ
NP2318 -> NP2317 NN
NP -> NP2318 NNS
NP2319 -> NPR JJ
NP -> NP2319 NNS
NP2320 -> NPR NP
NP -> NP2320 NPR
NP2321 -> NPR PRN
NP -> NP2321 NPR
NP2322 -> NPR QP
NP2323 -> NP2322 COMMA
NP -> NP2323 QP
NP2324 -> NPR QP
NP2325 -> NP2324 COMMA
NP2326 -> NP2325 QP
NP -> NP2326 COMMA
NP2327 -> NPR QP
NP -> NP2327 NNS
NP2328 -> NPR PUNCbquotebquote
NP2329 -> NP2328 NPR
NP2330 -> NP2329 PUNCquotequote
NP -> NP2330 NPR
NP2331 -> NPRS NP
NP -> NP2331 NPR
NP2332 -> PDT DT
NP2333 -> NP2332 JJ
NP -> NP2333 NN
NP2334 -> PDT DT
NP2335 -> NP2334 JJ
NP -> NP2335 NNS
NP2336 -> PDT DT
NP -> NP2336 NN
NP2337 -> PDT DT
NP2338 -> NP2337 NN
NP -> NP2338 NN
NP2339 -> PDT DT
NP2340 -> NP2339 NN
NP -> NP2340 NNS
NP2341 -> PDT DT
NP -> NP2341 NNS
NP2342 -> PRPdollar ADJP
NP2343 -> NP2342 JJ
NP -> NP2343 NN
NP2344 -> PRPdollar ADJP
NP -> NP2344 NN
NP2345 -> PRPdollar ADJP
NP2346 -> NP2345 NN
NP -> NP2346 NN
NP2347 -> PRPdollar ADJP
NP -> NP2347 NNS
NP2348 -> PRPdollar JJ
NP2349 -> NP2348 JJ
NP2350 -> NP2349 JJ
NP -> NP2350 NN
NP2351 -> PRPdollar JJ
NP2352 -> NP2351 JJ
NP -> NP2352 NN
NP2353 -> PRPdollar JJ
NP2354 -> NP2353 JJ
NP2355 -> NP2354 NN
NP -> NP2355 NN
NP2356 -> PRPdollar JJ
NP2357 -> NP2356 JJ
NP -> NP2357 NNS
NP2358 -> PRPdollar JJ
NP -> NP2358 NN
NP2359 -> PRPdollar JJ
NP2360 -> NP2359 NN
NP -> NP2360 NN
NP2361 -> PRPdollar JJ
NP2362 -> NP2361 NN
NP2363 -> NP2362 NN
NP -> NP2363 NN
NP2364 -> PRPdollar JJ
NP2365 -> NP2364 NN
NP -> NP2365 NNS
NP2366 -> PRPdollar JJ
NP -> NP2366 NNS
NP2367 -> PRPdollar JJ
NP2368 -> NP2367 NNS
NP -> NP2368 NN
NP2369 -> PRPdollar JJ
NP -> NP2369 NPR
NP2370 -> PRPdollar JJ
NP2371 -> NP2370 NPR
NP -> NP2371 NP
NP2372 -> PRPdollar JJS
NP2373 -> NP2372 JJ
NP -> NP2373 NN
NP2374 -> PRPdollar JJS
NP -> NP2374 NN
NP2375 -> PRPdollar JJS
NP -> NP2375 NNS
NP2376 -> PRPdollar NN
NP -> NP2376 NN
NP2377 -> PRPdollar NN
NP2378 -> NP2377 NN
NP -> NP2378 NN
NP2379 -> PRPdollar NN
NP2380 -> NP2379 NN
NP -> NP2380 NNS
NP2381 -> PRPdollar NN
NP -> NP2381 NNS
NP2382 -> PRPdollar NN
NP -> NP2382 NPR
NP2383 -> PRPdollar NN
NP -> NP2383 S
NP2384 -> PRPdollar NN
NP -> NP2384 SBAR
NP2385 -> PRPdollar NNS
NP -> NP2385 NN
NP2386 -> PRPdollar NNS
NP -> NP2386 NNS
NP2387 -> PRPdollar NNS
NP -> NP2387 S
NP2388 -> PRPdollar NPR
NP2389 -> NP2388 JJ
NP -> NP2389 NN
NP2390 -> PRPdollar NPR
NP -> NP2390 NP
NP2391 -> PRPdollar NPR
NP2392 -> NP2391 QP
NP -> NP2392 NN
NP2393 -> PRPdollar NPRS
NP -> NP2393 NP
NP2394 -> PRPdollar QP
NP2395 -> NP2394 JJ
NP -> NP2395 NNS
NP2396 -> PRPdollar QP
NP -> NP2396 NN
NP2397 -> PRPdollar QP
NP2398 -> NP2397 NN
NP -> NP2398 NN
NP2399 -> PRPdollar QP
NP2400 -> NP2399 NN
NP -> NP2400 NNS
NP2401 -> PRPdollar QP
NP -> NP2401 NNS
NP2402 -> PRPdollar VBG
NP -> NP2402 NN
NP2403 -> PRPdollar VBG
NP -> NP2403 NNS
NP2404 -> PRPdollar VBN
NP -> NP2404 NN
NP2405 -> QP ADJP
NP2406 -> NP2405 JJ
NP2407 -> NP2406 JJ
NP2408 -> NP2407 NN
NP -> NP2408 NNS
NP2409 -> QP ADJP
NP -> NP2409 NNS
NP2410 -> QP JJ
NP2411 -> NP2410 JJ
NP -> NP2411 NNS
NP2412 -> QP JJ
NP -> NP2412 NN
NP2413 -> QP JJ
NP2414 -> NP2413 NN
NP -> NP2414 NN
NP2415 -> QP JJ
NP2416 -> NP2415 NN
NP -> NP2416 NNS
NP2417 -> QP JJ
NP -> NP2417 NNS
NP2418 -> QP JJ
NP2419 -> NP2418 NPR
NP -> NP2419 NP
NP2420 -> QP JJR
NP -> NP2420 NNS
NP2421 -> QP NN
NP -> NP2421 NN
NP2422 -> QP NN
NP2423 -> NP2422 NN
NP -> NP2423 NNS
NP2424 -> QP NN
NP -> NP2424 NNS
NP2425 -> QP NN
NP -> NP2425 NPR
NP2426 -> QP NNS
NP -> NP2426 NNS
NP2427 -> QP NPR
NP2428 -> NP2427 JJ
NP -> NP2428 NNS
NP2429 -> QP NPR
NP -> NP2429 NP
NP2430 -> QP RB
NP -> NP2430 PUNCpoint
NP2431 -> QP VBN
NP -> NP2431 NNS
NP2432 -> RB DT
NP2433 -> NP2432 ADJP
NP -> NP2433 NN
NP2434 -> RB DT
NP2435 -> NP2434 JJ
NP -> NP2435 NN
NP2436 -> RB DT
NP2437 -> NP2436 JJ
NP -> NP2437 NNS
NP2438 -> RB DT
NP -> NP2438 NN
NP2439 -> RB DT
NP2440 -> NP2439 NN
NP -> NP2440 NN
NP2441 -> RB DT
NP -> NP2441 NNS
NP2442 -> RB DT
NP -> NP2442 NPR
NP2443 -> RB JJ
NP -> NP2443 NN
NP2444 -> RB JJ
NP -> NP2444 NNS
NP2445 -> RB NN
NP -> NP2445 NNS
NP2446 -> RB QP
NP -> NP2446 NN
NP2447 -> RB QP
NP -> NP2447 NNS
NP2448 -> RB VBN
NP -> NP2448 NNS
NP2449 -> RBS JJ
NP -> NP2449 NNS
NP2450 -> SBARNOM PUNCcolon
NP -> NP2450 NP
NP2451 -> VBG JJ
NP -> NP2451 NN
NP2452 -> VBG JJ
NP -> NP2452 NNS
NP2453 -> VBG NN
NP -> NP2453 NN
NP2454 -> VBG NN
NP -> NP2454 NNS
NP2455 -> VBG NPR
NP -> NP2455 NP
NP2456 -> VBN JJ
NP -> NP2456 NN
NP2457 -> VBN JJ
NP -> NP2457 NNS
NP2458 -> VBN NN
NP -> NP2458 NN
NP2459 -> VBN NN
NP -> NP2459 NNS
NP2460 -> VBN NPR
NP -> NP2460 NP
NP2461 -> PUNCbquotebquote JJ
NP2462 -> NP2461 PUNCquotequote
NP -> NP2462 NN
NP2463 -> PUNCbquotebquote JJ
NP2464 -> NP2463 PUNCquotequote
NP -> NP2464 NNS
NP2465 -> PUNCbquotebquote NP
NP2466 -> NP2465 PUNCquotequote
NP -> NP2466 PP
NP2467 -> PUNCbquotebquote NP
NP2468 -> NP2467 COMMA
NP2469 -> NP2468 PUNCquotequote
NP -> NP2469 NP
NP2470 -> PUNCbquotebquote NPR
NP2471 -> NP2470 PUNCquotequote
NP -> NP2471 PRN
NP2472 -> PUNCbquotebquote NPR
NP2473 -> NP2472 COMMA
NP2474 -> NP2473 PUNCquotequote
NP -> NP2474 NP
PP2475 -> ADVP IN
PP -> PP2475 NP
PP2476 -> ADVP IN
PP -> PP2476 PP
PP2477 -> ADVP IN
PP -> PP2477 SNOM
PP2478 -> ADVP TO
PP -> PP2478 NP
PP2479 -> IN PUNCquotequote
PP -> PP2479 NP
PP2480 -> IN NP
PP -> PP2480 ADVP
PP2481 -> IN NP
PP -> PP2481 ADVPTMP
PP2482 -> IN NP
PP -> PP2482 NPTMP
PP2483 -> IN NP
PP -> PP2483 PP
PP2484 -> IN NP
PP -> PP2484 PPTMP
PP2485 -> IN PRN
PP -> PP2485 NP
PP2486 -> IN PUNCbquotebquote
PP -> PP2486 ADJP
PP2487 -> IN PUNCbquotebquote
PP -> PP2487 NP
PP2488 -> IN PUNCbquotebquote
PP2489 -> PP2488 NP
PP -> PP2489 PUNCquotequote
PP2490 -> IN PUNCbquotebquote
PP -> PP2490 NPR
PP2491 -> IN PUNCbquotebquote
PP2492 -> PP2491 NPR
PP -> PP2492 PUNCquotequote
PP2493 -> JJ IN
PP -> PP2493 NP
PP2494 -> JJ TO
PP -> PP2494 NP
PP2495 -> NP IN
PP -> PP2495 NP
PP2496 -> NPADV IN
PP -> PP2496 NP
PP2497 -> PP COMMA
PP -> PP2497 PP
PP2498 -> PP COMMA
PP2499 -> PP2498 RB
PP -> PP2499 PP
PP2500 -> RB IN
PP -> PP2500 NP
PP2501 -> RB IN
PP -> PP2501 PP
PP2502 -> RB IN
PP -> PP2502 SNOM
PP2503 -> TO NP
PP -> PP2503 NPTMP
PP2504 -> TO NP
PP -> PP2504 PPTMP
PP2505 -> TO PUNCbquotebquote
PP -> PP2505 NP
SQ2506 -> MD NP
SQ -> SQ2506 VP
SQ2507 -> MD NP
SQ2508 -> SQ2507 VP
SQ -> SQ2508 PUNCpoint
SQ2509 -> VBD NP
SQ -> SQ2509 VP
SQ2510 -> VBP NP
SQ -> SQ2510 VP
SQ2511 -> VBP NP
SQ2512 -> SQ2511 VP
SQ -> SQ2512 PUNCpoint
SQ2513 -> VBZ NP
SQ2514 -> SQ2513 NPPRD
SQ -> SQ2514 PUNCpoint
SQ2515 -> VBZ NP
SQ -> SQ2515 VP
SQ2516 -> VBZ NP
SQ2517 -> SQ2516 VP
SQ -> SQ2517 PUNCpoint
ADJP2518 -> JJ COMMA
ADJP -> ADJP2518 JJ
ADJP2519 -> JJ NPTMP
ADJP -> ADJP2519 PP
ADJP2520 -> JJ TO
ADJP -> ADJP2520 JJ
ADJP2521 -> NPR COMMA
ADJP -> ADJP2521 JJ
ADJP2522 -> QP JJ
ADJP -> ADJP2522 NN
ADJP2523 -> RB JJ
ADJP -> ADJP2523 PP
ADJP2524 -> RB RB
ADJP -> ADJP2524 JJ
ADJP2525 -> RB RBR
ADJP -> ADJP2525 JJ
ADJP2526 -> RBR JJ
ADJP -> ADJP2526 PP
ADJP2527 -> RBS RB
ADJP -> ADJP2527 JJ
PPLOCPRD2528 -> ADVP IN
PPLOCPRD -> PPLOCPRD2528 NP
SBARPRP2529 -> ADVP IN
SBARPRP -> SBARPRP2529 S
SBARPRP2530 -> IN IN
SBARPRP -> SBARPRP2530 S
SBARPRP2531 -> IN NN
SBARPRP -> SBARPRP2531 S
SBARPRP2532 -> IN PUNCbquotebquote
SBARPRP -> SBARPRP2532 S
SBARPRP2533 -> RB IN
SBARPRP -> SBARPRP2533 S
PPPRD2534 -> ADVP IN
PPPRD -> PPPRD2534 NP
PPPRD2535 -> RB IN
PPPRD -> PPPRD2535 NP
QPMONEY2536 -> IN JJS
QPMONEY -> QPMONEY2536 QPMONEY
QPMONEY2537 -> IN QPMONEY
QPMONEY -> QPMONEY2537 PP
QPMONEY2538 -> IN TO
QPMONEY -> QPMONEY2538 QPMONEY
QPMONEY2539 -> JJR IN
QPMONEY -> QPMONEY2539 QPMONEY
QPMONEY2540 -> RB JJ
QPMONEY2541 -> QPMONEY2540 IN
QPMONEY -> QPMONEY2541 QPMONEY
QPMONEY2542 -> RB QPMONEY
QPMONEY -> QPMONEY2542 PP
QPMONEY2543 -> RB TO
QPMONEY -> QPMONEY2543 QPMONEY
QPMONEY2544 -> RBR IN
QPMONEY -> QPMONEY2544 QPMONEY
PRN2545 -> COMMA PUNCquotequote
PRN2546 -> PRN2545 S
PRN -> PRN2546 COMMA
PRN2547 -> COMMA PUNCquotequote
PRN2548 -> PRN2547 S
PRN2549 -> PRN2548 COMMA
PRN -> PRN2549 PUNCbquotebquote
PRN2550 -> COMMA PUNCquotequote
PRN2551 -> PRN2550 SINV
PRN -> PRN2551 COMMA
PRN2552 -> COMMA PUNCquotequote
PRN2553 -> PRN2552 SINV
PRN2554 -> PRN2553 COMMA
PRN -> PRN2554 PUNCbquotebquote
PRN2555 -> COMMA ADVP
PRN -> PRN2555 COMMA
PRN2556 -> COMMA NP
PRN2557 -> PRN2556 VP
PRN -> PRN2557 COMMA
PRN2558 -> COMMA PP
PRN -> PRN2558 COMMA
PRN2559 -> COMMA S
PRN -> PRN2559 COMMA
PRN2560 -> COMMA SBAR
PRN -> PRN2560 COMMA
PRN2561 -> COMMA SBARADV
PRN -> PRN2561 COMMA
PRN2562 -> COMMA SINV
PRN -> PRN2562 COMMA
PRN2563 -> PUNCLRB ADJP
PRN -> PRN2563 PUNCRRB
PRN2564 -> PUNCLRB ADVP
PRN -> PRN2564 PUNCRRB
PRN2565 -> PUNCLRB JJ
PRN -> PRN2565 PUNCRRB
PRN2566 -> PUNCLRB NN
PRN -> PRN2566 PUNCRRB
PRN2567 -> PUNCLRB NP
PRN2568 -> PRN2567 COMMA
PRN2569 -> PRN2568 NP
PRN2570 -> PRN2569 COMMA
PRN2571 -> PRN2570 NP
PRN -> PRN2571 PUNCRRB
PRN2572 -> PUNCLRB NP
PRN2573 -> PRN2572 COMMA
PRN2574 -> PRN2573 NPLOC
PRN -> PRN2574 PUNCRRB
PRN2575 -> PUNCLRB NP
PRN -> PRN2575 PUNCRRB
PRN2576 -> PUNCLRB NPLOC
PRN -> PRN2576 PUNCRRB
PRN2577 -> PUNCLRB NPTMP
PRN -> PRN2577 PUNCRRB
PRN2578 -> PUNCLRB NPR
PRN -> PRN2578 PUNCRRB
PRN2579 -> PUNCLRB NPR
PRN2580 -> PRN2579 PUNCpoint
PRN -> PRN2580 PUNCRRB
PRN2581 -> PUNCLRB PP
PRN -> PRN2581 PUNCRRB
PRN2582 -> PUNCLRB S
PRN -> PRN2582 PUNCRRB
PRN2583 -> PUNCLRB SBAR
PRN -> PRN2583 PUNCRRB
PRN2584 -> PUNCLRB VP
PRN -> PRN2584 PUNCRRB
PRN2585 -> PUNCcolon NP
PRN -> PRN2585 PUNCcolon
PRN2586 -> PUNCcolon PP
PRN -> PRN2586 PUNCcolon
PRN2587 -> PUNCcolon S
PRN -> PRN2587 PUNCcolon
PRN2588 -> PUNCcolon SADV
PRN -> PRN2588 PUNCcolon
PRN2589 -> PUNCcolon SBAR
PRN -> PRN2589 PUNCcolon
QP2590 -> IN JJS
QP -> QP2590 QP
QP2591 -> IN QP
QP2592 -> QP2591 NN
QP -> QP2592 PP
QP2593 -> IN TO
QP -> QP2593 QP
QP2594 -> JJR IN
QP -> QP2594 DT
QP2595 -> JJR IN
QP -> QP2595 NN
QP2596 -> JJR IN
QP -> QP2596 QP
QP2597 -> QP NN
QP -> QP2597 PP
QP2598 -> RB POUND
QP -> QP2598 QP
QP2599 -> RB DT
QP -> QP2599 JJ
QP2600 -> RB IN
QP -> QP2600 QP
QP2601 -> RB JJ
QP2602 -> QP2601 IN
QP -> QP2602 QP
QP2603 -> RB JJR
QP2604 -> QP2603 IN
QP -> QP2604 QP
QP2605 -> RB QP
QP -> QP2605 NNS
QP2606 -> RB QP
QP -> QP2606 PP
QP2607 -> RB RB
QP2608 -> QP2607 IN
QP -> QP2608 QP
QP2609 -> RB RB
QP -> QP2609 QP
QP2610 -> RBR IN
QP -> QP2610 DT
QP2611 -> RBR IN
QP -> QP2611 QP
SBARQ2612 -> RB WHNP
SBARQ2613 -> SBARQ2612 SQ
SBARQ -> SBARQ2613 PUNCpoint
SBARQ2614 -> WHADVP SQ
SBARQ -> SBARQ2614 PUNCpoint
SBARQ2615 -> WHNP SQ
SBARQ -> SBARQ2615 PUNCpoint
SBARQ2616 -> PUNCbquotebquote WHADVP
SBARQ2617 -> SBARQ2616 SQ
SBARQ -> SBARQ2617 PUNCpoint
NPR2618 -> NNP NNP
NPR -> NPR2618 NNP
NPR2619 -> NNP NNP
NPR2620 -> NPR2619 NNP
NPR -> NPR2620 NNP
NPR2621 -> NNP NNP
NPR2622 -> NPR2621 NNP
NPR2623 -> NPR2622 NNP
NPR -> NPR2623 NNP
NPR2624 -> NNP NNP
NPR2625 -> NPR2624 NNP
NPR2626 -> NPR2625 NNP
NPR2627 -> NPR2626 NNP
NPR -> NPR2627 NNP
NPR2628 -> NNP NNP
NPR2629 -> NPR2628 NNP
NPR2630 -> NPR2629 NNP
NPR2631 -> NPR2630 NNP
NPR2632 -> NPR2631 NNP
NPR -> NPR2632 NNP
NPR2633 -> NNP NNP
NPR2634 -> NPR2633 NNP
NPR2635 -> NPR2634 NNPS
NPR -> NPR2635 NNP
NPR2636 -> NNP NNP
NPR2637 -> NPR2636 NNPS
NPR -> NPR2637 NNP
NPR2638 -> NNP NNP
NPR2639 -> NPR2638 NNPS
NPR2640 -> NPR2639 NNP
NPR -> NPR2640 NNP
NPR2641 -> NNP NNPS
NPR -> NPR2641 NNP
NPR2642 -> NNP NNPS
NPR2643 -> NPR2642 NNP
NPR -> NPR2643 NNP
NPR2644 -> NNPS NNP
NPR -> NPR2644 NNP
NPR2645 -> NNPS NNP
NPR2646 -> NPR2645 NNP
NPR -> NPR2646 NNP
NPRS2647 -> NNP NNP
NPRS2648 -> NPRS2647 NNP
NPRS -> NPRS2648 NNPS
NPRS2649 -> NNP NNP
NPRS -> NPRS2649 NNPS
NPPRD2650 -> DT ADJP
NPPRD -> NPPRD2650 NN
NPPRD2651 -> DT JJ
NPPRD2652 -> NPPRD2651 COMMA
NPPRD2653 -> NPPRD2652 JJ
NPPRD -> NPPRD2653 NN
NPPRD2654 -> DT JJ
NPPRD2655 -> NPPRD2654 JJ
NPPRD -> NPPRD2655 NN
NPPRD2656 -> DT JJ
NPPRD -> NPPRD2656 NN
NPPRD2657 -> DT JJ
NPPRD2658 -> NPPRD2657 NN
NPPRD -> NPPRD2658 NN
NPPRD2659 -> DT JJ
NPPRD2660 -> NPPRD2659 NN
NPPRD -> NPPRD2660 SBAR
NPPRD2661 -> DT JJ
NPPRD -> NPPRD2661 NNS
NPPRD2662 -> DT JJ
NPPRD2663 -> NPPRD2662 NPR
NPPRD -> NPPRD2663 NP
NPPRD2664 -> DT JJ
NPPRD -> NPPRD2664 QP
NPPRD2665 -> DT JJ
NPPRD2666 -> NPPRD2665 QP
NPPRD -> NPPRD2666 NNS
NPPRD2667 -> DT NN
NPPRD -> NPPRD2667 NN
NPPRD2668 -> DT NN
NPPRD2669 -> NPPRD2668 NN
NPPRD -> NPPRD2669 NN
NPPRD2670 -> DT NN
NPPRD -> NPPRD2670 S
NPPRD2671 -> DT NN
NPPRD -> NPPRD2671 SBAR
NPPRD2672 -> DT NPR
NPPRD -> NPPRD2672 NP
NPPRD2673 -> DT VBG
NPPRD -> NPPRD2673 NN
NPPRD2674 -> DT PUNCbquotebquote
NPPRD2675 -> NPPRD2674 JJ
NPPRD2676 -> NPPRD2675 PUNCquotequote
NPPRD -> NPPRD2676 NN
NPPRD2677 -> DT PUNCbquotebquote
NPPRD2678 -> NPPRD2677 JJ
NPPRD2679 -> NPPRD2678 NN
NPPRD -> NPPRD2679 PUNCquotequote
NPPRD2680 -> DT PUNCbquotebquote
NPPRD -> NPPRD2680 NN
NPPRD2681 -> JJ NN
NPPRD -> NPPRD2681 NNS
NPPRD2682 -> NP COMMA
NPPRD -> NPPRD2682 ADJP
NPPRD2683 -> NP COMMA
NPPRD -> NPPRD2683 ADVP
NPPRD2684 -> NP COMMA
NPPRD -> NPPRD2684 NP
NPPRD2685 -> NP COMMA
NPPRD -> NPPRD2685 PP
NPPRD2686 -> NP COMMA
NPPRD -> NPPRD2686 SBAR
NPPRD2687 -> NP COMMA
NPPRD -> NPPRD2687 VP
NPPRD2688 -> NP PUNCcolon
NPPRD -> NPPRD2688 NP
NPPRD2689 -> NP PP
NPPRD2690 -> NPPRD2689 COMMA
NPPRD -> NPPRD2690 SBAR
NPPRD2691 -> NP PP
NPPRD -> NPPRD2691 PP
NPPRD2692 -> NP PP
NPPRD -> NPPRD2692 PPLOC
NPPRD2693 -> NP PP
NPPRD -> NPPRD2693 PPTMP
NPPRD2694 -> NP PP
NPPRD -> NPPRD2694 S
NPPRD2695 -> NP PP
NPPRD -> NPPRD2695 SBAR
NPPRD2696 -> NP PP
NPPRD -> NPPRD2696 VP
NPPRD2697 -> NP PPLOC
NPPRD -> NPPRD2697 PP
NPPRD2698 -> NP PPLOC
NPPRD -> NPPRD2698 SBAR
NPPRD2699 -> NPdollar JJ
NPPRD -> NPPRD2699 NN
NPPRD2700 -> NPdollar JJ
NPPRD2701 -> NPPRD2700 NN
NPPRD -> NPPRD2701 NN
NPPRD2702 -> NPdollar JJS
NPPRD -> NPPRD2702 NN
NPPRD2703 -> NPdollar JJS
NPPRD2704 -> NPPRD2703 NN
NPPRD -> NPPRD2704 NN
NPPRD2705 -> PRPdollar JJ
NPPRD -> NPPRD2705 NN
NPPRD2706 -> QP JJ
NPPRD -> NPPRD2706 NNS
NPPRD2707 -> RB DT
NPPRD2708 -> NPPRD2707 JJ
NPPRD -> NPPRD2708 NN
NPPRD2709 -> RB DT
NPPRD -> NPPRD2709 NN
PPTMP2710 -> ADVP IN
PPTMP -> PPTMP2710 NP
PPTMP2711 -> ADVP IN
PPTMP -> PPTMP2711 SNOM
PPTMP2712 -> NP IN
PPTMP -> PPTMP2712 NP
PPTMP2713 -> PP COMMA
PPTMP -> PPTMP2713 PP
PPTMP2714 -> RB IN
PPTMP -> PPTMP2714 NP
STPC2715 -> ADVP COMMA
STPC2716 -> STPC2715 NP
STPC -> STPC2716 VP
STPC2717 -> ADVP NP
STPC -> STPC2717 VP
STPC2718 -> ADVPTMP COMMA
STPC2719 -> STPC2718 NP
STPC -> STPC2719 VP
STPC2720 -> ADVPTMP NP
STPC -> STPC2720 VP
STPC2721 -> NP ADVP
STPC -> STPC2721 VP
STPC2722 -> NP ADVPTMP
STPC -> STPC2722 VP
STPC2723 -> NP VP
STPC -> STPC2723 COMMA
STPC2724 -> NP VP
STPC2725 -> STPC2724 COMMA
STPC -> STPC2725 PUNCquotequote
STPC2726 -> NP PUNCbquotebquote
STPC -> STPC2726 VP
STPC2727 -> NP PUNCbquotebquote
STPC2728 -> STPC2727 VP
STPC2729 -> STPC2728 COMMA
STPC -> STPC2729 PUNCquotequote
STPC2730 -> NPTMP COMMA
STPC2731 -> STPC2730 NP
STPC -> STPC2731 VP
STPC2732 -> PP COMMA
STPC2733 -> STPC2732 NP
STPC -> STPC2733 VP
STPC2734 -> PP COMMA
STPC2735 -> STPC2734 PUNCbquotebquote
STPC2736 -> STPC2735 NP
STPC -> STPC2736 VP
STPC2737 -> PPLOC COMMA
STPC2738 -> STPC2737 NP
STPC -> STPC2738 VP
STPC2739 -> PPTMP COMMA
STPC2740 -> STPC2739 NP
STPC -> STPC2740 VP
STPC2741 -> S COMMA
STPC -> STPC2741 S
STPC2742 -> S PUNCcolon
STPC -> STPC2742 S
STPC2743 -> SADV COMMA
STPC2744 -> STPC2743 NP
STPC -> STPC2744 VP
STPC2745 -> SBARADV COMMA
STPC2746 -> STPC2745 NP
STPC -> STPC2746 VP
STPC2747 -> SBARTMP COMMA
STPC2748 -> STPC2747 NP
STPC -> STPC2748 VP
STPC2749 -> PUNCbquotebquote NP
STPC -> STPC2749 VP
STPC2750 -> PUNCbquotebquote NP
STPC2751 -> STPC2750 VP
STPC2752 -> STPC2751 COMMA
STPC -> STPC2752 PUNCquotequote
NACTMP2753 -> NPR COMMA
NACTMP2754 -> NACTMP2753 NPR
NACTMP2755 -> NACTMP2754 QP
NACTMP2756 -> NACTMP2755 COMMA
NACTMP2757 -> NACTMP2756 QP
NACTMP -> NACTMP2757 COMMA
ADVPTMP2758 -> RB RB
ADVPTMP -> ADVPTMP2758 PP
ADVPTMP2759 -> RB RB
ADVPTMP -> ADVPTMP2759 SBAR
PPLOC2760 -> ADVP IN
PPLOC -> PPLOC2760 NP
PPLOC2761 -> IN NP
PPLOC -> PPLOC2761 PUNCcolon
PPLOC2762 -> NP IN
PPLOC -> PPLOC2762 NP
PPLOC2763 -> NPADV IN
PPLOC -> PPLOC2763 NP
PPLOC2764 -> RB IN
PPLOC -> PPLOC2764 NP
''')

parser = ChartParser(grammar)

gr = parser.grammar()
print(' '.join(produce(gr, gr.start())))