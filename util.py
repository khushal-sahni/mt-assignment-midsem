import re
import os
import pandas as pd
from googletrans import Translator
from wxconv import WXC
from nltk.corpus import wordnet

translator = Translator()


def wx_converter(word):
    con = WXC(order='utf2wx')
    return con.convert(word)


def sentence_generator(word):
    syns = wordnet.synsets(word)
    # print(syns[0])

def get_mrs_concept_and_rels(word_start_pos, word_end_pos, mrs):
    pos = mrs.find('<' + str(word_start_pos) + ':' + str(word_end_pos) + '>')
    mrs_start = pos
    while mrs[mrs_start] != '[':
        mrs_start = mrs_start - 1
    mrs_concept = mrs[mrs_start + 1:pos]
    print(mrs)
    return mrs_concept


def Extraction(f, sub):
    res = [i for i in range(len(f)) if f.startswith(sub, i)]
    l = len(res)
    mc_dic = {}
    mv_dic = {}
    las = []
    for i in range(l):
        las.append(f.rfind("[", 0, res[i]))

    for i in range(l):
        mc_dic[i] = f[las[i]+1:res[i]]
    i = 0
    for i in range(l):
        xyz = ""
        p = 0
        k = f[res[i]+5:]
        for e in k:
            if e == '[':
                p = p+1
            elif e == "]" and p != 0:
                p = p-1
            elif e == ']' and p == 0:
                break
            elif p == 0:
                xyz += e
        mv_dic[i] = xyz
        xyz = ""

    for i in range(l):
        t = re.sub(r'\d', "*", mv_dic[i])
        t.replace("**", "*")
        mv_dic.update({i: t})

    pos = []
    for j in range(l):
        k = mv_dic[j]
        pos.append([i for i in range(len(k)) if k.startswith("ARG", i)])
        w = 0
        for h in pos[j]:
            u = k[0:h+3]
            u += str(w)
            u += k[h+4:]
            w = w+1
        mv_dic.update({j: u})
        u = ''

    DIC = {sub: [mc_dic, mv_dic]}
    return(DIC)


# Driver code
# Y = Extraction("/content/test.txt", "<0:2>")

# print(Y)
