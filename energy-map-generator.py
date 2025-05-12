# Python 3
# Create a Gui with 6 sections each with check boxes inside

#TODO Add void of course
#TODO Get rid of tabs
#TODO exe
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import random


class Tab:
  def __init__(self, date, planet, lunarSign, solarSign):
    self.date = date
    self.planet = planet
    self.lunarSign = lunarSign
    self.solarSign = solarSign

tabs = []

lunarDays = []
dates = []
planets = []
lunarSigns = []
solarSigns = []

day1 = ''
day2 = ''
day3 = ''
day4 = ''
day5 = ''
day6 = ''
day7 = ''
day8 = ''
day9 = ''
day10 = ''
day11 = ''
day12 = ''
day13 = ''
day14 = ''
day15 = ''
day16 = ''
day17 = ''
day18 = ''
day19 = ''
day20 = ''
day21 = ''
day22 = ''
day23 = ''
day24 = ''
day25 = ''
day26 = ''
day27 = ''
day28 = ''
day29 = ''
day30 = ''
day31 = ''
sun = ''
moon = ''
mars = ''
mercury = ''
jupiter = ''
venus = ''
saturn = ''
aries = ''
taurus = ''
gemini = ''
cancer = ''
leo = ''
virgo = ''
libra = ''
scorpio = ''
sagittarius = ''
capricorn = ''
aquarius = ''
pisces = ''

pn1Influences = ["New Situation", "New Idea", "Beginnings", "Catalyst", "Potential"]
pn2Influences = ["Choice", "Decision", "Crossroad", "Balance", "Awareness"]
pn3Influences = ["Creativity", "Mediation", "Nurturing", "Synthesis", "Nurturing", "Options", "Direction", "Progress"]
pn4Influences = ["Stability", "Structure", "Building", "Effort", "Grounding", "Routine", "Dependability", "Planning"]
pn5Influences = ["Change", "Adventure", "Adjustment", "Modification", "Creativity", "Conviction"]
pn6Influences = ["Obstacles", "Perserverance", "Responsibility", "Nexus"]
pn7Influences = ["Confidence", "Experience", "Progression", "Momentum", "Drive", "Art", "Production", "Vision", "Creativity"]
pn8Influences = ["Advancement", "Personal Power", "Will", "Bridge", "Understanding", "Pattern"]
pn9Influences = ["Attainment", "Completion", "Endings", "Gain", "Culmination", "Fruition"]

sunQualities = ["Creative Energy","Nature of self","Life","Purpose","Consciousness","Power","Vitality","Tradition","Masculine","Yang","Physical Energy","Stamina","The Father","Pride","Honor","Ruling","Authority","Integrity","Individual","Ego","Display","Projection","Fortune","Dignity","Confidence"]
moonQualities = ["Reactions","Soul Development","Inner Being","Feelings","Unconsciousness","Material Substance","Yin","Receptivity","Nurture","Change","Family","Domestic Life","The Mother","Cycles","Rhythm","Instincts","Belonging","Alienation","Containment","Creativity","Intuition","Flexible","Growth","Visionary","Magnetism"]
marsQualities = ["Self Projection","Drive","Ambition","Impulse","Ego","Aggression","Assertion","Sexual Desire","Survival","Yang","Passion","Courage","The Warrior","Anger","Stamina","Sports","Independence","Conflict","Force","Vigor","Mechanical Ability","Engineering","Expression","Destruction","Dynamic","Change","Risk","Punishment"]
mercuryQualities = ["Mental","Mind","Nerves","Sensitivity","Rational","Reason","Intelligence","Language","Duality","Writing","Memory","Pattern Recognition","The Mage","Association","Symbolization","Skills","Versatility","Adaptability","Short Travel","Movement","Transportation","Active","Efficient","Diffuse","Expressive","Inspiration","Androgyne","Mediation","Wit","Cunning"]
jupiterQualities = ["Spirit","Assimilation","Compensation","Good Fortune","Religion","Philosophy","Travel","Material Abundance","Luster","Extravagance","Higher Understanding","Integration","The Guru","Optimism","Aspiration","Poise","Reverence","Influence Over Authority","Wisdom","Benevolence","Prosperity"]
venusQualities = ["Values","Receptiveness","Intake","Harmony","Love","Relation","Social Urges","Art","Beauty","Creation","Affection","Attraction","The Caretaker","Luck","Animal Magnetism","Money","Sensuality","Bonding","Harmony","Gentle","Production","Devotion","Seduction","Refinement","Response","Recreation","Leisure"]
saturnQualities = ["Structure","Form","Responsibility","Protection","Limitation","Fear","Time","Age","Karma","Consequence","Consolidation","Delay","The Judge","Lessons Learned","Tests","Discipline","Law","School","Teachers","Contracts","Obligations","Banishing","Progress","Severity","Stern","Patience","Diplomacy","Humility","Justice"]

mansion1Waxing =["Beginnings", "Take medicine", "Journeys", "Make medicine", "Travel", "Build Energy"]
mansion1Waning =["Discord", "Destroy An Enemy"]

mansion2Waxing =["Find Treasures", "Resource Production", "Structure Work", "Remove Anger", "Grasp Things", "Fashion Magical Tools", "Self Expression", "Creativity", "Reach For Opportunities", "Bindings", "Safeguard Resources", "Reconcile With Authority", "Planting seeds"]
mansion2Waning =["Destroy Structures", "Sow Discord"]

mansion3Waxing =["Sailing", "Alchemy", "Strengthen Bindings", "Fire Workings", "Hunting", "Love", "Gaining Good Things", "Fortune", "Integration"]
mansion3Waning =["Curb overindulgence"]

mansion4Waxing =["Find Treasure", "Favor In Influence", "Big Ticket Items"]
mansion4Waning =["Discord", "Destruction Of Resources", "Bindings", "Destroy Societal Structures", "Fumigation", "Hinder", "Vengeance"]

mansion5Waxing =["Learning", "Scholarship", "Travel Of All Kind", "Structure Work", "Favor From Authority", "Practical Communication", "Joy", "Health", "Dream Work", "Goodwill"]
mansion5Waning =["Destroy Relationships"]

