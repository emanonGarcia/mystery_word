import mystery_word


def test_no_repeats():
    assert mystery_word.is_correct(['H', 'E', 'L', 'P'], 'HELP') == True


def test_with_repeats():
    assert mystery_word.is_correct(['O', 'T'], 'TOOT') == True


def test_incomplete():
    assert mystery_word.is_correct(['O', 'T', 'H', 'N'], 'PYTHON') == False


def test_y_lets_play():
    '''after executing nosetests, when prompted, type: y '''
    assert mystery_word.lets_play() == True



test_no_repeats()
test_with_repeats()
test_incomplete()
