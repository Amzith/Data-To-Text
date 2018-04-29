import csv
import random


# reorder sentences --------------
def sentenceimportance(a):
    if "average" in a:
        return 1
    else:
        return -1


health =[]
econactivity = []
density =[]
disability=[]


# Health ---------------
with open('health.csv') as csvfile:
    linereader = csv.reader(csvfile)
    for row in linereader:
        health.append(row)
city_information = {}  # [Population, Amount of Very Healthy people, Unhealthy people, 16 - 74 Population, Working Population, Population Density]
for city in health:
    name = city[0]
    population = city[1]
    VgoodH = city[2]
    VgoodH += city[3] # very good or good health
    VbadH = city[6]
    city_information[name] = []
    city_information[name].append(population)
    city_information[name].append(VgoodH)
    city_information[name].append(VbadH)
# -----------------------------------

# Economic Activity -----------------
with open('economicactivitydata.csv') as csvfile:
    linereader = csv.reader(csvfile)
    for row in linereader:
        econactivity.append(row)
for city in econactivity:
    name = city[0]
    workingpop = city[1]
    active = city[2]
    try:
        city_information[name].append(workingpop)
        city_information[name].append(active)
    except:
        print("error, data is not coherent, " + name + " is not in all data files")

# ---------------------------------------------------


# Density -----------------
with open('populationdensity.csv') as csvfile:
    linereader = csv.reader(csvfile)
    for row in linereader:
        density.append(row)

average=[]
for denav in density:
    average.append(denav[3])
average = list(map(float, average))
average = (sum(average)/len(average))
for city in density:
    name = city[0]
    population = city[1].split(',')
    area = city[2].split(',')
    density = city[3]
    try:
        city_information[name].append(density)
    except:
        print("error, data is not coherent, " + name + " is not in all data files")
# --------------------------------------

scotemployed = city_information["Scotland"][4].replace(',', '')
scotworkinage = city_information["Scotland"][3].replace(',', '')
scotbhealth = city_information["Scotland"][2].replace(',', '')
scotghealth = city_information["Scotland"][1].replace(',', '')
scotpop = city_information["Scotland"][0].replace(',','')
percenavwork = (float(scotemployed)/float(scotworkinage))*100
avscotbhealth = (float(scotbhealth)/float(scotpop))*100
avscotghealth = (float(scotghealth)/float(scotpop))*100

