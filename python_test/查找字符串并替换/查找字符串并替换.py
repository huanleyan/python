import nltk
import string 
import os


def extend_word(text):
    if text.find('\'') >0 :
        old2new = dict()
        words = text.split()
        for word in words:
            if word.find('\'') >0 :
                parts = word.split('\'')
                if parts[1] == 'm':
                    parts[1] = 'am'
                elif parts[1] == 's':
                    parts[1] = 'is'
                elif parts[1] == 're':
                    parts[1] = 'are'
                elif parts[1] == 't':
                    parts[1] = 'not'
                elif parts[1] == 've':
                    parts[1] = 'have'
                elif parts[1] == 'll':
                    parts[1] = 'will'
                elif parts[1] == 'd':
                    if words[words.index(word)+1] == 'better':
                        parts[1] = 'had'
                    else:
                        parts[1] = 'would'
                if parts[0].endswith('n'):
                    parts[0] = parts[0][:-1]
                old2new[word] = ' '.join(parts)
        _text = text
        for old_word in old2new.keys():
            _text = _text.replace(old_word, old2new[old_word])
        return _text


def return_order_key(record):
    return record[1]

def show_import_word(records):
    items = sorted(records.items(), key=return_order_key, reverse=True)
    freq=0
    for item in items:
        word,tag = nltk.pos_tag([item[0]])[0]
        if tag.startswith('NN'):
            print(word)
            if item[1]<freq:
                return 
            freq = item[1]
    if not frq:
        print(items[0][0])

def process_file(filename):
    with open(filename, 'r') as file:
        article = file.read()
        no_pun_text = article
        #查找含有字符的字符串
        _punctuation = string.punctuation.replace('\'','')
        #delete punctuation except '''
        for pun in _punctuation:
            no_pun_text = no_pun_text.replace(pun,'')
        complete_text = extend_word(no_pun_text)
        records = dict()
        for word in complete_text.lower().split():
            records[word] = records.get(word,0)+1
        print('='*30)
        print('current file:', filename)
        print('-'*20)
        show_import_word(records)

def process_files(path='.'):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.txt'):
            process_file(os.path.join(path, file))

process_files()

