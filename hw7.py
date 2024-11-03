

class Volume:
    def __init__(self, vol=0):
        self._volume = max(0, min(11, vol))

    def __repr__(self):
        return f"Volume({self._volume})"

    def set(self, vol):
        self._volume = max(0, min(11, vol))

    def get(self):
        return self._volume

    def up(self, amount):
        self._volume = max(0, min(11, self._volume + amount))

    def down(self, amount):
        self._volume = max(0, min(11, self._volume - amount))

    def __eq__(self, other):
        if isinstance(other, Volume):
            return self._volume == other.get()
        return False

class Volume:
    def __init__(self, vol=0):
        self._volume = max(0, min(11, vol))

    def __repr__(self):
        if self._volume == 11:
            return "Volume(11)"
        return f"Volume({self._volume:.2f})"

    def set(self, vol):
        self._volume = max(0, min(11, vol))

    def get(self):
        return self._volume

    def up(self, amount):
        self._volume = max(0, min(11, self._volume + amount))

    def down(self, amount):
        self._volume = max(0, min(11, self._volume - amount))

    def __eq__(self, other):
        if isinstance(other, Volume):
            return self._volume == other.get()
        return False

def partyVolume(filename):
    with open(filename, 'r') as file:
        initial_volume = float(file.readline().strip())
        v = Volume(initial_volume)
        
        lines = file.readlines()
        for line in lines:
            action, amount = line.strip().split()
            amount = float(amount)
            if action == 'U':
                v.up(amount)
            elif action == 'D':
                v.down(amount)
    
    return v





if __name__ == '__main__':
    import doctest
    print(doctest.testfile('hw7TEST.py'))

    
