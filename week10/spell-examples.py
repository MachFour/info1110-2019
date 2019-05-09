from spell import Spell
# from <file> import <Class>

cat_summoned = "You reach into your pocket for a can of tuna and " \
        "crack it open.  A cat pops into existence beside you in a puff of smoke!"

summon = Spell("Summon Cat", "Conjuration", 1, 4, cat_summoned)
# The spell "Summon Cat" belongs to the school of "Conjuration",
# has a level of 1 and can be cast 4 times per day.

cat_effects = "You throw a bag of catnip at a nearby, unfortunate soul, " \
        "and a giant cat comes crashing down on them from the heavens above!"

cataclysm = Spell("Cataclysm", "Conjuration", 6, 2, cat_effects)
# The spell "Cataclysm" belongs to the school of "Conjuration",
# has a level of 6 and can be cast 2 times per day.

# use the spells
summon.cast()
cataclysm.cast()