mansion6Waxing =["Friendship", "Hunting", "Love", "Bonds Of All Kinds", "Peace Between Enemies", "Gain Power"]
mansion6Waning =["Besiege Empire", "Revenge", "Destroy Resources", "Conquest"]

mansion7Waxing =["Boost Trade", "Travel", "Friendship Between Allies And Enemies", "Approach Authority", "Gain Favor", "Aquisition", "Strengthen Bonds", "Influence", "Love", "Contact"]
mansion7Waning =["Pest Control", "Destroy High Office", "Destroy Authority"]

mansion8Waxing =["Love", "Friendship", "Strengthen Bindings", "Unexpected Events", "Travel", "Victory"]
mansion8Waning =["Destroy Captives", "Pest Control", "Defense", "Mother Magick", "Vengeance"]

mansion9Waxing =["Defense", "Aid Others", "FBoost Empathy", "Increase Capability"]
mansion9Waning =["Destroy Resources", "Hinder Travel", "Malicious Acts", "Discord", "Sow Weakness"]

mansion10Waxing =["Goodwill", "Aid From Others", "Cure Illness", "Ease Birth", "Boost Imagination", "Strengthen Structure", "Love", "Benevolence", "Bindings"]
mansion10Waning =["Destroy Enemies"]

mansion11Waxing =["Voyages", "Sales", "Liberation", "Reverence", "Retain Respect", "Strengthen Structure", "Accolades", "Good Fortune In All Things"]
mansion11Waning =["Besiege Empire", "Aggression", "Inspire Fear", "Attack"]

mansion12Waxing =["Boost Harvest", "Destruction", "Starting Fresh", "Betterment", "Increase Service", "Compensation For Labor", "Begin Building", "Promotion", "Increase Resources", "Boost Allies"]
mansion12Waning =["Destroy Vehicles", "Separation", "Banish Bad Habits", "Banish Unserving", "Hinder Sails Loss of Investment", "Separation"]

mansion13Waxing =["Boost Trade", "Boost Harvest", "Complete Structure", "Liberation", "Working Practically To Achieve Goals", "Prosperity", "Cleaver Dealings", "Marriage", "Fertility", "Gain", "Bind Authority", "Voyages"]
mansion13Waning =["Maintain Status Quo", "Diminish Gains", "Sly Dealings"]

mansion14Waxing =["Love", "Cure Illness", "Cure Impotence", "Sailing", "Unlikely Bonds", "Boost Divination", "Material Gains", "Boost Leaders", "Friendship"]
mansion14Waning =["Destroy Resources", "Destroy Desire", "Let Go Of Rigidity", "Hinder Travel", "Separation"]

mansion15Waxing =["Locate Treasure", "Take Advantage Of Opportunity", "Create Opportunity", "Networking"]
mansion15Waning =["Hinder Travel", "Separation", "Discord", "Destroy Family Lines", "Destroy Enemies", "Debasement"]

mansion16Waxing =["Liberation", "Friendship", "Trading", "Obtaining All Good Things", "Working For Opportunities", "Increase Resources"]
mansion16Waning =["Destroy Resources", "Discord", "Hinder Travel", "Wedlock", "Hinder Trade"]

mansion17Waxing =["Strategic Maneuvering", "Love Magick", "Strengthen Structure", "Cure Illness", "Fortune", "Friendships", "Sailing"]
mansion17Waning =["Drive away Thieves", "Justice", "Boost Deception", "Banishing"]

mansion18Waxing =["Victory", "Strengthen Structure", "Cure Illness", "Boost Integrity", "Sacrifice Outmoded Thought Patterns", "Liberation", "Healing"]
mansion18Waning =["Scheming", "Conspiracy", "Destroy Friendships", "Discord", "Revolution"]

mansion19Waxing =["Besiege Empire", "Boost Resources", "Binding", "Speed Menses", "Develop Ideas", "Decisions", "Not A Good Time For Business", "Ease Birth"]
mansion19Waning =["Destroy Vehicles", "Ruin Harvest", "Discord", "Banishing", "Destroy Wealth"]

mansion20Waxing =["Tame Animals", "Hunting", "Attract To A Specific Place", "Influence", "Fortify Bonds", "Travel"]
mansion20Waning =["Destroy Wealth", "Discord", "Binding", "Destroy Discord"]

mansion21Waxing =["Strengthen Structures", "Harvest", "Sexual Prowess", "Boost Profits", "Travel"]
mansion21Waning =["Divorce", "Destroy Reputation"]

mansion22Waxing =["Protect The Ill", "Doing The Right Thing", "Cure Illness", "Goodwill", "Liberation", "Change In Lifestyle", "Profitable Partnership"]
mansion22Waning =["Discord", "Inspire Fear", "Marital Conflict"]

mansion23Waxing =["Cure Illness", "Marriage", "Reveal Secrets", "Seek Advice", "Liberation", "Bond Friends"]
mansion23Waning =["Destruction", "Divorce"]

mansion24Waxing =["Boost Trade", "Goodwill", "Increase Resources", "Victory", "Bond Spouses"]
mansion24Waning =["Obstruct Authority", "Gain Power Over Enemies", "Unveil Liars"]

mansion25Waxing =["Repair Structure", "Protect Resources", "New Solutions For Old Issues", "Finding Courage", "Messages", "Bindings", "Destroy Enemies"]
mansion25Waning =["Divorce", "infertility", "Addle", "Revenge", "Besiege"]

mansion26Waxing =["Goodwill", "Love", "Unity", "Favor", "Travel"]
mansion26Waning =["Break Barriers Of Communication", "Destroy Structure"]

mansion27Waxing =["Boost Trade", "Clairvoyance", "Psychic Pursuits", "Boost Spirituality", "Healing Illness", "harvest", "Gain Power", "Strengthen Bindings"]
mansion27Waning =["Obstruct Structure", "hinder Sailing", "Destroy Resources", "Discord"]

