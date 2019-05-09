from spell import Spell

class SpellBook:
    
    @staticmethod
    def validate_args(material, capacity, spells):

        if not isinstance(material, str):
            raise ValueError("material is not of type str")

        if not isinstance(capacity, int) or not capacity > 0:
            raise ValueError("capacity is not a positive integer")

        if not isinstance(spells, list):
            raise ValueError("spells is not of type list") 
        else:
            for spell in spells:
                if not instance(spell, Spell):
                    raise ValueError("list contianed non-Spell objects")


    def __init__(self, material, capacity, spells = []):
        """
        Constructor method for SpellBook.
        
        :param material: The material the book is made out of.
        :param capacity: The maximam capacity of the SpellBook.
        :param spells: A list of spells to be contained within the SpellBook.
    
        """
        Spell.validate_args(material, capacity, spells)

        self.material = material
        self.capacity = capacity

        self.spells = spells

    def add_spell(self, spell):
        if not isinstance(spell, Spell):
            raise ValueError("spell is not of type Spell")
        
        if <condition>: # TODO
            self.spells.append(spell)

    def cast_spell(self, name):
        # TODO
        pass

    def cast_strongest(self):
        # TODO
        pass

    def cast_all(self):
        # TODO
        pass
    
    def recharge_all(self):
        # TODO
        pass


