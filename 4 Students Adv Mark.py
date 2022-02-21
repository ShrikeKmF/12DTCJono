name = ""
bestMark = 0
BestName = ""
divider = 0
mark_total = 0


while name != "X":
    mark = -1
    name = input("What is the Students Name")
    while mark > 100 and name != "X" or mark < 0 and name != "X":
        mark = int(input("Students Mark "))
    if name == "X":
        mark = 0
    divider += 1
    mark_total += mark

    if mark > bestMark:
        bestMark = mark
        BestName = name

print("Average {}\n"
      "\nBest Student {}\n"
      "Mark {}\n"
      .format(mark_total/divider, BestName, bestMark))
