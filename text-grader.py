 #!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org

# Copyright 2011 Malcolm Prentice
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

#Define filter lists - names or any other words you want excluded from analysis
filterlistunsplit = ('''Malcolm Prentice ''')

# Define and convert the word lists
base1unsplit = ('''a an
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

base2unsplit = ('''above
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


base3unsplit = ('''abbey abbeys
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


awlunsplit = ('''abandon abandoned abandoning abandonment abandons
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

gsl1unsplit = ('''a an
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

gsl2unsplit = ('''abroad
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

bnccoca1unsplit = ('''a an
able abilities ability abler ablest ably inability unable
about
above
absolute absolutely absolutes absolutism absolutist absolutists
accept acceptability acceptable acceptably acceptance acceptances accepted accepting acceptor acceptors accepts unacceptability unacceptable unacceptably
across
act acted acting action actionable actioned actioning actions actor actors actress actresses acts inaction unactioned
actual actualisation actualisations actualise actualised actualises actualising actualities actuality actualization actualizations actualize actualized actualizes actualizing actually
add added adding addition additional additionality additionally additions additive additives adds
address addressed addressee addressees addresses addressing
admit admits admittance admittances admitted admittedly admitting readmit readmits readmittance readmitted readmitting
advertise ad ads advert advertised advertisement advertisements advertiser advertisers advertises advertising advertize advertized advertizement advertizements advertizer advertizers advertizes advertizing adverts
afford affordability affordable afforded affording affords unaffordable
afraid unafraid
after afterward afterwards
afternoon afternoons
again
against
age aged ageing ageism ageist ageists ageless ager agers ages aging underage
ago
agree agreeable agreeably agreed agreeing agreement agreements agrees
ahead
air aired airier airiest airily airiness airing airings airless airs airy midair
all
allow allowable allowance allowances allowed allowing allows
almost
alone
along
already
alright alrighty
also
although
always allus
amaze amazed amazement amazes amazing amazingly
among amongst
amount amounted amounting amounts
and ands
angry angrier angriest angrily angriness
animal animals
another
answer answerable answered answering answers unanswerable unanswered
any anybody anyhow anymore anyone anythin anything anyway anyways anywhere owt
apart
apparent apparently
appear appearance appearances appeared appearing appears reappear reappearance reappearances reappeared reappearing reappears
area areas
arm armful armfuls arms
around
arrange arranged arrangement arrangements arranger arrangers arranges arranging prearrange prearranged prearranges prearranging rearrange rearranged rearrangement rearrangements rearranges rearranging
arrive arrival arrivals arrived arrives arriving
art artist artistic artistically artistries artistry artists arts arty
as
ashamed ashamedly unashamed unashamedly
ask aske asked asking asks unasked
at
aunt aunthood auntie aunties aunts aunty
autumn autumnal autumns
aware awareness unaware unawares
away aways
awful awfully awfulness
baby babby babies babyish
back backed backer backers backing backs backward backwardness backwardnesses backwards
bad baddie baddies baddy badly badness
bag bagful bagfuls baggage bagged bagging bags
ball balled balling balls
bank banked banker bankers banking banks
bar barred barring bars unbarred
base based baseless baser bases basest basing
basic basically basics
bath baths
be ain am are aren been beens bein being beings innit is isn m re s tis twas was wasn were weren wert wuz
beach beached beaches beaching
bear bearable bearably bearer bearers bearing bearings bears bore borne unbearable unbearably
beat beaten beater beaters beating beatings beats unbeatable unbeaten
beauty beauteous beautician beauticians beauties beautification beautified beautifies beautiful beautifully beautify
because cos coz
become became becomes becoming
bed bedded bedding beds
before
begin began beginner beginners beginning beginnings begins begun
behind
believe believable believed believer believers believes believing unbelievable unbelievably unbeliever unbelievers unbelieving unbelievingly
below
beneath
beside besides
best
bet bets betting
better bettered bettering betterment betterments betters
between betweens
beyond
big bigger biggest biggish bigness
bill billed billing bills
billion billions billionth billionths
bird birdie birdied birdies birdlike birds birdy
birth birthed birthing births rebirth rebirths
bit bits bitty
black blacked blacken blackened blackening blackens blacker blackest blacking blackish blackly blackness blacks
blood blooded bloodied bloodier bloodies bloodiest bloodiness bloodless bloodlessly bloodlessness bloods bloody bloodying
blow blew blowed blower blowers blowing blown blows
blue blueness bluer blues bluest bluey bluish
board boards
boat boated boating boats
body bodied bodies bodily
bone boned boneless bones boney bonier boniest boniness boning bony
book bookish booklet booklets books
boring bored boredom bores boringly
born reborn unborn
both
bother bothered bothering bothers bovver
bottle bottled bottles bottling unbottled
bottom bottomed bottoming bottomless bottoms
box boxes
boy boyhood boyish boys
bread breads
break breakable breakage breakages breaker breakers breaking breaks broke broken brokenly unbreakable unbroken
breakfast breakfasted breakfasting breakfasts
breath breathless breathlessly breathlessness breaths breathy
bright brighten brightened brightening brightens brighter brightest brightly brightness
bring bringer bringers bringing brings brought
brother bro bros brotherhood brotherhoods brotherly brothers
brown browned browner brownest browning brownish browns browny
build builder builders building buildings builds built prebuilt rebuild rebuilding rebuilds rebuilt unbuilt
burn burnable burned burner burners burning burnings burns burnt unburnable
bus buses bussed busses bussing
bush bushes bushy
business businesses businesslike unbusinesslike
busy busied busier busies busiest busily busying busyness
but buts
buy bought buyer buyers buying buys
by bys
cake cakes
call called caller callers calling calls uncalled
camp camped camper campers camping camps
can cannot
car cars
card carding cards
care cared careful carefully carefulness careless carelessly carelessness carer carers cares caring uncared uncaring
carry carried carrier carriers carries carrying
case cases
cat catlike cats
catch catcher catchers catches catching catchy caught uncaught
cause causation causative caused causes causing
centre center centered centering centerist centerists centers central centralisation centralise centralised centralises centralising centralism centralist centralists centralities centrality centralization centralize centralized centralizes centralizing centrally centred centredness centres centric centring centrist centrists
certain cert certainly certainties certainty uncertain uncertainly uncertainties uncertainty
chair chairs
chance chanced chances chancing mischance
change changeable changed changer changers changes changing unchangeable unchangeably unchanged unchanging
charge chargeable charged chargee chargees charger chargers charges charging uncharged
cheap cheapen cheapened cheapening cheapens cheaper cheapest cheaply cheapness
check checked checker checkers checking checks unchecked
chicken chick chickened chickening chickens chicks
child childhood childhoods childish childishly childishness childless childlessness childlike children childrens
chip chipped chipping chippings chips
choice choices choicest
choose chooses choosing choosy chose chosen unchosen
christmas christmases christmassy
church churches
city cities
class classed classes classier classiest classiness classing classless classlessness classy subclass subclasses
clean cleaned cleaner cleaners cleanest cleaning cleanliness cleanly cleanness cleans unclean uncleanliness
clear clearance clearances cleared clearer clearest clearing clearings clearly clearness clears unclear
climb climbed climber climbers climbing climbs unclimbed
clock clocked clocker clockers clocking clocks oclock
close closely closeness closer closest
closed closes closing unclosed
clothes clothe clothed clothing unclothed unclothing
club clubbed clubber clubbers clubbing clubs
coat coated coating coatings coats
coffee coffees
cold colder coldest coldish coldly coldness colds
collect collectable collectables collected collecting collection collections collective collectively collectives collectivism collectivist collectivists collectivities collectivity collectivization collector collectors collects uncollected
college colleges collegian collegians
colour color coloration colorations colored coloreds colorful colorfully coloring colorings colorless colors colouration colourations coloured coloureds colourful colourfully colouring colourings colourist colourists colourless colours
come came comer comers comes cometh comin coming comings
comfort comfortable comfortably comforted comforting comfortingly comforts uncomfortable uncomfortably uncomforted
company co companies
complete completed completely completeness completes completing completion completions incomplete incompletely incompleteness uncompleted
computer computable computation computational computationally computations compute computed computerisation computerise computerised computerises computerising computerization computerize computerized computerizes computerizing computers computes computing
concern concerned concerning concerns unconcern unconcerned
consider consideration considerations considered considering consideringly considers reconsider reconsideration reconsiderations reconsidered reconsidering reconsiders unconsidered
continue continual continually continuance continuation continuations continued continues continuing continuities continuity continuous continuously
control controllable controlled controller controllers controlling controls uncontrollable uncontrollably uncontrolled
conversation conversant conversational conversationalist conversationalists conversationally conversations converse conversed converses conversing
cook cooked cooker cookeries cookers cookery cooking cooks overcooked overcooking uncooked
cool coolant coolants cooled cooler coolers coolest cooling coolly coolness cools uncool uncooled
corner cornered cornering corners
cost costed costing costings costless costlier costliest costly costs
could couldn
count countable counted counting countless counts recount recounted recounting recounts uncountable uncounted
country countries
couple coupled couples coupling couplings uncoupled
course courses
court courted courting courts
cover coverage covered covering coverings coverlet coverlets covers uncover uncovered uncovering uncovers
crazy crazier crazies craziest crazily craziness
crime crimes
cross crossed crosses crossing crossings crosslike crossly crossness uncrossed
cry cried crier criers cries crying
cup cuplike cupped cupping cups
cut cuts cutter cutters cutting cuttings uncut
dad daddies daddy dads
dance danceable danced dancer dancers dances dancing
danger dangerous dangerously dangers endanger endangered endangering endangerment endangerments endangers
dark darken darkened darkener darkeners darkening darkens darker darkest darkie darkies darkly darkness darky
darling darlin darlings
date datable dated dates dating undated
daughter daughters
day dailies daily daylight daylights days midday
dead deaden deadened deadening deadens deadlier deadliest deadly undead
deal dealer dealers dealership dealerships dealing dealings deals dealt undealt
dear dearer dearest dearie dearly dears
death deathless deathlessly deathlike deathly deaths
decide decided decidedly decider deciders decides deciding undecided
deep deepen deepened deepening deepens deeper deepest deeply depth depths
definite definitely indefinite indefinitely
degree deg degrees
delicious deliciously deliciousness
depend dependability dependable dependably dependant dependants depended dependent dependents depending depends undependable
die died dies dying undying
difference differences
different differently
difficult difficulties difficulty
dig digger diggers digging digs dug undug
dinner dinners
dirty dirt dirtier dirtiest
discover discovered discoverer discoverers discoveries discovering discovers discovery rediscover rediscovered rediscoveries rediscovering rediscovers rediscovery undiscovered
do did didn doer doers does doesn doin doing doings don done redid redo redoes redoing redone undid undo undoes undoing undone
doctor doc docs doctored doctoring doctors dr
dog doggie doggies doggy dogs
door doors indoor indoors outdoor outdoors
double doubled doubles doubling doubly redouble redoubled redoubles redoubling
doubt doubted doubter doubters doubtful doubtfully doubting doubtless doubts undoubtably undoubted undoubtedly
down downed downing downings downs downward downwards
draw drawing drawings drawn draws drew redraw redrawing redrawn redraws redrew undrawn
dream dreamed dreamer dreamers dreamily dreaming dreamless dreamlessly dreamlike dreams dreamt dreamy undreamed undreamt
dress dressed dresses dressing dressings undress undressed undresses undressing
drink drank drinkable drinker drinkers drinking drinks drunk drunks undrunk
drive driven driver drivers drives driving drove
drop droplet droplets dropped dropper droppers dropping droppings drops
drug drugged druggie druggies drugging drugs
dry dried drier driers dries driest drily dryer dryers drying dryly dryness
during
each
ear eared earful earless ears
early earlier earliest earliness
earth earthed earthen earthly earths earthy unearthliness unearthly
east easterlies easterly eastward eastwards
easy easier easiest easily easiness
eat ate eaten eater eaters eating eats uneaten
edge edged edger edges edgewise edging
educate educated educates educating education educational educationalist educationalists educationally educationist educationists educations educative educator educators miseducated uneducated
egg eggs
eight eighteen eighteenth eighteenths eighth eighths eighties eightieth eightieths eights eighty
either
eleven elevens eleventh elevenths
else elsewhere
employ employability employable employed employee employees employer employers employing employment employments employs unemployable unemployed unemployment
empty emptied empties emptiness emptying
end ended ending endings endless endlessly ends unended unending
engine engined engines
enjoy enjoyable enjoyed enjoying enjoyment enjoys unenjoyable
enough
enter entered entering enters unentered
especially especial
even
evening evenings
ever
every everybody everyday everydayness everyone everything everytime everywhere
exact exactly exactness inexact inexactness
except cept cepting excepted excepting
excite excitable excitably excitation excitations excited excitedly excitement excitements exciter exciters excites exciting unexciting
excuse excusable excused excuses excusing inexcusable
expect expectancies expectancy expectant expectantly expectation expectations expected expectedly expecting expects unexpected unexpectedly unexpectedness
expensive expensively inexpensive inexpensively inexpensiveness
experience experienced experiences experiencing experiential experientially inexperience inexperienced
explain explained explainer explainers explaining explains explanation explanations explanatory unexplained
express expressed expresses expressible expressing expression expressionless expressionlessly expressions expressive expressively expressiveness expressly inexpressible unexpressed
extra extras
eye eyed eyeful eyefuls eyeing eyeless eyelet eyelets eyes
face faced faceless faces facing facings
fact factly facts
fair fairer fairest fairly fairness unfair unfairly unfairness
fall fallen falling falls fell
family familial families subfamilies subfamily
far farther farthest
farm farmed farmer farmers farming farms unfarmed
fast faster fastest
fat fatless fatly fatness fats fatten fattened fattening fattens fatter fattest fattier fattiest fattiness fattish fatty
father fathered fatherhood fathering fatherless fatherly fathers
favourite favorite favorites favoritism favourites favouritism
fear feared fearful fearfully fearing fearless fearlessly fearlessness fears unfeared
feed fed feeder feeders feeding feeds unfed
feel feeler feelers feeling feelings feels felt unfeeling
fellow fella fellas fellows fellowship fellowships
few fewer fewest
field fielded fielder fielders fielding fields midfielder midfielders
fight fighter fighters fighting fights fought
figure fig figs figural figuration figurations figured figures figuring figurings
fill filled filler fillers filling fillings fills refill refillable refilled refilling refills unfilled
film filmed filming films filmy
final finalise finalised finalises finalising finalist finalists finality finalize finalized finalizes finalizing finally finals semifinalist semifinalists
find finder finders finding findings finds found unfound
fine finely fineness finer finery finest
finger fingered fingering fingers
finish finished finisher finishers finishes finishing unfinished
fire fired fires firing misfire misfired misfires misfiring
first firstly firsts
fish fished fisheries fishers fishery fishes fishier fishiest fishily fishiness fishing fishy
fit fitness fits fitted fitter fitters fittest fitting fittingly fittings unfit unfitness unfitted unfitting
five fifteen fifteenth fifteenths fifth fifthly fifths fifties fiftieth fiftieths fifty fives
fix fixable fixed fixedly fixer fixers fixes fixing fixings fixity unfixed
flat flatly flatness flatten flattened flattening flattens flattest flattish
floor floored flooring floorings floors
flower flowered flowerer flowerers flowerier floweriest floweriness flowering flowers flowery
fly flew flier fliers flies flown flyer flyers flying unflown
follow ff followed follower followers following follows
food foods
foot feet footed footer footers ft
football footballer footballers footballing footballs footie footies
for fer
force forced forceful forcefully forces forcible forcibly forcing unforced
forest forested forester foresters foresting forestry forests
forget forgetful forgetfully forgetfulness forgets forgettable forgetting forgot forgotten unforgettable unforgotten
form formed forming formless formlessness forms preform preformed preforming preforms unformed
fortunate fortunately unfortunate unfortunately unfortunates
forward forwarded forwarder forwarders forwarding forwards
four forties fortieth fortieths forty fortyish fours fourteen fourteenth fourteenths fourth fourthly fourths
free freed freedom freedoms freeing freely freer frees freest unfree unfreed
freeze freezable freezer freezers freezes freezing froze frozen unfrozen
fresh freshen freshened freshener fresheners freshening freshens fresher freshest freshly freshness
friday fri fridays
friend friendless friendlier friendlies friendliest friendliness friendly friends friendship friendships unfriendliest unfriendly
fright frighten frightened frightener frighteners frightening frighteningly frightens frightful frightfully frights
from
front forefront forefronts frontage frontages frontal frontally fronted fronting frontmost fronts frontwards
full fuller fullest fullness fully
fun funnier funnies funniest funnily funny
further furtherance furthered furtherest furthering furthers furthest futherer
game games gaming
garden gardened gardener gardeners gardening gardens
gas gaseous gases gassed gassing
general generalisabilty generalisable generalisation generalisations generalise generalised generalises generalising generalist generalists generalities generality generalizabilty generalizable generalization generalizations generalize generalized generalizes generalizing generally
gentle gentleness gentler gentlest gently
get gets gettin getting got gotcha gotta gotten
girl gal gals girlhood girlie girlies girlish girlishly girlishness girls girly
give gave gimme given giver givers gives giving ungiven
glad gladden gladdened gladdening gladdens gladder gladdest gladly gladness
glance glanced glances glancing
glass glasses glassier glassiest glassily glassiness glassy
go goer goers goes goin going goings gone goner goners gonna gunna went
god goddess goddesses godless godlike godliness godly gods
gold golden
good gidday goodday gooder gooders goodies goodly goodness goody
goodbye bye goodbyes
govern gov governed governing government governmental governments governor governors governorship governorships governs govt intergovernmental misgoverned misgoverning misgoverns ungovernable
grandfather gran grandad grandads grandchild grandchildren granddad granddads granddaughter granddaughters grandfathers grandma grandmas grandmother grandmothers grandpa grandparent grandparents grandpas grandpop grandpops grandson grandsons grans
grass grassed grasses grassing grassless grasslike grassy
great greater greatest greatly greatness greats
green greener greenest greening greenish greenness greens greeny
grey gray grayed graying grayish grayly grayness grays greyer greyest greying greyish greyly greyness greys
ground foreground foregrounded foregrounding foregrounds grounded grounding groundless grounds ungrounded
group grouped grouping groupings groups intergroup regroup regrouped regrouping regroups subgroup subgroups ungrouped
grow grew grower growers growing grown grows growth growths regrow regrowth
guess guessable guessed guesses guessing unguessable
gun gunless gunned gunner gunners gunnery gunning guns
guy guys
hair haired hairless hairs hairy
half halfs halves
hall halls
hand handed handedly handedness hander handers handful handfuls handing hands
handle handled handler handlers handles handling mishandle mishandled mishandles mishandling
hang hanged hanger hangers hanging hangings hangs hung unhung
happen happened happening happenings happens
happy happier happiest happily happiness unhappier unhappiest unhappily unhappiness unhappy
hard harden hardened hardener hardeners hardening hardens harder hardest hardness hardship hardships
hardly
hat hatful hatfuls hats hatted hatter hatters
hate hated hateful hatefully hatefulness hater haters hates hating
have d had hadn hadst has hasn hast hath haven haves having ve
he him himself his
head headed headedness heading headings headless heads headship headships subheading subheadings
health healthfully healthfulness healthier healthiest healthily healthy unhealthier unhealthiest unhealthy
hear heard hearer hearers hearing hearings hears mishear misheard mishearing mishears reheard rehearing unheard
heart dishearten disheartened disheartening disheartens hearted heartedly heartedness hearten heartened heartening heartens heartless heartlessly heartlessness hearts
heat heated heatedly heater heaters heating heats preheat preheated preheating preheats reheat reheated reheating reheats unheated
heavy heavier heavies heaviest heavily heaviness
hell hellish hellishly hellishness hells
hello allo hallo hey hi hullo
help helped helper helpers helpful helpfully helpfulness helping helpings helpless helplessly helplessness helps unhelpful unhelpfully
here
hide hid hidden hider hiders hides hiding unhidden
high higher highest highly highs
hill hills hilly
history historian historians historic historical historically historicism historicist historicists historicity histories prehistories prehistory
hit hits hitter hitting mishit mishits unhit
hold held holder holders holding holdings holds unheld
hole holed holes holing
holiday holidayed holidayer holidayers holidaying holidays hols
home homed homeless homelessness homes homeward homewards homing
honest honestly honesty
honour hon honor honorable honorably honorary honored honorific honoring honors honourable honourably honourary honoured honouring honours hons
hope hoped hopeful hopefully hopefulness hopefuls hopeless hopelessly hopelessness hoper hopers hopes hoping
horrible horribleness horribly orrible
horse horses horsey horsy unhorsed
hospital hospitalisation hospitalise hospitalised hospitalises hospitalising hospitalization hospitalize hospitalized hospitalizes hospitalizing hospitals
hot hotly hotness hots hotted hotter hottest hotting
hour hourly hours hr hrs
house housed houses housing rehouse rehoused rehouses rehousing unhoused
how hows
however
huge hugely hugeness
human humanism humanist humanistic humanists humanity humanly humanness humans inhuman inhumanity nonhuman nonhumans
hundred hundreds hundredth hundredths
hunger hungered hungering hungers hungrier hungriest hungrily hungry
hunt hunted hunter hunters hunting huntress hunts
hurry hurried hurriedly hurries hurrying unhurried unhurriedly
hurt hurter hurters hurtful hurtfully hurtfulness hurting hurts unhurt
husband husbands
i me meself mine my myself
ice iced icily icy
idea ideas
if ifs
imagine imaginable imaginably imaginary imagination imaginations imaginative imaginatively imagined imagines imagining imaginings unimaginable unimaginably unimaginative unimaginatively unimagined
important importantly unimportant
in inner innermost inward inwardly inwardness inwards
indeed
inform info informant informants information informational informed informer informers informing informs misinform misinformation misinformations misinformed misinforming misinforms uninformed
inside insider insiders insides
instead
insure insurable insurance insurances insured insurer insurers insures insuring reinsurance reinsure reinsured reinsures reinsuring uninsurable uninsured
interest interested interestedly interesting interestingly interests uninterested uninteresting
internet
into
involve involved involvement involvements involves involving uninvolved
island islander islanders islands
issue issuance issued issuer issuers issues issuing
it its itself
job jobber jobbers jobbery jobless jobs
join joined joining joins rejoin rejoined rejoining rejoins
joke joked joker jokers jokes jokey joking jokingly
judge judged judgement judgemental judgements judges judging judgment judgmental judgments misjudge misjudged misjudgement misjudgements misjudges misjudging prejudge prejudged prejudgement prejudgements prejudges prejudging
jump jumped jumper jumpers jumping jumps jumpy
just
keep keeper keepers keepin keeping keeps kept
key keyed keying keys
kick kicked kicker kickers kicking kicks
kid kids
kill killed killer killers killing killings kills
kind kinda kinds
king kingdom kingdoms kingly kings kingship kingships
kiss kissed kisser kisses kissing unkissed
kitchen kitchenette kitchenettes kitchens
knock knocked knocker knockers knocking knocks
know dunno knew knowable knowed knowing knowingly known knows unknowable unknowing unknowingly unknown unknowns
lady ladies ladylike ladyship ladyships unladylike
lake lakes
land landed landing landings landless lands landward landwards
large largeish largely larger largest largish
last lastly
late lately lateness later latest
laugh laughable laughably laughed laughing laughingly laughs
law lawful lawfully lawfulness lawless lawlessness laws unlawful unlawfully
lay laid lain laying lays
lazy lazier laziest lazily laziness
lead leader leaderless leaders leadership leaderships leading leads led mislead misleading misleadingly misleads misled
learn learned learnedly learner learners learning learns learnt relearn relearned relearning relearns unlearn unlearned
least
leave leaver leavers leaves leaving
left lefthand lefthanded lefthander lefthanders leftist leftists leftmost lefts leftward leftwards
leg legged legging leggings leggy legless legs
less lessen lessened lessening lessens lesser
let lemme lets letting
letter lettered lettering letterings letters unlettered
level leveled leveler leveling levelled leveller levellers levelling levelly levels
lie liar liars lied lies lying
life lifeless lifelessly lifelike lifes midlife
lift lifted lifter lifters lifting lifts
light lighted lighters lighting lights lit unlit
like dislike disliked dislikes disliking likeable likeably liked likes liking
line lined lines unlined
lip lipped lips
list listed listing listings lists unlisted
listen listened listener listeners listening listenings listens
little leetle littleness littler littlest
live lived lives living livings
load loaded loader loaders loading loadings loads reload reloaded reloading reloads unload unloaded unloading unloads
local localisation localise localised localises localising localism localization localize localized localizes localizing locally locals
lock lockable locked locking locks unlock unlocked unlocking unlocks
long longer longest longish
look looked looker lookin looking looks unlooked
lord lorded lording lordly lords lordship lordships
lose loser losers loses losing lost
lot lots
loud louder loudest loudly loudness
love lovable loveable loved loveless lover lovers loves lovey loveys loving lovingly luv luvs unlovable unloved
lovely lovelier loveliest loveliness unlovely
low lowish lowlier lowliest lowly lows
luck luckier luckiest luckily luckless lucky unluckier unluckiest unluckily unlucky
lunch lunched lunches lunching
machine machined machinery machines machining machinist machinists
mad madden maddened maddening maddeningly maddens madder maddest madding madly madness
main mainly mains
major majored majoring
make made maker makers makes making makings remade remake remakes remaking unmade unmake
man manfully manhood manliness manly manned manning mannish mans men mens unmanned
manage manageable managed management managements manager manageress manageresses managerial managers manages managing mismanage mismanaged mismanagement mismanages mismanaging unmanageable
many
mark marked markedly marker markers marking markings marks unmarked
market marketability marketable marketed marketeer marketeers marketer marketers marketing markets nonmarket
marry intermarriage intermarriages intermarried intermarries intermarry intermarrying marriage marriageable marriages married marries marrying remarriage remarriages remarried remarries remarry remarrying unmarriageable unmarried
master mastered masterful mastering masterly masters mastery
matter mattered mattering matters
may
maybe
meal meals
mean meaning meaningful meaningfully meaningfulness meaningless meaninglessness meanings means meant
meet meeting meetings meets met unmet
member members membership memberships
mention mentioned mentioning mentions unmentionable unmentioned
mess messed messes messier messiest messily messiness messing messy
middle middles middling
might mightn
mile mileage mileages miles
milk milked milking milks milky
million millions millionth
mind minded mindedly mindedness minder minders mindful mindfulness minding mindless mindlessly mindlessness minds
minute min mins minutes
miss missed misses missing unmissed
mistake mistaken mistakenly mistakes mistaking mistook unmistakable unmistakably unmistakeable unmistakeably
mister mr
moment momentarily momentary moments
monday mon mondays
money moneyed moneys monied monies
month monthly months
more
morning morn mornin mornings
most mostly
mother mothered motherhood mothering motherly mothers
mountain mountaineer mountaineering mountaineers mountainous mountains mountainside mountainsides
mouth mouthed mouthful mouthfuls mouthing mouthings mouths mouthy
move immovable immoveable movable moveable moved movement movements mover movers moves moving movingly unmovable unmoveable unmoved unmoving
movie movies
mrs missis missus missuses
much
mum mam mammies mammy mams mom mommies mommy moms mummy mums
music musical musically musicals musician musicians musicianship musics
must mustn
name misnamed misnaming named nameless namely names naming rename renamed renames renaming renamings unnamed
nation national nationalisation nationalisations nationalise nationalised nationalising nationalism nationalisms nationalist nationalistic nationalistically nationalists nationalization nationalize nationalized nationalizing nationally nationals nationhood nationhoods nations nationwide
nature natural naturalism naturalist naturalistic naturalistically naturalists naturally naturalness natured naturedly natures unnatural unnaturally
naughty naughtier naughtiest naughtily naughtiness
near nearby neared nearer nearest nearing nearly nearness nears nearside
neat neater neatest neatly neatness
necessary necessaries necessarily unnecessarily unnecessary
neck necked necking necks
need needed needful needing needless needlessly needn needs unneeded
neighbour neighbor neighborhood neighborhoods neighboring neighborliness neighborly neighbors neighbourhood neighbourhoods neighbouring neighbourliness neighbourly neighbours
never
new newer newest newish newly newness renew renewable renewables renewal renewals renewed renewing renews
news newsy
next
nice nicely niceness nicer nicest
night nightly nights nts
nine niner niners nines nineteen nineteenth nineteenths nineties ninetieth ninetieths ninety ninth ninths
no noes
nobody nobodies
noise noiseless noiselessly noises noisier noisiest noisily noisy
none
normal normalisation normalise normalised normalises normalising normality normalization normalize normalized normalizes normalizing normally
north ne nne nnw northerlies northerly northernmost northward northwards northwest nw
nose nosed noseless noses nosing
not nots nt t
note notable notables notably noted notes noting
nothing nothin nothingness nothings nowt nuffink
notice noticeable noticeably noticed notices noticing unnoticeable unnoticed
now
number nos numbered numbering numberless numbers renumber renumbered renumbering renumbers unnumbered
nurse nursed nurses nursing
obvious obviously obviousness
odd odder oddest oddities oddity oddly oddness odds
of
off offs orf
offer offered offeree offerees offerer offerers offering offerings offeror offerors offers
office offices
officer officers
often oft
oil oiled oiler oilers oiliness oiling oils oily unoiled
ok okay okey
old olde olden older oldest oldie oldies oldish oldy
on onto
once
one noone oneness ones oneself
only
open opened opener openers opening openings openly openness opens reopen reopened reopening reopens unopened
or ors
orange orangeish oranges orangey orangish orangy
order ordered ordering orderlies orderliness orderly orders reorder reordered reordering reorders unordered
other otherness others
ought oughta oughtn
out outer outs outside outsider outsiders outsides outta outward outwardly outwards
over overly
own
owned owner owners ownership owning owns
pack package packaged packages packaging packed packer packers packing packs unpack unpacked unpacking unpacks
page pages pp
pain pained painful painfully painfulness paining painless painlessly painlessness pains
paint painted painter painterly painters painting paintings paints repaint repainted repainting repaintings repaints unpainted
pair paired pairing pairings pairs unpaired
paper papered papering paperless papers papery
pardon pardonable pardoned pardoning pardons unpardonable
parent parentage parental parented parenthood parenting parentless parents
park parked parking parks
part parted partial partially parting partly parts pt pts
particular particularisation particularise particularised particularises particularising particularism particularisms particularistic particularities particularity particularization particularize particularized particularizes particularizing particularly particulars
party partied parties partying
pass impassable impassably passable passably passed passer passers passes passing
past pasts
pay paid payable payed payee payees payer payers paying payment payments pays prepaid prepay prepayment prepayments unpaid
penny pence pennies penniless
people peopled peoples peopling
perfect imperfect imperfection imperfections imperfectly perfected perfecting perfection perfectionism perfectionist perfectionists perfections perfectly perfects
perhaps
person interpersonal personal personalism personalistic personally personhood persons
photograph photo photographed photographer photographers photographic photographically photographing photographs photography photos
pick picked picker pickers picking pickings picks picky unpick unpicked unpicking unpicks
picture pic pics pictured pictures picturing
piece pieced pieces piecing
place placed placement placements places placing placings unplaced
plan planned planner planners planning plans unplanned
plant planted planter planters planting plantings plants replant replanted replanting replants unplanted
play playability playable played player players playful playfully playfulness playing plays replay replayed replaying replays unplayable
please pleased pleases pleasing pleasingly unpleased unpleasing
plenty plentiful plentifully
plus pluses
point midpoint midpoints pointed pointedly pointer pointers pointing pointless pointlessly pointlessness points pointy
police policed polices policing
poor poorer poorest poorly poorness
pop popped popping pops
position positional positioned positioning positions reposition repositioned repositioning repositions
possible impossibility impossible impossibly possibilities possibility possibles possibly
post postage postages postal posted posting postings posts
pot potful potfuls pots potted potter potteries potters pottery potting
pound pounds
power powered powerful powerfully powering powerless powerlessly powerlessness powers
prepare prep preparation preparations preparatory prepared preparedness prepares preparing unprepared
present presentable presentably presentation presentational presentations presented presenter presenters presenting presents unpresentable
press pressed presses pressing unpressed
pretty prettier prettiest prettily prettiness
price priced priceless prices pricey pricing unpriced
prince princedom princedoms princelier princeliest princeliness princeling princelings princely princes princess princesses
prison imprison imprisoned imprisoning imprisonment imprisonments imprisons prisoned prisoner prisoners prisons
probably improbabilities improbability improbable improbably probabilistic probabilistically probabilities probability probable
problem problematic problematical problematically problems unproblematic
programme program programed programing programmable programmatic programmed programmer programmers programmes programming programs
promise promised promises promising unpromising
proper improper improperly properly
protect protected protecting protection protectionism protectionist protectionists protections protective protectively protectiveness protector protectors protectorship protectorships protects unprotected
public publically publicly publics
pull pulled pulling pulls
push pushed pusher pushers pushes pushing pushy
put puts putting
quarter quartered quartering quarterly quarters
queen queene queenly queens
question questionable questionably questioned questioner questioners questioning questioningly questions unquestionability unquestionable unquestionably unquestioned unquestioning unquestioningly
quick quicken quickened quickening quickens quicker quickest quickie quickies quickly quickness
quiet quieten quietened quietening quietens quieter quietest quietly quietness
quite
rabbit rabbits rabbitted rabbitter rabbitters rabbitting
race raced racer racers races racing
radio radioed radios
rain rained rainier rainiest raining rains rainy
raise raised raiser raisers raises raising
rate rateable rated rater raters rates rating ratings
rather
reach reached reaches reaching
read misread misreading misreads readability readable reader readers reading readings reads reread rereading rereadings rereads unread unreadable
ready readied readier readies readiest readily readiness readying unready
real realism realisms realist realistic realistically realists realities reality unreal unrealistic unrealistically unreality
realise realisable realisation realisations realised realises realising realizable realization realizations realize realized realizes realizing unrealised unrealized
really
reason reasonable reasonableness reasonably reasoned reasoning reasons unreasonable unreasonableness unreasonably unreasoning
recent recently
record prerecord prerecorded prerecording prerecords recorded recorder recorders recording recordings records unrecorded
red redden reddened reddening reddens redder reddest reddish reddy redness reds
relate interrelate interrelated interrelates interrelating interrelation interrelations interrelationship interrelationships related relatedness relates relating relation relational relations relationship relationships unrelated
remember remembered remembering remembers remembrance remembrances
rent rentable rental rentals rented renting rents unrentable
reply replied replies replying
report reported reportedly reporter reporters reporting reports unreported
responsible irresponsible irresponsibly responsibilities responsibility responsibly
rest rested restful restfully restfulness resting restless restlessly restlessness rests
return returnable returned returnee returnees returner returners returning returns unreturned
rich richer riches richest richly richness
rid ridding rids
ride ridden rideable rider riders ridership rides riding rode
right righthand righthanded righthander righthanders rightist rightists rightmost
rights righted rightful rightfully righting rightly rightness righto righty rt
ring rang ringed ringing rings rung
rise risen riser risers rises rising risings rose
river rivers
road rd roads
rock rocklike rocks rocky
roll rolled roller rollers rolling rolls unroll unrolled unrolling unrolls
room anteroom anterooms roomed roomful roomfuls roomier roomiest rooms roomy
rough roughage roughed roughen roughened roughening roughens rougher roughest roughing roughish roughly roughness roughs
round rounded rounder rounders roundest rounding roundly roundness rounds
rubbish rubbished rubbishes rubbishing
rule misrule misruled ruled ruler rulers rules ruling rulings unruled
run ran rans rerun rerunning reruns runner runners runnier runniest runnin running runny runs
sad sadden saddened saddening saddens sadder saddest sadly sadness sadnesses
safe safely safeness safer safes safest safety unsafe
sail sailed sailer sailers sailing sailings sailor sailors sails
same sameness
saturday saturdays
save saved saver savers saves saving savings unsaved
say said saying sayings says sez unsaid unsayable
scare scared scareder scaredest scares scarier scariest scaring scary
school preschool preschooled preschooler preschoolers preschooling preschools schooled schooling schools unschooled
science sciences scientific scientifically scientificity scientist scientists unscientific unscientifically
sea seas seaward seawards
seat seated seater seaters seating seats unseat unseated unseating unseats
second secondaries secondarily secondary seconder seconders secondly
secure insecure insecurities insecurity secured securely secures securing securities security unsecured
see saw seeing seen seer seers sees seest unseeing unseeingly unseen
seem seemed seeming seemingly seems
self selfhood selfish selfishly selfishness selfless selflessly selflessness selves unselfish unselfishly unselfishness
sell resell reseller resellers reselling resold seller sellers selling sells sold unsold
send sender senders sending sends sent unsent
sense senseless senselessness
serious seriously seriousness
serve servant servants served server serveries servers servery serves serving servings unserved
service serviceable serviced services servicing unserviced
set sets setting settings subset subsets unset
settle resettle resettled resettlement resettlements resettler resettlers resettles resettling settled settlement settlements settler settlers settles settling settlor settlors
seven sevens seventeen seventeenth seventeenths seventh sevenths seventies seventieth seventieths seventy
several severally
sex sexed sexes sexier sexiest sexily sexiness sexing sexism sexist sexists sexless sexual sexualisation sexualise sexualised sexualises sexualising sexuality sexualization sexualize sexualized sexualizes sexualizing sexually sexy
shake shakable shaken shaker shakers shakes shakily shakiness shaking shaky shook unshakable unshakeable
shall shalst shalt shan
shape misshape misshaped misshapen misshapes misshaping shaped shapeless shapelessly shapelessness shapelier shapeliest shapeliness shapely shaper shapers shapes shaping unshapely
share shared shares sharing unshared
she her hers herself
ship shipment shipments shipped shipper shippers shipping ships
shirt shirted shirts
shoe shoed shoeing shoeless shoes
shoot shooter shooters shooting shootings shoots shot shots
shop shopped shopper shoppers shopping shops
short shortage shortages shorten shortened shortening shortens shorter shortest shortish shortness
should shouldn
shoulder shouldered shouldering shoulders
shout shouted shouter shouters shouting shouts
show showed showing showings shown shows
shut shuts shutting
shy shyly shyness
sick sicken sickened sickening sickeningly sickens sicker sickest sickly sickness sicknesses
side sided sides sideways siding sidings
sight sighted sightedness sighter sighters sighting sightings sightless sightlessly sights unsighted unsightly
sign signed signer signers signing signings signs unsigned
silly sillier silliest sillily silliness
simple simpleness simpler simplest simplification simplifications simplified simplifies simplify simplifying simply unsimplified
since
sing sang singer singers singing sings sung unsung
single singled singleness singles singling singly
sir sirs
sister sisterhood sisterly sisters
sit resat resit resits resitting sat sits sitter sitters sittin sitting sittings
situation situate situated situating situational situationally situations
six sixes sixteen sixteenth sixteenths sixth sixthly sixths sixties sixtieth sixtieths sixty
size sizable sized sizes sizing
skin skinned skinning skins
sky skies skyward skywards
sleep sleeper sleepers sleepily sleepiness sleeping sleepless sleeplessness sleeps sleepy slept
slight slighter slightest slighting slightly
slip slippage slippages slipped slipping slippy slips
slow slowed slower slowest slowing slowly slowness slows
small smaller smallest smallish smallness smalls
smell smelled smelliness smelling smells smelly smelt
smile smiled smiles smiling smilingly unsmiling
smoke nonsmoking smoked smokeless smoker smokers smokes smokey smokier smokiest smokiness smoking smoky
snow snowed snowier snowiest snowiness snowing snows snowy
so
soft soften softened softener softeners softening softens softer softest softly softness
some somebody somehow someone somethin something sometime sometimes somewhere
son sonny sons
song songs
soon sooner soonest
sorry sorrier sorriest sorriness
sort sorts
sound sounded sounding soundings soundless soundlessly sounds
south southerlies southerly
space spaced spacer spacers spaces spacing spacious spaciously spaciousness unspaced
speak speaker speakers speaking speaks spoke spoken unspeakable unspeakably unspeaking unspoken
special specialisation specialisations specialise specialised specialises specialising specialism specialisms specialist specialists specialities speciality specialization specializations specialize specialized specializes specializing specially specials specialties specialty
spend misspent spender spenders spending spends spent unspent
sport sporting sports sporty
spot spotless spotlessly spotlessness spots spotted spotter spotters spottier spottiest spottily spottiness spotting spotty
spring sprang springing springs sprung
square sq squared squarely squareness squarer squares squarest squaring
stage staged stages staging
stand standin standing stands stood
star stardom starlet starlets starlike starred starring starry stars
stare stared stares staring
start restart restarted restarting restarts started starter starters starting starts
state stated statement statementing statements stating unstated
station stationed stationing stations substation substations
stay stayed stayer staying stays
steal stealer stealers stealing steals stole stolen
step stepped stepping steps stepwise
stick sticker stickers sticking sticks stuck unstuck
still stilled stiller stillest stilling stillness stills
stone stoned stones stoney stonier stonily stoniness stoning stony
stop nonstop stoppage stoppages stopped stopper stoppers stopping stops unstoppable
store storable storage stored stores storing
story stories
straight straighten straightened straightener straighteners straightening straightens straighter straightest straights unstraightened
strange strangely strangeness stranger strangers strangest
street st streets
strike striker strikers strikes striking strikingly struck
strong stronger strongest strongly
student students studentship studentships
study studied studies studious studiously studying
stuff
stupid stupider stupidest stupidity stupidly
subject subjects
such
sudden suddenly suddenness
suggest suggested suggestible suggesting suggestion suggestions suggestive suggestively suggestiveness suggests
suit suitability suitable suitably suited suiting suits unsuitability unsuitable unsuitably unsuited
summer midsummer summered summering summers summery
sun sunless sunlight sunned sunnier sunniest sunning sunny suns sunshine
sunday sundays
support supported supporter supporters supporting supportive supports unsupported
suppose supposed supposedly supposes supposing
sure surely sureness surer surest unsure
surprise surprised surprises surprising surprisingly unsurprised unsurprising unsurprisingly
sweet sweeten sweetened sweetener sweeteners sweetening sweetens sweeter sweetest sweetie sweeties sweetly sweetness sweets unsweetened
swim swam swimmer swimmers swimming swims swum
system subsystem subsystems systematic systematically systems unsystematic unsystematically
table tablecloth tablecloths tabled tables tabling
tail tailed tailing tailings tails
take retake retaken retakes retaking retook taken taker takers takes takin taking takings took
talk talked talker talkers talkin talking talks
tall taller tallest tallness
tape taped tapes taping
taste tasted tasteful tastefully tastefulness tasteless tastelessly tastelessness taster tasters tastes tastier tastiest tasting tasty
tax nontaxable pretax taxable taxation taxed taxes taxing taxpayer taxpayers untaxed
tea teas
teach taught teachable teacher teacherly teachers teaches teaching teachings
team teamed teaming teams
tear tearing tears tore torn
telephone phone phoned phones phoning tel telephoned telephones telephonic telephoning
television televise televised televises televising televisings televisions televize televized televizes televizing televizings tellies telly tv tvs
tell retell retelling retold telling tells told untold
ten tens tenth tenths
tend tended tendencies tendency tending tends
term midterm midterms preterm termed terming termism termly terms
terrible terribly
test retest retested retesting retests testable tested tester testers testing tests untestable untested
than
thank thanked thankful thankfully thankfulness thanking thankless thanks thankyou unthanked
that thats those
the
then
there
they em their theirs theirselves them themself themselves
thick thicken thickened thickener thickeners thickening thickens thicker thickest thickly thickness thicknesses
thing thingie thingies things thingy
think rethink rethinking rethinks rethought thinker thinkers thinkin thinking thinks thought thoughtful thoughtfully thoughtfulness thoughtless thoughtlessly thoughtlessness thoughts unthinkable unthinking unthinkingly unthought
thirst thirsted thirstier thirstiest thirstily thirstiness thirsting thirsts thirsty
thirteen thirteenth thirteenths
thirty thirties thirtieth thirtieths
this these
though tho
thousand thousands thousandth thousandths
three third thirdly thirds threes
throat throated throatily throats throaty
through thro throughout thru
throw threw thrower throwers throwing thrown throws
thursday thurs thursdays
tie tied ties tying untie untied unties untying
tight tighten tightened tightening tightens tighter tightest tightly tightness tights
till til
time anytime timed timeless timelessness timeliness timely timer timers times timing timings untimed untimeliness untimely
tire tired tireder tiredest tiredly tiredness tireless tirelessly tirelessness tires tiring untiring
to
today todays
together togetherness togethers
tomorrow tomorrows
tonight
too
tooth teeth teethed teethes teething teethings toothed toothless toothy
top topless topmost topped topper toppers topping toppings tops untopped
total totaled totaling totality totalizing totalled totalling totally totals untotalled
touch touchable touched touches touching touchingly untouchable untouchables untouched
toward towards
town towns township townships
track tracked tracker trackers tracking trackless tracks
train trained trainee trainees trainer trainers training trains untrained
travel traveled traveler travelers traveling travelled traveller travellers travelling travels
treat mistreat mistreated mistreating mistreatment mistreatments mistreats pretreated pretreatment treatable treated treating treatment treatments treats untreatable untreated
tree treeless trees
trip tripped tripping trips
trouble troubled troubles troublesome troubling troublingly untroubled
true truer truest truism truisms truly untrue
trust antitrust entrust entrusted entrusting entrusts trusted trustier trustiest trusting trusts trusty
truth truthful truthfully truthfulness truthiness truths untruth untruthful untruthfully untruthfulness untruths
try triable tried tries tryin trying untried
tuesday tue tues tuesdays
turn turned turning turnings turns unturned
twelve twelfth twelfths twelves
twenty twenties twentieth twentieths
two twice twos
type subtype subtypes types
ugly uglier ugliest ugliness
uncle uncles
under
underneath
understand misunderstand misunderstanding misunderstandings misunderstands misunderstood understandable understandably understanding understandingly understandings understands understood
unless
until
up upmost upped upping ups upside
upon
use misuse misused misuser misusers misuses misusing reusable reuse reused reuses reusing unusable unused usability usable useable used useful usefully usefulness useless uselessly uselessness user users uses using
usual unusual unusually usually
van vans
very
video videoed videoing videos
view viewable viewed viewer viewers viewing views
visit revisit revisitation revisitations revisited revisiting revisits unvisited visitation visitations visited visiting visitor visitors visits
voice voiced voiceless voices voicing
wait waited waitin waiting waits
wake wakeful wakefulness waken wakened wakening wakens wakes wakey waking woke woken
walk walkable walked walker walkers walkie walkies walking walks
wall walled walling walls
want unwanted wanna wanta wanted wanting wants
war interwar postwar prewar warred warring wars
warm warmed warmer warmers warmest warming warmly warms warmth
wash unwashable unwashed washable washed washer washers washes washing
waste wastage wastages wasted wasteful wastefully wastefulness waster wasters wastes wasting
watch watched watcher watchers watches watchful watchfully watchfulness watching
water watered waterier wateriest wateriness watering waters watery
wave waved waves waving
way midway ways
we our ours ourself ourselves us
wear unwearable unworn wearable wearer wearers wearing wears wore worn
weather weathered weathering weathers
web
wed unwed unwedded wedded wedding weddings weds
wednesday wednesdays
week midweek midweekly weeklies weekly weeks
weight unweighted weighted weighting weightings weightless weightlessly weightlessness weights
well unwell
west midwest westerlies westerly westward westwards wnw wsw
wet wetly wetness wets wettable wetted wetter wettest wetting
what whaddya whatcha whatever whats wot
wheel wheeled wheeler wheelers wheelie wheelies wheeling wheels
when whenever
where wherever
whether
which whichever
while whilst
white whiten whitened whitener whiteners whiteness whitening whitens whiter whites whitest whitish
who whoever whom whomever whose
whole wholeness wholes wholistic wholistically wholly
why whys
wide widely widen widened wideness widening widens wider widest width widths
wife wifely wives
wild wilder wildest wildly wildness wilds
will ll unwilling unwillingly unwillingness willed willing willingly willingness
win winner winners winning winnings wins won
wind winded windless winds windward windwards windy
window windowed windowless windows
wine wined wineries winery wines wining
winter midwinter wintered wintering winterise winterised winterising winterize winterized winterizing winters wintery wintry
wish wished wisher wishers wishes wishing
with wiv
within
without
woman womanhood womaniser womanisers womanising womanizer womanizers womanizing womanly women womens
wonder wondered wonderful wonderfully wondering wonderingly wonderment wonders wondrous wondrously
wood wooden woods woody
word worded wording wordings wordless wordlessly words wordy
work rework reworked reworking reworks unworkable unworked workable worked worker workers workin working workings works
world unworldliness unworldly worldliness worldly worlds
worry unworried worried worriedly worriedness worrier worriers worries worrying worryingly
worse worsen worsened worsening worsens worst
worth unworthy worthier worthies worthiest worthily worthiness worthless worthlessness worthy
would wouldn
write rewrit rewrite rewrites rewriting rewritten rewrote unwritten writer writers writes writing writings written wrote
wrong wronged wrongful wrongfully wrongfulness wronging wrongly wrongness wrongs
yard yards yd yds
year yearling yearlings yearly years yr yrs
yellow yeller yellowed yellower yellowest yellowing yellowish yellowness yellows yellowy
yes ya yah yea yeah yeh yep yeses yup
yesterday yesterdays
yet
you ye yer yerself your yours yourself yourselves yous youse
young younger youngest youngish youngster youngsters
zero zeroed zeroing zeros''')

bnccoca2unsplit = (''' accent accented accenting accents unaccented
access accessed accesses accessibility accessible accessing inaccessibility inaccessible
accident accidental accidentally accidently accidents
according accordingly
account accounted accounting accounts unaccounted
accuse accusation accusations accused accuser accusers accuses accusing accusingly
ace aced aces acing
active actively activism activist activists activities activity inactive inactivity
adapt adaptabilities adaptability adaptable adaptation adaptations adapted adapter adapters adapting adaption adaptive adaptor adaptors adapts maladaptive unadapted
admire admirable admirably admiration admired admirer admirers admires admiring admiringly
adult adulthood adults
advance advanced advancement advances advancing
advantage advantaged advantageous advantageously advantages advantaging
adventure adventured adventurer adventurers adventures adventuring adventurism adventurous misadventure misadventures
advice
advise advisability advisable advisably advised advisedly advisement adviser advisers advises advising advisor advisors advisory inadvisability inadvisable
affair affairs
affect affected affecting affects unaffected
agent agents
aid aided aider aiders aiding aids unaided
alarm alarmed alarming alarmingly alarmist alarmists alarms
alcohol alcoholic alcoholics alcoholism alcohols
alive
alter alterable alteration alterations altered altering alters unalterable unaltered
altogether
amuse amused amusement amusements amuses amusing amusingly unamused
angel angelic angelically angels
anger angered angering angers
announce announced announcement announcements announcer announcers announces announcing unannounced
annoy annoyance annoyances annoyed annoying annoyingly annoys
anxious anxiously
apartment apartments apts
appeal appealed appealing appealingly appeals unappealing
apple apples
apply application applications applied applies applying apps disapplication reapplication reapplications reapplied reapplies reapply
appoint appointed appointee appointees appointing appointment appointments appoints reappoint reappointed reappointing reappointment reappointments reappoints
appreciate appreciated appreciates appreciating appreciation appreciative appreciatively unappreciated unappreciative
approach approachable approached approaches approaching unapproachable
april apr
argue arguable arguably argued argues arguing argument argumentation argumentative argumentatively argumentativeness arguments unarguable unarguably
army armies
arrest arrestable arrested arresting arrests
article articles
aside asides
asleep
assist assistance assistant assistants assisted assisting assists unassisted
associate associated associates associateship associateships associating association associations associative associatively
assume assumed assumes assuming unassuming unassumingly
assure assurance assurances assured assuredly assurer assurers assures assuring reassurance reassurances reassure reassured reassures reassuring reassuringly
atmosphere atmospheres atmospheric
attach attached attaches attaching attachment attachments unattached
attack attacked attacker attackers attacking attacks
attempt attempted attempting attempts unattempted
attend attendance attendances attendant attendants attended attendee attendees attender attenders attending attends unattended
attention attentional attentions inattention
attitude attitudes attitudinal
attract attracted attracting attraction attractions attractive attractively attractiveness attractor attractors attracts unattractive unattractively
august aug
automatic automatically
available availability unavailability unavailable
average averaged averagely averages averaging
avoid avoidable avoidance avoided avoiding avoids unavoidable unavoidably
awake awaken awakened awakening awakenings awakens awakes awoke awoken reawaken reawakened reawakening reawakens
awkward awkwardly awkwardness awkwardnesses
background backgrounded backgrounding backgrounds
bacon bacons
bake baked baker bakeries bakers bakery bakes baking
balance balanced balances balancing imbalance imbalanced imbalances unbalance unbalanced unbalances unbalancing
banana bananas
band banded banding bands
bang banged banging bangings bangs
bare bared barely bareness barer bares barest baring
bark barked barking barks
basis
basket basketful basketry baskets basketsful
bat bats batted batter batters batting
battery batteries
battle battled battler battlers battles battling
bay bays
bean beans
bee bees
beef beefy
beer beers
beg beggar beggars begged begging begs
bell belled belling bells
belong belonged belonging belongings belongs
belt belted belting belts unbelted
bend bendable bended bending bends bendy bent unbend unbending unbends unbent
benefit benefited benefiting benefits benefitted benefitting
bike biked biker bikers bikes biking
bin binned binning bins
bind binder binderies binders bindery binding bindings binds bound unbind unbinding unbound
biscuit biscuits
bite biter biters bites biting bitten
bitter bitterer bitterest bitterly bitterness
blame blamed blameless blamelessly blames blaming
blank blanked blanking blankly blankness blanks
blanket blanketed blanketing blankets
bleed bled bleedin bleeding bleeds
bless blessed blesses blessing blessings blest unblessed
blind blinded blinding blindingly blindly blindness blinds
block blockage blockages blocked blocker blockers blocking blocks blocky unblock unblocked unblocking
blonde blond blonder blondes blondest blondness blondy
bloom bloomed bloomer bloomers bloomin blooming blooms
boil boiled boiler boilers boiling boils
bomb bombed bomber bombers bombing bombings bombs
bond bonded bonding bonds
boom boomed booming booms
boot booted booting boots
borrow borrowed borrower borrowers borrowing borrowings borrows unborrowed
boss bossed bosses bossing bossy
bounce bounced bouncer bouncers bounces bouncier bounciest bouncily bounciness bouncing bouncy
bow bowed bowing bows unbowed
bowl bowled bowler bowlers bowling bowls
brain brained brainier brainiest braininess brainless brains brainy
brake braked brakes braking
branch branched branches branching
brand branded branding brands
brave braved bravely braveness braver bravery braves bravest braving
breast breasted breasting breasts
breathe breathable breathed breathes breathing unbreathable unbreathing
breed bred breeder breeders breeding breeds interbred interbreed interbreeding interbreeds
brick bricked brickie brickies bricks bricky
bridge bridged bridges bridging unbridgeable
brief briefer briefest briefly briefs
brilliant brilliantly
broad broaden broadened broadening broadens broader broadest broadly
brush brushed brushes brushing unbrushed
buck bucked bucking bucks
bucket bucketful buckets bucketsful
bug bugged bugging bugs
bump bumped bumper bumpers bumping bumps
bunch bunched bunches bunching
burst bursting bursts
bury burial burials buried buries burying unburied
butter buttered buttering butters buttery unbuttered
button buttoned buttoning buttons unbutton unbuttoned unbuttoning unbuttons
cable cabled cabler cablers cables cabling cablings
cage caged cages caging
calculate calculated calculates calculating calculation calculations calculator calculators miscalculate miscalculated miscalculates miscalculating miscalculation miscalculations recalculate recalculated recalculates recalculating recalculation recalculations
calm calmed calmer calmest calming calmly calmness calms
camera cameras
canoe canoed canoeing canoeist canoeists canoes
cans canned canning
cap capped capping cappings caps uncapped
capable capabilities capability capably incapability incapable
cape caped capes
capital capitals
captain capt captaincies captaincy captained captaining captains capts
career careerist careers
carpet carpeted carpeting carpets
carrot carrots carroty
cart carted carter carters carting carts
cash cashed cashes cashing cashless
cast casting castings casts
castle castles
casual casually casualness casuals
ceiling ceilinged ceilings
cent cents
centimetre centimeter centimeters centimetres cm cms
century centuries
chain chained chaining chains unchained
challenge challenged challenger challengers challenges challenging challengingly unchallengeable unchallenged
champion champ championed championing champions championship championships champs
channel channelled channelling channels unchannelled
chapter ch chapt chapters
character characterful characterisation characterisations characterise characterised characterises characterising characterization characterize characterized characterizes characterizing characterless characters
charm charmed charmer charmers charming charmingly charmless charms
chase chased chaser chasers chases chasing
chat chats chatted chatting chatty
cheat cheated cheater cheaters cheating cheats
cheek cheeks
cheer cheered cheerful cheerfully cheerfulness cheerier cheeriest cheerily cheeriness cheering cheerless cheerlessly cheerlessness cheers cheery
cheese cheesed cheeses
chest chested chests
chew chewed chewer chewers chewier chewiest chewing chews chewy
chief chiefly chiefs
chocolate choc chocolates chocolatey chocs
chop chopped chopper choppers chopping chops
cigarette cig cigarettes ciggies ciggy cigs
circle circled circles circling circular circularity circulars encircle encircled encirclement encirclements encircles encircling semicircle semicircles semicircular
circumstance circumstances circumstantial circumstantially
citizen citizenry citizens citizenship citizenships
claim claimant claimants claimed claiming claims unclaimed
classic classical classically classicism classicist classicists classico classics neoclassical neoclassically neoclassicism neoclassicist neoclassicists
clever cleverer cleverest cleverly cleverness
cliff cliffs
clip clipped clipper clippers clipping clippings clips unclipped
cloth cloths
cloud clouded clouding cloudless clouds cloudy unclouded
clue clueless clues
coach coached coaches coaching
coal coals
coast coastal coasts
combine combinability combination combinations combined combines combining recombinant recombination recombinations recombine recombined recombines recombining
command commanded commander commanders commanding commandment commandments commands
comment commentaries commentary commented commenting comments
commerce commercial commercialisation commercialise commercialised commercialises commercialising commercialism commercialization commercialize commercialized commercializes commercializing commercially commercials uncommercial
commit commitment commitments commits committal committals committed committing uncommitted
committee committees subcommittee subcommittees
common commoner commoners commonest commonly commonness uncommon uncommonly
community communities
compare comparability comparable comparably compared compares comparing comparison comparisons incomparable incomparably
competition competitions
complain complained complaining complains uncomplaining
complicate complicated complicates complicating complication complications uncomplicated
concentrate concentrated concentrates concentrating concentration concentrations
condition conditional conditionally conditionals conditioned conditioner conditioners conditioning conditionings conditions unconditional unconditionally unconditioned
confuse confused confusedly confuses confusing confusingly confusion confusions
connect connected connectedness connecting connection connections connective connectives connectivity connector connectors connects connexion connexions interconnect interconnected interconnecting interconnection interconnections interconnects reconnect reconnected reconnecting reconnection reconnections reconnects unconnected
conscious consciously consciousness unconscious unconsciously unconsciousness
constant constantly constants inconstantly
contact contactable contacted contacting contacts uncontactable
contain contained container containers containing containment contains
contract contracted contracting contractor contractors contracts
contribute contributed contributes contributing contribution contributions contributor contributors contributory noncontributory
convince convinced convinces convincing convincingly unconvinced unconvincing unconvincingly
cop cops
cope coped copes coping
copy copied copier copiers copies copying copyist copyists
correct corrected correcting correction correctional corrections corrective correctly correctness corrects incorrect incorrectly uncorrected
cottage cottager cottagers cottages
cotton cottons
cough coughed coughing coughs
council cllr cllrs coun councillor councillors councilor councils
counter countered countering counters
county counties
cousin cousins cuz cuzzies
cow cows
crack cracked cracking cracks
crash crashed crashes crashing
crawl crawled crawler crawlers crawlies crawling crawls crawly
cream creamed creamery creamier creamiest creamily creaminess creaming creams creamy
create created creates creating creation creations creative creatively creativity creator creators recreate recreated recreates recreating
creature creatures
credit creditable creditably credited crediting creditor creditors credits
creep creeper creepers creeping creeps creepy crept
criminal crim criminality criminally criminals crims
crisp crisped crispier crispiest crispiness crisping crisply crispness crisps crispy
crowd crowded crowding crowds uncrowded
crown crowned crowning crowns uncrowned
cruel crueller cruellest cruelly cruelness cruelties cruelty
culture cultural culturally cultured cultures intercultural subcultural subculture subcultures uncultured
cure curable curative cured cures curing incurable incurably
curious curiosities curiosity curiously
curl curled curler curlers curlier curliest curliness curling curls curly uncurl uncurled uncurling uncurls
current currently currents
customer customers
damage damaged damager damagers damages damaging undamaged
dare dared dares daring daringly
dawn dawned dawning dawns
debt debtor debtors debts
december dec
decent decently indecent indecently
decision decisions
deck decking decks
decorate decorated decorates decorating decoration decorations decorative decoratively decorator decorators redecorate redecorated redecorates redecorating redecoration redecorations undecorated
defence defenceless defencelessly defences defense defenses defensible defensibly defensive defensively defensiveness indefensible indefensibly
delight delighted delightedly delightful delightfully delighting delights
deliver delivered deliveries delivering delivers delivery undelivered
demand demanded demanding demands undemanding
deny deniable denial denials denied denies denying undeniable undeniably
department departmental departmentally departments dept depts interdepartmental
depress antidepressant antidepressants depressant depressants depressed depresses depressing depressingly depression depressions depressive depressives
describe described describer describers describes describing indescribable indescribably
desert deserted deserter deserters deserting desertion desertions deserts
deserve deserved deservedly deserves deserving undeserved undeserving
design designed designer designers designing designs
desire desirability desirable desired desires desiring desirous undesirability undesirable undesirables undesired
desk desks
desperate desperately desperation
destroy destroyed destroyer destroyers destroying destroys
detail detailed detailing details
detect det detectable detected detecting detection detective detectives detector detectors detects undetectable undetected
determine determinable determinant determinants determination determinations determinative determined determinedly determines determining determinism determinist deterministic deterministically determinists indeterminacies indeterminacy undetermined
develop developed developer developers developing development developmental developmentally developments develops redevelop redeveloped redeveloping redevelopment redevelopments redevelops underdeveloped underdevelopment undeveloped
diet dietary dieted dieter dieters dietician dieticians dieting dietitian dietitians diets
dine dined diner diners dines dining
direct directly
directed directing directive directives director directorial directories directors directorship directorships directory directs misdirect misdirected misdirecting misdirection misdirections misdirects redirect redirected redirecting redirects undirected
direction bidirectional directional directions indirection unidirectional
disappear disappearance disappearances disappeared disappearing disappears
disappoint disappointed disappointing disappointingly disappointment disappointments disappoints
discipline disciplinarian disciplinary disciplined disciplines disciplining indiscipline interdisciplinary undisciplined
discuss discussed discusses discussing discussion discussions undiscussed
disease diseased diseases
disgust disgusted disgustedly disgusting disgustingly disgusts
dish dished dishes dishing
distance distanced distances distancing
district districts
disturb disturbance disturbances disturbed disturbing disturbingly disturbs undisturbed
dive diveable dived diver divers dives diving
divide divided divider dividers divides dividing undivided
divorce divorced divorcee divorcees divorces divorcing
doll dollies dolls dolly
dollar dollars
dozen dozens
drag dragged dragging drags
dragon dragons
drama dramas dramatic dramatically dramatics dramatisation dramatisations dramatise dramatised dramatises dramatising dramatist dramatists dramatization dramatizations dramatize dramatized dramatizes dramatizing undramatic
drawer drawers
drum drummed drummer drummers drumming drums
duck ducked ducking duckling ducklings ducks
due dues duly undue unduly
dump dumped dumper dumpers dumping dumps
dust dusted duster dusters dustier dustiest dustiness dusting dustless dusts dusty
duty dutiable duties dutiful dutifully dutifulness
earn earned earner earners earning earnings earns unearned
ease eased eases easing unease uneasily uneasiness uneasy
economy economic economical economically economics economies economise economised economises economising economist economists economize economized economizes economizing uneconomic uneconomical uneconomically
edit ed editable edited editing editor editorial editorialise editorialised editorialist editorialists editorialize editorialized editorializing editorials editors editorship editorships editress edits eds unedited
effect effected effecting effects
effort effortless effortlessly efforts
elder elderly elders
elect elected electing election electioneering elections elector electoral electorally electors elects reelect reelected reelecting reelection reelects unelected
electric electrical electrically electrician electricians electricity electrics
elephant elephants
email emailed emailing emailled emailling emails
embarrass embarrassed embarrasses embarrassing embarrassingly embarrassment embarrassments
emotion emotional emotionally emotionless emotionlessly emotions unemotional unemotionally
empire empires
encourage encouraged encouragement encouragements encourages encouraging encouragingly
enemy enemies
energy energetic energetically energetics energies energise energised energiser energisers energises energising energize energized energizer energizers energizes energizing
engage engaged engagement engagements engages engaging engagingly
engineer engineered engineering engineers
enormous enormously
entertain entertained entertainer entertainers entertaining entertainingly entertainment entertainments entertains unentertaining
entire entirely entirity
envelope envelop enveloped envelopes enveloping envelopment envelopments envelops
environment environmental environmentalism environmentalist environmentalists environmentally environments
equal equaled equaling equalisation equalise equalised equaliser equalisers equalises equalising equality equalization equalize equalized equalizer equalizers equalizes equalizing equalled equalling equally equals inequalities inequality unequal unequalled unequally
equipment equip equipments equipped equipping equips unequipped
escape esc escaped escapee escapees escaper escapers escapes escaping escapism escapist
establish established establishes establishing establishment establishments reestablish reestablished reestablishes reestablishing reestablishment
estate estates
event eventful events uneventful uneventfully
eventually eventual eventualities eventuality
evidence evidenced evidences evidential
evil eviler evilest evilly evilness evils
exam exams
examine examination examinations examined examinee examinees examiner examiners examines examining unexamined
example examples
excellent excellence excellently
exchange exchangeable exchanged exchanger exchangers exchanges exchanging
exercise exercisable exercised exercises exercising
exhaust exhausted exhaustible exhausting exhaustion exhaustions exhaustive exhaustively exhaustiveness exhausts inexhaustible
exist existed existence existences existent existing exists nonexistent
expense expenses
expose exposed exposes exposing exposure exposures unexposed
extend extendable extended extender extenders extending extends unextended
extreme extremely extremes extremism extremist extremists extremities extremity
fail failed failing failings fails unfailing unfailingly
faint fainted fainter faintest fainting faintings faintly faintness faints
fairy faerie faeries fairies
faith faithful faithfully faithfulness faithfuls faithless faithlessly faiths unfaithful unfaithfully unfaithfulness
familiar familiarisation familiarise familiarised familiarises familiarising familiarity familiarization familiarize familiarized familiarizes familiarizing familiarly unfamiliar unfamiliarity
famous famously
fan fanned fanning fans
fancy fancied fancier fancies fanciest fanciful fancifully fancifulness fancily fanciness fancying
fantastic fantastical fantastically
fascinate fascinated fascinates fascinating fascination fascinations
fashion fashionable fashionably fashioned fashioning fashions unfashionable unfashionably
fault faulted faulting faultless faultlessly faults faulty unfaulted
favour favor favorable favorably favored favoring favors favourable favourably favoured favouring favours unfavored unfavourable unfavourably unfavoured
feather feathered feathering featherless feathers feathery
feature featured featureless features featuring
february feb
female femaleness females
fence fenced fences fencing unfenced
fetch fetched fetches fetching
file filed files filing filings unfiled
finance financed finances financial financially financials financier financiers financing underfinanced unfinanced
firm firmed firmer firmest firming firmly firmness
flag flags
flame flamed flames flaming
flash flashed flasher flashers flashes flashing
flight flightless flights flighty flt
flip flipped flipping flips
float floatation floatations floated floater floaters floating floats floaty
flood flooded flooding floods
flow flowed flowing flows
fold folded folding folds unfold unfolded unfolding unfolds
folk folks
fool fooled fooling foolish foolishly foolishness fools
foreign foreigner foreigners foreignness
forgive forgave forgivable forgiven forgiveness forgives forgiving unforgivable unforgivably unforgiven unforgiving
forth
fortnight fortnightly fortnights
fortune fortunes
fox foxed foxes foxier foxiest foxily foxiness foxy
frame framed framer framers frames framing framings unframed
frankly franker frankest frankness
frog froggies froggy froglike frogs
frost frosted frostier frostiest frostily frostiness frosting frosts frosty
fruit fruited fruiter fruiters fruitily fruiting fruitless fruitlessly fruitlessness fruits fruity
frustrate frustrated frustrates frustrating frustratingly frustration frustrations
fry fried fries fryer fryers frying
fund funded funder funders funding funds unfunded
fur furred furrier furriest furriness furry furs
furniture
future futures futurism futurist futuristic futuristically futurists
gain gained gainer gainers gainful gainfully gaining gains
garage garaged garages garaging
gate gateless gates
gather gathered gatherer gatherers gathering gatherings gathers
gay gaily gayer gayest gayness gays
gear geared gearing gearings gearless gears
generation generational generations intergenerational
gentleman gent gentlemanly gentlemen gents ungentlemanly
ghost ghosted ghosting ghostlike ghostly ghosts
giant giantess giantesses giantism giants
gift gifted giftedness gifting giftings gifts
glory gloried glories glorification glorifications glorified glorifies glorify glorifying glorious gloriously glorying inglorious
goal goalless goals
golf golfer golfers golfing
gorgeous gorgeously gorgeousness
grab grabbed grabber grabbers grabbing grabby grabs
grace graced graceful gracefully graceless graces gracing
grade gradable graded grader graders grades grading gradings regrade regraded regrades regrading ungraded
grand grander grandest grandly grandness grands
grant granted granting grantor grantors grants
grin grinned grinning grins
grocer groceries grocers grocery
guarantee guaranteed guaranteeing guarantees
guard guarded guardedly guarding guards unguarded
guest guests
guide guidance guided guider guiders guides guiding unguided
guilty guilt guiltily guiltless
habit habits
handy handier handiest handily handiness
harm harmed harmful harmfully harmfulness harming harmless harmlessly harms unharmed
heap heaped heaping heaps
heaven heavenly heavens heavenwards
hedge hedged hedges hedging
height heights
hero heroes heroic heroically heroics heroism
hesitate hesitated hesitates hesitating hesitatingly hesitation hesitations unhesitating unhesitatingly
hire hired hirer hirers hires hiring
hobby hobbies hobbyist hobbyists
honey honeyed honeys
hook hooked hooking hooks unhook unhooked unhooking unhooks
hotel hotels
identify identifiable identification identifications identified identifier identifiers identifies identifying identities identity unidentifiable unidentified
idiot idiotic idiotically idiots
ignore ignored ignores ignoring
ill illness illnesses ills
illustrate illustrated illustrates illustrating illustration illustrations illustrative illustrator illustrators unillustrated
image imaged imager imagers imagery images imaging
immediate immediacy immediately immediateness
impress impressed impresses impressing impressive impressively unimpressed unimpressive
improve improved improvement improvements improver improvers improves improving unimproved
inch inched inches inching
include incl included includes including
income incomes
increase increased increases increasing increasingly
incredible incredibly
indicate indicated indicates indicating indication indications indicative indicator indicators
individual individualise individualised individualism individualist individualistic individualists individuality individualize individualized individually individuals
industry industrial industrialisation industrialise industrialised industrialises industrialising industrialism industrialist industrialists industrialization industrialize industrialized industrializes industrializing industrially industries
influence influenced influences influencing influential uninfluenced
injure injured injures injuries injuring injurious injury uninjured
innocent innocently innocents
insist insisted insistence insistences insistent insistently insisting insists
inspect insp inspected inspecting inspection inspections inspector inspectors inspects
instance instanced instances
instant instantaneous instantaneously instantly instants
instruct instructed instructing instruction instructional instructionally instructions instructive instructively instructor instructors instructs
instrument instrumental instrumentalist instrumentalists instrumentation instruments
intend intended intending intends unintended
intense intensely intenseness intensification intensified intensifies intensify intensifying intensities intensity intensive intensively
intent intention intentional intentionality intentionally intentioned intentions intently intentness intents unintentional unintentionally
interrupt interrupted interrupting interruption interruptions interrupts uninterrupted uninterruptedly
interview interviewed interviewee interviewees interviewer interviewers interviewing interviews
introduce intro introduced introduces introducing introduction introductions introductory intros reintroduce reintroduced reintroduces reintroducing reintroduction reintroductions
investigate investigated investigates investigating investigation investigations investigative investigator investigators investigatory
invite invitation invitations invited invites inviting invitingly uninvited uninviting
iron
item itemisation itemise itemised itemises itemising itemization itemize itemized itemizes itemizing items
jacket jacketed jackets
jam jammed jamming jams
january jan
jaw jawed jawing jaws
jeans
journey journeyed journeying journeys
joy joyful joyfully joyfulness joyless joylessly joyous joyously joyousness joys
juice juices juicier juiciest juicily juiciness juicy
july jul
june jun
junior jnr jr juniors
justice injustice injustices justices justiciable
keen keener keenest keenly keenness
kilometre kilometer kilometers kilometres km kms
kindly kinder kindest kindliness kindlinesses kindness kindnesses unkind unkindest unkindly unkindness
knee kneed kneeing knees
knife knifed knifes knifing knives
knit knits knitted knitter knitters knitting
knowledge knowledgable knowledgeable knowledgeably knowledges
laboratory lab laboratories labs
labour labor labored laborer laborers laboring labors laboured labourer labourers labouring labourism labours
lack lacked lacking lacks
lamb lambed lambing lambs
lamp lamps
lane lanes
language languages
lasted everlasting lasting lasts longlasting
lawn lawns
lawyer lawyers
league leaguer leaguers leagues
lean leaned leaning leanings leans leant
leap leaped leaper leapers leaping leaps leapt
legal illegal illegality illegally legalese legalisation legalise legalised legalising legalism legalisms legalist legalists legality legalization legalize legalized legalizing legally
lend lender lenders lending lends lent
length lengthen lengthened lengthening lengthens lengthier lengthiest lengthily lengthiness lengths lengthways lengthwise lengthy
lesson lessons
library librarian librarians librarianship libraries
licence licenced licences licencing license licensed licensee licensees licenses licensing unlicenced unlicensed
lid lidded lids
lightly lighten lightened lightening lightens lighter lightest lightness lightweight
likely likelier likeliest likelihood unlikeliest unlikely
limit limitation limitations limited limiting limitless limitlessly limits ltd unlimited
lion lioness lionesses lions
loan loaned loaning loans
locate located locater locaters locates locating location locational locations locator locators relocate relocated relocates relocating relocation relocations
log logged logger loggers logging loggings logs
lone lonelier loneliest loneliness lonely loner loners lonesome
loose loosed loosely loosen loosened loosener looseness loosening loosenings loosens looser loosest loosing
loss losses
lower lowered lowering lowers lowest
lump lumped lumpily lumpiness lumping lumps lumpy
magazine mag magazines mags
magic magical magically magician magicians
mail mailed mailing mailings mails
maintain maintainability maintainable maintained maintaining maintains maintenance unmaintained
male maleness males
mama maman mamas mamma mammas momma mommas
manner mannered manners
map mappable mapped mapper mappers mapping mappings maps unmapped
march
marvel marveled marveling marvelled marvelling marvellous marvellously marvelous marvelously marvels
mask masked masking masks unmask unmasked unmasking unmasks
mass massed masses massing
massive massively
match matched matches matching matchless mismatch mismatched mismatches mismatching rematch unmatched
mate mated mates mateship matey mating matings
material materialism materialisms materialist materialistic materialistically materialists materiality materially materials
mathematics math mathematical mathematically mathematician mathematicians maths
maximum max maximums
measure immeasurable immeasurably measurable measurably measured measurement measurements measures measuring unmeasured
meat meats meaty
medical medicalization medically medicals
medicine medicinal medicinally medicines
melt meltdown melted melting melts
memory memorial memorials memories memorisation memorisations memorise memorised memorises memorising memorization memorizations memorize memorized memorizes memorizing
mental mentalist mentality mentally
merry merrier merriest merrily merriment merriness
message messages messaging
metal metalled metallic metals nonmetallic
metre meter metered metering meters metres metric metrical metrically metricize metricized metricizes metricizing metrics
microwave microwavable microwaveable microwaved microwaves microwaving
military militarily militarism militarist militaristic militarists
mill millage milled miller millers milling millings mills
minister ministered ministerial ministering ministers
minor minorities minority minors
minus minuses
mirror mirrored mirroring mirrors
mission missionaries missionary missioner missioners missions
mix mixed mixer mixers mixes mixing unmixed
model modeled modeler modelers modeling modelled modeller modellers modelling models
modern moderner modernisation modernise modernised modernising modernism modernisms modernist modernists modernity modernization modernize modernized modernizer modernizers modernizing moderns postmodern postmodernism postmodernist postmodernists
monkey monkeys
mood moodily moodiness moods moody
moon moonless moons
motor motored motoring motorisation motorise motorised motorises motorising motorist motorists motorization motorize motorized motorizes motorizing motors
mount mounted mounting mountings mounts mt
mouse mice mousey mousy
mow mowed mower mowers mowing mown mows
mud muddied muddiness muddy muds
murder murdered murderer murderers murderess murdering murderous murderously murders
muscle muscled muscles muscling
mystery mysteries mysterious mysteriously
nail nailed nailing nails
nanny nan nana nanas nanna nannas nannie nannies nans
narrow narrowed narrower narrowest narrowing narrowly narrowness narrows
nasty nastier nasties nastiest nastily nastiness
native nativelike natives unnativelike
navy naval navies
neither
nerve nerveless nerves nervily
nervous nervously nervousness
nest nested nesting nests
newspaper newspapers
non
nor
northern northerner northerners
november nov
nowhere
nut nuts
oak oaken oaks
object objects
observe nonobservant observable observant observantly observation observational observations observatories observatory observed observer observers observes observing unobservable unobservant unobserved
occasion occasional occasionally occasioned occasioning occasions
occur occurred occurrence occurrences occurring occurs reoccur reoccurred reoccurring reoccurs
october oct
official officialdom officially officials unofficial unofficially
onion onions
operate op operated operates operating operation operational operationally operations operative operatively operatives operator operators ops
opinion opinionated opinions
opportunity opportunities
oppose opposed opposes opposing opposition oppositional oppositions unopposed
opposite opposites
option optional optionally options
ordinary ordinarily ordinariness
organize organisation organisational organisationally organisations organise organised organiser organisers organises organising organization organizational organizationally organizations organized organizer organizers organizes organizing reorganisation reorganisations reorganise reorganised reorganises reorganising reorganization reorganizations reorganize reorganized reorganizes reorganizing unorganised unorganized
original originality originally originals unoriginal
otherwise
oven ovens
owe owed owes owing
pan pans
panic panick panicked panickier panickiest panicking panicky panics
partner pardner pardners partnered partnering partners partnership partnerships
pat pats patted patting
patch patched patches patching
path paths
patient patiently
pattern patterned patterning patterns
pause pausal paused pauses pausing
peace peaceable peaceably peaceful peacefully peacefulness
pen penned penning pens
pension pensionable pensioned pensioner pensioners pensioning pensions
per
percent percentage percentages
perform performance performances performed performer performers performing performs
period periodic periodical periodically periodicals periodicity periods
pet pets
physical physicality physically
piano pianist pianists pianos
pie pies
pig pigged piggies pigging piggish piggy piglet piglets piglike pigs
pile piled piles piling pilings
pin pinned pinning pins unpinned
pine pines piney
pink pinker pinkest pinkie pinkies pinkish pinkly pinkness pinks pinky
pipe piped pipes piping pipings
pitch pitched pitcher pitchers pitches pitching
pity piteous pitiable pitiably pitied pities pitiful pitifully pitiless pitilessly pitying unpitied
plain plainer plainest plainly plainness
plane planes aeroplane aeroplanes
planet interplanetary planetary planets
plastic plasticity plastics
plate plated plateful platefuls plates plating
pleasant pleasanter pleasantly pleasantness pleasantries pleasantry unpleasant unpleasantly unpleasantness unpleasantnesses
pleasure displeasure pleasurable pleasurably pleasures
plug plugged plugging plugs unplug unplugged unplugging unplugs
pocket pocketed pocketful pocketfuls pocketing pockets pocketsful
poem poems
poet poetess poetesses poetic poetical poetically poetry poets
poison poisoned poisoner poisoners poisoning poisonous poisons
pole poles
policy policies
polish polished polisher polishers polishes polishing unpolished
polite impolite impolitely impoliteness politely politeness politenesses politer politest
politics nonpolitical politic political politically politician politicians politicisation politicise politicised politicises politicising politicization politicize politicized politicizes politicizing politicking unpolitical
pollute antipollution pollutant pollutants polluted polluter polluters pollutes polluting pollution pollutions unpolluted
pool pooled pooling pools
popular popularisation popularisations popularise popularised populariser popularisers popularising popularity popularization popularizations popularize popularized popularizer popularizers popularizing popularly unpopular unpopularity
population populate populated populates populating populations unpopulated
port ported ports
positive positively positives positivism positivist positivistic positivists positivity
possess possessed possesses possessing possession possessions possessive possessively possessiveness possessor possessors possessory repossess repossessed repossesses repossessing repossession repossessions
potato potatoes
pour poured pouring pours
practical impractical impracticalities impracticality practicalities practicality practically
practise practice practiced practices practicing practised practises practising
pray prayed prayer prayers praying prays
prefer preferable preferably preference preferences preferential preferentially preferment preferments preferred preferring prefers unpreferred
pregnant pregnancies pregnancy
president presidential presidentially presidents
pressure pressured pressures pressuring pressurisation pressurise pressurised pressurising pressurization pressurize pressurized pressurizing
presume presumably presumed presumes presuming presumption presumptions
pretend pretended pretender pretenders pretending pretends
prevent preventable preventative prevented preventer preventing prevention preventive preventively prevents unpreventable
previous previously
pride prided prides priding
prime primed primes priming
print misprint misprints printable printed printer printers printing prints reprint reprinted reprinting reprints
privacy
private privately
process processed processer processers processes processing processor processors reprocess reprocessed reprocesses reprocessing reprocessings unprocessed
produce produced producer producers produces producing
product counterproductive production productions productive productively productivity products unproductive
profession pro professional professionalism professionality professionally professionals professions pros semipro semipros unprofessional
progress progressed progresses progressing progression progressions progressive progressively progressives
project projected projecting projection projectionist projectionists projections projective projects
pronounce mispronounce mispronounced mispronounces mispronouncing mispronunciation mispronunciations pronounceable pronounced pronounces pronouncing pronunciation pronunciations unpronounceable
property propertied properties
propose proposal proposals proposed proposer proposers proposes proposing
protest protestation protestations protested protester protesters protesting protestor protestors protests
proud prouder proudest proudly proudness
prove proved proven proves proving unproved unproven
provide provided provider providers provides providing
pub pubs
pudding pud puddings puds
pump pumped pumper pumpers pumping pumps
punch punched puncher punchers punches punching
punish nonpunishable punishable punished punisher punishers punishes punishing punishment punishments unpunished
pup puppies puppy pups
purchase purchasable purchased purchaser purchasers purchases purchasing repurchase repurchased repurchaser repurchasers repurchases repurchasing
pure impure impurities impurity pured purely pureness purer purest purism purist purists purity
purple purples purplish
purpose purposeful purposefully purposefulness purposeless purposelessness purposely purposes purposive
qualify qualification qualifications qualified qualifier qualifiers qualifies qualifying unqualified
quality qualities
quit quits quitted quitter quitters quitting
quote misquote misquoted misquotes misquoting quotation quotations quoted quotes quoting unquote unquoted
range midrange ranged ranges ranging
rapid rapidity rapidly rapids
rare rarely rareness rarer rarest rarified rarifies rarify rarifying rarities rarity
rat ratlike rats ratty
ray rayed rays
react overreact overreacted overreacting overreaction overreactions overreacts reactance reactant reactants reacted reacting reaction reactionaries reactionary reactions reactive reactivity reactor reactors reacts unreactive
recall recalled recalling recalls
receive receivable received receives receiving
recipe recipes
reckon reckoned reckoning reckonings reckons
recognize recognisable recognisably recognise recognised recognises recognising recognizable recognizably recognized recognizes recognizing unrecognisable unrecognised unrecognizable unrecognized
recommend recommendation recommendations recommended recommending recommends
recover irrecoverable recoverable recovered recoveries recovering recovers recovery
reduce reduced reduces reducible reducing reduction reductionism reductionist reductionists reductions
refer ref reference referenced references referencing referent referential referents referral referrals referred referring refers refs
refrigerator fridge fridges refrigerate refrigerated refrigerates refrigerating refrigeration refrigerations refrigerators
refuse refusal refusals refused refuser refusers refuses refusing
regard disregard disregarded disregarding disregards regarded regarding regardless regards
region regional regionalism regionalist regionalists regionally regions
register preregistration registered registering registers registrable registration registrations unregistered
regular irregular irregularities irregularity irregularly irregulars regularisation regularisations regularise regularised regularises regularising regularities regularity regularization regularizations regularize regularized regularizes regularizing regularly regulars
relax relaxation relaxations relaxed relaxer relaxers relaxes relaxing
release releasable released releaser releasers releases releasing unreleased
relief reliefs
rely reliabilities reliability reliable reliably reliance reliant relied relies relying unreliability unreliable
remain remained remaining remains
remark remarkable remarkably remarked remarking remarks unremarkable unremarkably unremarked
remind reminded reminder reminders reminding reminds
remove removable removal removals removed remover removers removes removing
repair repaired repairer repairers repairing repairs unrepaired
repeat repeatable repeated repeatedly repeater repeaters repeating repeats repetition repetitions repetitious unrepeatable
replace irreplaceable replaceable replaced replacement replacements replacer replacers replaces replacing
represent rep representation representational representations representative representativeness representatives represented representing represents reps unrepresentative unrepresented
require required requirement requirements requires requiring
research researched researcher researchers researches researching
reserve reservation reservations reserved reserves reserving reservist reservists unreserved unreservedly
resist nonresistant resistance resistances resistant resisted resister resisters resistible resisting resistive resistivity resistless resistor resistors resists unresistant unresisting unresistingly
respect respectable respectably respected respecter respecters respectful respectfully respecting respects
restaurant restaurants
result resultant resulted resulting results
retire ret retd retiral retired retirement retirements retires retiring
rice rices
ridiculous ridicule ridiculed ridicules ridiculing ridiculously
rip ripped ripping rips
risk risked riskier riskiest riskiness risking riskless risks risky
roar roared roarer roarers roaring roars
rob robbed robber robberies robbers robbery robbing robs
role roles
roof roofed roofing roofless roofs rooves
root rooted rootedness rooting rootless rootlessness rootlet rootlets roots
rope roped ropes roping
rot rots rotted rotten rottener rottenest rottenly rottenness rotting
row rowed rower rowers rowing rows
royal royalism royalist royalists royally royals royalties royalty
rub rubbed rubbing rubs
rude rudely rudeness ruder rudest
ruin ruination ruined ruining ruinous ruinously ruins
rush rushed rusher rushers rushes rushing
saint sainthood sainthoods saintliness saintly saints
sake sakes
salad salads
salary salaried salaries salarys
sale resale resales saleable sales unsaleable
salt salted saltier saltiest salting salts salty unsalted
sand sanded sander sanders sanding sands sandy
sandwich sandwiched sandwiches sandwiching
satisfy satisfied satisfies satisfying satisfyingly unsatisfied unsatisfying
sauce sauces
sausage sausages
scale scalable scaled scales scaling scalings
scene scenery scenes scenic scenically
schedule nonscheduled reschedule rescheduled reschedules rescheduling sch scheduled schedules scheduling unscheduled
score scored scorer scorers scores scoring
scratch scratched scratches scratchiness scratching scratchings scratchy unscratched
scream screamed screamer screamers screaming screams
screen screened screening screenings screens
screw screwed screwing screws unscrew unscrewed unscrewing unscrews
seal reseal resealed resealing reseals sealant sealants sealed sealer sealers sealing seals unsealed
search searched searcher searchers searches searching searchingly
season nonseasonal seasonal seasonality seasonally seasons unseasonal
seconds sec secs
secret secretive secretively secretiveness secretly secrets
section sectional sectioned sectioning sections subsection subsections
seed seeded seeding seedless seedling seedlings seeds unseeded
seek seeker seekers seeking seeks sought unsought
select reselection selectable selected selecting selection selections selective selectively selectivities selectivity selector selectors selects unselected
senior seniority seniors snr
sentence sentences
separate separated separately separateness separatenesses separates separating separation separations separatism separatist separatists
september sept
series
sew sewed sewing sewn sews unsewn
shade shaded shades shadiness shading shadings shady unshaded
shadow shadowed shadowing shadows shadowy
shame shamed shameful shamefully shameless shamelessly shames shaming
sharp sharpen sharpened sharpener sharpeners sharpening sharpens sharper sharpest sharpish sharply sharpness
shave shaved shaven shaver shavers shaves shaving shavings unshaven
shed shedding sheds
sheep
sheet sheeted sheeting sheets
shelf shelve shelved shelves shelving
shell shelled shelling shells unshelled
shelter sheltered sheltering shelters unsheltered
shift shifted shifting shifts
shine shined shines shininess shining shiny shone
shiver shivered shivering shivers shivery
shock shocked shocker shockers shocking shockingly shocks unshockable
shore shores
shove shoved shoves shoving
shower showered showering showers showery
signal signaling signalled signalling signally signals
silence silenced silencer silencers silences silencing unsilenced
silver silvered silvering silvery
similar dissimilar dissimilarities dissimilarity similarities similarity similarly
sink sank sinkable sinker sinkers sinking sinks sunk sunken unsinkable
site sited sites siting
ski skied skier skiers skiing skiings skis
skill skilful skilfully skilled skillful skillfully skilling skills unskilfully unskilled unskillfully
skirt skirts
slave antislavery slaved slavery slaves slaving slavish slavishly
slide slid slider sliders slides sliding
smart smarten smartened smartening smartens smarter smartest smartly smartness smarty
smash smashed smasher smashers smashes smashing unsmashed
smooth smoothed smoother smoothest smoothing smoothly smoothness smoothnesses smooths
snake snaked snakes snaking
snap snapped snapper snappers snapping snaps
social antisocial socially unsocial
society societal societies
sock socks
soil soils subsoil subsoils
soldier soldiered soldiering soldiers soldiery
solid solidification solidified solidifies solidify solidifying solidities solidity solidly solids
somewhat
sore sorely soreness sorer sores sorest
sorted sorting unsorted
soul soulful soulfully soulless soullessly souls
soup soups soupy
southern southerner southerners southernmost
spare spared spares sparing sparingly unsparing unsparingly
species sp specie spp subspecies
specific nonspecific specifically specification specifications specificities specificity specifics unspecific
speech speeches speechless
speed sped speeded speedier speediest speedily speeding speeds speedy
spell misspell misspelled misspelling misspellings misspelt spelled spelling spellings spells spelt
spin spinner spinners spinning spins spun
spirit spirited spiritedly spirits spiritual spiritualised spiritualism spiritualist spiritualists spirituality spiritualized spiritually
split splits splitting
spoil spoiled spoiler spoilers spoiling spoils spoilt unspoiled unspoilt
spray respray resprayed respraying resprays sprayed sprayer sprayers spraying sprays
spread spreadable spreader spreaders spreading spreads
stable instabilities instability stabilisation stabilise stabilised stabiliser stabilisers stabilises stabilising stability stabilization stabilize stabilized stabilizer stabilizers stabilizes stabilizing stabler stablest unstable
staff staffed staffer staffers staffing staffs understaffed
stairs stair
stamp stamped stamping stamps unstamped
standard standardisation standardise standardised standardising standardization standardize standardized standardizing standards substandard unstandardised unstandardized
starve starvation starved starves starving
states interstate statehood stateless statist
steady steadied steadier steadies steadiest steadily steadiness steadying unsteadily unsteadiness unsteady
steak steaks
steam steamed steaming steams steamy
steel steeled steeling steels steely
stiff stiffen stiffened stiffening stiffens stiffer stiffest stiffly stiffness stiffs
stir stirred stirrer stirrers stirring stirrings stirs
stock overstock overstocked overstocking overstocks stocked stocks
stomach stomachs
storm stormed stormier stormiest stormily storminess storming storms stormy
strawberry strawberries
stream streamed streaming streams
strength strengthen strengthened strengthening strengthens strengths
stress stressed stresses stressful stressing unstressed
stretch stretchable stretched stretches stretchiness stretching stretchy unstretched
string stringed stringing strings stringy strung
strip stripped stripper strippers stripping strips
stroke stroked strokes stroking
struggle struggled struggler strugglers struggles struggling
style restyle restyled restyles restyling styled styles styling stylisation stylise stylised stylises stylish stylishly stylising stylist stylistic stylistically stylistics stylists stylization stylize stylized stylizes stylizing
success successes successful successfully unsuccessful unsuccessfully
suck sucked sucking sucks
suffer suffered sufferer sufferers suffering sufferings suffers
sugar sugared sugars sugary
super
supply resupplied resupplies resupply resupplying supplied supplier suppliers supplies supplying
surface resurface resurfaced resurfaces resurfacing subsurface subsurfaces surfaced surfaces surfacing
surround surrounded surrounding surroundings surrounds
survive survivability survival survivalist survivalists survivals survived survives surviving survivor survivors
suspect suspected suspecting suspects unsuspected unsuspecting
suspicion suspicions suspicious suspiciously
swallow swallowed swallowing swallows
swear swearing swears swore sworn
sweep sweeper sweepers sweeping sweeps swept
swing swinging swings swung
switch switchable switched switches switching
sword swords
tale tales
tank antitank tankful tankless tanks
tap tapped tapper tappers tapping taps untapped
taxi taxied taxiing taxis
tease teased teaser teasers teases teasing teasingly
technology tech technological technologically technologies technologist technologists
teenage teenaged teenager teenagers
tempt temptation temptations tempted tempting tempts
tense tensed tensely tenseness tenser tenses tensest tensing tension tensions
tent tented tents
th
theatre theater theaters theatres theatric theatrical theatricality theatrically theatrics
therefore
thief thieved thieves thieving
thin thinly thinned thinner thinness thinnest thinning thins
threat threaten threatened threatening threateningly threatens threats unthreatening
thus
ticket ticketless tickets ticketted ticketting
tide intertidal tidal tides
tin tinful tinfuls tinned tinny tins
tiny tinier tiniest tininess
tip tipped tipper tippers tipping tips
title titled titles titling untitled
toast toasted toaster toasters toastier toastiest toasting toasts toasty untoasted
toe toed toeing toes
toilet toileted toileting toilets
tomato tomatoes
tone tonal tonality toned toneless tonelessly toner toners tones toning
tongue tongued tongues
tool tooled tooling tools
topic topical topicality topically topics
tough toughen toughened toughener tougheners toughening toughens tougher toughest toughies toughness toughy
tour toured tourer tourers touring tourism tourist touristic tourists tours
towel towelette towelettes towelling towels
tower towered towering towers
toy toyed toying toys
trace traceable traced traces tracing untraceable
trade traded trader traders trades trading
tradition trad traditional traditionalism traditionalist traditionalists traditionally traditions
traffic
transfer transferability transferable transferee transferees transference transferer transferers transferor transferors transferral transferrals transferred transferring transfers
trap trapped trapper trappers trapping traps
tray trays
trial retrial retrials trialed trialing trialings trials
trick tricked tricker trickeries trickers trickery trickier trickiest trickily trickiness tricking tricks tricky
truck trucked trucker truckers trucking trucks
trunk trunks
tune tuned tuneful tunefully tuneless tunelessly tuner tuners tunes tuning
twin twinned twinning twins
twist twisted twister twisters twisting twistings twists twisty untwisted
typical typically untypical untypically
union unionisation unionism unionisms unionist unionists unionization unions
unit subunit subunits units
unite reunite reunited reunites reuniting united unites uniting
university preuniversity univ universities
upper uppermost
upset upsets upsetting
valley valleys
value invaluable invaluably revaluation revaluations revalue revalued revalues revaluing valuable valuables valuation valuations valued valueless valuer valuers values valuing
various variously
vary invariable invariably invariance invariant invariate unvaried unvarying variability variable variables variably variance variances variant variants variate variates variation variations varied varies varying
vegetable veg vegetables veggie veggies vegs
vehicle vehicles vehicular
version versions
victim victimisation victimise victimised victimising victimization victimize victimized victimizing victimless victims
village villager villagers villages
violent nonviolent nonviolently violently
vote voted voter voters votes voting
wage unwaged waged wages waging
wander wandered wanderer wanderers wandering wanderings wanders
warn warned warning warningly warnings warns
weak weaken weakened weakening weakens weaker weakest weakling weaklings weakly weakness weaknesses
weapon weaponless weapons
weed weeded weedier weediest weeding weedless weeds weedy
weird weirder weirdest weirdly weirdness weirdo weirdos
welcome unwelcome unwelcomed unwelcoming welcomed welcomes welcoming
western midwestern westerner westerners westernisation westernise westernised westernises westernising westernization westernize westernized westernizes westernizing westerns
whereas
whip whipped whipping whips
whistle whistled whistler whistlers whistles whistling
wicked wickeder wickedest wickedly wickedness
wing winged winging wings
wipe unwiped wiped wiper wipers wipes wiping
wire wired wires wiring wirings
wise unwise unwisely wisdom wisely wiseness wiser wisest
witness unwitnessed witnessed witnesses witnessing
wolf wolfish wolfishly wolves
wool woolen woolens woolies woollen woollens woollies woolly wools
worm wormed wormier wormiest worming worms wormy
wound unwounded wounded wounding wounds
wrap unwrap unwrapped unwrapping unwraps wrapped wrapper wrappers wrapping wrappings wraps
yell yelled yelling yells''')

bnccoca3unsplit = ('''abandon abandoned abandoning abandonment abandons
abort aborted aborting abortion abortions abortive abortively aborts
abroad
absence absences
absorb absorbance absorbed absorbency absorbent absorber absorbers absorbing absorbs absorption absorptions absorptive
abstract abstracted abstractedly abstracting abstraction abstractions abstractly abstractness abstracts
abuse abused abuser abusers abuses abusing abusive
academy academic academically academicals academician academicians academics academies unacademic
accelerate accelerated accelerates accelerating acceleration accelerations accelerator accelerators
accommodate accommodated accommodates accommodating accommodation accommodations
accompany accompanied accompanies accompaniment accompaniments accompanist accompanists accompanying unaccompanied
accomplish accomplished accomplishes accomplishing accomplishment accomplishments
accountable accountabilities accountability unaccountable unaccountably
accumulate accumulated accumulates accumulating accumulation accumulations accumulative accumulatively accumulator accumulators
accurate accuracies accuracy accurately inaccuracies inaccuracy inaccurate inaccurately
ache ached aches aching
achieve achievable achieved achievement achievements achiever achievers achieves achieving unachievable
acknowledge acknowledged acknowledgement acknowledgements acknowledges acknowledging acknowledgment acknowledgments unacknowledged
acquire acquired acquirer acquirers acquires acquiring unacquired
acquisition acquisitions
acre acreage acres
addict addicted addicting addiction addictions addictive addicts nonaddictive
adequate adequately inadequate inadequately
adjust adjustable adjusted adjuster adjusters adjusting adjustment adjustments adjusts nonadjustable readjust readjusted readjusting readjustment readjustments readjusts unadjusted
administration admin administrations
administrative administratively
administrator administrators
admission admissions readmission readmissions
adolescent adolescence adolescences adolescents
adopt adopted adopter adopters adopting adoption adoptions adoptive adopts
advocate advocated advocates advocating
affection affectionate affectionately affections affective affectively
affirm affirmation affirmations affirmative affirmatively affirmatives affirmed affirming affirms reaffirm reaffirmation reaffirmations reaffirmed reaffirming reaffirms
agency agencies interagency
agenda agendas
aggressive aggressively aggressiveness aggressivenesses
agriculture agricultural agriculturalist agriculturalists agriculturally agriculturist agriculturists
aim aimed aiming aimless aimlessly aimlessness aims
aircraft
airline airliner airliners airlines
album albums
alert alerted alerting alertly alertness alerts
alien alienate alienated alienates alienating alienation aliens inalienable
allege allegation allegations alleged allegedly alleges alleging
alliance alliances
allocate allocated allocates allocating allocation allocations reallocate reallocated reallocates reallocating reallocation reallocations
ally allied allies allying
alongside
alternative alternatively alternatives
amend amendable amended amending amendment amendments amends
analyse analysed analyser analysers analyses analysing analysis analyze analyzed analyzes analyzing
analyst analysts
ancient anciently ancients
angle angled angles angling
annual annually annuals
anticipate anticipated anticipates anticipating anticipation anticipations anticipatory unanticipated
anxiety anxieties
apology apologies apologise apologised apologises apologising apologist apologists apologize apologized apologizes apologizing
appropriate appropriacy appropriately appropriateness inappropriacy inappropriate inappropriately inappropriateness
approve approval approvals approved approver approvers approves approving approvingly preapprove preapproved preapproves preapproving
approximate approx approximated approximately approximates approximating approximation approximations
archaeology archaeological archaeologically archaeologist archaeologists archeologist archeologists archeology
architect architects
architecture architectural architecturally architectures
arise arisen arises arising arose
armed arming unarmed
aspect aspects
assault assaulted assaulting assaults
assemble assemblage assemblages assembled assembler assemblers assembles assembling
assembly assemblies
assert asserted asserting assertion assertions assertive assertively assertiveness asserts unassertive
assess assessable assessed assesses assessing assessment assessments assessor assessors reassess reassessed reassessing reassessment reassessments unassessed
asset assets
assign assigned assignee assignees assigning assignment assignments assigns reassign reassigned reassigning reassignment reassignments reassigns unassigned
assumption assumptions
athlete athletes athletic athletically athleticism athletics nonathletic
atom atomic atomise atomised atomiser atomisers atomises atomising atomism atomize atomized atomizer atomizers atomizes atomizing atoms subatomic
attribute attributable attributed attributes attributing attribution attributions attributive attributives unattributed
audience audiences
audit audited auditing auditor auditors auditory audits
author authored authoress authoresses authorial authoring authors authorship
authorise authorisation authorisations authorised authorises authorising authorization authorizations authorize authorized authorizes authorizing unauthorised unauthorized
authority authorities
award awarded awarding awards
bacterium bacteria bacterial
ban banned banning bans
bargain bargained bargaining bargains
barrier barriers
beam beamed beaming beams
behave behaved behaves behaving misbehave misbehaved misbehaves misbehaving
behaviour behavior behavioral behaviorism behaviorist behaviorists behaviors behavioural behaviourism behaviourist behaviourists behaviours misbehavior misbehaviors misbehaviour misbehaviours
belief beliefs disbelief unbelief
bench bencher benchers benches
bias biased biases biasing unbiased
bible bibles biblical
bid bidden bidder bidders bidding bids unbidden
biological biologically
bishop archbishop archbishops archbishopship bishops bishopship
blast blasted blaster blasters blasting blasts
blend blended blender blenders blending blends unblended
boost boosted booster boosters boosting boosts
border bordered bordering borders
boundary boundaries
broadcast broadcasted broadcaster broadcasters broadcasting broadcasts
budget budgetary budgeted budgeting budgets
burden burdened burdening burdens unburden unburdened unburdening unburdens
bureau bureaus bureaux
cabinet cabinets
campaign campaigned campaigner campaigners campaigning campaigns
cancel canceled canceling cancellation cancellations cancelled cancelling cancels
cancer cancerlike cancerous cancers
candidate candidacies candidacy candidates candidature
capacity capacities incapacities incapacity
capture captured captures capturing uncaptured
carbon carbons
carve carved carver carveries carvers carvery carves carving carvings
catalogue catalog catalogs catalogued catalogues cataloguing
category categories categorisation categorise categorised categorises categorising categorization categorize categorized categorizes categorizing uncategorised uncategorized
catholic catholicism catholics
cattle
cease ceased ceaseless ceaselessly ceases ceasing unceasing unceasingly
celebrate celebrated celebrates celebrating celebration celebrations celebratory uncelebrated
cell celled cells
ceremony ceremonial ceremonially ceremonials ceremonies ceremonious ceremoniously unceremoniously
chairman chairmanship chairmanships chairmen chairperson chairpersons chairwoman chairwomen
chamber chambered chambers
characteristic characteristically characteristics uncharacteristic uncharacteristically
charity charities
chart charted charting charts uncharted
charter chartered charterer charterers chartering charters
chemical chemically chemicals
chill chilled chiller chillier chilliest chilliness chilling chillingly chills chilly
circuit circuited circuiting circuitous circuitries circuitry circuits
circulate circulated circulates circulating circulation circulations circulatory uncirculated
cite citation citations cited cites citing uncited
civil civilities civility
civilian civilians
civilise civilisation civilisations civilised civilises civilising civilization civilizations civilize civilized civilizes civilizing uncivilised uncivilized
clarify clarification clarified clarifies clarifying clarity
clause clauses
client clients
climate climates climatic climatically climatological
clinic clinical clinically clinician clinicians clinics nonclinical
cluster clustered clustering clusters
coalition coalitionist coalitionists coalitions
code coded codes coding uncoded
coin coinage coinages coined coining coins
coincide coincided coincidence coincidences coincident coincidental coincidentally coincides coinciding
collaborate collaborated collaborates collaborating collaboration collaborationist collaborationists collaborations collaborative collaboratively collaborator collaborators
collapse collapsed collapses collapsible collapsing
colleague colleagues
colony colonial colonialism colonialisms colonialist colonialists colonially colonials colonies colonisation colonise colonised colonising colonist colonists colonization colonize colonized colonizing neocolonialism
column col cols columnar columned columns
combat combatant combatants combated combating combative combativeness combats combatted combatting
comedy comedian comedians comedies
commission commissioned commissioner commissioners commissioning commissions uncommisioned
communicate communicated communicates communicating communication communications communicative communicatively communicator communicators uncommunicative
communist anticommunist anticommunists commie commies communists
companion companionable companionably companions companionship
compensate compensated compensates compensating compensation compensations compensatory
compete anticompetitive competed competes competing competitive competitively competitiveness competitor competitors uncompetitive uncompetitiveness
competent competencies competency competently incompetence incompetences incompetent incompetently incompetents
complaint complainant complainants complaints
complex complexed complexes complexities complexity
component componentry components
compose composed composer composers composes composing composition compositional compositions
compound compoundable compounded compounding compounds
comprehensive comp comprehensively comprehensiveness comps
comprise comprised comprises comprising
compromise compromised compromises compromising uncompromising uncompromisingly
conceive conceivable conceivably conceived conceives conceiving inconceivable inconceivably
concept conception conceptions concepts conceptual conceptualisation conceptualisations conceptualise conceptualised conceptualises conceptualising conceptualization conceptualizations conceptualize conceptualized conceptualizes conceptualizing conceptually
concert concerts
conclude concluded concludes concluding unconcluded
conclusion conclusions
concrete concreted concretely concretes concreting
condemn condemnation condemned condemning condemns
conduct conductance conducted conducting conduction conductive conductivity conductor conductors conducts semiconductor semiconductors
confer conference conferences conferencing conferred conferring confers
confess confessed confesses confessing confession confessional confessions confessor confessors
confidence confidences
confident confidently unconfident
confine confined confinement confinements confines confining unconfined
confirm confirmation confirmations confirmatory confirmed confirming confirms unconfirmed
conflict conflicted conflicting conflicts conflictual
confront confrontation confrontational confrontations confronted confronting confronts
congress congresses congressional
consent consented consenting consents
consequence consequences
consequent consequently
conservative conservatively conservatives
conserve conservation conservationism conservationist conservationists conservator conservators conserved conserves conserving
considerable considerably inconsiderable
consist consisted consisting consists
consistent consistently inconsistent
constitute constituent constituents constituted constitutes constituting constitutive constitutively
constitution constitutional constitutionalism constitutionality constitutionally constitutions unconstitutional
constrain constrained constraining constrains constraint constraints unconstrained
construct constructed constructing construction constructional constructions constructive constructively constructivist constructivists constructor constructors constructs reconstruct reconstructed reconstructing reconstruction reconstructions reconstructs unreconstructed
consult consultancies consultancy consultant consultants consultation consultations consultative consulted consulting consults
consume consumable consumables consumed consumer consumerism consumerist consumers consumes consuming
consumption
contemporary contemporaries
contend contended contender contenders contending contends contention contentions
content contents
contest contestable contestant contestants contested contesting contests incontestable uncontested
context contexts contextual contextualise contextualised contextualising contextualize contextualized contextualizing contextually uncontextualised uncontextualized
continent continental continentals continents
contradict contradicted contradicting contradiction contradictions contradictory contradicts
contrast contrasted contrasting contrastive contrasts
controversy controversial controversially controversies uncontroversial
convention conventional conventionalism conventionality conventionally conventions unconventional unconventionally
convert converted converter converters convertibility convertible convertibles converting converts unconverted
convey conveyance conveyancer conveyancers conveyances conveyancing conveyancings conveyed conveyer conveyers conveying conveyor conveyors conveys
convict convicted convicting conviction convictions convicts unconvicted
cooperate cooperated cooperates cooperating cooperation cooperative cooperatively cooperatives uncooperative uncooperatively
coordinate coordinated coordinates coordinating coordination coordinator coordinators ordinated ordinating ordinator ordinators uncoordinated
core cored cores coring
corporate corp corporately corporates corporation corporations corporatism corporatist corporatists
correlate correlated correlates correlating correlation correlational correlations uncorrelated
correspond corresponded correspondence correspondences corresponding correspondingly corresponds
correspondent correspondents
corridor corridors
corrupt corrupted corrupter corrupters corruptest corruptible corrupting corruption corruptly corruptness corrupts incorruptible
counsel counseled counseling counselings counselled counselling counsellings counsellor counsellors counselor counselors counsels
courage courageous courageously
craft crafted crafting crafts
crew crewed crewing crews
crisis crises crisises
criteria criterion criterions
critic critical critically critics uncritical uncritically
criticise criticised criticises criticising criticize criticized criticizer criticizers criticizes criticizing
criticism criticisms
crop cropped cropper croppers cropping crops
crucial crucially
cruise cruised cruiser cruisers cruises cruising
crush crushed crusher crushers crushes crushing crushingly
crystal crystallisation crystallise crystallised crystallises crystallising crystallization crystallize crystallized crystallizes crystallizing crystals
currency currencies
curriculum curricula curricular curriculums
curtain curtained curtaining curtains
curve curvaceous curvature curvatures curved curves curving curvy
custom customarily customary customs
cycle cycled cycles cyclic cyclical cycling cyclist cyclists
damn dammit damnable damnation damndest damned damnedest damning damnit damns
damp damped dampen dampened dampener dampeners dampening dampens damper dampers dampest damping damply dampness damps
data datum
database databases dbase dbases
debate debatable debated debates debating
decade decades
declare declaration declarations declared declarer declarers declares declaring undeclared
decline declined declines declining
decrease decreased decreases decreasing
dedicate dedicated dedicatedly dedicates dedicating dedication dedications
defeat defeated defeating defeatism defeatist defeatists defeats undefeated
defend defended defender defenders defending defends undefended
defendant defendants
deficit deficits
define definable defined defines defining definition definitional definitions indefinable indefinably predefined redefine redefined redefines redefining redefinition redefinitions undefinable undefined
delay delayed delaying delays
delegate delegated delegates delegating delegation delegations
deliberate deliberately
democracy democracies
democrat democratic democratically democratisation democratisations democratise democratised democratises democratising democratization democratizations democratize democratized democratizes democratizing democrats dems nondemocratic undemocratic
demonstrate demo demonstrated demonstrates demonstrating demonstration demonstrations demonstrative demonstratively demonstratives demonstrator demonstrators demos undemonstrative
dense densely denseness denser densest densities density
depict depicted depicting depiction depictions depicts
deposit deposited depositing depositor depositors depository deposits
deputy deputies deputise deputised deputises deputising deputize deputized deputizes deputizing
derive derivation derivations derivative derivatives derived derives deriving
descend descendant descendants descended descending descends
description descriptions descriptive
designate designated designates designating designation designations
despite
destruction destruct destructive destructively destructiveness indestructible indestructibly
devastate devastated devastates devastating devastatingly devastation devastations
device devices
devote devoted devotedly devotee devotees devotes devoting devotion devotional devotions
dialogue dialog dialogic dialogs dialogues
dictate dictated dictates dictating dictation dictations dictator dictatorial dictatorially dictators dictatorship dictatorships
differ differed differing differs
digital digitally
dimension dimensional dimensions
diplomat diplomatic diplomatically diplomats
disabled disabilities disability disable disablement disablements disables disabling
disagree disagreeable disagreeably disagreed disagreeing disagreement disagreements disagrees
disaster disasters disastrous disastrously
disc discette discettes discs disk diskette diskettes disks
discharge discharged discharger dischargers discharges discharging undischarged
discount discounted discounter discounters discounting discounts
discourse discourses
discreet discreeter discreetest discreetly discreetness discretely discretion discretionary indiscreet indiscreetly indiscrete indiscretion indiscretions
discriminate discriminated discriminates discriminating discrimination discriminations discriminatory indiscriminate indiscriminately nondiscriminatory
dismiss dismissal dismissals dismissed dismisses dismissing dismissive dismissively
disorder disordered disorderly disorders
display displayed displaying displays undisplayed
dispose disposable disposal disposals disposed disposes disposing dispositive indisposed
dispute disputation disputations disputed disputes disputing undisputed
disrupt disrupted disrupting disruption disruptions disruptive disruptively disrupts
distant distantly
distinct distinction distinctions distinctive distinctively distinctiveness distinctivenesses distinctly distinctness indistinct indistinctly
distinguish distinguishable distinguished distinguishes distinguishing indistinguishable undistinguished
distribute distributable distributed distributes distributing distribution distributional distributions distributive distributor distributors redistribute redistributed redistributes redistributing redistribution redistributive
diverse diversely diverseness diversities diversity
division divisional divisions
dna dnas
doctrine doctrinal doctrines
document documentation documented documenting documents undocumented
domestic domestically domesticities domesticity domestics
dominant
dominate dominated dominates dominating domination
donate donated donates donating donation donations
dose dosage dosages dosed doses dosing dosings
draft drafted drafter drafters drafting drafts redraft redrafted redrafting redrafts
drain drainage drainages drained drainer draining drains
drift drifted drifter drifters drifting drifts
drill drilled driller drillers drilling drills
duke archduke archdukes dukedom dukedoms dukes
eager eagerly eagerness uneager
eastern easterner easterners easternmost
echo echoed echoes echoing
edition editions
effective effectively effectiveness ineffective ineffectively ineffectiveness ineffectivenesses
efficient efficiencies efficiency efficiently inefficiencies inefficiency inefficient inefficiently
elaborate elaborated elaborately elaborateness elaborates elaborating elaboration elaborations unelaborated
electronic electronically electronics
element elements
elevate elevated elevates elevating elevation elevations elevator elevators
eliminate eliminated eliminates eliminating elimination eliminations eliminator eliminators
elite elites elitism elitist elitists
embrace embraced embraces embracing
emerge emerged emergence emergent emerges emerging
emergency emergencies
emit emission emissions emits emitted emitter emitters emitting
emphasis emphases
emphasise emphasised emphasises emphasising emphasize emphasized emphasizes emphasizing unemphasised unemphasized
enable enabled enabler enablers enables enabling
encounter encountered encountering encounters unencountered
endorse endorsed endorsement endorsements endorser endorsers endorses endorsing
endure endurable endurance endurances endured endures enduring unendurable
enforce enforceability enforceable enforced enforcement enforcements enforcer enforcers enforces enforcing nonenforceable unenforceable
enhance enhanced enhancement enhancements enhancer enhancers enhances enhancing
ensure ensured ensures ensuring
enterprise enterprises
enthusiasm enthusiasms
enthusiastic enthusiast enthusiastically enthusiasts unenthusiastic unenthusiastically
entitle entitled entitlement entitlements entitles entitling unentitled
entrance entrances
entry entries reentries reentry
episode episodes episodic episodically
equation equations
equivalent equivalently equivalents
era eras
error errors
essay essayist essayists essays
essential essentialist essentialists essentiality essentialized essentially essentials
estimate est estimated estimates estimating estimation estimations estimator estimators
etc cetera etcetera
ethnic ethnical ethnically ethnicity ethnicization ethnics
evaluate evaluated evaluates evaluating evaluation evaluations evaluative evaluator evaluators
evident evidently
evolution evolutionarily evolutionary evolutionism evolutionist evolutionists
evolve evolved evolves evolving
exceed exceeded exceeding exceedingly exceeds
exception exceptionable exceptional exceptionalities exceptionality exceptionally exceptions unexceptionable unexceptional
excess excesses excessive excessively
exclude excluded excludes excluding
exclusive exclusively exclusiveness exclusivity
execute executable executed executes executing execution executioner executioners executions
executive exec execs executives
exhibit exhibited exhibiting exhibition exhibitionism exhibitionist exhibitionists exhibitions exhibitor exhibitors exhibits
expand expandability expandable expanded expanding expands
expansion expansionary expansionism expansionist expansionists expansions
expenditure expenditures
experiment experimental experimentalism experimentalist experimentalists experimentally experimentation experimented experimenter experimenters experimenting experiments
expert expertly expertness experts inexpert
explicit explicitly explicitness
exploit exploitable exploitation exploitations exploitative exploited exploiter exploiters exploiting exploits
explore exploration explorations exploratory explored explorer explorers explores exploring unexplored
explosion explosions explosive explosively explosiveness explosives nonexplosive
export exported exporter exporters exporting exports
extension ext extensions
extensive extensively extensiveness
extent extents
external externalisation externalise externalised externalises externalising externalities externality externalization externalize externalized externalizes externalizing externally externals
extract extracted extracting extraction extractions extractive extractor extractors extracts
extraordinary extraordinarily
fabric fabrics
facilitate facilitated facilitates facilitating facilitation facilitative facilitator facilitators
facility facilities
factor factored factoring factors
factory factories
faculty faculties
fade faded fades fading unfaded unfading
failure failures
false falsehood falsehoods falsely falseness falsifiable falsification falsifications falsified falsifies falsify falsifying falsity
fantasy fantasies fantasise fantasised fantasises fantasising fantasize fantasized fantasizes fantasizing phantasies phantasy
fate fated fates fating
federal federalism federalist federalists federalize federalized federalizes federalizing federally
fee fees
feminist feminists
fertile fertilisation fertilise fertilised fertiliser fertilisers fertilises fertilising fertility fertilization fertilize fertilized fertilizer fertilizers fertilizes fertilizing infertile infertility
festival festivals
fibre fiber fibers fibres fibrous
fiction fictional fictions nonfiction
fierce fiercely fierceness fiercer fiercest
filter filtered filtering filters filtrate filtrated filtrating filtration filtrations unfiltered
firms
flavour flavor flavored flavoring flavorings flavors flavoured flavouring flavourings flavours
flee fled fleeing flees
flesh fleshed fleshes fleshiness fleshing fleshy
flexible flexibility flexibly inflexibility inflexible inflexibly
focus foci focused focuses focusing focussed focusses focussing refocus refocused refocuses refocusing refocussed refocusses refocussing unfocused unfocussed
forecast forecasted forecaster forecasters forecasting forecasts
formal formalisation formalise formalised formalising formalism formalist formalistic formalists formalities formality formalization formalize formalized formalizing formally
format formats formatted formatting
formation formations
former formerly
formula formulae formulaic formulas formulate formulated formulates formulating formulation formulations reformulate reformulated reformulating reformulation reformulations
foster fostered fostering fosters
foundation foundations
founded founder founders founding founds unfounded
fragment fragmentary fragmentation fragmented fragmenting fragments
framework frameworks
frequency frequencies infrequency
frequent frequented frequenting frequently frequents infrequent infrequently
fuel fueled fueling fuelled fuelling fuels
fulfil fulfill fulfilled fulfilling fulfillment fulfillments fulfills fulfilment fulfilments fulfils unfulfilled unfulfilling
function functional functionalism functionalist functionalists functionalities functionality functionally functioned functioning functions
fundamental fundamentalism fundamentalist fundamentalists fundamentally fundamentals
funeral funerals
furthermore
gallery galleried galleries
gang ganged ganging gangs
gap gapped gappy gaps
gaze gazed gazes gazing
gender gendered genders
gene genes
generate generated generates generating generative generatively
generous generosities generosity generously ungenerous
genetic genetically geneticist geneticists genetics
genuine genuinely genuineness
geography geographer geographers geographic geographical geographically geographies
gesture gestured gestures gesturing
global globalisation globalise globalised globalises globalising globalism globalist globalists globalization globalize globalized globalizes globalizing globally
glow glowed glowing glowingly glows
goods
gradual gradualism gradualist gradually
graduate graduated graduates graduating graduation graduations
grain grained grains grainy
graphic graphical graphically graphics
grasp grasped grasping grasps
grateful gratefully gratefulness ungrateful ungratefully ungratefulness
grave graves
gravity gravitate gravitated gravitates gravitating gravitation gravitational gravities
greet greeted greeting greetings greets
grip gripped gripper grippers gripping grips
gross grosser grossest grossly grossness
guideline guidelines
guitar guitarist guitarists guitars
halt halted halting haltingly halts
harbor harbored harboring harbors harbour harboured harbouring harbours
harsh harsher harshest harshly harshness
hazard hazarded hazarding hazardous hazardously hazards nonhazardous
headquarters headquartered hq hqs
heal healed healer healers healing healings heals
heel heeled heels
hence
heritage heritages
highlight highlighted highlighter highlighters highlighting highlights
highway highways
hint hinted hinting hints
hip hipped hips
holy holier holiest holiness unholier unholiest unholiness unholy
horror horrors
host hosted hostess hostesses hosting hosts
hostile hostiles hostilities hostility
household households
humour humor humored humoredly humoring humorless humorlessly humorous humorously humors humoured humouredly humouring humourless humourlessly humourous humourously humours
hypothesis hypotheses hypothesise hypothesised hypothesises hypothesising hypothesize hypothesized hypothesizes hypothesizing
ideal idealisation idealisations idealise idealised idealising idealism idealist idealists ideality idealization idealizations idealize idealized idealizing ideally ideals
ideology ideologies ideologist ideologists
immigrant immigrants
immune immunisation immunisations immunise immunised immunising immunities immunity immunization immunizations immunize immunized immunizing immuno
impact impacted impacting impacts
imperial imperialism imperialist imperialists
implement implementation implementations implemented implementing implements
implicate implicated implicates implicating implication implications
imply implied impliedly implies implying
import importation importations imported importer importers importing imports
importance unimportance
impose imposed imposer imposers imposes imposing imposingly imposition impositions
impression impressionable impressions
incentive incentives
incident incidents
incorporate inc incorporated incorporates incorporating incorporation incorporations unincorporated
independence
independent independently independents
index indexation indexed indexer indexers indexes indexical indexing indices
inevitable inevitability inevitably
infant infancy infants
infect infected infecting infection infections infectious infectiously infectiousness infective infects noninfectious reinfect reinfected reinfecting reinfection reinfections reinfects uninfected
inflate hyperinflation inflatable inflated inflates inflating inflation inflationary
ingredient ingredients
inhabit inhabitable inhabitant inhabitants inhabited inhabiting inhabits uninhabitable uninhabited
inherit inheritance inheritances inherited inheriting inheritor inheritors inherits
initial initialisation initialisations initialise initialised initialises initialising initialization initializations initialize initialized initializes initializing initialled initialling initially initials
initiate initiated initiates initiating initiation initiations initiative initiatives initiator initiators uninitiated
inject injected injecting injection injections injector injectors injects
innovate innovated innovates innovating innovation innovations innovator innovators innovatory
input inputs inputting
inquire inquired inquirer inquirers inquires inquiries inquiring inquiry
insert inserted inserting insertion insertions inserts
insight insightful insights
inspire inspiration inspirational inspirations inspired inspires inspiring uninspired uninspiring
install instal installation installations installed installer installers installing installs
instinct instinctive instinctively instincts instinctual instinctually
institute instituted institutes instituting
institution institutional institutionalisation institutionalise institutionalised institutionalises institutionalising institutionalization institutionalize institutionalized institutionalizes institutionalizing institutionally institutions
integrate integrated integrates integrating integration integrative integrator integrators reintegrate reintegrated reintegrates reintegrating reintegration reintegrations
intellectual intellectualise intellectualism intellectualize intellectually intellectuals
intelligence intelligences
interact interacted interacting interaction interactional interactionally interactionism interactionist interactions interactive interactively interactivity interacts
interfere interfered interference interferes interfering
interior interiors
internal internalisation internalise internalised internalises internalising internalization internalize internalized internalizes internalizing internally
international internationalisation internationalise internationalised internationalises internationalism internationalist internationalists internationalization internationalize internationalized internationalizes internationally internationals
interpret interpretable interpretation interpretations interpretative interpreted interpreter interpreters interpreting interpretive interprets misinterpret misinterpretation misinterpretations misinterpreted misinterpreting misinterprets reinterpret reinterpretation reinterpretations reinterpreted reinterpreting reinterprets
intervene intervened intervener interveners intervenes intervening intervention interventionism interventionist interventionists interventions
intimate intimacies intimacy intimated intimately intimates intimating intimation intimations
invasion invasions
invent invented inventing invention inventions inventor inventors invents reinvent reinvented reinventing reinvention reinventions reinvents
invest invested investing investment investments investor investors invests reinvest reinvested reinvesting reinvestment reinvests
irony ironic ironical ironically ironies
isolate isolated isolates isolating isolation isolationism isolationist isolationists
jail jailed jailer jailers jailing jails
jet jets jetted jetting
joint jointed jointing jointly joints
journal journals
journalist journalistic journalists
jury juries
justify justifiable justifiably justification justifications justified justifies justifying unjustifiable unjustifiably unjustified
label labeled labeling labelled labeller labellers labelling labels unlabeled unlabelled
landscape landscaped landscaper landscapers landscapes landscaping
latter latterly
laughter
launch launched launcher launchers launches launching
layer layered layering layers
leak leakage leakages leaked leakier leakiest leakiness leaking leaks leaky
lease leased leaser leasers leases leasing sublease subleased subleases subleasing
leather leatheriness leathers leathery
lecture lectured lecturer lecturers lectures lectureship lectureships lecturing
legend legendarily legendary legends
legislate legislated legislates legislating legislation legislations legislative legislatively legislator legislators
legitimate illegitimacy illegitimate illegitimately legit legitimacy legitimated legitimately legitimates legitimating legitimation
liable liabilities liability
liberal illiberal lib liberalisation liberalise liberalised liberalises liberalising liberalism liberality liberalization liberalize liberalized liberalizes liberalizing liberally liberals
liberate liberated liberates liberating liberation liberationist liberationists liberations liberator liberators
liberty liberties
likeness likenesses unlike
link interlink interlinked interlinking interlinks linkage linkages linked linker linkers linking links unlinked
liquid liquidities liquidity liquids
literal literally
literary
literature literatures
lobby lobbied lobbies lobbying lobbyings lobbyist lobbyists
lodge lodged lodger lodgers lodges lodging lodgings
logic illogical illogicality illogically logical logically logician logicians logics
loyal loyalist loyalists loyally loyalties loyalty
luxury luxuriance luxuriant luxuriantly luxuries luxurious luxuriously
magnet magnetic magnetically magnetics magnetise magnetised magnetises magnetising magnetism magnetization magnetize magnetized magnetizes magnetizing magnets nonmagnetic
majority majorities
manifest manifestation manifestations manifested manifesting manifestly manifests
manipulate manipulated manipulates manipulating manipulation manipulations manipulative manipulator manipulators
manual manually manuals
manufacture manufacturable manufactured manufacturer manufacturers manufactures manufacturing
margin marginal marginalisation marginalise marginalised marginalising marginality marginalization marginalize marginalized marginalizing marginally marginals margined margins
marine
mature immature immaturely immatures immaturity maturation maturational matured maturely matures maturing maturities maturity prematurity
mayor mayoral mayoress mayoresses mayors
meanwhile
mechanic mechanical mechanically mechanics
mechanism mechanisms
media
medium mediums
menu menus
mere merely merest
merge demerger merged merger mergers merges merging
method methodical methodically methodological methodologically methodologies methodology methods
migrate migrated migrates migrating migration migrations migratory nonmigratory transmigration
mild milder mildest mildly mildness
miner mined miners mines mining
minimum minimums
ministry ministries
missile antimissile missiles
mixture mixtures
mobile immobile immobility mobiles mobilities mobility
mode modes modish
moderate immoderate immoderately moderately moderateness moderates
modest immodest immodestly modestly modesty
modify modification modifications modified modifier modifiers modifies modifying unmodified
module modular modularity modules
molecule molecular molecules
monitor monitored monitoring monitors unmonitored
monster monsters monstrosities monstrosity monstrous monstrously
moral moralise moralised moralises moralising moralist moralistic moralistically moralists morality moralize moralized moralizes moralizing morally morals
moreover
mortal immortal immortalise immortalised immortalises immortalising immortalities immortality immortalize immortalized immortalizes immortalizing immortally immortals mortalities mortality mortally mortals
mortgage mortgaged mortgagee mortgagees mortgages mortgaging remortgage remortgaged remortgages remortgaging unmortgaged
motion motioned motioning motionless motions
motive motivate motivated motivates motivating motivation motivational motivations motivator motivators motiveless motives unmotivated
multiple multiples
museum museums
mutual mutuality mutually
myth mythic mythical mythically myths
naked nakedly nakedness
narrate narrated narrates narrating narration narrations narrative narratives narrator narrators
negative negatively negatives negativism negativity
neglect neglected neglecting neglects
negotiate negotiated negotiates negotiating negotiation negotiations negotiator negotiators renegotiate renegotiated renegotiates renegotiating renegotiation renegotiations
net nets netted netter netters netting nettings
network networked networker networkers networking networks
neutral neutralisation neutralise neutralised neutralises neutralising neutrality neutralization neutralize neutralized neutralizes neutralizing neutrally neutrals
nevertheless
nod nodded nodding nods
nominate nominated nominates nominating nomination nominations
notion notions
novel novelist novelistic novelists novels
nuclear
numerous
objected objecting objection objectionable objectionably objections objector objectors unobjectionable
objective objectively objectives objectivism objectivist objectivistic objectivity
oblige nonobligatory obligate obligated obligates obligating obligation obligations obligatorily obligatory obliged obligee obligees obliges obliging obligingly
obtain obtainable obtained obtaining obtains unobtainable
occupation occupational occupationally occupations
occupy occupancy occupant occupants occupied occupier occupiers occupies occupying unoccupied
ocean oceanic oceans
offence inoffensive inoffensively inoffensiveness offences offense offenses offensive offensively offensiveness offensives unoffensive
offend offended offender offenders offending offends
opera operas operatic
opponent opponents
oral orally
organ organist organists organs
organic inorganic inorganically organically organics
oriented orientate orientated orientates orientation orientations orienteering orienting orients reorient reorientation reoriented reorienting reorients
origin origins
outcome outcomes
outline outlined outlines outlining
output outputs
outrage outraged outrageous outrageously outrages outraging
overall
overcome overcame overcomes overcoming
overlook overlooked overlooking overlooks
overseas
overwhelm overwhelmed overwhelming overwhelmingly overwhelms
pace paced pacer pacers paces pacing
pad padded padding pads
palace palaces
pale paled paleness paler pales palest
palm palmed palming palms
panel paneled paneling panelled panelling panels
paragraph para paragraphed paragraphing paragraphs paras
parallel paralleled paralleling parallelism parallelled parallelling parallels unparalleled
parish parishes
parliament parliamentarian parliamentarians parliamentary parliaments
participant participants
participate participated participates participating participation participations participative participatory
passage passages
passenger passengers
passion passionate passionately passionless passions
patients
pave paved pavement pavements paves paving pavings unpaved
peak peaked peaking peaks
peasant peasantries peasantry peasants
peer peerage peerages peerless peers
penalty penalties
pepper peppered peppers peppery
perceive perceived perceives perceiving
perception misperception misperceptions perceptions
permanent impermanent permanently
permission permissions
permit permits permitted permitting
persist persisted persistence persistency persistent persistently persisting persists
personality personalities
personnel
perspective perspectival perspectives
persuade persuaded persuader persuaders persuades persuading
petrol petrological
phase phased phases phasing
phenomenon phenomena phenomenoms
philosophy philosopher philosophers philosophic philosophical philosophically philosophies philosophise philosophised philosophises philosophising philosophize philosophized philosophizes philosophizing
phrase misphrased misphrasing misphrasings phrasal phrased phrases phrasing phrasings rephrase rephrased rephrases rephrasing
pilot piloted piloting pilots
pit pits pitted pitting
platform platforms
plot plots plotted plotter plotters plotting
poll polled polling pollings polls
portion portioned portioning portions
portrait portraits portraiture
pose posed poser posers poses posing
potential potentialities potentiality potentially potentials
poverty
powder powdered powdering powders powdery
practitioner practitioners
praise praised praises praising
precede preceded precedence precedent precedents precedes preceding unprecedented unprecedentedly
precise imprecise imprecision precisely preciseness precision
predict predictability predictable predictably predicted predicting prediction predictions predictive predictor predictors predicts unpredictability unpredictable unpredictably
premise premised premises premising
presence presences
preserve preservation preservative preservatives preserved preserver preservers preserves preserving
priest priestess priestesses priesthood priestlier priestliest priestliness priestly priests
primary primaries primarily
principal principally principals
principle principled principles unprincipled
prior priors
priority priorities prioritisation prioritise prioritised prioritises prioritising prioritization prioritize prioritized prioritizes prioritizing
privilege privileged privileges privileging
prize prized prizes
probe probed probes probing
procedure procedural procedures
proceed proceeded proceeding proceedings proceeds
professor prof professorial professors professorship professorships profs
profile profiled profiles profiling
profit nonprofit profitability profitable profitably profited profiteer profiteered profiteering profiteers profiting profitless profits unprofitability unprofitable
profound profounder profoundest profoundly profoundness
prohibit prohibited prohibiting prohibition prohibitionist prohibitionists prohibitions prohibitive prohibitively prohibitory prohibits
prominent prominently
promote promo promos promoted promoter promoters promotes promoting promotion promotional promotions
prompt prompted prompting promptings promptly prompts unprompted
proof disproof disproofs proofed proofing proofs
proportion proportional proportionality proportionally proportionate proportionately proportioned proportions
prosecute prosecuted prosecutes prosecuting prosecution prosecutions prosecutor prosecutors
prospect prospective prospectively prospects
prosper prospered prospering prosperities prosperity prosperous prosperously prosperousness prospers
protein proteins
province provinces provincial provincialism provincially
provision provisioning provisions
provoke provocation provocations provocative provocatively provocativeness provoked provokes provoking unprovoked
psychiatry psychiatric psychiatrics psychiatrist psychiatrists
psychology psychological psychologically psychologies psychologist psychologists
publication publications
publish publishable published publisher publishers publishes publishing republish republished republishes republishing unpublished
pupil pupils
pursue pursued pursuer pursuers pursues pursuing
puzzle puzzled puzzlement puzzlements puzzler puzzlers puzzles puzzling
quantity quantitative quantitatively quantities
racial interracially intraracial nonracial racialisation racialised racialism racialist racialists racialization racialized racially racism racist racists
radiate radiated radiates radiating radiation radiations radiative
radical radicalism radicalisms radically radicals
rage enrage enraged enrages enraging raged rages raging
raid raided raider raiders raiding raids
rail railed railing railings rails
rally rallied rallies rallying
random randomisation randomisations randomise randomised randomises randomization randomizations randomize randomized randomizes randomizing randomly randomness ranomising
rank ranked ranking rankings ranks unranked
rape raped rapes raping rapist rapists
ratio ratios
rational irrational irrationalities irrationality irrationally rationalisation rationalisations rationalise rationalised rationalises rationalising rationalism rationalist rationalistic rationalists rationality rationalization rationalizations rationalize rationalized rationalizes rationalizing rationally
raw rawer rawest rawness
rear reared rearing rears
rebel rebelled rebelling rebellings rebellion rebellions rebellious rebelliously rebelliousness rebels
receiver receivers receivership receiverships
reception receptionist receptionists receptions
recession recessional recessionary recessions
recognition recognitions
recruit recruited recruiter recruiters recruiting recruitment recruits
reflect reflectance reflected reflecting reflection reflections reflective reflectively reflectiveness reflects unreflecting
reform reformation reformative reformatory reformed reformer reformers reforming reformism reformist reformists reforms unreformed
refuge refugee refugees refuges
regime regimes 
regret regretful regretfully regrets regrettable regrettably regretted regretting
regulate regulated regulates regulating regulation regulations regulator regulators regulatory unregulated
reinforce reinforced reinforcement reinforcements reinforcer reinforcers reinforces reinforcing
reject rejected rejecting rejection rejections rejects
relative relatively relativise relativised relativises relativising relativism relativist relativistic relativists relativize relativized relativizes relativizing
relatives
relevant irrelevancies irrelevancy irrelevant relevancy relevantly
relieve relieved relieves relieving
religion religions
religious irreligious religiosity religiously
reluctant reluctantly
remedy remediable remedial remedially remedied remedies remedying
remote remotely remoteness remoter remotest
render rendered rendering renderings renders
reproduce reproduced reproduces reproducibility reproducible reproducing reproduction reproductions
republic republican republicanism republicans republics
reputation reputations
request requested requester requesters requesting requests
rescue rescued rescuer rescuers rescues rescuing
resemble resemblance resemblances resembled resembles resembling
reside resided residence residences residencies residency resident residential residents resides residing
resign resignation resignations resigned resignedly resigning resigns
resolution resolutions
resolve resolved resolves resolving unresolved
resort resorted resorting resorts
resource resourced resourceful resourcefulness resources resourcing underresourced unresourceful
respective irrespective irrespectively respectively
respond responded respondent respondents responder responders responding responds
response responses responsive responsively responsiveness unresponsive
restore restoration restorations restorative restored restorer restorers restores restoring unrestored
restrain restrained restraining restrains restraint restraints unrestrained
restrict restricted restricting restriction restrictions restrictive restrictively restricts unrestricted unrestrictive
resume resumed resumes resuming resumption
retail retailed retailer retailers retailing retails
retain retained retainer retainers retaining retains
retreat retreated retreating retreats
reveal revealed revealing revealingly reveals revelation revelations unrevealed
revenue revenues
reverse irreversible irreversibly reversal reversals reversed reverser reversers reverses reversible reversibly reversing
review reviewable reviewed reviewer reviewers reviewing reviews
revise revised reviser revisers revises revising revision revisionary revisionism revisionist revisionists revisions unrevised
revive revival revivalist revivals revived revives reviving
revolution revolutionaries revolutionary revolutionise revolutionised revolutionises revolutionising revolutionist revolutionists revolutionize revolutionized revolutionizes revolutionizing revolutions
reward rewarded rewarding rewards unrewarded unrewarding
rhythm rhythmic rhythmical rhythmically rhythmics rhythms
ritual ritualisation ritualised ritualistic ritualistically ritualization ritualized ritually rituals
rival rivalled rivalling rivalries rivalry rivals unrivalled
romantic romantically romanticisation romanticise romanticised romanticises romanticising romanticization romanticize romanticized romanticizes romanticizing romantics unromantic
route routed routes routing
routine routinely routines subroutine subroutines
rumour rumor rumored rumoring rumors rumoured rumouring rumours
rural
sacrifice sacrificed sacrifices sacrificial sacrificing
sample sampled samples sampling
sanction sanctioned sanctioning sanctions unsanctioned
satellite satellites
satisfaction satisfactions
scan scanned scanner scanners scanning scans
scandal scandalise scandalised scandalises scandalising scandalize scandalized scandalizes scandalizing scandalous scandals
scatter scattered scattering scatters
scheme schematic schematically schemed schemes scheming
scholar scholarly scholars
scope scoped scoping scpes
sculpt sculpted sculpting sculptor sculptors sculpts sculptural sculpture sculptured sculptures sculpturing
secretary secretarial secretaries secretaryship
sector sectoral sectors
segment segmental segmentary segmentation segmentations segmented segmenting segments
seize seized seizes seizing
senate senates
senses sensed sensing sensings
sensible sensibilities sensibility sensibly
sensitive insensitive insensitivity sensitively sensitivities sensitivity
sequence sequenced sequences sequencing sequential sequentially unsequenced
session sessional sessions
severe severely severeness severer severest severity
shield shielded shielding shields unshielded
shortly
shrug shrugged shrugging shrugs
sigh sighed sighing sighs
significance insignificance significances
significant insignificant insignificantly significantly
silent silently
silk silken silkier silkiest silkily silkiness silks silky
simultaneous simultaneity simultaneously
sin sinful sinfully sinfulness sinned sinner sinners sinning sins
slice sliced slicer slicers slices slicing unsliced
slope sloped slopes sloping
software softwares
sole solely
solution solutions
solve solved solves solving unsolvable unsolved
sophisticated sophisticate sophisticates sophisticating unsophisticated
source sourced sources sourcing unsourced
sovereign sovereigns sovereignties sovereignty
specify specifiable specified specifies specifying unspecified
speculate speculated speculates speculating speculation speculations speculative speculatively speculator speculators
spill spillage spillages spilled spilling spills spilt unspilt
sponsor sponsored sponsoring sponsors sponsorship sponsorships
squeeze squeezed squeezes squeezing
stain stained staining stainless stains unstained
stake staked stakes staking
statistic statistical statistically statistician statisticians statistics
status statuses
statute statutes statutorily statutory
stem stemmed stemming stems
stimulate stimulated stimulates stimulating stimulation stimulations stimulatory
strain strained strainer strainers straining strains
strategy strategic strategically strategies strategist strategists
strict stricter strictest strictly strictness
structure poststructuralism poststructuralist restructure restructured restructures restructuring structural structuralism structuralisms structuralist structuralists structurally structured structures structuring unstructured
studio studios
stun stunned stunner stunners stunning stunningly stuns
submit submits submitted submitting
subsequent subsequently
subsidy subsidies subsidise subsidised subsidises subsidising subsidize subsidized subsidizes subsidizing
substance substances
substantial insubstantial insubstantially substantiality substantially
substitute substituted substitutes substituting substitution substitutions
subtle subtleness subtler subtlest subtly unsubtle
suburb suburban suburbanisation suburbanite suburbanites suburbanization suburbs
succeed succeeded succeeding succeeds
succession successions successive successively successor successors
sufficient insufficient insufficiently sufficiently
suicide suicidal suicidally suicides
sum summed summing sums
summary summaries summarily summarisation summarisations summarise summarised summarises summarising summarization summarizations summarize summarized summarizes summarizing
summit summits
superior superiority superiors
supervise supervised supervises supervising supervision supervisor supervisors supervisory unsupervised
supplement supplemental supplementary supplementation supplemented supplementing supplements
supreme supremely
surgery surgeries
survey surveyed surveying surveyor surveyors surveys unsurveyed
suspend suspended suspender suspenders suspending suspends suspension suspensions
sustain sustainability sustainable sustained sustaining sustains unsustainable
sweat sweated sweatier sweatiest sweating sweats sweaty
swell swelled swelling swellings swells swollen
symbol symbolic symbolical symbolically symbolise symbolised symbolises symbolising symbolism symbolize symbolized symbolizes symbolizing symbols
sympathy sympathetic sympathetically sympatheticly sympathies sympathise sympathised sympathiser sympathisers sympathises sympathising sympathize sympathized sympathizer sympathizers sympathizes sympathizing unsympathetic unsympathetically
symptom symptomatic symptomatically symptoms
tackle tackled tackles tackling
tactic tactical tactically tactics
talent talented talents untalented
target targeted targeting targets targetted targetting
task tasked tasking tasks
technical technically
technique techniques
temperature temperatures
temporary temp temporarily temps
tender tenderly tenderness
tennis
territory territorial territoriality territorially territories
terror terrorise terrorised terrorising terrorism terrorist terrorists terrorize terrorized terrorizing terrors
text subtext subtexts texts textual textualism textuality textualized
theme thematic thematically themed themes
theoretical theoretic theoretically theoretician theoreticians
theory theories theorist theorists
therapy therapies therapist therapists
thereby
thorough thoroughly thoroughness
thrill thrilled thriller thrillers thrilling thrills
tissue tissues
ton tonnage tonnages tonne tonner tonners tonnes tons
toss tossed tosses tossing
tournament tournaments
tragedy tragedian tragedians tragedies
trail trailed trailing trails
transact transacted transacting transaction transactions transacts
transform transformation transformational transformations transformed transformer transformers transforming transforms
transition transitional transitionally transitions
translate translatable translated translates translating translation translations translator translators untranslatable untranslated
transmit transmissible transmission transmissions transmits transmittal transmitted transmitter transmitters transmitting
transport transportable transportation transported transporter transporters transporting transports
treasure treasured treasurer treasurers treasures treasuries treasuring treasury
treaty treaties
tremendous tremendously
trend trended trending trends
tribe tribal tribalism tribes
trigger triggered triggering triggers
triumph triumphal triumphalism triumphalist triumphalists triumphant triumphantly triumphed triumphing triumphs
troop trooped trooping troops
tube tubed tubes tubing
tunnel tunnelled tunnelling tunnellings tunnels
ultimate ultimately
undergo undergoes undergoing undergone underwent
underlie underlain underlay underlies underly underlying
undertake undertaken undertakes undertaking undertakings undertook
uniform uniformed uniformity uniformly uniforms
unique uniquely uniqueness
unity unities
universe universal universalisation universalise universalised universalises universalising universalism universalist universalistic universalists universality universalization universalize universalized universalizes universalizing universally universals universes
update updated updates updating updatings
urban urbanisation urbanise urbanised urbanist urbanists urbanization urbanize urbanized
urge urged urges urging urgings
urgent nonurgent urgency urgently
utility utilities
vague vaguely vagueness vaguer vaguest
valid invalidity validity validly
variety varietal varieties
vast vaster vastly vastness
venture ventured ventures venturing
versus vs
vessel vessels
veteran veterans
via
vice vices
victory victories victorious
violate violated violates violating violation violations violator violators
violence nonviolence
virtual virtually
virtue virtues virtuous virtuously
virus viruses
visible invisibility invisible invisibly visibility visibly
vision visionaries visionary visions
visual visualisation visualise visualised visualising visualization visualize visualized visualizing visually visuals
vital vitally
volume vol vols volumes
voluntary voluntarily voluntariness voluntaristic
volunteer volunteered volunteering volunteerism volunteers
vulnerable invulnerability invulnerable vulnerabilities vulnerability vulnerably
wealth wealthier wealthiest wealthiness wealthy
weave weaved weaver weavers weaves weaving wove woven
weigh unweighed weighed weigher weighers weighing weighs
welfare
whisper whispered whisperer whisperers whispering whispers
withdraw withdrawal withdrawals withdrawing withdrawn withdraws withdrew
yield unyielding yielded yielding yields
youth youthful youthfully youthfulness youths
zone zonal zoned zones zoning''')



#Check Version - TkInter breaks on 2.6
import sys, os, string, re
if not sys.version_info[:2] == (2, 7):
	print "THIS PROGRAM REQUIRES PYTHON 2.7"

import tkFileDialog

from Tkinter import *
root = Tk()
root.geometry("700x600")
root.title("Text Grader")

p = re.compile(r'\W+')

#set up lists
BNC1=string.split(base1unsplit)
BNC2=string.split(base2unsplit)
BNC3=string.split(base3unsplit)
AWL= string.split(awlunsplit)
GSL1 = string.split(gsl1unsplit)
GSL2=string.split(gsl2unsplit)
BNCCOCA1=string.split(bnccoca1unsplit)
BNCCOCA2=string.split(bnccoca2unsplit)
BNCCOCA3=string.split(bnccoca3unsplit)



filterlist = string.split(filterlistunsplit.lower())


'''
TODO
find out how to autoidentify the temp folder and put the file there
'''



#define
def GradeTextGSL():
	text.delete(1.0, END)
	data = resultsbox.get(1.0,END)    
	resultsbox.delete(1.0, END)
	f = open("tempfile.txt", 'w')    
	data = data.encode('utf-8')
	f.write(data)
	text.insert(END, "INDEX: \n")
	text.insert(END, "GSL1 words are this colour\n", "CLR1")
	text.insert(END, "GSL2 words are this colour \n", "CLR2")
	text.insert(END, "AWL words are this colour\n", "CLR3")
	text.insert(END, "Numbers, web addresses and anything in your filterlist including names are marked this colour \n", "name")
	text.insert(END, "Anything offlist - not in the above lists - is this colour \n", "offlist")
	f = open("tempfile.txt", 'r')  
	count = 0
	for line in f:
	    count += 1
	f.close()
	f = open("tempfile.txt", 'r')  
	for i in range(0,count):
		data = f.readline()
		data = string.split(data)
		for token in data:
			checktokensplit = p.split(token)
			checknum = token[0]
			checktoken = checktokensplit[0]    
			if not checktoken.isalpha() and not len(checktokensplit) < 2:
				checktoken=checktokensplit[1]
			if checknum.isdigit():
				resultsbox.insert(END, token, "name")
				resultsbox.insert(END, " ")
			elif checktoken.startswith("http"):
				resultsbox.insert(END, token, "name")
				resultsbox.insert(END, " ")    
			elif checktoken.lower() in AWL:  
					resultsbox.insert(END, token, "CLR3")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in GSL2:   
					resultsbox.insert(END, token, "CLR2")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in GSL1:   
					resultsbox.insert(END, token, "CLR1")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in filterlist:   
					resultsbox.insert(END, token, "name")
					resultsbox.insert(END, " ")
			else:
					resultsbox.insert(END, token, "offlist")
					resultsbox.insert(END, " ")  
		resultsbox.insert(END, "\n")  


def GradeTextBNC():
	text.delete(1.0, END)
	data = resultsbox.get(1.0,END)    
	resultsbox.delete(1.0, END)
	f = open("tempfile.txt", 'w')    
	data = data.encode('utf-8')
	f.write(data)
	text.insert(END, "INDEX: \n")
	text.insert(END, "BNC1 tokens are this colour\n", "CLR1")
	text.insert(END, "BNC2 tokens are this colour \n", "CLR2")
	text.insert(END, "BNC3 tokens are this colour\n", "CLR3")
	text.insert(END, "Numbers, web addresses and anything in your filterlist including names are this colour \n", "name")
	text.insert(END, "Anything offlist -  not in the above lists - are this colour \n", "offlist")    
	f = open("tempfile.txt", 'r')  
	count = 0
	for line in f:
		count += 1
	f.close()
	f = open("tempfile.txt", 'r')  
	for i in range(0,count):
		data = f.readline()
		data = string.split(data)
		for token in data:
			checktokensplit = p.split(token)
			checknum = token[0]
			checktoken = checktokensplit[0]    
			if not checktoken.isalpha() and not len(checktokensplit) < 2:
				checktoken=checktokensplit[1]
			if checknum.isdigit():
				resultsbox.insert(END, token, "name")
				resultsbox.insert(END, " ")
			elif checktoken.startswith("http"):
				resultsbox.insert(END, token, "name")
				resultsbox.insert(END, " ")    
			elif checktoken.lower() in BNC3:  
					resultsbox.insert(END, token, "CLR3")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in BNC2:   
					resultsbox.insert(END, token, "CLR2")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in BNC1:   
					resultsbox.insert(END, token, "CLR1")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in filterlist:   
					resultsbox.insert(END, token, "name")
					resultsbox.insert(END, " ")
			else:
					resultsbox.insert(END, token, "offlist")
					resultsbox.insert(END, " ")  
		resultsbox.insert(END, "\n")  

def GradeTextBNCCOCA():
	text.delete(1.0, END)
	data = resultsbox.get(1.0,END)    
	resultsbox.delete(1.0, END)
	f = open("tempfile.txt", 'w')    
	data = data.encode('utf-8')
	f.write(data)
	text.insert(END, "INDEX: \n")
	text.insert(END, "BNCCOCA1 tokens are this colour\n", "CLR1")
	text.insert(END, "BNCCOCA2 tokens are this colour \n", "CLR2")
	text.insert(END, "BNCCOCA3 tokens are this colour\n", "CLR3")
	text.insert(END, "Numbers, web addresses and anything in your filterlist including names are this colour \n", "name")
	text.insert(END, "Anything offlist -  not in the above lists - are this colour \n", "offlist")    
	f = open("tempfile.txt", 'r')  
	count = 0
	for line in f:
		count += 1
	f.close()
	f = open("tempfile.txt", 'r')  
	for i in range(0,count):
		data = f.readline()
		data = string.split(data)
		for token in data:
			checktokensplit = p.split(token)
			checknum = token[0]
			checktoken = checktokensplit[0]    
			if not checktoken.isalpha() and not len(checktokensplit) < 2:
				checktoken=checktokensplit[1]
			if checknum.isdigit():
				resultsbox.insert(END, token, "name")
				resultsbox.insert(END, " ")
			elif checktoken.startswith("http"):
				resultsbox.insert(END, token, "name")
				resultsbox.insert(END, " ")    
			elif checktoken.lower() in BNCCOCA3:  
					resultsbox.insert(END, token, "CLR3")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in BNCCOCA2:   
					resultsbox.insert(END, token, "CLR2")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in BNCCOCA1:   
					resultsbox.insert(END, token, "CLR1")
					resultsbox.insert(END, " ")
			elif checktoken.lower() in filterlist:   
					resultsbox.insert(END, token, "name")
					resultsbox.insert(END, " ")
			else:
					resultsbox.insert(END, token, "offlist")
					resultsbox.insert(END, " ")  
		resultsbox.insert(END, "\n")  
            
    
def ShowInfoGSL():
	#didn't bother changing the names - BNC1 is GSL 1, BNC2 is GLS2, BNC3isAWL
	datalist=[]
	infoBNC1list=[]
	infoBNC2list=[]
	infoBNC3list=[]
	infoofflist=[]
	infoBNC1familylist=[]
	infoBNC2familylist=[]
	infoBNC3familylist=[]
	infoofflistfamily=[]
	p= r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"
	l = re.compile("\n")
	text.delete(1.0, END)    
	data = resultsbox.get(1.0,END)


	#Clean and lower text
	httplist = re.findall(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', data)		
	websiteaddressremoved = len(httplist)
	data = re.sub(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', r' ', data) 
	rawtext= re.findall(p, data)
	punctuation=re.compile("\W")
	number=re.compile("\d")
	punctuationremoved=0 
	numberremoved=0
	filterremoved=0
	for token in rawtext:
			if punctuation.match(token):
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
				datalist.append(token.lower())                
	

	text.insert(END, "\n Website addresses cleaned: ")
	text.insert(END, websiteaddressremoved)
	text.insert(END, "\n Punctuation marks removed: ")
	text.insert(END, punctuationremoved)
	text.insert(END, "\n Digits removed: ")
	text.insert(END, numberremoved)
	text.insert(END, "\n Tokens removed using filterlist (see terminal for list): ")
	text.insert(END, filterremoved)
	text.insert(END, "\n\n")



	BNC1missing=[]
	for line in l.split(gsl1unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC1missing.append(words[0])
		else:
			infoBNC1list = infoBNC1list + intersect
			infoBNC1familylist = infoBNC1familylist+ [words[0]]
			
	BNC2missing=[]
	for line in l.split(gsl2unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC2missing.append(words[0])
		else:
			infoBNC2list = infoBNC2list + intersect
			infoBNC2familylist = infoBNC2familylist+ [words[0]]
	
	BNC3missing=[]			
	for line in l.split(awlunsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC3missing.append(words[0])
		else:
			infoBNC3list = infoBNC3list + intersect
			infoBNC3familylist = infoBNC3familylist+ [words[0]]

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
	text.insert(END, 'Number of recognisable word GSL/AWL families in text: ')
	text.insert(END, str(len(set(ALLfamilylists))))
	text.insert(END, "\n")
	text.insert(END, 'Lexical richness: ')
	if len(datalist) < 1:
		text.insert(END, '\n\n ERROR: NO DATA IN INPUT BOX')
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
	totalfamilieslength = len(set(ALLfamilylists))

	text.insert(END, 'From General Service List 1 (998 word families) there are  '),
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc1familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC1familylist)))), "CLR1")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')
	
	text.insert(END, 'From General Service List 2 (988 word families) there are  '),
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc2familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC2familylist)))), "CLR2")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')

	text.insert(END, 'From Academic Word List (570 word families) there are  '),
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc3familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC3familylist)))), "CLR3")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')

	text.insert(END, 'Tokens NOT in GSL1, GSL2 or AWL account for '),
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

	text.insert(END, 'From General Service List 1, the following ')
	text.insert(END, str(len(set(BNC1missing))))
	text.insert(END, ' families are missing.')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC1missing)))), "CLR1")
	text.insert(END, "\n\n")    


	text.insert(END, 'From General Service List 2, these ')
	text.insert(END, str(len(set(BNC2missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC2missing)))), "CLR2")
	text.insert(END, "\n\n")    

	text.insert(END, 'From the Academic Word List, these ')
	text.insert(END, str(len(set(BNC3missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC3missing)))), "CLR3")
	text.insert(END, "\n\n")    


    
