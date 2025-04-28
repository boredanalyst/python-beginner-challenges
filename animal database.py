## multiple dictionaries nested in a list.

bumblebee = {
    "scientific name" : "Bombus lapidarius",
    "common name" : "red bumblebee",
    "genus" : "bombus"
}

moth = {
    "scientific name" : "Attacus atlas",
    "common name" : "Atlas moth",
    "genus" : "Attacus"
}

butterfly = {
    "scientific name" : "Danaus plexippus",
    "common name" : "Monarch butterfly",
    "genus" : "Danaus"
}

insects = [bumblebee, moth, butterfly]

for insect in insects:
    for details in insect.keys():
        print(f'{details.upper()} : {insect[details]}')
    print("## ------- ## \n")    
