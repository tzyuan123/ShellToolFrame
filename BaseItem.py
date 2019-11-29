# -*- coding:utf-8 -*-

statusList = ["Waiting", "Running", "Done"]


class BaseItem(object):
    def __init__(self):
        self.itemName = ""
        self.itemRunStatus = 0  # 任务状态 0：等待   1：运行中   2：结束
        self.itemRunResult = 0  # 执行结果  0：未知   1：成功   2：失败

    def showItem(self, id=""):
        if id != "":
            # print("{:>4}. {:-<46} [{:^9}]".format(id, self.showItemName(), statusList[self.itemRunStatus]))
            id = '(' + str(id) + ').'
        print("{:>6} {:-<46} [{:^9}]".format(id, self.showItemName() + " ", statusList[self.itemRunStatus]))
        if (self.showItemMsg() != ""):
            print(" " * 7 + self.showItemMsg())

    def doWork(self):
        print('run doWork')
        raise Exception('please override this function')

    def showItemName(self):
        raise Exception('please override this function')

    def showItemMsg(self):
        raise Exception('please override this function')
