import BaseItem


class Item1(BaseItem.BaseItem):

    def doWork(self):
        print('run doWork')

    def showItemName(self):
        return  "run showItemName"

    def showItemMsg(self):
       return "run showItemMsg"