mansion28Waxing =["Boost Trade", "Promote Peace", "Strengthen Bindings", "Fishing", "Group Work", "Inner Tranquility", "Visualize Future", "Harvest", "Travel", "Marital Joy"]
mansion28Waning =["Banish", "Besiege Empire", "Destroy", "Hide Treasure", "Hinder Sailing", "Bindings"]

ariesPositive =["Beginning work", "Riding", "Tailoring", "Blood Work", "Swift Action", "Appearing Before Authorities", "Winning competition", "Blood Work", "Travel", "Push Thru Obstacles", "Protection", "Tapping Resources", "Independence", "Hunting", "New Looks", "Transplant", "Focus", "Intensity", "Leadership"]
ariesNegative =["-Concentration", "-Selflessness", "-Truth", "-Justice", "-Laying Foundations", "-Purgatives", "-Arrogance", "-Tyranny", "-Intolerance", "-Lack of -Completion", "-Intensity"]

taurusPositive =["Cultivation", "Foundation Work", "Strengthen Group Bonds", "Acquisition", "Stability", "Fertility", "Earth Magick", "Growth", "Healing", "Introspection", "Meditation", "Grounding", "Renewal", "Maintain Energy", "Appearing Before Authority", "Marrying", "Foundation", "Communicating", "Buying Gems", "Communication", "Making Perfumes", "Reliability", "Productivity", "Stubbornness", "Trading"]
taurusNegative =["-Travel", "-Blood Work", "-Hunting", "-Miserly", "-Violence For Love", "-Opposition", "-Possessiveness", "-Resistance To Change", "-Greed", "-Materialistic", "-Self Indulgence", "-Slow To Move", "-Lazy"]

geminiPositive =["Communication", "integration", "Rapid Thinking", "Swiftness", "Adaptability", "Survival Through Wit", "Glamour", "Politics", "Truth", "Insight", "Heighten Perception", "Making Order", "Education", "Planting Vineyards", "Reconciliation", "Mediation"]
geminiNegative =["-Fighting", "-Foundation Work", "-Marrying", "-Planting", "-Blood Work", "-Completion", "-Wholeness", "-Stability", "-Internal Quests", "-Scattered", "-Scheming", "-Ungrateful", "-Fickle", "-Superficial", "-Tense", "-Nervousness", "-Impatience", "-Restlessness"]

cancerPositive =["Feminine Touch", "Deep Impressions", "Transmute Material Relations", "Attract Aid", "Recollection", "Bindings", "Deception", "Protection", "Protection", "Banishment", "Divination", "Travel", "Purging", "Transplanting", "Trading", "Tailoring"]
cancerNegative =["-Foundation Work", "-Planting", "-Blood Work", "-Independence", "-Focus", "-Stability", "-Forgiveness", "-Withdrawn", "-Moody", "-Erratic", "-Passive", "-Self Absorption", "-Accident Prone", "-Possessiveness", "-Overthinking", "-Laziness", "-Manipulation", "-Materialistic", "-Easily Harmed", "-Self Pity", "-Selfish"]

leoPositive =["Creative Insight", "Loyalty", "Sovereignty", "Money", "Pride", "Vanity", "Creation Of Big Ideas", "Domination Of Will", "Overcome Challenge", "Inner Strength", "Take Control", "Remove Influence", "To Influence", "Appearing Before Authority", "Starting Big Business", "Blood Work", "Fire", "Planting", "Taking Power"]
leoNegative =["-Purging", "-Tailoring", "-New Garb", "-Treating A Patient", "-Distrust", "-Equality", "-Justice", "-Sacrifice", "-Condescending", "-Self Centered", "-Boastful", "-Childishness", "-Cruelness", "-Dramatic", "-Domineering", "-Challenges", "-Provocative", "-Impatience", "-Laziness"]

virgoPositive =["Healing", "Detail Work Of Manifestation", "Protection", "Longevity", "Multiaction Spells", "Longevity", "Manifest Thought Into Form", "Exorcism", "Infrastructure", "Spirit Channeling", "Karmic Cleansing", "Weight Loss", "Making Order", "Cultivating", "Trading", "Communication"]
virgoNegative =["-Planting", "-Travel Over Water", "-Seeing A Woman", "-Playing Music", "-Chaos", "-Sex", "-Love", "-Hyper Critical", "-Perfectionist", "-Unemotional", "-Fearful", "-Pedantic", "-Pettiness", "-Melancholy", "-Pickiness", "-Sloppiness", "-Worry", "-Impatience", "-Obsession"]

libraPositive =["Fairness", "Gain Both Perspectives", "Partnership", "Balance", "Harmonizing", "Conflict Resolution", "Unity", "Networking", "Mediation", "Peace", "Slow / Stop A Process", "Protection", "Legal Matters", "Clear Obstacles", "Seeing Family", "Buying Assets", "Meeting Eunuchs", "Meeting Musicians", "Meeting Prostitutes", "Buying Gems", "Marriage"]
libraNegative =["-Indecisiveness", "-Self Indulgence", "-Apathy", "-Fickleness", "-Impracticality", "-Judgment", "-Peace For A Price", "-Pouting", "-Faithlessness", "-Love Given Too Easily", "-Independence", "-Speedy Endings", "-Finality", "-Banishment", "-Planting", "-Travel Over Water", "-Foundation Work"]

scorpioPositive =["Investigation", "Intensity", "Desire", "Transformation", "Renewal", "Sex Magick", "Jealousy", "Cultivation", "Love", "Attraction", "Fixation", "Enchantment", "Seduction", "Bending Will", "Illumination", "Emotional Healing", "Stimulating Action", "Root Cause", "Purging", "Treating A Patient", "Beginning A Trial", "Fishing", "Navigation", "Leading Many"]
scorpioNegative =["-Possessiveness", "-Clinginess", "-Contradiction", "-Extremeness", "-Intenseness", "-Vengeance", "-Turbulence", "-Suspicions", "-Intolerance", "-Overbearing", "-Probing", "-Tempermentalness", "-Violence", "-Elusion", "-Resentment", "-Obsessiveness", "-Sobriety", "-Forgiveness", "-Weight Loss", "-Meeting With Authority", "-Travel", "-Transplanting"]

