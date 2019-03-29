import wx

class TextCtrlExampleFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, \
         "Text ctrl example", pos =(0,0), size =(800, 600))
        panel = wx.Panel(self, -1)

        #输入文本居中对齐
        text = wx.TextCtrl(panel, wx.ID_ANY,pos=(0,30), size =(200, 20), style = wx.TE_CENTER)

        #显示密码文本框
        text = wx.TextCtrl(panel, wx.ID_ANY, pos=(0,60), size =(200, 20), style = wx.TE_PASSWORD)

        #显示只读文本
        text = wx.TextCtrl(panel, wx.ID_ANY, pos=(0,90), size =(200, 20), style = wx.TE_READONLY)


def main():
    app = wx.PySimpleApp()
    frame = TextCtrlExampleFrame()
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()