import BaseItem
import time
import random


class Item1(BaseItem.BaseItem):
    def __init__(self):
        super(Item1, self).__init__()

    def doWorkItem(self):
        t = random.randint(1, 10)
        i = 0
        for i in range(random.randint(1, 10)):
            time.sleep(1)
            self.setItemRunMsg('run %s s' % i)
        self.setItemRunMsg('finish in %s s' % i)

    def showItemName(self):
        return "this a Item Name"
