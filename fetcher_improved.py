import requests
import json

#url_for_fetching_comments = '''https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=ViowcwfiWMU&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo&fields=items(snippet(topLevelComment(snippet(textOriginal))))'''
class Fetcher:
    def fetch(self,videoId):
        print("received "+str(videoId))
        str1="https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId="
        str2="&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo&fields=nextPageToken,items(snippet(topLevelComment(snippet(textOriginal))))&textFormat=plainText"
        url_for_multipage_comments_fetching = str1+str(videoId)+str2
        results = requests.get(url_for_multipage_comments_fetching)
        print(url_for_multipage_comments_fetching)
        json_data = json.loads(results.text)
        items = json_data['items']

        str3 = "https://www.googleapis.com/youtube/v3/videos?id="
        str4 = "&key=AIzaSyDMYdJcqDvNv985rJMheuR-bDfDg4FEsJo%20&part=statistics"

        url_for_commentCount = str3 + videoId + str4;
        results_comment = requests.get(url_for_commentCount)
        print(url_for_commentCount)
        json_comment = json.loads(results_comment.text)
        items_list = json_comment['items']
        items_count = items_list[0]['statistics']['commentCount']
        print('Number of comments'+items_count)
        comments = []
        count=0
        for item in items:
            comments.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])
#print(comments)

        try:
            while True:
                nextPageToken = json_data["nextPageToken"]
                new_url_for_multipage_comments_fetching = url_for_multipage_comments_fetching + '&pageToken=' + nextPageToken
                results = requests.get(new_url_for_multipage_comments_fetching)
                json_data = json.loads(results.text)
                items = json_data['items']
                for item in items:
                    comments.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])

        except:
            print('no nextpage')
            file = open(str(videoId)+".txt","w")
            comments=[comment.lower() for comment in comments]
            #comments = set(comments)
            #comments = list(comments)
            file.write(','.join(comments))
            file.close()
            print(comments)
            print(len(comments))
        else:
            print('fine')
    
    

f = Fetcher()
f.fetch('fRh_vgS2dFE')
    
#while()
