class Spell: 

    @staticmethod
    def validate_args(name, school, level, cast_limit, effect):
        if not isinstance(name, str):
            raise ValueError("name is not of type str")

        if not isinstance(school, str):
            raise ValueError("school is not of type str")
        
        if not isinstance(effect, str):
            raise ValueError("effect is not of type str")

        if not isinstance(level, int) or not (0 <= level <= 9):
            raise ValueError("level is not an integer between 0 and 9")
        if not isinstance(cast_limit, int) or not cast_limit > 0:
            raise ValueError("cast_limit is not a positive integer")


    def __init__(self, name, school, level, cast_limit, effect):
        
        self.validate_args(name, school, level, cast_limit, effect) 

        self.name = name
        self.school = school
        self.level = level
        self.cast_limit = cast_limit
        self.effect = effect
        self.__casts = cast_limit

    def __repr__(self):
        """
        Returns a string to be outputted to console
        """
        return "Spell name: {}, school: {}, level: {}, cast_limit: {}, effect: {}, casts: {}".format(self.name, self.school, self.level, self.cast_limit, self.effect, self.__casts)

    def cast(self):
        if self.__casts > 0:
            # This means we CAN cast it
            self.__casts -= 1
            print("Casting '{}'...".format(self.name))
            print(self.effect)
            print("You can cast '{}' {} more time(s) today.".format(self.name, self.__casts))
        else:
            # We can't
            print("Can't cast '{}' any more today.".format(self.name))


    def recharge(self):
        self.__casts = self.cast_limit


    def get_casts(self):
        """
        Getter Function: Returns self.__casts
        Read Access Only
        """
        return self.__casts

    def set_casts(self, casts):
        """
        :param casts: Number of casts
        Setter Function: Sets self.__casts to param:casts
        Write Access Only
        """
        self.__casts = casts
