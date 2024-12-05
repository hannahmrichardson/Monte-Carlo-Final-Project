from Analyzer import Analyzer
from Die import Die
from Game import Game
from MonteCarlo import Die
from MonteCarlo import Game
from MonteCarlo import Analyzer


import unittest
import pandas as pd
import numpy as np




class MonteCarloSuite(unittest.TestCase):

    def test_1_die_initializer(self): 
        """
        Test if number of faces initialized correctly. The np.array and the current die df should be equal length 
        """
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        expected = len(myFaces)
        actual = len(myDie.die_currentstate())
        self.assertEqual(actual, expected)
        
    def test_2_change_weight(self): 
        """
        Test if change_side_weight method from Die successfully changes the
        weight for the expected side of the die
        """
        #create a test Die
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        #change the weight
        myDie.change_side_weight("a", 6)
        #pull the current df
        currentdf = myDie.die_currentstate()
        #save the actual weight that is showing after calling .change_side_weight
        myDieState = myDie.die_currentstate()
        actual = int(myDieState.weights["a"])
        #we expect the value to change to 6
        expected = 6
        #assert method
        self.assertEqual(actual, expected)

    def test_3_roll_die(self): 
        """
        Test if the roll_the_dice method from Die successfully returns a python list
        """
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        myResult = myDie.roll_the_dice(10)
        self.assertTrue(type(myResult ) == list)


    def test_4_current_state(self): 
        """
        Test if the die_currentstate method from Die successfully returns a dataframe
        """
        #create a test Die
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        
        #pull the current df
        currentdf = myDie.die_currentstate()

        #check type
        self.assertTrue(type(currentdf) == pd.core.frame.DataFrame)

    def test_5_game_initializer(self): 
        """
        Test if the initializer correctly returns a game type 
        """
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        myGameDice = [myDie, myDie]
        myGame = Game(myGameDice)
        self.assertTrue(type(myGame) == Game)
        
    def test_6_play(self):
        """
        Test if the play method from Game rolls the correct amount of times 
        """
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        myGameDice = [myDie, myDie]
        myGame = Game(myGameDice)
        myGame.play(3)
        expected = 3
        actual = len(myGame.play_result().index)
        self.assertEqual(actual, expected)

    def test_7_play_result(self):
        """
        Test if the play_result method from Game successfully returns a dataframe
        """
        
        myFaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myFaces)
        myGameDice = [myDie, myDie]
        myGame = Game(myGameDice)
        myGame.play(3)
        currentdf = myGame.play_result()

        #check type
        self.assertTrue(type(currentdf) == pd.core.frame.DataFrame)

    def test_8_analyzer_initializer(self):
        """
        Test if the initializer correctly throws a value errror if not input correctly
        """
        myfaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myfaces)
        myDieList = [myDie, myDie]
        myGame = Game(myDieList)
        myGame.play(3)
        #testanalyzer = Analyzer(myGame)
        self.assertRaises(ValueError, Analyzer, (myGame,myGame))

    def test_9_jackpot(self):
        """
        Test if the jackpot method from Analyzer returns a numeric value 
        """
        myfaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myfaces)
        myDieList = [myDie, myDie]
        myGame = Game(myDieList)
        myGame.play(3)
        testanalyzer = Analyzer(myGame)
        self.assertTrue(type(testanalyzer.jackpot()) is int)

    def test_10_face_counts_per_roll(self):
        """
        Test if the if the face_counts_per_roll method from Analyzer successfully returns a dataframe
        """
        myfaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myfaces)
        myDieList = [myDie, myDie]
        myGame = Game(myDieList)
        myGame.play(3)
        testanalyzer = Analyzer(myGame)
        currentdf = testanalyzer.face_counts_per_roll()
        self.assertTrue(type(currentdf) == pd.core.frame.DataFrame
)
    
    def test_11_combo_count(self):
         """
         Test if the if the combo_count method from Analyzer successfully returns a dataframe
         """
         myfaces = np.array([1,2,3,"a","b","c"])
         myDie = Die(myfaces)
         myDieList = [myDie, myDie]
         myGame = Game(myDieList)
         myGame.play(3)
         testanalyzer = Analyzer(myGame)
         currentdf = testanalyzer.combo_count()
         self.assertTrue(type(currentdf) == pd.core.frame.DataFrame)
    
    def test_12_permutation_count(self):
        """
        Test if the if the permutation_count method from Analyzer successfully returns a dataframe
        """
        myfaces = np.array([1,2,3,"a","b","c"])
        myDie = Die(myfaces)
        myDieList = [myDie, myDie]
        myGame = Game(myDieList)
        myGame.play(3)
        testanalyzer = Analyzer(myGame)
        currentdf = testanalyzer.permutation_count()
        self.assertTrue(type(currentdf) == pd.core.frame.DataFrame)
    

if __name__ == '__main__':
    unittest.main(verbosity=3)