# cities now have their data assigned, time to interpret the data ----------
for cityname, numbers in city_information.items():
    sentences = []

    #assign variables to the values ------
    pop = numbers[0].replace(',', '')
    health = numbers[1].replace(',', '')
    bhealth = numbers[2].replace(',', '')
    workinage = numbers[3].replace(',', '')
    employed = numbers[4].replace(',', '')
    popdens = numbers[5].replace(',', '')
    percenhealth = (float(health)/float(pop))*100
    percenbhealth = (float(bhealth)/float(pop))*100
    percenwork = (float(employed)/float(workinage))*100


    #sortingdensity -----------
    sentences.append(cityname)
    if float(popdens) > (average + 2):
        dens = [("a high population density of " + popdens + " per km2"),
                ("a population density of " + popdens + " per km2"),
                ("a high amount of people per km2, " + popdens),
                ("a high population density")
                ]
        sentences.append(random.choice(dens))
    elif float(popdens) < (average - 2):
        dens = [( "a low population density of " + popdens  + " per km2"),
                ("a below average population density of " + popdens + " per km2"),
                ("a population density of " + popdens + " per km2"),
                ("a low population density")]
        sentences.append(random.choice(dens))
    else:
        dens = [( "an average population density of " + popdens  + " per km2"),
                ("a population density of " + popdens + " per km2, which is average,"),
                ("an average population density")]
        sentences.append(random.choice(dens))

        # employment sentence ---------------
    if percenwork > (percenavwork + 2):
        employy = [(
            "a high employment rate of " + str(round(percenwork, 1)) + "% of the population economically active"),
            ("a high employment rate of " + str(round(percenwork, 1)) + "%"), (str(round(percenwork, 1))
            + "% of the population economically active, which is higher than the average"),
            ("a high employment rate"), ("a very low number of unemployed"), ("a high amount of employed people"), ("a low unemployment, where " + str(round(percenwork,1)) + "% of people work")]
        sentences.append(random.choice(employy))
    elif percenwork < (percenavwork - 2):
        employy = [(
            "a low employment rate of " + str(round(percenwork, 1)) + "% of the population economically active"),
            ("a low employment rate of " + str(round(percenwork, 1)) + "%, compared to the average of " + str(round(percenavwork))
             + "%"), (str(round(percenwork, 1)) + "% of the population economically active"),
            ("a low employment rate"), ("a high amount of unemployed"), ("a poor amount of employed people"),
            ("Only " + str(round(percenwork, 1)) + "% of people are even employed")]

        sentences.append(random.choice(employy))
    else:
        employy = [(
            "an average employment rate of " + str(round(percenwork, 1)) + "% of the population economically active"),
            (str(round(percenwork, 1)) + "% of the population economically active, which remains average"),
            ("with the employment rates falling under average"), ("with an average employment rate"),
            ("with " + str(round(percenwork, 1)) + "% of people working"), ("an average number people employed"),
            ("a normal percentage of people working (" + str(round(percenwork, 1)) + "%)"), ("7 out of 10 people employed"), ("a average employmenet rate, which is roughly 7 out of 10 people employed")]
        sentences.append(random.choice(employy))


    #assign a sentence for health ----------
    if percenhealth > (avscotghealth + 2):
        if percenbhealth > (avscotbhealth + 2):
            hhhealth = [("a high amount of very healthy people of " + str(round(percenhealth,1))
                         + "%, despite also having a high rate of poor health of " + str(round(percenbhealth,1))),
                        ("many people with very bad health of " + str(round(percenbhealth,1))
                         + "%, in contrast to the high rate of very healthy people")]
            sentences.append(random.choice(hhhealth))
        elif percenbhealth < (avscotbhealth - 2):
            hhhealth = [("a high amount of very healthy people of " + str(
                round(percenhealth, 1)) + "%, with only " + str(
                round(percenbhealth, 1)) + "% of people having poor health"), ("many people with very good health of " + str(
                round(percenhealth, 1)) + "%, in addition to the low rate of bad health"), ("over half of the population are very healthy, where there are not many people of poor health ")]
            sentences.append(random.choice(hhhealth))
        else:
            hhhealth = [("a high amount of very healthy people of " + str(
                round(percenhealth, 1)) + "%, with an average poor health rate of " + str(
                round(percenbhealth, 1))), ("a very high quality of life with " + str(
                round(percenhealth, 1)) + "% of people have very good health and an only average poor health rate")]
            sentences.append(random.choice(hhhealth))

    elif percenhealth < (avscotghealth - 2):
        if percenbhealth > (avscotbhealth + 2):
            hhhealth = [("a low amount of very healthy people of " + str(
                round(percenhealth, 1)) + "%, demonstrated by the high rate of poor health of " + str(
                round(percenbhealth, 1)) + "%"), ("a poor rate of healthy people where only " + str(
                round(percenhealth, 1)) + "% of people are of good health, and " +  str(
                round(percenbhealth, 1)) + "% have bad health")]
            sentences.append(random.choice(hhhealth))
        elif percenbhealth < (avscotbhealth - 2):
            hhhealth = [("a low amount of very healthy people of " + str(
                round(percenhealth, 1)) + "% despite the low poor health rate of " + str(
                round(percenbhealth, 1)) + "%"), ("a poor rate of healthy people where only " + str(
                round(percenhealth, 1)) + "% of people are of good health, in contrast to only " + str(
                round(percenbhealth, 1)) + "% of people having bad health")]
            sentences.append(random.choice(hhhealth))
        else:
            hhhealth = [("a low amount of very healthy people of " + str(
                round(percenhealth, 1)) + "% and an average poor health rate of " + str(
                round(percenbhealth, 1)) + "%"), ("a poor rate of healthy people where only " + str(
                round(percenhealth, 1)) + "% of people are of good health, alongside the average bad health rate of " + str(
                round(percenbhealth, 1)) + "%")]
            sentences.append(random.choice(hhhealth))
    else:
        hhhealth = [("an average health rate, where " + str(
            round(percenhealth, 1)) + "% of people are very healthy and " + str(
            round(percenbhealth, 1)) + "% of people have very bad health"), ("a average rate of healthy people where " + str(
            round(percenhealth, 1)) + "% of people are of good health, alongside " + str(
            round(percenbhealth, 1)) + "% of people having bad health")]
        sentences.append(random.choice(hhhealth))



    #sentencestart ---------------
    sentences = sentences[1:]
    sentencestart = [(cityname + " has " + sentences[0] ), ("In " + cityname + " there is " + sentences[0]), ("In " + cityname + " it has " + sentences[0]), ("There is " + sentences[0] + " in " + cityname + " ") ]
    sentenceconnect = [(" and has " + sentences[1]), (" along with having " + sentences[1]), (" as well as " + sentences[1]), (" whilst also having " + sentences[1])]
    sentenceend = [(". " + cityname + " has " + sentences[2]), (". The area has " + sentences[2]),
                       (". There is " + sentences[2]), (". In terms of health it has " + sentences[2])]

    #sentences.sort(key = sentenceimportance)
    sentences[0] = random.choice(sentencestart)
    sentences[1] = random.choice(sentenceconnect)
    sentences[2] = random.choice(sentenceend)

    #list the paragraphs ------------------
    print(''.join(sentences))
    #Display in text file --------------
    file = open("text.txt","a")
    file.write(str(''.join(sentences))+ "\n" + "\n")
file.close()



