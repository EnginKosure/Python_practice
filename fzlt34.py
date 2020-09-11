# daily-python-challenge
# This is an interview question asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class Log:
    def __init__(self, N):
        self.N = N
        self.log = []

    def record(self, order_id):
        if len(self.log) < self.N:
            self.log.append(order_id)
        else:
            self.log.pop(0)
            self.log.append(order_id)

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
a.record(21)
a.record(22)
a.record(23)
a.record(24)


print(a.get_last(3))
