
class Spellbook:
    @staticmethod
    def validate(material, capacity, spells):
        # TODO make sure material is a string and capacity is an int
        pass
        if not isinstance(spells, list):
            raise ValueError("spells must be a list of spells")

    def __init__(self, material, capacity, spells=[]):
        Spellbook.validate(material, capacity, spells)
        self.material = material
        self.capacity = capacity
        self.spells = spells

    def __repr__(self):
        #TODO
        pass

    def add_spell(self, spell):
        if not isinstance(spell, Spell):
            raise ValueError("spell must be an instance of the Spell class")
        if ## capacity requirement is met:
            self.spells.append(spell)