def ShowInfoBNC():
	datalist=[]
	infoBNC1list=[]
	infoBNC2list=[]
	infoBNC3list=[]
	infoofflist=[]
	infoBNC1familylist=[]
	infoBNC2familylist=[]
	infoBNC3familylist=[]
	infoofflistfamily=[]
	p= r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"
	l = re.compile("\n") #for 
	text.delete(1.0, END)    
	data = resultsbox.get(1.0,END)

	#Clean and lower text
	httplist = re.findall(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', data)		
	websiteaddressremoved = len(httplist)
	data = re.sub(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', r' ', data) 
	rawtext= re.findall(p, data)
	punctuation=re.compile("\W")
	number=re.compile("\d")
	punctuationremoved=0 
	numberremoved=0
	filterremoved=0
	for token in rawtext:
			if punctuation.match(token):
				token=""    
				punctuationremoved=punctuationremoved+1        
			elif number.match(token):
				token=""
				numberremoved=numberremoved+1    
			elif token in filterlist:
				token=""
				filterremoved = filterremoved+1
			else:
				datalist.append(token.lower())                
	

	text.insert(END, "\n Website addresses cleaned: ")
	text.insert(END, websiteaddressremoved)
	text.insert(END, "\n Punctuation marks removed: ")
	text.insert(END, punctuationremoved)
	text.insert(END, "\n Digits removed: ")
	text.insert(END, numberremoved)
	text.insert(END, "\n Tokens removed using filterlist (see terminal for list): ")
	text.insert(END, filterremoved)
	text.insert(END, "\n\n")



	BNC1missing=[]
	for line in l.split(base1unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC1missing.append(words[0])
		else:
			infoBNC1list = infoBNC1list + intersect
			infoBNC1familylist = infoBNC1familylist+ [words[0]]
			
	BNC2missing=[]
	for line in l.split(base2unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC2missing.append(words[0])
		else:
			infoBNC2list = infoBNC2list + intersect
			infoBNC2familylist = infoBNC2familylist+ [words[0]]
	
	BNC3missing=[]			
	for line in l.split(base3unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC3missing.append(words[0])
		else:
			infoBNC3list = infoBNC3list + intersect
			infoBNC3familylist = infoBNC3familylist+ [words[0]]
	
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
	if len(datalist) < 1:
		text.insert(END, '\n\n ERROR: NO DATA IN INPUT BOX')

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
	totalfamilieslength = len(set(ALLfamilylists))

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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc1familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC1familylist)))), "CLR1")
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc2familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC2familylist)))), "CLR2")
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc3familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC3familylist)))), "CLR3")
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




	text.insert(END, 'From BNC List 1, the following ')
	text.insert(END, str(len(set(BNC1missing))))
	text.insert(END, ' families are missing.')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC1missing)))), "CLR1")
	text.insert(END, "\n\n")    



	text.insert(END, 'From BNC List 2, these ')
	text.insert(END, str(len(set(BNC2missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC2missing)))), "CLR2")
	text.insert(END, "\n\n")    


	text.insert(END, 'From BNC List 3, these ')
	text.insert(END, str(len(set(BNC3missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC3missing)))), "CLR3")
	text.insert(END, "\n\n")    


