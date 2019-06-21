import csv
import pandas as pd
import numpy as eigenvector


playerDict = {}
Allplayers = []
winnerList = []
loserList = []

with open('UTRTennisData.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        numGamePlayed = 0
        matchwin = 0
        print(row)
        # print(row["resultid"])
        # print(row["resultdate"])
        # print(row["winner1id"])
        # print(row["loser1id"])
        # print(row["winnerset1"])
        # print(row["winnerset2"])
        # print(row["winnerset3"])
        # print(row["winnerset4"])
        # print(row["winnerset5"])
        # print(row["loserset1"])
        # print(row["loserset2"])
        # print(row["loserset3"])
        # print(row["loserset4"])
        # print(row["loserset5"])
        line_count = line_count+1
        print("linecount: " + str(line_count))
        # print(int(row["winnerset1"]) - int(row["loserset1"]))
        # print(int(row["winnerset2"]) - int(row["loserset2"]))
        # print(int(row["winnerset3"]) - int(row["loserset3"]))
        # print(int(row["winnerset4"]) - int(row["loserset4"]))
        # print(int(row["winnerset5"]) - int(row["loserset5"]))

        listGames = []

        #Counts the difference of points in a full game
        score1 = (int(row["winnerset1"]) - int(row["loserset1"]))
        score2 =(int(row["winnerset2"]) - int(row["loserset2"]))
        score3 =(int(row["winnerset3"]) - int(row["loserset3"]))
        score4 =(int(row["winnerset4"]) - int(row["loserset4"]))
        score5 =(int(row["winnerset5"]) - int(row["loserset5"]))

        if score1 != 0:
            numGamePlayed = numGamePlayed +1
        if score2 != 0:
            numGamePlayed = numGamePlayed +1
        if score3 != 0:
            numGamePlayed = numGamePlayed +1
        if score4 != 0:
            numGamePlayed = numGamePlayed +1
        if score5 != 0:
            numGamePlayed = numGamePlayed +1

        if score1 >= 1:
            matchwin = matchwin +1
        if score2 >= 1:
            matchwin = matchwin +1
        if score3 >= 1:
            matchwin = matchwin +1
        if score4 >= 1:
            matchwin = matchwin +1
        if score5 >= 1:
            matchwin = matchwin +1

        ## Puts the total score generated in an n by n matrix
        # Suppose player B wins against player C
        # winner score will be cell[B][C] and loser score will be cell[C][B]

        winnerTotalScore = (int(row["winnerset1"]) + int(row["winnerset2"]) + int(row["winnerset3"])
                            + int(row["winnerset4"]) + int(row["winnerset5"])) / numGamePlayed

        loserTotalScore = (int(row["loserset1"]) + int(row["loserset2"]) + int(row["loserset3"]) + int(row["loserset4"])
                           + int(row["loserset5"])) / numGamePlayed


        ## Bonus points if winner won convincingly
        if(score1 != 0):
            if(score1>2):
                winnerTotalScore = winnerTotalScore+2
        if (score2 != 0):
            if (score2 > 2):
                winnerTotalScore = winnerTotalScore + 2
        if (score3 != 0):
            if (score3 > 2):
                winnerTotalScore = winnerTotalScore + 2
        if (score4 != 0):
            if (score4 > 2):
                winnerTotalScore = winnerTotalScore + 2
        if (score5 != 0):
            if (score5 > 2):
                winnerTotalScore = winnerTotalScore + 2



        # Generates list all unique players
        if row["winner1id"] not in Allplayers:
            Allplayers.append(row["winner1id"])
        if row["loser1id"] not in Allplayers:
            Allplayers.append(row["loser1id"])


    # ####---- TESTING Who won and never lost?
    ## Bad algorithm because players who never lost won against bad players
    #     if row["winner1id"] not in winnerList:
    #         # Allplayers.append(row["winner1id"])
    #         winnerList.append(row["winner1id"])
    #         print(len(winnerList))
    #
    #     if row["loser1id"] not in loserList:
    #         # Allplayers.append(row["loser1id"])
    #         loserList.append(row["loser1id"])
    #
    #
    # for x in loserList:
    #     if x in winnerList:
    #         winnerList.remove(x)
    #
    # print(winnerList)
    # print(len(winnerList))


        if winnerTotalScore > 0:
            key = str(row["winner1id"] + "-" + row["loser1id"])
            if key not in playerDict:
                dataList = []
                dataList.append(winnerTotalScore)
                playerDict[key] = dataList
            else:
                # print(row["winner1id"]+"-"+row["loser1id"])
                print("curr TAlly" + str(playerDict[key]))
                dataList = playerDict[key]
                dataList.append(winnerTotalScore)
                playerDict[key] = dataList

        if loserTotalScore > 0:
            key = str(row["loser1id"] + "-" + row["winner1id"])
            if key not in playerDict:
                dataList = []
                dataList.append(loserTotalScore)
                playerDict[key] = dataList
            else:
                dataList = playerDict[key]
                dataList.append(loserTotalScore)
                playerDict[key] = dataList




#     #-First attempt : output FirstSolution.csv
#         if(score1 != 0):
#             listGames.append(score1)
#         if (score2 != 0):
#             listGames.append(score2)
#         if (score3 != 0):
#             listGames.append(score3)
#         if (score4 != 0):
#             listGames.append(score4)
#         if (score5 != 0):
#             listGames.append(score5)
#
#         posTally = 0
#         negTally = 0
#         # key = ""
#         for x in listGames:
#             key = ""
#             print("# games played " + str(len(listGames)))
#             print("curr score " + str(x))
#             if x >= 1:
#                 key = str(row["winner1id"]+"-"+row["loser1id"])
#                 posTally = x
#                 print(key)
#                 print("pos Tally" + str(posTally))
#
#                 if key not in playerDict:
#                     posList = []
#                     posList.append(posTally)
#                     playerDict[key] = posList
#                 else:
#                     # print(row["winner1id"]+"-"+row["loser1id"])
#                     print("PLAYED AGAIN")
#                     # print("curr TAlly" + str(playerDict[key]))
#                     newposList = playerDict[key]
#                     newposList.append(posTally)
#                     playerDict[key] = newposList
#                     print("APPENDING " + str(posTally))
#                     print("final pos TAlly" + str(playerDict[key]))
#
#             if x < 0:
#                 key = str(row["loser1id"]+"-"+row["winner1id"])
#                 negTally = x
#                 print(key)
#                 print("neg Tally" + str(negTally))
#
#                 if key not in playerDict:
#                     negList = []
#                     negList.append(negTally)
#                     playerDict[key] = negList
#                 else:
#                     # print(row["winner1id"]+"-"+row["loser1id"])
#                     # print("curr TAlly" + str(playerDict[key]))
#                     newnegList = playerDict[key]
#                     newnegList.append(negTally)
#                     playerDict[key] = newnegList
#                     print("APPENDING " + str(negTally))
#                     print("final neg TAlly" + str(playerDict[key]))
#
# # --END ALGORITHM


    ## for debuggine / testing
    # print("Printing Dictionary of points")
    # print(playerDict)
    # print("number players " + str(len(Allplayers)))
    # print(len(playerDict))
    # ## Print Keys
    # for key in playerDict:
    #     print(key)



    ## Store values in a data frame
    df = pd.DataFrame(index=Allplayers, columns=Allplayers)

    # print(df)

    for x in playerDict:
        players = x.split("-")
        # print(players[0])
        # print(players[1])
        # print(playerDict[x][0])
        average = 0
        for scores in playerDict[x]:
            average = scores + average

            # print("length " + str(len()))
        # average = average/len(playerDict[x])

        df = df.set_value(str(players[0]), str(players[1]), average)

    ## initialize arbitrary eigenvector
    eigenvector = eigenvector.ones([len(Allplayers),1])
    df = df.fillna(0)
    result = df.dot(eigenvector)
    print(result)

    #solve for dominant eigen vector
    print(result/result.max())

    # Solve for dominant eigen vector

    for x in range(0,500):
        result = df.dot(result)
        result = result/result.max()


    df.to_csv("matrix.csv")
    result.to_csv("rank.csv")


