#coding:utf-8
path='poems.txt'
poem_dict='poems_dict.pkl'
words_dict='words_dict.pkl'
import random
# import cPickle as pickle
import pickle
import re

def build_word_dict(path_txt,path_pkl):
    f=open(path_pkl,'wb')
    s = open(path_txt,'r',encoding='utf-8').read()
    p = re.findall(r'[\u4e00-\u9fa5]', s)
    pickle.dump(p,f)

def build_poem_dict(path_txt,path_pkl):
    f=open(path_pkl,'wb')
    poem_dict={}
    with open(path_txt,'r',encoding='utf-8')as rt:
        content=rt.read().replace('\n ','\n').replace('\n\n\n','\n\n\n').split('\n\n\n')
        # print(len(content))
        i=0
        for poem in content:
            poem_dict[str(i)]=poem
            i+=1

    pickle.dump(poem_dict,f)
    print('Written Done!!!')

def get_single_poem(id):
    poems=pickle.load(open(poem_dict,'rb'))
    return poems[str(id)]

def get_three_word(word):
    word_list = pickle.load(open(words_dict, 'rb'))
    # print(word_list[:10])
    rd=random.sample(range(0,len(word_list)),4)
    words_=[word_list[e] for e in rd if word_list[e] != word]
    return words_[:3]

def get_one_sentence(poem):
    poem=get_single_poem(poem)
    while(1):
        poem_=poem.split('\n')
        ret=[]
        pp=re.compile(r'[，、()（）]')
        for p in poem_:
            p_s=pp.split(p)
            # print(p_s)
            if len(p_s)==2:
                ret.append(p)
        if len(ret)>=1:
            break
        else:
            poem = get_single_poem(poem)
    return ret[random.randint(0,len(ret)-1)]

def main():
    pass
    # build_poem_dict(path,poem_dict)
    # build_word_dict(path,words_dict)
    # print(get_three_word('新'))
    # print(get_one_sentence(50))
    # print(get_one_sentence(50))


if __name__ == '__main__':
    main()