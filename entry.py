# -*- coding:utf-8 -*-
import time
import Item1
import sys
import os
import threading

Show_flush_Time = 2


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
        self.steplist = []
        self.showStatus = 0  # 界面显示的状态标识， 0 不显示， 1 正常显示

    # 增加需要操作的项目，项目要求继承自BaseItem 类
    def addSetp(self, item):
        self.steplist.append(item)

    # 清除屏幕显示
    def cleanScreen(self):
        cmd = "";
        if sys.platform == "win32":
            cmd = "cls"
        elif sys.platform == "linux2":
            cmd = "clear"
        else:
            cmd = "clear"
        os.system(cmd)

    # 显示界面信息（在独立的子线程运行）
    def showFrame(self):
        while self.showStatus == 1:
            self.cleanScreen()
            print(self.title)
            index = 1
            for item in self.steplist:
                print(item.showItem(index))
                if item.showItemMsg() != None:
                    print(item.showItemMsg())
                index += 1
            time.sleep(Show_flush_Time)

    # 逐个执行项目（在独立的子线程运行）
    def doWork(self):
        for item in self.steplist:
            item.doWork()
        time.sleep(Show_flush_Time + 2)
        self.showStatus = 0

    # 运行整个框架， 运行过程中会启动2个线程，分别为显示线程和工作线程
    def run(self):
        self.showStatus = 1
        show = threading.Thread(target=self.showFrame)
        show.start()

        work = threading.Thread(target=self.doWork)
        work.start()
        show.join()


if __name__ == '__main__':
    mf = MainFrame()

    # 此处添加需要操作的项目，项目要求继承自BaseItem 类
    mf.addSetp(Item1.Item1())
    mf.addSetp(Item1.Item1())

    # 运行
    mf.run()
