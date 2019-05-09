
class Spellbook:
    # store the error message as a class variable
    capacity_error = "We're nearing the end of our power budget. " \
                    "You can't write '{}' into this spellbook."

    @staticmethod
    def validate(material, capacity, spells):
        if not isinstanceof(material, str):
            raise ValueError("material must be a string")
        if not isinstance(capacity, int) or not capacity > 0
            raise ValueError("capacity must be a positve integer")

    def __init__(self, material, capacity, spells):
        Spellbook.validate(material, capacity)
        self.material = material
        self.capacity = capacity
        self.spells = []
        # we can call an instance method in the constructor too
        for spell in spells:
            self.add_spell(spell)

    def __repr__(self):
        s = "{:s} spellbook, capacity {:d}, {:d} spells with total level {:d}"
        return s.format(self.material, self.capacity, len(spells),
                self.get_total_level())

    # These two are also 'getter' methods, but we don't need corresponding
    # instance variables (attributes), because the answer can just be
    # calculated from other instance variables
    def get_total_level(self):
        total_level = 0
        # let's use a while loop for the practice
        i = 0
        while i < len(self.spells):
            # use the getter method of the Spell class to find the level
            total_level += spells[i].get_level()
            i += 1
        return total_level

    def get_remaining_capacity(self):
        # using get_total_level() makes this instance method very easy
        return self.capacity - self.get_total_level()

    # From the lab sheet

    def add_spell(self, spell):
        if not isinstance(spell, Spell):
            raise ValueError("spell must be an instance of the Spell class")
        # check whether there is enough capacity left to store
        # this new spell (based on its level)
        if self.get_remaining_capacity() >= spell.get_level():
            self.spells.append(spell)
        else:
            # error message (format string) is stored as a class variable
            # and then formatted as needed
            raise ValueError(Spellbook.capacity_error.format(spell.get_name()))

    def cast_spell(self, name):
        # this will be set to the spell in this spellbook matching 'name'
        # if there is such a spell
        spell = None
        for s in self.spells:
            if s.get_name() == name:
                spell = s
                break # don't need to keep looking

        if spell is not None:
            spell.cast()
        else:
            print("There is no spell called '{}' here".format(name))

    def cast_strongest(self):
        # What should happen if the spellbook contains no spells?
        # The spec doesn't say, so we will just print a message
        if len(self.spells) == 0:
            print("There are no spells in this spellbook!")
             # may as well end the function, so we don't need to use 'else'
            return

        # to begin, assume the first spell is the strongest
        strongest_spell = self.spells[0]
        # then look through the rest to see if there's a stronger one
        i = 1
        while i < len(self.spells):
            next_spell = self.spells[i]
            if next_spell.get_level() > strongest_spell.get_level():
                strongest_spell = next_spell
            i += 1
        # now cast it!
        strongest_spell.cast()


    # these two methods are very easy with for loops!
    # (and not much harder with while loops)
    def cast_all(self):
        spells_cast = 0
        for spell in self.spells:
            if spell.get_casts() > 0:
                spell.cast()
                spells_cast += 1
            # otherwise skip

        print("Cast {:d} spells!".format(spells_cast))

    def recharge_all(self):
        for spell in self.spells:
            spell.recharge()




