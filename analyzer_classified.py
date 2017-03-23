import nltk
import re,operator
class Analyzer:
    def Analyze(self,filename):
        
        file = open(filename+".txt","r")
        comments = file.read()
        comments = comments.split(",")
#print(comments)
        file_pos = open("positive-words.txt","r")
        file_neg = open("negative_words.rtf","r")
        pos_words = file_pos.read()
        neg_words = file_neg.read()

        pos_words = pos_words.split('\n')
        neg_words = neg_words.split("\\\n")

        file_stopwords = open("stop_words.txt")
        stop_words = file_stopwords.read()
        stop_words = stop_words.split("*")
        stop_words = set(stop_words)
        print(stop_words)
        comment_words=''
        newly_added_pos=[]
        pos = 0
        neg = 0
        neutral = 0
        for comment in comments:
            flag=1
            spams = ["http\:","www\.","https\:","justin"]
            for spam in spams:
                chunk = spam+".*"
                if not re.search(chunk,comment)==None:
                    flag=0
                    
            if flag==0:
                print("spam "+comment)
                continue
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
                pos_words = pos_words+list(remains_set)
                pos+=1
            elif comment_count_pos<comment_count_neg:
                neg_words = neg_words+list(remains_set)
                newly_added_pos = newly_added_pos+list(remains_set)
                neg+=1
                print("negative comment "+comment)
            else:
                neutral+=1
                print("neutral------ comment "+comment)
            
        print("Total comments = "+str(len(comments)))
        print("Total positive comments = "+str(pos))
        print("Total negatiive comments = "+str(neg))
        print("Total neutral/unassessed comments = "+str(neutral))
        print(str(pos*100/(pos+neg))+"% found it useful")
        #print(stop_words)
        #pos_words=set(pos_words)
        #pos_words=list(pos_words)
        dict = {}
        for pos_word in pos_words:
            if pos_word in dict:
                dict[pos_word] = dict[pos_word]+1
            else:
                dict[pos_word] = 1
        #sorted = list(dict)
        sorted_pos = sorted(dict.items(), key=operator.itemgetter(1))
        print(str(sorted_pos))
        file_stop = open("new_stop.txt","w")
        file_stop.write(",".join(stop_words))
        file_stop.close()
        file_pos = open("pos-words.txt","w")
        file_pos.write(",".join(pos_words))
        file_pos.close()

        file_neg = open("neg-words.txt","w")
        file_neg.write(",".join(neg_words))
        file_neg.close()


#a = Analyzer()
#a.Analyze('shape')
