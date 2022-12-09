
a = {
    "li":["is"],"e":["the"],
    "mi":["me","my"],"sina":["you","your"],"ona":["he","she","it","they"],"ijo":["thing"],"jan":["person"],"pona":["good","fix"],"ike":["bad"],"moku":["eat","food"],"suli":["big","old","important"],"toki":["speak","language","hello"],
    "lili":["small"],"telo":["water","liquid"],"suno":["the sun"],"ilo":["tool"],"kili":["fruit","vegetable"],"ni":["this","that"],"pipi":["pest","bug"],"ma":["place"],"pakala":["mistake","break"],
    "esun":["shop","buy"],"lukin":["eye","see"],"jo":["have"],"pana":["give"],"pali":["do","make","work"],"pi":["of"],"wile":["want","need"],"kute":["ear","hear"],"kalama":["sound"],"nasa":["strange","stupid"],
    "lipu":["document","book","record"],"kulupu":["group","community"],"tenpo":["time","duration","event"],"jaki":["unclean","gross"],"linja":["rope","hair"],"luka":["hand","arm"],"noka":["foot","leg"],"lawa":["head","control"],"mama":["parent","ancestor","creator"],
    "en":["_and"],"kala":["fish"],"lape":["sleep"],"len":["fabric","clothing"],"kiwen":["stone","metal","hard object"],"kon":["air","gas","invisibe thing"],"poki":["box","container"],"musi":["entertainment","art"],"awen":["continue","stay"],"soweli":["animal","land animal"],"olin":["love"],"sin":["new","additional","extra"],
    "ala":["not"],"sona":["know"],"seme":["what","which","unknown to me"],"anu":["or"],"alasa":["hunt","gather"],"mani":["money"],"lupa":["hole","doorway"],"meli":["female"],"mije":["male"],"moli":["death","kill"],"mun":["moon"],
}

rules = {"#1" : "If the subject of the sentence is mi or sina the predicate comes immediately afte",
         "#2" : "If the subject of the sentence is anything other than mi or sina the predicate is separated from the subject with li",
         "#3" : "The predicate is separated from the direct object with the work e",
         "#3B" : "'A,B' mean A of type B, and 'A B C' means (A of type B) of type C. The parenthesis are redrawn using the word pi, meaning of",
         "#6" : "Yes/No question are formed by doubling the sentence's verb, with the word ala in the middle. To respond 'yes', you repeat the verb, and to respond 'no', you repeat the verb followed by ala"
}


en_tp = {}
for tp_word,en_list in a.items():
    for i in en_list:
        en_tp[i] = tp_word
        
print(a["esun"])

sentences = {"mama sina li lawa e kulupu lipu suli":"your parents lead the large book club",
             "mama sina li lawa e kulupu pi lipu suli":"your parents are in charge of a collection of large books",
             "toki mi jan misali li pana sona pi toki pona tawa":"",
             "mi moku e kala e kili":"I eat fish and fruit",
             "pipi li lape li moku":"bugs sleep and eat",
             "sina pona li lukin e lipu a jan":"you are good and you see books and people",
             "ona li moku ala moku e moku pona":"do they eat good food?",
             "sina sona ala sona e toki pona":"do you know toki pona?",
             "sina sona e seme":"what do you know?",
             "soweli li moli ala moli e mun":"did an animal kill the moon?",
             "soweli li moli e mun anu suno anu seme":"did the animal kil the moon or the sun",
             "tenpo seme la soweli li moli e mun":"when did the animal kill the moon",
             "soweli li moli e mun anu seme":"didn't an animal kill the moon"
             }

syllable1 = ['','j','k','l','m','n','p','s','t','w']
syllable2 = ['a','an','e','en','i','in','o','on','u','un']
unused = ['kan','lan','man','san','jen','men','nen','sen','min','nin','win','on','jon','non', 'pon', 'son', 'ton', 'ju', 'jun', 'kun', 'lun','nun', 'pun', 'tun']
forbidden = ['ji','ti','jin','tin','wo','won','wu','wun']

# english to toki pona
def trans_en(s,en_tp):
    x = s.split()
    r = ' '.join([en_tp[i] for i in x if i in en_tp])
    return r
        
for s1,s2 in sentences.items():
    w = s1.split()
    x = ''
    for i in w:
        
        if i in a:
            x += a[i][0] + " "
        else:
            pass
    print(f"{s1} --> {x}")

print(trans_en("you are good and you see book and people",en_tp))
print(len(a))


import re
f = open("lexicon.txt", 'r')
## weka – ~pu~ absent, away, ignored
tp_words = {}
for i in f:
    xx = re.sub('\s+',' ',i)
    if '~pu~' in xx:
        word,rest = xx.split(' – ')
        print(xx)
        rest = rest.replace('~pu~','')
        rest = rest.split(';')
        wlist = rest[0].split(',')
        tp_words[word] = wlist
    '''
    if '←' in xx:
        print(f"<- [{xx}]")
    elif '-' in xx:
        if 'post-pu' in xx:
            print(f"POST PU [{xx}]")
        elif 'pre-pu' in xx:
            print(f"PRE PU [{xx}]")
        elif 'pu' in xx:
            print(f"PU [{xx}]")
            tp_words.append(xx)
    '''
for i,j in tp_words.items():
    print(f"{i} ::: {j}")
'''
for s1,s2 in sentences.items():
    w = s1.split()
    x = ''
    for i in w:
        
        if i in a:
            x += tp_words[i] + " "
        else:
            pass
    print(f"{s1} --> {x}")
'''    
print(len(tp_words))
