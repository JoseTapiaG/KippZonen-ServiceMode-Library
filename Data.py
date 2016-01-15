class Data:
    # Estructure of a registry in SDCard
    # e.g: 2015-12-13 23:10:03   0.011   0.079   0.45
    def __init__(self, date, time, data1, data2, data3):
        self.date = date
        self.time = time
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
