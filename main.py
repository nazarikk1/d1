class Counter:
    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1
        print(f"додав +1: {self.count}")

    def decrement(self):
        self.count -= 1
        print(f"відняв -1: {self.count}")

    def reset(self):
        self.count = 0
        print(f"ресет: {self.count}")

    def info(self):
        print(f"рахунок: {self.count}")


counter = Counter()
counter.info()
counter.increment()
counter.decrement()
counter.reset()
counter.info()