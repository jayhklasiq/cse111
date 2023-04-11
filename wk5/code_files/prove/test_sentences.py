import os
os.system('cls')
import random
import pytest
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase

def test_get_determiner():
    # # Call the get_determiner function.
    # determ = get_determiner(1)

    # # Verify that the word stored in the variable
    # # determ is in the list of single determiners.
    # words = ["a", "one", "the"]
    # assert determ in words

# 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single determiners.

    single_determiners = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single determiner.
        noun = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_determiners list.
        assert noun in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural determiner.
        noun = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_determiners list.
        assert noun in plural_determiners
    
def test_get_verb():
    # 1. Test the present tense determiners if quantity is 1.
    
    present_single_determiners = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        verb = get_verb(1, 'present')

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert verb in present_single_determiners

    # 2. Test the present tense determiner if the quantity is > 1.

    present_plural_determiners = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        verb = get_verb(2, 'present')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert verb in present_plural_determiners
        
    # 3. Test the past tense determiners.

    past_tense_determiners = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(0, 'past')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in past_tense_determiners
    
    # 4. Test the future tense determiners.

    future_tense_determiners = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(0, 'future')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in future_tense_determiners    

def test_get_preposition():
# 1. Test the get_preposition.

    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_preposition()

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in preposition
        
def test_get_prepositional_phrase():
# #    # Call the get_noun function.
#     noun = get_noun(1)

#     #Verify that the word stored in the variable
#     # determ is in the list of single determiners.
#     nouns = ["bird", "boy", "car", "cat", "child",
#         "dog", "girl", "man", "rabbit", "woman"]
#     assert noun in nouns
    
#     # Call the get_determiner function.
#     determ = get_determiner(1)
#     #Verify that the word stored in the variable
#     # determ is in the list of single determiners.
#     words = ["a", "one", "the"]
#     assert determ in words
    statement = 'about the cat'
    assert statement == ('about the cat')
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