sagittariusPositive =["Big Magick", "Growth", "Opportunity", "Deepen Relations", "Spontaneity", "Protect Personal Freedoms", "Multitasking", "Versatility", "Aid Understanding", "Social Justice", "Lift Depression", "Starting Ecclesiastical Work", "Marrying", "Consecrating Temples", "Meeting Matchmakers", "Foundation Work", "Travel", "Engagement"]
sagittariusNegative =["-Waste", "-Accidents Likely", "-Incite Jealousy / Possessiveness", "-Bluntness", "-Arguments", "-Gambling", "-Hot Headedness", "-Impatience", "-Tactlessness", "-Restlessness", "-Superficiality", "-Bindings", "-Control", "-Love", "-Purging"]

capricornPositive =["Survival", "Initiation", "Fate", "Time", "Achievement", "Ambition", "Organization", "Accomplishment", "Discipline", "Restriction", "Career Reputation", "Stabilization", "Long Term Projects", "Generosity", "Defuse Emotional Tension", "Lower Emotional Sensitivity", "Affect Confidence", "Moving forward", "Tailoring", "New clothes", "Communication", "Meeting Civilians", "Meeting Monks", "Philosophers", "Buying Moveable Assets"]
capricornNegative =["-Love", "-Sex", "-Management", "-Meeting With Authority", "-Aloofness", "-Gloominess", "-Conservativeness", "-Brooding", "-Coldness", "-Domineering", "-Fatalistic", "-Inhibition", "-Judgment", "-Over Ambition", "-Perfectionism", "-Status Seeking", "-Stubbornness", "-Unforgiving", "-Reserved", "-Rigidness", "-Pessimism"]

aquariusPositive =["Solitary Magick", "Originality", "Career Development", "Starting A New Business", "Sex", "Power", "New Friends", "New Allies", "Gain Respect", "Generational Healing", "Divination", "Hope", "Speed Up Decisions", "Foundation Work", "Magic", "Playing Cymbals", "Guarding Property", "Buying Land", "Building High Edifices"]
aquariusNegative =[ "-Aloofness", "-Inflexibility", "-Inflation Of Ego", "-Verbal Sparring", "-Bored By Detail", "-Coldness", "-Impersonal", "-Temperamental", "-Unpredictability", "-Strong Dislikes", "-Firm Opinions", "-Intenseness", "-Partnership", "-Cleansing", "-Truth", "-Tailoring", "-New Clothes", "-Transplanting"]

piscesPositive =["Trance", "Astral Projection", "Divination", "Spirit Contact", "Sympathy", "To Create Internal Conflict", "Cleansing", "Inspiration", "Bring Adventure", "Break Cycles", "Contact With Spirit Allies", "Psychic Expression", "Dissolution", "Merging", "Intuition", "Faith", "Spirituality", "Faith", "Spirituality", "Creativity", "Dreams", "Illusion", "Love", "Meeting Religious Officials", "Tailoring", "Meeting Mediators", "New Clothes", "Navigating", "Purgatives", "Fishing", "Contracts and Bonds"]
piscesNegative =["-Transplanting","-Travel Out Of The City","-Laziness","-Impractical","-Indecisive","-Overindulgence","-Escapism","-Inhibition","-Melancholy","-Pessimism","-Spacey","-Timidness","-Withdrawn"]

ageLabels = ["Day 1: Gambling / Luck / Strategy", "Day 2: Gain a winning strategy","Day 3: Talismans / War","Day 4: Love / Bonds","Day 5: Gaining affection of Authority","Day 6 Beneficial Judgment","Day 7: Scrying","Day 8: Burying / Shadow Work","Day 9: Familial Joy / Home Care","Day 10: Epileptic Cure","Day 11: DM Obeisance","Day 12: DM Affection","Day 13: Increase of resources","Day 14: Dealing with Spirits","Day 15: Speaking with Demons","Day 16: Man’s love for woman","Day 17: Stopping a ship from sailing","Day 18: Woman’s confession","Day 19: Opening Locks","Day 20: Eliminating Enemies","Day 21: Avoiding Gossip, Rumors & Insults","Day 22: Unbinding","Day 23: Fishing","Day 24: Accepting Consequence","Day 25: Unbinding a couple","Day 26: Persuading Authority","Day 27: Love","Day 28: Love","Day 29: Destruction"]

dateLabels = ["1st", "2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

dateInfluences = ["[[Archetype 1#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]","[[Archetype 5#Influences|Influences]]","[[Archetype 6#Influences|Influences]]","[[Archetype 7#Influences|Influences]]","[[Archetype 8#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 1#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]","[[Archetype 5#Influences|Influences]]","[[Archetype 6#Influences|Influences]]","[[Archetype 7#Influences|Influences]]","[[Archetype 8#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 1#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]","[[Archetype 5#Influences|Influences]]","[[Archetype 6#Influences|Influences]]","[[Archetype 7#Influences|Influences]]","[[Archetype 8#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]"]

planetLabels = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]

planetInfluences = ["[[Book of Shadows/MOD/Astrology/Planets/Sun#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Planets/Moon#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Planets/Mars#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Planets/Mercury#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Planets/Jupiter#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Planets/Venus#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Planets/Saturn#Influences|Influences]]"]

lunarLabels = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

lunarInfluences = ["[[Book of Shadows/MOD/Astrology/Zodiac/Aries#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Taurus#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Gemini#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Cancer#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Leo#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Virgo#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Libra#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Scorpio#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Sagittarius#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Capricorn#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Aquarius#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Pisces#Influences|Influences]]"]

solarLabels = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

solarInfluences = ["[[Book of Shadows/MOD/Astrology/Zodiac/Aries#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Taurus#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Gemini#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Cancer#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Leo#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Virgo#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Libra#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Scorpio#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Sagittarius#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Capricorn#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Aquarius#Influences|Influences]]","[[Book of Shadows/MOD/Astrology/Zodiac/Pisces#Influences|Influences]]"]


# Window initiation
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Energy Map Generator")
window.geometry("500 x 500")
window.configure(fg_color="#333333")

# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

center = ctk.CTkFrame(window)
center.grid(row=0)

