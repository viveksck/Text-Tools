#!/usr/bin/env python
#Copyright 2011 Malcolm Prentice
#malc@alba-english.com
#File Chooser
'''
   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


'''
THANKS TO:
Word lists from Range embedded by permission - originals available from http://www.victoria.ac.nz/lals/staff/paul-nation.aspx
Various snippets of code came from stackoverflow (http://stackoverflow.com/), the NLTK manual and website (http://www.nltk.org/)
'''

# define filter lists - names or any other words you want excluded from analysis
filterlistunsplit = ('''Malcolm Prentice ''')

# Define and convert the word lists
base1unsplit = ('''
a an
able ability abler ablest ably abilities unable inability
about
absolute absolutely absolutist absolutists
accept acceptability acceptable acceptably unacceptable acceptance accepted accepting accepts unacceptably
account accounted accounting accounts
achieve achievable unachievable achieved achievement achievements achiever achievers achieves achieving
across
act acted acting action inaction actions actionable acts actor actors actress actresses
active actively activities activity inactive inactivity activist activists activism
actual actually actuality
add added adding addition additional additionally additive additives additions adds
address addressed addresses addressing addressee addressees
admit admission admissions admittedly admits admitted admitting admissible admissibly inadmissible admittance readmit readmitted readmitting readmits readmittance readmission admissibility admissibilities inadmissibility
advertise advertising advertises advertiser advertisers advertised advertisement advertisements advertize advertizing advertizes advertizer advertizers advertized advertizement advertizements ad ads advert adverts
affect affected affecting affects unaffected affectation affectations
afford afforded affording affords affordable unaffordable
after afterward afterwards
afternoon afternoons
again
against
age aged ages aging ageing ageism ageist ageless ager agers
agent agency agencies agents
ago
agree agreed agreeing agreement agreements agrees agreeable agreeably disagreeably disagreements disagree disagreeable disagreed disagreeing disagreement disagrees
air airy airier airiest airiness airily airless airs aired airing airings midair
all
allow allowance allowances allowed allowing allows allowable
almost
along
already
alright
also
although
always
america american americans americanise americanised americanising americanisation americanize americanized americanizing americanization
amount amounted amounting amounts
and
another
answer answered unanswered answering answers answerable unanswerable
any anybody anyhow anymore anyone anything anyway anywhere
apart
apparent apparently
appear appearance appeared appearing appears appearances reappear reappears reappeared reappearing reappearance reappearances
apply application applications applied applies applicable applying applicant applicants applicability applicator applicators
appoint appoints appointed appointing appointments appointment reappoint reappointed reappointing reappointments reappointment reappoints appointee appointees
approach approachable approached approaches approaching unapproachable
appropriate appropriacy appropriately appropriateness inappropriacy inappropriate inappropriately
area areas
argue arguing argues argued arguable arguably unarguably argument arguments
arm armed arms unarmed armful
around
arrange arranged arranging arranges arrangement arrangements
art arts artist artistic artists artistically arty
as
ask asked unasked asking asks
associate associates associated associating associative associatively associations association disassociate disassociated
assume assumed assumes assuming assumption assumptions unassuming unassumingly
at
attend attends attending attended unattended attendant attendants attendance attendances attention attentions attender attenders
authority authoritative authoritatively authoritativeness authorities
available availability unavailability unavailable
aware awareness unaware unawares
away
awful awfully
b
baby babies babyish
back backed backing backs backbone backwards backward backwardness backwardnesses
bad badly badness baddy baddies
bag bags bagging bagged baggage baggy baggier baggiest bagginess baggily
balance balancing balances balanced imbalance imbalances unbalanced unbalance unbalances unbalancing
ball balls
bank banked banker bankers banking banks interbank
bar bars barred unbarred barring
base based baseless bases basic basics basically basing
basis
be am are aren ain been is isn re s was wasn were weren being beings bein twas tis
bear bearing bearings bearable unbearable bears bore born reborn unborn borne bearer bearers unbearably bearably
beat beats beating beatings beaten unbeaten unbeatable beater beaters
beauty beautiful beautifully beauties
because cos coz
become became becomes becoming
bed bedroom bedrooms bedroomed bedding bedded beds
before
begin began beginner beginners beginning beginnings begins begun
behind
believe believed believes believing disbelief believable unbelievable unbelievably believer believers unbeliever unbelievers disbelievingly disbelieving disbelieved disbelieves disbeliever disbelievers unbelief unbelieving unbelievingly disbelieve
benefit beneficial beneficially beneficiary beneficiaries benefitted benefitting benefited benefiting benefits
best better betterment betterments
bet betting bets
between
big bigger bigness biggest biggish
bill bills billed billing
birth births birthdays birthday
bit bits
black blacker blackest blackly blacken blackened blackening blackens blackness blacks blackish blacking blacked
bloke blokes
blood bled bleed bleeding bleeds blooded bloody bloodied bloodying bloodies bloodiness bloodless bloodlessness bloodlessly
blow blew blowing blows blown blower blowers
blue blueness bluer bluest bluish bluey blues
board boarded boarding boards boarder boarders
boat boats boated boating boatman boatmen boater boaters
body bodies bodily bodied
book books booklet booklets bookish
both
bother bothered bothering bothers
bottle bottling bottles bottled unbottled
bottom bottoms bottomed bottoming bottomless
box boxes
boy boyhood boys boyish
break breaking breakage breakages breaks broke broken unbreakable outbreaks outbreak unbroken breaker breakers
brief briefed briefing briefly briefs
brilliant brilliantly
bring bringing brings brought
britain british brit brits
brother brothers brotherly bro bros
budget budgetary budgeted budgeting budgets
build builder builders building buildings builds built unbuilt rebuild rebuilding rebuilt prebuilt
bus bussing buses busses bussed
business businesses businessmen unbusinesslike businesslike businessman businesswoman businesswomen
busy busily busiest busier busied busies busying
but
buy bought buying buys buyer buyers
by
c
cake caked caking cakes
call called calling calls caller callers
can cannot
car cars
card cards
care cared uncared careful carefully careless carelessness cares caring carelessly uncaring carer carers
carry carried carrier carriers carries carrying
case cases
cat cats catlike
catch catches catching caught uncaught catcher catchers catchy
cause caused causes causing causation causative
cent cents
centre center centerist centerists centers centred centered central centralism centrally centrality centralities centres centrist centrists centralise centralises centralised centralising centralisation centralized centralize centralizes centralizing centralization
certain certainly certainty uncertain uncertainties uncertainty uncertainly
chair chairs chaired chairing
chairman chairmen
chance chanced chances chancing
change changed changes changing changeable unchanged unchangeable unchangeably unchanging changer changers
chap chaps chappie chappies
character characteristic characteristically characteristics characterize characterized characterization characterizes characterise characterised characterises characterising characterizing characters uncharacteristic uncharacteristically
charge charged uncharged charges charging charger chargers chargeable nonchargeable
cheap cheapness cheaply cheapest cheaper cheapen cheapening cheapened cheapens
check checks checking checked unchecked
child children childish childhood childless childlike
choice choices
choose chooses choosing chose chosen unchosen choosy
christ christian christians christianity christendom
christmas christmases
church churches
city cities
claim claimed claiming claims unclaimed claimant claimants
class classed classes classing classless classlessness classy classier classiest classiness subclass subclasses
clean cleaned cleaner cleaners cleanest cleaning cleanly cleans cleanness cleanliness unclean uncleanliness
clear cleared clearer clearest clearing clearings clearly clearness clears unclear clearance clearances
client clients
clock clocks clocked clocking clocker clockers oclock
close closely closeness closer closest
closes closed unclosed closing
clothe clothes clothed clothing unclothe unclothes unclothed unclothing clothier clothiers
club clubbed clubbing clubs
coffee coffees
cold colder coldest coldly coldness colds coldish
colleague colleagues
collect collects collecting collected uncollected collective collectively collector collectors collection collections collectable collectables collectivist collectivists collectivism collectivity
college colleges collegiate
colour color colored colorful colorfully coloring colorless colors coloured colourful colourfully colouring colourless colours coloration colouration
come came comes coming comings comer comers
comment commentaries commentary commented commenting comments
commit commitment commitments commits committed uncommitted
committee committees subcommittee subcommittees committing committal committals
common commoner commoners commonest commonly commonness commons uncommon uncommonly
community communities
company companies co
compare comparable comparably comparability incomparable compared compares comparative comparison comparisons comparing comparatively
complete completed uncompleted completely completion completions completes completeness completing incomplete incompletely
compute computation computational computationally computations computable computer computed computerize computerise computerising computerizing computerises computerizes computerised computerized computerisation computerization computers computing
concern concerned concerning concerns unconcerned
condition conditional conditionally unconditionally conditions unconditional conditioned conditioning conditioner conditioners unconditioned conditionings
confer conference conferences conferencing conferred conferring confers
consider consideration considerations considered unconsidered considering considers reconsider reconsiders reconsidered reconsidering reconsideration reconsiderations
consult consultancy consultant consultants consultation consultations consultative consulted consults consulting
contact contactable uncontactable contacted contacting contacts
continue continual continually continuance continued continuity continues continuing continuous continuously continuation continuations
contract contracted contracting contractor contractors contracts
control controlled controller controllers controlling controls uncontrollable uncontrollably controllable uncontrolled
converse converses conversed conversing conversant conversation conversations conversational conversationally conversationalist conversationalists
cook cooks cooking cookers cooker cooked uncooked cookery cookeries
copy copying copies copied copier copiers copyist copyists
corner corners cornered cornering
correct corrects correctly correcting corrected correctness correction corrections corrective incorrect incorrectly uncorrected
cost costing costings costed costs costly costless
could couldn
council councillor councillors cllr cllrs councilor councils
count counted uncounted counting countless counts countable uncountable
country countries
county counties
couple coupled uncoupled coupling couples
course courses
court courts courtly courted courting
cover covered covering coverings coverage covers uncover uncovered uncovers coverlet coverlets
create created creates creating creation creations creative creatively creativity creator creators recreate recreated recreates recreating
cross crossed crosses crossing crossings crossly crossness
cup cups cupping cupped cuplike
current currents currently
cut cuts cutting cuttings uncut cutter cutters
d
dad daddy dads
danger dangerous dangerously dangers endanger endangers endangered endangering endangerment endangerments
date dates dated undated dating datable
day daily daylight days midday goodday gidday
dead deaden deadened deadening deadens deadly
deal dealer dealers dealership dealerships dealing dealings deals dealt undealt
dear dearer dearest dearly dears
debate debatable debated debates debating
decide decided decidedly decides deciding undecided decider deciders
decision decisions
deep deepen deepens deepened deeper deepest deeply depth depths deepening
definite definitely definitive definitively indefinite indefinitely
degree degrees deg
department departments departmental departmentally dept depts
depend depends depended depending dependant dependants dependent dependents dependable undependable dependably
describe described describes indescribable indescribably describing description descriptions descriptive
design designed designer designers designing designs
detail detailed detailing details
develop developed developer developers developing development developments developmental developmentally develops underdeveloped underdevelopment undeveloped redevelop redevelops redeveloped redeveloping redevelopment redevelopments
die died dies dying undying
difference differences different differently
difficult difficulties difficulty
dinner dinners
direct directed undirected directing directly director directors directorship directorships directs indirect indirectly directness directnesses
discuss discussing discusses discussed undiscussed discussion discussions
district districts
divide divided divides dividing undivided division divisions divider dividers
do did didn does doesn doing doings don done doer doers
doctor doctors dr doc docs doctoral
document documentation documented undocumented documenting documents
dog dogs doggy doggies
door doors indoors indoor outdoors outdoor
double doubled doubles doubling doubly redoubled redoubles redoubling redouble
doubt doubted doubtful doubtfully doubter doubters doubting doubtless undoubted undoubtedly doubts
down downs downed downing downings downward downwards
draw drawing drawings drawn undrawn draws drew redraw redraws redrawing redrew redrawn
dress dressed dresses dressing undressed undress undresses undressing
drink drinks drinker drinkers drank drunk undrunk drinking
drive driven undriven driver drivers drives driveway driving drove
drop dropped dropping droppings drops droplet droplets
dry dried dries driest dryer drying dryly drily dryness drier driers
due duly undue unduly dues
during
e
each
early earlier earliest earliness
east eastward eastwards easterly easterlies
easy easier easiest easily easiness
eat ate eaten uneaten eating eats eater eaters
economy economic economical economically economics economies economist economists uneconomic uneconomical uneconomically economise economises economised economising economize economizes economized economizing
educate educating educates educated educative miseducated educator educators uneducated education educationist educationists educational educationally educationalist educationalists
effect effected effecting effective effectively effectiveness effects ineffective ineffectively ineffectiveness ineffectivenesses effector effectors
egg eggs
eight eighteen eighteenth eighth eighths eighties eightieth eighty eights
either
elect elected unelected electing election elections elects elector electors electoral electorally
electric electricity electricians electrician electrical electrically electrics
eleven elevens eleventh
else elsewhere
employ employed employee employees employer employers employing employment employs employable unemployed unemployable unemployment
encourage encouragingly encouraging encourages encouraged encouragement
end ended unended ending endings endless endlessly ends unending
engine engines engineer engineering engineers engineered
english englishman englishmen englishwoman englishwomen englishes england englander englanders englishness
enjoy enjoyed enjoying enjoyment enjoys enjoyable unenjoyable
enough
enter entered unentered entering enters entrance entrances entries entry
environment environmental environmentalist environmentalists environmentally environments environmentalism
equal equaled equaling equality equalled equalling equally equals inequality inequalities unequal unequalled equalise equalised equalises equalisation equalize equalized equalizes equalization equaliser equalisers equalizer equalizers
especial especially
europe european europeans
even evenly uneven unevenly
evening evenings
ever
every everybody everyday everyone everything everywhere
evidence evidenced evidential
exact exactly exactness
example examples
except exception exceptional exceptionally exceptions excepting
excuse excusing excuses excused excusable inexcusable
exercise exercised exercises exercising exercisable
exist existed existence existing exists existent nonexistent
expect expectancy expectation expectations expected expectedly expecting expects unexpected unexpectedly expectant expectantly
expense expenses expensive expensively inexpensive inexpensiveness inexpensively
experience experienced experiences experiencing inexperienced inexperience experiential experientially
explain explained unexplained explaining explains explanation explanatory explanations
express expressed unexpressed expresses expressing expression expressions expressionless expressionlessly expressive expressively expressiveness expressly
extra extras
eye eyes eyed eyeing eyeful
f
face faced faces facing faceless facial facially
fact facts factual factually
fair fairer fairest fairly fairness unfairness unfair unfairly
fall fallen falling falls fell
family families familial
far farther farthest faraway
farm farmer farmers farms farming farmed unfarmed
fast faster fastest
father fathers fatherly fatherhood
favour favor favors favorite favorites favourite favourable favourably favoured unfavoured favorable favorably favored unfavored favouring favoring favourites favours unfavourable unfavourably favouritism favoritism
feed fed feeding feeds unfed feeder feeders
feel feeling feelings unfeeling feels felt
few fewer fewest
field fields fielded fielding fielder fielders midfielder midfielders
fight fighter fighters fighting fought fights
figure figures figured figuring figurings figural fig figs
file filed unfiled files filing
fill filled unfilled filling fillings fills filler fillers refill refilled refilling refills refillable
film films filming filmed
final finalise finalised finalist finalists semifinalist semifinalists finalises finalising finalize finalized finalizes finalizing finality finally finals
finance financed unfinanced finances financial financially financier financiers financing
find finding findings finds found unfound finder finders
fine finely fineness finer finest finery
finish finished finishes finishing unfinished finisher finishers
fire fires fired firing misfire misfires misfired misfiring
first firsts firstly
fish fished fishes fishing fisherman fishermen fishy fishery fisheries fishier fishiest fishiness fishily
fit fitness fits fitted fitter fittest fitting fittings fittingly unfit
five fives fifteen fifteenth fifth fifths fifthly fifties fiftieth fifty
flat flattest flatten flattens flattened flattening flattish flatness flatly
floor floors flooring floorings floored
fly flew flown unflown flying flies flyer flyers flier fliers
follow followed unfollowed follower followers following ff follows
food foods
foot feet footed football footballing footballs footballer footballers ft
for fer
force forced unforced forcible forcibly forces forcing forceful forcefully
forget forgets forgetting forgot forgotten unforgotten unforgettable forgetful forgetfulness forgetfully
form formation formations formed forming forms formless formlessness
fortune fortunate fortunately fortunes unfortunately unfortunate
forward forwards forwarding forwarded forwarder forwarders
four fours forties forty fortyish fourteen fourteenth fourth fourthly fortieth th
france french frenchman frenchmen frenchwoman frenchwomen
free freed unfreed freedom freedoms freeing freely freer freest
friday fri fridays
friend friendly unfriendly friends friendship friendships friendliness
from
front fronts fronting fronted frontage frontages
full fuller fullest fullness fully
fun funny funnily funniest funnier
function functional functionally functioned functioning functions functionalist functionalists functionalism functionality functionalities
fund funded unfunded funder funders funding funds
further furthest furthering furthers furthered furtherance
future futures futuristic futuristically
g
game games gaming
garden gardener gardeners gardens gardening gardened
gas gases gaseous gasoline
general generally generalise generalisable generalised generalisation generalisations generality generalities generalization generalizations generalize generalizes generalized generalizing generalises generalising generalist generalists
germany german germans germanic
get gets getting got gotten gotta gotcha
girl girls gal gals girlish girlishness girlishly girly girlie girlies
give gave given gives giving giver givers gimme
glass glasses glassy glassier glassiest glassiness glassily
go goes going goings goin gone went gonna gunna
god gods goddess godless godly godliness godlike
good goodness goodly goody goodies
goodbye goodbyes bye
govern govt governs governor governors governing governed government governments governmental governorship intergovernmental gov
grand grandsons grandson grandparents grandparent grandpa grandpas grandmother grandmothers grandma grandmas grandfather grandfathers granddaughters granddaughter grandchildren grandchild gran grans granddad granddads
grant granted granting grants
great greater greatest greatly greatness
green greener greenest greenness greenish greeny greens greening
ground grounded grounds grounding groundless
group grouped grouping groupings groups subgroup subgroups
grow grew growing grown grows growth growths grower growers
guess guessing guesses guessed guessable unguessable
guy guys
h
hair hairy hairs haired
half halves halfway
hall halls
hand handed handedness handful handfuls handing hands handwriting handwritten
hang hanged hanging hangings hangs hung unhung hanger hangers
happen happened happening happenings happens
happy happier happiest happily happiness unhappy unhappily unhappiness unhappier unhappiest
hard harden hardened hardening hardens harder hardest hardness hardship hardships hardworking
hate hatred hatreds hating hates hated hateful hatefully hatefulness
have had hadn hasn has haven haves having ve hath
he him himself his
head headed heading headings heads headless headship
health healthier healthiest healthily healthy unhealthy unhealthiest
hear heard hearer hearing hearings hears unheard
heart hearts heartfelt hearten heartened heartens heartening heartless heartlessness heartlessly hearted disheartening disheartened disheartens
heat heated unheated heating heats heater heaters reheat reheated reheating reheats preheat preheats preheated preheating
heavy heavier heaviest heavily heaviness heavies
hell hells
help helped helpful helpfully unhelpful helpfulness unhelpfully helping helpless helplessly helplessness helps helper helpers
here
high higher highest highly highs highway highways
history historian historians historic historical historically histories historicist historicists historicism historicity
hit hitting hitter hits unhit
hold held unheld holder holders holding holdings holds
holiday holidays holidaying holidayed holidayer holidayers
home homeless homelessness homes
honest honesty honestly dishonest dishonesty dishonestly
hope hoped hopeful hopefuls hopefully hopefulness hopeless hopelessly hopelessness hopes hoping
horse horses unhorsed
hospital hospitals hospitalise hospitalises hospitalised hospitalising hospitalisation hospitalize hospitalizes hospitalized hospitalizing hospitalization
hot hotly hotness hotter hottest
hour hourly hours hr hrs
house housed housing houses
how
however
hullo hello hey hi hallo
hundred hundreds hundredth
husband husbands
i me mine my myself meself
idea ideas
identify identifiable identification identifications identified unidentified identifies identifying identities identity unidentifiable identifier identifiers
if ifs
imagine imagining imagines imagined unimagined imagination imaginations imaginative imaginatively imaginary imaginable unimaginable unimaginably imaginably unimaginative unimaginatively
important unimportant importantly
improve improving improves improved unimproved improvement improvements
in inner
include included includes including incl inclusive inclusion
income incomes
increase increased increases increasing increasingly
indeed
individual individualised individuality individualism individualist individualists individualistic individually individuals industrialist industrialists industrialise industrialisation industrialised industrialising industrialises industrialize industrialization industrialized industrializing industrializes
industry industrial industrially industries
inform informs informing informed informer informers information informational info informant informants uninformed
inside insides insider insiders
instead
insure insuring insures insured insurance insurer insurers insurable uninsurable reinsure reinsuring reinsures reinsured reinsurance
interest interested interesting interests uninterested uninteresting interestingly
into
introduce introduced introduces introducing introduction introductions introductory intro intros reintroduce reintroduces reintroduced reintroducing reintroduction reintroductions
invest invested investing investment investments investor investors invests reinvest reinvested reinvesting reinvestment reinvests
involve involved involvement involves involving uninvolved
issue issued issues issuing issuer issuers issuance
it its itself
item itemisation itemise itemised itemises itemising items itemization itemize itemized itemizes itemizing
jesus
job jobs jobless
join joined joining joins
judge judged judges judging judgment judgments judgement judgements judgemental misjudge misjudges misjudged misjudging misjudgement misjudgements prejudge prejudges prejudged prejudging prejudgement prejudgements
jump jumps jumping jumped jumpy
just justly unjust unjustly
k
keep keeper keepers keeping keeps kept
key keys keyed keying
kid kids
kill kills killed killer killers killing killings
kind unkind kindly unkindly kindness kinds kinda kinder kindest
king kings kingdom kingdoms
kitchen kitchens kitchenette kitchenettes
knock knocks knocking knocked knocker knockers
know knew knowing knowingly known knows unknown unknowing unknowingly dunno unknowable
l
labour labor laboured labouring labours labored laboring labors labourer labourers laborer laborers
lad lads
lady ladies ladylike unladylike ladyship ladyships
land landed landing landings lands landless
language languages
large largely larger largest
last lasted lasting lasts lastly
late lately lateness later latest
laugh laughs laughing laughed laughable
law laws lawyer lawyers lawful lawfully unlawful lawless lawlessness unlawfully lawmaker lawmakers
lay laid laying lays lain
lead leader leaders leadership leading leads mislead misleading misleadingly misled led
learn learned learner learners learning learns learnt
leave leaves leaving leaver leavers
left lefts leftist leftists lefthand lefthanded lefthander lefthanders
leg legs legged legging leggings leggy
less lessen lessened lessening lesser least
let lets letting lemme
letter letters
level levelled leveller levelling leveled leveler leveling levels levelly
lie liar liars lied lies lying
life lifetime lifetimes lifelike lifesize lifelong lifeless lifelessly
light lighted lighten lightened lightens lightening lighter lightest lighting lightly lightness lights lightweight lit unlit
like liked likes liking dislike dislikes disliked disliking likeable likeably
likely likelier likeliest likelihood unlikely
limit limitation limitations limited limiting limits unlimited limitless limitlessly
line lines lined lining
link linkage linkages linked unlinked linking links linker linkers
list unlisted lists listed listing
listen listened listener listeners listening listens
little littler littlest
live lived liveliest lively liveliness livelier lives living
load unload unloads unloading unloaded loads loading loaded
local locally locals localise localize localised localized localises localizes localising localizing localization localisation localism
lock unlocks unlocking unlocked unlock locks locking locked
london londoner londoners
long longer longest longish
look looked looking lookin looks
lord lords lordship lordships lordly lorded lording
lose loser losers loses losing lost
lot lots
love loved unloved loveless lovely lovelier loveliest loveliness loves loving lovingly lovable lover lovers luv luvs lovey loveys
low lows lowly lowlier lowliest lower lowered lowest lowering lowers
luck lucky luckily luckiest luckier luckless unlucky unluckily unluckiest unluckier
lunch lunches
m
machine machinery machines machinist machinists
main mains mainly
major majorities majority majors maj
make made unmade maker makers makes making makings remake remakes remaking remade
man mankind men mens manly manhood manliness mans manning manned unmanned
manage managing manages managers manager manageress manageresses managed management managements mismanage mismanaged mismanages mismanaging mismanagement manageable unmanageable
many
mark marked markedly unmarked marker markers marking markings marks
market marketed marketing markets nonmarket marketable marketer marketers marketeer marketeers
marry marriage marriages married marries marrying unmarried remarry remarries remarried remarrying remarriage
match matching matches matched unmatched mismatch mismatched mismatches mismatching
matter mattered mattering matters
may
maybe
mean meaner meanest meanly meanness
meaning meaningful meaningfulness meaningfully meaningless meanings means meant
measure measured measurement measurements measures measurable measurably immeasurably measuring
meet meeting meetings meets met unmet
member members membership memberships
mention mentioned mentioning mentions unmentioned
middle middles middling
might mightn
mile miles
milk milky milked milks milking
million millions millionth
mind minded mindless mindlessness mindful mindfulness minding minds minder minders
minister ministers ministerial ministering ministered
minus
minute minutes min mins
miss missed unmissed misses missing
mister mr
moment momentary momentarily moments
monday mon mondays
money moneys monies
month monthly months
more
morning mornin mornings
most mostly
mother mothers motherhood mothered mothering motherly mum mom mummy mums mam mams mammy mammies mommy mommies
motion motions motioning motioned motionless
move moved movement moves moving movements unmoving unmoved movable moveable unmovable unmoveable immovable immoveable mover movers
mrs missus missuses
much
music musical musicals musician musicians musically musique
must mustn
n
name named unnamed names naming namely nameless
nation national nationals nationally nationwide nations nationalism nationalisms nationalisations nationalist nationalists nationalistic nationalistically nationalise nationalised nationalising nationalisation nationalize nationalized nationalizing nationalization nationhood nationhoods
nature natural unnatural unnaturally naturally natures naturalistic naturalistically naturalness naturalist naturalists naturalism
near nearby nearer nearest nearly nearness nears nearing neared nearside
necessary necessarily unnecessarily unnecessary
need needed unneeded needing needless needs needn needlessly
never
new newer newest newly newness renew renewed renews renewing renewable renewal renewals
news newsy
next
nice nicest nicer niceness nicely
night nightly nights goodnight midnight
nine nines nineteen nineteenth nineties ninetieth ninety ninth
no nobody noone nothing nothingness nowhere nope
non
none
normal normalisation normalise normalised normalises normalising normalization normalize normalized normalizes normalizing normality normally
north northerly northerlies northwest nw northwestern northwesterner northwesterners northeast ne northeastern northeasterner northeasterners northwards northward
not t nt
note notable notes noting notably noted
notice noticeable noticeably noticed unnoticed notices noticing
now nowadays
number numbered unnumbered numberless numbering numbers nos
o
obvious obviously
occasion occasional occasionally occasions
odd odds odder oddest oddness oddly oddity oddities
of
off orf
offer offered offering offerings offers offerer offerers offerors offeror
office officer officers offices
often oft
okay ok
old older oldest oldish oldy oldies olden
on onto
once
one ones oneness
only
open opening openings openly openness opens opened unopened opener openers
operate operated operates operating operation operations operator operators operational operationally operative operatives
opportunity opportunities
oppose opposing opposes opposed opposition oppositional unopposed
or
order ordered ordering orderly orderliness orderlies orders unordered reorder reordered reordering reorders
organize organisation organisations organise organised disorganised disorganized unorganised organises organising organization organizations organized organizes organizing organisational organisationally organiser organisers organizer organizers organizational organizationally reorganise reorganises reorganised reorganising reorganisation reorganisations reorganize reorganizes reorganized reorganizing reorganization reorganizations
original originally originality unoriginal originals
other others otherness
otherwise
ought oughtn
out outer outside outsider outsiders outward outwardly outwards outs outta
over overly
own owned owner owners ownership owning owns
p
pack packs packing packed package packages packaging packaged packer packers unpack unpacking unpacked unpacks
page pages pp
paint painted painter painters painting paintings paints unpainted
pair pairs pairing paired unpaired
paper papers papered papering
paragraph paragraphing paragraphs para paras
pardon pardons pardoned pardoning pardonable unpardonable
parent parents parental parentage parented parenting
park parks parking parked
part parted parting partly parts partial partially pt pts
particular particulars particularly particularity particularities
party parties
pass passed passes passing passable passably impassable impassably passer passers
past
pay paid paying payment payments pays unpaid payer payers payable
pence
pension pensions pensioner pensioners pensioned pensioning pensionable
people peoples
per
percent percentage percentages
perfect perfected perfecting perfectly perfects perfection imperfect imperfectly imperfection imperfections perfectionist perfectionists
perhaps
period periodic periods periodical periodically periodicals
person personal personally persons
photograph photography photographs photographing photographers photographer photographed photographic photographically photo photos
pick picks picking pickers picker picked unpicked
picture pictured pictures picturing pic pics
piece pieces
place placed places placing placement placements
plan planned planner planners planning plans unplanned
play played player players playing plays replay replays replaying replayed playable unplayable playful playfulness playfully
please pleasant pleasantly pleasantness pleased pleases pleasing unpleasant unpleasantly unpleasantness unpleasantnesses pleasantry pleasantries displease displeased displeasing
plus pluses
point pointed pointedly pointing pointless pointlessly points pointer pointers midpoint midpoints
police policing policewoman policewomen polices policemen policeman policed
policy policies
politic politics political unpolitical politically nonpolitical politicize politicizes politicized politicizing politicization politicise politicises politicised politicising politicisation politician politicians
poor poorer poorest poorly poorness
position positions positioning positioned positional reposition repositions repositioning repositioned
positive positives positively positivist positivists positivism positivity
possible possibles possibilities possibility possibly impossibility impossible impossibly
post posted poster posters posting posts postal postage postages
pound pounds
power powered powerful powerfully powers powerless powerlessly powerlessness
practise practises practised practising practice practices practicing practiced
prepare preparation preparations prepared prepares preparing unprepared preparatory prep preparedness
present presenter presenters presentation presentations presentational presented presenting presents presentable unpresentable presentably
press pressed unpressed presses pressing
pressure pressured pressures pressuring pressurise pressurize pressurised pressurized pressurising pressurizing pressurisation pressurization
presume presumably presumed presumes presuming presumption presumptions
pretty prettier prettiest prettily prettiness
previous previously
price priced prices pricing priceless pricey
print printed printer printers printing prints printable reprint reprints reprinting reprinted
private privately
probable probably probability probabilities probabilistic probabilistically improbable improbably improbability improbabilities
problem problems problematic
proceed procedural procedure procedures proceeded proceeding proceedings proceeds
process processed processes processing unprocessed reprocess reprocesses reprocessed reprocessing reprocessings processor processors processer processers
produce produced producer producers produces producing
product products production productions productive productively unproductive productivity
programme program programmed programmes programming programs programed programing programmer programmers programmable
project projected projecting projection projections projects projective
proper properly improper improperly
propose proposal proposals proposed proposes proposing proposer proposers
protect protected protecting protection protections protectionism protectionist protectionists protective protects unprotected protector protectorate protectorates protectors protectively protectiveness
provide provided provides providing provider providers
public publicity publicly
pull pulled pulling pulls
purpose purposes purposely purposeful purposefully purposefulness purposeless purposelessness purposive
push pushing pushes pushed pushy pusher pushers
put puts putting
quality qualities
quarter quarterly quarters
question questions questioned questioning questioningly questionable questionably unquestionably questioner questioners unquestioned unquestioning unquestionable unquestionability
quick quickness quickly quickest quicker
quid quids
quiet quieter quietest quietly quietness quieten quietens quietened quietening
quite
r
radio radios radioed
rail railways railway rails railroads railroad railwayman
raise raised raises raising raiser raisers
range ranged ranges ranging
rate rated rates rating ratings rateable
rather
read reader readers reading readings reads misread misreads misreading readability readable unreadable reread rereads rereading unread
ready readily readiness unready
real unreal unrealistic unrealistically unreality realistic realistically reality realities realist realists realism realisms
realise realize realization realizations realized unrealised unrealized realizes realizing realisation realisations realised realising realises realisable realizable
really
reason reasonable unreasonable reasonableness unreasonableness reasonably unreasonably reasoned reasoning reasons
receive received receives receiving receivable
recent recently
reckon reckoned reckoning reckons
recognize recognise recognised recognises recognising recognition recognized recognizes recognizing recognisable unrecognisable unrecognizable recognisably unrecognised unrecognized recognizable recognizably
recommend recommends recommending recommended recommendation recommendations
record recorded unrecorded recording recordings records recorder recorders
red redder reddest redness redden reddened reddening reddens reddish reddy reds
reduce reduced reduces reducing reduction reductionist reductionists reductionism reductions reducible
refer refers referring referred referral referrals referent referents reference references referential
regard disregard disregarded disregarding disregards regarded regarding regardless regards
region regional regionalist regionalists regionalism regionally regions
relation relate related relates relating relations relationship relationships unrelated relational
remember remembered remembering remembers remembrance
report reported unreported reportedly reporter reporters reporting reports
represent representative representatives rep reps represented unrepresented representing represents representation representations representational unrepresentative representativeness
require required requirement requirements requires requiring
research researched researcher researchers researches researching
resource resourced resourceful resources resourcing unresourceful underresourced
respect respected respecting respects respectful respectable respectfully
responsible irresponsible responsibility responsibilities responsibly irresponsibly
rest rested resting restful restfully restfulness restless restlessly restlessness rests
result resulted resulting results resultant
return returned unreturned returning returns returner returners returnee returnees returnable
rid ridding rids
right rightful rightfully rightist rightists rightly rights rightness rt
ring rang ringed ringing rings rung
rise rises rising rose risen riser risers
road roads roadside rd
role roles
roll rolled rolling rolls roller rollers unroll unrolled unrolling unrolls
room rooms classroom classrooms roomy roomier roomiest
round rounded rounding rounder roundest roundly roundness rounds rounders
rule ruled unruled ruler rulers rules ruling rulings
run ran runner runners running runs runny runnier runniest
safe safely safeness safer safest safety unsafe
sale sales saleable unsaleable
same sameness
saturday saturdays
save saved unsaved saves saving savings saver savers
say said unsaid saying sayings says
scheme schematic schematically schemed schemes scheming
school schooling schools schooled preschool preschools preschooling preschooled preschooler preschoolers
science sciences scientific scientist scientists scientifically unscientifically unscientific
score scored scoring scores scorer scorers
scotland scotch scot scots scottish
seat seated seating seats seater seaters unseated unseats unseating unseat
second secondary secondarily secondly seconder seconders secondee
secretary secretaries secretarial
section sectional sectioned sectioning sections subsection subsections
secure insecure insecurities insecurity secured securely secures securing securities security unsecured
see saw seeing unseeing seen sees unseen seer seers
seem seemed seeming seemingly seems
self selfishness selfishly selfish selves selfless selflessness selflessly unselfish unselfishness unselfishly
sell seller sellers selling sells sold unsold resell reselling resold reseller resellers
send sender senders sending sends sent unsent
sense senseless senselessness senses sensing sensings sensed
separate separated separately separates separating separation separations separatist separatists inseparable separateness separatenesses separatism separable separably inseparably
serious seriously seriousness
serve servant servants served unserved serves serving servings server servers servery
service services serviced unserviced servicing
set sets setting settings unset
settle settled settlement settlements settler settlers settles settling settlor settlors resettle resettled resettlement resettlements resettler resettlers resettles resettling
seven seventeen seventeenth seventh seventies seventieth seventy
sex sexes sexism sexual sexuality sexually sexy sexier sexiest sexiness sexily sexist sexists
shall shan shalt
share shared unshared shares sharing
she her hers herself
sheet sheets
shoe shoed shoeing shoes shoeless
shoot shooting shootings shoots shot shots shooter shooters
shop shops shopping shoppers shopper shopped
short shortage shortages shorten shortened shortening shortens shorter shortest shortly shortness
should shouldn
show showed showing shown shows
shut shutting shuts
sick sickness sickly sickest sicker sicken sickened sickens sickening sickeningly
side sides sided siding
sign signed signing signs unsigned signer signers
similar dissimilar similarities dissimilarity dissimilarities similarity similarly
simple simpleness simpler simplest simplicity simplification simplified simplify simplifies simplifying simply
since
sing sings sang sung unsung singer singers singing
single singled singly singleness singling singles
sir
sister sisters sisterly
sit sat sits sitting sittings sitter sitters
site sited siting sites
situate situation situational situationally situations situated situating
six sixes sixteen sixteenth sixteenths sixth sixthly sixths sixties sixtieth sixtieths sixty
size sizes sizing sized sizable
sleep sleeping sleeps sleepy sleepiness slept sleepless sleeper sleepers sleepily
slight slighter slightest slighting slights slighted slightly
slow slowed slower slowest slowing slowly slowness slows
small smaller smallest smallness smallish
smoke smoked smokes smoking smokeless smoker smokers smokefree nonsmoking smoky smokier smokiest smokiness smokey
so
social socially antisocial
society societies societal
some somebody somehow someone something somethin sometime sometimes somewhere
son sons sonny
soon sooner soonest
sorry sorriness sorriest sorrier
sort sorted unsorted sorting sorts
sound sounds sounded sounding soundless soundlessly
south southeast se southeastern southeasterners southward southwards southwest sw southwestern southwesterner southwesterners southerly southerlies
space spaced unspaced spaces spacing spacious spaciousness spaciously
speak speaker speakers speaking speaks spoke spoken unspoken unspeaking unspeakable
special specials specially specialist speciality specialty specialities specialists specialize specialization specialized specializations specialise specialises specialised specialising specialisation specializes specializing specialism specialisms
specific specifically specification specifications specificity specifics
speed sped speeded speeding speeds speedy speedily highspeed
spell spelt spells spelling spellings spelled misspelt
spend spending spends spent unspent spender spenders
square squarely squareness squarer squares squarest squared squaring sq
staff staffed staffing staffs staffer staffers
stage staging staged stages
stairs stair upstairs downstairs
stand standing stands stood
standard standards standardise standardised unstandardised standardising standardisation standardize standardized unstandardized standardizing standardization substandard
start started starting starts starter starters restart restarts restarted restarting
state stated unstated statement statements stating
station stations stationed stationing
stay stayed staying stays stayer
step stepped stepping steps
stick sticking sticks stuck unstuck sticker stickers
still stiller stillest stillness stills stilled stilling
stop stopped stopping stops unstoppable stoppage stoppages stopper stoppers
story stories
straight straighten straightener straighteners straightened unstraightened straightening straightens straighter straightest
strategy strategic strategies strategically strategist strategists
street streets st
strike strikes striking strikingly struck striker strikers
strong stronger strongest strongly
structure restructure restructured restructures restructuring structural structurally structured structures structuring unstructured structuralism structuralisms structuralist
student students
study studied studies studying studious studiously
stuff stuffs stuffing stuffed
stupid stupidity stupidly stupidest stupider
subject subjected subjecting subjects subjection subjections
succeed succeeded succeeding succeeds success successes successful successfully unsuccessful unsuccessfully
such
sudden suddenly suddenness
suggest suggested suggesting suggestion suggestions suggests suggestive suggestiveness suggestively
suit suits suiting suited suitability suitable suitably unsuited unsuitable
summer summers midsummer summery summered summering
sun sunlight sunny suns sunshine sunned sunning
sunday sundays
supply supplied supplier suppliers supplies supplying
support supported supporter supporters supporting supports supportive unsupported
suppose supposed supposedly supposes supposing
sure surely sureness surer surest unsure
surprise surprised surprises surprising surprisingly unsurprising unsurprised unsurprisingly
switch switched switches switching
system systematic unsystematic unsystematically systems systematically subsystem subsystems
table tablecloth tables tabled tabling
take taken takes taking takings took taker takers
talk talked talking talks talker talkers
tape taped tapes taping
tax taxes taxed taxing taxpayer taxpayers taxation taxable nontaxable untaxed
tea teas
teach taught teacher teachers teaches teaching teachings
team teamed teaming teams
telephone telephoning telephones telephoned phones phoning phoned phone tel
television televisions tv telly tellies tvs
tell retell retelling telling tells told untold
ten tens tenth tenths
tend tends tended tending tendency tendencies
term terms termed terming
terrible terribly
test tested untested testing tests tester testers testable untestable retest retested retests retesting
than
thank thanks thanking thankfully thankful thankless thanked
the
then
there
therefore
they their theirs them em themselves
thing things thingy thingies
think thinking unthinkable thinks thought thoughts thoughtful thoughtfully thoughtfulness unthought unthinking unthinkingly thoughtless thoughtlessly thoughtlessness thinker thinkers rethink rethought rethinks rethinking
thirteen thirteenth thirteenths
thirty thirties thirtieth thirtieths
this these those that
thou thee thine thy thyself tha thi
though tho
thousand thousands thousandth thousandths
three threes third thirdly thirds
through throughout
throw threw throwing thrown throws thrower throwers
thursday thurs thursdays
tie untied untie tying ties tied unties untying
time timer times timeless timely timing timed untimed
to
today
together togetherness
tomorrow tomorrows
tonight
too
top topped untopped topping tops topless
total totaled totaling totalled untotalled totalling totally totals totality
touch touched touches touching untouched touchable untouchable untouchables
toward towards
town towns
trade traded trades trading trader traders
traffic
train trained trainer untrained trainers training trains trainee trainees
transport transportation transported transporter transporters transporting transports
travel traveled traveling travelled traveller travellers travelling travels traveler travelers
treat treats treating treated treatable untreated treatment treatments pretreatment
tree trees treeless
trouble troubled untroubled troubles troubling troublesome troublemaker troublemakers
true truthful truthfully truth truest truer truism truisms truthfulness truly truths untrue untruth untruthful untruthfully untruths untruthfulness
trust trusted trusting entrust entrusted entrusting entrusts trusts trusty trustier trustiest
try tried untried tries trying
tuesday tues tuesdays
turn turned turning turns
twelve twelves twelfth twelfths
twenty twenties twentieth
two twice twos
type typed types typing typist typists subtype subtypes
u
under underneath
understand understanding understandings understands understood understandable understandably misunderstand misunderstands misunderstood misunderstanding misunderstandings
union unions unionist unionists unionism unionisms
unit units subunit subunits
unite united unites uniting unity reunite reunites reunited reuniting
university universities
unless
until til till
up ups upside
upon
use misused misuse misusing misuses misuser misusers used unused useful usefulness useless uselessness uselessly uses using usefully user users usable usability unusable reuse reuses reused reusing
usual usually unusual unusually
v
value valuable valuables valuation revalues revalued revaluing revaluation revaluations valuations valued valuer valueless values valuing invaluable invaluably
various variously
very
video videoed videoing videos
view viewed viewing views viewer viewers
village villager villagers villages
visit visited visiting visitor visitors visits visitation
vote voted voter voters votes voting
w
wage wages unwaged waged waging
wait waited waiting waits waiter waiters waitress waitresses
walk walked walking walks walker walkers walkable
wall walled walls
want wanted wanting wants unwanted wanna
war warred warring wars
warm warms warmly warming warmed warmth warmer warmest
wash washed washes washing unwashed washer washers washable unwashable
waste wasted wastes wasting wasteful wastefully wastage wastages
watch watched watches watching watcher watchers
water watered waters watering watery waterier wateriest wateriness
way ways
we our ours ourselves us
wear wearing wears wore worn unworn wearable unwearable wearer wearers
wednesday wednesdays
wee
week weekend weekends weekly weeks midweek midweekly
weigh weights weight weighs weighing weighed unweighed weighted weighting weightings weightless weightlessness
welcome welcomed welcomes welcoming unwelcome
well unwell
west westerly westerlies westward westwards midwest midwestern
what whatever wot whatcha whaddya
when whenever
where wherever
whether
which whichever
while whilst
white whiteness whiter whitest whitish whites whiten whitening whitens whitened whitener whiteners
who whoever whom whose
whole wholes wholeness wholly wholistic wholistically
why
wide widely widen widens widened wideness widening wider widest width widths
wife wives
will ll wo willing willingness unwillingness willingly unwilling unwillingly willed
win winner winners winning winnings wins won
wind winded winds windy
window windows windowless
wish wished wishes wishing
with wiv
within
without
woman women womanly
wonder wondered wonderful wondering wonderingly wonders wonderfully wondrous wondrously wonderment
wood woods wooden woodland woodlands woody
word words worded wording wordy wordless wordlessly
work worked worker workers working workings works workman workmen workable unworkable
world worlds worldly unworldly worldliness unworldliness
worry worrying worries worried worriedly worryingly worriedness
worse worst
worth worthy worthier worthiest unworthy worthless
would wouldn
write writer writers writes writing writings written unwritten wrote rewrite rewrote rewritten rewrites rewriting rewrit
wrong wronged wronging wrongs wrongly wrongful wrongfulness wrongfully
x
y
year years yearly yr yrs yearling yearlings
yes yeses ya yah yeah yeh yea yep yup
yesterday yesterdays
yet
you your yourselves yourself yours ye yer yerself yous
young younger youngster youngest youngsters youngish''')

base2unsplit = ('''
above
abuse abused abusive abusing abuses abuser abusers
accent accented unaccented accenting accents
access accessed accesses accessibility accessible accessing inaccessible
accident accidents accidental accidentally
accommodate accommodated accommodates accommodating accommodation accommodations
according
accurate accuracy accuracies inaccuracy inaccuracies accurately inaccurate inaccurately
acid acids acidly acidic acidity
adequate adequacy adequately inadequacies inadequacy inadequate inadequately
adjust adjusted adjusting adjusts adjustment adjustments adjustable nonadjustable adjuster adjusters
adopt adopted adopting adoption adoptions adopts adoptive adopter adopters
adult adulthood adults
advance advanced advances advancement advancing
advantage advantages disadvantage disadvantages advantaging advantaged disadvantaged advantageous disadvantageous disadvantageously advantageously
advice
advise advising advises advisers adviser advised advisable advisably inadvisable advisor advisors advisory
affair affairs
afraid unafraid
africa african africans
agenda agendas
ahead
aid aided aiding aids unaided
aim aims aiming aimed aimless aimlessness aimlessly
aircraft
airport airports
alarm alarmed alarming alarmingly alarms alarmist alarmists
alive
allocate allocated allocates allocating allocation allocations
alone
alter alterable alteration alterations altered altering alters unalterable unaltered
alternative alternatively alternatives
altogether
amaze amazes amazed amazing amazingly amazement
among amongst
analyse analysed analyser analysers analyses analysing analysis analyst analysts analytic analytical analytically analyze analyzed analyzes analyzing
angle angles angling angled
animal animals
announce announced announcement announcements announcer announcers announces announcing unannounced
annoy annoys annoyed annoying annoyance annoyances
annual annuals annually
anti
apology apologize apologies apologetic apologetically apologist apologists apologizes apologized apologise apologising apologizing apologises apologised
appeal appealed appealing appeals
apple apples
appreciate appreciable appreciably appreciated appreciates appreciating appreciation unappreciated appreciative unappreciative appreciatively
approve approving approves approved approval approvals approvingly
april apr
army armies
arrive arrival arrivals arrived arrives arriving
article articles
asleep
aspect aspects
assemble assembled assembles assemblies assembling assembly assembler assemblers assemblage
assess assessable assessed assesses assessing assessment assessments reassess reassessed reassessing reassessment unassessed assessor assessors
assign assigned assigning assignment assignments assigns reassign reassigned reassigning reassigns unassigned reassignment assignee assignees
assist assistance assistant assistants assisted assisting assists unassisted
assure assurance assurances assured assuredly assures assuring reassure reassured reassures reassuring reassuringly reassurance reassurances
attach attached attaches attaching attachment attachments unattached
attack attacked attacking attacks attacker attackers
attempt attempted unattempted attempting attempts
attitude attitudes attitudinal
attract attracts attracting attracted attractive unattractive unattractively attraction attractions attractively attractiveness
audience audiences
august aug
aunt aunts aunty auntie aunties
australia australian australians aussie aussies
automatic automatically
average averaged averages averaging
avoid avoids avoiding avoided avoidance avoidable unavoidable unavoidably
award awarded awarding awards
awkward awkwardly awkwardness awkwardnesses
background backgrounds backgrounded backgrounding backer backers
bake bakes baked baking baker bakers bakery bakeries
band banded banding bands
bang banged banging bangs banger
bath baths
bathroom bathrooms
battery batteries
battle battled battles battling battler battlers
bean beans
beer beers
beg begs begging begged beggars beggar
behalf
behaviour behaviours behaviors behavioural behavior behavioral behaviourist behaviourists behaviorist behaviorists behaviourism behaviorism
bell bells
belong belonged belonging belongings belongs
below
belt belts belted unbelted belting
bend bending bent bends bendable unbending
beside besides
beyond
bid bidding bids bidder bidders
bike bikes biker bikers
bin bins
bind binds binding binders binder bound unbound
bird birds
biscuit biscuits
bite bites biting bitten
blame blaming blames blamed blameless blamelessly
blank blankly blanked blanks blanking
bless blessed unblessed blesses blessing blessings
blind blinds blindly blinding blinded blindness
block blocks blocking blocked unblocked blockage blockages blocker blockers
bloom bloomed blooming blooms bloomer bloomers
boil boils boiling boilers boiler boiled
bomb bombed bombing bombings bomber bombers bombs
bone boning bones boned bony bonier boniest boniness
bonus bonuses
booking booked bookings
boot boots booted booting
boring bores bored boringly boredom
borrow borrows borrowing borrowings borrowed unborrowed borrower borrowers
boss bosses bossy
boundary boundaries
bowl bowled bowling bowls bowler bowlers
bracket brackets
brain brains brainy brainier brainiest braininess brainless
branch branches branched branching
bread
breakfast breakfasts breakfasting breakfasted
brick bricks
bridge bridges bridging bridged
bright brighten brightened brightening brightens brighter brightest brightly brightness
broad broadly broader broadest broaden broadened broadening broadens
brochure brochures
brown browns browning browned browny brownish browner brownest
brush brushing brushes brushed unbrushed
bugger buggered buggers buggering buggery
burn burned burning burnings burns burnt burnable unburnable burner burners
butter butters buttering buttered unbuttered
button buttons buttoning buttoned unbutton unbuttoning unbuttons unbuttoned
cabinet cabinets
calculate calculator calculators calculating calculates calculated calculation calculations
calm calms calmly calming calmed calmness calmer calmest
camera cameras
camp camped camping camps camper campers
campaign campaigned campaigning campaigns campaigner campaigners
cancel cancelled cancelling cancels cancellation cancellations
candidate candidates candidature candidacy candidacies
capable capably capabilities capability incapable incapability
capacity capacities incapacity incapacities
capital capitals
career careers
carpet carpeted carpeting carpets
cash cashes cashed cashing
cast casting castings casts
category categories categorisation categorise categorised categorises categorising categorization categorize categorized categorizes categorizing uncategorised uncategorized
celebrate celebrated uncelebrated celebrating celebrates celebration celebrations celebratory
cell cells
century centuries
chain chains chaining chained unchained
challenge challenged unchallenged challenger challengers challenges challenging
channel channelled unchannelled channelling channels
chapter chapters chapt ch
charity charities
chase chased chases chasing chaser chasers
chat chatting chatted chats chatty
cheer cheers cheered cheering cheerless cheerlessness cheerlessly cheery cheerier cheeriest cheeriness cheerily
cheese cheeses
chemical chemically chemicals
cheque cheques
chest chests
chicken chickens chick chicks
chief chiefs chiefly
china chinese chinas chinaman chinamen
chip chips chipped chipping chippings
chocolate chocolates chocolatey choc chocs
chop chopping chopped chops chopper choppers
chuck chucks chucked chucking
cigarette cigarettes
circle circled circles circling circular
circumstance circumstances
citizen citizens citizenship citizenships
civil civility civilities
clarify clarification clarified clarifies clarifying clarity
clerk clerks clerkish
clever cleverness cleverly cleverest cleverer
climb climbs climbing climbers climber climbed unclimbed
cloud cloudy clouded unclouded clouds clouding cloudless
clue clues clueless
coach coached coaching coaches
coal coals
coast coasts coastal
coat coats coated coating coatings
code coded uncoded codes coding
combine combining combines combined combination combinations recombine recombined recombines recombining recombination recombinant
comfort uncomfortable uncomfortably discomfort comforts comforting comforted comfortably comfortable comfortingly
command commanded commanding commands commander commanders commandment commandments
commerce commercial commercials commercially commercialisation commercialise commercialised commercialising commercialises commercialize commercialized commercializing commercializes commercialization commercialism
commission commissioned uncommisioned commissioner commissioners commissioning commissions
communicate communicable communicated communicates communicating communication communications communicative communicatively uncommunicative communicator communicators
compensate compensated compensates compensating compensation compensations compensatory
compete competing competes competed competitive competitively competitiveness competitor competitors uncompetitive uncompetitiveness
competition competitions
complain complains complaining complained
complaints complaint complainant complainants
complex complexes complexities complexity
complicate complicated complicates complication complications complicating uncomplicated
concentrate concentrated concentrates concentrating concentration concentrations
concept conception conceptions concepts conceptual conceptualisation conceptualisations conceptualise conceptualised conceptualises conceptualising conceptualization conceptualizations conceptualize conceptualized conceptualizes conceptualizing conceptually
conclusion conclusions
confidence confidences confident confidently
confirm confirmation confirmed unconfirmed confirming confirms
conflict conflicted conflicting conflicts
confuse confusing confusingly confuses confused confusion
connect connected connecting connects connection connections connexion connexions unconnected connector connectors interconnect interconnected interconnects interc0nnecting interconnection interconnections connective connectives connectivity
conscious consciousness unconsciousness unconscious unconsciously consciously
conservative conservatively conservatives
considerable inconsiderable considerably
consistent consistently inconsistencies inconsistency inconsistent
constant constantly constants inconstantly constancy inconstancy constancies inconstancies
consume consumed consumer consumers consumes consuming consumption consumerism consumable consumables
contain contained container containers containing contains containment
content contented contenting contentment contents contentedly
context contexts contextual contextualise contextualised contextualising uncontextualised contextualize contextualized contextualizing uncontextualized
contribute contributed contributes contributing contribution contributions contributor contributors contributory noncontributory
convince convinced convinces convincing convincingly unconvincing unconvincingly unconvinced
cool cools coolness coolly cooling coolest cooler coolers cooled uncooled coolant coolants
cope coped coping copes
corporate corporates corporation corporations corp corporatism corporatist corporatists
cottage cottages cottager cottagers cottaged
cough coughs coughed coughing
counter countered counters countering
countryside
cow cows
crack cracks cracking cracked
crap craps crapped crapping crappy
cream creams creaming creamed creamy creamier creamiest creaminess creamily
credit credited crediting creditor creditors credits
crime crimes
criminal criminals criminally criminality
crisis crises
crisp crisped crisping crisps crispy crispier crispiest crispiness crisply
criterion criteria criterions
critic critics critically critical uncritical uncritically
crowd crowded uncrowded crowding crowds
cry cried cries crying crier criers
culture cultural culturally cultured cultures uncultured
cupboard cupboards
curtain curtains curtained curtaining
customer customers
cycle cycled cycles cyclic cyclical cycling cyclist cyclists bicyclist bicyclists
damage damaging damages damaged undamaged
damn damned damning damns damnable damnedest damnation dammit damnit
dance danced dancer dancers dances dancing
dare dared dares daring
dark darker darkest darkness darken darkens darkened darkening darkener darkeners darkly
data datum
daughter daughters
death deathly deaths deathless deathlessly
debt debts debtor debtors
december dec
decent indecent indecently decently
declare declaration declarations declared undeclared declares declaring
decorate decoration decorations decorated undecorated decorates decorating decorative decoratively decorator decorators redecorate redecorates redecorated redecorating redecoration redecorations
defence defences defense defenses defensive defensively defenceless defencelessly defensible indefensible indefensibly defensibly
defend defends defending defenders defender defended undefended
define definable indefinable indefinably undefinable defined defines defining definition definitions definitional redefine redefined redefines redefining redefinition redefinitions undefined
delay delays delaying delayed
delegate delegates delegated delegating delegation delegations
delight delights delighting delightfully delightful delighted delightedly
deliver delivered deliveries delivering delivers undelivered delivery
demand demanded demanding demands undemanding
democrat democrats democratize democratizes democratized democratizing democratise democratises democratised democratising democratic undemocratic nondemocratic democratically democratisation democratisations democratization democratizations
demonstrate demonstrable demonstrably demonstrated demonstrates demonstrating demonstration demonstrations demonstrative demonstratively demonstrator demonstrators demo demos
deny deniable denial denials denied denies denying undeniable undeniably
depress depressed depresses depressing depression depressions depressive depressives depressingly antidepressant antidepressants
deputy deputies
desire desired desirability desirable desires desiring undesirable desirous
desk desks
desperate desperation desperately
despite
destroy destroyed destroying destroys destruction destructive destroyer destroyers
detect detectable detected detecting detection detective detectives detector detectors detects undetected
determine determination determinations determined undetermined determinedly indeterminate determinate determines determining determinant determinants determinism determinist determinists deterministic deterministically indeterminacy indeterminacies
diagram diagrams diagrammed diagramming diagrammatic diagrammatically
diary diaries diarist diarists
dictionary dictionaries
diet dietary dieted dieting diets dieter dieters dietician dieticians
dig digger diggers digging digs dug undug
direction directional directions
directory directories
dirty dirtier dirtiest dirt
disabled disability disabilities disable disabling disables
disappear disappearance disappearances disappeared disappearing disappears
disappoint disappoints disappointing disappointingly disappointed disappointment disappointments
disaster disasters disastrous disastrously
discount discounted discounting discounts discounter
discover discovered discoveries discovering discovers discovery discoverer discoverers undiscovered rediscover rediscovers rediscovered rediscovering rediscovery rediscoveries
disease diseases diseased
disgust disgusted disgusts disgusting disgustingly
dish dishes dished dishing
display displayed displaying displays undisplayed
distance distances distant distantly distanced distancing
distinct distinction distinctions distinctive distinctively distinctly indistinct indistinctly distinctiveness distinctivenesses
distribute distributes distributed distributing distribution distributional distributions distributive distributor distributors distributable redistribute redistributed redistributes redistributing redistribution redistributive
dock docked docking docks docker dockers
dollar dollars
domestic domestically domestics domesticity domesticities
dot dotted dotting dots
dozen dozens
draft drafted drafting drafts redraft redrafts redrafted redrafting
drag drags dragging dragged
drama dramas dramatic dramatically dramatise dramatised dramatising dramatises dramatisation dramatisations dramatist dramatists dramatization dramatizations dramatize dramatized dramatizes dramatizing
drawer drawers
dream dreamed undreamed dreamer dreamers dreaming dreams dreamt dreamy dreamily
drug drugged drugging drugs
duck ducks ducking ducked duckling ducklings
dump dumped dumping dumps
dust dusts dustless dusty dustier dustiest dustiness dusted dusting duster dusters
duty duties dutiful dutifully dutifulness
ear ears
earn earns earning earned unearned earnings earner earners
earth earths earthy earthly unearthly unearthliness
easter
edge edged edges edging
edit edited unedited editing edition editions editor editorial editorials editors edits ed eds editorship editorships
efficient efficiency efficiencies inefficiency inefficiencies efficiently inefficient inefficiently
effort efforts effortless effortlessly
elder elderly elders
element elements
embarrass embarrassed embarrasses embarrassing embarrassingly embarrassment
emergency emergencies
emotion emotional emotionally unemotionally unemotional emotions
emphasis emphases emphasise emphasises emphasised unemphasised emphasising emphasize emphasized unemphasized emphasizes emphasizing
empty emptying empties emptied emptiness
enable enabled enables enabling
energy energetic energetically energies energise energised energising energises energize energized energizing energizes energiser energisers
engage engaged engaging engagingly engages engagement engagements
enormous enormously
enquire enquiry enquiries enquires enquiring enquiringly enquired enquirer enquirers
ensure ensured ensures ensuring
entertain entertains entertaining unentertaining entertained entertainment entertainments entertainer entertainers
entire entirity entirely
entitle entitled unentitled entitles entitling entitlement entitlements
equip equipment equipped unequipped equipping equips
escape escaped escapes escaping escapee escapees escaper escapers escapism escapist esc
essential essentials essentially
establish disestablish disestablished disestablishes disestablishing disestablishment established establishes establishing establishment establishments reestablish reestablishing reestablished reestablishes reestablishment
estate estates
estimate estimated est estimates estimating estimation estimations estimator estimators inestimable inestimably
etc etcetera cetera
event eventful events uneventful uneventfully
eventual eventuality eventualities eventually
evolve evolution evolved evolving evolves evolutionary evolutionist evolutionists
ex
exam exams
examine examining examines examined unexamined examiner examiners examination examinations
excellent excellence excellently
excess excesses excessive excessively
exchange exchanged exchanges exchanging exchanger exchangers
excite exciting excites excitedly excited excitement excitable excitably excitation excitations
exclude excluded excludes excluding exclusion exclusionary exclusionist exclusions exclusive exclusively exclusivity
exhibit exhibited exhibiting exhibition exhibitions exhibits exhibitor exhibitors exhibitionism
expand expanded expanding expands expandable expandability
experiment experimental experimentally experimentation experimented experimenting experiments experimenter experimenters
expert expertly experts
extend extended unextended extending extends
extension extensions extensive extensively
extent
extreme extremely extremes extremity extremities extremist extremists extremism
facility facilities
factor factored factoring factors
factory factories
fail failed failing failings fails unfailing unfailingly
faith faithful faithfulness faithfully faiths unfaithful unfaithfulness unfaithfully faithless faithlessly
familiar familiarly familiarity unfamiliar unfamiliarity familiarise familiarises familiarised familiarising familiarisation familiarize familiarizes familiarized familiarizing familiarization
famous famously
fan fans fanning fanned
fancy fancied fancier fancies fanciest fancily fanciness fancying
fashion fashionable fashionably fashioned fashioning fashions unfashionable unfashionably
fat fatter fattest fatness fatty fattier fattiest fattiness fatten fattening fattened fattens fattish fats
fault faulty faults faultless faulted unfaulted
fear feared unfeared fearful fearfully fearless fearlessly fearlessness fearing fears
feature featured features featuring featureless
february feb
fee fees
fellow fellows fellowship fellowships fella fellas
female females
fence fencing fences fenced unfenced
fetch fetched fetches fetching
finger fingers fingered fingering
firm firmness firmly firmer firmest firmed firming
firms
fix fixed unfixed fixes fixing fixable fixedly fixer fixers
flatting flats flatted
flexible flexibility inflexible inflexibility flexibly inflexibly
float floats floating floated
flow flowed flows flowing
flower flowered flowering flowers flowery flowerier floweriest floweriness
focus focused focuses focusing focusses focussed focussing refocus refocused refocuses refocusing refocussed refocusses refocussing unfocused unfocussed
folk folks
fool fools foolishness foolishly foolish fooling fooled
foreign foreigner foreigners
forest forests foresting forested forester foresters
forgive forgiving forgives forgiveness forgiven forgave unforgiving unforgiven unforgivable unforgivably
formal formally formality formalities formalise formalised formalisation formalising formalize formalized formalization formalizing formalism formalist formalists
forth
fortnight fortnights fortnightly
fraction fractions fractionally fractional
frame framing frames framed
frank franker frankest frankness frankly
freeze froze frozen unfrozen freezing freezes freezer freezers
fresh freshness fresher freshest freshly freshen freshening freshens freshened
fright frights frightful frightens frightening frightened frighten frighteningly frightener frighteners frightfully
fruit fruits fruity fruitless
fuel fueled fueling fuelled fuelling fuels
furniture
gain gained gaining gains gainer gainers gainful
gap gaps
garage garages
gate gates
gather gathered gathering gatherings gathers gatherer gatherers
gear gears geared gearing gearings
generate generated generates generating generative degenerative generatively degeneratively generation generations generational
gentleman gentlemen gentlemanly ungentlemanly gent gents
gift gifts gifted
glad gladder gladdest gladly gladness gladden gladdens gladdened gladdening
goal goalless goals
gold golden
golf golfer golfers golfing
goods
grab grabbed grabbing grabs
grace gracing graces gracefully graceful graced graceless
grade grades graded ungraded grading grader graders
gradual gradually
graph graphs graphed graphing
grass grasses grassy grassed grassing
grateful gratefully ungrateful ungratefully ungratefulness
grey greys greyly greyish greyness gray grayly grayish grayness
guarantee guaranteed guaranteeing guarantees
guard guarded unguarded guarding guards
guide guiding guides guided unguided guidance
guilty guiltily guilt guiltless
gun guns gunner gunners
handle handled handles handling handler handlers
hardly
harm harms harmless harmlessly harmfully harming harmful harmed unharmed
hat hats hatter hatters
heaven heavenly heavens
hide hid hidden unhidden hides hiding
highlight highlighted highlighting highlights
hill hills hillside hillsides hilly
hire hiring hires hired hirer hirers
hole holes holed holing
holy holier holiest holiness unholy unholier unholiest unholiness
homework homeworks
honour honor honorable honorably honorary honored honoured honoring honouring honors honours honourable honourably hon
hook hooks hooking hooked unhooked
horrible horribly horribleness
hotel hotels
household households
huge hugely hugeness
human humans humanity nonhuman nonhumans humanly inhuman inhumanity humanist humanists humanism humanistic
hunger hungry hungrily hungers hungering hungered
hunt hunts hunting hunters hunter hunted
hurry hurries hurried unhurried hurriedly unhurriedly hurrying
hurt hurts hurting hurtful unhurt
ice icy icily iced
ideal ideals ideally idealist idealists idealism idealise idealised idealising idealize idealized idealizing idealisation idealization idealisations idealizations
ignorant ignorance ignore ignored ignores ignoring
ill ills illness illnesses
image imagery images imaged imaging
immediate immediacy immediately immediateness
impact impacted impacting impacts
implicate implicated implicates implicating implication implications
impose imposed imposes imposing imposition
impress impressed unimpressed unimpressive impresses impressing impressive impressively impression impressionable impressions
inch inches inched inching
incredible incredibly
independent independents independently independence
india indian indians
indicate indicated indicates indicating indication indications indicative indicator indicators
influence influenced influencing influences influential uninfluenced
initial initials initially
initiate initiated initiates initiating initiation initiations initiative initiatives initiator initiators uninitiated
injure injured injures injuries injuring injury uninjured injurious
inspect inspected inspecting inspection inspections inspector inspectors inspects insp
instance instances
institute instituted institutes instituting institution institutional institutionalise institutionalised institutionalises institutionalising institutionalizing institutionalization institutionally institutions institutionalize institutionalized institutionalizes institutionalisation
instruct instruction instructed instructing instructions instructive instructor instructors instructs instructional instructionally
intelligence intelligent intelligently unintelligent
intend intended intending intends unintended
intent intently intention intentions intentional intentionally unintentional unintentionally
internal internalise internalised internalises internalising internalize internalized internalizes internalizing internally
international internationals internationally internationalise internationalised internationalises internationalisation internationalize internationalized internationalizes internationalization internationalist internationalists internationalism
interpret interpretation interpretations interpretative interpreted interpreting interpretive interprets misinterpret misinterpretation misinterpretations misinterpreted misinterpreting misinterprets reinterpret reinterpreted reinterprets reinterpreting reinterpretation reinterpretations interpreter interpreters
interview interviewed interviewing interviewer interviewers interviews interviewee interviewees
investigate investigated investigates investigating investigation investigations investigative investigator investigators
invite inviting invites invited uninvited uninviting invitation invitations
irish irishman irishmen irishwoman irishwomen ireland
iron
island islands islander islanders
italy italian italians italianate
j
jacked jacking jacks
jacket jackets
jam jams jamming jammed
january jan
japan japanese jap japs
joint joints jointly jointed disjointed
joke jokes joked joking joker jokers jokingly
journey journeys journeying journeyed
joy joyful joyfully joys joyless joyous joyousness joyously
juice juices juicy juicier juiciest juiciness juicily
july
junction junctions
june
justice justices
justify justifiable justifiably justification justifications justified justifies justifying unjustified unjustifiable unjustifiably
keen keener keenest keenly
kick kicks kicking kicked kicker kickers
knee knees
knife knives
knowledge knowledges knowledgeable
label labelled unlabelled labelling labels labeled labeling unlabeled
lack lacked lacking lacks
landlord landlords
lane lanes
leaflet leaflets
league leagues
lecture lectured lecturer lecturers lectures lecturing
legal illegal illegality illegally legality legally legalise legalising legalised legalisation legalize legalizing legalized legalization
lend lender lenders lending lends lent
length lengthening lengths lengthy lengthen lengthened lengthens lengthways
lesson lessons
liberal lib liberalise liberalism liberalisation liberalised liberalises liberalising liberalization liberalize liberalized liberalizes liberalizing liberally liberals
library librarian librarians libraries librarianship
licence licences license licensed licensing licenced licencing licenses unlicensed unlicenced licensee licensees
lift lifted lifting lifts lifter lifters
literal literally
loan loans
locate located locating location locations locational relocate relocated relocates relocating relocation
log logging logs logged loggings logger loggers
logic illogical illogically logical logically logician logicians
loose loosely loosen loosens loosened loosening loosenings
lorry lorries
loss losses
loud loudness loudly loudest louder
lump lumped lumping lumps lumpy lumpiness
ma mas
mad madness madly maddest madder madman madden maddens maddened maddening
madam madams
magazine magazines mag mags
mail mails mailing mailed
maintain maintained unmaintained maintaining maintains maintenance
male males maleness
manufacture manufactured manufacturing manufactures manufacturers manufacturer
map maps mapping mapped unmapped
march
margin marginal marginalise marginalised marginalising marginalisation marginalize marginalized marginalizing marginalization marginally margins marginality
marvel marvels marveled marveling marvelous marvelously marvelled marvelling marvellous marvellously
mass masses massed massing
massive massively
master masters mastered mastering masterly masterful mastery
mate mates mateship mated mating matings matey
material materialistic materialistically materially materials materialism materialisms materialist materialists materiality
mathematics mathematician mathematicians mathematical mathematically maths math
maximum maximums max
mayor mayors mayoress mayoresses
meal meals
meat meats meaty
medical medically
medicine medicines medicinal medicinally
memory memorial memories memorise memorised memorises memorising memorize memorized memorizes memorizing memorials
mental mentality mentally
mere merely merest
mess messy messier messiest messiness messily messes messed messing
message messages
metal metals metallic nonmetallic
method methodical methodological methodologically methodologies methodology methods methodically
metre metres meter meters metric metricize metricizes metricized metricizing metrical metrically metered metering
microphone microphones
mid
midland midlands
mill mills miller milled millers milling millings
miner miners mined mining mines
minimum minimums
minor minorities minority minors
mirror mirrors mirrored mirroring
mistake mistaking mistakes mistakenly mistaken unmistakably unmistakable
mix mixing mixes mixed mixer mixers
model models modelling modelled modeling modeled modeller modellers
modern modernise modernised modernising modernisation modernize modernized modernizing modernization modernity modernism modernisms modernist modernists
monitor monitored monitoring monitors unmonitored
moon moons moonlight moonlit
moral morals morally morality moralist moralists moralistic moralistically
mortgage mortgaged unmortgaged mortgaging mortgages mortgagee mortgagees
motor motorist motorists motors motored motoring motorise motorised motorises motorising motorisation motorize motorized motorizes motorizing motorization
motorway motorways
mountain mountains mountainside mountainous mountaineer mountaineers mountaineering
mouth mouthful mouths mouthed mouthing mouthings mouther mouthers
muck mucks mucked mucking mucky muckier muckiest
multiply multiplying multiplies multiplied multiplication multiplier multipliers
murder murders murdering murderers murderer murdered murderous murderously
muscle muscles
nail nails nailing nailed
narrow narrowed narrower narrowest narrowing narrowly narrowness narrows
nasty nastiness nastily nastier nastiest
naughty naughtier naughtiest naughtiness naughtily
neck necks necking necked
negative negatively negatives negativism negativity
negotiate negotiated negotiating negotiates negotiator negotiators negotiation negotiations
neighbour neighbor neighborhood neighborhoods neighbors neighbourhood neighbourhoods neighbouring neighboring neighbours
neither
nerve nerves
net nets netted netting nettings
nevertheless
newspaper newspapers
nick nicks nicked nicking
nil nils
noise noisy noisily noises
nor
northern northerner northerners
nose noses nosed nosing
nought noughts naught
november nov
nurse nursing nurses nursed
nursery nurseries
object objects
objected objecting objector objectors objection objections objectionable unobjectionable objectionably
oblige obliges obliged obliging obligation obligations obligatory obligatorily nonobligatory obligingly
observe observable observation observations observational observatory observed observer observers observes observing observant observantly nonobservant unobserved unobservant
obtain obtainable obtained obtaining obtains unobtainable
occupy occupancy occupant occupants occupied unoccupied occupier occupiers occupies occupying
occur occurred occurrence occurrences occurring occurs reoccur reoccurred reoccurring reoccurs
october oct
offence offences offense offenses offensive offensively inoffensive inoffensively offensiveness unoffensive inoffensiveness
official officially officialdom officials unofficial unofficially
oil oily oiliness oils oiled unoiled
op
opinion opinions opinionated
opposite opposites
option optional options
orange oranges orangish
ordinary ordinarily ordinariness
overall
owe owed owes owing
packet packets
pad pads padding padded
pain pains pained paining painful painfully painkiller painkillers painless painlessness painlessly
panel panelled panelling panels
parish parishes
parliament parliamentary parliaments parliamentarian parliamentarians
partner partners partnered partnering partnership partnerships
pat patting patted pats
patch patched patching patches
path paths
patient patiently patience
patients
pattern patterns patterned patterning
peace peaceful peacefully peaceable
pen pens
pencil pencils
penny pennies penniless
perform performs performing performer performers performed performance performances
permanent permanently impermanent impermanence permanence permanency permanences
permit permission permits permitted permitting permissible
persuade persuasion persuasions persuades persuaded persuading persuasive persuasively
petrol
physical physically
pie pies
pig pigs piggy piggies piglet piglets
pile piling piles piled
pin pins pinned unpinned pinning
pink pinks pinkness pinkest pinker pinkish pinky
pint pints
pipe pipes piped piping pipings
pit pitted pitting pits
pitch pitched pitches pitching pitcher pitchers
plain plainer plainest plainly
plane planes planed planing planer planers
plant planted unplanted planting plants planter planters
plastic plastics plasticity
plate plates plated plating
pleasure pleasures displeasure pleasurable pleasurably
plenty plentiful
plug plugging plugged plugs unplug unplugging unplugged unplugs
pocket pockets pocketed pocketing
poem poems
polish polishing polishes polished
poll polls polled polling pollings
pool pools pooling pooled
pop popped popping pops
popular popularity popularly unpopular unpopularity popularise popularised popularising popularisation popularisations populariser popularisers popularize popularized popularizing popularization popularizer popularizers popularizations
population populations populate populating populated populates
pot pots potted potting
potato potatoes
potential potentials potentiality potentialities potentially
pour pours pouring poured
practical practically practicable impractical impracticable impracticably practicality practicalities impracticality impracticalities
pray prays praying prayers prayer prayed
pre
precise imprecise precisely precision
prefer prefers preferring preferred unpreferred preferable preferably preference preferences preferential preferentially preferment preferments
pregnant pregnancy
pretend pretends pretending pretended pretence pretender pretenders
prevent prevented preventing prevention prevents preventable preventative unpreventable preventive
prime primes primed priming
principle principled principles unprincipled
priority priorities prioritisation prioritise prioritised prioritises prioritising prioritization prioritize prioritized prioritizes prioritizing
prison prisons prisoners prisoner imprison imprisoning imprisons imprisoned imprisonment imprisonments
prize prized prizes
pro pros semipro semipros
professional professionally professionals professionalism unprofessional
profit profited profiting profits profitable unprofitable profitability unprofitability profitably profitless
progress progressed progresses progressing progressive progressively progression progressions
promise promised promises promising unpromising
promote promoted promoter promoters promotes promoting promotion promotions promotional promo promos
property properties
proportion proportioned proportional proportionality proportionally proportionate proportionately proportions
prospect prospects prospecting prospected prospective prospector prospectors
proud proudly proudest prouder proudness
prove proved proven proves proving unproven
psychology psychological psychologically psychologist psychologists
pub pubs
publish published publisher publishers publishes publishing unpublished republish republished republishes republishing
pudding puddings
pump pumps pumping pumped
pupil pupils
purchase purchased purchaser purchasers purchases purchasing repurchase repurchased repurchaser repurchasers repurchases repurchasing
pure purest purer purely purity impure impurity impurities purist purists pureness
q
qualify qualifying qualifies qualified qualification qualifications unqualified qualifier qualifiers
queen queens queenly queene
quote quotation quotations quoted quotes quoting
race racecourse raced races racing racer racers
rain rains raining rained raindrops raindrop rainy rainier rainiest
rare rarest rarer rareness rarely rarity rarefied
ray rays
reach reached reaches reaching
react reacted reacts reacting reaction reactionaries reactionary reactions reactive reactivity reactor reactors reactant reactants
recall recalls recalled recalling
recession recessions recessional recessionary
recover recoverable irrecoverable recovered recovering recovers recovery
recruit recruited recruiting recruits recruitment recruiter recruiters
redundant redundancy redundancies redundantly
reflect reflects reflecting unreflecting reflected reflective reflectively reflectiveness reflection reflections reflectance
refrigerate refrigerated refrigerating refrigerates refrigeration refrigerations refrigerator refrigerators fridge fridges
refuse refusal refusals refused refuses refusing
register registered registering registers registration unregistered
regular regulars irregular regularly regularity irregularly irregularity irregularities
regulate regulated regulates regulating regulation regulations regulator regulators regulatory unregulated
reject rejected rejecting rejection rejects rejections
relative relatives relatively relativism relativist relativists
relax relaxation relaxed relaxes relaxing
release released releases releasing
relevant irrelevance irrelevant relevance
relief
religion religions
religious religiously
rely reliability unreliability reliable reliably reliance reliant relied relies relying unreliable
remain remained remaining remains
remark remarked remarking remarks remarkable remarkably unremarkable unremarkably
remind reminds reminding reminded reminder reminders
remove removable removal removals removed removes removing remover removers
rent renting rented rents rental rentals
repair repairs repairing repaired unrepaired repairer repairers
repeat repeated repeatedly repeating repeats repeater repeaters repetition repetitions repetitious
replace replacing replaces replaced replacement replacements replaceable irreplaceable
reply replied replies replying
request requests requesting requested
reserve reserves reservation reservations reserved reserving unreserved unreservedly reservist reservists
reside resided residence residences residency residencies resident residential residents resides residing
resist resists resisting resisted resistible resistance resistances resistant unresistant nonresistant resistor resistors
respond responded respondent respondents responding responds responder responders
response responses responsive responsiveness unresponsive
restrict restricted restricting restriction restrictions restrictive restrictively restricts unrestricted unrestrictive
retire retiring retires retired retirement
reverse reversal reversed reverses reversible reversing reversals irreversible
revise revised unrevised revises revising revision revisions revisionist revisionists revisionism revisionary
revolution revolutionary revolutionaries revolutionise revolutionised revolutionises revolutionising revolutionist revolutionists revolutionize revolutionized revolutionizes revolutionizing revolutions
rich richer richest richly richness riches
ride ridden rider riders rides riding rode
ridiculous ridiculously
risk risks risking risked risky riskiness
river rivers riverside
rob robs robbing robber robbed robbers robbery robberies
rock rocks rocky
rome roman romans
roof roofs roofing roofed rooftop rooftops
root roots rooting rooted rootless
rough roughly roughness rougher roughest
route routed routes routing
row rows rowing rowed rower rowers
royal royals royalty royalties royally
rub rubs rubbing rubbed
rubbish rubbished rubbishes rubbishing
rush rushed rushes rushing
russia russian russians
sack sacked sacking sacks
sad sadness sadly saddest sadder sadden saddened saddening saddens
sail sailed sailing sailings sails sailor sailors
sake sakes
salary salaried salaries
salt salty salted unsalted salts salting
sample sampling samples sampled
sand sandy sands sanding sanded sander sanders
sandwich sandwiched sandwiches sandwiching
satisfy satisfying satisfies satisfied satisfactory satisfaction satisfactorily unsatisfied unsatisfying unsatisfactory unsatisfactorily
scale scaled scales scaling scalings scalable
scare scares scared scaring scareder scaredest scary scarier scariest
scene scenery scenes scenic scenically
schedule scheduled scheduling schedules sch unscheduled nonscheduled reschedule rescheduled rescheduling reschedules
screen screens screening screened
screw screws screwed screwing unscrew unscrews unscrewed unscrewing
sea seaman seaside seamen seas
search searching searches searched searcher searchers
season seasons seasonal seasonally nonseasonal seasonality
seconds sec secs
secret secrecy secretly secrets secretive secretiveness secretively
seek seeking seeks sought unsought seeker seekers
select selected selecting selection selections selective selectively selector selectors selects selectivity selectivities
senior seniors seniority
sensible sensibly sensibility sensibilities
sentence sentences
september sept
series
session sessions
several
severe severity severest severer severeness severely
shake shaken shakes shakily shaking shaky shook unshakeable shaker shakers
shame shaming shames shameful shamefully shamed shameless shamelessly
shape shaped shapes shaping shapeless shapely shapelier shapeliest shapeliness unshapely misshape misshapen misshapes misshaping misshaped
sharp sharpness sharply sharpest sharper sharpens sharpening sharpened sharpen sharpener sharpeners
shed shedding sheds
sheep
shift shifted shifting shifts
ship ships shipping shipped shipments shipment shipper shippers
shirt shirts
shock shocks shocking shocked shockingly shocker shockers
shoulder shouldered shouldering shoulders
shout shouted shouting shouts
shower showers showering showered
sight sights unsightly sighted unsighted sighting sightings
signal signals signalling signalled signaling signalman
significant insignificant insignificantly significance significantly insignificance insignificances
silly sillier silliest silliness
sin sinned sinning sins sinner sinners
sink sunk sinks sinking sank sunken sinker sinkers
skill skilled skills skillful skilful skilfully unskilled unskilfully
skin skins skinning skinned
sky skies
slide slid slides sliding
slip slips slipping slipped slippage slippages
smart smarter smartest smartly smartness smarten smartens smartened smartening smarty
smash smashed unsmashed smashes smashing
smell smelt smells smelling smelled smelly smelliness
smile smiled smiles smiling unsmiling
snow snows snowed snowing snowy snowier snowiest snowiness
sock socks
sod sods
soft soften softened softening softens softer softest softly softness
solicitor solicitors
solid solidify solidified solidifies solidifying solidly solids solidity solidities
solution solutions
solve solving solves solved unsolved unsolvable
song songs
source sourced unsourced sources sourcing
southern southerner southerners
spain spanish
spare sparing spares spared sparingly
speech speeches speechless
spirit spirits spiritual spiritually spirituality
split splitting splits
sponsor sponsored sponsoring sponsors sponsorship
sport sporting sports sporty
spot spots spotted spotting spotless spotlessness spotlessly spotty spottier spottiest spottiness spottily spotter spotters
spread spreading spreads
spring sprang springing springs sprung
stable instability stabilisation stabilise stabilised stabilises stabilising stabilization stabilize stabilized stabilizes stabilizing stability unstable stabiliser stabilisers stabilizer stabilizers
stall stalls stalled stalling
stamp stamps stamping stamped unstamped
star starred stars starring stardom starry
states interstate
status
steel steely
stock stocks stocked
stone stoned stones stoning stony
store stored stores storing storage
strange strangely strangeness stranger strangers strangest
strength strengthen strengthened strengthening strengthens strengths
stress stressed stresses stressful stressing unstressed
stretch stretched unstretched stretches stretching stretchy stretchiness
strip strips stripped stripping stripper strippers
struggle struggled struggles struggling
style styled styles styling stylish stylise stylised stylises stylising stylize stylized stylizes stylizing stylist stylists stylistic stylistically stylistics
sub
substantial substantially
sue sued sues suing
suffer suffered suffering sufferings suffers sufferer sufferers
sufficient sufficiency insufficiency insufficient insufficiently sufficiently
sugar sugars sugared sugary
sum summation summed summing sums
super
surface surfaced surfaces surfacing
survey surveyed unsurveyed surveying surveys surveyor surveyors
survive survival survived survives surviving survivor survivors
suspect suspects suspecting suspected unsuspected unsuspecting
swear sworn swore swears swearing
sweet sweeter sweetest sweetness sweetly sweets sweeten sweetens sweetened sweetening sweetener sweeteners unsweetened sweetie sweeties
swim swum swims swimming swam swimmer swimmers
tablet tablets
tackle tackled tackles tackling
tail tails tailed tailing tailings
tall tallest taller tallness
tank tanks tankful antitank
tap taps tapping tapped untapped
target targeted targeting targets
taste tasted tastes tasting tasty tastier tastiest tasteful tastefulness tastefully tasteless tastelessness tastelessly taster tasters
tear tearing tears tore torn
technical technically
technique techniques
technology technologies tech technological technologically technologist technologists
temperature temperatures
temporary temporarily temp temps
text texts textual
theatre theatres theater theaters theatrical theatrically
theory theoretical theoretically theories theorist theorists
thick thickness thicknesses thickly thickest thicker thicken thickens thickened thickening thickener thickeners
thin thins thinning thinnest thinness thinner thinned thinly
threat threats threatens threatening threateningly threatened threaten
tick ticks ticked ticking ticker tickers
ticket tickets
tidy tidier tidiest tidiness untidy untidier untidiest untidiness untidily tidily tidied tidying tidies
tight tighter tightest tightly tightness tightens tightening tightened tighten tights
tile tiles tiling tiled
tin tins tinny tinned tinful tinfuls
tiny tinier tiniest tininess
tip tips tipping tipped
tire tiring tires tired tiredly tiredness tireless tirelessness tirelessly
title titled titles titling untitled
toilet toilets
ton tons tonne tonnes tonnage tonnages
tool tools
tooth teeth toothless toothy teething teethed teethes teethings toothed
topic topical topics
tory tories
tough toughness toughest tougher
tour tours touring toured tourist tourists tourism
tower towers towering towered
toy toys toyed toying
track tracks tracking tracked tracker trackers trackless
tradition traditional traditionalist traditionally traditions
transfer transferable transferability transference transferred transferring transfers transferral transferrals transferor transferors transferer transferee transferees transferers
treasure treasuring treasures treasured treasury treasurer
tremendous tremendously
trial trials trialing trialed
trick tricks tricked tricking tricky trickier trickiest trickiness trickily trickery trickeries
trip trips tripping tripped
trousers trouser
tune tuning tunes tuned tuneless tuneful tunelessly tunefully tuner tuners
typical typically untypical untypically
ultimate ultimately
un
update updates updated updating
upset upsetting upsets
valid invalidate invalidity validate validated validating validation validity validly invalid
van vans
variety varieties
vary invariable invariably variability variable variables variably variance variant variants variation variations varied varies varying
vast vastly vastness
vegetable vegetables veg vegs veggies
vehicle vehicles
verse verses versed
version versions
victim victims victimize victimized victimizing victimization victimise victimised victimising victimisation
violent violently violence nonviolent
virtual virtually
voice voiced voices voicing voiceless
volume volumes vol vols
voluntary voluntarily
volunteer volunteering volunteered volunteers
wake woke waking wakes waken woken wakeful wakefulness
wales welsh welshman welshmen
ward wards wardship wardships
warn warned warning warnings warningly warns
wave waved waves waving
weak weaker weakest weakly weakness weaknesses weaken weakens weakening weakened
weather weathers weathering weathered
wed wedding weddings wedded weds unwed unwedded unweds
weird weirder weirdest weirdness weirdly
western westerner westerners westerns
wet wetting wets wetted wetness wetly wetter wettest
wheel wheels wheeler wheeled wheeling
whereas
wine wining wines wined
wing wings winging winged
winter winters wintry midwinter wintered wintering
wipe wiping wipes wiped unwiped wiper wipers
wire wires wired wiring wirings
wise unwise unwisely wisdom wisely wiseness wiser wisest
withdraw withdrawal withdrawals withdrawing withdraws withdrew withdrawn
witness witnessing witnesses witnessed unwitnessed
wrap wrapping wraps wrapper wrappers wrapped unwrap unwrapped unwraps unwrapping
yard yards yd yds
yellow yellowish yellowness yellowed yellowing yellows yellower yellowest
youth youths youthful youthfully
zero zeros''')


base3unsplit = ('''
abbey abbeys
abroad
absence absences
accelerate accelerated accelerates accelerating accelerator accelerators acceleration accelerations
accordingly
accountant accountants accountancy
accuse accusing accusingly accuses accused accusation accusations accuser accusers
ache aches ached aching achy
adapt adapted unadapted adapting adapts adaptation adaptations adaptable adapter adapters adaptor adaptors adaptability adaptabilities adaptive
addict addicts addicted addicting addictive addiction addictions nonaddictive
admire admiring admires admired admirable admirably admiration admirer admirers admiringly
adventure adventures adventurer adventurers adventurous misadventure misadventures
aerial aerials aerially aerialist aerialists
aeroplane aeroplanes aero
affection affections affectionate affectionately affective affectively
aggressive aggressively aggressiveness aggressivenesses aggro
airline airlines airliner airliners
album albums
alcohol alcoholic alcoholics alcoholism
alert alerts alerted alerting alertly
alley alleys alleyway alleyways
almighty
alongside
aluminium aluminum
ambulance ambulances ambulanceman ambulancemen
amuse amuses amused unamused amusing amusingly amusement amusements
ancient
anger angers angering angered
angry angrily angrier angriest
anniversary anniversaries
anonymous anonymously
apartment apartments
appal appalled appalling appals appallingly
appliance appliances
approximate approximated approximately approximates approximating approximation approximations approx
arrears
arrest arrests arresting arrested arrestable
arrow arrows
artificial artificially artificiality
ashamed unashamed unashamedly ashamedly
asia asian asians asiatic
aside
astonish astonishes astonished astonishing astonishment astonishments astonishingly
atmosphere atmospheric atmospheres
author authored authoring authorial authors authorship
authorise authorises authorised unauthorised authorising authorisation authorize authorizes authorized unauthorized authorizing authorization
autumn autumns autumnal
avenue avenues
awake awaken awoken awakens awakened awakening awakes awoke
backside backsides
badge badges
ban banned banning bans
banana bananas
bare baring bares bared barely bareness
bargain bargains bargaining bargained
bark barks barked barking
barn barns
barrel barrels
barrier barriers
basement basements
bash bashes bashed bashing
basket baskets basketful basketsful
bat batted batting bats batter batters
beach beaches beachfront
beam beams beamed beaming
beef beefy
beforehand
behave behaves behaved behaving
belief beliefs
bench benches bencher benchers
bible bibles
bicycle bicycling bicycles bicycled
bingo
bishop bishops archbishop archbishops archbishopship bishopship
bitter bitterness bitterly bitterest bitterer
blade blades
blanket blanketed blanketing blankets
blimey
bog bogged bogging bogs boggy
bold boldness boldly boldest bolder
bolt bolted bolting bolter bolters bolts
bond bonded bonding bonds
boo booed booing boos
boom boomed booming booms
boost boosts boosted boosting booster boosters
border borders bordering bordered
borough boroughs
bounce bounces bounced bouncing bouncer bouncers bouncy bouncier bounciest bounciness bouncily
bow bows bowing bowed unbowed
boxed boxing boxer boxers
boyfriend boyfriends
brake braked braking brakes
brand brands branded branding
brass brassy
brave braving braves bravely braved bravery braveness braver bravest
breakdown breakdowns
breast breasts breasted breasting
breath breaths breathlessly breathless breathy
breathe breathing breathes breathed unbreathing breathable unbreathable
breed bred breeding breeder breeders breeds
buck bucked bucking bucks
bucket buckets bucketful bucketsful
bug bugged bugging bugs
bulk bulky
bull bulls bullish
bully bullied bullies bullying
bump bumps bumped bumping bumper bumpers
bunch bunched bunching bunches
burden burdened burdening burdens unburdened unburden unburdening unburdens
burgle burgles burgled burgling burglar burglars burglary burglaries burglarize burglarizes burglarized burglarizing
burst bursts bursting
bury burying buries buried burial burials
bush bushes bushy
bust busts busty bustier bustiest
butcher butchers butchered butchering butchery
buzz buzzed buzzes buzzing buzzy buzzer buzzers
bypass bypassed bypassing bypasses
cable cabled cables cabling cablings cabler cablers
calendar calendars
camel camels
canada canadian canadians
canal canals
cancer cancerous cancers
candle candles
cans canned canning
canteen canteens
cap caps cappings capping capped
captain captains captained captaining capt capts captaincy captaincies
capture captured capturing captures uncaptured
cardboard
carol carols caroled caroling
cart carts carted carting carter carters
cassette cassettes
castle castles
casual casually casualness
casualty casualties
catalogue catalogues catalogued cataloguing catalog catalogs
cater catered catering caters caterer caterers
cathedral cathedrals
catholic catholics catholicism
ceiling ceilings
certificate certificates certificated uncertificated
chamber chambers
champion champions championship championships championed championing champ champs
chapel chapels
charm charms charming charmed charmless charmingly charmer charmers
chart charted charting charts uncharted
cheat cheats cheated cheating cheater cheaters
cheek cheeks
cheerio cheerios
chemist chemists
chew chews chewed chewing chewer chewers chewy chewier chewiest
chimney chimneys
choke chokes choked choking choker chokers
chunk chunks chunky chunkier chunkiest chunkiness
cinema cinemas cinematic
circuit circuits circuitous
civilise civilised civilising civilises civilize civilized civilizing civilizes civilisation civilisations civilization civilizations uncivilized uncivilised
clap clapping clapped claps
clash clashes clashed clashing
classic classical classics classically classicism classicist classicists
click clicks clicked clicking clicker clickers
cliff cliffs
climate climates climatic climatically
clinic clinics clinical clinically nonclinical clinician clinicians
clip clipping clippings clipped clips clipper clippers
cloth cloths
clutch clutches clutched clutching
cock cocks cocked cocking cocky cockier cockiest cockiness cockily
coin coins coined coining coinage coinages
coincide coincided coincides coinciding coincidence coincidences coincident coincidental coincidentally
collapse collapsed collapses collapsible collapsing
collar collars collarless
column columns col cols columnar
comedy comedies
compact compactly compactness compacts compacting compacted compaction
compile compilation compilations compiled compiles compiling compiler compilers
compliment complimented complimenting compliments complimentary
comprehensive comprehensively comprehensiveness comp comps
compromise compromised compromises compromising uncompromising uncompromisingly
conceive conceivable conceivably conceived conceives conceiving inconceivable inconceivably
concert concerts
concrete concretely
condense condensation condensations condenses condensed condensing condenser condensers
confess confessing confesses confessed confession confessions confessor confessors confessional
confidential confidentiality confidentially
congratulate congratulates congratulated congratulating congratulatory congratulation congratulations
congregate congregates congregated congregating congregation congregations congregational congregationalism congregationalist congregationalists
consequent consequently
contest contests contested contesting contestable incontestable contestant contestants
continent continents continental
contrast contrasted contrasting contrastive contrasts
convenience conveniences convenient conveniently inconvenient
convention conventional conventionally conventions unconventional unconventionally
convert converted unconverted convertible convertibility converting converts converter converters
convey conveyance conveyed conveyer conveyers conveying conveys conveyor conveyors conveyancing conveyancings
coordinate coordinating coordinated coordinates coordination coordinator coordinators uncoordinated
cop cops
cord cords cordless
core cores coring cored
correspond corresponded correspondence corresponding correspondingly corresponds
corridor corridors
cotton
courage courageous courageously
cousin cousins
cracker crackers
craft crafts crafty craftiness craftier craftiest craftily crafted crafting
crash crashing crashes crashed
crawl crawled crawling crawls
crazy crazier craziest crazily craziness
creep crept creeps creeping creepy creeper creepers
cricket cricketer cricketers cricketing cricketed
criticism criticisms
crop crops cropping cropped cropper croppers
crown crowns crowned crowning uncrowned
crucial crucially
cruel cruelly cruelness cruellest crueller cruelty cruelties
crush crushing crushes crushed
crystal crystals crystallise crystallised crystallising crystallises crystallize crystallized crystallizes crystallizing crystallization crystallisation
cube cubes cubic cu
cure curing cures cured curable incurable curative
curious curiously curiosity
curl curls curly curlier curliest curliness curled curling curler curlers uncurl uncurls uncurled uncurling
cushion cushioned cushioning cushions
custom customs customary customarily
cylinder cylinders
daft dafter daftest daftness daftly
damp dampness dampest damper dampen dampens dampened dampening dampener dampeners damping damps damped
dash dashes dashed dashing dasher dashers
deaf deafer deafest deafness deafen deafens deafened deafening deafeningly
deduct deducted deducting deducts deduction deductions deductible deductibility deductive deductively
deed deeds
deliberate deliberately
delicate delicately delicacy delicacies
denmark dane danes danish
derby derbies
desert deserted deserting deserts deserter deserters desertion desertions
deserve deserving deserves deservedly deserved undeserved
detach detaches detached detaching detachable nondetachable detachment detachments
deteriorate deteriorates deteriorated deteriorating deterioration deteriorations
devil devils devilish devilishly devilishness
devote devoted devotedly devotes devoting devotion devotions devotional devotee devotees
dial dials dialed dialing dialled dialling
dialect dialects dialectal
dictate dictated dictates dictating dictation dictator dictators dictatorial dictatorially dictatorship dictatorships
digest digests digested undigested digesting digestion digestive digestives digestible indigestible
dimension dimensional dimensions
dine dined dines dining diner diners
dinosaur dinosaurs
dip dips dipping dipped dipper dippers
discipline disciplined undisciplined disciplining disciplines disciplinary disciplinarian interdisciplinary indiscipline
discriminate indiscriminate discriminates discriminated discriminating discriminatory nondiscriminatory indiscriminately discrimination discriminations
disgrace disgraces disgracing disgraced disgraceful disgracefulness disgracefully
dispose disposable disposal disposed disposes disposing
distress distressed distresses distressing
disturb disturbs disturbing disturbed undisturbed disturbance disturbances disturbingly
ditch ditches ditched ditching
dive diving dives dived dove diver divers
divorce divorced divorces divorcing divorcee divorcees
dodgy dodgier dodgiest
dole doled doling doles
dominate dominated dominates dominating domination
donate donated donates donating donation donations
doorstep doorsteps
dose doses dosed dosing dosings dosage dosages
drain drained draining drains
draught draughts draughty draughtier draughtiest
dread dreads dreaded dreading
dreadful dreadfully
drift drifted drifting drifts drifter drifters
drill drilled drilling drills driller drillers
drip dripping dripped drips
drown drowns drowning drowned
drum drums drumming drummed drummer drummers
dual duality
duke dukes dukedom dukedoms
dull dullness dullest duller dully dulled dulls dulling
dummy dummies
dutch dutchman dutchmen
dye dyed dyeing dyer dyers dyes
ease easing eases eased unease uneasily uneasy uneasiness
eastern easterner easterners
echo echoed echoes echoing
egypt egyptian egyptians
elbow elbows
eldest
electronic electronics electronically
empire empires
enemy enemies
enthusiasm enthusiasms
enthusiastic enthusiastically unenthusiastic unenthusiastically
envelope enveloped enveloping envelopes envelop envelops enveloper envelopers envelopment envelopments
equivalent equivalents equivalently equivalence equivalences
error errors
escort escorted unescorted escorting escorts
essay essays
eve eves
evil eviler evilest evilly evilness evils
exaggerate exaggerates exaggerated exaggerating exaggeration exaggerations
exhaust exhausted exhaustible exhausting exhausts inexhaustible
exit exits exited exiting
explode explodes exploded exploding
export exports exporting exported exporter exporters
expose exposed unexposed exposes exposing exposure exposures
external externalisation externalise externalised externalises externalising externality externalization externalize externalized externalizes externalizing externally
extract extracted extracting extraction extractions extracts extractor extractors
fade fading unfading fades faded unfaded
failure failures
faint faints faintly fainting fainter faintest fainted faintness
false falsely falsehood falseness falsity
fare fares fared faring
fascinate fascinated fascinates fascinating fascination
fatal fatality fatalities fatally fatalist fatalists fatalistic fatalistically fatalism
fax faxed faxes faxing
feather feathers featherless feathery feathered feathering
feedback feedbacks
felled fells felling feller fellers
fertile infertile fertility infertility fertilise fertilize fertilised fertilized fertilises fertilizes fertilizing fertilising fertiliser fertilisers fertilizer fertilizers fertilisation fertilization
fiction fictional nonfiction
fiddle fiddles fiddled fiddling fiddler fiddlers
fierce fiercest fiercer fierceness fiercely
filter filtered unfiltered filtering filters filtrate filtrated filtrating filtration filtrations
fined fines fining finings unfined
fir firs
flag flags
flame flames flaming flamed
flap flapping flapped flaps
flare flares flared flaring
flash flashing flashes flashed
flavour flavours flavouring flavoured flavor flavors flavoring flavored
flight flights flightless flt flighty
flood floods flooding flooded
flu flus influenza influenzas
fold folds folding folded unfold unfolds unfolded unfolding
folder folders
fond fondness fondly fondest fonder
ford fords
forecast forecasted forecasting forecaster forecasters forecasts
foresee foreseeing foresaw foreseen foresees foreseer foreseers foreseeable unforeseeable unforeseen
forever
fork forked forking forks
format formatted formatting formats
foster fostered fostering fosters
foundation foundations
founded founding unfounded founder founders
framework frameworks
frequent frequents frequently frequenting frequented frequency frequencies infrequent infrequently
fringe fringes fringed fringing
frost frosts frosted frosting frosty frostier frostiest frostiness frostily
frustrate frustrated frustrates frustration frustrations frustrating
fry fries fried frying fryer fryers
fume fumed fumes fuming
funeral funerals
fur furs furry furrier furriest furriness
furnish furnished unfurnished furnishes furnishing furnishings
fuss fusses fussy fussier fussiest fussiness fussily fussed fussing fusser
gallery galleries
gallon gallons
gamble gambled gambler gamblers gambling gamblings
gang gangs
gee
generous generously generosity
gentle gently gentleness gentler gentlest
genuine genuinely
geography geographical geographic geographically geographies geographer geographers
gesture gestured gestures gesturing
ghost ghosts ghostly
giant giants
glance glanced glances glancing
glaze glazes glazed unglazed glazing glazings
global globally globalism globalist globalists globalize globalizes globalized globalizing globalise globalisation globalization globalises globalised globalising
glory glories glorious gloriously glorify glorifies glorified glorifying glorification glorifications
glove gloves gloved
glow glowed glows glowing glowingly
glue glues glued gluing gluey
gospel gospels
gracious graciousness ungracious ungraciously graciously
grain grains grainy
gram grams gramme grammes milligram milligrams milligramme milligrammes mg mgs centigram centigrams centigramme centigrammes
grammar grammars grammarian grammarians
graphic graphically graphical graphics
greece greek greeks grecian grecians
greed greeds greedy greedier greediest greediness greedily
greet greetings greets greeting greeted
grief
grind grinds grinding grinder grinders
grip gripped gripping grips
gross grossly
guest guests
gut gutted gutting guts gutless gutlessness gutsy gutsier gutsiest
habit habits
hairdresser hairdressers
ham hams
hammer hammers hammering hammered
handicap handicapping handicapper handicappers handicapped handicaps
handy handier handiest handiness unhandy unhandier unhandiest handily
harass harasses harassed harassing harasser harassers harassment harassments
hardware
harry harries harried harrying
harvest harvests harvesting harvester harvested
hassle hassles
hay hays
headache headaches
headline headlines
headmaster headmasters
heal heals healed healing healings healer healers
heather heathers
heck
hedge hedges
heel heels
height heights
helicopter helicopters
hen hens
hero heroes heroic heroics heroically heroism
hesitate hesitating unhesitating hesitatingly unhesitatingly hesitates hesitated hesitation hesitations
hint hinted hinting hints
hip hips
hobby hobbies hobbyist hobbyists
hockey hockeys
holland
honey honeys
hood hooded hoods
hooray hurray hurrah hurrahs
hop hops hopped hopping
horrendous horrendously
horror horrors
host hosts hosting hosted
housewife housewives housewifely
humour humourous humourously humorously humor humorous humourless humorless humourlessly humorlessly
hut huts
identical identically
idiot idiots idiotic idiotically idiocy idiocies
idle idleness idly idling idled idles idlest idler
illustrate illustrated unillustrated illustrates illustrating illustration illustrations illustrative illustrator illustrators
immense immensely immensity immenseness
incentive incentives
incidental incidentally
incline inclination inclinations inclined inclines inclining
incorporate incorporated unincorporated incorporates incorporating incorporation incorporations inc
index indexed indexes indexing indices indexation
indulge indulged indulges indulging indulgent indulgently indulgence indulgences
infect infected uninfected infects infecting infection infections infectious infectiousness infectiously noninfectious infective
inherit inheritance inherited inheriting inherits inheritor inheritors
inject injected injecting injection injections injects injector injectors
inn inns
insist insistent insistently insisted insisting insists
inspire inspired inspires inspiring inspiration inspirations inspirational uninspired uninspiring
install installation installations installed installing installs installer installers
instant instants instantly instantaneous instantaneously
instrument instruments instrumental instrumentation
insult insults insulted insulting
intellectual intellectualise intellectualize intellectually intellectuals
intense intensely intenseness intensification intensified intensifies intensify intensifying intensity intensities intensive intensively
inter
interfere interfering interferes interfered interference
interrupt interrupts interrupting interrupted uninterrupted interruption interruptions
interval intervals
intrigue intrigues intrigued intriguing intriguingly
invent invents invented inventing inventor inventors invention inventions
ironed irons ironing ironings
irony ironies ironic ironically ironical
irritate irritates irritated irritating irritation irritations
isle isles
jar jars jarful
jaw jaws
jeans
jewel jewels jewelled jewellers jeweller
jewellery jewelry jewelery
jog jogging jogged jogs jogger joggers
jolly jolliness jollity
jug jugs jugful
junior juniors jr jnr
kettle kettles
kidding kidded kidder kidders
kidney kidneys
kit kits
knot knotted knotting knots knotty knottier knottiest
laboratory laboratories lab labs
ladder ladders
lake lakes
lamb lambs lambed lambing
lamp lamps
landscape landscaped landscapes landscaping landscaper landscapers
lap laps
lawn lawns
layer layered layering layers
layout layouts
lazy lazier laziest laziness lazily
leaf leafy leafless leafed
leak leaks leaked leaking leakage leakages leaky leakier leakiest leakiness
lean leans leaning leanings leaned leant
leap leaping leaps leapt leaped
leisure leisurely
lever levered levering levers leverage leverages leveraged leveraging
liable liability liabilities
lid lids
likeness unlike
lip lips
liquid liquids liquidity liquidities
literature literatures
litre litres liter liters millilitre millilitres milliliter milliliters mil mils mll mlls
litter litters littered littering litterer litterers
lodge lodged lodging lodges lodgings lodger lodgers
loft lofts
lone lonely loneliness loner loners lonesome
loo loos
loop loops
lounge lounged lounging lounges
lunchtime lunchtimes
lung lungs
luxury luxuries luxurious luxuriously luxuriant luxuriantly luxuriance
magic magical magically
magnet magnets magnetize magnetizes magnetized magnetizing magnetization magnetise magnetises magnetised magnetising magnetism magnetic nonmagnetic magnetically
manner manners mannered
manoeuvre manoeuvred manoeuvring manoeuvres manoeuverable unmanoeuverable manoeuver manoeuvered manoeuvering manoeuvers
manor manors manorial
manual manually manuals
mar marring marred mars
marched marches marching marcher marchers
mask masked unmask unmasking unmasks unmasked masking masks
mature immature immaturity maturation maturational matured matures maturing maturity maturely immaturely
meantime
meanwhile
mechanic mechanics mechanical mechanically
medium
melt melts melting melted
mend mends mended unmended mending mender menders
menu menus
merchant merchants merchantable
merit merited unmerited meriting merits
merry merrier merriest merriness merrily merriment
micro
mild mildness mildly mildest milder
military militarily militarist militarists militarism
millimetre millimetres millimeter millimeters
mini
miracle miracles
miserable miserably
misery miseries
mission missions missionary missionaries
mixture mixtures
moan moans moaned moaning moaner moaners
mobile mobility mobilities immobile immobility
mock mocking mocked mocks mocker mockers mockingly
monopoly monopolies monopolise monopolises monopolised monopolising monopolisation monopolize monopolizes monopolized monopolizing monopolization monopolistic monopolist monopolists
monster monsters monstrous monstrously monstrosity monstrosities
mood moods moody moodiness moodily
moor moors
mortal mortals mortally mortality mortalities immortal immortally immortality immortalities immortalize immortalizes immortalized immortalizing immortalise immortalises immortalised immortalising
motive motivate motivated motivates motivating motivation motivational motivations motives unmotivated motivator motivators
motorbike motorbikes
mount mt mounts mounted mounting
mouse mice
movie movies
mud muddy muddied
mug mugs mugful
multi
multiple multiples
museum museums
mystery mysteries mysterious mysteriously
naive naively naivety naiveties
naked nakedness
nay
neat neatness neatly neatest neater
necessity necessities
needle needling needles needled
neglect neglects neglecting neglected
nervous nervously nervousness
nest nests nesting nested
neutral neutralisation neutralise neutralised neutralises neutralising neutrality neutralization neutralize neutralized neutralizes neutralizing
niece nieces
nightmare nightmares nightmarish
nip nipping nipped nips
nod nodding nodded nods
nonsense nonsensical
norm norms
nowt
nuclear
nuisance nuisances
numerous
nut nuts
oak oaken oaks
obscure obscurely obscured obscures obscuring obscurity obscurities
occupation occupational occupations
offend offends offended offending offender offenders
onwards onward
oral orally
orchestra orchestras orchestral
organ organs
orient orients oriented orienting orientate orientated orientates orientation reorient reorients reorienting reoriented reorientation orientations
origin origins originate originates originated originating originator originators
outcome outcomes
outrage outrages outraged outrageous outrageously outraging
oven ovens
overcome overcoming overcomes overcame
overhead overheads
overnight
overtake overtook overtakes overtaking overtaken
overtime overtimes
pace pacing paced paces
paddy paddies
pal pals
pale paling pales paled paleness
palm palms
pan pans
panic panicked panicking panics panick panicky panickier panickiest
paperwork paperworks
par pars
parade paraded parading parades
parcel parcels parcelled
paris parisian
passage passages
passenger passengers
passion passionate passionately passions
pathetic pathetically
pause pausing pauses paused
pave paved unpaved paves paving pavement pavements
peak peaks peaked peaking
peculiar peculiarly peculiarity peculiarities
penalty penalties
perception perceptions
personality personalities
pet pets
phase phased phases phasing
phenomenon phenomena phenomenal
photocopy photocopied photocopying photocopies photocopier photocopiers
piano pianos pianist pianists
pigeon pigeons
pilot pilots piloted piloting
pinch pinches pinched pinching
pity pitying pitiful pitiless pitilessly pitifully pities pitied unpitied
plaster plastered plasters plastering
platform platforms
plonk plonks plonked plonking plonker plonkers
plot plotted plotting plots plotter plotters
plough ploughs ploughed ploughing ploughman ploughmen plowed plowing plows
plumb plumbs plumbed plumbing plumber plumbers
poison poisons poisonous poisoning poisoned poisoner poisoners
poke pokes poked poking poker pokers
pole poles
polite politely politest politer politeness politenesses
pollute pollutes polluted polluting polluter polluters pollutant pollutants pollution pollutions antipollution
pond ponds
port ports
portion portions
pose posed poses posing poser posers
posh posher poshest
possess possessed possesses possessing possessive possession possessions possessor possessors repossess repossesses repossessed repossessing repossession repossessions
postcard postcards
potter potters pottered pottering
powder powders powdered powdery
praise praises praised praising
preach preaching preaches preachers preacher preached
precede preceded precedence precedent precedents precedes preceding unprecedented
predict predictability predictable predictably predicted predicting prediction predictions predicts unpredictability unpredictable predictive predictor predictors
premise premises
prescription prescriptions
pride prides
prince princes princely princelier princeliest princeliness
princess princesses
principal principally principals
privilege privileged privileges
prominent prominently
prompt prompts promptly prompting prompted
pronounce pronouncing pronounces pronounced
proof proofs
punch punched punches punching
punish punishable nonpunishable punishing punishes punished punishment punishments
purple purplish
purse purses pursed pursing
puzzle puzzles puzzled puzzling puzzler puzzlers puzzlement puzzlements
quantity quantities quantitative quantitatively
query queried querying queries
questionnaire questionnaires
queue queues queued queuing
rabbit rabbits
racist racists racism
rack racks racked racking rackings
rag rags raggy
random randomly randomness randomise randomises randomised ranomising randomisation randomisations randomize randomizes randomized randomizing randomization randomizations
rank ranked ranking ranks
rat rats ratty
rattle rattles rattled rattling rattler rattlers
raw rawness rawest rawer
rear reared rearing rears
rebel rebels rebelled rebelling rebellings rebellion rebellions rebellious rebelliousness rebelliously
receipt receipts
reception receptions receptionist receptionists
recipe recipes
referee refereed refereeing referees
refresh refreshes refreshed refreshing refreshingly refreshment refreshments refresher refreshers
regret regretting regretful regretted regrets regrettable regrettably regretfully
rehearse rehearses rehearsed rehearsing rehearsal rehearsals
relieve relieving relieves relieved
remote remotely remoteness remoter remotest
reproduce reproduces reproducing reproduced reproduction reproductions reproducible
reputation reputations
rescue rescued rescuer rescuers rescues rescuing
resign resigns resigning resigned resignedly resignation resignations
resort resorts resorted resorting
restaurant restaurants
restore restoration restorations restored unrestored restores restoring restorer restorers restorative
retail retailer retailers retails retailed retailing
reveal revealed unrevealed revealing reveals revelation revelations
revolt revolted revolting revolts
reward rewarded unrewarded unrewarding rewarding rewards
rhyme rhyming unrhyming rhymed rhymes
rhythm rhythms rhythmic rhythmical rhythmically
ribbon ribbons
rip ripped ripping rips
rocket rockets rocketed rocketing
rope ropes roping roped
roses rosy rosier rosiest rosiness rosily
rot rotting rotted rots
rotate rotates rotated rotating rotatory rotation rotations rotational
rotten rottener rottenest rottenness rottenly
routine routinely routines subroutine subroutines
rove roving roved roves rover rovers
rubber rubbers rubbery
rude rudeness rudely ruder rudest
rugby
ruin ruins ruinous ruinously ruined ruining ruination
rumour rumoured rumours rumor rumors rumored rumoring rumouring
sacrifice sacrificing sacrifices sacrificed sacrificial
saint saintly saints
salvation
satellite satellites
sausage sausages
scan scanned scanning scans scanner scanners
scope
scout scouts
scrap scrapped scrapping scraps
scrape scrapes scraped scraping scraper scrapers
scratch scratching scratches scratched unscratched scratchy scratchiness
scream screamed screaming screams
scribble scribbles scribbled scribbling scribbler scribblers
script scripts unscripted
scrub scrubbing scrubbed scrubs
seal sealed unsealed sealing seals sealant sealants
seed seeds seeding seeded seedling seedlings
seldom
semi
sensitive sensitivity sensitivities insensitivity insensitive sensitively
sergeant sergeants sgt sgts serjeant serjeants sarge
sew sews sewed sewing sewn unsewn
shade shaded shading shadings shady shadiness shades
shadow shadowed shadowing shadows shadowy
shave shaves shaved shaving shaver shavers shaven unshaven
sheer sheerness
shelf shelves
shell shells shelling shelled unshelled
shelter shelters sheltering sheltered unsheltered
shield shields shielding shielded unshielded
shine shined shines shining shone shiny
shore shores shoreline
shove shoves shoved shoving
shovel shovels shovelful shovelling shovelled
shy shyly shyness
signature signatures
silence silenced unsilenced silences silencing silent silently silencer silencers
silk silks silky silkiness silkier silkiest silkily silken
silver silvery
sincere sincerely sincerity
sixpence sixpences
sketch sketched sketches sketching
skip skipping skipped skips
slap slapping slapped slaps
slash slashes slashed slashing slasher slashers
slave slaves slavery
sleeve sleeves sleeveless
slice sliced unsliced slices slicing
slim slimmed slims slimming slimmings slimmer slimmers slimmest slimly slimness
slot slots slotting slotted
smack smacks smacked smacking smacker smackers
smooth smooths smoothly smoothing smoothed smoothness smoothnesses smoother smoothest
snap snapped snaps snapping snapper snappers
sneak sneaks sneaked sneaking sneaker sneakers sneaky sneakiness sneakily
sniff sniffs sniffed sniffing sniffer sniffers
soak soaks soaked soaking
socialist socialists
soil soils
soldier soldiers
sole solely
somewhat
sophisticated unsophisticated
sore soreness sorely sores sorer sorest
soul souls soulful soulfully soulless soullessly
soup soups soupy
spark sparks sparked sparking
species sp spp
spectacle spectacles spec specs
speculate speculated speculates speculating speculation speculations speculator speculators speculative speculatively
spill spills spilling spilled spilt unspilt spillage spillages
spin spun spins spinning
spit spits spitting spat spitter spitters
spite spiteful spitefulness spitefully
splash splashes splashed splashing
splendid splendidly
spoil spoils spoiling spoiled spoilt unspoilt unspoiled
spoon spooned spooning spoons spoonful
spray sprays sprayed spraying sprayer sprayers
squash squashed squashing squashes squashy squashier squashiest
squeeze squeezed squeezes squeezing
stab stabbing stabbed stabs
stack stacks stacked unstacked stacking
stain stains stained staining stainless
stake staked stakes staking
stare stared stares staring
starve starves starved starving starvation
steady unsteady unsteadily steadying steadily steadies steadied steadier steadiest steadiness
steal stole stolen steals stealing stealer stealers
steam steaming steams steamed steamy
steep steepness steepest steeper steeply
steer steers steering steered
sticky stickier stickiest stickiness stickily
stiff stiffly stiffness stiffest stiffer stiffens stiffening stiffened stiffen
stink stank stunk stinks stinking stinker stinkers
stir stirs stirring stirred
stitch stitches stitched stitching stitchery
stomach stomachs
storm stormed storming storms
straightforward straightforwardly
strain strained straining strains
strap strapless strapping strapped straps unstrap unstrapping unstrapped unstraps
straw straws
stream streamed streaming streams
strict strictness strictly strictest stricter
string strings stringing strung stringy
stripe stripes stripey striped striping
stroke strokes stroked stroking strokings
subsidy subsidies subsidize subsidizes subsidized subsidizing subsidizer subsidizers subsidise subsidises subsidised subsidising subsidiser subsidisers
substance substances
substitute substituted substitutes substituting substitution
subtle unsubtle subtly subtleness subtler subtlest
suck sucks sucking sucked
suicide suicidal suicides
suite suites
superb superbly
supermarket supermarkets
supervise supervised unsupervised supervises supervising supervision supervisors supervisor supervisory
supper suppers
supplement supplementary supplemented supplementing supplements supplementation supplemental
surgeon surgeons
surgery surgeries
surname surnames
surround surrounded surrounding surrounds surroundings
suspend suspended suspending suspends suspension suspensions suspenders
suspicious suspiciously
swallow swallows swallowing swallowed
swan swans
swap swapping swapped swaps
sweat sweats sweaty sweatier sweatiest sweated sweating
swede swedes sweden swedish
sweep swept sweeps sweeping sweeper sweepers
swing swung swings swinging
switzerland swiss
symbol symbolic symbolical symbolically symbolise symbolises symbolised symbolising symbolism symbolize symbolized symbolizes symbolizing symbols
sympathy sympathies sympathetic unsympathetic unsympathetically sympathetically
symptom symptoms symptomatic symptomatically
tab tabs tabbed tabbing
tack tacks tacked tacking
tag tags tagged untagged tagging
tale tales
talent talented untalented talents
taxi taxis
tease teases teased teasing teasingly teaser teasers
teenage teenager teenagers teenaged
telecom telecoms
temper tempers
tempt tempts tempting tempted temptation temptations
tender tenderness tenderly
tennis
tense tensed tenses tensing tension tensely tenser tensest tensions
tent tents
terminal terminally terminals
terminate terminated terminates terminating termination terminations terminator terminators
terrace terraced terraces terracing
terrific terrifically
terrify terrifies terrified terrifying terrifyingly
therapy therapies therapist therapists
thief thieves thieved thieving
thorough thoroughness thoroughly
thrill thrilled thrilling thrills thriller thrillers
throat throats throaty
thumb thumbs thumbed thumbing thumbings
thunder thundered thundering thunders thundery thunderous thunderously
thus
tide tides tidal
tilled tilling tills tiller tillers
timber timbered timbers
timetable timetables timetabled timetabling
tissue tissues
toe toes
token tokens tokenism
tone tones tonal tonality toned toning toner toners
tongue tongues
torch torched torching torches
toss tosses tossed tossing
towel towels towelette towelettes towelling towellings
trace traced traces tracing traceable untraceable
tragedy tragedies tragedian tragedians
tragic tragically
trail trailed trails trailing
transform transformation transformations transformational transformed transforming transforms transformer transformers
translate translating translates translated translation translations translator translators
transmit transmission transmissions transmitted transmitting transmits transmitter transmitters
trap traps trapping trapped trapper trappers
tread trod treads treading
triangle triangles triangular
trigger triggered triggering triggers
trivial trivially triviality trivialities trivialize trivializes trivialized trivializing trivialization trivialise trivialises trivialised trivialising trivialisation
trolley trolleys
troop troops
trophy trophies
truck trucks trucked trucking trucker truckers
tube tubes
tumble tumbles tumbled tumbling tumbler tumblers
tunnel tunnels tunnelled tunnelling tunnellings
turkey turk turks turkish
twin twins twinned twinning
twist twists twisting twisted untwisted
tyre tyres
underground
underline underlined underlines underlining
undo undid undone undoes undoing
uniform uniforms uniformed uniformity uniformly
unique uniquely uniqueness
upper
upwards upward upwardly
urge urging urges urged
urgent urgently urgency nonurgent
utilise utilises utilised utilising utilisation utiliser utilisers utilize utilizes utilized utilizing utilization utilizer utilizers
utility utilities
vacuum vacuums vacuumed vacuuming
vague vaguely vagueness
vandal vandals vandalize vandalizes vandalized vandalizing vandalise vandalises vandalised vandalising vandalism vandalisms
vat
verbal verbally nonverbal verbalize verbalizes verbalized verbalizing verbalise verbalises verbalised verbalising verbalisation verbalizations
versus vs
vest vests vested vesting
vet vets veterinary veterinarian veterinarians
via
vice vices
victorian victorians
victory victories victorious
virgin virginity virginal virgins
virus viruses
visible visibly invisible invisibly visibility invisibility
vision visions visionary
visual visualise visualised visualising visualisation visualize visualized visualizing visualization visually
vital vitally
voucher vouchers
wagon wagons waggon waggons
wallet wallets
wallpaper wallpapers
wander wanders wandering wanderings wandered wanderer wanderers
wardrobe wardrobes
warehouse warehouses
weapon weapons
weed weeds weedless weedy weedier weediest weeded weeding
welfare
whack whacks whacked whacking whacker whackers
whatsoever
wheelchair wheelchairs
whereabouts
whereby
whip whipping whipped whips
whiskey whiskeys whisky whiskies
whistle whistles whistled whistling whistler whistlers
whoop whoops whooped whooping whooper whoopers
wicked wickeder wickedest wickedness wickedly
widow widows widower widowed widowhood widowhoods
wig wigs wigged
wild wilder wildest wildly wildness
willy willies
wobble wobbles wobbled wobbling wobbly
wolf wolves wolfish
wool wools woollen woolly woolies
workshop workshops
worthwhile
wound wounds wounded unwounded wounding
wreck wrecks wrecked wrecking wrecker wreckers wreckage wreckages
wrestle wrestles wrestled wrestling wrestler wrestlers
wrist wrists
yugoslavia yugoslavian yugoslavians yugoslav yugoslavs
zealand zealander zealanders
zone zones zonal zoned zoning
articulate articulates articulated articulating articulation articulations
cement cemented cementing cements
cramp cramped cramps cramping
cripple cripples crippled crippling crippler cripplers
disguise disguises disguised undisguised disguising
doorway doorways
embassy embassies
era eras
pier piers
skeleton skeletons
stride strode strides striding
vicious viciousness viciously
warrant warrants warranted unwarranted warranting''')


awlunsplit = ('''
abandon abandoned abandoning abandonment abandons
abstract abstraction abstractions abstractly abstracts
academy academia academic academically academics academies
access accessed accesses accessibility accessible accessing inaccessible
accommodate accommodated accommodates accommodating accommodation
accompany accompanied accompanies accompaniment accompanying unaccompanied
accumulate accumulated accumulating accumulation accumulates
accurate accuracy accurately inaccuracy inaccuracies inaccurate
achieve achievable achieved achievement achievements achieves achieving
acknowledge acknowledged acknowledges acknowledging acknowledgement acknowledgements
acquire acquired acquires acquiring acquisition acquisitions
adapt adaptability adaptable adaptation adaptations adapted adapting adaptive adapts
adequate adequacy adequately inadequacies inadequacy inadequate inadequately
adjacent
adjust adjusted adjusting adjustment adjustments adjusts readjust readjusted readjusting readjustment readjustments readjusts
administrate administrates administration administrations administrative administratively administrator administrators
adult adulthood adults
advocate advocacy advocated advocates advocating
affect affected affecting affective affectively affects unaffected
aggregate aggregated aggregates aggregating aggregation
aid aided aiding aids unaided
albeit
allocate allocated allocates allocating allocation allocations
alter alterable alteration alterations altered altering alternate alternating alters unalterable unaltered
alternative alternatively alternatives
ambiguous ambiguities ambiguity unambiguous unambiguously
amend amended amending amendment amendments amends
analogy analogies analogous
analyse analysed analyser analysers analyses analysing analysis analyst analysts analytic analytical analytically analyze analyzed analyzes analyzing
annual annually
anticipate anticipated anticipates anticipating anticipation unanticipated
apparent apparently
append appendix appended appends appending appendices appendixes
appreciate appreciable appreciably appreciated appreciates appreciating appreciation unappreciated
approach approachable approached approaches approaching unapproachable
appropriate appropriacy appropriately appropriateness inappropriacy inappropriate inappropriately
approximate approximated approximately approximates approximating approximation approximations
arbitrary arbitrariness arbitrarily
area areas
aspect aspects
assemble assembled assembles assemblies assembling assembly
assess assessable assessed assesses assessing assessment assessments reassess reassessed reassessing reassessment unassessed
assign assigned assigning assignment assignments assigns reassign reassigned reassigning reassigns unassigned
assist assistance assistant assistants assisted assisting assists unassisted
assume assumed assumes assuming assumption assumptions
assure assurance assurances assured assuredly assures assuring
attach attached attaches attaching attachment attachments unattached
attain attainable attained attaining attainment attainments attains unattainable
attitude attitudes
attribute attributable attributed attributes attributing attribution
author authored authoring authors authorship
authority authoritative authorities
automate automatic automated automates automating automatically automation
available availability unavailable
aware awareness unaware
behalf
benefit beneficial beneficiary beneficiaries benefited benefiting benefits
bias biased biases biasing unbiased
bond bonded bonding bonds
brief brevity briefed briefing briefly briefs
bulk bulky
capable capabilities capability incapable
capacity capacities incapacitate incapacitated
category categories categorisation categorise categorised categorises categorising categorization categorized categorizes categorizing
cease ceased ceaseless ceases ceasing
challenge challenged challenger challengers challenges challenging
channel channelled channelling channels
chapter chapters
chart charted charting charts uncharted
chemical chemically chemicals
circumstance circumstances
cite citation citations cited citing cites
civil
clarify clarification clarified clarifies clarifying clarity
classic classical classics
clause clauses
code coded codes coding
coherent coherence coherently incoherent incoherently
coincide coincided coincides coinciding coincidence coincidences coincident coincidental
collapse collapsed collapses collapsible collapsing
colleague colleagues
commence commenced commences commencement commencing recommences recommenced recommencing
comment commentaries commentary commentator commentators commented commenting comments
commission commissioned commissioner commissioners commissioning commissions
commit commitment commitments commits committed committing
commodity commodities
communicate communicable communicated communicates communicating communication communications communicative communicatively uncommunicative
community communities
compatible compatibility incompatibility incompatible
compensate compensated compensates compensating compensation compensations compensatory
compile compilation compilations compiled compiles compiling
complement complementary complemented complementing complements
complex complexities complexity
component componentry components
compound compounded compounding compounds
comprehensive comprehensively
comprise comprised comprises comprising
compute computation computational computations computable computer computed computerised computers computing
conceive conceivable conceivably conceived conceives conceiving inconceivable inconceivably
concentrate concentrated concentrates concentrating concentration
concept conception concepts conceptual conceptualisation conceptualise conceptualised conceptualises conceptualising conceptually
conclude concluded concludes concluding conclusion conclusions conclusive conclusively inconclusive inconclusively
concurrent concurrently
conduct conducted conducting conducts
confer conference conferences conferred conferring confers
confine confined confines confining unconfined
confirm confirmation confirmed confirming confirms
conflict conflicted conflicting conflicts
conform conformable conformability conformance conformation conformed conforming conformist conformists conformity conforms nonconformist nonconformists nonconformity non-conformist non-conformists non-conformity
consent consensus consented consenting consents
consequent consequence consequences consequently
considerable considerably
consist consisted consistency consistent consistently consisting consists inconsistencies inconsistency inconsistent
constant constancy constantly constants inconstancy inconstantly
constitute constituencies constituency constituent constituents constituted constitutes constituting constitution constitutions constitutional constitutionally constitutive unconstitutional
constrain constrained constraining constrains constraint constraints unconstrained
construct constructed constructing construction constructions constructive constructs reconstruct reconstructed reconstructing reconstruction reconstructs
consult consultancy consultant consultants consultation consultations consultative consulted consults consulting
consume consumed consumer consumers consumes consuming consumption
contact contactable contacted contacting contacts
contemporary contemporaries
context contexts contextual contextualise contextualised contextualising uncontextualised contextualize contextualized contextualizing uncontextualized
contract contracted contracting contractor contractors contracts
contradict contradicted contradicting contradiction contradictions contradictory contradicts
contrary contrarily
contrast contrasted contrasting contrastive contrasts
contribute contributed contributes contributing contribution contributions contributor contributors
controversy controversies controversial controversially uncontroversial
convene convention convenes convened convening conventional conventionally conventions unconventional
converse conversely
convert conversion conversions converted convertible converting converts
convince convinced convinces convincing convincingly unconvinced
cooperate cooperated cooperates cooperating cooperation cooperative cooperatively co-operate co-operated co-operates co-operation co-operative co-operatively
coordinate coordinated coordinates coordinating coordination coordinator coordinators co-ordinate co-ordinated co-ordinates co-ordinating co-ordination co-ordinator co-ordinators
core cores coring cored
corporate corporates corporation corporations
correspond corresponded correspondence corresponding correspondingly corresponds
couple coupled coupling couples
create created creates creating creation creations creative creatively creativity creator creators recreate recreated recreates recreating
credit credited crediting creditor creditors credits
criteria criterion
crucial crucially
culture cultural culturally cultured cultures uncultured
currency currencies
cycle cycled cycles cyclic cyclical cycling
data
debate debatable debated debates debating
decade decades
decline declined declines declining
deduce deduced deduces deducing deduction deductions
define definable defined defines defining definition definitions redefine redefined redefines redefining undefined
definite definitely definitive indefinite indefinitely
demonstrate demonstrable demonstrably demonstrated demonstrates demonstrating demonstration demonstrations demonstrative demonstratively demonstrator demonstrators
denote denotation denotations denoted denotes denoting
deny deniable denial denials denied denies denying undeniable
depress depressed depresses depressing depression
derive derivation derivations derivative derivatives derived derives deriving
design designed designer designers designing designs
despite
detect detectable detected detecting detection detective detectives detector detectors detects
deviate deviated deviates deviating deviation deviations
device devices
devote devoted devotedly devotes devoting devotion devotions
differentiate differentiated differentiates differentiating differentiation
dimension dimensional dimensions multidimensional
diminish diminished diminishes diminishing diminution undiminished
discrete discretely discretion discretionary indiscrete indiscretion
discriminate discriminated discriminates discriminating discrimination
displace displaced displacement displaces displacing
display displayed displaying displays
dispose disposable disposal disposed disposes disposing
distinct distinction distinctions distinctive distinctively distinctly indistinct indistinctly
distort distorted distorting distortion distortions distorts
distribute distributed distributing distribution distributional distributions distributive distributor distributors redistribute redistributed redistributes redistributing redistribution
diverse diversely diversification diversified diversifies diversify diversifying diversity
document documentation documented documenting documents
domain domains
domestic domestically domesticate domesticated domesticating domestics
dominate dominance dominant dominated dominates dominating domination
draft drafted drafting drafts redraft redrafted redrafting redrafts
drama dramas dramatic dramatically dramatise dramatised dramatising dramatises dramatisation dramatisations dramatist dramatists dramatization dramatizations dramatize dramatized dramatizes dramatizing
duration
dynamic dynamically dynamics
economy economic economical economically economics economies economist economists uneconomical
edit edited editing edition editions editor editorial editorials editors edits
element elements
eliminate eliminated eliminates eliminating elimination
emerge emerged emergence emergent emerges emerging
emphasis emphasise emphasised emphasising emphasize emphasized emphasizes emphasizing emphatic emphatically
empirical empirically empiricism
enable enabled enables enabling
encounter encountered encountering encounters
energy energetic energetically energies
enforce enforced enforcement enforces enforcing
enhance enhanced enhancement enhances enhancing
enormous enormity enormously
ensure ensured ensures ensuring
entity entities
environment environmental environmentalist environmentalists environmentally environments
equate equated equates equating equation equations
equip equipment equipped equipping equips
equivalent equivalence
erode eroded erodes eroding erosion
error erroneous erroneously errors
establish disestablish disestablished disestablishes disestablishing disestablishment established establishes establishing establishment establishments
estate estates
estimate estimated estimates estimating estimation estimations over-estimate overestimate overestimated overestimates overestimating underestimate underestimated underestimates underestimating
ethic ethical ethically ethics unethical
ethnic ethnicity
evaluate evaluated evaluates evaluating evaluation evaluations evaluative re-evaluate re-evaluated re-evaluates re-evaluating re-evaluation
eventual eventuality eventually
evident evidenced evidence evidential evidently
evolve evolution evolved evolving evolves evolutionary evolutionist evolutionists
exceed exceeded exceeding exceeds
exclude excluded excludes excluding exclusion exclusionary exclusionist exclusions exclusive exclusively
exhibit exhibited exhibiting exhibition exhibitions exhibits
expand expanded expanding expands expansion expansionism expansive
expert expertise expertly experts
explicit explicitly
exploit exploitation exploited exploiting exploits
export exported exporter exporters exporting exports
expose exposed exposes exposing exposure exposures
external externalisation externalise externalised externalises externalising externality externalization externalize externalized externalizes externalizing externally
extract extracted extracting extraction extracts
facilitate facilitated facilitates facilities facilitating facilitation facilitator facilitators facility
factor factored factoring factors
feature featured features featuring
federal federation federations
fee fees
file filed files filing
final finalise finalised finalises finalising finalize finalized finalizes finalizing finality finally finals
finance financed finances financial financially financier financiers financing
finite infinite infinitely
flexible flexibility inflexible inflexibility
fluctuate fluctuated fluctuates fluctuating fluctuation fluctuations
focus focused focuses focusing focussed focussing refocus refocused refocuses refocusing refocussed refocusses refocussing
format formatted formatting formats
formula formulae formulas formulate formulated formulating formulation formulations reformulate reformulated reformulating reformulation reformulations
forthcoming
foundation foundations
founded founder founders founding unfounded
framework frameworks
function functional functionally functioned functioning functions
fund funded funder funders funding funds
fundamental fundamentally
furthermore
gender genders
generate generated generates generating
generation generations
globe global globally globalisation globalization
goal goals
grade graded grades grading
grant granted granting grants
guarantee guaranteed guaranteeing guarantees
guideline guidelines
hence
hierarchy hierarchical hierarchies
highlight highlighted highlighting highlights
hypothesis hypotheses hypothesise hypothesised hypothesises hypothesising hypothesize hypothesized hypothesizes hypothesizing hypothetical hypothetically
identical identically
identify identifiable identification identified identifies identifying identities identity unidentifiable
ideology ideological ideologically ideologies
ignorant ignorance ignore ignored ignores ignoring
illustrate illustrated illustrates illustrating illustration illustrations illustrative
image imagery images
immigrate immigrant immigrants immigrated immigrates immigrating immigration
impact impacted impacting impacts
implement implementation implemented implementing implements
implicate implicated implicates implicating implication implications
implicit implicitly
imply implied implies implying
impose imposed imposes imposing imposition
incentive incentives
incidence incident incidentally incidents
incline inclination inclinations inclined inclines inclining
income incomes
incorporate incorporated incorporates incorporating incorporation
index indexed indexes indexing
indicate indicated indicates indicating indication indications indicative indicator indicators
individual individualised individuality individualism individualist individualists individualistic individually individuals
induce induced induces inducing induction
inevitable inevitability inevitably
infer inference inferences inferred inferring infers
infrastructure infrastructures
inherent inherently
inhibit inhibited inhibiting inhibition inhibitions inhibits
initial initially
initiate initiated initiates initiating initiation initiations initiative initiatives initiator initiators
injure injured injures injuries injuring injury uninjured
innovate innovation innovated innovates innovating innovations innovative innovator innovators
input inputs
insert inserted inserting insertion inserts
insight insightful insights
inspect inspected inspecting inspection inspections inspector inspectors inspects
instance instances
institute instituted institutes instituting institution institutional institutionalise institutionalised institutionalises institutionalising institutionalized institutionalizes institutionalizing institutionally institutions
instruct instruction instructed instructing instructions instructive instructor instructors instructs
integral
integrate integrated integrates integrating integration
integrity
intelligence intelligent intelligently unintelligent
intense intensely intenseness intensification intensified intensifies intensify intensifying intension intensity intensive intensively
interact interacted interacting interaction interactions interactive interactively interacts
intermediate
internal internalise internalised internalises internalising internalize internalized internalizes internalizing internally
interpret interpretation interpretations interpretative interpreted interpreting interpretive interprets misinterpret misinterpretation misinterpretations misinterpreted misinterpreting misinterprets reinterpret reinterpreted reinterprets reinterpreting reinterpretation reinterpretations
interval intervals
intervene intervened intervenes intervening intervention interventions
intrinsic intrinsically
invest invested investing investment investments investor investors invests reinvest reinvested reinvesting reinvestment reinvests
investigate investigated investigates investigating investigation investigations investigative investigator investigators
invoke invoked invokes invoking
involve involved involvement involves involving uninvolved
isolate isolated isolates isolating isolation isolationism
issue issued issues issuing
item itemisation itemise itemised itemises itemising items
job jobs
journal journals
justify justifiable justifiably justification justifications justified justifies justifying unjustified
label labeled labeling labelled labelling labels
labour labor labored labors laboured labouring labours
layer layered layering layers
lecture lectured lecturer lecturers lectures lecturing
legal illegal illegality illegally legality legally
legislate legislated legislates legislating legislation legislative legislator legislators legislature
levy levies
liberal liberalise liberalism liberalisation liberalised liberalises liberalising liberalization liberalize liberalized liberalizes liberalizing liberate liberated liberates liberation liberations liberating liberator liberators liberally liberals
licence licences license licensed licensing licenses unlicensed
likewise
link linkage linkages linked linking links
locate located locating location locations relocate relocated relocates relocating relocation
logic illogical illogically logical logically logician logicians
maintain maintained maintaining maintains maintenance
major majorities majority
manipulate manipulated manipulates manipulating manipulation manipulations manipulative
manual manually manuals
margin marginal marginally margins
mature immature immaturity maturation maturational matured matures maturing maturity
maximise max maximised maximises maximising maximisation maximize maximized maximizes maximizing maximization maximum
mechanism mechanisms
media
mediate mediated mediates mediating mediation
medical medically
medium
mental mentality mentally
method methodical methodological methodologies methodology methods
migrate migrant migrants migrated migrates migrating migration migrations migratory
military
minimal minimalisation minimalise minimalises minimalised minimalising minimalist minimalists minimalistic minimalization minimalize minimalized minimalizes minimalizing minimally
minimise minimised minimises minimising minimize minimized minimizes minimizing
minimum
ministry ministerial ministries
minor minorities minority minors
mode modes
modify modification modifications modified modifies modifying unmodified
monitor monitored monitoring monitors unmonitored
motive motivate motivated motivates motivating motivation motivations motives unmotivated
mutual mutually
negate negative negated negates negating negatively negatives
network networked networking networks
neutral neutralisation neutralise neutralised neutralises neutralising neutrality neutralization neutralize neutralized neutralizes neutralizing
nevertheless
nonetheless
norm norms
normal abnormal abnormally normalisation normalise normalised normalises normalising normalization normalize normalized normalizes normalizing normality normally
notion notions
notwithstanding
nuclear
objective objectively objectivity
obtain obtainable obtained obtaining obtains unobtainable
obvious obviously
occupy occupancy occupant occupants occupation occupational occupations occupied occupier occupiers occupies occupying
occur occurred occurrence occurrences occurring occurs reoccur reoccurred reoccurring reoccurs
odd odds
offset offsets offsetting
ongoing
option optional options
orient orientate orientated orientates orientation orientating oriented orienting orients reorient reorientation
outcome outcomes
output outputs
overall
overlap overlapped overlapping overlaps
overseas
panel panelled panelling panels
paradigm paradigms
paragraph paragraphing paragraphs
parallel paralleled parallelled parallelling parallels unparalleled
parameter parameters
participate participant participants participated participates participating participation participatory
partner partners partnership partnerships
passive passively passivity
perceive perceived perceives perceiving perception perceptions
percent percentage percentages
period periodic periodical periodically periodicals periods
persist persisted persistence persistent persistently persisting persists
perspective perspectives
phase phased phases phasing
phenomenon phenomena phenomenal
philosophy philosopher philosophers philosophical philosophically philosophies philosophise philosophised philosophises philosophising philosophize philosophized philosophizes philosophizing
physical physically
plus pluses
policy policies
portion portions
pose posed poses posing
positive positively
potential potentially
practitioner practitioners
precede preceded precedence precedent precedes preceding unprecedented
precise imprecise precisely precision
predict predictability predictable predictably predicted predicting prediction predictions predicts unpredictability unpredictable
predominant predominance predominantly predominate predominated predominates predominating
preliminary preliminaries
presume presumably presumed presumes presuming presumption presumptions
previous previously
primary primarily
prime primacy
principal principally
principle principled principles unprincipled
prior
priority priorities prioritisation prioritise prioritised prioritises prioritising prioritization prioritize prioritized prioritizes prioritizing
proceed procedural procedure procedures proceeded proceeding proceedings proceeds
process processed processes processing
professional professionally professionals professionalism
prohibit prohibited prohibiting prohibition prohibitions prohibitive prohibits
project projected projecting projection projections projects
promote promoted promoter promoters promotes promoting promotion promotions
proportion disproportion disproportionate disproportionately proportional proportionally proportionate proportionately proportions
prospect prospective prospects
protocol protocols
psychology psychological psychologically psychologist psychologists
publication publications
publish published publisher publishers publishes publishing unpublished
purchase purchased purchaser purchasers purchases purchasing
pursue pursued pursues pursuing pursuit pursuits
qualitative qualitatively
quote quotation quotations quoted quotes quoting
radical radically radicals
random randomly randomness
range ranged ranges ranging
ratio ratios
rational irrational rationalisation rationalisations rationalise rationalised rationalises rationalising rationalism rationality rationalization rationalizations rationalize rationalized rationalizes rationally
react reacted reacts reacting reaction reactionaries reactionary reactions reactive reactivate reactivation reactor reactors
recover recoverable recovered recovering recovers recovery
refine refined refinement refinements refines refining
regime regimes
region regional regionally regions
register deregister deregistered deregistering deregisters deregistration registered registering registers registration
regulate deregulated deregulates deregulating deregulation regulated regulates regulating regulation regulations regulator regulators regulatory unregulated
reinforce reinforced reinforcement reinforcements reinforces reinforcing
reject rejected rejecting rejection rejects rejections
relax relaxation relaxed relaxes relaxing
release released releases releasing
relevant irrelevance irrelevant relevance
reluctance reluctant reluctantly
rely reliability reliable reliably reliance reliant relied relies relying unreliable
remove removable removal removals removed removes removing
require required requirement requirements requires requiring
research researched researcher researchers researches researching
reside resided residence resident residential residents resides residing
resolve resolution resolved resolves resolving unresolved
resource resourced resourceful resources resourcing unresourceful under-resourced
respond responded respondent respondents responding responds response responses responsive responsiveness unresponsive
restore restoration restored restores restoring
restrain restrained restraining restrains restraint restraints unrestrained
restrict restricted restricting restriction restrictions restrictive restrictively restricts unrestricted unrestrictive
retain retained retaining retainer retainers retains retention retentive
reveal revealed revealing reveals revelation revelations
revenue revenues
reverse reversal reversed reverses reversible reversing reversals irreversible
revise revised revises revising revision revisions
revolution revolutionary revolutionaries revolutionise revolutionised revolutionises revolutionising revolutionist revolutionists revolutionize revolutionized revolutionizes revolutionizing revolutions
rigid rigidities rigidity rigidly
role roles
route routed routes routing
scenario scenarios
schedule reschedule rescheduled reschedules rescheduling scheduled schedules scheduling unscheduled
scheme schematic schematically schemed schemes scheming
scope
section sectioned sectioning sections
sector sectors
secure insecure insecurities insecurity secured securely secures securing securities security
seek seeking seeks sought
select selected selecting selection selections selective selectively selector selectors selects
sequence sequenced sequences sequencing sequential sequentially
series
sex sexes sexism sexual sexuality sexually
shift shifted shifting shifts
significant insignificant insignificantly significance significantly signified signifies signify signifying
similar dissimilar similarities similarity similarly
simulate simulated simulates simulating simulation
site sites
so-called
sole solely
somewhat
source sourced sources sourcing
specific specifically specification specifications specificity specifics
specify specifiable specified specifies specifying unspecified
sphere spheres spherical spherically
stable instability stabilisation stabilise stabilised stabilises stabilising stabilization stabilize stabilized stabilizes stabilizing stability unstable
statistic statistician statisticians statistical statistically statistics
status
straightforward
strategy strategic strategies strategically strategist strategists
stress stressed stresses stressful stressing unstressed
structure restructure restructured restructures restructuring structural structurally structured structures structuring unstructured
style styled styles styling stylish stylise stylised stylises stylising stylize stylized stylizes stylizing
submit submission submissions submits submitted submitting
subordinate subordinates subordination
subsequent subsequently
subsidy subsidiary subsidies subsidise subsidised subsidises subsidising subsidize subsidized subsidizes subsidizing
substitute substituted substitutes substituting substitution
successor succession successions successive successively successors
sufficient sufficiency insufficient insufficiently sufficiently
sum summation summed summing sums
summary summaries summarise summarised summarises summarising summarisation summarisations summarization summarizations summarize summarized summarizes summarizing
supplement supplementary supplemented supplementing supplements
survey surveyed surveying surveys
survive survival survived survives surviving survivor survivors
suspend suspended suspending suspends suspension
sustain sustainable sustainability sustained sustaining sustains sustenance unsustainable
symbol symbolic symbolically symbolise symbolises symbolised symbolising symbolism symbolize symbolized symbolizes symbolizing symbols
tape taped tapes taping
target targeted targeting targets
task tasks
team teamed teaming teams
technical technically
technique techniques
technology technological technologically
temporary temporarily
tense tension tensely tenser tensest tensions
terminate terminal terminals terminated terminates terminating termination terminations
text texts textual
theme themes thematic thematically
theory theoretical theoretically theories theorist theorists
thereby
thesis theses
topic topical topics
trace traceable traced traces tracing
tradition non-traditional traditional traditionalist traditionally traditions
transfer transferable transference transferred transferring transfers
transform transformation transformations transformed transforming transforms
transit transited transiting transition transitional transitions transitory transits
transmit transmission transmissions transmitted transmitting transmits
transport transportation transported transporter transporters transporting transports
trend trends
trigger triggered triggering triggers
ultimate ultimately
undergo undergoes undergoing undergone underwent
underlie underlay underlies underlying
undertake undertaken undertakes undertaking undertook
uniform uniformity uniformly
unify unification unified unifies unifying
unique uniquely uniqueness
utilise utilisation utilised utilises utilising utiliser utilisers utility utilities utilization utilize utilized utilizes utilizing
valid invalidate invalidity validate validated validating validation validity validly
vary invariable invariably variability variable variables variably variance variant variants variation variations varied varies varying
vehicle vehicles
version versions
via
violate violated violates violating violation violations
virtual virtually
visible visibility visibly invisible invisibility
vision visions
visual visualise visualised visualising visualisation visualize visualized visualizing visualization visually
volume volumes vol
voluntary voluntarily volunteer volunteering volunteered volunteers
welfare
whereas
whereby
widespread''')

gsl1unsplit = ('''
a an
able ability abler ablest ably abilities unable inability
about
above
accept acceptability acceptable unacceptable acceptance accepted accepting accepts
accord accorded accordance according accordingly accords
account accounted accounting accounts accountant accountants accountancy
accountable accountability
across
act acted acting action actions acts
active actively activities activity
actor actors
actress actresses
actual actually
add added adding addition additional additive additions adds
address addressed addresses addressing
admit admission admittedly admits admitted admitting
adopt adopted adopting adoption adoptions adopts
advance advanced advances advancement advancing
advantage advantages disadvantage disadvantages advantaging advantaged disadvantaged
adventure adventures adventurer adventurers adventurous
affair affairs
after afterwards
again
against
age aged ages aging
agent agency agencies agents
ago
agree agreed agreeing agreement agreements agrees agreeable disagreements disagree disagreeable disagreed disagreeing disagreement disagrees
air
all
allow allowance allowances allowed allowing allows
almost
alone
along
already
also
although
always
among amongst
amount amounted amounting amounts
ancient
and
animal animals
another
answer answered answering answers
any anybody anyhow anymore anyone anything anyway anywhere
appear appearance appeared appearing appears appearances disappearances disappear disappearance disappeared disappearing disappears
apply application applications applied applies applicable applying applicant applicants applicability
appoint appointed appointing appointments appointment appoints
april
arise arisen arises arose arising
arm armed arms unarmed
army armies
around
arrive arrival arrivals arrived arrives arriving
art arts artist artistic artists artistically
article articles
as
ask asked asking asks
associate associations association associating associates associated disassociate disassociated
at
attack attacked attacking attacks
attempt attempted attempting attempts
august
average averaged averages averaging
away
b
back backed background backing backs backbone backgrounds backwards backward
bad badly badness
ball balls
bank banked banker bankers banking banks
bar bars barred barring
base based bases basic basically basing basis
battle battled battles battling
be am are aren been is isn re s was wasn were weren being beings
bear bearing bearings bears bore born borne
beauty beautiful beautifully
because
become became becomes becoming
bed bedroom bedrooms bedding beds
before
begin began beginner beginners beginning beginnings begins begun
behind
believe belief beliefs believed believes believing disbelief
belong belonged belonging belongings belongs
below
beneath
beside besides
best better
between
beyond
big bigger biggest biggish
bill bills billed billing
bird birds
black blacker blackest blackly blacken blackness blacks blackish
blood bled bleed bleeding bleeds bloody
blow blew blowing blows blown
blue blueness bluer bluest
board boarded boarding boards
boat boats
body bodies bodily
book books
both
box boxes
boy boyhood boys
branch branches branched branching
bread
break breaking breakage breaks broke broken unbreakable outbreaks outbreak unbroken
bridge bridges
bright brighten brightened brightening brightens brighter brightest brightly brightness
bring bringing brings brought
broad broadly breadth broader broadest
brother brothers brotherly
build build-up builders building buildings builds built
burn burned burning burns burnt
business businesses businessmen unbusinesslike businesslike businessman businesswoman businesswomen
but
buy bought buying buys buyer buyers
by
c
call called calling calls
can cannot cans canned canning
capital capitals
captain captains
car cars
care cared careful carefully careless cares caring carelessly
carry carried carries carrying
case cases
castle castles
catch catches catching caught
cause caused causes causing
centre center centerist centerists centers centred centered central centralization centres centrist centrists
certain certainly certainty uncertain uncertainties uncertainty
chance chanced chances chancing
change changed changes changing unchanged unchangeable unchanging
character characteristic characteristically characteristics characterize characterized characterization characterizes characterise characterised characterises characters
charge charged charges charging
chief chiefs chiefly
child children childish childhood childlike
choose choice choices chooses choosing chose chosen
church churches
circle circled circles circling circular
city cities citizen citizens
claim claimed claiming claims unclaimed
class classed classes classing classify classifying classified classifies classification classifications
clear cleared clearer clearest clearing clearings clearly clearness clears
close closed closely closeness closer closes closest closure closing
cloud cloudy clouded clouds
coal
coast coasts
coin coins
cold colder coldest coldly coldness colds
college colleges
colony colonial colonies colonials colonize colonization colonized colonising colonist colonists
colour color colored colorful coloring colorless colors coloured colourful colouring colourless colours
come came comes coming
command commanded commanding commands commander commanders
committee committees
common commoner commonest commonly commonness commons uncommon uncommonly
company companies
complete completed completely completion completions completes completeness completing incomplete incompletely
concern concerned concerning concerns unconcerned
condition conditional conditions unconditional
consider consideration considerations considered considering considers reconsider reconsidering reconsideration
contain contained container containers containing contains
content contented contenting contentment contents discontent discontentment
continue continuance continued continuity continues continuing continuous continuously
control controlled controller controlling controls uncontrollable uncontrollably uncontrolled
corn
cost costing costs costly
cotton
could couldn
council councillor councillors councilor councils
count counted counting countless counts countable uncountable
country countries
course courses
court courts
cover covered covering coverage covers uncover uncovered uncovers
cross crossed crosses crossing
crowd crowded crowding crowds
crown crowns crowned crowning uncrowned
cry cried cries crying
current currently
cut cuts cutting uncut
d
danger dangerous dangerously dangers
dark darker darkest darkness
date dates dated dating
daughter daughters
day daily daylight days
dead death deaths
deal dealer dealers dealing dealings deals dealt
dear dears
december
decide decided decidedly decides deciding decision decisions decisive undecided
declare declaration declarations declared declares declaring
deep deepen deepened deeper deepest deeply depth depths deepening
defeat defeated defeats defeating undefeated
degree degrees
demand demanded demanding demands
department departments departmental
depend depends depended depending dependant dependants dependent
describe described describes describing description descriptions descriptive
desert deserted deserting deserts
desire desired desirability desirable desires desiring undesirable
destroy destroyed destroying destroys destruction destructive
detail detailed detailing details
determine determination determined indeterminate determinate determines determining
develop developed developers developing development developments develops underdeveloped undeveloped
die died dies dying undying
difference differ differences different differs differing differently
difficult difficulties difficulty
direct directed directing direction directions directly director directors directs indirect indirectly
discover discovered discoveries discovering discovers discovery
distance distances distant distanced distancing
distinguish distinguished distinguishes distinguishing distinguishable
district districts
divide divided divides dividing division divisions undivided
do did didn does doesn doing don done
doctor doctors dr
dog dogs dogged
dollar dollars
door doors indoors outdoors
doubt doubted doubtful doubting doubtless undoubtedly doubts
down downwards
draw drawing drawn draws drew
dream dreamed dreaming dreams dreamt dreamy
dress dressed dresses dressing undressed
drink drinks drinker drinkers drank drunk drinking
drive driven driver drivers drives driveway driving drove
drop dropped dropping drops
dry dried dries driest dryer drying dryly dryness
due
duty duties
e
each
ear ears
early earlier earliest earliness
earth earthy earthquake earthquakes
east eastern
easy easier easiest easily easiness
eat ate eaten eating eats
effect effected effecting effective effectively effectiveness effects ineffective ineffectively
efficient efficiency inefficient
effort efforts
egg eggs
eight eighteen eighteenth eighth eighties eightieth eighty eights th
either
elect elected electing election elections elects electors electoral
eleven elevens eleventh
else elsewhere
empire empires
employ employed employee employees employer employers employing employment employs unemployed unemployment
end ended ending endless endlessly ends
enemy enemies
english
enjoy enjoyed enjoying enjoyment enjoys enjoyable
enough
enter entered entering enters entrance entrances entries entry
equal equaled equaling equality equalled equalling equally equals inequality unequal
escape escaped escapes escaping
even evenly
evening evenings
event events
ever
every everybody everyday everyone everything everywhere
example examples
except exception exceptional exceptions
exchange exchanged exchanges exchanging
exercise exercised exercises exercising
exist existed existence existing exists nonexistent
expect expectancy expectation expectations expected expecting expects
expense expenses expensive
experience experienced experiences experiencing
experiment experimental experimentation experimented experimenting experiments
explain explained explaining explains explanation explanatory explanations
express expressed expresses expressing expression expressions expressive
extend extended extending extends extension extensions extensive extensively extent
eye eyes
f
face faced faces facing
fact facts factual
factory factories
fail failed failing fails failure failures
fair fairer fairest fairly fairness unfair unfairly
faith faithful faithfully faiths
fall fallen falling falls fell
familiar familiarity unfamiliar unfamiliarity familiarly
family families
famous
far farther farthest further furthest
farm farmer farmers farms farming
fast faster fastest fastness
father fathers dad dads father-in-law
favour favor favorite favourite favourable favourably favoured favouring favourites favours
fear feared fearful fearing fears
february
feel feeling feelings feels felt
fellow fellows
few fewer fewest
field fields
fight fighter fighters fighting fought fights
figure figures
fill filled filling fills
find finding findings finds found
fine finely fineness finer finest
finish finished finishes finishing unfinished
fire fired fires firing
first firstly
fish fished fishes fishing fisherman
fit fitness fits fitted fitter fittest fitting
five fives fifteen fifteenth fifth fifthly fifties fiftieth fifty
fix fixed fixes fixing fixable
floor floors
flow flowed flows flowing
flower flowers
fly flew flown flying flight flights flies
follow followed follower followers following follows
food foods
for
force forced forces forcing forceful forcefully
foreign foreigner foreigners
forest forests foresting forested
forget forgets forgetting forgot forgotten unforgettable
form formation formed forming forms
former formerly
forth
fortune fortunate fortunately fortunes unfortunately unfortunate
four fours forties forty fourteen fourteenth fourth fourthly fortieth
free freed freedom freedoms freeing freely freer freest
fresh freshness fresher freshest freshly
friday fri fridays
friend friendly friends friendship friendships
from
front
full fuller fullest fullness fully
furnish furnishes furnished furnishing furniture
future futures
g
gain gained gaining gains
game games
garden gardener gardeners gardens
gas gases
gate gates
gather gathered gathering gatherings gathers
general generally generals generalise generalisable generalised generalisation generalisations generality generalizations
gentle gentleman gentlemen gently
get gets getting got gotten
gift gifts gifted
girl girls
give gave given gives giving
glad gladder gladdest gladly gladness
glass glasses
go goes going gone went
god gods goddess
gold golden
good goodbye goodbyes goodness
great greater greatest greatly greatness
green greener greenest greenness greenish
ground grounded grounds grounding
group grouped grouping groupings groups
grow grew growing grown grows growth
h
half halves
hand handed handful handfuls handing hands handwriting
hang hanged hanging hangs hung
happen happened happening happens
happy happier happiest happily happiness unhappy
hard harden hardened hardening hardens harder hardest hardness hardship hardships
hardly
have had hadn hasn has haven haves having ve
he him himself his
head headed heading heads
hear heard hearer hearing hears
heart hearts
heat heated heating heats
heaven heavenly heavens
heavy heavier heaviest heavily
help helped helpful helping helpless helplessly helps helper helpers
here
high higher highest highly highness highway highways
hill hills hillside hilly
history historian historic historical histories
hold held holders holding holds
home homeless homes
honour dishonour dishonourable honor honorable honorably honorary honored honoring honors honourable honourably
hope hoped hopeful hopeless hopelessness hopes hoping
horse horses
hot hotly hotness hotter hottest
hour hourly hours
house housed housing houses
how
however
human humans
hundred hundreds hundredth
husband husbands
i me mine my myself
idea ideas
if
ill illness illnesses
important importance unimportant unimportance importantly
in inner
inch inches
include included includes including inclusive inclusion
increase increased increases increasing increasingly
indeed
independent independently independence
industry industrial industrially industries
influence influenced influences influencing influential
instead
interest interested interesting interests
into
introduce introduced introduces introducing introduction introductions introductory
iron
it its itself
j
january jan
join joined joining joins
joint jointed disjointed joints jointly
joy joyful joyfully joys
judge judged judges judging judgment judgments judgement judgements judgemental
july
june
just justly unjust unjustly
justice
k
keep keepers keeping keeps kept
kill killed killer killers killing kills
kind kindly kindness kinds
king kings kingdom kingdoms
know knew knowing knowledge known knows unknown knowledgeable
l
lack lacked lacking lacks
lady ladies
lake lakes
land landed landing lands landlords
language languages
large largely larger largest
last lasted lasting lasts lastly
late lately lateness later latest
latter
laugh laughs laughed laughing laughable
laughter
law laws lawyer lawyers lawful lawfully unlawful lawless
lay laid laying lays
lead leaded leader leaders leadership leading leads mislead misleading misled led
learn learned learner learners learning learns learnt
leave leaves leaving
left leftist leftists
length lengthening lengths lengthy lengthen
less lessen lessened lessening lesser least
let lets letting
letter letters
level levelled leveller levelling levels
library librarian librarians libraries
lie liar liars lied lies lying
life lifetime lifetimes lifelike lifesize lifelong
lift lifted lifting lifts
light lighted lighten lighter lightest lighting lightly lightness lights lightweight lit
like liked likes liking unlike dislike dislikes disliked disliking
likely likelier likeliest likelihood unlikely
limit limitation limitations limited limiting limits unlimited
line lines lined lining
lip lips
listen listened listener listeners listening listens
literature literary
little littler littlest
live lived liveliest lively lives living
local locally locals
long longer longest
look looked looking looks outlook
lord lords lordship lordships
lose losers loses losing lost
loss losses
love loved lovely loves loving lovable lover
low lower lowered lowest lowering
m
machine machinery machines
main mainly
make made maker makers makes making
man mankind men manly manhood manliness
manner manners
manufacture manufactured manufacturing manufactures manufacturers manufacturer
many
march marched marchers marches marching
mark marked marker markers marking marks
market marketed marketing markets
marry marriage marriages married marries marrying
mass masses
master masters mastered mastering masterful mastery
material materialistic materialistically materially materials
matter mattered mattering matters
may
maybe
mean meaner meanest meaning meaningful meaningless meanings meanly meanness means meant
measure measured measurement measurements measures measurable measurably measuring
meet meeting meetings meets met
member members membership memberships
memory memorial memories memorise memorised memorises memorising memorize memorized memorizes memorizing memorials
mention mentioned mentioning mentions unmentioned
mere merely merest
metal metals
middle mid midnight midst
might mightn
mile miles
milk milky milked milks milking
million millions millionth
mind minded minding minds
miner miners mined mining mines
minister ministers
minute minutes
miss missed misses missing
mister mr
modern modernise modernisation
moment momentary moments
monday mon mondays
money
month monthly months
moon moons moonlight
moral morals morally morality
more
moreover
morning mornings
most mostly
mother mother-in-law mothers mom motherhood mum
motor motorist motorists motors
mountain mountains mountainside mt
mouth mouthful mouths
move moved movement moves moving movements
mrs ms
much
music musical musician musicians musically
must
n
name named names naming namely nameless
nation national nationally nationwide nations
native natives
nature natural naturally natures
near nearby nearer nearest nearly nearness
necessary necessarily unnecessarily unnecessary
necessity necessities
need needed needing needless needs needn
neighbour neighbor neighborhood neighborhoods neighbors neighbourhood neighbourhoods neighbours
neither
never
new newer newest newly newness renew renewed renews renewing
news
newspaper newspapers
next
night nightly nights
nine nines nineteen nineteenth nineties ninetieth ninety ninth
no nobody noone nothing nowhere
noble nobility nobler noblest nobly nobles
none
nor
north north-east north-west northeast northern northwards northwest
not t
note notable notes noting notably noted
notice noticeable noticeably noticed notices noticing
november nov
now nowadays
number numbered numbering numbers
numerous
numerical numerically
o
object objected objection objecting objects objectionable objections
observe observable observation observations observatory observed observer observers observes observing
occasion occasional occasionally occasions
october oct
of
off
offer offered offering offerings offers
office officer officers offices
official officially officialdom officials
often
oh
oil oily oiliness oils oiled
old older oldest
on onto
once
one ones
only
open opening openly openness opens opened
operate operated operates operating operation operations operator operators operational operative
opinion opinions opinionated
opportunity opportunities
or
order ordered ordering orderly orders
ordinary ordinarily
organize organisation organisations organise organised organises organising organization organizations organized organizes organizing organisational
other others
otherwise
ought oughtn
out outer outside outsider outsiders outward outwards
over
owe owed owes owing
own owned owner owners ownership owning owns
p
page pages
paint painted painter painters painting paintings paints
paper papers papered papering
part parted parting partly parts partial partially particle particles
particular particularly
party parties
pass passed passes passing
past
pay paid paying payment payments pays repaid unpaid
peace peaceful peacefully
people peoples
per
perhaps
permit permission permits permitted permitting
person personal personalities personally persons
picture pictured pictures picturing
piece pieces
place placed places placing
plain plainly plains
plan planned planner planners planning plans
plant planted planting plants
play played player players playing plays replay replays replaying replayed
please pleasant pleasantly pleasantness pleased pleases pleasing pleasure unpleasant unpleasantly displease displeased displeasing displeasure
point pointed pointing points pointer pointers
political politically politician politicians politics
poor poorer poorest poorly
poverty
popular popularity popularly
population populations populate populating populated populates
position positions positioning positioned
possess possessed possesses possessing possession possessions
possible possibilities possibility possibly impossibility impossible impossibly
post posted poster posters posting posts
pound pounds
power powered powerful powers
prepare preparation preparations prepared prepares preparing unprepared
present presence presentation presented presenting presently presents
president presidents presidential
press pressed presses pressing
pressure pressured pressures pressuring
pretty prettier prettiest prettily prettiness
prevent prevented preventing prevention prevents preventable preventative unpreventable
price priced prices pricing
private privately
problem problems problematic
produce produced producer producers produces producing
product products production productions productive productivity
profit profited profiting profits profitable
progress progressed progresses progressing progressive progressively
promise promised promises promising
proper properly improper improperly
property properties
propose proposal proposals proposed proposes proposing
protect protected protecting protection protections protective protects
prove proved proven proves proving unproven
proof proofs
provide provided provides providing provider providers
provision provisions
public publicity publicly
pull pulled pulling pulls
purpose purposes
put puts putting
q
quality qualities
quantity quantities
quarter quarterly quarters
queen queens
question questions questioned questioning questionable
quite
r
race racecourse raced races racing
raise raised raises raising
rank ranked ranking ranks
rate rated rates rating
rather
reach reached reaches reaching
read reader readers reading readings reads
ready readily
real realistic reality
realise realize realization realized realizes realizing realisation realisations realised realising realises
really
reason reasonable reasonably reasoned reasoning reasons
receive received receiver receives receiving
receipt receipts
recent recently
recognize recognise recognised recognises recognising recognition recognized recognizes recognizing
record recorded recording records
red redder reddest redness redden reddish
reduce reduced reduces reducing reduction reductions
refuse refusal refusals refused refuses refusing
regard disregard disregarded disregarding disregards regarded regarding regardless regards
relation relate related relates relating relations relationship relationships
relative relatively relatives
religion religions religious
remain remained remaining remainder remainders remains
remark remarked remarking remarks remarkable remarkably
remember remembered remembering remembers
reply replied replies replying
report reported reporter reporters reporting reports
represent representative representatives represented representing represents representation representations
republic republics republican republicans republicanism
reserve reserves reservation reservations reserved reserving
respect disrespect disrespectful respected respecting respects respectful respectable respectfully respective respectively irrespective irrespectively
rest rested resting restless restlessness rests
result resulted resulting results
return returned returning returns
rich richer richest richly richness riches
ride ridden rider riders rides riding rode
right rightful rightfully rightist rightists rightly rights
ring rang ringed ringing rings rung
rise rises rising rose
river rivers riverside
road roads roadside
rock rocky rocked rocking rocks
roll rolled rolling rolls roller rollers
room rooms
rough roughly roughness
round rounded rounder roundest roundly roundness rounds roundabout
royal royalty royally
rule ruled ruler rulers rules ruling
run ran runner runners running runs
safe safely safeness safer safest safety
sail sailed sailing sailings sailor sailors sails
sale sales
salt salty
same sameness
saturday saturdays
save saved saves saving savings
say said saying says
scarce scarcely scarcer scarcest scarcity
scene scenery scenes
school schooling schools
science sciences scientific scientist scientists scientifically
sea seaman seaside seamen seas
season seasons
seat seated seating seats
second secondary secondly seconds
secret secrecy secretly secrets
secretary secretaries
see saw seeing seen sees unseen
seem seemed seeming seems
sell seller sellers selling sells sold resell reselling resold
send sender senders sending sends sent
sense senseless senselessness senses sensible
sensitive sensitivity
separate separated separately separates separating separation separations separatist separatists
september sept
serious seriously seriousness
serve servant servants served serves serving servings
service services serviced servicing
set sets setting
settle settled settlement settlements settler settlers settles settling
seven seventeen seventeenth seventh seventies seventieth seventy
several
shadow shadowed shadowing shadows shadowy
shake shaken shakes shakily shaking shaky shook
shall shan
shape shaped shapes shaping shapeless
share shared shares sharing
she her hers herself
shine shined shines shining shone shiny
ship ships shipping shipped shipments shipment
shoot shooting shootings shoots shot shots
shore shores
short shortage shorten shortened shortening shortens shorter shortest shortly shortness
should shouldn
shoulder shoulders
show showed showing shown shows
side sides
sight sights
sign signature signatures signed signing signs
silence silenced silences silencing silent silently
silver
simple simpleness simpler simplest simplicity simplification simplified simplify simply
since
sing sings sung sang singer singers singing song songs
single singled
sir
sister sisters sisterly
sit sat sits sitting
situation situations situate situated
six sixes sixteen sixteenth sixteenths sixth sixthly sixths sixties sixtieth sixtieths sixty
size sizes sizing sized
sky skies
sleep sleeping sleeps sleepy slept sleepless
small smaller smallest smallness
smile smiled smiles smiling
snow snows snowed snowing
so
social socially
society societies
soft soften softened softening softens softer softest softly softness
soldier soldiers
some somebody somehow someone something sometime sometimes somewhere
son sons
soon sooner soonest
sort sorted sorting sorts
soul souls
sound sounds sounded sounding
south southeast southern southerners southward southwards southwest
space spaced spaces spacing
speak speaker speakers speaking speaks speech speeches spoke spoken
special specially specialist speciality specialities specialists specialize specialization specialized specializations
speed sped speeding speeds speedy
spend spending spends spent
spirit spirits spiritual
spite
spot spots spotted spotting
spread spreading spreads
spring sprang springing springs sprung
square squarely squareness squarer squares squarest
stage staging staged stages
stand outstanding standing stands stood
standard standards
star starred stars starring
start started starting starts
state stated statement statements states stating
station stations
stay stayed staying stays
steel
step stepped stepping steps
still stiller stillest stillness
stock stocked stocks
stone stoned stones stoning stony
stop stopped stopping stops
store stored stores storing
story stories
strange strangely strangeness stranger strangers strangest
stream streamed streaming streams
street streets
strength strengthen strengthened strengthening strengthens
strike strikes striking struck stroke
strong stronger strongest strongly
struggle struggled struggles struggling
study studied studies studying
student students
subject subjected subjecting subjects
substance substances substantial substantially substantive
succeed succeeded succeeding succeeds success successful successfully unsuccessful
such
suffer suffered suffering suffers
suggest suggested suggesting suggestion suggestions suggests
summer summers
sun sunlight sunny suns sunshine
sunday sundays
supply supplied supplier suppliers supplies supplying
support supported supporters supporting supports supportive
suppose supposed supposes supposing
sure surely sureness surer surest unsure
surface surfaced surfaces surfacing
surprise surprised surprises surprising surprisingly
surround surrounded surrounding surrounds
sweet sweetness sweetly sweets
sword swords
system systematic systems systematically
table tablecloth tables
take taken takes taking took
talk talked talking talks
tax taxes taxed taxing taxpayer taxpayers
teach taught teacher teachers teaches teaching teachings
tear tearing tears tore torn
tell retell retelling telling tells told
temple temples
ten tens tenth tenths
term terms
test tested testing tests
than
the
then
there
therefore
they their theirs them themselves
thing things
think thinking thinks thought thoughts thoughtful thoughtfully thoughtfulness
thirteen thirteenth thirteenths
thirty thirties thirtieth thirtieths
this these those that
though
thousand thousands thousandth thousandths
three threes third thirdly thirds
through throughout
throw threw throwing thrown throws
thursday thurs thursdays
thus
till
time timer times timeless timely
to
today
together
ton tons
too
top topped topping tops
total totaled totaling totalled totalling totally totals totality
touch touched touches touching untouched
toward towards
town towns
trade traded trades trading trader traders
train trained trainers training trains
travel traveled traveling travelled travellers travelling travels
tree trees
trouble troubled troubles troubling troublesome
true truthful truth truest truer truthfulness truly truths
trust trusted trusting entrust trusts
try tried tries trying trial trials trialing trialed
tuesday tues tuesdays
turn turned turning turns
twelve twelves twelfth twelfths
twenty twenties twentieth
two twice
type typed types typing typist typists
u
under underneath
understand understanding understands understood
union unions
unite united unites uniting unity unit units
university universities
unless
until
up upside
upon
use misused used useful usefulness useless uses using usefully user users
usual usually unusual unusually
v
valley valleys
value valuable valuables valuation valued valuer valueless values valuing invaluable invaluably
variety varieties
various variously
very
vessel vessels
victory victories victorious
view viewed viewing views
village villager villagers villages
virtue virtues virtuous
visit visited visiting visitor visitors visits visitation
voice voiced voices voicing voiceless
vote voted voter voters votes voting
w
wage wages unwaged
wait waited waiting waits waiter waiters waitress waitresses
walk walked walking walks
wall walled walls
want wanted wanting wants unwanted
war warred warring wars
watch watched watches watching
water watered waters watering
wave waved waves waving
way ways
we our ours ourselves us
wealth wealthy
wear wearing wears wore worn
wednesday wednesdays
week weekend weekends weekly weeks
welcome welcomed welcomes welcoming unwelcome
well wells
west westward westwards
western westerns
what whatever
when whenever
where wherever
whether
which whichever
while whilst
white whiteness whiter whitest whitish
who whoever whom whose
whole wholeness wholly
why
wide widely widened wideness widening wider widest width
wife wives
wild wilder wildest wildly wildness
will ll willing willingness willingly unwilling unwillingly
win winner winners winning wins won
wind winded winding winds windy
window windows
winter winters wintry
wise unwise wisdom wisely wiseness wiser wisest
wish wished wishes wishing
with
within
without
woman women
wonder wondered wonderful wondering wonders wonderfully
wood woods wooden woodland woody
word words wording
work worked worker workers working works workman workmen
world worlds
worth worthy worthless
would wouldn
wound wounds wounded wounding
write writer writers writes writing writings written wrote
wrong wronged wronging wrongs wrongly
y
year years yearly
yield yields yielded yielding
yes
yesterday
yet
you your yourselves yourself yours
young younger youngster youngest youngsters
youth youths youthful''')

gsl2unsplit = ('''
abroad
absence absences
absent
absolute
absolutely
accident accidents accidental accidentally
accuse accusing accuses accused
accustom accustoms accustoming accustomed
ache aching aches ached
admire admiring admires admired admirable admiration
advertise advertising advertises advertiser advertised advertisement advertisements
advice advisors advising advises advisers adviser advised advise advisory
aeroplane aeroplanes
afford afforded affording affords affordable
afraid
afternoon afternoons
agriculture agricultural
ahead
aim aims aiming aimed aimless aimlessness
airplane airplanes
alike
alive
aloud
altogether
ambition ambitions ambitious ambitiously
amuse amusing amuses amused amusement amusements
anger angers angering angered angry angrily angrier angriest
angle angles angling angled
annoy annoys annoying annoyed annoyance
anxiety anxieties anxious anxiously
apart
apologize apologizes apologized apologise apologising apologises apologised
apology apologies apologetic
applaud applauds applauding applauded
applause
apple apples
approve approving approves approved approval disapprove disapproving disapproves disapproved disapproval
arch arching arches arched
argue arguing argues argued arguable argument arguments
arrange arranged arranging arranges arrangement arrangements
arrest arrests arresting arrested
arrow arrows
artificial artificially
ash ashes
ashamed ashamedly
aside
asleep
astonish astonishing astonishes astonished astonishment
attend attends attending attended attendant attendance attendances
attention
attract attracts attracting attracted attractive attraction attractions attractively attractiveness
audience audiences
aunt aunty aunts
autumn
avenue avenues
avoid avoids avoiding avoided avoidance avoidable unavoidable
awake awaken awoken
awkward awkwardly
axe axing axes axed ax
baby babies
bag bags bagging bagged
baggage
bake baking bakes bakers baker baked
balance balancing balances balanced unbalanced
band banded banding bands
barber barbers
bare baring bares bared
barely
bargain bargains bargaining bargained
barrel barrels
basin basins
basket baskets
bath baths
bathe bathing bathes bathed
bay bays
beak beaks beaked
beam beams beamed beaming
bean beans
beard beards bearded
beast beasts
beat beats beating beaten
beg begs begging begged beggars beggar
behave behaves behaved behaving
behaviour behaviours behaviors behavioural behavior behavioral
bell bells
belt belts belting belted
bend bent bends bending
berry berries
bicycle bicycling bicycles bicycled
billion billions
bind binds binding binders binder
birth births birthdays birthday
bit bits
bite bites biting bitten
bitter bitterness bitterly bitterest bitterer
blade blades
blame blaming blames blamed blameless
bless blessed blesses blessing blessings
blind blinds blindly blinding blinded blindness
block blocks blocking blocked
boast boasts boasting boasted boastful
boil boils boiling boilers boiler boiled
bold boldness boldly boldest bolder
bone boning bones boned
border borders bordering bordered
borrow borrows borrowing borrowed
bottle bottling bottles bottled
bottom bottoms
bound bounds bounding bounded boundless
boundary boundaries
bow bows bowing bowed
bowl bowls bowling bowled
brain brains
brass
brave braving braves bravely braved bravery
breakfast breakfasts breakfasting breakfasted
breath breaths breathlessly breathless
breathe breathing breathes breathed
bribe bribing bribes bribed bribery
brick bricks
broadcast broadcasted broadcasting broadcasts
brown browns browning browned
brush brushing brushes brushed
bucket buckets
bunch bunches
bundle bundling bundles bundled
burst bursts bursting
bury burying buries buried
burial burials
bus bussing buses bussed
bush bushes bushy
busy busily busiest busier
butter butters buttering buttered
button buttons buttoning buttoned unbuttoned
cage caging cages caged
cake cakes
calculate calculator calculating calculates calculated calculation calculations
calm calms calmly calming calmed calmness
camera cameras
camp camped camping camps
canal canals
cap caps cappings capping capped
cape capes caped
card cards
carriage carriages
cart carts carting carted
cat cats
cattle
caution cautions cautioning cautioned cautious cautiously
cave caving caves caved
cent cents
centimetre centimetres
century centuries
ceremony ceremonies ceremonial
chain chains chaining chained
chair chairs chairman
chalk chalks
charm charms charming charmed
cheap cheapness cheaply cheapest cheaper
cheat cheats cheating cheated
check checks checking checked
cheer cheery cheers cheering cheerful cheered
cheese cheeses
cheque cheques
chest chests
chicken chickens
chimney chimneys
christmas christmases
civilise civilizing civilizes civilized civilize civilising civilises civilised civilisation civilisations
clay clays
clean cleaned cleaner cleaners cleanest cleaning cleanly cleans cleanness
clerk clerks
clever cleverness cleverly cleverest cleverer
cliff cliffs
climb climbs climbing climbers climber climbed
clock clocks
cloth cloths clothing clothes
club clubbed clubbing clubs
coarse coarsest coarser coarseness coarsely
coat coats
coffee coffees
collar collars
collect collects collecting collected collective collectively collector collectors collection collections
comb combs combing combed
combine combining combines combined combination combinations
comfort uncomfortable discomfort comforts comforting comforted comfortably comfortable
commerce commercial commercially
companion companions companionship
compare comparable compared compares comparative comparison comparisons comparing comparatively
compete competing competes competed
competition competitions
complain complaints complaint complains complaining complained
complicate complicated complicates complicating complication complications
compose composing composes composer composed composite composition
confess confessing confesses confessed confession confessions
confidence confidences confident confidently
confuse confusing confuses confused confusion
congratulate congratulating congratulates congratulated congratulations
connect connected connecting connects connection connections
conquer conquers conquerors conqueror conquering conquered conquest conquests
conscience consciences
conscious consciousness unconscious unconsciously consciously
convenience conveniences convenient conveniently
conversation conversations
cook cooks cooking cookers cooker cooked
cool cools coolness coolly cooling coolest cooler cooled
copper
copy copying copies copied
cork corks corking corked
corner corners cornered cornering
correct corrects correctly correcting corrected correctness correction corrections incorrect incorrectly
cottage cottages
cough coughs coughing coughed
courage courageous
cousin cousins
cow cows
coward cowards cowardly cowardice
crack cracks cracking cracked
crash crashing crashes crashed
cream creams creaming creamed
creature creatures
creep crept creeps creeping
crime crimes
criminal criminally
critic critics critically critical
crop crops cropping cropped
cruel cruelly cruelness cruellest crueller cruelty cruelties
crush crushing crushes crushed
cultivate cultivating cultivates cultivated cultivation
cup cups
cupboards cupboard
cure curing cures cured curable incurable
curious curiously curiosity
curl curls curling curled curly
curse cursing curses cursed
curtain curtains
curve curving curves curved
cushion cushions cushioned cushioning
custom customs customary
customer customers
damage damaging damages damaged undamaged
damp dampness dampest damper
dance danced dancer dancers dances dancing
dare dared dares daring
deaf deafness deafest deafer
debt debts
decay decays decaying decayed
deceive deceiving deceives deceived deception
decrease decreasing decreases decreased
deed deeds
deer
defend defence defends defending defenders defender defended
delay delays delaying delayed
delicate delicately delicacy delicacies
delight delights delighting delightfully delightful delighted
deliver delivered deliveries delivering delivers undelivered delivery
descend descends descending descended
deserve deserving deserves deservedly deserved
desk desks
despair despairs despairingly despairing despaired
devil devils
diamond diamonds
dictionary dictionaries
dig dug digs digging
dinner dinners dining dines dined dine
dip dips dipping dipped
dirt dirty
disappoint disappoints disappointing disappointed disappointment disappointments
discipline disciplining disciplines disciplined disciplinary
discuss discussing discusses discussed discussion discussions
disease diseases diseased
disgust disgusts disgusting disgusted
dish dishes
dismiss dismissing dismisses dismissed dismissive dismissively
disturb disturbs disturbing disturbed disturbance disturbances
ditch ditching ditches ditched
dive diving dives dived dove diver divers
donkey donkeys
dot dots
double doubled doubles doubling
dozen dozens
drag drags dragging dragged
drawer drawers
drown drowns drowning drowned
drum drums drumming drummed
duck ducks ducking ducked
dull dullness dullest duller
during
dust dusts dusting dusted duster dusters
eager eagerness eagerly
earn earns earning earned earnings
earnest earnestly
ease easing eases eased unease uneasy
edge edged edges edging
educate educating educates educated educator educators uneducated education educational
elastic elastics elasticity
elder elderly
electric electricity electricians electrician electrical electrically
elephant elephants
empty emptying empties emptied
enclose enclosing encloses enclosed enclosure
encourage encouragingly encouraging encourages encouraged encouragement
engine engines
engineer engineering engineers
entertain entertains entertaining entertained entertainment
entire entirely
envelope envelopes
envy envying envies envied envious
especial especially
essence essences
essential essentials essentially
evil eviler evilest evilly evilness evils
exact exactly
examining examines examined examine examiner examiners examination examinations
excellent excellence
excess excessive excessively
excite exciting excites excitedly excited excitement
excuse excusing excuses excused
explode exploding explodes exploded explosion explosions explosive
explore exploring exploration explores explored exploratory explorer explorers explorations
extra extras
extraordinary extraordinarily
extreme extremely
fade fading fades faded
faint faints faintly fainting fainter fainted faintness
false falsely falsehood
fan fans fanning fanned
fancy fancied fancier fancies fanciest fancily fanciness fancying
fashion fashionable fashioned fashioning fashions
fasten fastened fastener fasteners fastening fastens
fat fats fatten fatty
fate fates
fault faulty faults
feast feasts feasting feasted
feather feathers feathering feathered
female females
fence fencing fences fenced
fever feverish fevers
fierce fiercest fiercer fierceness fiercely
film films filming filmed
finger fingers
firm firms firmness firmly firmest
flag flags
flame flames flaming
flash flashing flashes flashed
flat flats flatten flattening
flavour flavours flavouring flavoured flavor flavors flavoring flavored
flesh
float floats floating floated
flood floods flooding flooded
flour
fold folds folding folded
fond fondness fondly fondest fonder
fool fools foolishness foolishly foolish fooling fooled
foot feet football footballs
forbid forbids forbidding forbidden
forgive forgiving forgives forgiven forgave
fork forks
formal formally formality
forward forwards
frame framing frames framed
freeze frozen freezing freezes
frequent frequents frequently frequenting frequented frequency infrequent infrequently
fright frights frightful frightens frightening frightened frighten
fruit fruits
fry frying fries fried
fun funny funniest funnier
funeral funerals
fur furs
gallon gallons
gap gaps
garage garages
gay gayness gayest gayer gaily gaiety
generous generously generosity
glory glories glorious
goat goats
govern govt governs governor governing governed government governments governmental
grace gracing graces gracefully graceful graced
gradual gradually
grain grains
gram grams
grammar grammars
grand grandsons grandson grandparents grandparent grandpa grandmother grandma grandfather granddaughters granddaughter grandchildren grandchild
grass grasses grassy
grateful gratefully
grave graves
grease greasing greases greased greasy
greed greedy greedily
greet greetings greets greeting greeted
grey
grind grinds grinding
guard guarded guarding guards
guess guessing guesses guessed
guest guests
guide guiding guides guided
guilty guiltily guilt guiltless
gun guns gunner
habit habits habitual habitually
hair hairy hairs
hall halls
hammer hammers hammering hammered
handkerchief handkerchiefs
handle handled handles handling
harbor harbours harbour harbors
harm harms harmless harming harmful harmed
harvest harvests harvesting harvester harvested
haste hastily hastens hastening hastened hasten
hat hats
hate hatred hating hates hated
hay
heal heals healing healed
health healthier healthiest healthily healthy
heap heaps heaping heaped
hesitate hesitating hesitates hesitated hesitation hesitations
hide hid hidden hides hiding
hinder hinders hindering hindered
hire hiring hires hired
hit hitting hitter hits
hole holes
holiday holidays
hollow hollows hollowing hollowed
holy holiness holiest holier
honest honesty honestly dishonest
hook hooks hooking hooked
horizon horizons
hospital hospitals
host hosts hosting hosted
hotel hotels
hullo hello hey hi
humble humbly humbling humbles humbled
hunger hungry hungrily hungers hungering
hunt hunts hunting hunters hunter hunted
hurrah
hurry hurrying hurries hurriedly hurried
hurt hurts hurting hurtful
hut huts
ice icy iced
ideal ideals ideally
idle idling idles idled idly
imagine imagining imagines imagined imagination imaginations imaginative imaginary
imitate imitating imitates imitated imitation imitations
immediate immediacy immediately
immense immensely
improve improving improves improved improvement improvements
inform informs informing informed information
informal informally
ink inks inky
inn inns
inquire inquiry inquiring inquiries inquires inquired enquire enquiry enquiring
insect insects
inside insider insiders
instant instantly
instrument instruments instrumental
insult insults insulting insulted
insure insuring insures insured insurance
intend intended intending intends intent intently intention intentions intentional intentionally
interfere interfering interferes interfered interference
international internationally
interrupt interrupts interrupting interrupted
invent invents inventors inventor inventing invented invention inventions
invite inviting invites invited invitation invitations
inward inwardly
island islands
jaw jaws
jealous jealously jealousy
jewel jewels jewellers jeweller jewellery
joke jokes joked joking
journey journeys journeying journeyed
juice juices juicy
jump jumps jumping jumped
key keys
kick kicks kicking kicked
kilogram kilograms
kilometre kilometres
kiss kissing kisses kissed
kitchen kitchens
knee knees
kneel kneels kneeling kneeled
knife knives
knock knocks knocking knocked
knot knotting knotted knots
ladder ladders
lamp lamps
lazy laziness lazily laziest lazier
leaf leafy
lean leans leaning leaned
leather leathers
leg legs
lend lent lends lending
lesson lessons
liberty liberties
lid lids
limb limbs
liquid liquids
list unlisted lists listed listing
litre litres
load unloads unloading unloaded loads loading loaded
loaf loaves
loan loans
lock unlocks unlocking unlocked unlock locks locking locked
lodging lodgings
log logs
lone lonely loneliness
loose loosely loosen
lot lots
loud loudness loudly loudest louder
loyal loyalty loyally
luck lucky luckily luckiest luckier unlucky unluckily
lump lumps
lunch lunches
lung lungs
mad madness madly maddest madder madman
mail mails mailing mailed
male males
manage managing manages managers manager managed management
map maps
mat mats
match matching matches matched
meal meals
meantime
meanwhile
meat meats
mechanic mechanics mechanical mechanically
medicine medicines medic
melt melts melting melted
mend mends mending mended
merchant merchants
mercy merciful mercies
merry merriness merriest merrier merrily
message messages
messenger messengers
metre metres
mild mildness mildly mildest milder
mill mills milling miller milled
milligram milligrams
millilitre millilitres
millimetre millimetres
mineral minerals
miserable miserably
mistake mistaking mistakes mistakenly mistaken unmistakably unmistakable
mix mixtures mixture mixing mixes mixed
model models modelling modelled modeling modeled
moderate moderately moderation
modest modesty modestly
monkey monkeys
motion motions motioning motioned motionless
mouse mice
mud muddy
multiply multiplying multiplies multiplied multiple multiplication
murder murders murdering murderers murderer murdered
mystery mysteriously mysterious mysteries
nail nails nailing nailed
narrow narrowed narrower narrowest narrowing narrowly narrowness narrows
neat neatness neatly neatest neater
neck necks
needle needling needles needled
neglect neglects neglecting neglected
nephew nephews
nest nests nesting nested
net nets
nice nicest nicer niceness nicely
niece nieces
noise noisy noisily noises
nonsense nonsensical
noon
nose noses
noun nouns
nuisance nuisances
nurse nursing nurses nursed
nut nuts
oar oars
obey obeys obeying obeyed obedience obediently obedient disobey disobeyed disobeying
ocean oceans
offend offenses offense offends offending offended offensive offensively inoffensive inoffensively
omit omitting omitted omits omission omissions
onwards onward
oppose opposing opposes opposed
opposite opposites
orange oranges orangish
organ organs
origin origins originates originated original originally originality
ornament ornaments ornamental
outline outlined outlines outlining
overcome overcoming overcomes overcame
pack packs packing packed package packages
pad pads padding padded
pain pains painful painfully
pair pairs pairing paired
pale paling pales paled paleness
pan pans
parcel parcels parcelled
pardon pardons pardoning pardoned unpardonable
parent parents parental parentage
park parks parking parked
permanent permanently
passage passages
passenger passengers
paste pasting pastes pasted
path paths
patient patiently patience
patriotic
pattern patterns patterned
pause pausing pauses paused
paw paws
pearl pearls
peculiar peculiarly peculiarity peculiarities
pen pens
pencil pencils
penny pennies
perfect perfected perfecting perfectly perfects perfection
perform performs performing performers performed performance performances
persuade persuasion persuades persuaded persuading persuasive persuasively
pet pets
photograph photography photographs photographing photographers photographer photographed
pick picks picking pickers picker picked
pig pigs
pigeon pigeons
pile piling piles piled
pin pins pinned pinning
pinch pinching pinches pinched
pink pinkness pinkest pinker
pint pints
pipe pipes
pity pitying pities pitied
plane planes
plaster plasters plastering plastered
plate plates
plenty plentiful
plough ploughs ploughing ploughed
plural plurals
pocket pockets
poem poetry poetic poet poems
poison poisons poisonous poisoning poisoned
police policing policewomen polices policemen policeman policed
polish polishing polishes polished
polite politest politer politeness
pool pools pooling
postpone postponing postpones postponed
pot potting potted pots
pour pours pouring poured
powder powders powdery
practical practically
practise practises practised practising practice practices
praise praising praises praised
pray prays praying prayers prayer prayed
preach preaching preaches preachers preacher preached
precious
prefer prefers preferring preferred preferable preference preferences preferential
prejudice prejudices prejudiced unprejudiced
preserve preserved preserves preserving preservation
pretend pretends pretending pretended pretence
pride prides
priest priests
print printed printers printing prints reprint reprints reprinting reprinted
prison prisons prisoners prisoner imprison
prize prized prizes
probable probably probability probabilities improbable
procession processions
profession professions
programme program programed programing programmed programmes programming programs
prompt prompts promptly prompting prompted
pronounce pronouncing pronounces pronounced
proud proudly proudest prouder
pump pumps pumping pumped
punctual punctually punctuality
punish punishing punishes punished punishment punishments
pupil pupils
pure purest purer pureness purely impure impurity
purple purplish
push pushing pushes pushed
puzzle puzzling puzzles puzzled
qualify qualifying qualifies qualified qualification qualifications
quarrel quarrels quarrelling quarrelled quarreling quarreled
quart quarts
quick quickness quickly quickest quicker
quiet quieter quietest quietly quietness
rabbit rabbits
radio radios radioed
rail railways railway rails railroads railroad
rain rains raining rained raindrops raindrop
rake raking rakes raked
rapid rapidly rapidity
rare rarest rarer rareness rarely
rat rats
raw rawness rawest rawer
ray rays
razor razors
recommend recommends recommending recommended recommendation recommendations
refer refers referring referred
reflect reflects reflecting reflected reflective reflection reflections
refresh refreshes refreshing refreshed refreshment
regular irregular regularly irregularly
regret regretting regretful regretted regrets
rejoice rejoicing rejoices rejoiced
relieve relieving relieves relieved relief
remedy remedying remedies remedied
remind reminds reminding reminded reminder
rent renting rented rents
repair repairs repairing repaired
repeat repeated repeatedly repeating repeats
replace replacing replaces replaced replacement replacements replaceable irreplaceable
reproduce reproduces reproducing reproduced reproduction reproductions
reputation reputations
request requests requesting requested
rescue rescuing rescues rescued
resign resigns resigning resigned resignation resignations
resist resists resisting resisted resistible resistance
responsible irresponsible responsibility responsibilities
restaurant restaurants
retire retiring retires retired retirement
revenge revenges
review reviews reviewing reviewed
reward rewards rewarding rewarded
ribbon ribbons
rice
rid rids ridding ridded
ripe ripest riper ripeness
risk risks risking risked risky
rival rivals rivalry rivalries rivalling rivalled
roar roars roaring roared
roast roasts roasting roasted
rob robs robbing robber robbed robbers
rod rods
roof roofs
root roots rooted
rope ropes
rot rotting rotted rots rotten
row rows rowing rowed
rub rubs rubbing rubbed
rubber rubbers
rubbish
rude rudest ruder rudeness rudely
rug rugs
ruin ruined ruining ruins
rush rushed rushes rushing
rust rusty rusts rusting rusted
sacred sacredness
sacrifice sacrificing sacrifices sacrificed sacrificial
sad sadness sadly saddest sadder sadden
saddle saddling saddles saddled
sake sakes
salary salaries
sample sampling samples sampled
sand sandy sands
satisfy satisfying satisfies satisfied satisfactory satisfaction dissatisfaction dissatisfying dissatisfy dissatisfies dissatisfied
sauce sauces
saucer saucers
saws sawing sawed
scale scales
scatter scatters scattering scattered
scent scents scenting scented
scissors
scold scolds scolding scolded
scorn scorns scorning scorned scornful scornfully
scrape scraping scrapes scraped
scratch scratching scratches scratched
screen screens screening screened
screw screws screwing screwed
search searching searches searched
seed seeds seeding seeded seedling
seize seized seizes seizing
seldom
self selfishness selfishly selfish selves
sentence sentences
severe severity severest severer severeness severely
sew sews sewn sewing sewed
shade shadings shading shades shaded
shallow shallowness shallowest shallower
shame shaming shames shameful shamefully shamed
sharp sharpness sharply sharpest sharper sharpens sharpening sharpened sharpen
shave shaved shaving shaves
sheep
sheet sheets
shelf shelves
shell shells shelling shelled
shelter shelters sheltering sheltered
shield shields shielding shielded
shilling shillings
shirt shirts
shock shocks shocking shocked
shoe shoed shoeing shoes
shop shops shopping shoppers shopper shopped
shout shouted shouting shouts
shower showers showering showered
shut shutting shuts
sick sickness sickly sickest sicker
signal signals signalling signalled
silk silks
sincere sincerely sincerity
sink sunk sinks sinking sank
skill skilled skills skilful skilfully
skin skins skinning skinned
skirt skirts
slave slaves slavery
slide sliding slides slid
slight slighted slighter slightest slighting slightly slights
slow slowed slower slowest slowing slowly slows
slip slips slipping slipped
slope sloping slopes sloped
smell smelt smells smelling smelled
smoke smoking smokes smokers smokeless smoked
smooth smooths smoothly smoothing smoothed
snake snakes
soap soaps
sock socks
soil soiled soiling soils
solemn solemnly
solid solidify solidly solids
solve solving solves solved solution solutions
sore sores
sorry sorriness sorriest sorrier
soup soups
sour sours sourly souring soured
sow sows sowing sowed
spade spades
spare sparing spares spared
spell spelt spells spelling spelled misspelt
spill spills spilling spilled
spin spun spins spinning
spit spits spitting spat
splendid splendidly
split splitting splits
spoil spoils spoiling spoiled
spoon spoons spoonful
sport sporting sports
staff staffs
stain stains staining stained
stairs upstairs downstairs
stamp stamps stamping stamped
steady unsteady unsteadily steadying steadily steadies steadied
steal stole stolen steals stealing
steam steams steaming steamed
steep steepness steepest steeper
steer steers steering steered
stem stems stemmed
stick sticking sticks stuck
stiff stiffness stiffest stiffer stiffens stiffening stiffened stiffen
sting stung stings stinging
stir stirs stirring stirred
stocking stockings
stomach stomachs
storm stormed storming storms
stove stoves
straight straightened straightening straightens straighter straightest
strap straps strapping strapped
straw straws
stretch stretched stretches stretching
strict strictness strictly strictest stricter
string strings stringing stringed
strip strips stripped stripping
stripe stripes striped striping
stuff stuffs stuffing stuffed
stupid stupidity stupidly stupidest stupider
suck sucks sucking sucked
sudden suddenly suddenness
sugar sugars sugary
suit suits suiting suited suitability suitable unsuitable
supper suppers
suspect suspects suspecting suspected unsuspecting
suspicion suspicions suspicious suspiciously
swallow swallows swallowing swallowed
swear sworn swore swears swearing
sweat sweats sweating sweated
sweep swept sweeps sweeping
swell swollen swells swelling swelled
swim swum swims swimming swam
swing swung swings swinging
sympathy sympathies sympathetic sympathetically
tail tails
tailor tailors tailoring tailored
tall tallest taller
tame taming tames tamed
tap taps tapping tapped
taste tasted tastes tasting
taxi taxis
tea teas
telegraph telegraphs telegraphing telegraphed
telephone telephoning telephones telephoned phones phoning phoned phone
temper tempers
temperature temperatures
tempt tempts tempting tempted
tend tends tended tendency tendencies
tender tenderness tenderly
tent tents
terrible terribly
thank thanks thanking thankfully thankful thanked
theatre theatres theatrical
thick thickness thickly thickest thicker
thief thieves
thin thins thinning thinnest thinness thinner thinned thinly
thirst thirsts
thorn thorns
thorough thoroughness thoroughly
thread threads threading threaded
threat threats threatens threatening threatened threaten
throat throats
thumb thumbs
thunder thunders thundering thundered
ticket tickets
tide tides tidal
tidy tidying tidies tidied
tie untied untie tying ties tied
tight tightness tightest tighter tightly tightens tightening tightened tighten
tin tins
tip tips tipping tipped
tire tiring tires tired
title titled titles
tobacco tobaccos
toe toes
tomorrow
tongue tongues
tonight
tool tools
tooth teeth toothless
tough toughness toughest tougher
tour tours touring toured tourist tourists
towel towels
tower towers towering
toy toys
track tracks tracking tracked
translate translating translates translated translation translations
trap traps trapping trapped
tray trays
treasure treasuring treasures treasured treasury treasurer
treat treats treating treated treatment treatments
tremble trembling trembles trembled
tribe tribes
trick trickster tricks tricking tricked
trip trips tripping tripped
trunk trunks
tube tubes
tune tuning tunes tuned
twist twists twisting twisted
typical typically
ugly ugliness ugliest uglier
umbrella umbrellas
uncle uncles
universe universal
upper
upright
upset upsetting upsets
upwards upward
urge urging urges urged
vain vainly vainest vainer
veil veils veiling veiled
verb verbs
verse verses
violent violently violence nonviolent
vowel vowels
voyage voyaging voyages voyaged
waist waists
wake woke waking wakes waken woken
wander wanders wandering wandered
warm warms warmly warming warmed warmth
warn warned warning warns
wash washed washes washing
waste wasted wastes wasting wasteful wastefully
wax waxing waxes waxed
weak weakly weakness weaken
weapon weapons
weather weathers weathering weathered
weave wove weaving weaves weaved
weed weeds weeding weeded
weigh weights weight weighs weighing weighed
wet wetting wets
wheat wheats
wheel wheels wheeler wheeled
whip whips whipping whipped
whisper whispers whispering whispered
whistle whistling whistles whistled
wicked wickedness wickedest wickeder wickedly
widow widows widower widowed
wine wining wines wined
wing wings winging winged
wipe wiping wipes wiped wiper wipers
wire wiring wires wired
witness witnessing witnesses witnessed
wool wools woollen woolly
worm worms worming wormed
worry worrying worries worried
worse worst worsen
worship worshipping worships worshipped
wrap wrapping wraps wrapper wrappers wrapped
wreck wrecked wrecking wrecks
wrist wrists
yard yards
yellow yellowish
zero zeros''')

#Stopword list from NLTK stopwords corpus
stopwords = (''' i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now''')

import string, re

from Tkinter import *
root = Tk()
root.geometry("1000x600")
root.title("Text Grader")

p = re.compile(r'\W+')

#set up lists
BNC1=string.split(base1unsplit)
BNC2=string.split(base2unsplit)
BNC3=string.split(base3unsplit)
AWL= string.split(awlunsplit)
GSL1 = string.split(gsl1unsplit)
GSL2=string.split(gsl2unsplit)
filterlist = string.split(filterlistunsplit.lower())

#set up allfiles
BNC_ALL = BNC1 + BNC1 + BNC3 + filterlist
GSLAWL_ALL = GSL1+ GSL2 + AWL + filterlist

#define
def OpenFile():
    import tkFileDialog
    resultsbox.delete(1.0,END)
    text.delete(1.0,END)
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        data = file.read()
        for word in data:
            if "\r" in word and not "\n" in word:
                resultsbox.insert(END, word)
                resultsbox.insert(END, "\n")
            else:
                resultsbox.insert(END, word)

def SaveResults():
    from time import gmtime, strftime
    reftime = strftime("%b_%d_%Y__%H_%M_%S")
    f = open("RESULTS_"+reftime+".txt", 'a')    
    notes = resultsbox.get(1.0, END)
    notes = notes.encode('utf-8')
    f.write(notes)
    f.close()

def GradeTextGSL():
    text.delete(1.0, END)
    data = resultsbox.get(1.0,END)    
    data = data.replace("\n", " ghj789 ")
    resultsbox.delete(1.0, END)
    rawtext = string.split(data)    
    text.insert(END, "INDEX: \n")
    text.insert(END, "GSL1 words are this colour\n", "BNC1")
    text.insert(END, "GSL2 words are this colour \n", "BNC2")
    text.insert(END, "AWL words are this colour\n", "BNC3")
    text.insert(END, "Numbers, web addresses and anything in your filterlist including names are marked this colour \n", "name")
    text.insert(END, "Anything offlist - not in the above lists - is this colour \n", "offlist")
    for token in rawtext:
            checktokensplit = p.split(token)
            checktoken = checktokensplit[0]    
            if checktoken.startswith("ghj789"):
                token = "\n"
            if not checktoken.isalpha() and not len(checktokensplit) < 2:
                checktoken=checktokensplit[1]
            if checktoken.isdigit():
                resultsbox.insert(END, token, "name")
                resultsbox.insert(END, " ")
            elif checktoken.startswith("http"):
                resultsbox.insert(END, token, "name")
                resultsbox.insert(END, " ")    
            elif checktoken.lower() in AWL:  
                    resultsbox.insert(END, token, "BNC3")
                    resultsbox.insert(END, " ")
            elif checktoken.lower() in GSL2:   
                    resultsbox.insert(END, token, "BNC2")
                    resultsbox.insert(END, " ")
            elif checktoken.lower() in GSL1:   
                    resultsbox.insert(END, token, "BNC1")
                    resultsbox.insert(END, " ")
            elif checktoken.lower() in filterlist:   
                    resultsbox.insert(END, token, "name")
                    resultsbox.insert(END, " ")
            else:
                    resultsbox.insert(END, token, "offlist")
                    resultsbox.insert(END, " ")    
    


def GradeTextBNC():
    text.delete(1.0, END)
    data = resultsbox.get(1.0,END)
    data = data.replace("\n", " ghj789 ")
    resultsbox.delete(1.0, END)
    rawtext = string.split(data)
    text.insert(END, "INDEX: \n")
    text.insert(END, "BNC1 tokens are this colour\n", "BNC1")
    text.insert(END, "BNC2 tokens are this colour \n", "BNC2")
    text.insert(END, "BNC3 tokens are this colour\n", "BNC3")
    text.insert(END, "Numbers, web addresses and anything in your filterlist including names are this colour \n", "name")
    text.insert(END, "Anything offlist -  not in the above lists - are this colour \n", "offlist")    
    
    
    for token in rawtext:
            checktokensplit = p.split(token)
            checktoken = checktokensplit[0]
            if checktoken.startswith("ghj789"):
                token = "\n"
            if not checktoken.isalpha() and not len(checktokensplit) < 2:
                checktoken=checktokensplit[1]
            if checktoken.isdigit():
                resultsbox.insert(END, token, "name")
                resultsbox.insert(END, " ")
            elif checktoken.startswith("http"):
                resultsbox.insert(END, token, "name")
                resultsbox.insert(END, " ")
            elif checktoken.lower() in BNC3:  
                    resultsbox.insert(END, token, "BNC3")
                    resultsbox.insert(END, " ")
            elif checktoken.lower() in BNC2:   
                    resultsbox.insert(END, token, "BNC2")
                    resultsbox.insert(END, " ")
            elif checktoken.lower() in BNC1:   
                    resultsbox.insert(END, token, "BNC1")
                    resultsbox.insert(END, " ")
            elif checktoken.lower() in filterlist:   
                    resultsbox.insert(END, token, "name")
                    resultsbox.insert(END, " ")
            else:
                    resultsbox.insert(END, token, "offlist")
                    resultsbox.insert(END, " ")

def ShowCollocations():
	text.insert(END, "If this doesn't work, please check you have NLTK, PyYAML and the stopword list from the NLTK loaded. See Help for details \n\n\n")
	import nltk
	from nltk.collocations import BigramCollocationFinder
	from nltk.collocations import TrigramCollocationFinder
	from nltk.metrics import BigramAssocMeasures
	from nltk.metrics import TrigramAssocMeasures
	pattern = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''
	data = resultsbox.get(1.0,END)
	rawtext=nltk.regexp_tokenize(data, pattern)
	prepcolloc = [word.lower() for word in rawtext if not word in stopwords and word.isalpha()]
	text.delete(1.0, END)
	text.insert(END, "Collocations (occurring at least 3 times with a PMI of 10)\n")
	text.insert(END, "\nBigram Collocations:\n")
	bigram = BigramAssocMeasures()
	bigramfinder = BigramCollocationFinder.from_words(prepcolloc)
	bigramfinder.apply_freq_filter (3)
	bigrams=bigramfinder.nbest(bigram.pmi, 10)
	for item in bigrams:
		first = item[0]
		second = item[1]
		text.insert(END, first)
		text.insert(END, " ")
		text.insert(END, second)
		text.insert(END, "\n")

    
	text.insert(END, "\nTrigram Collocations: Coming soon\n")
	'''
	trigram = TrigramAssocMeasures()
	trigramfinder = TrigramCollocationFinder.from_words(prepcolloc)
	trigramfinder.apply_word_filter(filter_stops)
	trigramfinder.apply_freq_filter (3)
	trigrams=trigramfinder.nbest(trigram.pmi, 10)
	print trigrams
	for item in trigrams:
		first = item[0]
		second = item[1]
		third = item[2]
		text.insert(END, first)
		text.insert(END, " ")
		text.insert(END, second)
		text.insert(END, " ")
		text.insert(END, third)
		text.insert(END, "\n")
    '''
def ShowReadability():
    text.insert(END, "If this doesn't work, NLTK and the Punkt Sentence Tokenizer installed. See Help for details \n\n\n")
    import nltk
    pattern = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''
    data = resultsbox.get(1.0,END)
    rawtext=nltk.regexp_tokenize(data, pattern)
    prepcolloc = (w.lower() for w in rawtext)
    text.delete(1.0, END)
    #sentences
    sentcountshort = 0
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(data)    
    for sent in sents:
        if len(sent) < 2:
            sentcountshort = sentcountshort+1
    
    numsents = len(sents) - sentcountshort
    numwords = len(p.split(data))-1
    sentcountshort = 0
    
    text.insert(END, "\nIgnoring one word sentences (like numbering), there are ")
    text.insert(END, numsents)
    text.insert(END, " sentences with an average of ")
    averagewordspersentence = numwords/numsents
    text.insert(END, averagewordspersentence)
    text.insert(END, " words per sentence.\n\n")

    text.insert(END, "READABILITY\n")

    #set up syllable dictionary        
    from math import sqrt as squareroot
    from nltk.corpus import cmudict
    syllables = dict()
    numeral = re.compile(r'\d')
    for (word, phonemes) in cmudict.entries():
        word = word.lower()
        count = len([x for x in list(''.join(phonemes)) if x >= '0' and x <= '9'])
        if syllables.has_key(word):
            count = min(count, syllables[word])
        syllables[word] = count        

    #count syllables    
    numsyllables=0
    wordsnotincmu=dict()
    for word in prepcolloc:
        if word in syllables:
            numsyllables = numsyllables + syllables[word]
    else:
        wordsnotincmu[word] = 1
        
    #count three syllable words
    threesyllcount=0
    for word in prepcolloc:
        if word in syllables and syllables[word] > 2:
            threesyllcount = threesyllcount + syllables[word]
        

    #calculate number of letters and numbers
    letnumcount=0
    for word in rawtext:
        if word.isalpha():
            letnumcount=letnumcount + len(word)        

    #adapted from Java at http://www.editcentral.com/gwt1/EditCentral.html
    #Flesch    
    Flesch = 206.835 - (1.015 * numwords) / numsents - (84.6 * numsyllables) / numwords
    
    #Automated readability index
    ARI = (4.71 * letnumcount) / numwords + (0.5 * numwords) / numsents -21.43;
    
    #Flesch-Kincaid grade level
    FK = (0.39 * numwords) / numsents + (11.8 * numsyllables) / numwords - 15.59;
    
    #Coleman-Liau index
    CL = (5.89 * letnumcount) / numwords - (30.0 * numsents) / numwords - 15.8;
    
    #gunning fog
    GunningFog = 0.4 * ( numwords / numsents + (100.0 * threesyllcount) / numwords );
    
    #SMOG
    smog = squareroot( threesyllcount * 30.0 / numsents ) + 3.0;
    #
    text.insert(END, "Flesch: ")
    text.insert(END, Flesch)
    text.insert(END, "\n")
    text.insert(END, "Automated readability index: ")
    text.insert(END, ARI)
    text.insert(END, "\n")
    text.insert(END, "Flesch-Kincaid grade level")
    text.insert(END, FK)
    text.insert(END, "\n")

    text.insert(END, "Coleman-Liau index: ")
    text.insert(END, CL)
    text.insert(END, "\n")

    text.insert(END, "Gunning fog index: ")
    text.insert(END, GunningFog)
    text.insert(END, "\n")

    text.insert(END, "Smog: ")
    text.insert(END, smog)
    text.insert(END, "\n\n")
    
    text.insert(END, "These words were not included in readability stats because the syllable count is missing from the cmudict database")
    text.insert(END, "\n")
    for k,y in sorted(wordsnotincmu.items()):
        text.insert(END, k)

    
def ShowInfo():
	import nltk
	datalist=[]
	infoBNC1list=[]
	infoBNC2list=[]
	infoBNC3list=[]
	infoofflist=[]
	infoBNC1familylist=[]
	infoBNC2familylist=[]
	infoBNC3familylist=[]
	infoofflistfamily=[]
	p = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''
	l = re.compile("\n")

	text.delete(1.0, END)    
	data = resultsbox.get(1.0,END)


	#Clean and lower text
	rawtext= nltk.regexp_tokenize(data.lower(), p)
	punctuation=re.compile("\W")
	number=re.compile("\d")
	websiteaddressremoved = 0
	punctuationremoved=0 
	numberremoved=0
	filterremoved=0
	for token in rawtext:
			if token.startswith("http"):
				token=""
				websiteaddressremoved = websiteaddressremoved + 1
			elif punctuation.match(token):
				token=""    
				punctuationremoved=punctuationremoved+1        
			elif number.match(token):
				token=""
				numberremoved=numberremoved+1    
			elif token in filterlist:
				print token
				token=""
				filterremoved = filterremoved+1
			else:
				datalist.append(token)                
	

	text.insert(END, "\n Website addresses cleaned: ")
	text.insert(END, websiteaddressremoved)
	text.insert(END, "\n Punctuation marks removed: ")
	text.insert(END, punctuationremoved)
	text.insert(END, "\n Digits removed: ")
	text.insert(END, numberremoved)
	text.insert(END, "\n Tokens removed using filterlist (see terminal for list): ")
	text.insert(END, filterremoved)
	text.insert(END, "\n\n")



	for line in l.split(base1unsplit):
		words = nltk.regexp_tokenize(line, p)
		for word in words:
			if word in datalist:
				infoBNC1list.append(word)
				infoBNC1familylist.append(words[0])
			
	for line in l.split(base2unsplit):
		words = nltk.regexp_tokenize(line, p)
		for word in words:
			if word in datalist:
				infoBNC2list.append(word)
				infoBNC2familylist.append(words[0])
			
	for line in l.split(base3unsplit):
		words = nltk.regexp_tokenize(line, p)
		for word in words:
			if word in datalist:
				infoBNC3list.append(word)
				infoBNC3familylist.append(words[0])


	ALLlists = infoBNC1list + infoBNC2list + infoBNC3list
	ALLfamilylists = infoBNC1familylist + infoBNC2familylist + infoBNC3familylist

	offcount=0
	for token in datalist:
		if token not in ALLlists:
			infoofflist.append(token)
			offcount=offcount+1

	#Set up counts    
	BNC1count=0
	BNC2count=0
	BNC3count=0
	for word in datalist:
		if word in infoBNC1list:
			BNC1count=BNC1count+1
		elif word in infoBNC2list:
			BNC2count=BNC2count+1
		elif word in infoBNC3list:
			BNC3count=BNC3count+1

	text.insert(END, "Number of word tokens: ")
	text.insert(END, str(len(datalist)))
	text.insert(END, "\n")
	text.insert(END, 'Number of word types in text: ')
	text.insert(END, str(len(set(datalist))))
	text.insert(END, "\n")
	text.insert(END, 'Number of recognisable word BNC1-3 families in text: ')
	text.insert(END, str(len(set(ALLfamilylists))))
	text.insert(END, "\n")
	text.insert(END, 'Lexical richness: ')
	text.insert(END, str((len(datalist) / len(set(datalist)))))
	text.insert(END, "\n\n")    

	rawlength =  len(datalist)
	rawsetlength = len(set(datalist))
	bnc1length = BNC1count
	bnc1setlength= len(set(infoBNC1list))
	bnc1familylength = len(set(infoBNC1familylist))
	bnc2length= BNC2count
	bnc2setlength=len(set(infoBNC2list))
	bnc2familylength = len(set(infoBNC2familylist))
	bnc3length= BNC3count
	bnc3setlength=len(set(infoBNC3list))
	bnc3familylength = len(set(infoBNC3familylist))
	offlistlength= offcount
	offlistsetlength=len(set(infoofflist))
	totalfamilieslength = len(ALLfamilylists)

	text.insert(END, 'From BNC List 1 (first 1000 word families) there are  '),
	text.insert(END, str(bnc1length))
	text.insert(END, ' tokens (')
	text.insert(END, str(100 * bnc1length / rawlength))
	text.insert(END, '%), ')
	text.insert(END, str(bnc1setlength))
	text.insert(END, ' types (',)
	text.insert(END, str(100 * bnc1setlength / rawsetlength))
	text.insert(END, '%) and ')
	if totalfamilieslength > 0: 
		text.insert(END, str(bnc1familylength))
		text.insert(END, ' of the recognisable families (')
		text.insert(END, str(100 * bnc1familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC1familylist)))), "BNC1")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')
	
	text.insert(END, 'From BNC List 2 (second 1000 word families) there are  '),
	text.insert(END, str(bnc2length))
	text.insert(END, ' tokens (')
	text.insert(END, str(100 * bnc2length / rawlength))
	text.insert(END, '%),  ')
	text.insert(END, str(bnc2setlength))
	text.insert(END, ' types (',)
	text.insert(END, str(100 * bnc2setlength / rawsetlength))
	text.insert(END, '%) and ')
	if totalfamilieslength > 0: 
		text.insert(END, str(bnc2familylength))
		text.insert(END, ' of the recognisable families (')
		text.insert(END, str(100 * bnc2familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC2familylist)))), "BNC1")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')

	text.insert(END, 'From BNC List 3 (third 1000 word families) there are  '),
	text.insert(END, str(bnc3length))
	text.insert(END, ' tokens (')
	text.insert(END, str(100 * bnc3length / rawlength))
	text.insert(END, '%),  ')
	text.insert(END, str(bnc3setlength))
	text.insert(END, ' types (',)
	text.insert(END, str(100 * bnc3setlength / rawsetlength))
	text.insert(END, '%) and ')
	if totalfamilieslength > 0: 
		text.insert(END, str(bnc3familylength))
		text.insert(END, ' of the recognisable families (')
		text.insert(END, str(100 * bnc3familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC3familylist)))), "BNC1")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')

	text.insert(END, 'Tokens NOT in any BNC list account for '),
	text.insert(END, str(offlistlength))
	text.insert(END, ' tokens (')
	text.insert(END, str(100 * offlistlength / rawlength))
	text.insert(END, '%) and ')
	text.insert(END, str(offlistsetlength))
	text.insert(END, ' types (',)
	text.insert(END, str(100 * offlistsetlength / rawsetlength))
	text.insert(END, '%):')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((infoofflist)))), "offlist")
	text.insert(END, "\n\n")    


	#set up missing lists
	BNC1missing=[]
	for line in l.split(base1unsplit):
		words = nltk.regexp_tokenize(line, p)
		familycount=0
		for word in words:
			if word in infoBNC1familylist:
				familycount=familycount+1
			if familycount < 1:
				BNC1missing.append(words[0])
	text.insert(END, 'From BNC List 1, the following ')
	text.insert(END, str(len(set(BNC1missing))))
	text.insert(END, ' families are missing.')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC1missing)))), "BNC1")
	text.insert(END, "\n\n")    


	#Commented out unless you need to seed BNC2 and 3  
	BNC2missing=[]
	for line in l.split(base2unsplit):
		words = nltk.regexp_tokenize(line, p)
		familycount=0
		for word in words:
			if word in infoBNC2familylist:
				familycount=familycount+1
			if familycount < 1:
				BNC2missing.append(words[0])
	text.insert(END, 'From BNC List 2, these ')
	text.insert(END, str(len(set(BNC2missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC2missing)))), "BNC2")
	text.insert(END, "\n\n")    

	BNC3missing=[]
	for line in l.split(base3unsplit):
		words = nltk.regexp_tokenize(line, p)
		familycount=0
		for word in words:
			if word in infoBNC3familylist:
				familycount=familycount+1
			if familycount < 1:
				BNC3missing.append(words[0])
	text.insert(END, 'From BNC List 3, these ')
	text.insert(END, str(len(set(BNC3missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC3missing)))), "BNC3")
	text.insert(END, "\n\n")    


def ShowHelp():
    text.delete(1.0, END)
    text.insert(END, "If you want to use the collocation or readability functions, you need to install the Natural Language Toolkit (NLTK)\n 1) Install the Natural Language ToolkitNLTK, along with the other programs it needs - instructions at http://www.nltk.org/download.\n 2) Install the Punkt package - http://www.nltk.org/data") 


#PACK interface
                
textframe = Frame(root, bd=5, height="100", relief=SUNKEN)
resultsframe = Frame(root, bd=5, relief=SUNKEN)
buttonframe = Frame(root, bd=5, relief=SUNKEN)

BNC_button = Button(buttonframe, text="BNC",command = GradeTextBNC)
GSL_button = Button(buttonframe, text="GSL/AWL",command = GradeTextGSL)
info_button = Button (buttonframe, text="Word Lists", command = ShowInfo)
collocations_button = Button(buttonframe, text="Collocations", command = ShowCollocations)
readability_button = Button(buttonframe, text="Readability", command = ShowReadability)
openfile_button = Button(buttonframe, text="Open File", command = OpenFile)
save_button = Button(buttonframe, text="Save to File", command = SaveResults)
help_button = Button (buttonframe, text="Help", command = ShowHelp)


#text = Text(textframe, borderwidth=5)

textscrollbar = Scrollbar(textframe, orient=VERTICAL)
text = Text(textframe, yscrollcommand=textscrollbar.set, takefocus=0)
textscrollbar.configure(command=text.yview)


resultsscrollbar = Scrollbar(resultsframe, orient=VERTICAL)
resultsbox = Text(resultsframe, yscrollcommand=resultsscrollbar.set, takefocus=0)
resultsscrollbar.configure(command=resultsbox.yview)

resultsbox.tag_configure('BNC1', foreground='black')
#BNC1 also tag for GSL1
resultsbox.tag_configure('BNC2', foreground='green')
#BNC2 also tag for GSL2
resultsbox.tag_configure('BNC3', foreground='orange')
#BNC3 also tag for AWL
resultsbox.tag_configure('offlist', foreground='red')
resultsbox.tag_configure('name', foreground='pink')

text.tag_configure('BNC1', foreground='black')
text.tag_configure('BNC2', foreground='green')
text.tag_configure('BNC3', foreground='orange')
text.tag_configure('offlist', foreground='red')
text.tag_configure('name', foreground='pink')


text.pack(side=RIGHT, fill=BOTH, expand=1)
textscrollbar.pack(side=RIGHT, fill=Y)
BNC_button.pack(side=LEFT)
GSL_button.pack(side=LEFT)
info_button.pack(side=LEFT)
collocations_button.pack(side=LEFT)
readability_button.pack(side=LEFT)
save_button.pack(side=LEFT)
openfile_button.pack(side=LEFT)
help_button.pack(side=LEFT)
resultsbox.pack(side=LEFT,fill=BOTH, expand=1)
resultsscrollbar.pack(side=RIGHT, fill=Y)
buttonframe.pack(fill=X, expand=1)
textframe.pack(fill=X)
resultsframe.pack(fill=BOTH, expand=1)
buttonframe.focus()
resultsbox.insert(END, "Open a text (TXT) file using the buttons above, paste text here, or just start typing")
text.insert(END, "Information will appear here after you run the program")
root.mainloop()
    


