import pandas as pd
import numpy as np
import random
import itertools

class Die: 
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
    def __init__(self, faces): 
        '''
        PURPOSE 
        Given a numpy array of faces, create a single die. Upon creation each die has a set of faces and each die 
        has a weight value, initialized to 1. 
    
        INPUTS
        faces    NumPy array of faces. Array may be strings or numbers but values must be distinct.
        '''

        #throw an error if not a numpy array
        if type(faces) is np.ndarray:
            self.faces = faces 
        else:
            raise TypeError("The faces variable must be of type numpy array")    

        #check if the values in the array are distinct, if not raise ValueError
        value_list = []
        for i in faces:
            if i in value_list:
                raise ValueError("All values in the faces array must be unique")
            else:
                value_list.append(i)
        
        weights = 1.0
        df_die = pd.DataFrame(
                {
                'faces':faces, 
                'weights':weights
                }) 
        self._df_die = df_die.set_index('faces')
    
    #method to change the weight of a single side    
    def change_side_weight(self, face_value, new_weight):
        '''
        PURPOSE
        Change the weight of a single face value for a dice.
    
        INPUTS
        face_value    a face value that is present on the dice, this is the die face that the user wants 
                      to change the weight of.
        new_weight    a numeric value (integer, float, or castable as numeric). The weight will change 
                      to this numeric value.
        '''
        #check to see if the face passed is a valid value 
        if face_value not in self.faces:
            #if not a valid value, raise an IndexError
            raise IndexError("The face value provided is not on this die") 
       
        #check to see if new_weight is castable, if it is then convert to float
        try:
            new_weight = float(new_weight)
            test_num = 0
        except ValueError: 
            test_num = 1
            
        #check to see if the weight is a valid type or if our try except caught an error
        if (type(new_weight) not in (int, float)) or test_num ==1:
            #if not numeric or castable as numeric raise TypeError
            raise TypeError("The new_weight must be numeric")

        #change the weight of the side specified with the new weight
        self._df_die.loc[face_value, "weights"] = new_weight

    def roll_the_dice(self, num_of_rolls = 1):
        '''
        PURPOSE
        roll the dice one or more times. When the dice is rolled it applies the weight of each weight and chooses a random 
        sample that is the die roll result. 
    
        INPUTS
        num_of_rolls  the number of times a die should be rolled, defaults to one roll.
        '''
        dice_results = []
        for i in range(0,num_of_rolls):
            #some code to roll the dice
            roll_result = random.choices(self.faces, weights=self._df_die["weights"])
            #roll_result = self._df_die.faces.sample(weights=self._df_die.weights).values[0]
            dice_results.append(str(roll_result[0]))
        return dice_results 

    def die_currentstate(self):
        '''
        PURPOSE
        Show the die's current state, as a dataframe. Current state includes the dies faces and their respective weights. 

        OUTPUTS
        a dataframe where the faces are the index and there is a column showing the weights for each die face. 
        '''
        return self._df_die




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



class Analyzer: 
    def __init__(self, game):
        '''The purpose of the analyzer is to take the results of a single game and 
        compute various descriptive statistical properties about it.

        Summary: Can compute the number of jackpots, the number of times a given face is rolled in an game, 
        combinations of faces rolled, and the permutations of faces rolled. 
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
                
        