btm_frame2 = ctk.CTkFrame(master=window)
btm_frame2.grid(row=50, sticky="ew", pady=20)

month = ctk.CTkEntry(master=btm_frame2, placeholder_text="Month")
month.grid(row=0, column=0)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(0, weight=1)

def lunarDayCheckBoxes():
  lunarDay = ctk.CTkLabel(master=center, text="Lunar Day")
  lunarDay.grid(row=0, column=1)

  day1 = ctk.CTkCheckBox(center, text="1")
  day2 = ctk.CTkCheckBox(center, text="2")
  day3 = ctk.CTkCheckBox(center, text="3")
  day4 = ctk.CTkCheckBox(center, text="4")
  day5 = ctk.CTkCheckBox(center, text="5")
  day6 = ctk.CTkCheckBox(center, text="6")
  day7 = ctk.CTkCheckBox(center, text="7")
  day8 = ctk.CTkCheckBox(center, text="8")
  day9 = ctk.CTkCheckBox(center, text="9")
  day10 = ctk.CTkCheckBox(center, text="10")
  day11 = ctk.CTkCheckBox(center, text="11")
  day12 = ctk.CTkCheckBox(center, text="12")
  day13 = ctk.CTkCheckBox(center, text="13")
  day14 = ctk.CTkCheckBox(center, text="14")
  day15 = ctk.CTkCheckBox(center, text="15")
  day16 = ctk.CTkCheckBox(center, text="16")
  day17 = ctk.CTkCheckBox(center, text="17")
  day18 = ctk.CTkCheckBox(center, text="18")
  day19 = ctk.CTkCheckBox(center, text="19")
  day20 = ctk.CTkCheckBox(center, text="20")
  day21 = ctk.CTkCheckBox(center, text="21")
  day22 = ctk.CTkCheckBox(center, text="22")
  day23 = ctk.CTkCheckBox(center, text="23")
  day24 = ctk.CTkCheckBox(center, text="24")
  day25 = ctk.CTkCheckBox(center, text="25")
  day26 = ctk.CTkCheckBox(center, text="26")
  day27 = ctk.CTkCheckBox(center, text="27")
  day28 = ctk.CTkCheckBox(center, text="28")
  day29 = ctk.CTkCheckBox(center, text="29")

  day1.grid(row=1, column=0)
  day2.grid(row=1, column=1)
  day3.grid(row=1, column=2)
  day4.grid(row=2, column=0)
  day5.grid(row=2, column=1)
  day6.grid(row=2, column=2)
  day7.grid(row=3, column=0)
  day8.grid(row=3, column=1)
  day9.grid(row=3, column=2)
  day10.grid(row=4, column=0)
  day11.grid(row=4, column=1)
  day12.grid(row=4, column=2)
  day13.grid(row=5, column=0)
  day14.grid(row=5, column=1)
  day15.grid(row=5, column=2)
  day16.grid(row=6, column=0)
  day17.grid(row=6, column=1)
  day18.grid(row=6, column=2)
  day19.grid(row=7, column=0)
  day20.grid(row=7, column=1)
  day21.grid(row=7, column=2)
  day22.grid(row=8, column=0)
  day23.grid(row=8, column=1)
  day24.grid(row=8, column=2)
  day25.grid(row=9, column=0)
  day26.grid(row=9, column=1)
  day27.grid(row=9, column=2)
  day28.grid(row=10, column=0)
  day29.grid(row=10, column=1)
  lunarDays.append(day1)
  lunarDays.append(day2)
  lunarDays.append(day3)
  lunarDays.append(day4)
  lunarDays.append(day5)
  lunarDays.append(day6)
  lunarDays.append(day7)
  lunarDays.append(day8)
  lunarDays.append(day9)
  lunarDays.append(day10)
  lunarDays.append(day11)
  lunarDays.append(day12)
  lunarDays.append(day13)
  lunarDays.append(day14)
  lunarDays.append(day15)
  lunarDays.append(day16)
  lunarDays.append(day17)
  lunarDays.append(day18)
  lunarDays.append(day19)
  lunarDays.append(day20)
  lunarDays.append(day21)
  lunarDays.append(day22)
  lunarDays.append(day23)
  lunarDays.append(day24)
  lunarDays.append(day25)
  lunarDays.append(day26)
  lunarDays.append(day27)
  lunarDays.append(day28)
  lunarDays.append(day29)
  
  return(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25,day26,day27,day28,day29)

