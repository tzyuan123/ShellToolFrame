# -*- coding:utf-8 -*-

statusList = ["Waiting", "Running", "Done"]


class BaseItem(object):
    "'运行项目的父类，所有要运行的项目都必须继承自本类，并重写 doWorkItem， showItemName 2个方法"

    def __init__(self):
        self.itemName = ""
        self.itemRunStatus = 0  # 任务状态 0：等待   1：运行中   2：结束
        self.itemRunResult = 0  # 执行结果  0：未知   1：成功   2：失败
        self.itemRunMsg = None

    def getItemRunMsg(self):
        return self.itemRunMsg

    # 可以调用此方法，写入运行过程需要显示的界面信息，信息显示在项目名所在行的下一行
    def setItemRunMsg(self, msg):
        self.itemRunMsg = msg

    def showItem(self, id=""):
        if id != "":
            id = '(' + str(id) + ').'
        return "{:>6} {:-<46} [{:^9}]".format(id, self.showItemName() + " ", statusList[self.itemRunStatus])

    def showItemMsg(self):
        if (self.itemRunMsg != None and self.itemRunMsg != ""):
            return " " * 7 + self.getItemRunMsg()



    def doWork(self):
        self.itemRunStatus = 1
        self.doWorkItem()
        self.itemRunStatus = 2

    def doWorkItem(self):
        raise Exception('please override this function')

    def showItemName(self):
        raise Exception('please override this function')
