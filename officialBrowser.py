import wx
import wx.html2
import sys
from redirect import RedirectText


class MyWindow(wx.Frame):
    def __init__(self, videoId, *args, **kwargs):
        app = wx.App()
        wx.Frame.__init__(self, None, wx.ID_ANY,'asd',(10, 20), (1000, 750))
        print('showing 2')
        panel = wx.Panel(self, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        url = "https://www.youtube.com/watch?v="+videoId
        browser = wx.html2.WebView.New(panel, wx.ID_ANY, url, (-50,-50), (665, 425))
        browser.LoadURL(url)
        sizer.Add(browser)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        txtCtrl = wx.TextCtrl(panel,wx.ID_ANY,pos=(600,10),size=(390,710))
        hbox.Add(txtCtrl)

        redir=RedirectText(txtCtrl)
        sys.stdout=redir
        self.Show()
        app.MainLoop()
