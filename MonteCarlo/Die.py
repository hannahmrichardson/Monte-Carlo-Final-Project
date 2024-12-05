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