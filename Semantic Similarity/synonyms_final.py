import math
import re


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''

    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]

    # Make sure empty vectors don't cause an error -- return -1 as
    # suggested in the handout for Project 2.
    norm_product = norm(vec1) * norm(vec2)
    if norm_product == 0.0:
        return -1.0
    else:
        return dot_product / norm_product


def get_sentence_lists(text):
    ''' Return text as list of sentences, each a list of words
    in lower case, ignoring punctuation
    '''
    text_list = re.split('[.?!]', text)
    list = []
    for i in range(0, len(text_list)):
        sentence = re.split(',| |-|--|:|\. |;|\'|\"|\n|\)|\(', text_list[i].lower().strip())
        list.append([x for x in sentence if x != ''])
    final_list = [x for x in list if x != []]
    return final_list


def get_sentence_lists_from_files(filenames):
    ''' Return text from several files as list of sentences,
    each a list of words
    '''
    list = []
    for file in filenames:
        infile = open(file,'r')
        list.append(get_sentence_lists(infile.read()))
        infile.close()
    final_list = [val for sublist in list for val in sublist]
    return final_list


def build_semantic_descriptors(sentences):
    '''Return semantic descriptor vector of each word in 'sentences'
    as a dictionary
    '''
    d = {}   #create empty dictionary
    for list in sentences:
        for w in list:
            d[w]={}
            for list2 in sentences:
                if w in list2:
                    for i in list2:
                        if i != w:
                            d[w][i] = d[w].get(i, 0) + 1
    return d



def most_similar_word(word, choices, semantic_descriptors):
    '''Return 'choices' option most similar to 'word'
    using semantic descriptor
    '''
    max = -1
    answer = 'Error'
    for i in choices:
         if (semantic_descriptors.get(word) and semantic_descriptors.get(i)) != None and cosine_similarity(semantic_descriptors[word], semantic_descriptors[i])>=max:
            max = cosine_similarity(semantic_descriptors[word], semantic_descriptors[i])
            answer = i
    return answer #return 'Error' for case where 'word' or any of 'choices' not present in semantic descriptor


def run_similarity_test(filename, semantic_descriptors):
    '''Return percentage accuracy of most_similar_word function'''
    count = 0
    infile = open(filename,'r')
    lines = infile.readlines()
    infile.close()
    for i in lines:
        list = i.split()
        word = list[0]
        choices = list[2:]
        answer = most_similar_word(word, choices, semantic_descriptors)
        if answer == list[1]:
            count += 1
    percent = float((count/len(lines))*100)
    return percent



file_list = get_sentence_lists_from_files(['wp.txt', 'sw.txt'])
semantic_descriptors = build_semantic_descriptors(file_list)
similarity = run_similarity_test('test.txt', semantic_descriptors)
print(similarity)



