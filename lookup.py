import json
import requests

osrsSkillDict = {   "total":0,
                "attack":1,
                "defence":2,
                "hitpoints":4,
                "prayer":6,
                "magic":7,
                "woodcutting":9,
                "fletching":10,
                "firemaking":12,
                "crafting":13,
                "mining":15,
                "herblore":16,
                "agility":17,
                "thieving":18,
                "slayer":19,
                "farming":20,
                "runecrafting":21,
                "hunter":22,
                "construction":23,
             }
rs3SkillDict = {
                "total":0,
                "attack":1,
                "defense":2,
                "strength":3,
                "constitution":4,
                "ranged":5,
                "prayer":6,
                "magic":7,
                "cooking":8,
                "woodcutting":9,
                "fletching":10,
                "fishing":11,
                "firemaking":12,
                "crafting":13,
                "smithing":14,
                "mining":15,
                "herblore":16,
                "agility":17,
                "thieving":18,
                "slayer":19,
                "farming":20,
                "runecrafting":21,
                "hunter":22,
                "construction":23,
                "summoning":24,
                "dungeoneering":25,
                "divination":26,
                "invention":27
}
xpArr = [0, 83, 174, 276, 388, 512, 650, 801, 969, 1154,
         1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470,
         5018, 5624, 6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363,
         14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224,
         41171, 45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333,
         111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742,
         302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627,
         814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808, 1986068,
         2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 4385776, 4842295, 5346332,
         5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431
         ]

URL = "https://secure.runescape.com/m=hiscore"

print("Stat Checker, enter \'exit\' on any prompt (except rsn) to quit.")

#HiScore query format: Rank,Level,XP Rank,Level,XP
while 0 == 0:
    game = input("RS3 or OSRS?: ")
    game = game.lower()
    if game == 'osrs':
        URL = URL + '_oldschool/index_lite.wd?player='
        break
    elif game == 'rs3':
        URL = URL + '/index_lite.ws?player='
        break
    elif game == 'exit':
        print("Closing by user request")
        exit(2)
    else:
        print("Please type in either RS3 or OSRS!")

while 0 == 0:
    rsn = input("Please enter your rsn: ")
    rsn = rsn.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    rsnLen = len(rsn)
    if 1 <= rsnLen <= 12 and rsn[0] != ' ' and rsn[-1] != ' ':
        break
    else:
        print("Not a valid RSN, try again!")

for letter in rsn:
    if letter == ' ':
        URL = URL + '%20'
    else:
        URL = URL + letter

query = requests.get(url=URL)
if query.status_code != 200:
    print("Status code not OK, had code", query.status_code)
    exit(-1)
x = query.text
queryList = x.split('\n')

while 0 == 0:
    while 0 == 0:
        skill = input("What skill would you like the level of?: ")
        skillIndex = -1
        skill = skill.lower()
        if game == 'osrs':
            if skill in osrsSkillDict:
                skillIndex = osrsSkillDict[skill]
                break
            else:
                print("Not a valid skill, please enter a valid skill")
        elif game == 'rs3':
            if skill in rs3SkillDict:
                skillIndex = rs3SkillDict[skill]
                break
            else:
                print("Not a valid skill, please enter a valid skill")

    queryResult = queryList[skillIndex].split(',')
    xpToNext = xpArr[int(queryResult[1])] - int(queryResult[2])

    print(rsn + "'s", skill, "level: " + queryResult[1])
    print(rsn + "'s", skill, "XP: " + queryResult[2])
    print("XP to next level:", xpToNext)