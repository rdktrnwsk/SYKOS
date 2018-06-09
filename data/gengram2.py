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
S -> NP
S -> NP PPLOCPRD
S -> NP PPPRD
S -> NPPRD
S -> NPTMP VP
S -> PPTMP VP
S -> PRN VP
S -> SNOM VP
S -> VP
S -> VP PUNCpoint
SBAR -> WDT S
PPPRD -> IN NP
PPPRD -> JJ NP
PPPRD -> TO NP
SBARPRPPRD -> IN S
WDT -> 'whatever'
JJ -> '12year'
JJ -> '190point'
JJ -> '20th'
JJ -> '300ashare'
JJ -> '30share'
JJ -> '52week'
JJ -> 'African'
JJ -> 'Arab'
JJ -> 'Asian'
JJ -> 'Canadian'
JJ -> 'Colombian'
JJ -> 'Communist'
JJ -> 'Democratic'
JJ -> 'European'
JJ -> 'Finnish'
JJ -> 'French'
JJ -> 'German'
JJ -> 'Great'
JJ -> 'Highgrade'
JJ -> 'Hungarian'
JJ -> 'Indian'
JJ -> 'Israeli'
JJ -> 'Italian'
JJ -> 'Korean'
JJ -> 'Londonbased'
JJ -> 'Northern'
JJ -> 'Polish'
JJ -> 'Spanish'
JJ -> 'Swedish'
JJ -> 'Taiwanese'
JJ -> 'Vietnamese'
JJ -> 'Washingtonbased'
JJ -> 'able'
JJ -> 'acceptable'
JJ -> 'adjustable'
JJ -> 'administrative'
JJ -> 'adverse'
JJ -> 'affluent'
JJ -> 'aftertax'
JJ -> 'aggressive'
JJ -> 'agricultural'
JJ -> 'ample'
JJ -> 'annual'
JJ -> 'annualized'
JJ -> 'anticipated'
JJ -> 'anxious'
JJ -> 'apparent'
JJ -> 'appropriate'
JJ -> 'atmospheric'
JJ -> 'attractive'
JJ -> 'available'
JJ -> 'average'
JJ -> 'aware'
JJ -> 'back'
JJ -> 'bad'
JJ -> 'base'
JJ -> 'bearish'
JJ -> 'benchmark'
JJ -> 'black'
JJ -> 'blackandwhite'
JJ -> 'bleak'
JJ -> 'blue'
JJ -> 'bluechip'
JJ -> 'brief'
JJ -> 'bright'
JJ -> 'brisk'
JJ -> 'budgetary'
JJ -> 'buy'
JJ -> 'buyout'
JJ -> 'call'
JJ -> 'careful'
JJ -> 'certain'
JJ -> 'charitable'
JJ -> 'chief'
JJ -> 'civil'
JJ -> 'classic'
JJ -> 'clinical'
JJ -> 'closedend'
JJ -> 'collective'
JJ -> 'combined'
JJ -> 'coming'
JJ -> 'comparable'
JJ -> 'compelling'
JJ -> 'complex'
JJ -> 'comprehensive'
JJ -> 'computerdriven'
JJ -> 'concentrated'
JJ -> 'concrete'
JJ -> 'confidential'
JJ -> 'congressional'
JJ -> 'conservative'
JJ -> 'considerable'
JJ -> 'constant'
JJ -> 'continuing'
JJ -> 'conventional'
JJ -> 'convinced'
JJ -> 'core'
JJ -> 'covert'
JJ -> 'creative'
JJ -> 'current'
JJ -> 'damaged'
JJ -> 'daytoday'
JJ -> 'dead'
JJ -> 'deep'
JJ -> 'defunct'
JJ -> 'democratic'
JJ -> 'dependent'
JJ -> 'depositary'
JJ -> 'deputy'
JJ -> 'desirable'
JJ -> 'desperate'
JJ -> 'diplomatic'
JJ -> 'direct'
JJ -> 'disappointing'
JJ -> 'discount'
JJ -> 'discretionary'
JJ -> 'domestic'
JJ -> 'down'
JJ -> 'downward'
JJ -> 'dramatic'
JJ -> 'dry'
JJ -> 'dual'
JJ -> 'dutyfree'
JJ -> 'east'
JJ -> 'educational'
JJ -> 'electric'
JJ -> 'enough'
JJ -> 'environmental'
JJ -> 'estimated'
JJ -> 'evident'
JJ -> 'exact'
JJ -> 'excellent'
JJ -> 'excessive'
JJ -> 'expected'
JJ -> 'extensive'
JJ -> 'external'
JJ -> 'fair'
JJ -> 'famous'
JJ -> 'favorable'
JJ -> 'federal'
JJ -> 'few'
JJ -> 'first'
JJ -> 'fiscal'
JJ -> 'former'
JJ -> 'fourthquarter'
JJ -> 'fouryearold'
JJ -> 'free'
JJ -> 'fresh'
JJ -> 'friendly'
JJ -> 'fundamental'
JJ -> 'further'
JJ -> 'generous'
JJ -> 'genuine'
JJ -> 'global'
JJ -> 'gold'
JJ -> 'golden'
JJ -> 'grand'
JJ -> 'gray'
JJ -> 'green'
JJ -> 'handy'
JJ -> 'happy'
JJ -> 'healthcare'
JJ -> 'heavy'
JJ -> 'hefty'
JJ -> 'high'
JJ -> 'highdefinition'
JJ -> 'hightech'
JJ -> 'historical'
JJ -> 'horrible'
JJ -> 'identical'
JJ -> 'imminent'
JJ -> 'immune'
JJ -> 'important'
JJ -> 'improved'
JJ -> 'incomplete'
JJ -> 'industrial'
JJ -> 'inevitable'
JJ -> 'influential'
JJ -> 'informal'
JJ -> 'initial'
JJ -> 'innovative'
JJ -> 'institutional'
JJ -> 'interbank'
JJ -> 'interim'
JJ -> 'international'
JJ -> 'interstate'
JJ -> 'jumbo'
JJ -> 'junkbond'
JJ -> 'large'
JJ -> 'last'
JJ -> 'lastminute'
JJ -> 'leading'
JJ -> 'leftist'
JJ -> 'legislative'
JJ -> 'legitimate'
JJ -> 'liberal'
JJ -> 'likely'
JJ -> 'limited'
JJ -> 'loanloss'
JJ -> 'low'
JJ -> 'loyal'
JJ -> 'magnetic'
JJ -> 'main'
JJ -> 'mandatory'
JJ -> 'massmarket'
JJ -> 'mechanical'
JJ -> 'middle'
JJ -> 'military'
JJ -> 'modest'
JJ -> 'moneymarket'
JJ -> 'municipal'
JJ -> 'narrow'
JJ -> 'nasty'
JJ -> 'national'
JJ -> 'nationwide'
JJ -> 'nearby'
JJ -> 'negotiable'
JJ -> 'new'
JJ -> 'next'
JJ -> 'nice'
JJ -> 'nuclear'
JJ -> 'obvious'
JJ -> 'oneday'
JJ -> 'onetime'
JJ -> 'ongoing'
JJ -> 'onsite'
JJ -> 'open'
JJ -> 'optical'
JJ -> 'outside'
JJ -> 'outstanding'
JJ -> 'overnight'
JJ -> 'overseas'
JJ -> 'overthecounter'
JJ -> 'par'
JJ -> 'partial'
JJ -> 'payable'
JJ -> 'persistent'
JJ -> 'photographic'
JJ -> 'plastic'
JJ -> 'pleased'
JJ -> 'popular'
JJ -> 'portable'
JJ -> 'positive'
JJ -> 'preferred'
JJ -> 'preliminary'
JJ -> 'present'
JJ -> 'presidential'
JJ -> 'previous'
JJ -> 'prime'
JJ -> 'principal'
JJ -> 'prior'
JJ -> 'privatesector'
JJ -> 'procedural'
JJ -> 'prochoice'
JJ -> 'prodemocracy'
JJ -> 'programtrading'
JJ -> 'proposed'
JJ -> 'prudent'
JJ -> 'punitive'
JJ -> 'quarterly'
JJ -> 'radical'
JJ -> 'rare'
JJ -> 'reasonable'
JJ -> 'record'
JJ -> 'red'
JJ -> 'reduced'
JJ -> 'relative'
JJ -> 'reluctant'
JJ -> 'remarkable'
JJ -> 'residential'
JJ -> 'revised'
JJ -> 'right'
JJ -> 'rigid'
JJ -> 'risky'
JJ -> 'rough'
JJ -> 'sad'
JJ -> 'sales'
JJ -> 'savingsandloan'
JJ -> 'scarce'
JJ -> 'scheduled'
JJ -> 'scientific'
JJ -> 'secondquarter'
JJ -> 'serial'
JJ -> 'sevenday'
JJ -> 'seventh'
JJ -> 'sevenyear'
JJ -> 'significant'
JJ -> 'sixth'
JJ -> 'sizable'
JJ -> 'slim'
JJ -> 'sluggish'
JJ -> 'social'
JJ -> 'socialist'
JJ -> 'soft'
JJ -> 'southern'
JJ -> 'special'
JJ -> 'specific'
JJ -> 'square'
JJ -> 'standardized'
JJ -> 'steady'
JJ -> 'steep'
JJ -> 'stiff'
JJ -> 'strange'
JJ -> 'striking'
JJ -> 'strong'
JJ -> 'stupid'
JJ -> 'sure'
JJ -> 'sweeping'
JJ -> 'synthetic'
JJ -> 'technical'
JJ -> 'temporary'
JJ -> 'tentative'
JJ -> 'third'
JJ -> 'top'
JJ -> 'troublesome'
JJ -> 'troubling'
JJ -> 'twoday'
JJ -> 'twoyear'
JJ -> 'uncertain'
JJ -> 'unchanged'
JJ -> 'unclear'
JJ -> 'unconstitutional'
JJ -> 'unfair'
JJ -> 'unfilled'
JJ -> 'unsettled'
JJ -> 'unsuccessful'
JJ -> 'unusual'
JJ -> 'unwanted'
JJ -> 'upscale'
JJ -> 'urban'
JJ -> 'usual'
JJ -> 'vast'
JJ -> 'very'
JJ -> 'vigorous'
JJ -> 'visible'
JJ -> 'voluntary'
JJ -> 'weak'
JJ -> 'weird'
JJ -> 'western'
JJ -> 'white'
JJ -> 'whitecollar'
JJ -> 'whole'
JJ -> 'wide'
JJ -> 'wild'
JJ -> 'willing'
JJ -> 'wouldbe'
JJ -> 'yearago'
JJ -> 'yearend'
JJ -> 'yearly'
JJ -> 'young'
WP -> 'Who'
WP -> 'who'
PUNCdollar -> '$'
PUNCdollar -> 'Adollar'
PUNCdollar -> 'Cdollar'
PUNCdollar -> 'HKdollar'
NPRS -> NNPS NNPS
RP -> 'about'
RP -> 'along'
RP -> 'around'
RP -> 'aside'
RP -> 'by'
RP -> 'over'
RP -> 'up'
PRN -> PUNCcolon NP
PRN -> SINV
PRP -> 'It'
PRP -> 'himself'
PRP -> 'it'
PRP -> 'itself'
PRP -> 'me'
PRP -> 'one'
PRP -> 'you'
PRP -> 'yourself'
RB -> "n't"
RB -> 'Maybe'
RB -> 'Never'
RB -> 'Now'
RB -> 'about'
RB -> 'actively'
RB -> 'actually'
RB -> 'adequately'
RB -> 'after'
RB -> 'afterward'
RB -> 'again'
RB -> 'almost'
RB -> 'altogether'
RB -> 'anyway'
RB -> 'anywhere'
RB -> 'apart'
RB -> 'apointmpoint'
RB -> 'approximately'
RB -> 'around'
RB -> 'aside'
RB -> 'back'
RB -> 'before'
RB -> 'below'
RB -> 'broadly'
RB -> 'commonly'
RB -> 'considerably'
RB -> 'consistently'
RB -> 'deliberately'
RB -> 'downward'
RB -> 'due'
RB -> 'early'
RB -> 'easy'
RB -> 'entirely'
RB -> 'everywhere'
RB -> 'exactly'
RB -> 'exceptionally'
RB -> 'exclusively'
RB -> 'fast'
RB -> 'finally'
RB -> 'financially'
RB -> 'first'
RB -> 'forever'
RB -> 'formally'
RB -> 'formerly'
RB -> 'fractionally'
RB -> 'fully'
RB -> 'further'
RB -> 'gradually'
RB -> 'hard'
RB -> 'high'
RB -> 'illegally'
RB -> 'in'
RB -> 'increasingly'
RB -> 'indirectly'
RB -> 'jointly'
RB -> 'largely'
RB -> 'late'
RB -> 'likely'
RB -> 'literally'
RB -> 'mainly'
RB -> 'maybe'
RB -> 'moderately'
RB -> 'monthly'
RB -> 'moreover'
RB -> 'mostly'
RB -> 'much'
RB -> 'nearby'
RB -> 'nervously'
RB -> 'never'
RB -> 'no'
RB -> 'nonetheless'
RB -> 'not'
RB -> 'now'
RB -> 'often'
RB -> 'openly'
RB -> 'over'
RB -> 'partially'
RB -> 'particularly'
RB -> 'perfectly'
RB -> 'politically'
RB -> 'possibly'
RB -> 'prior'
RB -> 'probably'
RB -> 'promptly'
RB -> 'properly'
RB -> 'publicly'
RB -> 'rapidly'
RB -> 'rather'
RB -> 'real'
RB -> 'reasonably'
RB -> 'right'
RB -> 'seasonally'
RB -> 'shortly'
RB -> 'significantly'
RB -> 'similarly'
RB -> 'simply'
RB -> 'slowly'
RB -> 'solely'
RB -> 'somewhere'
RB -> 'specifically'
RB -> 'still'
RB -> 'substantially'
RB -> 'successfully'
RB -> 'supposedly'
RB -> 'temporarily'
RB -> 'there'
RB -> 'thereafter'
RB -> 'though'
RB -> 'together'
RB -> 'totally'
RB -> 'traditionally'
RB -> 'typically'
RB -> 'unanimously'
RB -> 'unfairly'
RB -> 'unsuccessfully'
RB -> 'upward'
RB -> 'very'
RB -> 'wildly'
RB -> 'worldwide'
RB -> 'yesterday'
RB -> 'yet'
NNS -> '1960s'
NNS -> '1990s'
NNS -> 'Americans'
NNS -> 'CFCs'
NNS -> 'Democrats'
NNS -> 'EURODOLLARS'
NNS -> 'Japanese'
NNS -> 'LBOs'
NNS -> 'Notes'
NNS -> 'Soviets'
NNS -> 'abuses'
NNS -> 'acceptances'
NNS -> 'accounts'
NNS -> 'acres'
NNS -> 'actions'
NNS -> 'adjusters'
NNS -> 'ads'
NNS -> 'advertisers'
NNS -> 'agencies'
NNS -> 'agreements'
NNS -> 'aides'
NNS -> 'alternatives'
NNS -> 'amounts'
NNS -> 'analysts'
NNS -> 'announcements'
NNS -> 'answers'
NNS -> 'apples'
NNS -> 'applications'
NNS -> 'appointments'
NNS -> 'appropriations'
NNS -> 'arrangements'
NNS -> 'articles'
NNS -> 'assets'
NNS -> 'attempts'
NNS -> 'backers'
NNS -> 'bacteria'
NNS -> 'barrels'
NNS -> 'bells'
NNS -> 'bidders'
NNS -> 'billions'
NNS -> 'bills'
NNS -> 'blacks'
NNS -> 'boards'
NNS -> 'bonds'
NNS -> 'books'
NNS -> 'borrowers'
NNS -> 'borrowings'
NNS -> 'boxes'
NNS -> 'breakers'
NNS -> 'broadcasts'
NNS -> 'brokers'
NNS -> 'budgets'
NNS -> 'bugs'
NNS -> 'builders'
NNS -> 'bushels'
NNS -> 'businessmen'
NNS -> 'buyouts'
NNS -> 'calls'
NNS -> 'camps'
NNS -> 'capitalgains'
NNS -> 'cards'
NNS -> 'careers'
NNS -> 'cells'
NNS -> 'chains'
NNS -> 'changes'
NNS -> 'charities'
NNS -> 'charts'
NNS -> 'children'
NNS -> 'cities'
NNS -> 'citizens'
NNS -> 'claims'
NNS -> 'clients'
NNS -> 'colleagues'
NNS -> 'commercials'
NNS -> 'commissions'
NNS -> 'committees'
NNS -> 'communications'
NNS -> 'companies'
NNS -> 'comparisons'
NNS -> 'concessions'
NNS -> 'conservatives'
NNS -> 'considerations'
NNS -> 'constituents'
NNS -> 'consumers'
NNS -> 'contracts'
NNS -> 'controls'
NNS -> 'corporations'
NNS -> 'costs'
NNS -> 'countries'
NNS -> 'credentials'
NNS -> 'creditors'
NNS -> 'criminals'
NNS -> 'curbs'
NNS -> 'cutbacks'
NNS -> 'cuts'
NNS -> 'cycles'
NNS -> 'data'
NNS -> 'days'
NNS -> 'dealers'
NNS -> 'dealings'
NNS -> 'decisions'
NNS -> 'defendants'
NNS -> 'defenses'
NNS -> 'demands'
NNS -> 'demonstrators'
NNS -> 'desks'
NNS -> 'developers'
NNS -> 'diabetics'
NNS -> 'difficulties'
NNS -> 'directors'
NNS -> 'discounts'
NNS -> 'discussions'
NNS -> 'displays'
NNS -> 'dissidents'
NNS -> 'dividends'
NNS -> 'dollars'
NNS -> 'drives'
NNS -> 'duties'
NNS -> 'economics'
NNS -> 'editions'
NNS -> 'editors'
NNS -> 'efforts'
NNS -> 'eggs'
NNS -> 'elevators'
NNS -> 'employees'
NNS -> 'engineers'
NNS -> 'entities'
NNS -> 'environments'
NNS -> 'estimates'
NNS -> 'events'
NNS -> 'exchanges'
NNS -> 'executives'
NNS -> 'expectations'
NNS -> 'expenditures'
NNS -> 'expenses'
NNS -> 'experts'
NNS -> 'exposures'
NNS -> 'facilities'
NNS -> 'factors'
NNS -> 'fans'
NNS -> 'fares'
NNS -> 'farmers'
NNS -> 'fibers'
NNS -> 'fields'
NNS -> 'financings'
NNS -> 'findings'
NNS -> 'firms'
NNS -> 'folks'
NNS -> 'forces'
NNS -> 'foreigners'
NNS -> 'fortunes'
NNS -> 'franchisees'
NNS -> 'francs'
NNS -> 'fuels'
NNS -> 'fundamentals'
NNS -> 'games'
NNS -> 'generations'
NNS -> 'genes'
NNS -> 'goals'
NNS -> 'goods'
NNS -> 'governments'
NNS -> 'graphics'
NNS -> 'groups'
NNS -> 'guests'
NNS -> 'guidelines'
NNS -> 'guns'
NNS -> 'guys'
NNS -> 'headquarters'
NNS -> 'hearings'
NNS -> 'heels'
NNS -> 'highs'
NNS -> 'holders'
NNS -> 'hopes'
NNS -> 'hospitals'
NNS -> 'hotels'
NNS -> 'hurdles'
NNS -> 'implications'
NNS -> 'imports'
NNS -> 'indications'
NNS -> 'indicators'
NNS -> 'individuals'
NNS -> 'insiders'
NNS -> 'installations'
NNS -> 'instructions'
NNS -> 'interests'
NNS -> 'inventories'
NNS -> 'investigators'
NNS -> 'journalists'
NNS -> 'kids'
NNS -> 'letters'
NNS -> 'levels'
NNS -> 'liabilities'
NNS -> 'liberals'
NNS -> 'licenses'
NNS -> 'lights'
NNS -> 'limits'
NNS -> 'lives'
NNS -> 'locations'
NNS -> 'losers'
NNS -> 'lows'
NNS -> 'magazines'
NNS -> 'mainframes'
NNS -> 'margins'
NNS -> 'marketers'
NNS -> 'marketmakers'
NNS -> 'markets'
NNS -> 'marks'
NNS -> 'masters'
NNS -> 'materials'
NNS -> 'maturities'
NNS -> 'members'
NNS -> 'men'
NNS -> 'metals'
NNS -> 'milestones'
NNS -> 'millions'
NNS -> 'mortgages'
NNS -> 'moves'
NNS -> 'movies'
NNS -> 'municipals'
NNS -> 'names'
NNS -> 'nations'
NNS -> 'needs'
NNS -> 'negotiations'
NNS -> 'newspapers'
NNS -> 'objections'
NNS -> 'objectives'
NNS -> 'occasions'
NNS -> 'offers'
NNS -> 'officers'
NNS -> 'ones'
NNS -> 'opponents'
NNS -> 'organizations'
NNS -> 'packages'
NNS -> 'pages'
NNS -> 'parents'
NNS -> 'partnerships'
NNS -> 'patients'
NNS -> 'payments'
NNS -> 'periods'
NNS -> 'permits'
NNS -> 'pickers'
NNS -> 'pictures'
NNS -> 'pigs'
NNS -> 'plaintiffs'
NNS -> 'plants'
NNS -> 'points'
NNS -> 'policies'
NNS -> 'portfolios'
NNS -> 'portions'
NNS -> 'predictions'
NNS -> 'preferences'
NNS -> 'pressures'
NNS -> 'priorities'
NNS -> 'prisons'
NNS -> 'problems'
NNS -> 'processors'
NNS -> 'products'
NNS -> 'projections'
NNS -> 'projects'
NNS -> 'promotions'
NNS -> 'properties'
NNS -> 'proponents'
NNS -> 'proposals'
NNS -> 'prospects'
NNS -> 'purchasers'
NNS -> 'puts'
NNS -> 'quarters'
NNS -> 'questions'
NNS -> 'quotas'
NNS -> 'ranks'
NNS -> 'rates'
NNS -> 'ratings'
NNS -> 'receipts'
NNS -> 'reductions'
NNS -> 'reforms'
NNS -> 'refugees'
NNS -> 'regions'
NNS -> 'relationships'
NNS -> 'repairs'
NNS -> 'reports'
NNS -> 'representatives'
NNS -> 'researchers'
NNS -> 'resignations'
NNS -> 'resources'
NNS -> 'respondents'
NNS -> 'responses'
NNS -> 'restrictions'
NNS -> 'retailers'
NNS -> 'returns'
NNS -> 'revenues'
NNS -> 'roads'
NNS -> 'routes'
NNS -> 'rules'
NNS -> 'rumors'
NNS -> 'salaries'
NNS -> 'salesmen'
NNS -> 'sanctions'
NNS -> 'scandals'
NNS -> 'scenarios'
NNS -> 'scientists'
NNS -> 'sectors'
NNS -> 'securities'
NNS -> 'seeds'
NNS -> 'senators'
NNS -> 'sentences'
NNS -> 'sessions'
NNS -> 'shareholders'
NNS -> 'sheets'
NNS -> 'sides'
NNS -> 'sources'
NNS -> 'sports'
NNS -> 'standards'
NNS -> 'statements'
NNS -> 'stations'
NNS -> 'statistics'
NNS -> 'stockholders'
NNS -> 'stories'
NNS -> 'strategists'
NNS -> 'students'
NNS -> 'studios'
NNS -> 'styles'
NNS -> 'suits'
NNS -> 'suppliers'
NNS -> 'supplies'
NNS -> 'syndicates'
NNS -> 'systems'
NNS -> 'talks'
NNS -> 'tariffs'
NNS -> 'taxes'
NNS -> 'teachers'
NNS -> 'teams'
NNS -> 'technologies'
NNS -> 'temperatures'
NNS -> 'thanks'
NNS -> 'things'
NNS -> 'thrifts'
NNS -> 'tickets'
NNS -> 'times'
NNS -> 'tourists'
NNS -> 'toys'
NNS -> 'traders'
NNS -> 'trades'
NNS -> 'traffickers'
NNS -> 'transactions'
NNS -> 'travelers'
NNS -> 'trends'
NNS -> 'troops'
NNS -> 'troubles'
NNS -> 'twothirds'
NNS -> 'units'
NNS -> 'visitors'
NNS -> 'wages'
NNS -> 'warnings'
NNS -> 'warrants'
NNS -> 'waves'
NNS -> 'ways'
NNS -> 'weeks'
NNS -> 'whites'
NNS -> 'winners'
NNS -> 'woes'
NNS -> 'workstations'
NNS -> 'years'
PUNCquotequote -> "''"
NNP -> 'ABB'
NNP -> 'ABC'
NNP -> 'Acquisition'
NNP -> 'Act'
NNP -> 'Admpoint'
NNP -> 'Advanced'
NNP -> 'Aetna'
NNP -> 'Air'
NNP -> 'Airport'
NNP -> 'Airways'
NNP -> 'Albert'
NNP -> 'Alfred'
NNP -> 'Alliance'
NNP -> 'Allianz'
NNP -> 'Amex'
NNP -> 'Amoco'
NNP -> 'Anderson'
NNP -> 'Andersson'
NNP -> 'Anne'
NNP -> 'Apogee'
NNP -> 'Apple'
NNP -> 'April'
NNP -> 'Arco'
NNP -> 'Arizona'
NNP -> 'Arizpoint'
NNP -> 'Armstrong'
NNP -> 'Army'
NNP -> 'Arnold'
NNP -> 'Ashland'
NNP -> 'Assembly'
NNP -> 'Asset'
NNP -> 'Associates'
NNP -> 'Association'
NNP -> 'Atlantic'
NNP -> 'Atlantis'
NNP -> 'Augpoint'
NNP -> 'August'
NNP -> 'Austin'
NNP -> 'Australia'
NNP -> 'Average'
NNP -> 'BNL'
NNP -> 'Banc'
NNP -> 'Banco'
NNP -> 'Bank'
NNP -> 'BankAmerica'
NNP -> 'Bankers'
NNP -> 'Banking'
NNP -> 'Banque'
NNP -> 'Barry'
NNP -> 'Bartlett'
NNP -> 'Bay'
NNP -> 'Beatrice'
NNP -> 'Belgium'
NNP -> 'Bell'
NNP -> 'Berry'
NNP -> 'Beverly'
NNP -> 'Bill'
NNP -> 'Black'
NNP -> 'Bob'
NNP -> 'Bombay'
NNP -> 'Boyd'
NNP -> 'Bradford'
NNP -> 'Bradley'
NNP -> 'Brawer'
NNP -> 'Breeden'
NNP -> 'Brian'
NNP -> 'Bridge'
NNP -> 'Broadcasting'
NNP -> 'Budapest'
NNP -> 'Budget'
NNP -> 'Buffett'
NNP -> 'Building'
NNP -> 'Bureau'
NNP -> 'Burmah'
NNP -> 'Burnham'
NNP -> 'Burt'
NNP -> 'Business'
NNP -> 'CFCs'
NNP -> 'CFTC'
NNP -> 'CMS'
NNP -> 'CS'
NNP -> 'Cabrera'
NNP -> 'Cadillac'
NNP -> 'Califpoint'
NNP -> 'Caltrans'
NNP -> 'Campbell'
NNP -> 'Cancer'
NNP -> 'Capital'
NNP -> 'Carl'
NNP -> 'Carlos'
NNP -> 'Cellular'
NNP -> 'CenTrust'
NNP -> 'Chancellor'
NNP -> 'Chapter'
NNP -> 'Chase'
NNP -> 'Cheer'
NNP -> 'Chevrolet'
NNP -> 'Chicago'
NNP -> 'China'
NNP -> 'Christie'
NNP -> 'Ciepoint'
NNP -> 'Cineplex'
NNP -> 'Citicorp'
NNP -> 'Clara'
NNP -> 'Clark'
NNP -> 'Class'
NNP -> 'Co'
NNP -> 'Cocom'
NNP -> 'Code'
NNP -> 'Cohen'
NNP -> 'Coleman'
NNP -> 'Colgate'
NNP -> 'College'
NNP -> 'Color'
NNP -> 'Commerce'
NNP -> 'Commission'
NNP -> 'Commodore'
NNP -> 'Commonwealth'
NNP -> 'Company'
NNP -> 'Compaq'
NNP -> 'Computer'
NNP -> 'Connecticut'
NNP -> 'Conner'
NNP -> 'Connpoint'
NNP -> 'Consolidated'
NNP -> 'Container'
NNP -> 'Continental'
NNP -> 'Contra'
NNP -> 'Corning'
NNP -> 'Corporate'
NNP -> 'Corppoint'
NNP -> 'Cospoint'
NNP -> 'Courter'
NNP -> 'Cpoint'
NNP -> 'Cross'
NNP -> 'Cruise'
NNP -> 'Cup'
NNP -> 'Czechoslovakia'
NNP -> 'DAX'
NNP -> 'DPC'
NNP -> 'DWG'
NNP -> 'Daily'
NNP -> 'Daiwa'
NNP -> 'Dalkon'
NNP -> 'Danny'
NNP -> 'Datapoint'
NNP -> 'Dataproducts'
NNP -> 'David'
NNP -> 'Davis'
NNP -> 'December'
NNP -> 'Delaware'
NNP -> 'Dell'
NNP -> 'Deloitte'
NNP -> 'Dentsu'
NNP -> 'Dick'
NNP -> 'Diego'
NNP -> 'Dingell'
NNP -> 'Dinkins'
NNP -> 'District'
NNP -> 'Doman'
NNP -> 'Don'
NNP -> 'Dow'
NNP -> 'DpointTpoint'
NNP -> 'Dresdner'
NNP -> 'Drexel'
NNP -> 'Dreyfus'
NNP -> 'Drpoint'
NNP -> 'Du'
NNP -> 'Dunkin'
NNP -> 'EPA'
NNP -> 'EPO'
NNP -> 'Earth'
NNP -> 'Eastman'
NNP -> 'Economic'
NNP -> 'Edelman'
NNP -> 'Education'
NNP -> 'Edward'
NNP -> 'Edwards'
NNP -> 'Egg'
NNP -> 'Electric'
NNP -> 'Elizabeth'
NNP -> 'English'
NNP -> 'Entertainment'
NNP -> 'Equity'
NNP -> 'Erich'
NNP -> 'Estate'
NNP -> 'Eurocom'
NNP -> 'European'
NNP -> 'Exterior'
NNP -> 'Exxon'
NNP -> 'FBI'
NNP -> 'FCC'
NNP -> 'FEMA'
NNP -> 'FTC'
NNP -> 'FTSE'
NNP -> 'Fannie'
NNP -> 'Far'
NNP -> 'February'
NNP -> 'Federated'
NNP -> 'Federation'
NNP -> 'Fidelity'
NNP -> 'Financiere'
NNP -> 'Finland'
NNP -> 'Fireman'
NNP -> 'First'
NNP -> 'Fitzwater'
NNP -> 'Flapoint'
NNP -> 'Foods'
NNP -> 'Force'
NNP -> 'Foreign'
NNP -> 'Fort'
NNP -> 'Fox'
NNP -> 'Fpoint'
NNP -> 'Frankfurt'
NNP -> 'Freddie'
NNP -> 'Freeman'
NNP -> 'French'
NNP -> 'Friday'
NNP -> 'Friedman'
NNP -> 'Friend'
NNP -> 'Funding'
NNP -> 'GMAC'
NNP -> 'Gabelli'
NNP -> 'Galileo'
NNP -> 'Gandhi'
NNP -> 'Gapoint'
NNP -> 'Gas'
NNP -> 'General'
NNP -> 'Generale'
NNP -> 'Genetics'
NNP -> 'George'
NNP -> 'Georgia'
NNP -> 'GeorgiaPacific'
NNP -> 'Giants'
NNP -> 'Ginnie'
NNP -> 'Glenn'
NNP -> 'Gold'
NNP -> 'Golden'
NNP -> 'Goldman'
NNP -> 'Goodson'
NNP -> 'Goupil'
NNP -> 'GrammRudman'
NNP -> 'Graphics'
NNP -> 'Gray'
NNP -> 'Grenfell'
NNP -> 'Guard'
NNP -> 'Guber'
NNP -> 'Guinness'
NNP -> 'Gulf'
NNP -> 'Guzman'
NNP -> 'H&R'
NNP -> 'HBO'
NNP -> 'Hall'
NNP -> 'Hammond'
NNP -> 'Hampshire'
NNP -> 'Hanover'
NNP -> 'Harris'
NNP -> 'Harvard'
NNP -> 'Hastings'
NNP -> 'Hatch'
NNP -> 'Henry'
NNP -> 'Herald'
NNP -> 'Hertz'
NNP -> 'Hess'
NNP -> 'HewlettPackard'
NNP -> 'Holdings'
NNP -> 'Holiday'
NNP -> 'Home'
NNP -> 'HomeFed'
NNP -> 'Honda'
NNP -> 'Honecker'
NNP -> 'Hong'
NNP -> 'Hooker'
NNP -> 'House'
NNP -> 'Hudson'
NNP -> 'Hughes'
NNP -> 'Humana'
NNP -> 'Hutchinson'
NNP -> 'IBM'
NNP -> 'ISI'
NNP -> 'Icahn'
NNP -> 'Ill'
NNP -> 'Illuminating'
NNP -> 'Inco'
NNP -> 'Income'
NNP -> 'Index'
NNP -> 'Industrial'
NNP -> 'Industry'
NNP -> 'Information'
NNP -> 'Ingersoll'
NNP -> 'Institute'
NNP -> 'Intelogic'
NNP -> 'Intermediate'
NNP -> 'Interstate'
NNP -> 'Investors'
NNP -> 'Ira'
NNP -> 'Iran'
NNP -> 'IranContra'
NNP -> 'Ireland'
NNP -> 'Irving'
NNP -> 'Island'
NNP -> 'Israel'
NNP -> 'Italy'
NNP -> 'Iverson'
NNP -> 'Jack'
NNP -> 'Jackson'
NNP -> 'January'
NNP -> 'Japan'
NNP -> 'Jefferies'
NNP -> 'Jeffrey'
NNP -> 'Jersey'
NNP -> 'John'
NNP -> 'Jonathan'
NNP -> 'Journal'
NNP -> 'Jpoint'
NNP -> 'Kangyo'
NNP -> 'Kao'
NNP -> 'Katz'
NNP -> 'Keating'
NNP -> 'Kenneth'
NNP -> 'Kingdom'
NNP -> 'Kohl'
NNP -> 'Korea'
NNP -> 'Kpoint'
NNP -> 'Kuala'
NNP -> 'Labor'
NNP -> 'Land'
NNP -> 'Larry'
NNP -> 'Latin'
NNP -> 'Law'
NNP -> 'Leader'
NNP -> 'League'
NNP -> 'Legal'
NNP -> 'Leipzig'
NNP -> 'Lewis'
NNP -> 'Lexington'
NNP -> 'Libor'
NNP -> 'Life'
NNP -> 'Lilly'
NNP -> 'Limited'
NNP -> 'Line'
NNP -> 'Litigation'
NNP -> 'Lloyd'
NNP -> 'London'
NNP -> 'Loral'
NNP -> 'Lorenzo'
NNP -> 'Louisville'
NNP -> 'LpointJpoint'
NNP -> 'MCA'
NNP -> 'MGM:slash:UA'
NNP -> 'Machines'
NNP -> 'Mack'
NNP -> 'Macmillan'
NNP -> 'Mae'
NNP -> 'Major'
NNP -> 'Majority'
NNP -> 'Malaysia'
NNP -> 'Malcolm'
NNP -> 'Management'
NNP -> 'Market'
NNP -> 'Marketing'
NNP -> 'Marlin'
NNP -> 'Maryland'
NNP -> 'Masspoint'
NNP -> 'Max'
NNP -> 'May'
NNP -> 'McCaw'
NNP -> 'McDonald'
NNP -> 'McDonough'
NNP -> 'McDuffie'
NNP -> 'McGrawHill'
NNP -> 'Mdpoint'
NNP -> 'Media'
NNP -> 'Medicine'
NNP -> 'Mehl'
NNP -> 'Merc'
NNP -> 'Mercantile'
NNP -> 'Meridian'
NNP -> 'Merieux'
NNP -> 'Merkur'
NNP -> 'Mesa'
NNP -> 'Miami'
NNP -> 'Michael'
NNP -> 'Mike'
NNP -> 'Milan'
NNP -> 'Miller'
NNP -> 'Mills'
NNP -> 'Milunovich'
NNP -> 'Ministry'
NNP -> 'Mips'
NNP -> 'Mississippi'
NNP -> 'Mitchell'
NNP -> 'Mobil'
NNP -> 'Money'
NNP -> 'Montgomery'
NNP -> 'Montreal'
NNP -> 'Moody'
NNP -> 'Moore'
NNP -> 'Morishita'
NNP -> 'Moscow'
NNP -> 'Motor'
NNP -> 'Mullins'
NNP -> 'Municipal'
NNP -> 'Murdoch'
NNP -> 'NAHB'
NNP -> 'NASA'
NNP -> 'NATO'
NNP -> 'NBC'
NNP -> 'NEC'
NNP -> 'NIH'
NNP -> 'NYSE'
NNP -> 'Nashua'
NNP -> 'National'
NNP -> 'Navigation'
NNP -> 'Neal'
NNP -> 'Nebpoint'
NNP -> 'Needham'
NNP -> 'Nekoosa'
NNP -> 'Nestle'
NNP -> 'Newport'
NNP -> 'Nielsen'
NNP -> 'Nikkei'
NNP -> 'Nixon'
NNP -> 'Norman'
NNP -> 'North'
NNP -> 'Northeast'
NNP -> 'Northern'
NNP -> 'NpointC'
NNP -> 'NpointJ'
NNP -> 'NpointYpoint'
NNP -> 'Oakland'
NNP -> 'Octel'
NNP -> 'October'
NNP -> 'Office'
NNP -> 'Oklahoma'
NNP -> 'Oklapoint'
NNP -> 'Options'
NNP -> 'Oregon'
NNP -> 'Orepoint'
NNP -> 'Organization'
NNP -> 'Orkem'
NNP -> 'Otto'
NNP -> 'P&G'
NNP -> 'PASOK'
NNP -> 'PLC'
NNP -> 'PLO'
NNP -> 'PS'
NNP -> 'Pacific'
NNP -> 'Packwood'
NNP -> 'PaineWebber'
NNP -> 'Panama'
NNP -> 'Paper'
NNP -> 'Papoint'
NNP -> 'Paribas'
NNP -> 'Paris'
NNP -> 'Parker'
NNP -> 'Part'
NNP -> 'Partnership'
NNP -> 'Party'
NNP -> 'Pat'
NNP -> 'Patrick'
NNP -> 'Pemex'
NNP -> 'Penney'
NNP -> 'Pentagon'
NNP -> 'Peterson'
NNP -> 'Petrie'
NNP -> 'Pharmacia'
NNP -> 'Philadelphia'
NNP -> 'Philip'
NNP -> 'Phoenix'
NNP -> 'Pickens'
NNP -> 'Picop'
NNP -> 'Pinnacle'
NNP -> 'Pioneer'
NNP -> 'Pizza'
NNP -> 'Plant'
NNP -> 'Poland'
NNP -> 'Polaroid'
NNP -> 'Posner'
NNP -> 'Prebon'
NNP -> 'President'
NNP -> 'Price'
NNP -> 'Prudential'
NNP -> 'PrudentialBache'
NNP -> 'Public'
NNP -> 'Publishing'
NNP -> 'Qintex'
NNP -> 'Quebecor'
NNP -> 'Quotron'
NNP -> 'Radio'
NNP -> 'Rally'
NNP -> 'Ratners'
NNP -> 'Raymond'
NNP -> 'Reagan'
NNP -> 'Recognition'
NNP -> 'Redford'
NNP -> 'Reed'
NNP -> 'Reinvestment'
NNP -> 'Remic'
NNP -> 'Renaissance'
NNP -> 'Report'
NNP -> 'Reppoint'
NNP -> 'Republic'
NNP -> 'Republican'
NNP -> 'Research'
NNP -> 'Reserve'
NNP -> 'Resolution'
NNP -> 'Resources'
NNP -> 'Revenue'
NNP -> 'Revpoint'
NNP -> 'Reynolds'
NNP -> 'Richard'
NNP -> 'Richmond'
NNP -> 'Richter'
NNP -> 'Rick'
NNP -> 'Right'
NNP -> 'River'
NNP -> 'Roberts'
NNP -> 'Robertson'
NNP -> 'Rock'
NNP -> 'Rockwell'
NNP -> 'Roderick'
NNP -> 'Roh'
NNP -> 'Roman'
NNP -> 'Rowe'
NNP -> 'Runkel'
NNP -> 'Russell'
NNP -> 'Ruth'
NNP -> 'Ryder'
NNP -> 'S&L'
NNP -> 'SCI'
NNP -> 'SaabScania'
NNP -> 'Sachs'
NNP -> 'Salinger'
NNP -> 'Salomon'
NNP -> 'Sam'
NNP -> 'Sanford'
NNP -> 'Saudi'
NNP -> 'Savaiko'
NNP -> 'Schaeffer'
NNP -> 'ScheringPlough'
NNP -> 'Schwab'
NNP -> 'Schwarz'
NNP -> 'Sea'
NNP -> 'Sears'
NNP -> 'Section'
NNP -> 'Seidman'
NNP -> 'Seoul'
NNP -> 'Service'
NNP -> 'Services'
NNP -> 'Shack'
NNP -> 'Showtime'
NNP -> 'Simmons'
NNP -> 'Singapore'
NNP -> 'Sisulu'
NNP -> 'SmithKline'
NNP -> 'Social'
NNP -> 'Sony'
NNP -> 'Soo'
NNP -> 'Sotheby'
NNP -> 'Soup'
NNP -> 'Southeast'
NNP -> 'Southern'
NNP -> 'Soviet'
NNP -> 'Spain'
NNP -> 'Speaker'
NNP -> 'Sperry'
NNP -> 'Spiegel'
NNP -> 'Spointp'
NNP -> 'Springs'
NNP -> 'Squibb'
NNP -> 'Stanley'
NNP -> 'Star'
NNP -> 'State'
NNP -> 'States'
NNP -> 'StatesWest'
NNP -> 'Stateswest'
NNP -> 'Statistics'
NNP -> 'Stephen'
NNP -> 'Sterling'
NNP -> 'Steve'
NNP -> 'Stevens'
NNP -> 'Stewart'
NNP -> 'Store'
NNP -> 'Straszheim'
NNP -> 'Street'
NNP -> 'Suisse'
NNP -> 'Sun'
NNP -> 'Sunday'
NNP -> 'Superfund'
NNP -> 'Supervision'
NNP -> 'Sweden'
NNP -> 'Systems'
NNP -> 'Tax'
NNP -> 'Technology'
NNP -> 'Teddy'
NNP -> 'Telecommunications'
NNP -> 'Temple'
NNP -> 'Tenneco'
NNP -> 'Tennpoint'
NNP -> 'Texas'
NNP -> 'The'
NNP -> 'Thi'
NNP -> 'Third'
NNP -> 'Thompson'
NNP -> 'Three'
NNP -> 'Timbers'
NNP -> 'Times'
NNP -> 'Today'
NNP -> 'Tokyo'
NNP -> 'Toronto'
NNP -> 'Toseland'
NNP -> 'Tower'
NNP -> 'Trade'
NNP -> 'Trading'
NNP -> 'Trans'
NNP -> 'Trinity'
NNP -> 'Trump'
NNP -> 'Turner'
NNP -> 'UNESCO'
NNP -> 'Unilever'
NNP -> 'United'
NNP -> 'UpointSpointSpointRpoint'
NNP -> 'Va'
NNP -> 'Vancouver'
NNP -> 'Vapoint'
NNP -> 'Vax'
NNP -> 'Viacom'
NNP -> 'View'
NNP -> 'Vincent'
NNP -> 'Virginia'
NNP -> 'Volokh'
NNP -> 'WSJ'
NNP -> 'War'
NNP -> 'Ward'
NNP -> 'Warner'
NNP -> 'Warren'
NNP -> 'Warsaw'
NNP -> 'Webster'
NNP -> 'Wedtech'
NNP -> 'Weisfield'
NNP -> 'West'
NNP -> 'Westmoreland'
NNP -> 'Wilson'
NNP -> 'Windsor'
NNP -> 'Wisconsin'
NNP -> 'World'
NNP -> 'Wpoint'
NNP -> 'Xerox'
NNP -> 'Yale'
NNP -> 'Zealand'
NNP -> 'aids'
NNP -> 'assets'
NNP -> 'baker'
NNP -> 'chase'
NNP -> 'china'
NNP -> 'computer'
NNP -> 'control'
NNP -> 'du'
NNP -> 'giant'
NNP -> 'government'
NNP -> 'house'
NNP -> 'integrated'
NNP -> 'international'
NNP -> 'loan'
NNP -> 'midOctober'
NNP -> 'paper'
NNP -> 'prime'
NNP -> 'quantum'
NNP -> 'rally'
NNP -> 'rate'
NNP -> 'ready'
NNP -> 'royal'
NNP -> 'secretary'
NNP -> 'security'
NNP -> 'separately'
NNP -> 'silicon'
NNP -> 'south'
NNP -> 'sun'
NNP -> 'trust'
NNP -> 'van'
WRB -> 'How'
WRB -> 'where'
NPADV -> DT
NPADV -> DT NN
NPADV -> DT RB
NPADV -> NP PP
NPADV -> NP SBAR
NPADV -> NP VP
NPADV -> PRP
NPADV -> QP NNS
QPMONEY -> IN QPMONEY
QPMONEY -> RB QPMONEY
SBARNOM -> IN S
SBARNOM -> WHADVP S
SBARNOM -> WHNP S
X -> IN
X -> X NP
SYM -> 'a'
SYM -> STAR
NPR -> NNP
NPR -> NNP NNP
NPR -> NNPS NNP
NPR -> NPRS
WHADVP -> IN
WHADVP -> WRB RB
PP -> IN
PP -> IN ADJP
PP -> IN ADVP
PP -> IN NP
PP -> IN NPLOC
PP -> IN PP
PP -> NPR NP
PP -> RB PP
PP -> RP NP
PP -> TO NP
PP -> VBG NP
PP -> VBN NP
SBARTMP -> IN S
SBARTMP -> IN SNOM
PUNCpoint -> '.'
PUNCpoint -> '?'
LST -> LS
SBARPRD -> IN S
ROOT -> S
PUNCbquotebquote -> '`'
PUNCbquotebquote -> '``'
ADVP -> IN
ADVP -> IN DT
ADVP -> IN NN
ADVP -> JJ
ADVP -> JJR
ADVP -> RB IN
ADVP -> RB JJ
ADVP -> RB NP
ADVP -> RB RB
ADVP -> RB S
ADVP -> RBR
ADVP -> RBR IN
VBD -> 'accepted'
VBD -> 'accounted'
VBD -> 'accused'
VBD -> 'acknowledged'
VBD -> 'added'
VBD -> 'agreed'
VBD -> 'alleged'
VBD -> 'amended'
VBD -> 'amounted'
VBD -> 'appealed'
VBD -> 'appeared'
VBD -> 'argued'
VBD -> 'arrived'
VBD -> 'asked'
VBD -> 'asserted'
VBD -> 'attended'
VBD -> 'authorized'
VBD -> 'averaged'
VBD -> 'became'
VBD -> 'blamed'
VBD -> 'boosted'
VBD -> 'broke'
VBD -> 'built'
VBD -> 'came'
VBD -> 'capped'
VBD -> 'cited'
VBD -> 'climbed'
VBD -> 'closed'
VBD -> 'collapsed'
VBD -> 'concluded'
VBD -> 'considered'
VBD -> 'cost'
VBD -> 'created'
VBD -> 'cut'
VBD -> 'doubled'
VBD -> 'drove'
VBD -> 'earned'
VBD -> 'ended'
VBD -> 'endorsed'
VBD -> 'estimated'
VBD -> 'exceeded'
VBD -> 'expired'
VBD -> 'feared'
VBD -> 'fell'
VBD -> 'flew'
VBD -> 'fueled'
VBD -> 'gained'
VBD -> 'gave'
VBD -> 'generated'
VBD -> 'got'
VBD -> 'had'
VBD -> 'happened'
VBD -> 'held'
VBD -> 'helped'
VBD -> 'hinted'
VBD -> 'hoped'
VBD -> 'indicated'
VBD -> 'insisted'
VBD -> 'kicked'
VBD -> 'landed'
VBD -> 'led'
VBD -> 'looked'
VBD -> 'managed'
VBD -> 'marked'
VBD -> 'meant'
VBD -> 'moved'
VBD -> 'named'
VBD -> 'needed'
VBD -> 'noted'
VBD -> 'observed'
VBD -> 'occurred'
VBD -> 'placed'
VBD -> 'played'
VBD -> 'pleaded'
VBD -> 'plummeted'
VBD -> 'pointed'
VBD -> 'postponed'
VBD -> 'predicted'
VBD -> 'preferred'
VBD -> 'provided'
VBD -> 'pulled'
VBD -> 'questioned'
VBD -> 'raised'
VBD -> 'received'
VBD -> 'recommended'
VBD -> 'recorded'
VBD -> 'referred'
VBD -> 'reflected'
VBD -> 'resigned'
VBD -> 'retired'
VBD -> 'returned'
VBD -> 'rose'
VBD -> 'ruled'
VBD -> 'said'
VBD -> 'saw'
VBD -> 'seemed'
VBD -> 'served'
VBD -> 'shed'
VBD -> 'shot'
VBD -> 'signed'
VBD -> 'soared'
VBD -> 'sold'
VBD -> 'sparked'
VBD -> 'staged'
VBD -> 'stated'
VBD -> 'stemmed'
VBD -> 'stopped'
VBD -> 'stressed'
VBD -> 'succeeded'
VBD -> 'suffered'
VBD -> 'supported'
VBD -> 'surprised'
VBD -> 'suspended'
VBD -> 'termed'
VBD -> 'threw'
VBD -> 'triggered'
VBD -> 'trimmed'
VBD -> 'unveiled'
VBD -> 'used'
VBD -> 'valued'
VBD -> 'visited'
VBD -> 'went'
VBD -> 'withdrew'
MD -> 'Can'
MD -> 'may'
MD -> 'must'
MD -> 'wo'
SBARQ -> WHNP SQ
SPRP -> VP
UH -> 'quack'
SPRD -> VP
STPC -> SBARNOM VP
STPC -> VP
VBG -> 'Excluding'
VBG -> 'Having'
VBG -> 'Looking'
VBG -> 'Reflecting'
VBG -> 'Using'
VBG -> 'accepting'
VBG -> 'accompanying'
VBG -> 'acquiring'
VBG -> 'adjusting'
VBG -> 'advancing'
VBG -> 'affecting'
VBG -> 'announcing'
VBG -> 'attempting'
VBG -> 'attending'
VBG -> 'attracting'
VBG -> 'awaiting'
VBG -> 'backing'
VBG -> 'banning'
VBG -> 'beginning'
VBG -> 'being'
VBG -> 'believing'
VBG -> 'blocking'
VBG -> 'building'
VBG -> 'buying'
VBG -> 'catching'
VBG -> 'circulating'
VBG -> 'claiming'
VBG -> 'climbing'
VBG -> 'closing'
VBG -> 'coming'
VBG -> 'competing'
VBG -> 'concerning'
VBG -> 'confirming'
VBG -> 'considering'
VBG -> 'consisting'
VBG -> 'continuing'
VBG -> 'declaring'
VBG -> 'delivering'
VBG -> 'demanding'
VBG -> 'doubling'
VBG -> 'earning'
VBG -> 'encouraging'
VBG -> 'excluding'
VBG -> 'experiencing'
VBG -> 'explaining'
VBG -> 'exploring'
VBG -> 'facing'
VBG -> 'failing'
VBG -> 'featuring'
VBG -> 'feeling'
VBG -> 'finding'
VBG -> 'floating'
VBG -> 'flying'
VBG -> 'focusing'
VBG -> 'following'
VBG -> 'gaining'
VBG -> 'getting'
VBG -> 'granting'
VBG -> 'growing'
VBG -> 'helping'
VBG -> 'hitting'
VBG -> 'imposing'
VBG -> 'increasing'
VBG -> 'investing'
VBG -> 'issuing'
VBG -> 'joining'
VBG -> 'keeping'
VBG -> 'killing'
VBG -> 'lagging'
VBG -> 'launching'
VBG -> 'learning'
VBG -> 'limiting'
VBG -> 'living'
VBG -> 'lobbying'
VBG -> 'looking'
VBG -> 'losing'
VBG -> 'maintaining'
VBG -> 'marketing'
VBG -> 'matching'
VBG -> 'moving'
VBG -> 'mulling'
VBG -> 'negotiating'
VBG -> 'opening'
VBG -> 'ordering'
VBG -> 'picking'
VBG -> 'posting'
VBG -> 'pouring'
VBG -> 'predicting'
VBG -> 'preparing'
VBG -> 'preventing'
VBG -> 'prompting'
VBG -> 'pulling'
VBG -> 'pushing'
VBG -> 'reacting'
VBG -> 'referring'
VBG -> 'reflecting'
VBG -> 'remaining'
VBG -> 'resigning'
VBG -> 'resisting'
VBG -> 'responding'
VBG -> 'resulting'
VBG -> 'reviewing'
VBG -> 'riding'
VBG -> 'running'
VBG -> 'rushing'
VBG -> 'sending'
VBG -> 'serving'
VBG -> 'shifting'
VBG -> 'showing'
VBG -> 'shrinking'
VBG -> 'signing'
VBG -> 'slowing'
VBG -> 'soaring'
VBG -> 'spending'
VBG -> 'standing'
VBG -> 'starting'
VBG -> 'succeeding'
VBG -> 'suggesting'
VBG -> 'talking'
VBG -> 'thinking'
VBG -> 'trading'
VBG -> 'underlying'
VBG -> 'watching'
VBG -> 'weakening'
VBG -> 'wearing'
VBG -> 'working'
VBG -> 'writing'
VBG -> 'yielding'
FW -> 'glasnost'
FW -> 'pro'
FW -> 'vspoint'
VBN -> 'Asked'
VBN -> 'Given'
VBN -> 'Guaranteed'
VBN -> 'Posted'
VBN -> 'accepted'
VBN -> 'achieved'
VBN -> 'adjusted'
VBN -> 'advanced'
VBN -> 'affected'
VBN -> 'aged'
VBN -> 'aimed'
VBN -> 'appointed'
VBN -> 'approved'
VBN -> 'argued'
VBN -> 'arrived'
VBN -> 'asked'
VBN -> 'attached'
VBN -> 'authorized'
VBN -> 'awarded'
VBN -> 'barred'
VBN -> 'become'
VBN -> 'been'
VBN -> 'begun'
VBN -> 'believed'
VBN -> 'bound'
VBN -> 'brought'
VBN -> 'built'
VBN -> 'caused'
VBN -> 'changed'
VBN -> 'claimed'
VBN -> 'collapsed'
VBN -> 'combined'
VBN -> 'complicated'
VBN -> 'concluded'
VBN -> 'conducted'
VBN -> 'confirmed'
VBN -> 'continued'
VBN -> 'contributed'
VBN -> 'controlled'
VBN -> 'converted'
VBN -> 'convinced'
VBN -> 'covered'
VBN -> 'criticized'
VBN -> 'cut'
VBN -> 'dated'
VBN -> 'declined'
VBN -> 'delivered'
VBN -> 'denied'
VBN -> 'described'
VBN -> 'developed'
VBN -> 'died'
VBN -> 'diluted'
VBN -> 'disclosed'
VBN -> 'discovered'
VBN -> 'dominated'
VBN -> 'dropped'
VBN -> 'earned'
VBN -> 'elected'
VBN -> 'eliminated'
VBN -> 'employed'
VBN -> 'enacted'
VBN -> 'encouraged'
VBN -> 'engineered'
VBN -> 'entered'
VBN -> 'entitled'
VBN -> 'expanded'
VBN -> 'exposed'
VBN -> 'fallen'
VBN -> 'fed'
VBN -> 'felt'
VBN -> 'filed'
VBN -> 'financed'
VBN -> 'forecast'
VBN -> 'fueled'
VBN -> 'gotten'
VBN -> 'guaranteed'
VBN -> 'headed'
VBN -> 'hidden'
VBN -> 'hired'
VBN -> 'hurt'
VBN -> 'ignored'
VBN -> 'imported'
VBN -> 'included'
VBN -> 'initiated'
VBN -> 'installed'
VBN -> 'insured'
VBN -> 'intended'
VBN -> 'interpreted'
VBN -> 'introduced'
VBN -> 'justified'
VBN -> 'killed'
VBN -> 'known'
VBN -> 'learned'
VBN -> 'lifted'
VBN -> 'limited'
VBN -> 'located'
VBN -> 'matched'
VBN -> 'mentioned'
VBN -> 'narrowed'
VBN -> 'needed'
VBN -> 'noted'
VBN -> 'notified'
VBN -> 'opposed'
VBN -> 'ousted'
VBN -> 'owed'
VBN -> 'painted'
VBN -> 'passed'
VBN -> 'permitted'
VBN -> 'planned'
VBN -> 'pleased'
VBN -> 'presented'
VBN -> 'priced'
VBN -> 'printed'
VBN -> 'processed'
VBN -> 'produced'
VBN -> 'promised'
VBN -> 'proved'
VBN -> 'published'
VBN -> 'pulled'
VBN -> 'pushed'
VBN -> 'put'
VBN -> 'quoted'
VBN -> 'reflected'
VBN -> 'related'
VBN -> 'released'
VBN -> 'remained'
VBN -> 'renewed'
VBN -> 'replaced'
VBN -> 'requested'
VBN -> 'required'
VBN -> 'resolved'
VBN -> 'restricted'
VBN -> 'retired'
VBN -> 'returned'
VBN -> 'revised'
VBN -> 'risen'
VBN -> 'run'
VBN -> 'seen'
VBN -> 'selected'
VBN -> 'served'
VBN -> 'settled'
VBN -> 'shown'
VBN -> 'shut'
VBN -> 'slowed'
VBN -> 'soared'
VBN -> 'sold'
VBN -> 'sought'
VBN -> 'specified'
VBN -> 'stated'
VBN -> 'stolen'
VBN -> 'stopped'
VBN -> 'stuck'
VBN -> 'studied'
VBN -> 'succeeded'
VBN -> 'sued'
VBN -> 'supported'
VBN -> 'switched'
VBN -> 'taped'
VBN -> 'tendered'
VBN -> 'tested'
VBN -> 'thrown'
VBN -> 'tied'
VBN -> 'told'
VBN -> 'traded'
VBN -> 'transferred'
VBN -> 'tried'
VBN -> 'triggered'
VBN -> 'turned'
VBN -> 'used'
VBN -> 'viewed'
VBN -> 'watched'
VBN -> 'written'
VBP -> "'m"
VBP -> 'Do'
VBP -> 'account'
VBP -> 'appear'
VBP -> 'approve'
VBP -> 'are'
VBP -> 'build'
VBP -> 'buy'
VBP -> 'change'
VBP -> 'charge'
VBP -> 'cite'
VBP -> 'come'
VBP -> 'complain'
VBP -> 'consider'
VBP -> 'face'
VBP -> 'fall'
VBP -> 'fare'
VBP -> 'favor'
VBP -> 'hate'
VBP -> 'indicate'
VBP -> 'insist'
VBP -> 'intend'
VBP -> 'keep'
VBP -> 'like'
VBP -> 'live'
VBP -> 'lose'
VBP -> 'love'
VBP -> 'mean'
VBP -> 'pay'
VBP -> 'put'
VBP -> 'range'
VBP -> 'reach'
VBP -> 'read'
VBP -> 'realize'
VBP -> 'reflect'
VBP -> 'remain'
VBP -> 'rise'
VBP -> 'see'
VBP -> 'seem'
VBP -> 'show'
VBP -> 'stay'
VBP -> 'suspect'
VBP -> 'total'
VBP -> 'understand'
VBP -> 'view'
VBP -> 'wish'
VBP -> 'worry'
VBZ -> 'acknowledges'
VBZ -> 'admits'
VBZ -> 'advises'
VBZ -> 'agrees'
VBZ -> 'amounts'
VBZ -> 'asks'
VBZ -> 'asserts'
VBZ -> 'attracts'
VBZ -> 'bears'
VBZ -> 'boosts'
VBZ -> 'carries'
VBZ -> 'causes'
VBZ -> 'claims'
VBZ -> 'comes'
VBZ -> 'complains'
VBZ -> 'considers'
VBZ -> 'contains'
VBZ -> 'continues'
VBZ -> 'controls'
VBZ -> 'costs'
VBZ -> 'covers'
VBZ -> 'declines'
VBZ -> 'demonstrates'
VBZ -> 'denies'
VBZ -> 'does'
VBZ -> 'drops'
VBZ -> 'emerges'
VBZ -> 'explains'
VBZ -> 'faces'
VBZ -> 'falls'
VBZ -> 'follows'
VBZ -> 'gives'
VBZ -> 'goes'
VBZ -> 'grows'
VBZ -> 'happens'
VBZ -> 'has'
VBZ -> 'helps'
VBZ -> 'includes'
VBZ -> 'increases'
VBZ -> 'indicates'
VBZ -> 'is'
VBZ -> 'joins'
VBZ -> 'knows'
VBZ -> 'leaves'
VBZ -> 'likes'
VBZ -> 'maintains'
VBZ -> 'manages'
VBZ -> 'marks'
VBZ -> 'matches'
VBZ -> 'meets'
VBZ -> 'misses'
VBZ -> 'narrows'
VBZ -> 'offers'
VBZ -> 'pays'
VBZ -> 'places'
VBZ -> 'plans'
VBZ -> 'points'
VBZ -> 'prohibits'
VBZ -> 'provides'
VBZ -> 'quotes'
VBZ -> 'raises'
VBZ -> 'reaches'
VBZ -> 'recalls'
VBZ -> 'reflects'
VBZ -> 'remains'
VBZ -> 'requires'
VBZ -> 'retains'
VBZ -> 'returns'
VBZ -> 'says'
VBZ -> 'seeks'
VBZ -> 'seems'
VBZ -> 'shares'
VBZ -> 'specializes'
VBZ -> 'states'
VBZ -> 'stems'
VBZ -> 'takes'
VBZ -> 'talks'
VBZ -> 'throws'
VBZ -> 'tracks'
VBZ -> 'trades'
VBZ -> 'understands'
VBZ -> 'wants'
VBZ -> 'widens'
VBZ -> 'works'
NN -> 'Chapter'
NN -> 'Everybody'
NN -> 'HDTV'
NN -> 'House'
NN -> 'LBO'
NN -> 'Nothing'
NN -> 'S&L'
NN -> 'Series'
NN -> 'a'
NN -> 'absence'
NN -> 'acceptance'
NN -> 'accord'
NN -> 'act'
NN -> 'activity'
NN -> 'ad'
NN -> 'addition'
NN -> 'address'
NN -> 'administration'
NN -> 'advertising'
NN -> 'advice'
NN -> 'aftermath'
NN -> 'age'
NN -> 'aid'
NN -> 'aircraft'
NN -> 'airport'
NN -> 'ally'
NN -> 'aluminum'
NN -> 'analysis'
NN -> 'animal'
NN -> 'announcement'
NN -> 'anticipation'
NN -> 'anxiety'
NN -> 'apartheid'
NN -> 'apartment'
NN -> 'appeal'
NN -> 'appearance'
NN -> 'appetite'
NN -> 'application'
NN -> 'appointment'
NN -> 'appreciation'
NN -> 'area'
NN -> 'argument'
NN -> 'arm'
NN -> 'army'
NN -> 'asbestos'
NN -> 'assassination'
NN -> 'assembly'
NN -> 'asset'
NN -> 'assistance'
NN -> 'associate'
NN -> 'association'
NN -> 'assurance'
NN -> 'atmosphere'
NN -> 'attorney'
NN -> 'audience'
NN -> 'baby'
NN -> 'back'
NN -> 'balloon'
NN -> 'band'
NN -> 'bank'
NN -> 'banker'
NN -> 'banking'
NN -> 'bar'
NN -> 'base'
NN -> 'bear'
NN -> 'bearing'
NN -> 'beef'
NN -> 'beginning'
NN -> 'behavior'
NN -> 'benchmark'
NN -> 'bid'
NN -> 'bidding'
NN -> 'bill'
NN -> 'binge'
NN -> 'biotechnology'
NN -> 'blame'
NN -> 'board'
NN -> 'boiler'
NN -> 'book'
NN -> 'boost'
NN -> 'border'
NN -> 'brand'
NN -> 'break'
NN -> 'breaker'
NN -> 'brewer'
NN -> 'broadcast'
NN -> 'brokerage'
NN -> 'building'
NN -> 'burden'
NN -> 'bureau'
NN -> 'bus'
NN -> 'bushel'
NN -> 'business'
NN -> 'buy'
NN -> 'cable'
NN -> 'calendar'
NN -> 'candidate'
NN -> 'capacity'
NN -> 'card'
NN -> 'care'
NN -> 'cargo'
NN -> 'carpet'
NN -> 'carpeting'
NN -> 'carrier'
NN -> 'catalog'
NN -> 'category'
NN -> 'caution'
NN -> 'ceiling'
NN -> 'cell'
NN -> 'cent'
NN -> 'center'
NN -> 'chamber'
NN -> 'champion'
NN -> 'check'
NN -> 'chemical'
NN -> 'chief'
NN -> 'chip'
NN -> 'choice'
NN -> 'chunk'
NN -> 'church'
NN -> 'cigarette'
NN -> 'circuit'
NN -> 'city'
NN -> 'claim'
NN -> 'climate'
NN -> 'climb'
NN -> 'closing'
NN -> 'coal'
NN -> 'cocoa'
NN -> 'code'
NN -> 'coffee'
NN -> 'collateral'
NN -> 'collection'
NN -> 'color'
NN -> 'column'
NN -> 'comfort'
NN -> 'commission'
NN -> 'community'
NN -> 'comparison'
NN -> 'competition'
NN -> 'competitor'
NN -> 'complaint'
NN -> 'completion'
NN -> 'compound'
NN -> 'compromise'
NN -> 'computer'
NN -> 'conclusion'
NN -> 'confidence'
NN -> 'conglomerate'
NN -> 'congress'
NN -> 'congressman'
NN -> 'conservation'
NN -> 'consolidation'
NN -> 'consortium'
NN -> 'construction'
NN -> 'consultant'
NN -> 'consumption'
NN -> 'contest'
NN -> 'context'
NN -> 'contract'
NN -> 'convention'
NN -> 'corner'
NN -> 'cost'
NN -> 'council'
NN -> 'course'
NN -> 'coverage'
NN -> 'credit'
NN -> 'crime'
NN -> 'criticism'
NN -> 'cruise'
NN -> 'currency'
NN -> 'cycle'
NN -> 'danger'
NN -> 'data'
NN -> 'date'
NN -> 'day'
NN -> 'deal'
NN -> 'dealer'
NN -> 'debacle'
NN -> 'debut'
NN -> 'decade'
NN -> 'declaration'
NN -> 'decline'
NN -> 'default'
NN -> 'defense'
NN -> 'definition'
NN -> 'deflator'
NN -> 'degree'
NN -> 'delegation'
NN -> 'demand'
NN -> 'depositary'
NN -> 'depository'
NN -> 'deputy'
NN -> 'destruction'
NN -> 'detective'
NN -> 'deterioration'
NN -> 'devaluation'
NN -> 'device'
NN -> 'difficulty'
NN -> 'direction'
NN -> 'director'
NN -> 'disappointment'
NN -> 'disaster'
NN -> 'discipline'
NN -> 'discount'
NN -> 'disease'
NN -> 'disk'
NN -> 'dismissal'
NN -> 'distance'
NN -> 'distributor'
NN -> 'district'
NN -> 'dog'
NN -> 'doubt'
NN -> 'downtown'
NN -> 'draft'
NN -> 'drop'
NN -> 'drug'
NN -> 'duty'
NN -> 'earning'
NN -> 'earthquake'
NN -> 'edge'
NN -> 'editor'
NN -> 'efficiency'
NN -> 'effort'
NN -> 'egg'
NN -> 'electricity'
NN -> 'element'
NN -> 'embarrassment'
NN -> 'embryo'
NN -> 'employee'
NN -> 'enactment'
NN -> 'encouragement'
NN -> 'energy'
NN -> 'enforcement'
NN -> 'engine'
NN -> 'engineer'
NN -> 'engineering'
NN -> 'entry'
NN -> 'environment'
NN -> 'equity'
NN -> 'era'
NN -> 'error'
NN -> 'estate'
NN -> 'estimate'
NN -> 'ethylene'
NN -> 'evening'
NN -> 'event'
NN -> 'everyone'
NN -> 'evolution'
NN -> 'examination'
NN -> 'exception'
NN -> 'exclusion'
NN -> 'excuse'
NN -> 'exercise'
NN -> 'exhibit'
NN -> 'exhibition'
NN -> 'expansion'
NN -> 'experience'
NN -> 'export'
NN -> 'extradition'
NN -> 'facility'
NN -> 'factory'
NN -> 'failure'
NN -> 'fairness'
NN -> 'fall'
NN -> 'family'
NN -> 'fate'
NN -> 'father'
NN -> 'favor'
NN -> 'fee'
NN -> 'feeling'
NN -> 'fence'
NN -> 'filing'
NN -> 'fine'
NN -> 'fire'
NN -> 'flag'
NN -> 'flavor'
NN -> 'fleet'
NN -> 'flexibility'
NN -> 'flight'
NN -> 'flood'
NN -> 'floor'
NN -> 'flow'
NN -> 'following'
NN -> 'food'
NN -> 'football'
NN -> 'forest'
NN -> 'form'
NN -> 'formation'
NN -> 'formula'
NN -> 'fraction'
NN -> 'franchise'
NN -> 'friend'
NN -> 'front'
NN -> 'fuel'
NN -> 'fund'
NN -> 'gain'
NN -> 'gallery'
NN -> 'gamble'
NN -> 'gas'
NN -> 'gasoline'
NN -> 'general'
NN -> 'ghost'
NN -> 'giant'
NN -> 'glass'
NN -> 'group'
NN -> 'growth'
NN -> 'guarantee'
NN -> 'guide'
NN -> 'habit'
NN -> 'headline'
NN -> 'headquarters'
NN -> 'hearing'
NN -> 'heart'
NN -> 'hell'
NN -> 'high'
NN -> 'highway'
NN -> 'hit'
NN -> 'hold'
NN -> 'holder'
NN -> 'home'
NN -> 'honor'
NN -> 'hope'
NN -> 'hospital'
NN -> 'host'
NN -> 'household'
NN -> 'husband'
NN -> 'i'
NN -> 'idea'
NN -> 'identity'
NN -> 'image'
NN -> 'impact'
NN -> 'impeachment'
NN -> 'impression'
NN -> 'improvement'
NN -> 'incentive'
NN -> 'incident'
NN -> 'incinerator'
NN -> 'inclination'
NN -> 'independence'
NN -> 'indexarbitrage'
NN -> 'indication'
NN -> 'indictment'
NN -> 'industry'
NN -> 'initiative'
NN -> 'insider'
NN -> 'inspector'
NN -> 'institute'
NN -> 'institution'
NN -> 'insulin'
NN -> 'insurer'
NN -> 'intelligence'
NN -> 'interview'
NN -> 'intraday'
NN -> 'introduction'
NN -> 'investigation'
NN -> 'investor'
NN -> 'involvement'
NN -> 'island'
NN -> 'issue'
NN -> 'jail'
NN -> 'jewelry'
NN -> 'job'
NN -> 'joint'
NN -> 'judge'
NN -> 'judgment'
NN -> 'junkbond'
NN -> 'kind'
NN -> 'knowledge'
NN -> 'labormanagement'
NN -> 'lack'
NN -> 'lady'
NN -> 'land'
NN -> 'launch'
NN -> 'law'
NN -> 'lawsuit'
NN -> 'lawyer'
NN -> 'leader'
NN -> 'leadership'
NN -> 'lease'
NN -> 'leg'
NN -> 'legislation'
NN -> 'leisure'
NN -> 'lesson'
NN -> 'letter'
NN -> 'level'
NN -> 'library'
NN -> 'license'
NN -> 'life'
NN -> 'linage'
NN -> 'liquidity'
NN -> 'load'
NN -> 'loan'
NN -> 'lobby'
NN -> 'location'
NN -> 'look'
NN -> 'low'
NN -> 'luxury'
NN -> 'luxurycar'
NN -> 'machine'
NN -> 'machinery'
NN -> 'magazine'
NN -> 'mainframe'
NN -> 'maintenance'
NN -> 'man'
NN -> 'management'
NN -> 'mandate'
NN -> 'maneuver'
NN -> 'manufacturer'
NN -> 'march'
NN -> 'marketplace'
NN -> 'massacre'
NN -> 'master'
NN -> 'material'
NN -> 'matter'
NN -> 'mayor'
NN -> 'measure'
NN -> 'medicine'
NN -> 'member'
NN -> 'memory'
NN -> 'merchandise'
NN -> 'merit'
NN -> 'mess'
NN -> 'message'
NN -> 'midday'
NN -> 'middle'
NN -> 'midnight'
NN -> 'milk'
NN -> 'mine'
NN -> 'minute'
NN -> 'missile'
NN -> 'mix'
NN -> 'moment'
NN -> 'month'
NN -> 'mood'
NN -> 'mortality'
NN -> 'mother'
NN -> 'move'
NN -> 'mural'
NN -> 'mystery'
NN -> 'nation'
NN -> 'niche'
NN -> 'nomination'
NN -> 'none'
NN -> 'north'
NN -> 'nose'
NN -> 'notebook'
NN -> 'notion'
NN -> 'obligation'
NN -> 'officer'
NN -> 'one'
NN -> 'onethird'
NN -> 'operator'
NN -> 'opinion'
NN -> 'opponent'
NN -> 'optimism'
NN -> 'order'
NN -> 'organization'
NN -> 'outcome'
NN -> 'output'
NN -> 'ownership'
NN -> 'ozone'
NN -> 'p53'
NN -> 'pace'
NN -> 'packaging'
NN -> 'page'
NN -> 'painting'
NN -> 'paper'
NN -> 'parent'
NN -> 'park'
NN -> 'parliament'
NN -> 'participation'
NN -> 'partner'
NN -> 'partnership'
NN -> 'past'
NN -> 'pasta'
NN -> 'pattern'
NN -> 'pay'
NN -> 'peak'
NN -> 'percent'
NN -> 'perception'
NN -> 'period'
NN -> 'permission'
NN -> 'personalcomputer'
NN -> 'perspective'
NN -> 'petrochemical'
NN -> 'petroleum'
NN -> 'phone'
NN -> 'place'
NN -> 'placement'
NN -> 'plan'
NN -> 'plant'
NN -> 'plastic'
NN -> 'plate'
NN -> 'platform'
NN -> 'platinum'
NN -> 'play'
NN -> 'playing'
NN -> 'plea'
NN -> 'poison'
NN -> 'police'
NN -> 'policy'
NN -> 'poll'
NN -> 'pollution'
NN -> 'popularity'
NN -> 'position'
NN -> 'poverty'
NN -> 'power'
NN -> 'preamble'
NN -> 'predecessor'
NN -> 'prelude'
NN -> 'premium'
NN -> 'presence'
NN -> 'presidency'
NN -> 'president'
NN -> 'press'
NN -> 'pressure'
NN -> 'pretax'
NN -> 'pride'
NN -> 'primetime'
NN -> 'print'
NN -> 'printer'
NN -> 'prison'
NN -> 'privatization'
NN -> 'problem'
NN -> 'procedure'
NN -> 'process'
NN -> 'producer'
NN -> 'program'
NN -> 'programming'
NN -> 'programtrading'
NN -> 'progress'
NN -> 'promise'
NN -> 'proportion'
NN -> 'prosperity'
NN -> 'protest'
NN -> 'province'
NN -> 'proxy'
NN -> 'psyllium'
NN -> 'publication'
NN -> 'publisher'
NN -> 'pulp'
NN -> 'purchasing'
NN -> 'push'
NN -> 'quake'
NN -> 'quarter'
NN -> 'question'
NN -> 'radar'
NN -> 'railroad'
NN -> 'rain'
NN -> 'ranch'
NN -> 'rate'
NN -> 'ratio'
NN -> 'reaction'
NN -> 'rebound'
NN -> 'recognition'
NN -> 'recommendation'
NN -> 'recording'
NN -> 'recovery'
NN -> 'red'
NN -> 'reduction'
NN -> 'refund'
NN -> 'region'
NN -> 'registration'
NN -> 'regulation'
NN -> 'regulator'
NN -> 'reinsurance'
NN -> 'rejection'
NN -> 'relationship'
NN -> 'reliance'
NN -> 'relief'
NN -> 'remainder'
NN -> 'renewal'
NN -> 'repair'
NN -> 'repeal'
NN -> 'replacement'
NN -> 'representative'
NN -> 'reputation'
NN -> 'request'
NN -> 'requirement'
NN -> 'rescue'
NN -> 'research'
NN -> 'resignation'
NN -> 'resistance'
NN -> 'resort'
NN -> 'restaurant'
NN -> 'restraint'
NN -> 'restructuring'
NN -> 'result'
NN -> 'retailing'
NN -> 'retirement'
NN -> 'retreat'
NN -> 'return'
NN -> 'revision'
NN -> 'revival'
NN -> 'ride'
NN -> 'rise'
NN -> 'risk'
NN -> 'rival'
NN -> 'rout'
NN -> 'route'
NN -> 'rule'
NN -> 'ruling'
NN -> 'run'
NN -> 'safety'
NN -> 'satisfaction'
NN -> 'scale'
NN -> 'scandal'
NN -> 'scenario'
NN -> 'schedule'
NN -> 'school'
NN -> 'science'
NN -> 'search'
NN -> 'season'
NN -> 'second'
NN -> 'section'
NN -> 'security'
NN -> 'seed'
NN -> 'segment'
NN -> 'selfincrimination'
NN -> 'selloff'
NN -> 'sense'
NN -> 'sentence'
NN -> 'session'
NN -> 'setback'
NN -> 'sex'
NN -> 'shadow'
NN -> 'shame'
NN -> 'share'
NN -> 'shareholder'
NN -> 'shelf'
NN -> 'shift'
NN -> 'shipping'
NN -> 'shipyard'
NN -> 'shock'
NN -> 'shop'
NN -> 'shopping'
NN -> 'shortage'
NN -> 'show'
NN -> 'shuttle'
NN -> 'sign'
NN -> 'signal'
NN -> 'silver'
NN -> 'ski'
NN -> 'slowing'
NN -> 'smoking'
NN -> 'softdrink'
NN -> 'somebody'
NN -> 'source'
NN -> 'spacecraft'
NN -> 'specialty'
NN -> 'speculation'
NN -> 'speed'
NN -> 'spite'
NN -> 'sponsor'
NN -> 'spring'
NN -> 'square'
NN -> 'stability'
NN -> 'stadium'
NN -> 'staff'
NN -> 'star'
NN -> 'start'
NN -> 'status'
NN -> 'statute'
NN -> 'steelmaker'
NN -> 'step'
NN -> 'stock'
NN -> 'stockindex'
NN -> 'storage'
NN -> 'store'
NN -> 'strain'
NN -> 'stretch'
NN -> 'strike'
NN -> 'string'
NN -> 'strip'
NN -> 'struggle'
NN -> 'student'
NN -> 'style'
NN -> 'subcommittee'
NN -> 'substance'
NN -> 'substitute'
NN -> 'successor'
NN -> 'suggestion'
NN -> 'suitor'
NN -> 'support'
NN -> 'surplus'
NN -> 'surprise'
NN -> 'survey'
NN -> 'survival'
NN -> 'swing'
NN -> 'table'
NN -> 'takeover'
NN -> 'talk'
NN -> 'tape'
NN -> 'target'
NN -> 'task'
NN -> 'taste'
NN -> 'teacher'
NN -> 'team'
NN -> 'tender'
NN -> 'term'
NN -> 'test'
NN -> 'testing'
NN -> 'theater'
NN -> 'theory'
NN -> 'third'
NN -> 'threat'
NN -> 'time'
NN -> 'timetable'
NN -> 'title'
NN -> 'tonight'
NN -> 'total'
NN -> 'tour'
NN -> 'tourism'
NN -> 'town'
NN -> 'toxin'
NN -> 'track'
NN -> 'trading'
NN -> 'traffic'
NN -> 'training'
NN -> 'transport'
NN -> 'treasurer'
NN -> 'tree'
NN -> 'trip'
NN -> 'trough'
NN -> 'turnaround'
NN -> 'turnover'
NN -> 'tv'
NN -> 'type'
NN -> 'uncertainty'
NN -> 'unit'
NN -> 'upscale'
NN -> 'uptick'
NN -> 'utility'
NN -> 'valuation'
NN -> 'verdict'
NN -> 'victory'
NN -> 'video'
NN -> 'view'
NN -> 'vision'
NN -> 'volatility'
NN -> 'vote'
NN -> 'voting'
NN -> 'wake'
NN -> 'war'
NN -> 'warming'
NN -> 'watch'
NN -> 'weather'
NN -> 'weight'
NN -> 'well'
NN -> 'while'
NN -> 'willingness'
NN -> 'winter'
NN -> 'wire'
NN -> 'withdrawal'
NN -> 'work'
NN -> 'worker'
NN -> 'writedown'
NN -> 'writeoff'
NN -> 'writer'
NN -> 'year'
NN -> 'yearend'
NN -> 'yeast'
NN -> 'yesterday'
NN -> 'youth'
ADVPTMP -> ADVP SBAR
ADVPTMP -> NP IN
ADVPTMP -> RB RB
ADVPTMP -> RBR
ADVPTMP -> RBR NP
RRC -> ADVPTMP PPLOC
NX -> NPR
WHPP -> IN WHNP
WHPP -> TO WHNP
NP -> ADJP NN
NP -> ADJP NNS
NP -> ADJP NPRS
NP -> DT FW
NP -> DT NN
NP -> DT NNS
NP -> DT QPMONEY
NP -> FW
NP -> IN
NP -> IN QP
NP -> JJ NN
NP -> JJ NPR
NP -> JJ NPRS
NP -> JJR
NP -> JJR NN
NP -> JJR NNS
NP -> JJS
NP -> JJS NNS
NP -> NAC NNS
NP -> NAC NPR
NP -> NN PUNCcolon
NP -> NN PUNCpoint
NP -> NN QP
NP -> NN SBAR
NP -> NP
NP -> NP ADVPTMP
NP -> NP NP
NP -> NP NPLOC
NP -> NP NPTMP
NP -> NP PP
NP -> NP PPLOC
NP -> NP S
NP -> NP SBARLOC
NP -> NP SBARPRP
NP -> NP SBARTMP
NP -> NPR
NP -> NPR JJ
NP -> NPR NP
NP -> NPR PP
NP -> NPR PUNCcolon
NP -> NPR PUNCpoint
NP -> NPRS
NP -> NPRS NP
NP -> NPRS PUNCcolon
NP -> NPdollar NP
NP -> NPdollar NPR
NP -> PRP
NP -> PRP NP
NP -> PRPdollar
NP -> PRPdollar JJ
NP -> PRPdollar NNS
NP -> PRPdollar QPMONEY
NP -> QP
NP -> QP NN
NP -> QP NPRS
NP -> QP RB
NP -> QPMONEY
NP -> RB JJ
NP -> RB NN
NP -> RB NNS
NP -> RBR
NP -> S
NP -> VB NN
NP -> VBG
NP -> VBG NNS
NP -> VBN NN
NP -> WDT
ADVPPRD -> RB
PDT -> 'all'
NPdollar -> NP POS
CD -> '1,200'
CD -> '10'
CD -> '10,'
CD -> '100,'
CD -> '102'
CD -> '103'
CD -> '107'
CD -> '10point2'
CD -> '11'
CD -> '110'
CD -> '115'
CD -> '125'
CD -> '12:slash:32'
CD -> '12point5'
CD -> '130'
CD -> '13point50'
CD -> '14'
CD -> '149'
CD -> '14point5'
CD -> '155'
CD -> '15point6'
CD -> '16'
CD -> '16,'
CD -> '160'
CD -> '170'
CD -> '179'
CD -> '18'
CD -> '18,'
CD -> '1929'
CD -> '1967'
CD -> '1969'
CD -> '1970s'
CD -> '1972'
CD -> '1973'
CD -> '1975'
CD -> '1976'
CD -> '1978'
CD -> '198'
CD -> '1980'
CD -> '1981'
CD -> '1986'
CD -> '1990'
CD -> '1990s'
CD -> '1992'
CD -> '1995'
CD -> '1999'
CD -> '1:slash:2'
CD -> '1point1'
CD -> '1point15'
CD -> '1point20'
CD -> '1point25'
CD -> '1point26'
CD -> '1point39'
CD -> '1point5'
CD -> '1point50'
CD -> '1point75'
CD -> '1point8'
CD -> '2,'
CD -> '20'
CD -> '20,'
CD -> '2004'
CD -> '2018'
CD -> '2019'
CD -> '21'
CD -> '22'
CD -> '225'
CD -> '22point6'
CD -> '25'
CD -> '26'
CD -> '260'
CD -> '2638point73'
CD -> '2659point22'
CD -> '26point23'
CD -> '27'
CD -> '270'
CD -> '28'
CD -> '280'
CD -> '2point2'
CD -> '2point25'
CD -> '2point4'
CD -> '2point50'
CD -> '2point58'
CD -> '2point6'
CD -> '2point75'
CD -> '2point8'
CD -> '2point9'
CD -> '30,'
CD -> '35'
CD -> '350'
CD -> '350,'
CD -> '37'
CD -> '38'
CD -> '39point55'
CD -> '3:slash:32'
CD -> '3:slash:4'
CD -> '3point2'
CD -> '3point3'
CD -> '3point35'
CD -> '3point4'
CD -> '3point6'
CD -> '3point7'
CD -> '4,'
CD -> '400'
CD -> '41'
CD -> '44'
CD -> '46'
CD -> '4point4'
CD -> '4point75'
CD -> '4point875'
CD -> '5'
CD -> '50'
CD -> '51'
CD -> '52'
CD -> '53'
CD -> '54'
CD -> '550'
CD -> '56'
CD -> '57'
CD -> '58'
CD -> '5:slash:16'
CD -> '5point6'
CD -> '5point9'
CD -> '600'
CD -> '61'
CD -> '62'
CD -> '62point5'
CD -> '63point52'
CD -> '650'
CD -> '66'
CD -> '68'
CD -> '6point2'
CD -> '6point25'
CD -> '700,'
CD -> '71'
CD -> '74'
CD -> '750'
CD -> '76'
CD -> '78'
CD -> '79'
CD -> '7point10'
CD -> '7point5'
CD -> '7point93'
CD -> '7point95'
CD -> '8'
CD -> '800'
CD -> '85'
CD -> '88'
CD -> '89'
CD -> '8point25'
CD -> '8point30'
CD -> '8point32'
CD -> '8point33'
CD -> '8point375'
CD -> '8point5'
CD -> '8point50'
CD -> '8point75'
CD -> '8point8'
CD -> '9'
CD -> '96'
CD -> '97'
CD -> '98'
CD -> '9point4'
CD -> '9point6'
CD -> '9point7'
CD -> 'Ten'
CD -> 'Three'
CD -> 'billion'
CD -> 'four'
CD -> 'hundred'
CD -> 'nine'
CD -> 'seven'
CD -> 'three'
CD -> 'trillion'
PUNCcolon -> '-'
PUNCcolon -> '--'
PUNCcolon -> ':'
PUNCcolon -> ';'
NNPS -> 'Airlines'
NNPS -> 'Americans'
NNPS -> 'Appeals'
NNPS -> 'Appropriations'
NNPS -> 'Bankers'
NNPS -> 'Containers'
NNPS -> 'Contras'
NNPS -> 'Dealers'
NNPS -> 'Democrats'
NNPS -> 'Dynamics'
NNPS -> 'Facilities'
NNPS -> 'Giants'
NNPS -> 'Harbors'
NNPS -> 'Hills'
NNPS -> 'Investments'
NNPS -> 'Laboratories'
NNPS -> 'Lines'
NNPS -> 'Motors'
NNPS -> 'Netherlands'
NNPS -> 'Options'
NNPS -> 'Poles'
NNPS -> 'Rights'
NNPS -> 'Sciences'
NNPS -> 'Services'
NNPS -> 'States'
NNPS -> 'Systems'
NNPS -> 'Treasurys'
NNPS -> 'Utilities'
NNPS -> 'Workers'
SBARADV -> RB S
SBARADV -> SINV
SBARADV -> WHADVP S
SBARADV -> X S
PPTMP -> IN ADJP
PPTMP -> IN ADVP
PPTMP -> IN NP
PPTMP -> IN SBAR
PPTMP -> PP PP
SQ -> MD VP
JJS -> 'Most'
JJS -> 'biggest'
JJS -> 'greatest'
JJS -> 'highest'
JJS -> 'hottest'
JJS -> 'least'
JJS -> 'lowest'
JJR -> 'bigger'
JJR -> 'broader'
JJR -> 'cleaner'
JJR -> 'harder'
JJR -> 'smaller'
JJR -> 'steeper'
JJR -> 'wider'
JJR -> 'younger'
WPdollar -> 'whose'
SINV -> VP NP
ADJP -> ADJP PRN
ADJP -> ADVP JJ
ADJP -> IN NN
ADJP -> JJ NP
ADJP -> JJ PPTMP
ADJP -> JJ S
ADJP -> JJS
ADJP -> NPR JJ
ADJP -> PUNCdollar JJ
ADJP -> QP JJ
ADJP -> QP JJR
ADJP -> QP NN
ADJP -> QPMONEY
ADJP -> RB
ADJP -> RB JJR
ADJP -> RB JJS
ADJP -> RB VBG
ADJP -> RBR
ADJP -> VBN
ADVPLOC -> IN
ADVPLOC -> RB RB
SBARNOMPRD -> WHNP S
DT -> 'An'
DT -> 'Some'
DT -> 'The'
DT -> 'These'
DT -> 'This'
DT -> 'a'
DT -> 'an'
DT -> 'another'
DT -> 'any'
DT -> 'both'
DT -> 'each'
DT -> 'the'
DT -> 'this'
DT -> 'those'
ADJPPRD -> ADJP PP
ADJPPRD -> ADVP JJ
ADJPPRD -> JJ
ADJPPRD -> JJ PPLOC
ADJPPRD -> JJ S
ADJPPRD -> JJ SBAR
ADJPPRD -> NN
ADJPPRD -> NP JJR
ADJPPRD -> RB JJ
ADJPPRD -> RB VBN
ADJPPRD -> VBG
ADJPPRD -> VBN
ADJPPRD -> VBN PP
POS -> "'"
POS -> "'s"
TO -> 'to'
LS -> '3'
SBARLOC -> WHADVP S
NPPRD -> DT ADJP
NPPRD -> DT NNS
NPPRD -> JJ
NPPRD -> JJ NN
NPPRD -> JJ NNS
NPPRD -> JJR
NPPRD -> NP ADJP
NPPRD -> NP ADVP
NPPRD -> NP PP
NPPRD -> NP PPLOC
NPPRD -> NP SBARTMP
NPPRD -> NPR
NPPRD -> NPRS
NPPRD -> PRPdollar NN
NPPRD -> QP NN
SSBJ -> VP
NPLOC -> NP PP
NPLOC -> NPR
VB -> 'absorb'
VB -> 'accept'
VB -> 'act'
VB -> 'add'
VB -> 'address'
VB -> 'advise'
VB -> 'affect'
VB -> 'announce'
VB -> 'appeal'
VB -> 'appear'
VB -> 'apply'
VB -> 'approve'
VB -> 'argue'
VB -> 'ask'
VB -> 'assume'
VB -> 'attempt'
VB -> 'auction'
VB -> 'bear'
VB -> 'beat'
VB -> 'block'
VB -> 'bolster'
VB -> 'boost'
VB -> 'buy'
VB -> 'care'
VB -> 'cause'
VB -> 'challenge'
VB -> 'choose'
VB -> 'clear'
VB -> 'collapse'
VB -> 'comment'
VB -> 'compete'
VB -> 'contribute'
VB -> 'control'
VB -> 'convert'
VB -> 'correct'
VB -> 'count'
VB -> 'curtail'
VB -> 'cut'
VB -> 'decide'
VB -> 'defend'
VB -> 'delay'
VB -> 'demand'
VB -> 'deny'
VB -> 'depend'
VB -> 'describe'
VB -> 'design'
VB -> 'die'
VB -> 'discover'
VB -> 'do'
VB -> 'draw'
VB -> 'drive'
VB -> 'earn'
VB -> 'elaborate'
VB -> 'eliminate'
VB -> 'enhance'
VB -> 'ensure'
VB -> 'erode'
VB -> 'establish'
VB -> 'examine'
VB -> 'exchange'
VB -> 'execute'
VB -> 'expect'
VB -> 'explain'
VB -> 'express'
VB -> 'extend'
VB -> 'feel'
VB -> 'fight'
VB -> 'float'
VB -> 'get'
VB -> 'give'
VB -> 'go'
VB -> 'guarantee'
VB -> 'hear'
VB -> 'help'
VB -> 'hide'
VB -> 'hit'
VB -> 'identify'
VB -> 'indicate'
VB -> 'induce'
VB -> 'insist'
VB -> 'intend'
VB -> 'intensify'
VB -> 'intervene'
VB -> 'invest'
VB -> 'join'
VB -> 'keep'
VB -> 'know'
VB -> 'last'
VB -> 'launch'
VB -> 'lead'
VB -> 'learn'
VB -> 'lend'
VB -> 'lift'
VB -> 'look'
VB -> 'lose'
VB -> 'lower'
VB -> 'make'
VB -> 'manage'
VB -> 'match'
VB -> 'merge'
VB -> 'move'
VB -> 'name'
VB -> 'need'
VB -> 'notify'
VB -> 'obtain'
VB -> 'occur'
VB -> 'oppose'
VB -> 'oust'
VB -> 'override'
VB -> 'pay'
VB -> 'plan'
VB -> 'produce'
VB -> 'profit'
VB -> 'propose'
VB -> 'publish'
VB -> 'purchase'
VB -> 'quit'
VB -> 'receive'
VB -> 'record'
VB -> 'recover'
VB -> 'reduce'
VB -> 'reinforce'
VB -> 'represent'
VB -> 'resolve'
VB -> 'retain'
VB -> 'return'
VB -> 'revive'
VB -> 'risk'
VB -> 'say'
VB -> 'seek'
VB -> 'seem'
VB -> 'select'
VB -> 'sell'
VB -> 'send'
VB -> 'ship'
VB -> 'sit'
VB -> 'solve'
VB -> 'sort'
VB -> 'spark'
VB -> 'speak'
VB -> 'speculate'
VB -> 'stabilize'
VB -> 'start'
VB -> 'stay'
VB -> 'stock'
VB -> 'succeed'
VB -> 'supply'
VB -> 'talk'
VB -> 'total'
VB -> 'transform'
VB -> 'travel'
VB -> 'treat'
VB -> 'trust'
VB -> 'tumble'
VB -> 'veto'
VB -> 'visit'
VB -> 'wait'
VB -> 'watch'
VB -> 'wear'
VB -> 'win'
VB -> 'withdraw'
VB -> 'withstand'
VB -> 'worry'
RBS -> 'most'
RBR -> 'better'
RBR -> 'earlier'
RBR -> 'faster'
RBR -> 'further'
RBR -> 'higher'
RBR -> 'later'
INTJ -> RB
INTJ -> UH PUNCpoint
INTJ -> VB
VP -> JJ
VP -> JJ NP
VP -> TO
VP -> TO VP
VP -> VB
VP -> VB ADJPPRD
VP -> VB NPPRD
VP -> VB PP
VP -> VB PPLOCPRD
VP -> VB PPPRD
VP -> VB SBARADV
VP -> VB VP
VP -> VBD
VP -> VBD ADJPPRD
VP -> VBD ADVPLOCPRD
VP -> VBD ADVPTMP
VP -> VBD PP
VP -> VBD PPLOCPRD
VP -> VBD SBAR
VP -> VBD SBARADV
VP -> VBD SBARPRD
VP -> VBD SPRP
VP -> VBG ADJPPRD
VP -> VBG ADVP
VP -> VBG ADVPTMP
VP -> VBG PPLOC
VP -> VBG PPTMP
VP -> VBN ADVPPRD
VP -> VBN ADVPTMP
VP -> VBN NP
VP -> VBN NPTMP
VP -> VBN PP
VP -> VBN PPLOCPRD
VP -> VBN PPTMP
VP -> VBN SBARADV
VP -> VBN SPRD
VP -> VBN SPRP
VP -> VBP ADVPPRD
VP -> VBP NPTMP
VP -> VBP PP
VP -> VBP PPLOC
VP -> VBP PPPRD
VP -> VBP RB
VP -> VBP SBARNOM
VP -> VBZ
VP -> VBZ ADJPPRD
VP -> VBZ ADVP
VP -> VBZ ADVPLOC
VP -> VBZ ADVPLOCPRD
VP -> VBZ ADVPTMP
VP -> VBZ NP
VP -> VBZ PPLOC
VP -> VBZ PPPRD
VP -> VBZ PPTMP
VP -> VBZ SBARADV
SADV -> ADJPPRD
SADV -> ADVP VP
SADV -> ADVPPRD
SADV -> NP VP
SADV -> VP
IN -> 'By'
IN -> 'During'
IN -> 'For'
IN -> 'From'
IN -> 'In'
IN -> 'Of'
IN -> 'Unless'
IN -> 'While'
IN -> 'against'
IN -> 'although'
IN -> 'among'
IN -> 'as'
IN -> 'at'
IN -> 'behind'
IN -> 'below'
IN -> 'beneath'
IN -> 'beyond'
IN -> 'by'
IN -> 'de'
IN -> 'despite'
IN -> 'down'
IN -> 'during'
IN -> 'if'
IN -> 'into'
IN -> 'next'
IN -> 'of'
IN -> 'off'
IN -> 'on'
IN -> 'onto'
IN -> 'past'
IN -> 'so'
IN -> 'under'
IN -> 'up'
IN -> 'vspoint'
IN -> 'whether'
IN -> 'while'
IN -> 'with'
QP -> IN QP
QP -> JJ QP
QP -> RB DT
QP -> RB NN
QP -> RB QP
POUND -> '#'
PPLOC -> IN NP
PPLOC -> TO NP
WHADJP -> WRB JJ
WHNP -> NP PP
WHNP -> WDT NNS
WHNP -> WHNP WHPP
WHNP -> WP
WHNP -> WPdollar NN
WHNP -> WRB JJ
SNOM -> ADVP VP
SNOM -> ADVPTMP VP
SNOM -> NPdollar VP
PRPdollar -> 'My'
PRPdollar -> 'Their'
PRPdollar -> 'his'
PRPdollar -> 'my'
PRPdollar -> 'your'
NPTMP -> DT NN
NPTMP -> NN
NPTMP -> NP ADVP
NPTMP -> NP NPADV
NPTMP -> NP PP
NPTMP -> NP SBAR
NPTMP -> NPR NP
NPTMP -> QP
NPTMP -> RB NPR
S1 -> S0 NP
S2 -> S1 ADVPTMP
S3 -> S2 VP
S -> S3 PUNCpoint
S5 -> S4 NP
S6 -> S5 VP
S -> S6 PUNCpoint
S8 -> S7 PP
S10 -> S9 NP
S11 -> S10 VP
S -> S11 PUNCpoint
S12 -> ADVP NP
S -> S12 VP
S13 -> ADVP NP
S14 -> S13 VP
S -> S14 PUNCpoint
S15 -> ADVPLOC NP
S16 -> S15 VP
S -> S16 PUNCpoint
S18 -> S17 ADVP
S20 -> S19 NP
S21 -> S20 VP
S -> S21 PUNCpoint
S23 -> S22 PPTMP
S25 -> S24 NP
S26 -> S25 VP
S -> S26 PUNCpoint
S27 -> ADVPTMP NP
S -> S27 VP
S28 -> ADVPTMP PRN
S29 -> S28 NP
S30 -> S29 VP
S -> S30 PUNCpoint
S32 -> S31 NP
S33 -> S32 VP
S -> S33 PUNCpoint
S34 -> NP ADJPPRD
S -> S34 SBAR
S35 -> NP ADVP
S -> S35 VP
S36 -> NP ADVP
S37 -> S36 VP
S -> S37 PUNCpoint
S38 -> NP ADVPTMP
S39 -> S38 VP
S40 -> S39 PUNCpoint
S -> S40 PUNCquotequote
S42 -> S41 ADVP
S -> S43 VP
S45 -> S44 PP
S47 -> S46 VP
S -> S47 PUNCpoint
S49 -> S48 SBARADV
S51 -> S50 VP
S -> S51 PUNCpoint
S53 -> S52 VP
S -> S53 PUNCpoint
S54 -> NP PP
S55 -> S54 VP
S -> S55 PUNCpoint
S56 -> NP PPLOC
S57 -> S56 VP
S -> S57 PUNCpoint
S58 -> NP PPTMP
S59 -> S58 VP
S -> S59 PUNCpoint
S60 -> NP PRN
S -> S60 VP
S61 -> NP PRN
S62 -> S61 VP
S -> S62 PUNCpoint
S63 -> NP PRN
S64 -> S63 VP
S65 -> S64 PUNCpoint
S -> S65 PUNCquotequote
S66 -> NP PUNCbquotebquote
S -> S66 ADJPPRD
S67 -> NP PUNCbquotebquote
S -> S67 VP
S68 -> NP PUNCbquotebquote
S69 -> S68 VP
S -> S69 PUNCpoint
S70 -> NP VP
S -> S70 PP
S71 -> NP VP
S -> S71 PUNCpoint
S73 -> S72 NP
S74 -> S73 VP
S -> S74 PUNCpoint
S75 -> NPR VP
S -> S75 PUNCpoint
S77 -> S76 NP
S -> S77 VP
S79 -> S78 NP
S80 -> S79 VP
S81 -> S80 PUNCpoint
S -> S81 PUNCquotequote
S83 -> S82 SBARTMP
S85 -> S84 NP
S86 -> S85 VP
S -> S86 PUNCpoint
S87 -> NPTMP NP
S88 -> S87 VP
S -> S88 PUNCpoint
S90 -> S89 NP
S91 -> S90 ADVP
S92 -> S91 VP
S -> S92 PUNCpoint
S -> S93 VP
S94 -> PP NP
S95 -> S94 VP
S -> S95 PUNCpoint
S97 -> S96 ADVP
S99 -> S98 NP
S100 -> S99 VP
S -> S100 PUNCpoint
S102 -> S101 NP
S103 -> S102 ADVP
S104 -> S103 VP
S -> S104 PUNCpoint
S106 -> S105 NP
S107 -> S106 VP
S -> S107 PUNCpoint
S109 -> S108 NP
S110 -> S109 VP
S111 -> S110 PUNCpoint
S -> S111 PUNCquotequote
S113 -> S112 PP
S115 -> S114 NP
S116 -> S115 VP
S -> S116 PUNCpoint
S117 -> PPLOC PRN
S118 -> S117 NP
S119 -> S118 VP
S -> S119 PUNCpoint
S121 -> S120 NP
S122 -> S121 ADVP
S123 -> S122 VP
S -> S123 PUNCpoint
S125 -> S124 NP
S126 -> S125 VP
S -> S126 PUNCpoint
S128 -> S127 SBARTMP
S130 -> S129 NP
S131 -> S130 VP
S -> S131 PUNCpoint
S133 -> S132 VP
S134 -> S133 PUNCpoint
S -> S134 PUNCRRB
S137 -> S136 NP
S138 -> S137 VP
S139 -> S138 PUNCpoint
S -> S139 PUNCRRB
S140 -> PUNCbquotebquote ADVP
S141 -> S140 NP
S142 -> S141 VP
S143 -> S142 PUNCpoint
S -> S143 PUNCquotequote
S144 -> PUNCbquotebquote NP
S146 -> S145 PUNCquotequote
S147 -> S146 NP
S148 -> S147 VP
S -> S148 PUNCpoint
S149 -> PUNCbquotebquote NP
S150 -> S149 PRN
S151 -> S150 VP
S152 -> S151 PUNCpoint
S -> S152 PUNCquotequote
S153 -> PUNCbquotebquote NP
S154 -> S153 PUNCquotequote
S -> S154 VP
S155 -> PUNCbquotebquote NP
S -> S155 VP
S156 -> PUNCbquotebquote NP
S157 -> S156 VP
S158 -> S157 PUNCpoint
S -> S158 PUNCquotequote
S159 -> PUNCbquotebquote NPR
S160 -> S159 PUNCquotequote
S -> S160 VP
S161 -> PUNCbquotebquote PP
S163 -> S162 NP
S164 -> S163 VP
S -> S164 PUNCpoint
S165 -> PUNCbquotebquote PPTMP
S167 -> S166 NP
S168 -> S167 VP
S -> S168 PUNCpoint
S169 -> PUNCbquotebquote S
S171 -> S170 PUNCquotequote
S172 -> S171 NP
S173 -> S172 VP
S -> S173 PUNCpoint
S174 -> PUNCbquotebquote S
S175 -> S174 PUNCcolon
S176 -> S175 S
S177 -> S176 PUNCpoint
S -> S177 PUNCquotequote
S178 -> PUNCbquotebquote SBARADV
S180 -> S179 NP
S181 -> S180 VP
S -> S181 PUNCpoint
S182 -> PUNCbquotebquote STPC
S184 -> S183 PUNCquotequote
S185 -> S184 NP
S186 -> S185 VP
S -> S186 PUNCpoint
S187 -> PUNCbquotebquote STPC
S189 -> S188 PUNCquotequote
S190 -> S189 VP
S191 -> S190 NP
S -> S191 PUNCpoint
S192 -> PUNCcolon NP
S193 -> S192 VP
S -> S193 PUNCpoint
S194 -> PUNCcolon SBARADV
S196 -> S195 NP
S197 -> S196 VP
S -> S197 PUNCpoint
S198 -> S PUNCcolon
S199 -> S198 S
S -> S199 PUNCpoint
S200 -> S PUNCcolon
S201 -> S200 S
S202 -> S201 PUNCpoint
S -> S202 PUNCquotequote
S204 -> S203 NP
S205 -> S204 ADVP
S206 -> S205 VP
S -> S206 PUNCpoint
S208 -> S207 NP
S209 -> S208 ADVP
S210 -> S209 VP
S -> S210 PUNCpoint
S212 -> S211 NP
S213 -> S212 ADVPTMP
S214 -> S213 VP
S -> S214 PUNCpoint
S216 -> S215 NP
S217 -> S216 VP
S -> S217 PUNCpoint
S219 -> S218 NP
S220 -> S219 VP
S221 -> S220 PUNCpoint
S -> S221 PUNCquotequote
S222 -> SBARADV NP
S223 -> S222 VP
S -> S223 PUNCpoint
S224 -> SBARNOM VP
S -> S224 PUNCpoint
S226 -> S225 NP
S227 -> S226 VP
S -> S227 PUNCpoint
S228 -> SBARSBJ VP
S -> S228 PUNCpoint
S229 -> SBARTMP NP
S230 -> S229 VP
S -> S230 PUNCpoint
S232 -> S231 NP
S -> S232 VP
S234 -> S233 NP
S235 -> S234 VP
S -> S235 PUNCpoint
S236 -> STPC NP
S237 -> S236 VP
S -> S237 PUNCpoint
SBAR238 -> IN IN
SBAR -> SBAR238 S
SBAR239 -> RB IN
SBAR -> SBAR239 S
SBAR -> SBAR240 SBAR
PPPRD241 -> ADVP IN
PPPRD -> PPPRD241 NP
PPPRD242 -> RB IN
PPPRD -> PPPRD242 NP
NPRS243 -> NNP NNP
NPRS -> NPRS243 NNPS
PRN246 -> PRN245 VP
PRN -> PRN250 PUNCRRB
PRN253 -> PRN252 NP
PRN255 -> PRN254 NP
PRN -> PRN255 PUNCRRB
PRN258 -> PRN257 NPLOC
PRN -> PRN258 PUNCRRB
PRN -> PRN259 PUNCRRB
PRN -> PRN260 PUNCRRB
PRN -> PRN261 PUNCRRB
PRN -> PRN262 PUNCRRB
PRN263 -> PUNCcolon S
PRN -> PRN263 PUNCcolon
PRN264 -> PUNCcolon SBAR
PRN -> PRN264 PUNCcolon
QPMONEY265 -> IN QPMONEY
QPMONEY -> QPMONEY265 PP
PPLOCPRD266 -> ADVP IN
PPLOCPRD -> PPLOCPRD266 NP
NPR267 -> NNP NNP
NPR268 -> NPR267 NNP
NPR -> NPR268 NNP
NPR269 -> NNP NNP
NPR270 -> NPR269 NNP
NPR271 -> NPR270 NNP
NPR -> NPR271 NNP
NPR272 -> NNP NNP
NPR273 -> NPR272 NNP
NPR274 -> NPR273 NNP
NPR275 -> NPR274 NNP
NPR -> NPR275 NNP
NPR276 -> NNP NNP
NPR277 -> NPR276 NNP
NPR278 -> NPR277 NNP
NPR279 -> NPR278 NNP
NPR280 -> NPR279 NNP
NPR -> NPR280 NNP
NPR281 -> NNP NNP
NPR282 -> NPR281 NNP
NPR283 -> NPR282 NNPS
NPR -> NPR283 NNP
NPR284 -> NNP NNP
NPR285 -> NPR284 NNPS
NPR -> NPR285 NNP
PP286 -> ADVP IN
PP -> PP286 SNOM
PP287 -> IN PUNCbquotebquote
PP -> PP287 NP
PP288 -> IN PUNCbquotebquote
PP289 -> PP288 NP
PP -> PP289 PUNCquotequote
PP290 -> IN PUNCquotequote
PP -> PP290 NP
PP291 -> NP IN
PP -> PP291 NP
PP292 -> RB IN
PP -> PP292 NP
PP293 -> RB IN
PP -> PP293 PP
PP294 -> RB IN
PP -> PP294 SNOM
PP295 -> TO NP
PP -> PP295 PPTMP
PP296 -> TO PUNCbquotebquote
PP -> PP296 NP
SBARTMP297 -> ADVP IN
SBARTMP -> SBARTMP297 S
SBARTMP298 -> NP IN
SBARTMP -> SBARTMP298 S
SBARTMP299 -> NPADV IN
SBARTMP -> SBARTMP299 S
NACTMP301 -> NACTMP300 NPR
NACTMP302 -> NACTMP301 QP
NACTMP304 -> NACTMP303 QP
ADVP305 -> IN NP
ADVP -> ADVP305 PP
ADVP306 -> RB NP
ADVP -> ADVP306 PP
SBARQ307 -> PUNCbquotebquote WHADVP
SBARQ308 -> SBARQ307 SQ
SBARQ -> SBARQ308 PUNCpoint
SBARQ309 -> RB WHNP
SBARQ310 -> SBARQ309 SQ
SBARQ -> SBARQ310 PUNCpoint
STPC311 -> ADVPTMP NP
STPC -> STPC311 VP
STPC312 -> NP ADVPTMP
STPC -> STPC312 VP
STPC313 -> NP PUNCbquotebquote
STPC -> STPC313 VP
STPC314 -> NP VP
STPC315 -> NP VP
STPC -> STPC316 PUNCquotequote
STPC318 -> STPC317 NP
STPC -> STPC318 VP
NP319 -> ADJP DT
NP -> NP319 NN
NP320 -> ADJP JJ
NP -> NP320 NN
NP321 -> ADJP NN
NP -> NP321 NN
NP322 -> DT ADJP
NP323 -> NP322 JJ
NP -> NP323 NN
NP324 -> DT ADJP
NP325 -> NP324 JJ
NP326 -> NP325 NN
NP -> NP326 NN
NP327 -> DT ADJP
NP328 -> NP327 JJ
NP -> NP328 NNS
NP329 -> DT ADJP
NP -> NP329 NNS
NP330 -> DT ADJP
NP331 -> NP330 NNS
NP -> NP331 NN
NP332 -> DT ADJP
NP -> NP332 NPR
NP333 -> DT ADVP
NP -> NP333 NN
NP334 -> DT DT
NP335 -> NP334 JJ
NP -> NP335 NNS
NP336 -> DT JJ
NP337 -> NP336 ADJP
NP338 -> NP337 JJ
NP -> NP338 NN
NP339 -> DT JJ
NP341 -> NP340 JJ
NP -> NP341 NN
NP342 -> DT JJ
NP344 -> NP343 JJ
NP345 -> NP344 NPR
NP -> NP345 NP
NP346 -> DT JJ
NP -> NP346 JJ
NP347 -> DT JJ
NP348 -> NP347 JJ
NP -> NP348 NPR
NP349 -> DT JJ
NP350 -> NP349 JJ
NP351 -> NP350 NPR
NP -> NP351 NP
NP352 -> DT JJ
NP353 -> NP352 NN
NP354 -> NP353 NN
NP -> NP354 NNS
NP355 -> DT JJ
NP356 -> NP355 NN
NP357 -> NP356 NNS
NP -> NP357 NN
NP358 -> DT JJ
NP359 -> NP358 NN
NP -> NP359 NPR
NP360 -> DT JJ
NP361 -> NP360 NNS
NP -> NP361 NN
NP362 -> DT JJ
NP363 -> NP362 NNS
NP364 -> NP363 NN
NP -> NP364 NN
NP365 -> DT JJ
NP366 -> NP365 NNS
NP -> NP366 NNS
NP367 -> DT JJ
NP368 -> NP367 NPR
NP369 -> NP368 JJ
NP -> NP369 NN
NP370 -> DT JJ
NP371 -> NP370 QP
NP372 -> NP371 JJ
NP -> NP372 NNS
NP373 -> DT JJ
NP374 -> NP373 QP
NP -> NP374 NN
NP375 -> DT JJ
NP376 -> NP375 VBN
NP -> NP376 NN
NP377 -> DT JJR
NP378 -> NP377 NN
NP -> NP378 NN
NP379 -> DT JJS
NP380 -> NP379 JJ
NP -> NP380 NN
NP381 -> DT NAC
NP -> NP381 NPR
NP382 -> DT NACLOC
NP383 -> NP382 JJ
NP -> NP383 NN
NP384 -> DT NACLOC
NP385 -> NP384 NN
NP -> NP385 NN
NP386 -> DT NACTMP
NP -> NP386 NN
NP387 -> DT NN
NP388 -> NP387 NN
NP -> NP388 NPR
NP389 -> DT NN
NP390 -> NP389 QP
NP -> NP390 NN
NP391 -> DT NN
NP -> NP391 SBAR
NP392 -> DT NNS
NP -> NP392 NNS
NP393 -> DT NNS
NP -> NP393 SBAR
NP394 -> DT NPR
NP395 -> NP394 JJ
NP -> NP395 NN
NP396 -> DT NPR
NP397 -> NP396 JJ
NP398 -> NP397 NN
NP399 -> NP398 NN
NP -> NP399 NN
NP400 -> DT NPR
NP401 -> NP400 JJ
NP -> NP401 NNS
NP402 -> DT NPR
NP -> NP402 NP
NP403 -> DT NPR
NP404 -> NP403 QP
NP -> NP404 NN
NP405 -> DT NPR
NP406 -> NP405 QP
NP -> NP406 NPR
NP407 -> DT NPR
NP408 -> NP407 VBG
NP -> NP408 NN
NP409 -> DT NPdollar
NP -> NP409 NN
NP410 -> DT PUNCbquotebquote
NP411 -> NP410 JJ
NP -> NP411 NN
NP412 -> DT PUNCbquotebquote
NP413 -> NP412 JJ
NP414 -> NP413 NN
NP -> NP414 PUNCquotequote
NP415 -> DT PUNCbquotebquote
NP416 -> NP415 NN
NP417 -> NP416 NN
NP -> NP417 PUNCquotequote
NP418 -> DT PUNCbquotebquote
NP419 -> NP418 NN
NP -> NP419 PUNCquotequote
NP420 -> DT QP
NP421 -> NP420 JJ
NP -> NP421 NN
NP422 -> DT QP
NP423 -> NP422 JJ
NP -> NP423 NNS
NP424 -> DT QP
NP425 -> NP424 NN
NP -> NP425 NNS
NP426 -> DT QP
NP -> NP426 NPR
NP427 -> DT QP
NP -> NP427 NPRS
NP428 -> DT RB
NP429 -> NP428 JJ
NP -> NP429 NN
NP430 -> DT RB
NP431 -> NP430 JJ
NP432 -> NP431 NN
NP -> NP432 NN
NP433 -> DT RBS
NP434 -> NP433 JJ
NP -> NP434 NNS
NP435 -> DT VBG
NP -> NP435 NNS
NP436 -> DT VBG
NP -> NP436 NPR
NP437 -> DT VBN
NP438 -> NP437 JJ
NP -> NP438 NN
NP439 -> DT VBN
NP -> NP439 NNS
NP440 -> DT VBN
NP -> NP440 NPR
NP441 -> DT VBN
NP442 -> NP441 NPR
NP -> NP442 NP
NP443 -> DT VBN
NP -> NP443 QP
NP444 -> DT VBN
NP -> NP444 QPMONEY
NP446 -> NP445 JJ
NP -> NP446 NN
NP447 -> JJ JJ
NP448 -> NP447 JJ
NP -> NP448 NN
NP449 -> JJ JJ
NP450 -> NP449 NN
NP -> NP450 NNS
NP451 -> JJ JJ
NP -> NP451 NNS
NP452 -> JJ NN
NP453 -> NP452 NN
NP -> NP453 NNS
NP454 -> JJ NN
NP -> NP454 NPR
NP455 -> JJ NNS
NP -> NP455 NN
NP456 -> JJ NNS
NP -> NP456 SBAR
NP457 -> JJ NPR
NP -> NP457 NP
NP458 -> JJ VBG
NP -> NP458 NNS
NP459 -> JJ VBN
NP -> NP459 NNS
NP460 -> JJS NN
NP -> NP460 NNS
NP461 -> NN JJ
NP -> NP461 NN
NP462 -> NN JJ
NP -> NP462 NNS
NP463 -> NN NN
NP -> NP463 NN
NP464 -> NN NN
NP465 -> NP464 NN
NP -> NP465 NNS
NP466 -> NN NNS
NP -> NP466 NN
NP467 -> NN NNS
NP -> NP467 PUNCcolon
NP468 -> NN VBN
NP -> NP468 NNS
NP469 -> NNS QP
NP -> NP469 PUNCpoint
NP470 -> NP ADJP
NP -> NP471 PP
NP472 -> NP ADJP
NP -> NP473 VP
NP474 -> NP ADVPTMP
NP -> NP474 PP
NP476 -> NP475 ADJP
NP478 -> NP477 ADJP
NP -> NP479 S
NP -> NP480 ADVP
NP482 -> NP481 ADVP
NP -> NP483 ADVPLOC
NP485 -> NP484 ADVPTMP
NP -> NP485 NP
NP -> NP486 NP
NP488 -> NP487 NP
NP490 -> NP489 NP
NP -> NP491 PUNCquotequote
NP493 -> NP492 NP
NP -> NP493 PUNCpoint
NP495 -> NP494 NP
NP -> NP495 SBAR
NP -> NP496 NPLOC
NP498 -> NP497 PP
NP500 -> NP499 PP
NP -> NP500 PUNCpoint
NP -> NP501 PPLOC
NP503 -> NP502 PPLOC
NP505 -> NP504 PUNCbquotebquote
NP -> NP505 S
NP -> NP506 RRC
NP -> NP507 SBAR
NP509 -> NP508 SBAR
NP -> NP510 VP
NP511 -> NP NP
NP -> NP512 ADVP
NP513 -> NP NP
NP -> NP513 PUNCpoint
NP514 -> NP NPLOC
NP -> NP514 PUNCpoint
NP515 -> NP NPTMP
NP516 -> NP515 PP
NP -> NP516 PP
NP517 -> NP NPTMP
NP -> NP517 SBAR
NP518 -> NP PP
NP -> NP518 ADJP
NP519 -> NP PP
NP -> NP520 ADVP
NP521 -> NP PP
NP -> NP522 NP
NP523 -> NP PP
NP -> NP524 PPLOC
NP525 -> NP PP
NP -> NP526 VP
NP527 -> NP PP
NP529 -> NP528 VP
NP530 -> NP PP
NP -> NP530 NPADV
NP531 -> NP PP
NP -> NP531 PP
NP532 -> NP PP
NP533 -> NP532 PP
NP -> NP533 PP
NP534 -> NP PP
NP535 -> NP534 PPLOC
NP -> NP535 PUNCpoint
NP536 -> NP PP
NP537 -> NP536 PPTMP
NP -> NP537 PP
NP538 -> NP PP
NP539 -> NP538 PPTMP
NP -> NP539 PPTMP
NP540 -> NP PP
NP -> NP540 PRN
NP541 -> NP PP
NP -> NP541 PUNCquotequote
NP542 -> NP PP
NP -> NP542 S
NP543 -> NP PP
NP -> NP543 SBAR
NP544 -> NP PP
NP -> NP544 VP
NP545 -> NP PPLOC
NP -> NP546 SBAR
NP547 -> NP PPLOC
NP548 -> NP547 PP
NP -> NP548 PP
NP549 -> NP PPLOC
NP -> NP549 SBAR
NP550 -> NP PPLOC
NP -> NP550 VP
NP551 -> NP PPTMP
NP -> NP551 SBAR
NP552 -> NP PRN
NP -> NP553 SBAR
NP555 -> NP554 PP
NP -> NP555 PUNCRRB
NP556 -> NP PUNCbquotebquote
NP -> NP556 NP
NP557 -> NP PUNCbquotebquote
NP558 -> NP557 NPR
NP -> NP558 PUNCquotequote
NP559 -> NP PUNCbquotebquote
NP -> NP559 SBAR
NP560 -> NP PUNCcolon
NP561 -> NP560 NP
NP562 -> NP561 PUNCcolon
NP -> NP562 NP
NP563 -> NP PUNCcolon
NP564 -> NP563 NP
NP565 -> NP564 PUNCcolon
NP566 -> NP565 NP
NP567 -> NP566 PUNCcolon
NP568 -> NP567 NP
NP569 -> NP568 PUNCcolon
NP -> NP569 NP
NP570 -> NP PUNCcolon
NP571 -> NP570 NP
NP572 -> NP571 PUNCcolon
NP573 -> NP572 NP
NP574 -> NP573 PUNCcolon
NP575 -> NP574 NP
NP576 -> NP575 PUNCcolon
NP577 -> NP576 NP
NP578 -> NP577 PUNCcolon
NP -> NP578 NP
NP579 -> NP PUNCcolon
NP580 -> NP579 NP
NP581 -> NP580 PUNCcolon
NP582 -> NP581 NP
NP583 -> NP582 PUNCcolon
NP584 -> NP583 NP
NP585 -> NP584 PUNCcolon
NP586 -> NP585 NP
NP587 -> NP586 PUNCcolon
NP588 -> NP587 NP
NP589 -> NP588 PUNCcolon
NP -> NP589 NP
NP590 -> NP PUNCcolon
NP591 -> NP590 RB
NP592 -> NP591 NP
NP -> NP592 PUNCpoint
NP593 -> NP PUNCcolon
NP -> NP593 S
NP594 -> NP PUNCcolon
NP -> NP594 SBAR
NP595 -> NP QP
NP -> NP595 PUNCpoint
NP596 -> NP SBAR
NP -> NP596 SBAR
NP597 -> NP VP
NP -> NP597 PUNCcolon
NP598 -> NPR FW
NP -> NP598 NPR
NP599 -> NPR JJ
NP -> NP599 NN
NP600 -> NPR JJ
NP601 -> NP600 NN
NP602 -> NP601 NN
NP -> NP602 NPR
NP603 -> NPR PUNCquotequote
NP -> NP603 NPR
NP604 -> NPR QP
NP -> NP605 QP
NP606 -> NPRS NP
NP -> NP606 NPR
NP607 -> NPdollar ADJP
NP608 -> NP607 JJ
NP -> NP608 NN
NP609 -> NPdollar ADJP
NP610 -> NP609 NN
NP -> NP610 NN
NP611 -> NPdollar JJ
NP612 -> NP611 JJ
NP -> NP612 NN
NP613 -> NPdollar JJ
NP614 -> NP613 JJ
NP615 -> NP614 NN
NP -> NP615 NN
NP616 -> NPdollar JJ
NP -> NP616 NNS
NP617 -> NPdollar JJ
NP -> NP617 NPR
NP618 -> NPdollar JJ
NP619 -> NP618 NPR
NP -> NP619 NP
NP620 -> NPdollar JJR
NP -> NP620 NN
NP621 -> NPdollar JJS
NP622 -> NP621 NN
NP -> NP622 NNS
NP623 -> NPdollar NN
NP624 -> NP623 JJ
NP -> NP624 NN
NP625 -> NPdollar NN
NP626 -> NP625 NN
NP -> NP626 NNS
NP627 -> NPdollar NN
NP -> NP627 NNS
NP628 -> NPdollar NN
NP -> NP628 SBAR
NP629 -> NPdollar NNS
NP -> NP629 NN
NP630 -> NPdollar NNS
NP -> NP630 NNS
NP631 -> NPdollar NNS
NP -> NP631 SBAR
NP632 -> NPdollar NPR
NP -> NP632 NP
NP633 -> NPdollar NPRS
NP -> NP633 NP
NP634 -> NPdollar PUNCbquotebquote
NP635 -> NP634 NX
NP -> NP635 PUNCquotequote
NP636 -> NPdollar QP
NP -> NP636 NN
NP637 -> NPdollar QP
NP638 -> NP637 NN
NP -> NP638 NNS
NP639 -> NPdollar QP
NP -> NP639 NNS
NP640 -> NPdollar VBN
NP -> NP640 NN
NP641 -> PDT DT
NP642 -> NP641 JJ
NP -> NP642 NN
NP643 -> PDT DT
NP644 -> NP643 JJ
NP -> NP644 NNS
NP645 -> PDT DT
NP -> NP645 NN
NP646 -> PDT DT
NP647 -> NP646 NN
NP -> NP647 NNS
NP648 -> PDT DT
NP -> NP648 NNS
NP649 -> PRPdollar ADJP
NP650 -> NP649 NN
NP -> NP650 NN
NP651 -> PRPdollar JJ
NP652 -> NP651 JJ
NP -> NP652 NN
NP653 -> PRPdollar JJ
NP654 -> NP653 JJ
NP -> NP654 NNS
NP655 -> PRPdollar NN
NP -> NP655 NN
NP656 -> PRPdollar NN
NP657 -> NP656 NN
NP -> NP657 NN
NP658 -> PRPdollar NN
NP -> NP658 S
NP659 -> PRPdollar NN
NP -> NP659 SBAR
NP660 -> PRPdollar NNS
NP -> NP660 NNS
NP661 -> PRPdollar NPR
NP -> NP661 NP
NP662 -> PRPdollar NPR
NP663 -> NP662 QP
NP -> NP663 NN
NP664 -> PRPdollar QP
NP665 -> NP664 JJ
NP -> NP665 NNS
NP666 -> PRPdollar QP
NP667 -> NP666 NN
NP -> NP667 NNS
NP668 -> PRPdollar VBG
NP -> NP668 NN
NP669 -> PRPdollar VBG
NP -> NP669 NNS
NP670 -> PUNCbquotebquote JJ
NP671 -> NP670 PUNCquotequote
NP -> NP671 NNS
NP672 -> PUNCbquotebquote NPR
NP673 -> NP672 PUNCquotequote
NP -> NP673 PRN
NP674 -> PUNCcolon NN
NP675 -> NP674 NN
NP676 -> NP675 NN
NP -> NP676 PUNCpoint
NP677 -> QP JJ
NP678 -> NP677 JJ
NP -> NP678 NNS
NP679 -> QP JJ
NP -> NP679 NN
NP680 -> QP JJ
NP -> NP680 NNS
NP681 -> QP JJR
NP -> NP681 NNS
NP682 -> QP NN
NP -> NP682 NN
NP683 -> QP NN
NP684 -> NP683 NN
NP -> NP684 NNS
NP685 -> QP NN
NP -> NP685 NNS
NP686 -> QP NNS
NP -> NP686 NNS
NP687 -> QP RB
NP -> NP687 PUNCpoint
NP688 -> RB DT
NP689 -> NP688 ADJP
NP -> NP689 NN
NP690 -> RB DT
NP691 -> NP690 JJ
NP -> NP691 NN
NP692 -> RB DT
NP -> NP692 NPR
NP693 -> RB JJ
NP -> NP693 NN
NP694 -> RB NN
NP -> NP694 NNS
NP695 -> RB QP
NP -> NP695 NNS
NP696 -> SBARNOM PUNCcolon
NP -> NP696 NP
NP697 -> VBG JJ
NP -> NP697 NNS
NP698 -> VBG NN
NP -> NP698 NNS
ADVPPRD699 -> RB NP
ADVPPRD -> ADVPPRD699 PP
SBARADV -> SBARADV700 S
PPTMP701 -> ADVP IN
PPTMP -> PPTMP701 SNOM
PPTMP702 -> NP IN
PPTMP -> PPTMP702 NP
PPTMP703 -> RB IN
PPTMP -> PPTMP703 NP
SQ704 -> MD NP
SQ -> SQ704 VP
SQ705 -> VBP NP
SQ706 -> SQ705 VP
SQ -> SQ706 PUNCpoint
SINV707 -> ADJPPRD VP
SINV708 -> SINV707 NP
SINV -> SINV708 PUNCpoint
SINV709 -> ADVP VP
SINV710 -> SINV709 VP
SINV711 -> SINV710 NP
SINV -> SINV711 PUNCpoint
SINV712 -> ADVPLOCPRD VP
SINV713 -> SINV712 NP
SINV -> SINV713 PUNCcolon
SINV714 -> PPLOC VP
SINV715 -> SINV714 NP
SINV -> SINV715 PUNCpoint
SINV716 -> PPLOCPRD VP
SINV717 -> SINV716 NP
SINV -> SINV717 PUNCpoint
SINV718 -> PPPRD VP
SINV719 -> SINV718 NP
SINV -> SINV719 PUNCpoint
SINV720 -> PUNCbquotebquote S
SINV722 -> SINV721 PUNCquotequote
SINV723 -> SINV722 VP
SINV724 -> SINV723 NP
SINV -> SINV724 PUNCpoint
SINV725 -> PUNCbquotebquote STPC
SINV727 -> SINV726 PUNCquotequote
SINV728 -> SINV727 VP
SINV729 -> SINV728 NP
SINV731 -> SINV730 SADV
SINV -> SINV731 PUNCpoint
SINV732 -> PUNCbquotebquote STPC
SINV734 -> SINV733 PUNCquotequote
SINV735 -> SINV734 VP
SINV736 -> SINV735 NP
SINV -> SINV736 PUNCpoint
SINV737 -> STPC VP
SINV738 -> SINV737 NP
SINV -> SINV738 PUNCpoint
ADJP -> ADJP739 JJ
ADJP740 -> QP JJ
ADJP -> ADJP740 NN
ADJP741 -> RB RB
ADJP -> ADJP741 JJ
ADJP742 -> RBR JJ
ADJP -> ADJP742 PP
ADJPPRD -> ADJPPRD743 ADJP
ADJPPRD744 -> JJ NPTMP
ADJPPRD -> ADJPPRD744 PP
ADJPPRD745 -> JJ RB
ADJPPRD -> ADJPPRD745 S
ADJPPRD746 -> PUNCbquotebquote JJ
ADJPPRD747 -> ADJPPRD746 PUNCquotequote
ADJPPRD -> ADJPPRD747 PP
ADJPPRD748 -> RB RBR
ADJPPRD -> ADJPPRD748 JJ
ADJPPRD749 -> RBR JJ
ADJPPRD -> ADJPPRD749 S
NACLOC -> NACLOC750 NPR
NPPRD751 -> DT ADJP
NPPRD -> NPPRD751 NN
NPPRD752 -> DT JJ
NPPRD -> NPPRD752 QP
NPPRD753 -> DT NN
NPPRD754 -> NPPRD753 NN
NPPRD -> NPPRD754 NN
NPPRD755 -> DT PUNCbquotebquote
NPPRD756 -> NPPRD755 JJ
NPPRD757 -> NPPRD756 NN
NPPRD -> NPPRD757 PUNCquotequote
NPPRD758 -> DT PUNCbquotebquote
NPPRD759 -> NPPRD758 JJ
NPPRD760 -> NPPRD759 PUNCquotequote
NPPRD -> NPPRD760 NN
NPPRD761 -> DT VBG
NPPRD -> NPPRD761 NN
NPPRD762 -> JJ NN
NPPRD -> NPPRD762 NNS
NPPRD -> NPPRD763 ADVP
NPPRD -> NPPRD764 NP
NPPRD765 -> NP PP
NPPRD -> NPPRD766 SBAR
NPPRD767 -> NP PP
NPPRD -> NPPRD767 PPTMP
NPPRD768 -> NP PP
NPPRD -> NPPRD768 S
NPPRD769 -> NP PP
NPPRD -> NPPRD769 SBAR
NPPRD770 -> NP PPLOC
NPPRD -> NPPRD770 SBAR
NPPRD771 -> NPdollar JJS
NPPRD772 -> NPPRD771 NN
NPPRD -> NPPRD772 NN
NPPRD773 -> QP JJ
NPPRD -> NPPRD773 NNS
NPPRD774 -> RB DT
NPPRD775 -> NPPRD774 JJ
NPPRD -> NPPRD775 NN
NPPRD776 -> RB DT
NPPRD -> NPPRD776 NN
NPLOC778 -> NPLOC777 NP
NPLOC780 -> NPLOC779 NP
NPLOC -> NPLOC780 PUNCpoint
VP781 -> ADVP VB
VP782 -> VP781 NP
VP -> VP782 PP
VP783 -> ADVP VB
VP -> VP783 S
VP784 -> ADVP VBG
VP -> VP784 PP
VP785 -> ADVP VBG
VP -> VP785 S
VP786 -> ADVP VBP
VP -> VP786 SBAR
VP787 -> ADVPTMP VBG
VP -> VP787 NP
VP788 -> ADVPTMP VBG
VP -> VP788 VP
VP789 -> MD RB
VP790 -> VP789 ADVPTMP
VP -> VP790 VP
VP791 -> PUNCbquotebquote VB
VP792 -> VP791 PUNCquotequote
VP -> VP792 NP
VP793 -> VB ADJPPRD
VP -> VP793 NPTMP
VP794 -> VB ADJPPRD
VP -> VP794 PP
VP795 -> VB ADJPPRD
VP -> VP795 PPLOC
VP796 -> VB ADJPPRD
VP -> VP796 S
VP797 -> VB ADJPPRD
VP -> VP797 SBARADV
VP798 -> VB ADJPPRD
VP -> VP798 SBARPRP
VP799 -> VB ADVP
VP -> VP799 NP
VP800 -> VB ADVP
VP -> VP800 PP
VP801 -> VB ADVP
VP -> VP801 PPTMP
VP802 -> VB ADVPTMP
VP -> VP802 PP
VP803 -> VB NP
VP -> VP803 ADVPLOC
VP804 -> VB NP
VP -> VP805 ADVP
VP806 -> VB NP
VP807 -> VP806 NP
VP -> VP807 PP
VP808 -> VB NP
VP809 -> VP808 NP
VP -> VP809 PPTMP
VP810 -> VB NP
VP -> VP810 NPTMP
VP811 -> VB NP
VP812 -> VP811 PP
VP -> VP813 SADV
VP814 -> VB NP
VP815 -> VP814 PP
VP -> VP816 SBARADV
VP817 -> VB NP
VP818 -> VP817 PP
VP -> VP818 PPLOC
VP819 -> VB NP
VP820 -> VP819 PP
VP -> VP820 SBARPRP
VP821 -> VB NP
VP822 -> VP821 PP
VP -> VP822 SPRP
VP823 -> VB NP
VP -> VP823 PPLOC
VP824 -> VB NP
VP825 -> VP824 PPLOC
VP -> VP825 PPTMP
VP826 -> VB NP
VP -> VP826 PPTMP
VP827 -> VB NP
VP828 -> VB NP
VP -> VP828 SBARPRP
VP829 -> VB NP
VP -> VP829 SBARTMP
VP830 -> VB NP
VP -> VP830 VP
VP831 -> VB NPPRD
VP -> VP831 PP
VP832 -> VB NPPRD
VP -> VP832 PPTMP
VP833 -> VB NPTMP
VP -> VP833 NP
VP834 -> VB PP
VP -> VP835 ADVP
VP836 -> VB PP
VP -> VP836 SBAR
VP837 -> VB PP
VP -> VP837 SBARPRP
VP838 -> VB PP
VP -> VP838 SBARTMP
VP839 -> VB PPLOC
VP -> VP839 SBARTMP
VP840 -> VB PPTMP
VP -> VP840 PP
VP842 -> VP841 NP
VP -> VP842 PP
VP844 -> VP843 NP
VP -> VP844 PPTMP
VP845 -> VB PUNCbquotebquote
VP -> VP845 ADJPPRD
VP846 -> VB PUNCbquotebquote
VP -> VP846 NP
VP847 -> VB PUNCquotequote
VP -> VP847 NP
VP848 -> VB S
VP -> VP849 SBARADV
VP850 -> VB S
VP -> VP850 SBARPRP
VP851 -> VB S
VP -> VP851 SBARTMP
VP852 -> VBD ADJPPRD
VP -> VP852 PPLOC
VP853 -> VBD ADJPPRD
VP -> VP853 PPTMP
VP854 -> VBD ADJPPRD
VP -> VP854 SBARADV
VP855 -> VBD ADVP
VP -> VP855 NPTMP
VP856 -> VBD ADVP
VP -> VP856 PP
VP857 -> VBD ADVP
VP858 -> VP857 PP
VP -> VP859 SADV
VP860 -> VBD ADVP
VP -> VP860 PPTMP
VP861 -> VBD ADVP
VP -> VP861 SBAR
VP862 -> VBD ADVP
VP -> VP862 VP
VP863 -> VBD ADVPTMP
VP -> VP863 ADJPPRD
VP864 -> VBD ADVPTMP
VP -> VP864 VP
VP -> VP865 S
VP -> VP866 SADV
VP867 -> VBD NP
VP -> VP867 ADVP
VP868 -> VBD NP
VP869 -> VP868 ADVP
VP -> VP869 PP
VP870 -> VBD NP
VP871 -> VP870 ADVPTMP
VP -> VP871 PP
VP872 -> VBD NP
VP -> VP873 ADVP
VP874 -> VBD NP
VP -> VP875 PP
VP876 -> VBD NP
VP878 -> VP877 PP
VP -> VP879 PP
VP880 -> VBD NP
VP -> VP881 SADV
VP882 -> VBD NP
VP -> VP883 SBARADV
VP884 -> VBD NP
VP -> VP884 NP
VP885 -> VBD NP
VP886 -> VP885 NP
VP -> VP886 PPTMP
VP887 -> VBD NP
VP888 -> VP887 NPTMP
VP -> VP889 PP
VP890 -> VBD NP
VP891 -> VP890 NPTMP
VP -> VP891 PPLOC
VP892 -> VBD NP
VP893 -> VP892 NPTMP
VP -> VP893 SBAR
VP894 -> VBD NP
VP895 -> VP894 NPTMP
VP -> VP895 SBARTMP
VP896 -> VBD NP
VP -> VP896 PP
VP897 -> VBD NP
VP898 -> VP897 PP
VP -> VP899 PP
VP900 -> VBD NP
VP901 -> VP900 PP
VP -> VP902 SBARADV
VP903 -> VBD NP
VP904 -> VP903 PP
VP -> VP904 PP
VP905 -> VBD NP
VP906 -> VP905 PP
VP907 -> VP906 PP
VP -> VP908 SADV
VP909 -> VBD NP
VP910 -> VP909 PP
VP -> VP910 PPTMP
VP911 -> VBD NP
VP912 -> VP911 PP
VP -> VP912 S
VP913 -> VBD NP
VP914 -> VP913 PP
VP -> VP914 SADV
VP915 -> VBD NP
VP916 -> VP915 PP
VP -> VP916 SBARADV
VP917 -> VBD NP
VP918 -> VP917 PPLOC
VP -> VP919 PP
VP920 -> VBD NP
VP921 -> VP920 PPLOC
VP -> VP921 NPTMP
VP922 -> VBD NP
VP923 -> VP922 PPTMP
VP -> VP924 PP
VP925 -> VBD NP
VP926 -> VP925 PPTMP
VP -> VP926 PPTMP
VP927 -> VBD NP
VP928 -> VP927 PPTMP
VP -> VP928 SBAR
VP929 -> VBD NP
VP -> VP929 S
VP930 -> VBD NP
VP -> VP930 SBARPRP
VP931 -> VBD NP
VP -> VP931 SBARTMP
VP932 -> VBD NP
VP -> VP932 SPRP
VP933 -> VBD NPADV
VP -> VP933 PP
VP934 -> VBD NPPRD
VP -> VP935 PP
VP936 -> VBD NPPRD
VP -> VP937 SBARADV
VP938 -> VBD NPPRD
VP -> VP938 PP
VP939 -> VBD NPPRD
VP -> VP939 PPLOC
VP940 -> VBD NPTMP
VP941 -> VP940 PP
VP -> VP942 ADVP
VP943 -> VBD NPTMP
VP -> VP943 S
VP944 -> VBD PP
VP -> VP944 ADVPTMP
VP945 -> VBD PP
VP -> VP946 ADVP
VP947 -> VBD PP
VP -> VP948 SBARADV
VP949 -> VBD PP
VP -> VP949 NP
VP950 -> VBD PP
VP951 -> VP950 NPTMP
VP -> VP951 PP
VP952 -> VBD PP
VP -> VP952 PP
VP953 -> VBD PP
VP954 -> VP953 PP
VP -> VP955 ADVP
VP956 -> VBD PP
VP957 -> VP956 PP
VP -> VP958 PP
VP959 -> VBD PP
VP -> VP959 PPLOC
VP960 -> VBD PP
VP -> VP960 PPTMP
VP961 -> VBD PP
VP962 -> VP961 PPTMP
VP -> VP962 PP
VP963 -> VBD PP
VP -> VP963 SBARPRP
VP964 -> VBD PP
VP -> VP964 SBARTMP
VP965 -> VBD PPLOC
VP -> VP966 ADVP
VP967 -> VBD PPLOC
VP -> VP967 PPTMP
VP968 -> VBD PPLOC
VP -> VP968 SPRP
VP969 -> VBD PPLOCPRD
VP -> VP969 SBARTMP
VP970 -> VBD PPTMP
VP -> VP970 PP
VP971 -> VBD PPTMP
VP -> VP971 SBAR
VP973 -> VP972 NP
VP -> VP973 PPTMP
VP -> VP974 S
VP975 -> VBD PUNCbquotebquote
VP -> VP975 S
VP976 -> VBD PUNCcolon
VP977 -> VP976 PUNCbquotebquote
VP -> VP977 S
VP978 -> VBD RB
VP979 -> VP978 ADVP
VP -> VP979 VP
VP980 -> VBD S
VP -> VP981 SBARADV
VP982 -> VBD S
VP -> VP982 NPTMP
VP983 -> VBD S
VP -> VP983 PPLOC
VP984 -> VBD SBAR
VP -> VP985 SADV
VP986 -> VBG ADVP
VP -> VP986 PPTMP
VP988 -> VP987 PUNCbquotebquote
VP -> VP988 S
VP989 -> VBG NP
VP -> VP990 PP
VP991 -> VBG NP
VP -> VP991 NP
VP992 -> VBG NP
VP993 -> VP992 PPTMP
VP -> VP993 PP
VP994 -> VBG NP
VP995 -> VBG NP
VP -> VP995 SBAR
VP996 -> VBG NP
VP -> VP996 SBARADV
VP997 -> VBG NP
VP -> VP997 SPRP
VP998 -> VBG PP
VP -> VP998 ADVPTMP
VP999 -> VBG PP
VP -> VP999 NPTMP
VP1000 -> VBG PP
VP -> VP1000 SBAR
VP1001 -> VBG PP
VP -> VP1001 SPRP
VP1002 -> VBG PPTMP
VP -> VP1002 SBAR
VP1003 -> VBG PUNCcolon
VP1004 -> VP1003 PUNCbquotebquote
VP -> VP1004 S
VP1005 -> VBG S
VP -> VP1005 PPTMP
VP1006 -> VBN ADJPPRD
VP -> VP1007 SADV
VP1008 -> VBN ADJPPRD
VP -> VP1008 SBARTMP
VP1009 -> VBN ADVP
VP -> VP1009 NPTMP
VP1010 -> VBN ADVP
VP -> VP1010 PPLOC
VP1011 -> VBN ADVP
VP -> VP1011 PPTMP
VP1012 -> VBN ADVP
VP -> VP1012 VP
VP -> VP1013 PP
VP1014 -> VBN NP
VP -> VP1014 ADVP
VP1015 -> VBN NP
VP -> VP1015 ADVPTMP
VP1016 -> VBN NP
VP -> VP1017 PP
VP1018 -> VBN NP
VP -> VP1018 NPTMP
VP1019 -> VBN NP
VP1020 -> VP1019 PP
VP -> VP1020 PPTMP
VP1021 -> VBN NP
VP -> VP1021 PPTMP
VP1022 -> VBN NP
VP1023 -> VP1022 PPTMP
VP -> VP1024 PP
VP1025 -> VBN NP
VP -> VP1025 S
VP1026 -> VBN NP
VP -> VP1026 SBARADV
VP1027 -> VBN NP
VP -> VP1027 SPRP
VP1028 -> VBN NPPRD
VP -> VP1028 PP
VP1029 -> VBN PP
VP -> VP1029 ADVPTMP
VP1030 -> VBN PP
VP -> VP1030 NPTMP
VP1031 -> VBN PP
VP -> VP1031 PP
VP1032 -> VBN PP
VP1033 -> VP1032 PP
VP -> VP1033 PP
VP1034 -> VBN PP
VP -> VP1034 PPLOC
VP1035 -> VBN PP
VP -> VP1035 PPTMP
VP1036 -> VBN PP
VP1037 -> VP1036 PPTMP
VP -> VP1037 PP
VP1038 -> VBN PP
VP -> VP1038 S
VP1039 -> VBN PPLOC
VP -> VP1040 SADV
VP1041 -> VBN PPLOC
VP -> VP1041 NPTMP
VP1042 -> VBN PPLOC
VP -> VP1042 PP
VP1043 -> VBN PPLOC
VP -> VP1043 PPLOC
VP1044 -> VBN PPLOC
VP -> VP1044 PPTMP
VP1045 -> VBN PPLOCPRD
VP -> VP1045 PPTMP
VP1046 -> VBN PPTMP
VP -> VP1046 PPLOC
VP1047 -> VBN PPTMP
VP -> VP1047 S
VP1048 -> VBN PPTMP
VP -> VP1048 SPRP
VP -> VP1049 PPTMP
VP1050 -> VBN S
VP -> VP1051 PP
VP1052 -> VBN S
VP -> VP1053 SADV
VP1054 -> VBN S
VP -> VP1054 PPLOC
VP1055 -> VBN S
VP -> VP1055 SBARADV
VP1056 -> VBN S
VP -> VP1056 SBARTMP
VP1057 -> VBP ADVP
VP -> VP1057 NP
VP1058 -> VBP ADVPTMP
VP -> VP1058 ADJPPRD
VP1059 -> VBP ADVPTMP
VP -> VP1059 VP
VP1060 -> VBP DT
VP -> VP1060 VP
VP1061 -> VBP NP
VP -> VP1062 SADV
VP1063 -> VBP NP
VP -> VP1063 NPTMP
VP1064 -> VBP NP
VP1065 -> VP1064 PP
VP -> VP1065 PP
VP1066 -> VBP NP
VP -> VP1066 PPLOC
VP1067 -> VBP NP
VP -> VP1067 SPRP
VP -> VP1068 NP
VP -> VP1069 PP
VP1070 -> VBP RB
VP -> VP1070 ADJPPRD
VP1071 -> VBP RB
VP1072 -> VP1071 ADVPTMP
VP -> VP1072 VP
VP1073 -> VBZ ADJPPRD
VP -> VP1073 PP
VP1074 -> VBZ ADJPPRD
VP -> VP1074 SBAR
VP1075 -> VBZ ADJPPRD
VP -> VP1075 SBARPRP
VP1076 -> VBZ ADVP
VP -> VP1076 NP
VP1077 -> VBZ ADVP
VP -> VP1077 NPPRD
VP1078 -> VBZ ADVP
VP -> VP1078 PPPRD
VP1079 -> VBZ ADVP
VP -> VP1079 VP
VP1080 -> VBZ ADVPTMP
VP -> VP1080 S
VP -> VP1081 SADV
VP1082 -> VBZ NP
VP -> VP1082 ADVP
VP1083 -> VBZ NP
VP -> VP1083 ADVPTMP
VP1084 -> VBZ NP
VP -> VP1084 SBAR
VP1085 -> VBZ NP
VP -> VP1085 SBARADV
VP1086 -> VBZ NPPRD
VP -> VP1086 PP
VP1087 -> VBZ NPPRD
VP -> VP1087 PPTMP
VP1088 -> VBZ NPPRD
VP -> VP1088 SBARTMP
VP1089 -> VBZ PP
VP -> VP1089 PPLOC
VP -> VP1090 NP
VP -> VP1091 SBAR
VP1092 -> VBZ PUNCbquotebquote
VP -> VP1092 ADJPPRD
VP1093 -> VBZ PUNCbquotebquote
VP -> VP1093 NP
VP1094 -> VBZ PUNCbquotebquote
VP -> VP1094 NPPRD
VP1095 -> VBZ PUNCbquotebquote
VP -> VP1095 VP
VP1096 -> VBZ RB
VP1097 -> VP1096 ADVPTMP
VP -> VP1097 VP
VP1098 -> VBZ RB
VP -> VP1098 NPPRD
VP1099 -> VBZ RB
VP -> VP1099 PPPRD
VP1100 -> VBZ RB
VP -> VP1100 VP
VP1101 -> VBZ S
VP -> VP1102 SBARADV
VP1103 -> VBZ S
VP -> VP1103 PP
VP -> VP1104 NP
VP -> VP1105 NPADV
VP1107 -> VP1106 RB
VP -> VP1107 VP
VP -> VP1108 SBARADV
VP -> VP1109 VP
QP1110 -> IN TO
QP -> QP1110 QP
QP1111 -> QP NN
QP -> QP1111 PP
QP1112 -> RB JJR
QP1113 -> QP1112 IN
QP -> QP1113 QP
QP1114 -> RB RB
QP1115 -> QP1114 IN
QP -> QP1115 QP
QP1116 -> RB RB
QP -> QP1116 QP
QP1117 -> RBR IN
QP -> QP1117 QP
PPLOC1118 -> IN NP
PPLOC -> PPLOC1118 PUNCcolon
PPLOC1119 -> NPADV IN
PPLOC -> PPLOC1119 NP
SBARPRP1120 -> IN IN
SBARPRP -> SBARPRP1120 S
SBARPRP1121 -> IN NN
SBARPRP -> SBARPRP1121 S
NPTMP1122 -> ADVP DT
NPTMP -> NPTMP1122 NN
NPTMP1123 -> DT NN
NPTMP -> NPTMP1123 NN
NPTMP1124 -> JJ NPR
NPTMP -> NPTMP1124 QP
NPTMP -> NPTMP1125 SBAR
NPTMP1126 -> NPR QP
NPTMP -> NPTMP1127 QP
NPTMP1128 -> RB JJ
NPTMP -> NPTMP1128 NN
NPTMP1129 -> RBR DT
NPTMP -> NPTMP1129 NN
''')

parser = ChartParser(grammar)

gr = parser.grammar()
print(' '.join(produce(gr, gr.start())))