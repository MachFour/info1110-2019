
class Spell:
    @staticmethod
    def validate(name, school, level, cast_limit, effect):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(school, str):
            raise ValueError("school must be a string")
        if not isinstance(level, int) or not 0 <= level <= 9:
            raise ValueError("level must be an integer between 0 and 9")
        if not isinstance(cast_limit, int) or not cast_limit > 0:
            raise ValueError("cast_limit must be a positive integer")
        if not isinstance(effect, str):
            raise ValueError("effect must be a string")

    def __init__(self, name, school, level, cast_limit, effect):
        Spell.validate(name, school, level, cast_limit, effect)
        # now we know that all of the arguments are 'correct'
        self.name = name
        self.school = school
        self.level = level
        self.cast_limit = cast_limit
        self.effect = effect
        self.casts = cast_limit

    def get_name(self):
        return self.name
    def get_school(self):
        return self.school
    def get_level(self):
        return self.level
    def get_cast_limit(self):
        return self.cast_limit
    def get_effect(self):
        return self.effect
    def get_casts(self):
        return self.casts

    def __repr__(self):
        return "Spell '{}' of school {}. Level: {:d}, cast limit: {:d}, " \
                "remaining casts: {:d}".format(self.name, self.school,
                        self.level, self.cast_limit, self.casts)

    def cast(self):
        if self.casts > 0:
            # can cast the spell
            self.casts -= 1
            print("Casting '{}'...".format(self.name))
            print(self.effect)
            print()
            print("You can cast '{}' {:d} more time(s) today.".format(self.name,
                self.casts))
        else:
            print("Can't cast '{}' any more today.".format(self.name))

    def recharge(self):
        # resets remaining casts to the maximum limit
        self.casts = self.cast_limit