def ShowInfoBNCCOCA():
	datalist=[]
	infoBNC1list=[]
	infoBNC2list=[]
	infoBNC3list=[]
	infoofflist=[]
	infoBNC1familylist=[]
	infoBNC2familylist=[]
	infoBNC3familylist=[]
	infoofflistfamily=[]
	p= r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"
	l = re.compile("\n")
	text.delete(1.0, END)    
	data = resultsbox.get(1.0,END)


	#Clean and lower text
	httplist = re.findall(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', data)		
	websiteaddressremoved = len(httplist)
	data = re.sub(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', r' ', data) 
	rawtext= re.findall(p, data)
	punctuation=re.compile("\W")
	number=re.compile("\d")
	punctuationremoved=0 
	numberremoved=0
	filterremoved=0
	for token in rawtext:
			if punctuation.match(token):
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
				datalist.append(token.lower())                
	

	text.insert(END, "\n Website addresses cleaned: ")
	text.insert(END, websiteaddressremoved)
	text.insert(END, "\n Punctuation marks removed: ")
	text.insert(END, punctuationremoved)
	text.insert(END, "\n Digits removed: ")
	text.insert(END, numberremoved)
	text.insert(END, "\n Tokens removed using filterlist (see terminal for list): ")
	text.insert(END, filterremoved)
	text.insert(END, "\n\n")

	

	BNC1missing=[]
	for line in l.split(bnccoca1unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC1missing.append(words[0])
		else:
			infoBNC1list = infoBNC1list + intersect
			infoBNC1familylist = infoBNC1familylist+ [words[0]]
			
	BNC2missing=[]
	for line in l.split(bnccoca2unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC2missing.append(words[0])
		else:
			infoBNC2list = infoBNC2list + intersect
			infoBNC2familylist = infoBNC2familylist+ [words[0]]
	
	BNC3missing=[]			
	for line in l.split(bnccoca3unsplit):
		words = re.findall(p,line)
		intersect = [word for word in words if word in datalist]
		if len(intersect) is 0:
				BNC3missing.append(words[0])
		else:
			infoBNC3list = infoBNC3list + intersect
			infoBNC3familylist = infoBNC3familylist+ [words[0]]


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
	text.insert(END, 'Number of recognisable word BNCCOCA1-3 families in text: ')
	text.insert(END, str(len(set(ALLfamilylists))))
	text.insert(END, "\n")
	text.insert(END, 'Lexical richness: ')
	if len(datalist) < 1:
		text.insert(END, '\n\n ERROR: NO DATA IN INPUT BOX')

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
	totalfamilieslength = len(set(ALLfamilylists))

	text.insert(END, 'From BNC-COCA List 1 (first 1000 word families) there are  '),
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc1familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC1familylist)))), "CLR1")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')
	
	text.insert(END, 'From BNC-COCA List 2 (second 1000 word families) there are  '),
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc2familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC2familylist)))), "CLR2")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')

	text.insert(END, 'From BNC-COCA List 3 (third 1000 word families) there are  '),
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
		text.insert(END, ' recognisable families (')
		text.insert(END, str(100 * bnc3familylength / totalfamilieslength))
		text.insert(END, '%)')
		text.insert(END, "\n")
		text.insert(END, string.join(sorted(set((infoBNC3familylist)))), "CLR3")
		text.insert(END, "\n\n")
	else: 
		text.insert(END, ' there are no recognisable families (')

	text.insert(END, 'Tokens NOT in the first three BNC-COCA lists account for '),
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
	text.insert(END, 'From BNC-COCA List 1, the following ')
	text.insert(END, str(len(set(BNC1missing))))
	text.insert(END, ' families are missing.')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC1missing)))), "CLR1")
	text.insert(END, "\n\n")    

	text.insert(END, 'From BNC-COCA List 2, these ')
	text.insert(END, str(len(set(BNC2missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC2missing)))), "CLR2")
	text.insert(END, "\n\n")    

	text.insert(END, 'From BNC-COCA List 3, these ')
	text.insert(END, str(len(set(BNC3missing))))
	text.insert(END, ' families are missing:')
	text.insert(END, "\n")
	text.insert(END, string.join(sorted(set((BNC3missing)))), "CLR3")
	text.insert(END, "\n\n")    

