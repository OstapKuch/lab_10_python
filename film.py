class Film:

    budget = 500000

    def __init__(self,
                 name = "Taxi",
                 duration = 88,
                 reviewsRate = 7.0,
                 counrty = "France",
                 year = 1998,
                 director = "Jerar Pires"):
        self.name = name
        self.duration = duration
        self.reviewRate = reviewsRate
        self.country = counrty
        self.year = year
        self.director = director

    def __del__(self):
        print("Destructor called, film " + self.name + " deleted")


    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def returnBudget():
        return Film.budget

