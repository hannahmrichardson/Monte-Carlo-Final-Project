# Monte-Carlo-Final-Project
Monte Carlo Package for DS5100 Final Project 

## Read Me File for Monte Carlo Module 
New repo containing all relevant files for the DS5100 final project.
Monte Carlo Folder includes the files: Analyzer.py, Die.py, Game.py, MonteCarloTest.py, MonteCarlo.py (Monte Carlo contains code for Analyzer, Die, Game), __init__.py

### Metadata: 
## Project Name: Monte Carlo Final Project
Class: DS 5100
Student Name: Hannah Richardson
Student Net ID: zhx9yf
This URL: https://github.com/hannahmrichardson/Monte-Carlo-Final-Project

### Synopsis:
1. **Installation and Import Demo**
   ```py
   #install in the file
   pip install MonteCarlo
   #import the code
   import MonteCarlo
   import pandas as pd
   import numpy as np
   ```
3. **Create Dice Demo**
   In this demo we will create a die object made up off six sides with side values of 1,2,3,a,b,c. Then we will change the die weight of side a to a value of 5. We will roll the die 10 times.
   Finally, we will check the current state of the die and verify that all die have a weight of 1 except for face a. 
   ``` py
   #create a numpy array to pass 
   myfaces = np.array([1,2,3,"a","b","c"])
   #create a Die 
   myDie = MonteCarlo.Die(myfaces)
   #change the Die Weights, in this example we change the weight of die side a to have a weight of 5 
   myDie.change_side_weight("a", 5)
   #roll the die, in this example we roll the die 5 times
   myDie.roll_the_dice(5)
   #check the dies current state
   myDie.die_currentstate()
   ```
   The die_currentstate() will output a table. Note faces is the index, weights is a column:


   
5. **Play a Game Demo**
   In this demo we will play a game with the die created in our previous die demo. We will play the game with 3 dice and roll the dice 5 times. We will then check the result of the game
   played by looking at both the wide and narrow formatted tables 
   Note: This code should not be run unless a die is created, in this example the die is called myDie
   ``` py
   #add the dice we want to use in a list, we are using 3 dice
   myGameDice = [myDie, myDie, myDie]
   #create tehe game
   myGame = MonteCarlo.Game(myGameDice)
   #roll the dice 5 times 
   myGame.play(5)
   #view the play result in narrow format
   myGame.play_result("narrow")
   #view the play result in wide format
    
   ```
    The play result in narrow format will output a table . The Roll Number and Die Number columns are indicies and the Outcomes column is the face
   result of the roll:
       		                

   The play result in wide format will output a table. The Roll Number column is an index and the number columns are the Die Numbers, for example
   column 1 is the results for the first die:

   
7. **Analyze a Game Demo**
   Note: This code should not be run unless a game has been created and played using Game.play(n), in this example our game is called myGame. 
   ``` py
   #create the game
   myAnalyzer = MonteCarlo.Analyzer(myGame)
   #get the number of jackpots, in our example this code returns 0 
   myAnalyzer.jackpot()
   #get the face counts per roll
   myAnalyzer.face_counts_per_roll()
   #get the permutations
   myAnalyzer.permutation_count()
   #get the combinations
   myAnalyzer.combo_count()

   ```

    The face counts per roll will output a data frame:


   The permutations count will output a dataframe in the format. permutations is the index and Counts as column:


   
    The combinations count will output a dataframe in the format (full output not shown). Combinations is the index and counts as a column:
   
### API Description: 

## The Die Class
    1. ** Class DocString**
    '''
    The purpose of this file is to play a game. 
    
    to create a single die. Each die has a certain number of sides, also known as faces,
    that is passed into the file. Each side contains a unique symbol.
    Each die side has a weight. The weight is a positive number, initialized as 1 and can be changed later. The weight 
    determines the probability that the die will land on that face, fair dice will 
    have equal weights and unfair will have different weight values. 

    A die can be any discrete random variable associated with a stochastic process, 
    such as using a deck of cards, flipping a coin, rolling an actual die, or speaking a language.

    The die has one behavior, to be rolled a certain number of times. 

    Summary: This class can create a die, roll a die, modify a dies face weight, and return the current state of the weight. 
    Current state includes the dies faces and their respective weights. 
    '''
    2. ** Initialize Method **
        Docstring: '''
        PURPOSE 
        Given a numpy array of faces, create a single die. Upon creation each die has a set of faces and each die 
        has a weight value, initialized to 1. 
    
        INPUTS
        faces    NumPy array of faces. Array may be strings or numbers but values must be distinct.
        '''

        Parameters: faces list (data type = numpyarray)
        
    3. ** change_side_weight Method**
        Docstring: '''
        PURPOSE
        Change the weight of a single face value for a dice.
    
        INPUTS
        face_value    a face value that is present on the dice, this is the die face that the user wants 
                      to change the weight of.
        new_weight    a numeric value (integer, float, or castable as numeric). The weight will change 
                      to this numeric value.
        '''
        
        Parameters: face_value (data type = string or numeric), new_weight (data type = numeric)
    
    4. ** roll_the_dice Method**
        Docstring: '''
        PURPOSE
        roll the dice one or more times. When the dice is rolled it applies the weight of each weight and chooses a random 
        sample that is the die roll result. 
    
        INPUTS
        num_of_rolls  the number of times a die should be rolled, defaults to one roll.
        '''
        
        Parameters: num_of_rolls (data type = integer)
        
    5. ** die_currentstate Method**
        Docstring: '''
        PURPOSE
        Show the die's current state, as a dataframe. Current state includes the dies faces and their respective weights. 

        OUTPUTS
        a dataframe where the faces are the index and there is a column showing the weights for each die face. 
        '''

        Return Values: Dataframe,faces are the index and there is a column showing the weights for each die face.
    

