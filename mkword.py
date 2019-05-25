# coding: utf-8

import random
import sys
import os
import re
import json

class wordmaker:
    def __init__(self):

        #子音連続のデータ(JSON)
        with open('cons_cluster.json', 'r') as fp:
            data = json.load(fp)
            self.vowl_list = data["vowl_list"]
            self.syllable_list = data["syllable_list"]
            self.cons_cluster = data["cons_clusters"]

    #母音や子音配列をランダムで選択する
    def choice(self, string):
        if string == 'v':
            return random.choice(self.vowl_list)
        else:
            return random.choice(self.cons_cluster[string])

    #口蓋化
    def palatalize(self, word):
        tempword = list(word)
        r = random.randint(1,len(tempword))
        
        #挿入場所に母音がある場合はひとつ前にずらす
        #例:tayp -> tyap
        if word[r-1] in self.vowl_list:
            r -= 1

        tempword.insert(r,'y')

        return ''.join(tempword)

    #単語を生成する
    def make_word(self, syllable):
        isFirstCons = True
        word = ''
        for s in syllable.replace('cv','c.v').replace('vc','v.c').split('.'):
            #最初の子音連続が現れた時
            if 'c' in s and isFirstCons:
                word += self.choice('start_cons_' + s)
                isFirstCons = False
                continue

            if 'c' in s:
                word += self.choice('end_cons_' + s)

            if 'v' in s:
                word += self.choice(s)

        #ランダムで口蓋化処理をする
        if random.choice([0,1,2,3,4,5]) == 0:
            return self.palatalize(word)
        else:
            return word

    #単語をn個生成する
    def make_wordlist(self, n):
        for i in range(0,n):
            print(self.make_word(random.choice(self.syllable_list)))

mw = wordmaker()
mw.make_wordlist(10)
