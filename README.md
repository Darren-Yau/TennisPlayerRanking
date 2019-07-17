# TennisPlayerRanking
Ranking Tennis Players

Completed a coding assignment that got me an interview round with UTRTennis


Created a script to rank tennis players from best to worst
My algorithm uses Google's page rank algorithm, and power method for EigenValues
This is useful for ranking players/teams even if they have never played against each other

1. Using the Tennis Data provided in UTRTennisData.csv, I created created a nxn matrix to keep track of total scores in each game.
2. I created my algorithm is weighted on difference of score, and if a player won convincingly (2 points or more on an individual set)
3. I create a matrix where winner's score will be cell[B][C] and loser's score will be cell[C][B]
4. I then plotted the points on a dataframe and can be viewed at matrix.csv
5. Using power method for EigenValues, I solved for a dominant eigen vector and output the result to rank.csv
6. I sorted the data to result.csv with player id in first column and their rank in the second column

Lessons Learned
1. In my first algorithm I just plotting a difference in score leads to a faulty eigenvector
2. Adding more variables such as adding points when a player won convincingly leads to better ranking results.
2. Just ranking by players that never lost will not work since the winning may have won against really bad players.






