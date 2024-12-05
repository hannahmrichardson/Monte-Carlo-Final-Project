import pandas as pd
import numpy as np
import random
import itertools

from Die import Die

class Game: 
    '''
    The purpose of this file is to play a game. A game consists of rolling one or more similar dice n number of times. 
    Similar dice means die with the same number of sides and face values, die rolled in the game may have different 
    weight values. 

    Summary: a list of die is passed to create a game, the die are rolled n number of times, only the most recent play is
    stored and it can be returned as a df. 
    '''
    def __init__(self, similar_dice):
        '''
        PURPOSE
        Initialize the game by taking in the receiveing the dice that will be used to play. 

        INPUTS
        similar_dice       a list of already instantiated similar die. 
                           Similar die means that the number and values of the faces are the same,
                           weights can have different values. 
        '''
        self.similar_dice = similar_dice

    def play(self, num_of_rolls):
        '''
        PURPOSE
        roll the dice a set number of times, privately saves a dataset with the game result.  

        INPUTS
        num_of_rolls        an integer to specify how many times the dice should be rolled
        '''
        rollnumlist = []
        dienumlist = self.similar_dice #remove this line, just so you remember what it represents

        #initialize the df
        for i in range(0,num_of_rolls):
            rollnumlist.append(i+1)
        result_df = pd.DataFrame(
        {
        'Roll Number' :rollnumlist
        })

        for i in range(0,len(self.similar_dice)):
            for j in self.similar_dice:
                #currentdiedf = j.die_currentstate()
                #h = currentdiedf.index[i]
                result_df[i+1] = j.roll_the_dice(num_of_rolls)

        self._play_result = result_df.set_index('Roll Number')

    def play_result(self, df_format = "wide"):
        '''
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
        if df_format == "narrow":
            Narrow = self._play_result.unstack().to_frame('Outcomes')
            Narrow.index.names = ['Die Number','Roll Number']
            Narrow = Narrow.reset_index().set_index(['Roll Number','Die Number'])
            return Narrow
            #code to return the most recent result in narrow format
        elif df_format == "wide":
            return self._play_result
        else:
            raise ValueError("Entered invalid dataframe format, must be narrow or wide")
        