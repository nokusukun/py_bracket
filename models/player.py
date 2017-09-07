import secrets

class Player():

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        self.id = secrets.token_hex(5)
        self.age = None
        self.sex = "m"
        self.dob = None
        self.coach = None
        self.gym = None
        self.weight = None
        self.height = None
        self.first_time = True
        self.seasoned = False
        self.skill_type = "novice"
        self.skill_rating = 0
        self.stamina = 0
        self.speed = 0
        self.power = 0
        self.achievement = None
        self.belt = None
        self.school_level = None
        self.category = None
        self.lost = False


    @property
    def combat_level(self):
        return ((int(self.skill_rating) + int(self.stamina) + int(self.speed) + int(self.power))/4) * 10


    def __str__(self):
        return f"<{self.last_name}_{self.first_name} {self.id}>"