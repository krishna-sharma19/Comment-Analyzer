import wx
import sys

# Set up a panel within a frame with a load of widgets
# Set up events on each of the widgets
# display the results in a scrolling text frame

class logging:
        def __init__(self):
                self.starts = ""
                self.ends = ""
        def setstart(self,place):
                self.starts = place
        def setend(self,place):
                self.ends = place
        def __str__(self):
                return "from "+self.starts+ " to "+self.ends

class Form1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Set up some basic element. Placement is a bit crude as this
        # is really an event handling demo! It would also be a good idea
        # to define constants for the IDs!
        file = open('justin1.txt','r')
        comments = file.read()
        print(comments)
        self.logger = wx.TextCtrl(self,5, comments,wx.Point(30,20), wx.Size(200,300),wx.TE_MULTILINE |  wx.TE_READONLY)

going = logging()
app = wx.App()

frame = wx.Frame(None, size=(550,425)) # top level window
# We have only had to set the size because the simple layout used
# hasn't allowed for an automatic sizing.

Form1(frame) # A panel in the frame
frame.Show()
app.MainLoop()