def dateCheckBox():
  lunarDay = ctk.CTkLabel(master=center, text="Date")
  lunarDay.grid(row=11, column=1)

  day1 = ctk.CTkCheckBox(center, text="1")
  day2 = ctk.CTkCheckBox(center, text="2")
  day3 = ctk.CTkCheckBox(center, text="3")
  day4 = ctk.CTkCheckBox(center, text="4")
  day5 = ctk.CTkCheckBox(center, text="5")
  day6 = ctk.CTkCheckBox(center, text="6")
  day7 = ctk.CTkCheckBox(center, text="7")
  day8 = ctk.CTkCheckBox(center, text="8")
  day9 = ctk.CTkCheckBox(center, text="9")
  day10 = ctk.CTkCheckBox(center, text="10")
  day11 = ctk.CTkCheckBox(center, text="11")
  day12 = ctk.CTkCheckBox(center, text="12")
  day13 = ctk.CTkCheckBox(center, text="13")
  day14 = ctk.CTkCheckBox(center, text="14")
  day15 = ctk.CTkCheckBox(center, text="15")
  day16 = ctk.CTkCheckBox(center, text="16")
  day17 = ctk.CTkCheckBox(center, text="17")
  day18 = ctk.CTkCheckBox(center, text="18")
  day19 = ctk.CTkCheckBox(center, text="19")
  day20 = ctk.CTkCheckBox(center, text="20")
  day21 = ctk.CTkCheckBox(center, text="21")
  day22 = ctk.CTkCheckBox(center, text="22")
  day23 = ctk.CTkCheckBox(center, text="23")
  day24 = ctk.CTkCheckBox(center, text="24")
  day25 = ctk.CTkCheckBox(center, text="25")
  day26 = ctk.CTkCheckBox(center, text="26")
  day27 = ctk.CTkCheckBox(center, text="27")
  day28 = ctk.CTkCheckBox(center, text="28")
  day29 = ctk.CTkCheckBox(center, text="29")
  day30 = ctk.CTkCheckBox(center, text="30")
  day31 = ctk.CTkCheckBox(center, text="31")

  day1.grid(row=12, column=0)
  day2.grid(row=12, column=1)
  day3.grid(row=12, column=2)
  day4.grid(row=13, column=0)
  day5.grid(row=13, column=1)
  day6.grid(row=13, column=2)
  day7.grid(row=14, column=0)
  day8.grid(row=14, column=1)
  day9.grid(row=14, column=2)
  day10.grid(row=15, column=0)
  day11.grid(row=15, column=1)
  day12.grid(row=15, column=2)
  day13.grid(row=16, column=0)
  day14.grid(row=16, column=1)
  day15.grid(row=16, column=2)
  day16.grid(row=17, column=0)
  day17.grid(row=17, column=1)
  day18.grid(row=17, column=2)
  day19.grid(row=18, column=0)
  day20.grid(row=18, column=1)
  day21.grid(row=18, column=2)
  day22.grid(row=19, column=0)
  day23.grid(row=19, column=1)
  day24.grid(row=19, column=2)
  day25.grid(row=20, column=0)
  day26.grid(row=20, column=1)
  day27.grid(row=20, column=2)
  day28.grid(row=21, column=0)
  day29.grid(row=21, column=1)
  day30.grid(row=21, column=2)
  day31.grid(row=22, column=1)
  dates.append(day1)
  dates.append(day2)
  dates.append(day3)
  dates.append(day4)
  dates.append(day5)
  dates.append(day6)
  dates.append(day7)
  dates.append(day8)
  dates.append(day9)
  dates.append(day10)
  dates.append(day11)
  dates.append(day12)
  dates.append(day13)
  dates.append(day14)
  dates.append(day15)
  dates.append(day16)
  dates.append(day17)
  dates.append(day18)
  dates.append(day19)
  dates.append(day20)
  dates.append(day21)
  dates.append(day22)
  dates.append(day23)
  dates.append(day24)
  dates.append(day25)
  dates.append(day26)
  dates.append(day27)
  dates.append(day28)
  dates.append(day29)
  dates.append(day30)
  dates.append(day31)
  return(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25,day26,day27,day28,day29,day30,day31)

def planetCheckBoxes ():
  sec3_label = ctk.CTkLabel(center, text="Planet")
  
  sun = ctk.CTkCheckBox(center, text="Sun")
  moon = ctk.CTkCheckBox(center, text="Moon")
  mars = ctk.CTkCheckBox(center, text="Mars")
  mercury = ctk.CTkCheckBox(center, text="Mercury")
  jupiter = ctk.CTkCheckBox(center, text="Jupiter")
  venus = ctk.CTkCheckBox(center, text="Venus")
  saturn = ctk.CTkCheckBox(center, text="Saturn")

  sec3_label.grid(row=23, column=1)

  sun.grid(row=24, column=0)
  moon.grid(row=24, column=1)
  mars.grid(row=24, column=2)
  mercury.grid(row=25, column=0)
  jupiter.grid(row=25, column=1)
  venus.grid(row=25, column=2)
  saturn.grid(row=26, column=1)

  planets.append(sun)
  planets.append(moon)
  planets.append(mars)
  planets.append(mercury)
  planets.append(jupiter)
  planets.append(venus)
  planets.append(saturn)

  return sun, moon, mars, mercury, jupiter, venus, saturn

def lunarSignCheckboxes():
  sec5_label = ctk.CTkLabel(center, text="Lunar Sign")

  aries = ctk.CTkCheckBox(center, text="Aries")
  taurus = ctk.CTkCheckBox(center, text="Taurus")
  gemini = ctk.CTkCheckBox(center, text="Gemini")
  cancer = ctk.CTkCheckBox(center, text="Cancer")
  leo = ctk.CTkCheckBox(center, text="Leo")
  virgo = ctk.CTkCheckBox(center, text="Virgo")
  libra = ctk.CTkCheckBox(center, text="Libra")
  scorpio = ctk.CTkCheckBox(center, text="Scorpio")
  sagittarius = ctk.CTkCheckBox(center, text="Sagittarius")
  capricorn = ctk.CTkCheckBox(center, text="Capricorn")
  aquarius = ctk.CTkCheckBox(center, text="Aquarius")
  pisces = ctk.CTkCheckBox(center, text="Pisces")

  sec5_label.grid(row=27, column=1)

  aries.grid(row=28, column=0)
  taurus.grid(row=28, column=1)
  gemini.grid(row=28, column=2)
  cancer.grid(row=29, column=0)
  leo.grid(row=29, column=1)
  virgo.grid(row=29, column=2)
  libra.grid(row=30, column=0)
  scorpio.grid(row=30, column=1)
  sagittarius.grid(row=30, column=2)
  capricorn.grid(row=31, column=0)
  aquarius.grid(row=31, column=1)
  pisces.grid(row=31, column=2)
    
  lunarSigns.append(aries)
  lunarSigns.append(taurus)
  lunarSigns.append(gemini)
  lunarSigns.append(cancer)
  lunarSigns.append(leo)
  lunarSigns.append(virgo)
  lunarSigns.append(libra)
  lunarSigns.append(scorpio)
  lunarSigns.append(sagittarius)
  lunarSigns.append(capricorn)
  lunarSigns.append(aquarius)
  lunarSigns.append(pisces)
  
  return aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces

