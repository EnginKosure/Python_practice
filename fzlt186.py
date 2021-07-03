class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.all_listeners = set()

    def how_many(self, listeners):
        count = 0
        for folk in listeners:
            if folk.lower() not in self.all_listeners:
                count += 1
            self.all_listeners.add(folk.lower())
        return count
