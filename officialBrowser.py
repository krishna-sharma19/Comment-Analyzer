import wx
import wx.html2
import sys
import threading
from fetcher_improved import Fetcher
#from fetcher_new import Fetcher

from analyzer_classified import Analyzer
import time
#from logger import Form1



class MyWindow(wx.Frame):
    def __init__(self, videoId, *args, **kwargs):
        self.fet = Fetcher()
        self.ana = Analyzer()
        app = wx.App()
        wx.Frame.__init__(self, None, wx.ID_ANY,'Running Analyzer',(10, 20), (1000, 750))
        print('showing 2')
        panel = wx.Panel(self, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        url = "https://www.youtube.com/watch?v="+videoId
        self.videoId = videoId
        browser = wx.html2.WebView.New(panel, wx.ID_ANY, url, (-40,-50), (665, 425))
        browser.LoadURL(url)
        sizer.Add(browser)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.txtCtrl = wx.TextCtrl(panel,wx.ID_ANY,pos=(600,10),size=(390,710),style=wx.TE_MULTILINE)
        hbox.Add(self.txtCtrl)
        self.Show()        
        self.start(self.fet.fetch,videoId)
        self.total = self.fet.get_total_comments(videoId)
        print('totali'+str(self.total))
        st = wx.StaticText(panel,size=(50,50),pos=(10,420))
        st.SetLabel('Fetching Comments')
        sizer.Add(st)
        
        self.gauge = wx.Gauge(panel, range = self.total, size = (550, 25), style = wx.GA_HORIZONTAL,pos=(10,450))
        sizer.Add(self.gauge)

        self.start(self.do_new_stuff)
        #self.write(filename = videoId)
        #self.
        
        app.MainLoop()

    
    def do_new_stuff(self):
        time.sleep(1)
        count = 0 
        while count<self.total:
            count = self.fet.get_counter()
            print('count is'+str(count))
            self.gauge.SetValue(count)
            time.sleep(1.5)
        self.callAnalyze()    
        return

    def callAnalyze(self):
        self.start(self.ana.Analyze,(self.videoId))
        self.start(self.CheckForEnd)
        self.write(self.videoId)
        #print('analyzing complete')
        #self.showDialog()
        return

    def CheckForEnd(self):
        hasEnded = False
        while not hasEnded:
            hasEnded = self.ana.hasEnded()
            if hasEnded:
                self.showDialog()
                break
        return
            
    def showDialog(self):
        '''st = wx.StaticText(panel,size=(50,50),pos=(10,480))
        file = open('out'+self.videoId,'r')
        result = file.read()
        st.SetLabel('ANALYSIS'+result)

        
        sizer.Add(st)'''

        file = open('out'+self.videoId,'r')
        result = file.read()
        wx.MessageBox("Results"+result, "Analysis" ,wx.OK | wx.ICON_INFORMATION)

    def startSelf(self,func,*args):
        thread = threading.Thread(target=func, args=args)
        thread.setDaemon(True)
        thread.start()

        

    def start(self,func, *args): # helper method to run a function in another thread             
        thread = threading.Thread(target=func, args=args)
        thread.setDaemon(True)
        thread.start()

    def write(self,filename):
        file = open(filename+'.txt','r')
        comments = file.read()
        comments = comments.split('***')
        for comment in comments:
#           print('printing')
            wx.CallAfter(self.txtCtrl.AppendText,(comment+"\n"))
            wx.Yield()
            time.sleep(0.0001)


