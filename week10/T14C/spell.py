
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