## The Game Class
    1. **Class DocString**
    '''
    The purpose of this file is to play a game. A game consists of rolling one or more similar dice n number of times. 
    Similar dice means die with the same number of sides and face values, die rolled in the game may have different 
    weight values. 

    Summary: a list of die is passed to create a game, the die are rolled n number of times, only the most recent play is
    stored and it can be returned as a df. 
    '''

    2. **Initialize Method**
        Docstring: '''
        PURPOSE
        Initialize the game by taking in the receiveing the dice that will be used to play. 

        INPUTS
        similar_dice       a list of already instantiated similar die. 
                           Similar die means that the number and values of the faces are the same,
                           weights can have different values. 
        '''

        Parameters: similar_dice (data type is a list made up of Dice)
        
    3. **Play Method**
        Docstring: '''
        PURPOSE
        roll the dice a set number of times, privately saves a dataset with the game result.  

        INPUTS
        num_of_rolls        an integer to specify how many times the dice should be rolled
        '''

        Parameters: num_of_rolls (data type = integer)
        
    4. **Play Result Method**
        Docstring: '''
        PURPOSE
        Show the result of the most recent play as a dataframe
        
        INPUTS
        df_format          optional input that takes the string "wide" or "narrow" to specify how the result dataframe 
                           will be formatted

        OUTPUTS 
        a dataframe summarizing the most recent play in either wide or narrow format. Narrow format will have a multiindex of 
        roll number and die number and a column outcome. The outcome means the face that was roled on the die. A wide 
        format dataframe will show  have the roll number as a named index,
        columns for each die number (using its list index as the column name), 
        and the face rolled in that instance in each cell.
        '''

        Parameters: df_format (data type = string)
        Return Values: dataframe in two different possible formats both include data on the roll number, die number, and the roll outcome. 

## The Analyzer Class 
    1. **Class DocString**:
        '''The purpose of the analyzer is to take the results of a single game and 
        compute various descriptive statistical properties about it.

        Summary: Can compute the number of jackpots, the number of times a given face is rolled in an game, 
        combinations of faces rolled, and the permutations of faces rolled. 
        '''
    2. *Initializer Class**
        Docsting: '''
        PURPOSE
        Create a analyzer object that can be used to determine statistics about a game

        INPUTS
        game     a game object, will through an error if the object passed is not a game
        '''

        Parameters: game (data type = Game)

    3. **Jackpot Method**
        Docstring:'''
        PURPOSE
        A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die. 
        Computes how many times the game resulted in a jackpot.

        OUTPUTS 
        Returns an integer for the number of jackpots.
        '''
        
        Outputs: number of jackpots
    
    4. **Face Counts Per Roll Method**
        Docstring: '''
        PURPOSE
        Computes how many times a given face is rolled in each event.

        OUTPUTS 
        Returns a data frame of results.
        The data frame has an index of the roll number, 
        face values as columns, and count values in the cells.
        '''
        Outputs: dataframe containing roll number, face values, and a count representing the number of times they have been rolled
        
    5. **Combo Count Method**
        Docstring: '''
        PURPOSE
        Computes the distinct combinations of faces rolled, along with their counts.
        Combinations are order-independent and may contain repetitions.

        OUTPUTS 
        Returns a data frame of results with distinct combinations and a column for the associated counts.
        '''

        Outputs: A dataframe. The data frame is made up an index column that is the possible combination. The column value Counts counts 
        the number of times that a combination was rolled in the game. Note that all possible combinations are equal to the number of 
        die rolled. For example if 3 die were rolled then each possible combination will only contain 3 values. 
        
    6. **Permutation Count Method**
        Docstring: '''
        PURPOSE
        Computes the distinct permutations of faces rolled, along with their counts. Permutations are order-dependent and 
        may contain repetitions.

        OUTPUTS 
        a dataframe summarizing the distinct permutation and a column for the associated counts
        '''

        Outputs:  A dataframe. The data frame is made up an index column that is the possible permutations. The column value Counts counts 
        the number of times that a permutation was rolled in the game. Note that all possible permutations are equal to the number of 
        die rolled. For example if 3 die were rolled then each possible permutation will only contain 3 values. 
    


