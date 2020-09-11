# daily-python-challenge
# This is an interview question asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class Log:
    def __init__(self, size):
        self.size = size
        self.log = []
        self.ind = 0

    def record(self, order_id):
        self.ind = (self.ind) % self.size
        if len(self.log) < self.size:
            self.log.append(order_id)
        else:
            self.log[self.ind] = order_id

    def get_last(self, i):
        print(self.log)
        return self.log[-i]


a = Log(10)
a.record(1)
a.record(2)
a.record(10)
a.record(11)
a.record(12)
a.record(14)
a.record(120)
a.record(19)
a.record(18)
a.record(17)
a.record(16)
a.record(15)

print(a.get_last(3))
