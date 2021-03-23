import synonyms_final as syn

'''Further tests for Question 1, Part (a)'''

def test_get_sentence_lists_a8():
    '''a8: word separation by -- and -'''
    text = 'Sometimes a change-- problem fixes everything- other times, not.'
    output = [['sometimes', 'a', 'change', 'problem', 'fixes', 'everything', 'other', 'times', 'not']]
    assert syn.get_sentence_lists(text) == output, "FAIL test a8"

def test_get_sentence_lists_a9():
    '''a9: word separation by new line'''
    text = 'this is a line\nthat runs onto another line but\nthen does it run onto a fourth line?'
    output = [['this', 'is', 'a', 'line', 'that', 'runs', 'onto', 'another', 'line', 'but', 'then', 'does', 'it', 'run',
               'onto', 'a', 'fourth', 'line']]
    assert syn.get_sentence_lists(text) == output, "FAIL test a9"

def test_get_sentence_lists_a10():
    '''a10: ignore irrelevant punctuation'''
    text = '"Is my use of commas, and other associated punctuation, correct!?" She asked, annoyed (and bored)' \
           ' with her lack of progress. She tried-with incredible effort- and finally managed it.'
    output = [['is', 'my', 'use', 'of', 'commas', 'and', 'other', 'associated', 'punctuation', 'correct'],
              ['she', 'asked', 'annoyed', 'and', 'bored', 'with', 'her', 'lack', 'of', 'progress'],
              ['she', 'tried', 'with', 'incredible', 'effort', 'and', 'finally', 'managed', 'it']]
    assert syn.get_sentence_lists(text) == output, "FAIL test a10"

def test_get_sentence_lists_a11():
    '''a11: ignore irrelevant space'''
    text = 'this is a line\nthat runs onto another               line but\nthen    does it--   run onto a fourth line?'
    output = [['this', 'is', 'a', 'line', 'that', 'runs', 'onto', 'another', 'line', 'but', 'then', 'does', 'it', 'run',
               'onto', 'a', 'fourth', 'line']]
    assert syn.get_sentence_lists(text) == output, "FAIL test a11"


#run the tests
test_get_sentence_lists_a8()
test_get_sentence_lists_a9()
test_get_sentence_lists_a10()
test_get_sentence_lists_a11()



'''Test for Question 1, Part (b)'''

def test_get_sentence_lists_from_files_b():
    '''b: split sentences of text from multiple files'''
    file_list = ['jack.txt','robot.txt'] # order of texts matters as ordering of lists in 'output' must exactly match result of function
    output = [['hello', 'jack'], ['how', 'is', 'it', 'going'], ['not', 'bad', 'pretty', 'good', 'actually'],
              ['very', 'very', 'good', 'in', 'fact'],
              ['i', 'robot', 'the', 'best', 'novel', 'by', 'asimov', 'the', 'worst', 'or', 'neither']]
    assert syn.get_sentence_lists_from_files(file_list) == output, "FAIL test b"

#run the test
test_get_sentence_lists_from_files_b()



'''Tests for Question 1, Part(c)'''

def test_build_semantic_descriptors_c1():
    '''c1: empty list'''
    output = {}
    assert syn.build_semantic_descriptors([]) == output, "FAIL test c1"

def test_build_semantic_descriptors_c2():
    '''c2: one sentence where every word appears once'''
    sentences = [['this', 'is', 'one', 'sentence']]
    output = {'this': {'is': 1, 'one': 1, 'sentence': 1}, 'is': {'this': 1, 'one': 1, 'sentence': 1},
              'one': {'this': 1, 'is': 1, 'sentence': 1}, 'sentence': {'this': 1, 'is': 1, 'one': 1}}
    assert syn.build_semantic_descriptors(sentences) == output, "FAIL test c2"

def test_build_semantic_descriptors_c3():
    '''c3: one sentence where some words appear multiple times'''
    sentences = [['this', 'is', 'this', 'one', 'sentence', 'this', 'one']]
    output = {'this': {'is': 1, 'one': 2, 'sentence': 1}, 'is': {'this': 3, 'one': 2, 'sentence': 1},
              'one': {'this': 3, 'is': 1, 'sentence': 1}, 'sentence': {'this': 3, 'is': 1, 'one': 2}}
    assert syn.build_semantic_descriptors(sentences) == output, "FAIL test c3"