def ShowHelp():
    text.delete(1.0, END)
    text.insert(END, "Word lists used are based on the General Service List, Academic Word List, British National Corpus and Corpus of Contemporary American English, adapted from the files distributed with Paul Nation's RANGE program - see http://www.victoria.ac.nz/lals/about/staff/paul-nation for originals. \n\n\n\n")
    
    text.insert(END, "Collocation/readability functions removed in this version to allow packaging. Please download earlier version of program to get these back, although note that they require NLTK packages. A standalone version will be released soon with these two functions. \n\n\n\n") 
    
    
    

def OpenFile():
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

                
def SaveInfo():
	notes = resultsbox.get(1.0, END)
	#notes = notes.encode('utf-8')
	f = tkFileDialog.asksaveasfile(parent=root,initialfile="results.txt",mode='w',title='Save File')
	if f != None:
		f.write(notes)
		f.close()
    
    
                
def SaveText():
	notes = text.get(1.0, END)
	#notes = notes.encode('utf-8')
	f = tkFileDialog.asksaveasfile(parent=root,initialfile="editedtext.txt",mode='w',title='Save File')
	if f != None:
		f.write(notes)
		f.close()
	


#PACK interface
                
textframe = Frame(root, bd=5, relief=SUNKEN)
resultsframe = Frame(root, bd=5, relief=SUNKEN)
buttonframe = Frame(root, bd=5, relief=SUNKEN)
buttonframe2 = Frame(root, bd=5, relief=SUNKEN)

