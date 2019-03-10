from film import Film

taxi = Film()

blackPanther = Film(name = "Black Panther",
               duration=134,
               reviewsRate=7.3,
               year=2018)

aquaman = Film(name = "Aquaman",
               duration=144,
               reviewsRate=7.5,
               counrty="USA",
               year=2018,
               director="James Van")

print(taxi)
print(aquaman)
print(blackPanther)
print(Film.returnBudget())
