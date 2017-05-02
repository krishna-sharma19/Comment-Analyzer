import requests
import json

#url_for_fetching_comments = '''https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ViowcwfiWMU&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo&fields=items(snippet(topLevelComment(snippet(textOriginal))))'''
class Fetcher:
    def __init__(self):
        self.count = 0
        self.Total_comments = 0
        self.flag = True 
        
    def get_counter(self):
        return self.count

    def get_total_comments(self,videoId):
        if self.flag:
            str3 = "https://www.googleapis.com/youtube/v3/videos?id="
            str4 = "&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo%20&part=statistics&fields=items(statistics(commentCount))"
            url_for_comment_count = str3 + videoId + str4;
            results_comment = requests.get(url_for_comment_count)
            print(url_for_comment_count)
            json_comment = json.loads(results_comment.text)
            comment_count = int(json_comment['items'][0]['statistics']['commentCount'])
            print('Number of comments'+str(comment_count))
            self.Total_comments = comment_count

        return self.Total_comments

    
        
        
        
    def fetch(self,videoId):#,custom_self.count=0):
        #print(self.count)
        comment_count = self.get_total_comments(videoId)
        print("received "+str(videoId))
        str1="https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId="
        str2="&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo&fields=nextPageToken,items(snippet(topLevelComment(snippet(textOriginal))))&textFormat=plainText"
        url_for_multipage_comments_fetching = str1+str(videoId)+str2
        results = requests.get(url_for_multipage_comments_fetching)
        print(url_for_multipage_comments_fetching)
        json_data = json.loads(results.text)
        items = json_data['items']
        self.comments = []
        self.count=0

        while True:
            print('inside loop comments fetched = '+str(self.count))
            for item in items:
                    self.comments.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])
            if self.count<comment_count:
                self.count = self.count + 20
            if comment_count - self.count < 20:
                self.count = self.count + 20
                break
            if 'nextPageToken' in json_data.keys():
                nextPageToken = json_data["nextPageToken"]
            else:
                nextPageToken = ""
                
            new_url_for_multipage_comments_fetching = url_for_multipage_comments_fetching + '&pageToken=' + nextPageToken
            results = requests.get(new_url_for_multipage_comments_fetching)
            json_data = json.loads(results.text)
            items = json_data['items']
            
                
                
#        print('no nextpage')
        file = open(str(videoId)+".txt","w")
        self.comments=[comment.lower() for comment in self.comments]
        file.write('***'.join(self.comments))
        file.close()
        print(self.comments)
        print(len(self.comments))
                                        
    

'''f = Fetcher()
f.fetch('RhU9MZ98jxo')
'''    
#while()
