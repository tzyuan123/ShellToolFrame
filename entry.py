# -*- coding:utf-8 -*-
import time
import Item1
import sys
import os


class MainFrame(object):
    ''' shell Tool 主界面，用于提供界面展示和各步骤调用
    '''

    title = """
    ###########################################################
    #                                                         #
    #               Welcome to use shell Tool                 #
    #                                                         #
    ###########################################################
    """

    def __init__(self):
        self.title = MainFrame.title
        self.current_step = -1
        self.steplist = []

    def addSetp(self, item):
        self.steplist.append(item)

    def cleanScreen(self):
        cmd = "";
        if sys.platform == "win32":
            cmd = "cls"
        elif sys.platform == "linux2":
            cmd = "clear"
        else:
            cmd = "clear"
        os.system(cmd)

    def run(self):

        self.current_step = 0;

        while True:
            self.cleanScreen()
            print(self.title)
            index = 1
            for item in self.steplist:
                item.showItem(index)
                index += 1
            time.sleep(2)


mf = MainFrame()

mf.addSetp(Item1.Item1())
mf.addSetp(Item1.Item1())

mf.run()
