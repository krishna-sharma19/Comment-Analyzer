import tkinter
#from fetcher_improved import Fetcher
#from analyzer_classified import Analyzer

def qf(quichPrint):
    print(quickPrint)

window = tkinter.Tk()
window.geometry('1000x500')
window.title('Comment Analyzer')
window.wm_iconbitmap('favicon.ico')
window.configure(background = '#32d45c')

label = tkinter.Label(window, text = 'Enter the video id of the youtube video you want to see analysis for:', bg = '#32d45c',fg = '#441463')
label.config(font=("Courier", 15))
#label.place(x=30,y=20)
label.pack(pady = 30)

entry = tkinter.Entry(window,fg = '#9f1609')
entry.config(font = ("Helvetica",16))
#entry.place(height=30,width=60)
entry.pack(ipadx = 30,ipady = 5, pady = 10)

button = tkinter.Button(window, command = lambda: qf('parameters passed'), text = 'Submit', bg = '#a1dbcd',fg = '#800000')
button.config(font=("Courier", 15))
#button.place(x=50,y=100)
button.pack(pady = 20)

'''def click(self):
    print('fetcher called')
    #Fetcher.fetch(entry.get())
    print('analyzer called')
    #Analyzer.Analyze(entry.get())
'''
window.mainloop()


