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
        self.current_Index = 0

    def record(self, order_id):
        self.log[self.current_Index] = order_id
        self.current_Index = (self.current_Index+1) % self.size

    def get_last(self, i):
        return self.log[(self.current_Index-i+self.size) % self.size]
