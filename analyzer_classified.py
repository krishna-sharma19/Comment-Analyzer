import nltk
import requests
import re,operator
import json
from smiley_dict import smiley_dict


class Analyzer:
    def hasEnded(self):
        return self.ended
        
    def Analyze(self,filename):
        self.ended = False
        print(smiley_dict)
        
        file = open(filename+".txt","r")
        comments = file.read()
        comments = comments.split("***")
#print(comments)
        file_pos = open("positive-words.txt","r")
        file_neg = open("negative_words.rtf","r")
        pos_words = file_pos.read()
        neg_words = file_neg.read()

        pos_words = pos_words.split('\n')
        neg_words = neg_words.split("\\\n")
#        pos_words = pos_words.split(',')
        pos_smileys = []
        neg_smileys = []

        file_stopwords = open("stop_words.txt")
        stop_words = file_stopwords.read()
        stop_words = stop_words.split("*")
        stop_words = set(stop_words)
        #print(stop_words)
        comment_words=''
        newly_added_pos=[]
        pos = 0
        neg = 0
        neutral = 0
        '''url = 'https://www.googleapis.com/youtube/v3/videos?id='+filename+'&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo&part=snippet&fields=items(snippet(title,description))'
        results = requests.get(url)
        print(url)
        json_data = json.loads(results.text)
        title = json_data['items'][0]['snippet']['title']
        print('TITLE '+title)'''
        emojis = {}
        for comment in comments:
            flag=1
            spams = ["http\:","www\.","https\:","[\d][\d][\d][\d]"]#,title] #justin
            for spam in spams:
                chunk = spam+".*"
                if not re.search(chunk,comment)==None:
                    flag=0
                    
                if flag==0:
                    print("spam "+comment)
                    comments.remove(comment)
                    break

            if flag==0:
                continue
            
            '''all_emoji = re.compile(u'([\U00002600-\U000027BF]|[\U0001f300-\U0001f64F]|[\U0001f680-\U0001f6FF])')
            emos = set(all_emoji.findall(comment))
            for emo in emos:
                if emo in emojis.keys():
                    emojis[emo] = emojis[emo] + 1
                else:
                    emojis[emo] = 1
            '''
            #print("old comment "+comment)
            
            arr = re.split(u'([\U00002600-\U000027BF]+|[\U0001f300-\U0001f64F]+|[\U0001f680-\U0001f6FF]+)',comment)
            emoji_arr = []
            if len(arr)>1:
                emoji_arr = re.findall(u'([\U00002600-\U000027BF]+|[\U0001f300-\U0001f64F]+|[\U0001f680-\U0001f6FF]+)',comment)
                comment = ""
                for sent in arr:
                    if sent not in emoji_arr:
                        comment = comment+sent
                
            #print("new comment "+comment)
            comment_count_pos = 0
            comment_count_neg = 0

            comment_words = nltk.word_tokenize(comment)
            comment_set = set(comment_words)
            #print("comment was "+str(comment_set))
            comment_tokens = comment_set - stop_words
            #print("comment_tokens"+str(comment_tokens))
            for word in comment_words:
                word = word.lower()
                if word in pos_words:
                    comment_count_pos+=1
#                    print('\n\n\n'+word+'\n\n\n')
                elif word in neg_words:
                    comment_count_neg+=1
                else:
                    comment_set = set(comment_words)
                    #print("________________________________****"+str(comment_set))
                    remains_set = comment_set - stop_words
                    #print("________________________________********"+str(list(remains_set)))
            '''print("analysis for comment "+comment)
            print("pos = "+str(comment_count_pos))
            print("neg = "+str(comment_count_neg))
            '''
            if comment_count_pos>comment_count_neg:
                pos+=1
                #pos_words = pos_words+list(remains_set)
                #pos_smileys = pos_smileys + emoji_arr
                '''for emoji in emoji_arr:
                    arr = re.split(u'([\U00002600-\U000027BF]|[\U0001f300-\U0001f64F]|[\U0001f680-\U0001f6FF])',emoji)
                    for elem in arr:
                        if elem is not ' ':
                            pos_words.append(elem)'''
                print('pasitivee comment'+comment)
                
            elif comment_count_pos<comment_count_neg:
 #               neg_words = neg_words+list(remains_set)
#                newly_added_pos = newly_added_pos+list(remains_set)
                neg+=1
                print("negative comment "+comment)
            else:
                neutral+=1
                print("neutral------ comment "+comment)

        file_out = open('out'+filename,'w')
        file_out.write("\nTotal comments = "+str(len(comments)))
        file_out.write("\nTotal positive comments = "+str(pos))
        file_out.write("\nTotal negative comments = "+str(neg))
        file_out.write("\nTotal neutral/unassessed comments = "+str(neutral))
        file_out.write('\n'+str(pos*100/(pos+neg))+"% people found it useful")
        file_out.close()
        print("Total comments = "+str(len(comments)))
        #print("spam comments = ")
        print("Total positive comments = "+str(pos))
        print("Total negatiive comments = "+str(neg))
        print("Total neutral/unassessed comments = "+str(neutral))
        print(str(pos*100/(pos+neg))+"% found it useful")
        #print(stop_words)
        #pos_words=set(pos_words)
        #pos_words=list(pos_words)
        dict = {}
        pos_words = set(pos_words)
        pos_words = list(pos_words)
        for pos_word in pos_words:
            if pos_word in dict:
                dict[pos_word] = dict[pos_word]+1
            else:
                dict[pos_word] = 1
        #sorted = list(dict)
        sorted_pos = sorted(dict.items(), key=operator.itemgetter(1))
        #print(str(sorted_pos))
        #print(emojis)
        print(pos_smileys)
        file_stop = open("new_stop.txt","w")
        file_stop.write(",".join(stop_words))
        file_stop.close()
        file_pos = open("pos-words.txt","w")
        file_pos.write(",".join(pos_words))
        file_pos.close()

        file_neg = open("neg-words.txt","w")
        file_neg.write(",".join(neg_words))
        file_neg.close()
        self.ended = True


#a = Analyzer()
#a.Analyze('ncdLBvFIIco')

