Hey this is starting repos of ML with basic datasets<br>
Added Data Preprocess for the text and standard dataset set<br> 
Added The Regression Folder into the Repository<br>
From Today it will contain outputs with graphs<br>
 # Data Preprocessing
  The subject matter in Machine Learning is Data preprocessing<br>
  It is said that 80% is data preprocessing from the 100% of data science.<br>
  So I introduce You two types of data preprocessing in numbers<br>
  - ### Categorical Variable
    There are mainly 2 types
     - Ordinal
     - Numeral
   #### Ordinal
   - They are the one's which can be compared or ordered<br>
      Say for example we can order grade A to grade B i.e.<br>
      Garde A > Grade B or say marks in grade A is > grade B.<br>
      They are handled by simply mapping ranking
  #### Nominal
   - This is the one's which can not be compared or at same level<br>
     best example gender we cannot compare gender<br>
     They are to be one hot encoded i.e. say male => [1, 0]<br>
     Female => [0, 1] as per this [Male, Female] is the data<br>
     <br>
 # Regression
   In Statistics, Regression is defined as the method of<br>
   Obtaining co realtions or a mapping such that F(x) ~= Y<br>
   i.e. an estimate of the general population.<br>
   <br>
   But let's see or look it with a simple human prespective<br>
   Not the stastical one, Let's say you are in a party <br>
   And rather interesting game pops up i.e. you need to guess<br>
   The number of balls in jar without counting, opening or anyway<br>
   touching the jar (Closest number wins. And Winner get's a good gift.<br>
   You need that gift<br>
   <br>
   So you think of a way to see, And guess a number, Now the way <br>
   To do this is Take note of the previous guess and perform an estimate<br>
   with the mean of the people who are coming back with wrong answer<br>
   This is basically sandwiching towards the right direction and make a guess.<br>
   The activity you just perform let you as a winner Why? Cause of stats<br>
   This activity is estimation, and that is what we do in regression<br>
   Like the jar winning method, we do is take the guess from avilable information<br>
   Calculate or guess a number find how much far we are and then see the next person(number)<br>
   with the closest and guess again until you reach the lowest error or estimate<br>
