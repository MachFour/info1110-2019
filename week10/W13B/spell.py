class Spell:
    
    def validate_args(self,name,school,level,cast_limit,effect):
        if not isinstance(name, str):
            raise ValueError("name is not of type str")
        if not isinstance(school, str):
            raise ValueError("school is not of type str")
        if not isinstance(effect, str):
            raise ValueError("effect is not of type str")
        if not isinstance(level, int) and not (0 <= level <= 9):
            raise ValueError("level is not of type int between 0 and 9")
        if not isinstance(cast_limit, int) and not cast_limit > 0:
            raise ValueError("cast_limit is not a non-zero positive integer")

    def __init__(self,name,school,level,cast_limit,effect):
        
        self.validate_args(name,school,level,cast_limit,effect)
        
        self.name = name
        self.school = school
        self.level = level
        self.cast_limit = cast_limit
        self.effect = effect
        self.__casts = cast_limit

    def __repr__(self):
        return "Spell Name: {}, school: {}, level: {}, cast_limit: {}, casts: {}".format(self.name, self.school, self.level, self.cast_limit,self.__casts)

    def cast(self):
        if self.__casts > 0:
            # This means the spell CAN be cast
            self.__casts -= 1
            print("Casting '{}'...".format(self.name))
            print("You can cast '{}' {} more time(s) today.".format(self.name, self.__casts))
        else:
            # If you can't cast it
            print("Can't cast '{}' any more today.".format(self.name))

    def recharge(self):
        self.__casts = self.cast_limit

    def get_casts(self):
        return self.__casts
    
    def set_casts(self, casts): 
        self.__casts = casts

