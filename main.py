# -*- coding: utf-8 -*-
import wx
import poem_quiz, Poem_utils

# 题面内容
Question_1 = 'Hello'
Question_2 = 'Hello'
Question_3_1 = 'Hello'
Question_3_2 = 'Hello'

# 答案
Answer_1 = 'Hello'
Answer_2 = 'Hello'
Answer_3 = 'Hello'

# 选项列表
radioList_1 = []
radioList_2 = []

# 总题数
Number_1 = 5
Number_2 = 5
Number_3 = 5

# 已选题
Done_1 = []
Done_2 = []
Done_3 = []

# 是否点击选项
Flag_1 = False
Flag_2 = False

# 总分
Score_1 = 0
Score_2 = 0
Score_3 = 0

# 当前题目序号
Count_1 = 1
Count_2 = 1
Count_3 = 1

# 当前选中答案
ans_1 = 0
ans_2 = 0
ans_3 = 0

enter_content = ''



###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        global Score_1
        global Question_1
        global Answer_1
        global radioList_1
        global ans_1
        global Number_1
        global Flag_1
        global Path
        global Done_1

        global Score_2
        global Question_2
        global Answer_2
        global radioList_2
        global ans_2
        global Number_2
        global Flag_2
        global Done_2

        global Score_3
        global Question_3_1
        global Question_3_2
        global Answer_3
        global ans_3
        global Number_3
        global Done_2

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"鹿鸣诗词大荟", pos=wx.DefaultPosition, size=(1024, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # wx.Frame.SetMaxSize((650, 650))

        # self.SetSizeHintsSz((650, 650))
        self.SetMaxSize((1024, 800))
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0)
        ###########################################################################
        ## Part 0
        ###########################################################################
        self.m_panel7 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel7.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground0)

        self.m_notebook1.AddPage(self.m_panel7, u"首页", True)
        self.m_notebook1.SetFont(wx.Font(18, 70, 90, 90, False, "楷体"))
        ###########################################################################
        ## Part 1
        ###########################################################################

        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel1.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.quote = wx.StaticText(self.m_panel1, wx.ID_ANY, u"当前第 %d 首.\n" % (Count_1), wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.quote.Wrap(-1)
        self.quote.SetFont(wx.Font(22, 70, 90, 90, False, "楷体"))
        self.quote.SetOwnForegroundColour('red')
        bSizer2.Add(self.quote, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        rd, title, author, content = poem_quiz.get_poem()
        Done_1.append(rd)
        self.quote_ = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\n%s\n%s\n\n%s" % (title, author, content), (512, 100),
                                    (800, 500), wx.ALIGN_CENTER)
        self.quote_.Wrap(-1)
        self.quote_.SetFont(wx.Font(20, 70, 90, 90, False, "楷体"))
        self.quote_.SetOwnForegroundColour('black')
        bSizer2.Add(self.quote_, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button_reset = wx.Button(self.m_panel1, wx.ID_ANY, u"再来一首", pos=(512, 550), size=(160, 60))
        self.button_reset.SetFont(wx.Font(20, 70, 90, 90, False, "楷体"))
        bSizer2.Add(self.button_reset, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick_reset, self.button_reset)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        self.m_notebook1.AddPage(self.m_panel1, u"诗词一首", False)
        self.Centre(wx.BOTH)

        ###########################################################################
        ## Part 2
        ###########################################################################
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground2)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.quote2 = wx.StaticText(self.m_panel2, wx.ID_ANY,
                                    u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n\n" % (Number_2, Count_2, 0, 0),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.quote2.Wrap(-1)
        bSizer4.Add(self.quote2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.quote2.SetFont(wx.Font(22, 70, 90, 90, False, "楷体"))
        self.quote2.SetOwnForegroundColour('blue')
        # Question_2, radioList_2, Answer_2 = test_01.create_quiz(dict_2_Path, 2)
        sentence, Question_2, radioList_2, Answer_2 = poem_quiz.get_poem_words()
        Done_2.append(sentence)
        self.rb2 = wx.RadioBox(self.m_panel2, wx.ID_ANY, Question_2, wx.DefaultPosition, wx.DefaultSize,
                               radioList_2, 1, wx.RA_SPECIFY_COLS)
        self.rb2.SetSelection(0)
        self.rb2.SetMinSize(wx.Size(800, -1))
        bSizer4.Add(self.rb2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.rb2.SetFont(wx.Font(22, 70, 90, 90, False, "楷体"))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox_2, self.rb2)

        self.button2 = wx.Button(self.m_panel2, wx.ID_ANY, u"下一题", wx.DefaultPosition, (200, 50), 0)
        self.button2.SetFont(wx.Font(20, 70, 90, 90, False, "楷体"))
        bSizer4.Add(self.button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick_2, self.button2)

        self.button2_reset = wx.Button(self.m_panel2, wx.ID_ANY, u"重新开始", wx.DefaultPosition, (200, 50), 0)
        self.button2_reset.SetFont(wx.Font(20, 70, 90, 90, False, "楷体"))
        bSizer4.Add(self.button2_reset, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_reset, self.button2_reset)

        self.m_panel2.SetSizer(bSizer4)
        self.m_panel2.Layout()
        bSizer4.Fit(self.m_panel2)
        self.m_notebook1.AddPage(self.m_panel2, u"空字选择", False)

        ###########################################################################
        ## Part 3
        ###########################################################################
        self.m_panel3 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground3)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.quote3 = wx.StaticText(self.m_panel3, wx.ID_ANY,
                                    u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n\n" % (Number_3, Count_3, 0, 0),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.quote3.Wrap(-1)
        self.quote3.SetOwnForegroundColour('blue')
        bSizer3.Add(self.quote3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.quote3.SetFont(wx.Font(22, 70, 90, 90, False, "楷体"))

        self.br = wx.StaticText(self.m_panel3, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0)
        # 空行
        bSizer3.Add(self.br, 0, wx.ALL, 5)

        # Question_3_1, Question_3_2, Answer_3 = test_03.create_quiz_03()
        sentence, Question_3_2, Answer_3 = poem_quiz.get_sentence()
        Done_3.append(sentence)

        self.english = wx.StaticText(self.m_panel3, wx.ID_ANY, u"%s\n\n" % Question_3_2, wx.DefaultPosition,
                                     wx.DefaultSize, wx.ALIGN_CENTER)
        self.english.Wrap(-1)
        self.english.SetFont(wx.Font(22, 70, 90, 90, False, "楷体"))
        bSizer3.Add(self.english, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER, 5)
        # self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (200, 50), 0
        self.enter = wx.TextCtrl(self.m_panel3, wx.ID_ANY,wx.EmptyString,(512, 400),(600, 50),0)
        # self.enter = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, (512,400),(600,50),wx.ALIGN_CENTER|wx.TE_PROCESS_ENTER)
        self.enter.SetFont(wx.Font(22, 70, 90, 90, False, "楷体"))
        bSizer3.Add(self.enter, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Bind(wx.EVT_TEXT, self.EvtText, self.enter)

        self.button3 = wx.Button(self.m_panel3, wx.ID_ANY, u"下一题", (512, 800), (200, 50), 0)
        self.button3.SetFont(wx.Font(20, 70, 90, 90, False, "楷体"))

        bSizer3.Add(self.button3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick_3, self.button3)

        self.m_panel3.SetSizer(bSizer3)
        self.m_panel3.Layout()
        bSizer3.Fit(self.m_panel3)
        self.m_notebook1.AddPage(self.m_panel3, u"古诗填空", False)

        bSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    # 英译中单选操作
    def EvtRadioBox_1(self, event):
        global radioList_1
        global Answer_1
        global ans_1
        global Flag_1
        Flag_1 = True
        ans = event.GetInt()
        # self.logger.AppendText('EvtRadioBox: %s\n' %radioList_1[ans])
        if radioList_1[ans] == Answer_1:
            # self.logger.AppendText('Correct!\n' )
            ans_1 = 1

        else:
            # self.logger.AppendText('错误!\n')
            ans_1 = 0

    # 中译英单选操作
    def EvtRadioBox_2(self, event):
        global radioList_2
        global Answer_2
        global ans_2
        global Flag_2
        Flag_2 = True
        ans = event.GetInt()
        # self.logger.AppendText('EvtRadioBox: %s\n' %radioList_1[ans])
        if radioList_2[ans] == Answer_2:
            # self.logger.AppendText('Correct!\n' )
            ans_2 = 1
        else:
            # self.logger.AppendText('错误!\n')
            ans_2 = 0
        # Flag_2=False

    def EvtText(self, event):
        global enter_content
        enter_content = event.GetString()
        # print (enter_content)

    def OnClick_1(self, event):
        global Count_1
        global Score_1
        global Question_1
        global Answer_1
        global ans_1
        global radioList_1
        global Done_1
        global Number_1
        global Flag_1
        if Flag_1 == False:
            if radioList_1[0] == Answer_1:
                # self.logger.AppendText('Correct!\n' )
                ans_1 = 1
            else:
                ans_1 = 0
        if Count_1 <= Number_1 + 1:
            Score_1 += ans_1
        ans_1 = 0
        Flag_1 = False
        # self.logger.AppendText("You have gotten %d point\n" % Score_1)
        Count_1 += 1
        if (Count_1 <= Number_1):
            self.quote.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n" % (Number_1, Count_1, Score_1, Count_1 - 1 - Score_1))
            self.button.SetLabel('下一题')

            Question_1, radioList_1, Answer_1 = test_01.create_quiz(dict_1_Path, 1)
            while (Answer_1 in Done_1):
                Question_1, radioList_1, Answer_1 = test_01.create_quiz(dict_1_Path, 1)
            Done_1.append(Answer_1)
            self.rb.SetLabel(Question_1)
            for i in range(len(radioList_1)):
                self.rb.SetString(i, radioList_1[i])
            self.rb.SetSelection(0)
            self.rb.Refresh()
            self.rb.Update()

            self.m_panel1.Refresh()
            self.m_panel1.Update()
        elif Count_1 == Number_1 + 1:
            self.quote.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n" % (Number_1, Count_1 - 1, Score_1, Count_1 - 1 - Score_1))
            self.rb.Disable()
            self.m_panel1.Refresh()
            self.m_panel1.Update()
            Count_1 += 5
            self.button.SetLabel('尝试更多!')
        else:
            self.rb.Enable()
            # self.quit.Show()
            Count_1 = Number_1 + 1
            Number_1 += 5
            self.quote.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n" % (Number_1, Count_1, Score_1, Count_1 - 1 - Score_1))
            self.button.SetLabel('下一题')

            Question_1, radioList_1, Answer_1 = test_01.create_quiz(dict_1_Path, 1)
            while (Answer_1 in Done_1):
                Question_1, radioList_1, Answer_1 = test_01.create_quiz(dict_1_Path, 1)
            Done_1.append(Answer_1)
            self.rb.SetLabel(Question_1)
            for i in range(len(radioList_1)):
                self.rb.SetString(i, radioList_1[i])
            self.rb.SetSelection(0)
            self.rb.Refresh()
            self.rb.Update()

            self.m_panel1.Refresh()
            self.m_panel1.Update()

    def OnClick_2(self, event):
        global Count_2
        global Score_2
        global Question_2
        global Answer_2
        global ans_2
        global radioList_2
        global Done_2
        global Number_2
        global Flag_2
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',radioList_2, Answer_2)
        if Flag_2 == False:
            if radioList_2[0] == Answer_2:
                # self.logger.AppendText('Correct!\n' )
                ans_2 = 1
            else:
                ans_2 = 0
        if Count_2 <= Number_2 + 1:
            Score_2 += ans_2
        ans_2 = 0
        Flag_2 = False
        # self.logger.AppendText("You have gotten %d point\n" % Score_1)
        Count_2 += 1
        if (Count_2 <= Number_2):
            self.quote2.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n" % (Number_2, Count_2, Score_2, Count_2 - 1 - Score_2))
            self.button2.SetLabel('下一题')
            # Question_2, radioList_2, Answer_2 = test_01.create_quiz(dict_2_Path,2)
            sentence, Question_2, radioList_2, Answer_2 = poem_quiz.get_poem_words()
            while (sentence in Done_2):
                sentence, Question_2, radioList_2, Answer_2 = poem_quiz.get_poem_words()
            Done_2.append(sentence)
            self.rb2.SetLabel(Question_2)
            for i in range(len(radioList_2)):
                self.rb2.SetString(i, radioList_2[i])
            self.rb2.SetSelection(0)
            self.rb2.Refresh()
            self.rb2.Update()

            self.m_panel2.Refresh()
            self.m_panel2.Update()
        elif Count_2 == Number_2 + 1:
            self.quote2.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n" % (Number_2, Count_2 - 1, Score_2, Count_2 - 1 - Score_2))
            self.rb2.Disable()
            self.m_panel2.Refresh()
            self.m_panel2.Update()
            Count_2 += 1
            self.button2.SetLabel('尝试更多!')
        else:

            self.rb2.Enable()
            # self.quit.Show()
            Count_2 = Number_2 + 1
            Number_2 += 5
            self.quote2.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n" % (Number_2, Count_2, Score_2, Count_2 - 1 - Score_2))
            self.button2.SetLabel('下一题')

            # Question_2, radioList_2, Answer_2 = test_01.create_quiz(dict_2_Path,2)
            sentence, Question_2, radioList_2, Answer_2 = poem_quiz.get_poem_words()
            while (sentence in Done_2):
                # Question_2, radioList_2, Answer_2 = test_01.create_quiz(dict_2_Path,2)
                sentence, Question_2, radioList_2, Answer_2 = poem_quiz.get_poem_words()
            Done_2.append(sentence)
            self.rb2.SetLabel(Question_2)
            for i in range(len(radioList_2)):
                self.rb2.SetString(i, radioList_2[i])
            self.rb2.SetSelection(0)
            self.rb2.Refresh()
            self.rb2.Update()
            self.m_panel2.Refresh()
            self.m_panel2.Update()

    def OnClick_3(self, event):
        global ans_3
        global Answer_3
        global Count_3
        global Number_3
        global Score_3
        global enter_content

        if enter_content == Answer_3:
            ans_3 = 1
        else:
            ans_3 = 0
        if Count_3 <= Number_3 + 1:
            Score_3 += ans_3

        ans_3 = 0
        enter_content = ''
        # self.logger.AppendText("You have gotten %d point\n" % Score_1)
        Count_3 += 1
        if (Count_3 <= Number_3):
            self.quote3.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n\n" % (Number_3, Count_3, Score_3, Count_3 - 1 - Score_3))
            self.button3.SetLabel('下一题')

            # chinese, english_, Answer_3 = test_03.create_quiz_03()
            sentence, english_, Answer_3 = poem_quiz.get_sentence()
            while (sentence in Done_3):
                # chinese, english_, Answer_3 = test_03.create_quiz_03()
                sentence, english_, Answer_3 = poem_quiz.get_sentence()
            Done_3.append(sentence)

            # self.chinese.SetLabel("中文: "+chinese)
            self.english.SetLabel(english_)
            self.enter.SetLabel('')

            self.m_panel3.Refresh()
            self.m_panel3.Update()

        elif Count_3 == Number_3 + 1:
            self.quote3.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n\n" % (Number_3, Count_3 - 1, Score_3, Count_3 - 1 - Score_3))
            self.enter.Disable()
            self.m_panel3.Refresh()
            self.m_panel3.Update()
            Count_3 += 1
            self.button3.SetLabel('尝试更多!')
        else:
            self.enter.Enable()
            # self.quit.Show()
            Count_3 = Number_3 + 1
            Number_3 += 5

            self.quote3.SetLabel(
                u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n\n" % (Number_3, Count_3, Score_3, Count_3 - 1 - Score_3))
            self.button3.SetLabel('下一题')

            # chinese, english_, Answer_3 = test_03.create_quiz_03()
            chinese, english_, Answer_3 = poem_quiz.get_sentence()
            while (chinese in Done_3):
                # chinese, english_, Answer_3 = test_03.create_quiz_03()
                chinese, english_, Answer_3 = poem_quiz.get_sentence()
            Done_3.append(chinese)

            # self.chinese.SetLabel("中文: " + chinese)
            self.english.SetLabel(english_)
            self.enter.SetLabel('')

            self.m_panel3.Refresh()
            self.m_panel3.Update()

    def OnClick_reset(self, event):
        global Done_1
        global Count_1

        # Question_1, radioList_1, Answer_1 = test_01.create_quiz(dict_1_Path, 1)
        rd, title, author, content = poem_quiz.get_poem()
        if len(Done_1) < 1001:
            while rd in Done_1:
                rd, title, author, content = poem_quiz.get_poem()
            Count_1 += 1
            self.quote_.SetLabel(u"\n%s\n%s\n\n%s" % (title, author, content))
            Done_1.append(rd)
        else:
            self.quote_.SetLabel(u"诗库已空！江湖再见！")
        self.quote.SetLabel(u"当前第 %d 首.\n" % (Count_1))
        self.m_panel1.Refresh()
        self.m_panel1.Update()

    def OnClick_2_reset(self, event):
        global Question_2
        global Answer_2
        global Done_2
        global Score_2
        global Count_2
        global Number_2
        global Flag_2
        global ans_2
        global radioList_2

        Number_2 = 5
        Score_2 = 0
        Count_2 = 1
        Flag_2 = False
        Done_2 = []
        self.quote2.SetLabel(u"共 %d 题，当前第 %d 题.\n 正确: %d 错误: %d\n\n" % (Number_2, Count_2, 0, 0))
        # Question_2, radioList_2, Answer_2 = test_01.create_quiz(dict_2_Path, 2)
        sentence, Question_2, radioList_2, Answer_2 = poem_quiz.get_poem_words()
        Done_2.append(sentence)
        self.rb2.SetLabel(Question_2)
        for i in range(len(radioList_2)):
            self.rb2.SetString(i, radioList_2[i])

        self.rb2.SetSelection(0)
        self.rb2.Refresh()
        self.rb2.Update()
        self.rb2.Enable()

        self.button2.SetLabel(u'下一题')
        self.m_panel2.Refresh()
        self.m_panel2.Update()

    def OnEraseBackground(self, evt):
        """
        设置背景的方法
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("bg.png")

        dc.DrawBitmap(bmp, 0, 550)

    def OnEraseBackground0(self, evt):
        """
        设置背景的方法
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("bg1.jpg")

        dc.DrawBitmap(bmp, 0, 0)

    def OnEraseBackground2(self, evt):
        """
        设置背景的方法
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("bg.png")

        dc.DrawBitmap(bmp, 0, 450)

    def OnEraseBackground3(self, evt):
        """
        设置背景的方法
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("bg.png")

        dc.DrawBitmap(bmp, 0, 450)


app = wx.App(0)
frame = wx.Frame(None, -1)
frame.Center()
frame = MyFrame1(frame)
frame.Show()
app.MainLoop()
