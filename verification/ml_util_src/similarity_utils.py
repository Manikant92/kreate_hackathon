from fuzzywuzzy import fuzz
from itertools import permutations


def detect_string_similarity(map1, map2):
    """ Detect Name Similarity Scores by doing all valid checks and operations"""
    name1 = map1.get('name')
    name2 = map2.get('name')
    if name1.lower() == name2.lower():
        cosine = 100
        reorder_flag = False
        # return cosine,
    else:
        list1 = name1.lower().split()
        list2 = name2.lower().split()
        perm_list1 = list(permutations(list1))
        perm_list2 = list(permutations(list2))
        score = []
        flag = False
        for i in perm_list1:
            if flag:
                break
            for j in perm_list2:

                new_s = ' '.join(i)
                new_j = ' '.join(j)
                percent = fuzz.ratio(new_s, new_j)
                if percent == 100:

                    score.append(percent)
                    flag = True
                    break
                else:
                    score.append(percent)
        cosine = max(score)
        reorder_flag = True
    return {'cosine_flag': cosine, 'reorder_flag': reorder_flag }


def detect_dob_matching(map1, map2):
    """ Detect DOB Matching logics """
    dob_flag = False
    yob_flag = False
    dob1 = map1.get('dob')
    dob2 = map2.get('dob')
    list1 = dob1.split('/')
    list2 = dob2.split('/')
    if dob1 == dob2:
        dob_flag = True
        yob_flag = False
    
    elif list1[0] == '00' or list2[0] == '00':
        if list1[2] == list2[2]:
            dob_flag = False
            yob_flag = True
        elif list1[2] != list2[2]:
            dob_flag =  False
            yob_flag = False
    return {'dob_flag': dob_flag, 'yob_flag': yob_flag }