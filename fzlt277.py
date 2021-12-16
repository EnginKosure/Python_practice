def load(self):
    self.tracks = []
    print("Loading tracks from CSV file.")
    file = open(self.filename, "r")
    for line in file:
        fields = line.split(";")
        track = Track(fields[0], fields[1], int(fields[2]))
        self.tracks.append(track)
    file.close()


def save(self):
    print("Saving your playlist...")
    file = open(self.filename, "w")
    for track in self.tracks:
        file.write(track.title + ";" + track.artist +
                   ";" + str(track.duration) + ";")
    file.close()
    print("Playlist saved!")