BNC_button = Button(buttonframe, text="BNC",command = GradeTextBNC)
BNCinfo_button = Button (buttonframe, text="BNC Word Lists", command = ShowInfoBNC)
BNCCOCA_button = Button(buttonframe, text="BNC-COCA",command = GradeTextBNCCOCA)
BNCCOCAinfo_button = Button (buttonframe, text="BNC-COCA Word Lists", command = ShowInfoBNCCOCA)
GSL_button = Button(buttonframe, text="GSL/AWL",command = GradeTextGSL)
GSLinfo_button = Button(buttonframe, text="GSL/AWL Word Lists",command = ShowInfoGSL)

openfile_button = Button(buttonframe2, text="Open File", command = OpenFile)
savetext_button = Button(buttonframe2, text="Save Text (bottom box)", command = SaveText)
saveinfo_button = Button(buttonframe2, text="Save Info (top box)", command = SaveInfo)
help_button = Button (buttonframe2, text="Help & About", command = ShowHelp)

textscrollbar = Scrollbar(textframe, orient=VERTICAL)
text = Text(textframe, yscrollcommand=textscrollbar.set, takefocus=0)
textscrollbar.configure(command=text.yview)


resultsscrollbar = Scrollbar(resultsframe, orient=VERTICAL)
resultsbox = Text(resultsframe, yscrollcommand=resultsscrollbar.set, takefocus=0)
resultsscrollbar.configure(command=resultsbox.yview)

