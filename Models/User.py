import csv

import config

class User():

    _id = 0
    name = ""
    rep = 0
    rank = 0
    storage = []

    def __init__(self, name, rep=0):
        self.name = name
        self.rep = rep

        self._setup()


    def _setup(self):
        self._load_data()
        index, data = self._get_user_data()
        if not data:
            self.storage.append(self.get_data())
            self._id = len(self.storage) -1
            self._store_data()
            return

        self._id = index
        self.rep = int(data[1])
        self.rank = int(data[2])


    def get_data(self):
        return [self.name,
                self.rep,
                self.rank]


    def update_rank(self):
        rank = config.RANKS
        i = 0
        new_rank = 0
        for r in rank:
            if self.rep >= r[0]:
                new_rank = i
            i += 1

        self.rank = new_rank


    def add_rep(self,rep=1):
        self.rep += int(rep)
        self.update_rank()
        self.storage[self._id] = self.get_data()
        self._store_data()
        return rep

    def remove_rep(self,rep=1):
        self.rep -= int(rep)
        self.update_rank()
        self.storage[self._id] = self.get_data()
        self._store_data()
        return rep

    def _get_user_data(self):
        users = [u[0] for u in self.storage]
        try:
            match = users.index(self.name)
            return match, self.storage[match]
        except ValueError:
            return (False,False)


    def _load_data(self):
        with open(config.CSV_FILE, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.storage = list(reader)


    def _store_data(self):
        with open(config.CSV_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.storage)
