import re
import numpy as np
from math import sqrt
from utils_coll import *
from clausal import *


def getSyntacticIndices(text_dict):
    '''
    25 syntactic complexity measures
    param: text_dict, type <dict>
    return: indices, type <dict>
    '''

    indices = {}

    # get linguistic features
    sent_length_list, clause_length_list, T_unit_length_list = [], [], []
    collocation_list = []

    for sent_id, info in text_dict.items():

        sent, worddict = info['sent'], info['worddict']

        # clausal features
        if not re.search('[，。？！；……]', sent):
            continue
        sent_length, clause_lengths, T_unit_lengths = clausal_index(sent, worddict)
        sent_length_list.append(sent_length)
        clause_length_list.extend(clause_lengths)
        T_unit_length_list.extend(T_unit_lengths)

        # collocations
        collocations = getColl(worddict)
        collocation_list.extend(collocations)

    # udpate clausal indices
    if len(sent_length_list) > 2:
        meanSL, meanCL, meanTL = np.mean(sent_length_list), np.mean(clause_length_list), np.mean(T_unit_length_list)
        indices['MLS'] = meanSL
        indices['MLC'] = meanCL
        indices['MLTU'] = meanTL
        indices['NCPS'] = len(clause_length_list) / len(sent_length_list)
        indices['NTPS'] = len(T_unit_length_list) / len(sent_length_list)

    # update collocation based indices
    if len(collocation_list) > 10:
        coll_num = len(collocation_list)
        sqrt_coll_num = sqrt(coll_num)

        set_colls = set(collocation_list)
        coll_diversity = len(set_colls) / sqrt_coll_num
        indices['TOTAL_RTTR'] = coll_diversity

        unique_colls = [coll for coll in collocation_list if isUniqueColl(coll)]
        indices['UNIQUE_RTTR'] = len(set(unique_colls)) / (sqrt(len(unique_colls)) + 1)
        indices['UNIQUE_RATIO'] = len(unique_colls) / coll_num

        lowfreq_collls = [coll for coll in collocation_list if isLowFreqColl(coll)]
        indices['LOWFREQ_RATIO'] = len(lowfreq_collls) / coll_num

        # coll indices based on different types
        coll_types = ['VO', 'SP', 'AN', 'AP', 'CN*', 'PP*', 'PV*', 'PC*']
        coll_type_dict = {k: [] for k in coll_types}

        for coll in collocation_list:
            typ = coll_dict[coll.split('\t')[-1]]
            coll_type_dict[typ].append(coll)

        for ct, v in coll_type_dict.items():
            indices[ct + '_RATIO'] = len(v) / len(collocation_list)
            indices[ct + '_RTTR'] = 0
            if v:
                indices[ct + '_RTTR'] = len(set(v)) / sqrt(len(v))

    return indices
