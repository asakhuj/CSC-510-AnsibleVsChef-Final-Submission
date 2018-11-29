'''

@author: atrivedi
'''
import pandas as pd
import pke
import re
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib import *
from pandas.tests.io.parser import comment



def KPMiner_suggestions(input_text):
    extractor = pke.unsupervised.KPMiner()
    # input_text = u"""vmware tools plugins resolutionSet pe rubygem net ssh pe ruby stomp vmware tools vmmemctl common"""
    
    extractor.read_text(input_text)
    extractor.candidate_selection()
    extractor.candidate_weighting()
    keyphrases = extractor.get_n_best(n=50, stemming=False)
    return keyphrases


def TopicRank_suggestions(input_text):
    extractor = pke.unsupervised.TopicRank()
    # input_text = u"""vmware tools plugins resolutionSet pe rubygem net ssh pe ruby stomp vmware tools vmmemctl common"""
    extractor.read_text(input_text)
    extractor.candidate_selection()
    extractor.candidate_weighting()
    keyphrases = extractor.get_n_best(n=1000, stemming=False)
    return keyphrases


def SingleRank_suggestions(input_text):
    extractor = pke.unsupervised.SingleRank()
    # input_text = u"""vmware tools plugins resolutionSet pe rubygem net ssh pe ruby stomp vmware tools vmmemctl common"""
    extractor.read_text(input_text)
    extractor.candidate_selection()
    extractor.candidate_weighting()
    keyphrases = extractor.get_n_best(n=50, stemming=False)
    return keyphrases


def TfIdf_suggestions(input_text):
    extractor = pke.unsupervised.TfIdf()
    # input_text = u"""vmware tools plugins resolutionSet pe rubygem net ssh pe ruby stomp vmware tools vmmemctl common"""
    extractor.read_text(input_text)
    extractor.candidate_selection()
    extractor.candidate_weighting()
    keyphrases = extractor.get_n_best(n=50, stemming=False)
    return keyphrases


'''Takes input data frame and returns a dictionary of counts of each class. Note: a comment can belong to more
than one class. eg. cit can pick ansible and another tool. it would have lass label as ansible and other
'''
def class_counter(df):
    
#     class counter dictionary
    class_counter_dict = {
        'ambivalent':0,
        'noise':0,
        'ans':0,
        'neg_ans':0,
        'neg_chef':0,
        'other':0,
        'chef':0
        }
    
    #   list containing words indacative of classes
    ambivalent = ['mixed', 'mixed,ansible', 'mixed-ansible']
    noise = ['Not-relevant', 'irr', 'non']
    ans = ['ansible', 'mixed,ansible', 'mixed-ansible', 'other, ansible', 'other,ansible']
    neg_ans = ['not-ansible', 'other,not-ansible']
    neg_chef = ['not-chef', 'other, not-chef']
    other = ['chef other', 'other', 'other, ansible', 'other, not-chef', 'other,ansible', 'other,chef', 'other,not-ansible']
    chef = ['chef', 'chef other', 'other,chef']
    
    for index, row in df.iterrows():
        if df.at[index, 'class'] in ambivalent:
            class_counter_dict['ambivalent'] += 1
        if df.at[index, 'class'] in noise:
            class_counter_dict['noise'] += 1
        if df.at[index, 'class'] in ans:
            class_counter_dict['ans'] += 1
        if df.at[index, 'class'] in neg_ans:
            class_counter_dict['neg_ans'] += 1
        if df.at[index, 'class'] in neg_chef:
            class_counter_dict['neg_chef'] += 1
        if df.at[index, 'class'] in other:
            class_counter_dict['other'] += 1
        if df.at[index, 'class'] in chef:
            class_counter_dict['chef'] += 1
            
    return class_counter_dict

def bar_plotter(D):
    plt.subplot()
    plt.xlabel('Classes')
    plt.ylabel('Scores')
    plt.title('Count of each class from the reddit data set')
    plt.bar(range(len(D)), D.values(), align='center')
    plt.xticks(range(len(D)), D.keys())
    plt.show()


def name_counter(df):
    ansib_cnt = 0
    chef_cnt = 0
    salt_cnt = 0
    puppet_cnt = 0
    ansib = "ansible"
    chef = "chef"
    salt = "salt"
    puppet = "puppet"
    
    comment_list = pd.read_csv(filepath)['comments'].tolist()
    for comment in comment_list:
        ansib_cnt+=len(re.findall(ansib, comment, re.IGNORECASE))
        chef_cnt+=len(re.findall(chef, comment, re.IGNORECASE))
        salt_cnt+=len(re.findall(salt, comment, re.IGNORECASE))
        puppet_cnt+=len(re.findall(puppet, comment, re.IGNORECASE))
    print "The Overall Counts are:"
    print "Ansible was used:", ansib_cnt
    print "Chef was used:", chef_cnt
    print "Salt was used:", salt_cnt
    print "Puppet was used:", puppet_cnt
    
def lang_pref(df):
    ans = ['ansible', 'mixed,ansible', 'mixed-ansible', 'other, ansible', 'other,ansible']
    neg_ans = ['not-ansible', 'other,not-ansible']
    neg_chef = ['not-chef', 'other, not-chef']
    chef = ['chef', 'chef other', 'other,chef']
    
    python_cnt_pos = 0
    ruby_cnt_pos = 0
    python_cnt_neg = 0
    ruby_cnt_neg = 0
    for index, row in df.iterrows():
        if df.at[index, 'class'] in ans or df.at[index, 'class'] in chef:
             if len(re.findall("python", df.at[index,"comments"], re.IGNORECASE))!=0:
                 python_cnt_pos+=1
             
             if len(re.findall("ruby", df.at[index,"comments"], re.IGNORECASE))!=0:
                 ruby_cnt_pos+=1
        elif df.at[index, 'class'] in neg_ans or df.at[index, 'class'] in neg_chef:
            if len(re.findall("python", df.at[index,"comments"], re.IGNORECASE))!=0:
                 python_cnt_neg+=1
             
            if len(re.findall("ruby", df.at[index,"comments"], re.IGNORECASE))!=0:
                 ruby_cnt_neg+=1
    return python_cnt_pos, ruby_cnt_pos, python_cnt_neg, ruby_cnt_neg
    
if __name__ == '__main__':
    filepath = '/home/atrivedi/eclipse-workspace/Visualization Application/server_code/reddit_ansible_vs_chef.csv'
#     comment_list = pd.read_csv(filepath)['comments'].tolist()
    df = pd.read_csv(filepath)
    name_counter(df)
    python_cnt_pos, ruby_cnt_pos, python_cnt_neg, ruby_cnt_neg = lang_pref(df)
    print "Python as a positive influencer is:", python_cnt_pos
    print "Ruby as a positive influencer is:", ruby_cnt_pos
    
    print "Python as a negative influencer is:", python_cnt_neg
    print "Ruby as a negative influencer is:", ruby_cnt_neg
    bar_plotter(class_counter(df))
    
    '''
    key_phrases = ""
    for comment in comment_list:
        if comment:
            input_text = ' '.join(re.split(' +', str(comment)))
            input_text = re.sub(r'[^\x00-\x7F]+',' ', input_text)
            s = ""
            for i in TfIdf_suggestions(input_text):
                s = s +  i[0] + ","
            print s
    print len(key_phrases)
    key_phrases = re.sub(r'[^\x00-\x7F]+',' ', key_phrases)
#     print TopicRank_suggestions(key_phrases)
    '''
