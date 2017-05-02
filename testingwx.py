import wx
from officialBrowser import MyWindow

class First(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self, None, wx.ID_ANY,'Video Browser',pos=(500,200), size = (650,500), style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
        print('inside')
        panel = wx.Panel(self)
        panel.SetBackgroundColour((255,153,153))
        staticText = wx.StaticText(panel,label="Enter Video Id",pos=(170,120))
        self.editText = wx.TextCtrl(panel,pos=(270,120))
        button=wx.Button(panel,pos=(250,170),label="submit")
        button.Bind(wx.EVT_BUTTON,self.fun)
        self.Show()

        
    def fun(self,event):
        print("video id is"+self.editText.GetValue())
        videoId = self.editText.GetValue()
        if videoId is None or videoId=="":
            return;
        print('showing1')
        #self.Hide()
        mw = MyWindow(videoId)
        mw.Show()
       # mw.play(videoId)
        
        
app=wx.App()
f = First()
app.MainLoop()