def test_build_semantic_descriptors_c4():
    '''c4: more sentences where one word appears in different ones'''
    sentences = [['what','is','going','on'], ['tell','me','what']]
    output = {'what': {'is': 1,'going': 1,'on': 1,'tell': 1,'me': 1},
             'is': {'what': 1, 'going': 1, 'on': 1}, 'going':{'what': 1, 'is': 1, 'on': 1},
             'on':{'what': 1, 'is': 1, 'going': 1}, 'tell':{'me': 1, 'what': 1},
             'me':{'tell': 1, 'what': 1}}
    assert syn.build_semantic_descriptors(sentences) == output, "FAIL test c4"

def test_build_semantic_descriptors_c5():
    '''c5: more sentences where multiple words appear multiple times'''
    sentences = [['what', 'on', 'is', 'going', 'on'], ['tell', 'me', 'on', 'what', 'going']]
    output = {'what': {'on': 3, 'is': 1, 'going': 2, 'tell': 1, 'me': 1},
              'on': {'what': 2, 'is': 1, 'going': 2, 'tell': 1, 'me': 1},
              'is': {'what': 1, 'on': 2, 'going': 1},
              'going': {'what': 2, 'on': 3, 'is': 1, 'tell': 1, 'me': 1},
              'tell': {'me': 1, 'on': 1, 'what': 1, 'going': 1},
              'me': {'tell': 1, 'on': 1, 'what': 1, 'going': 1}}
    assert syn.build_semantic_descriptors(sentences) == output, "FAIL test c5"

def test_build_semantic_descriptors_c6():
    '''c6: sentences with 1 word'''
    sentences = [['one'],['is'],['the'],['best'],['number']]
    output = {'one': {}, 'is': {}, 'the': {}, 'best': {}, 'number': {}}
    assert syn.build_semantic_descriptors(sentences) == output, "FAIL test c6"


# Run the tests
test_build_semantic_descriptors_c1()
test_build_semantic_descriptors_c2()
test_build_semantic_descriptors_c3()
test_build_semantic_descriptors_c4()
test_build_semantic_descriptors_c5()
test_build_semantic_descriptors_c6()



'''Tests for Question 1, Part(d)'''

'''NOTE:
The correct output is highly influenced by the quality 
of the semantic descriptor. Therefore these tests are just 
looking out for errors rather than the accuracy of the function
'''

#Build semantic descriptors
'''This is a very limited dictionary - the more text the input files 
have the more accurate it can be in determining the most similar word'''

file_list = syn.get_sentence_lists_from_files(['wp_part.txt', 'robot.txt','going_on.txt'])
semantic_descriptors = syn.build_semantic_descriptors(file_list)


def test_most_similar_word_d1():
    '''d1: empty arguments'''
    output = 'Error'
    assert syn.most_similar_word('',[], {}) == output, "FAIL test d1"

def test_most_similar_word_d2():
    '''d2: word is not in semantic descriptor'''
    word = 'draw'
    choices = ['is', 'expect']
    output = 'Error'
    assert syn.most_similar_word(word, choices, semantic_descriptors) == output, "FAIL test d2"

def test_most_similar_word_d3():
    '''d3: one of the choices is not in the semantic descriptor'''
    word = 'is'
    choices = ['draw', 'expect']
    output = 'expect'
    assert syn.most_similar_word(word, choices, semantic_descriptors) == output, "FAIL test d3"

def test_most_similar_word_d4():
    '''d4: the word and the choices are all in the semantic descriptor'''
    word = 'is'
    choices = ['believe', 'expect']
    output = 'believe'
    assert syn.most_similar_word(word, choices, semantic_descriptors) == output, "FAIL test d4"



# Run the tests
test_most_similar_word_d1()
test_most_similar_word_d2()
test_most_similar_word_d3()
test_most_similar_word_d4()



