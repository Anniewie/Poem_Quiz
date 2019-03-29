#coding:utf-8
import Poem_utils as poem
import random
import re

def get_sentence():
    rd=random.randint(0,1000)
    sentence=poem.get_one_sentence(rd)
    pp=re.compile(r'[，。！？()（）]')
    senence_=pp.split(sentence)
    # print(senence_)
    while(len(senence_[1])<2):
        rd = random.randint(0, 1000)
        sentence = poem.get_one_sentence(rd)

        pp = re.compile(r'[，。！？（）()]')
        senence_ = pp.split(sentence)
    rd_1=random.randint(0,1)
    mark_0=sentence[len(senence_[0])]
    mark_1=sentence[-1]
    # print(mark_0,mark_1)
    if rd_1==0:
        # print(senence_[1])
        return sentence,senence_[0]+mark_0+'_'*3*len(senence_[1])+mark_1,senence_[1]
    # print(senence_[0])
    return sentence,'_'*3*len(senence_[0])+mark_0+senence_[1]+mark_1,senence_[0]

def get_poem_words():
    rd = random.randint(0, 1000)
    sentence = poem.get_one_sentence(rd)
    sentence_ = sentence
    s='。、，！……？#@￥%$*&（）().,<>\\/《》|“”‘’'
    answer='__'
    # print(sentence)
    while(1):
        rd_1 = random.randint(0, len(sentence)-1)
        if sentence[rd_1] not in s:
            answer=sentence[rd_1]
            break
    try:
        sentence = sentence.replace(answer, '__', 1)
    except:
        print("Something Wrong!")
    items=[answer]
    items.extend(poem.get_three_word(answer))
    ans_ = random.sample(range(0,4), 4)
    items_=[items[e] for e in ans_]
    # answer_id=items_.index(answer)
    # print(answer_id)
    return sentence_,sentence,items_,answer

def get_poem():
    rd = random.randint(0, 1000)
    poem_ = poem.get_single_poem(rd)
    while('、' in poem_ or '！' in poem_ or '？' in poem_ or '（' in poem_ or '）' in poem_ or '(' in poem_ or ')' in poem_):
        rd = random.randint(0, 1000)
        poem_ = poem.get_single_poem(rd)
    poem__=poem_.split('\n')
    title=poem__[0]
    author=poem__[1]
    content='\n'.join(poem__[2:])
    return rd,title,author,content


if __name__ == '__main__':
    # print(get_sentence())
    # print(get_poem_words())
    # for i in range(1000):
    #     get_poem()
    pass