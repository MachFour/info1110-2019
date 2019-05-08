from spell import Spell 

class SpellBook:
    
    def validate_args(self, material, capacity):
        # TODO
        pass

    def __init__(self, material, capacity, spells=[]):
        """
        Creates a new instance of a SpellBook

        :param material: The material that the book is made of
        :param capacity: A numeric value that represents how many levels of spells it can have recorded inside
        :param spells: List of Spell objects. Default: []
        """

        self.material = material
        self.capacity = capacity
        self.spells = spells

    def add_spell(self, spell):
        if not isinstance(spell, Spell):
            raise ValueError("spell is not of type object Spell")
        if <condition>: # TODO
            self.spells.append(spell)
        else:
            # TODO
            pass

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

    

