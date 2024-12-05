import pandas as pd
import numpy as np
import random
import itertools

from Die import Die
from Game import Game

class Analyzer: 
    '''The purpose of the analyzer is to take the results of a single game and 
        compute various descriptive statistical properties about it.

        Summary: Can compute the number of jackpots, the number of times a given face is rolled in an game, 
        combinations of faces rolled, and the permutations of faces rolled. 
    '''
    def __init__(self, game):
        '''
        PURPOSE
        Create a analyzer object that can be used to determine statistics about a game

        INPUTS
        game     a game object, will through an error if the object passed is not a game
        '''
        self.game = game
        if type(self.game) !=  Game:
            raise ValueError("The game passed must be a Game object")
        
    
    def jackpot(self):
        '''
        PURPOSE
        A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die. 
        Computes how many times the game resulted in a jackpot.

        OUTPUTS 
        Returns an integer for the number of jackpots.
        '''
        counter = 0 
        dfj = self.game.play_result()
        
        for i in dfj.index:
            tempdf = dfj[dfj.index == i]
            myvals = np.array(tempdf.values)
            if (len(np.unique(myvals)) == 1):
                counter +=1 
        return counter
        
    def face_counts_per_roll(self):
        '''
        PURPOSE
        Computes how many times a given face is rolled in each event.

        OUTPUTS 
        Returns a data frame of results.
        The data frame has an index of the roll number, 
        face values as columns, and count values in the cells.
        '''
        dfh = self.game.play_result("narrow")
        face_counts = dfh.groupby(["Roll Number", "Outcomes"]).Outcomes.value_counts().unstack().fillna(0)
        return face_counts

    def combo_count(self):
        '''
        PURPOSE
        Computes the distinct combinations of faces rolled, along with their counts.
        Combinations are order-independent and may contain repetitions.

        OUTPUTS 
        Returns a data frame of results with distinct combinations and a column for the associated counts.
        '''
        mygameresult = self.game.play_result()
        combinations_list = mygameresult.values.tolist()

        for i in combinations_list:
            i = sorted(i)

        df = pd.DataFrame(
            {
                'Combinations': combinations_list,
                'Counts': 1
            })
        
        full_combinations_list = list(itertools.combinations_with_replacement((np.unique(mygameresult.values)).tolist(), len(mygameresult.columns.tolist())))

        #for i, val in enumerate(combinations_list):
        newlist = []

        for j in full_combinations_list:
            if sorted(list(j)) not in combinations_list:
                newlist.append(list(j))

        df_combos2 = pd.DataFrame(
            {
                'Combinations': newlist,
                'Counts': 0
            })
                

        df_combos_final = pd.concat([df, df_combos2], axis=0)
        df_combos_final_ = df_combos_final.set_index(['Combinations'])
        return df_combos_final_    

    

    def permutation_count(self):
        '''
        PURPOSE
        Computes the distinct permutations of faces rolled, along with their counts. Permutations are order-dependent and 
        may contain repetitions.

        OUTPUTS 
        a dataframe summarizing the distinct permutation and a column for the associated counts
        '''
        mygameresult = self.game.play_result()
        permutations_list = mygameresult.values.tolist()

        df_permutations = pd.DataFrame(
            {
                'permutations': permutations_list,
                'Counts': 0
            })
        permutationlist = []
        for i, element in enumerate(permutations_list):
            if list(df_permutations.loc[i]) in permutationlist:
                currentval = df_permutations.loc[i, "Counts"] #fix this line to pull the appropriate value
                newval = currentval + 1
                df_permutations.loc[i, "Counts"] = newval
            else:
                permutationlist.append(list(df_permutations.loc[i]))
                df_permutations.loc[i, "Counts"] = 1

        possiblepermutations = list(itertools.product((np.unique(mygameresult.values)).tolist(), repeat = len(mygameresult.columns.tolist())))

        newlist = []
        for j in possiblepermutations:
            if list(j) not in permutationlist:
                newlist.append(list(j))

        df_permutations2 = pd.DataFrame(
            {
                'permutations': newlist,
                'Counts': 0
            })
                

        df_permutations_final = pd.concat([df_permutations, df_permutations2], axis=0)
        df_permutations_final_ = df_permutations_final.set_index(['permutations'])
        return df_permutations_final_
                