resultsbox.tag_configure('CLR1', foreground='black')
#BNC1 also tag for GSL1 and BNCCOCA1
resultsbox.tag_configure('CLR2', foreground='green')
#BNC2 also tag for GSL2 and BNCCOCA2
resultsbox.tag_configure('CLR3', foreground='orange')
#BNC3 also tag for AWL and BNCCOCA3
resultsbox.tag_configure('offlist', foreground='red')
resultsbox.tag_configure('name', foreground='pink')

text.tag_configure('CLR1', foreground='black')
text.tag_configure('CLR2', foreground='green')
text.tag_configure('CLR3', foreground='orange')
text.tag_configure('offlist', foreground='red')
text.tag_configure('name', foreground='pink')


GSL_button.pack(side=LEFT)
GSLinfo_button.pack(side=LEFT)
BNC_button.pack(side=LEFT)
BNCinfo_button.pack(side=LEFT)
BNCCOCA_button.pack(side=LEFT)
BNCCOCAinfo_button.pack(side=LEFT)

openfile_button.pack(side=LEFT)
savetext_button.pack(side=LEFT)
saveinfo_button.pack(side=LEFT)
help_button.pack(side=LEFT)

text.pack(side=LEFT, fill=BOTH, expand=1)
textscrollbar.pack(side=RIGHT, fill=Y)

resultsbox.pack(side=LEFT, fill=BOTH, expand=1)
resultsscrollbar.pack(side=RIGHT, fill=Y)

buttonframe.pack(fill=X, expand=1)
buttonframe2.pack(fill=X, expand=1)

textframe.pack(fill=BOTH, expand=1)
resultsframe.pack(fill=BOTH, expand=1)

resultsbox.insert(END, "Open a text (TXT) file using the buttons above, paste text here, or just start typing")
text.insert(END, "Information will appear here after you run the program")
root.mainloop()