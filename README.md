# TennisPlayerRanking
Ranking Tennis Players

Created a script to rank tennis players from best to worst
This algorithm uses Google's page rank algorithm, and power method for EigenValues
This is useful when ranking players even if they have never played against each other

1. Using the Tennis Data provided in UTRTennisData, I created created a nxn matrix to keep track of total scores in each game.
2. I created my algorithm based on difference of score, and if a player won convincingly (more then 2 points)
3. Create a matrix where winner's score will be cell[B][C] and loser's score will be cell[C][B]
4. Plot the points on a dataframe matrix.csv
5. Using power method for EigenValues, I solved for a dominant eigen vector and output the result to rank.csv
6. I sorted the data to result.csv with player id in first column and their rank in the second column

Lessons
1. In my first algorithm I learned just plotting a difference in score will lead to a faulty eigenvector
2. Just ranking by players that never lost will not work since they may have won against bad players.