def solarSignCheckboxes():
  sec5_label = ctk.CTkLabel(center, text="Solar Sign")

  aries = ctk.CTkCheckBox(center, text="Aries")
  taurus = ctk.CTkCheckBox(center, text="Taurus")
  gemini = ctk.CTkCheckBox(center, text="Gemini")
  cancer = ctk.CTkCheckBox(center, text="Cancer")
  leo = ctk.CTkCheckBox(center, text="Leo")
  virgo = ctk.CTkCheckBox(center, text="Virgo")
  libra = ctk.CTkCheckBox(center, text="Libra")
  scorpio = ctk.CTkCheckBox(center, text="Scorpio")
  sagittarius = ctk.CTkCheckBox(center, text="Sagittarius")
  capricorn = ctk.CTkCheckBox(center, text="Capricorn")
  aquarius = ctk.CTkCheckBox(center, text="Aquarius")
  pisces = ctk.CTkCheckBox(center, text="Pisces")

  sec5_label.grid(row=32, column=1)

  aries.grid(row=33, column=0)
  taurus.grid(row=33, column=1)
  gemini.grid(row=33, column=2)
  cancer.grid(row=34, column=0)
  leo.grid(row=34, column=1)
  virgo.grid(row=34, column=2)
  libra.grid(row=35, column=0)
  scorpio.grid(row=35, column=1)
  sagittarius.grid(row=35, column=2)
  capricorn.grid(row=36, column=0)
  aquarius.grid(row=36, column=1)
  pisces.grid(row=36, column=2)
      
  solarSigns.append(aries)
  solarSigns.append(taurus)
  solarSigns.append(gemini)
  solarSigns.append(cancer)
  solarSigns.append(leo)
  solarSigns.append(virgo)
  solarSigns.append(libra)
  solarSigns.append(scorpio)
  solarSigns.append(sagittarius)
  solarSigns.append(capricorn)
  solarSigns.append(aquarius)
  solarSigns.append(pisces)
  
  return aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces

def tableOfContents():
  folder = selectOutput()
  with open(f"{folder}/{month.get()}.md",'a') as file:
    file.write("[[#Lunar Age: Day 1: Gambling / Luck / Strategy|Day 1]]\n")
    file.write("[[#Lunar Age: Day 2: Gain a winning strategy|Day 2]]\n")
    file.write("[[#Lunar Age: Day 3: Talismans / War|Day 3]]\n")
    file.write("[[#Lunar Age: Day 4: Love / Bonds|Day 4]]\n")
    file.write("[[#Lunar Age: Day 5: Gaining affection of Authority|Day 5]]\n")
    file.write("[[#Lunar Age: Day 6 Beneficial Judgment|Day 6]]\n")
    file.write("[[#Lunar Age: Day 7: Scrying|Day 7]]\n")
    file.write("[[#Lunar Age: Day 8: Burying / Shadow Work|Day 8]]\n")
    file.write("[[#Lunar Age: Day 9: Familial Joy / Home Care|Day 9]]\n")
    file.write("[[#Lunar Age: Day 10: Epileptic Cure|Day 10]]\n")
    file.write("[[#Lunar Age: Day 11: DM Obeisance|Day 11]]\n")
    file.write("[[#Lunar Age: Day 12: DM Affection|Day 12]]\n")
    file.write("[[#Lunar Age: Day 13: Increase of resources|Day 13]]\n")
    file.write("[[#Lunar Age: Day 14: Dealing with Spirits|Day 14]]\n")
    file.write("[[#Lunar Age: Day 15: Speaking with Demons|Day 15]]\n")
    file.write("[[#Lunar Age: Day 16: Man’s love for woman|Day 16]]\n")
    file.write("[[#Lunar Age: Day 17: Stopping a ship from sailing|Day 17]]\n")
    file.write("[[#Lunar Age: Day 18: Woman’s confession|Day 18]]\n")
    file.write("[[#Lunar Age: Day 19: Opening Locks|Day 19]]\n")
    file.write("[[#Lunar Age: Day 20: Eliminating Enemies|Day 20]]\n")
    file.write("[[#Lunar Age: Day 21: Avoiding Gossip, Rumors & Insults|Day 21]]\n")
    file.write("[[#Lunar Age: Day 22: Unbinding|Day 22]]\n")
    file.write("[[#Lunar Age: Day 23: Fishing|Day 23]]\n")
    file.write("[[#Lunar Age: Day 24: Accepting Consequence|Day 24]]\n")
    file.write("[[#Lunar Age: Day 25: Unbinding a couple|Day 25]]\n")
    file.write("[[#Lunar Age: Day 26: Persuading Authority|Day 26]]\n")
    file.write("[[#Lunar Age: Day 27: Love|Day 27]]\n")
    file.write("[[#Lunar Age: Day 28: Love|Day 28]]\n")
    file.write("[[#Lunar Age: Day 29: Destruction|Day 29]]\n\n\n")


def lengthCheck(symbol):
  length = len(symbol)
  return length

def randomGrabber(symbol):
  temp = []
  tempLength = lengthCheck(symbol)
  maxLimit = random.randint(0, tempLength-1)
  # print(tempLength)
  # print(maxLimit)
  if maxLimit > 0:
    for choice in range(maxLimit):
      chaos = random.randint(0,tempLength-1)
      quality = symbol[chaos]
      temp.append(quality)
  # print(temp)
  return temp

# randomGrabber(pn1Influences)

