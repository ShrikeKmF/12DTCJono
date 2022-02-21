buildingType = "C"
while buildingType != "X" or buildingType != "x":
    buildingType = input("What type of building is it | Residential or "
                         "Commercial \n")
    if buildingType != "X" and buildingType != "x":
        buildingLength = int(
            input('What is the length of the building in Metres '
                  '\n'))
        buildingWidth = int(
            input("What is the width of the building in Metres "
                  "\n"))
        if buildingType != "Residential":
            buildingDepth = 50
        else:
            buildingDepth = 25
        volume = buildingLength * buildingDepth * buildingWidth
        print(
            'The volume of concrete needed for a slab with a length of {} and '
            'width of {} and a depth of {} is {} cubic metres \n'.format(
                buildingLength, buildingWidth, buildingDepth, volume))
    else:
        break
