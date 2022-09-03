import csv
import re
# import pandas as pd
import emoji

with open('tweets_df2.csv', encoding="utf-8") as csvfile:
    # reader = csv.DictReader(csvfile)
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    my_dict = {}
    keywords = {
        'VM': 0,
        'VH': 0,
        'V': 0,
        'M': 0,
        'H': 0
    }
    for row in csv_reader:
        content = row[4]
        if "vestibular" in content and "migraine" in content:
            keywords['VM'] = keywords['VM'] + 1
        elif "vestibular" in content or "migraine" in content:
            if "vestibular" in content:
                keywords['V'] = keywords['V'] + 1
            else:
                keywords['M'] = keywords['M'] + 1
        if "vestibular" in content and "headache" in content:
            keywords['VH'] = keywords['VH'] + 1
        elif "headache" in content:
            keywords['H'] = keywords['H'] + 1

        word_array = re.split(' |,|_|-|!|\.|\|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|\#|"|“|”|‘|’|-|…|\n|/|\'|;', content)
        word_set = set(word_array)
        for word in word_set:
            if not word.startswith('@') and word and word != '▸':
                # do more checks on word
                word = word.lower()
                # word = removeTags(word)
                # remove plural s
                if word.endswith('s'):
                    word = word[0:len(word) - 1]
                if word in my_dict.keys():
                    my_dict[word] = my_dict[word] + 1
                else:
                    my_dict[word] = 1
    
    unsorted_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(unsorted_dict)
    print(sorted_dict)
    print(keywords)

with open('dictionary.csv', 'w') as csvfile:
    for key in keywords.keys():
        csvfile.write("%s,%s\n"%(key,keywords[key]))
    for key in sorted_dict.keys():
        if sorted_dict[key] > 251:
            csvfile.write("%s,%s\n"%(key,sorted_dict[key]))