def log():
  folder = selectOutput()
  influence = []
  with open(f"{folder}/{month.get()}.md",'a') as file:
    for day in range(len(lunarDays)-1):
        temp = lunarDays[day]
        tempVal = temp.get()
        if tempVal == 1:
          # print(f"{ageLabels[day]}")
          file.write(f"\n\n# Lunar Age: {ageLabels[day]}\n\n")

    for date in range(len(dates)-1):
        temp = dates[date]
        tempVal = temp.get()
        if tempVal == 1:
          # print(f"{ageLabels[day]}")
          file.write(f"\n\n# Date: {dateLabels[date]}\n\n")

    for planet in range(len(planets)-1):
      temp = planets[planet]
      tempVal = temp.get()
      if tempVal == 1:
        # print(f"{planetLabels[planet]}")
        file.write(f"## Planet: {planetLabels[planet]}\n{planetInfluences[planet]}\n\n")
        if planetLabels[planet] == "Sun" :
          influence.append(randomGrabber(sunQualities))
        elif planetLabels[planet] == "Moon" :
          influence.append(randomGrabber(moonQualities))
        elif planetLabels[planet] == "Mars" :
          influence.append(randomGrabber(marsQualities))
        elif planetLabels[planet] == "Mercury" :
          influence.append(randomGrabber(mercuryQualities))
        elif planetLabels[planet] == "Jupiter" :
          influence.append(randomGrabber(jupiterQualities))
        elif planetLabels[planet] == "Venus" :
          influence.append(randomGrabber(venusQualities))
        elif planetLabels[planet] == "Saturn" :
          influence.append(randomGrabber(saturnQualities))

    for lunar in range(len(lunarSigns)-1):
      temp = lunarSigns[lunar]
      tempVal = temp.get()
      if tempVal == 1:
        # print(f"{lunarLabels[lunar]}")
        file.write(f"## Lunar Sign: {lunarLabels[lunar]}\n{lunarInfluences[lunar]}\n\n")
        if lunarLabels[lunar] == "Aries" :
          influence.append(randomGrabber(ariesPositive))
          influence.append(randomGrabber(ariesNegative))
        elif lunarLabels[lunar] == "Taurus" :
          influence.append(randomGrabber(taurusPositive))
          influence.append(randomGrabber(taurusNegative))
        elif lunarLabels[lunar] == "Gemini" :
          influence.append(randomGrabber(geminiPositive))
          influence.append(randomGrabber(geminiNegative))
        elif lunarLabels[lunar] == "Cancer" :
          influence.append(randomGrabber(cancerPositive))
          influence.append(randomGrabber(cancerNegative))
        elif lunarLabels[lunar] == "Leo" :
          influence.append(randomGrabber(leoPositive))
          influence.append(randomGrabber(leoNegative))
        elif lunarLabels[lunar] == "Virgo" :
          influence.append(randomGrabber(virgoPositive))
          influence.append(randomGrabber(virgoNegative))
        elif lunarLabels[lunar] == "Libra" :
          influence.append(randomGrabber(libraPositive))
          influence.append(randomGrabber(libraNegative))
        elif lunarLabels[lunar] == "Scorpio" :
          influence.append(randomGrabber(scorpioPositive))
          influence.append(randomGrabber(scorpioNegative))
        elif lunarLabels[lunar] == "Sagittarius" :
          influence.append(randomGrabber(sagittariusPositive))
          influence.append(randomGrabber(sagittariusNegative))
        elif lunarLabels[lunar] == "Capricorn" :
          influence.append(randomGrabber(capricornPositive))
          influence.append(randomGrabber(capricornNegative))
        elif lunarLabels[lunar] == "Aquarius" :
          influence.append(randomGrabber(aquariusPositive))
          influence.append(randomGrabber(aquariusNegative))
        elif lunarLabels[lunar] == "Pisces" :
          influence.append(randomGrabber(piscesPositive))
          influence.append(randomGrabber(piscesNegative))

    for solar in range(len(solarSigns)-1):
      temp = solarSigns[solar]
      tempVal = temp.get()
      if tempVal == 1:
        # print(f"{solarLabels[solar]}")
        file.write(f"## Solar Sign: {solarLabels[solar]}\n{solarInfluences[solar]}\n\n")
        if solarLabels[solar] == "Aries" :
          influence.append(randomGrabber(ariesPositive))
          influence.append(randomGrabber(ariesNegative))
        elif solarLabels[solar] == "Taurus" :
          influence.append(randomGrabber(taurusPositive))
          influence.append(randomGrabber(taurusNegative))
        elif solarLabels[solar] == "Gemini" :
          influence.append(randomGrabber(geminiPositive))
          influence.append(randomGrabber(geminiNegative))
        elif solarLabels[solar] == "Cancer" :
          influence.append(randomGrabber(cancerPositive))
          influence.append(randomGrabber(cancerNegative))
        elif solarLabels[solar] == "Leo" :
          influence.append(randomGrabber(leoPositive))
          influence.append(randomGrabber(leoNegative))
        elif solarLabels[solar] == "Virgo" :
          influence.append(randomGrabber(virgoPositive))
          influence.append(randomGrabber(virgoNegative))
        elif solarLabels[solar] == "Libra" :
          influence.append(randomGrabber(libraPositive))
          influence.append(randomGrabber(libraNegative))
        elif solarLabels[solar] == "Scorpio" :
          influence.append(randomGrabber(scorpioPositive))
          influence.append(randomGrabber(scorpioNegative))
        elif solarLabels[solar] == "Sagittarius" :
          influence.append(randomGrabber(sagittariusPositive))
          influence.append(randomGrabber(sagittariusNegative))
        elif solarLabels[solar] == "Capricorn" :
          influence.append(randomGrabber(capricornPositive))
          influence.append(randomGrabber(capricornNegative))
        elif solarLabels[solar] == "Aquarius" :
          influence.append(randomGrabber(aquariusPositive))
          influence.append(randomGrabber(aquariusNegative))
        elif solarLabels[solar] == "Pisces" :
          influence.append(randomGrabber(piscesPositive))
          influence.append(randomGrabber(piscesNegative))

    file.write(f"## Boons & Banes\n")
    for quality in influence:
      # print(quality)
      temp = quality
      for item in temp:
        file.write(f"- {item}\n")
        # print(item)


def selectOutput():
    outputFolder = filedialog.askdirectory()
    # if outputFolder:
    #     # print(outputFolder)
    return(outputFolder)

def run():
  lunarDays.append(lunarDayCheckBoxes())
  dates.append(dateCheckBox())
  planets.append(planetCheckBoxes())
  lunarSigns.append(lunarSignCheckboxes())
  solarSigns.append(solarSignCheckboxes())
  submit_btn = tk.Button(btm_frame2, text="Submit")

    # Create a button
  output = tk.Button(btm_frame2, text="Select Output Folder", command=selectOutput)

  toc = tk.Button(btm_frame2, text="Print TOC", command=tableOfContents)


  # layout the widgets in the bottom frame
  submit_btn.grid(row=0, column=1)
  output.grid(row=0, column=2)
  toc.grid(row=0, column=3)

  # adds to file on submit
  submit_btn.config(command=log)
  
  window.mainloop()

run()