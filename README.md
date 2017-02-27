# Mystery Word
Mystery Word in an adaptation of the game hangman. After the user inputs 'Y/y' to begin the game and selects a difficulty level, a random word in generated and the user is given 8 tried to guess the work correctly. If the word is guessed correctly within the set number of attempts, the user will be prompted if he/she would like to play again. 

### Prerequisites
Python3

for mac
```
brew install python3
```

or visit https://www.python.org/downloads/

Install nose using setuptools/distribute:
for mac

```
easy_install nose
```
Or
```
pip install nose
```

### Running the tests
Run: 
```
nosetests
```
from the command line in the same directory as the mystery_word.py script


### Break down into end to end tests

Tests will determine if the correct guesses match the mystery word as well as check if the input of the lets_play() module retuns True when Y/y are entered. If an invalid entry is input the user is prompted to submit again
```
...y
```
## Authors

* **Luis Garcia** - *Initial work* - [emanonGarcia](https://github.com/emanonGarcia)
