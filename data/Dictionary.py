##Nathan Hinton
##This will deal with the dictionaries

class Dictionary:
    def __init__(self, filepath, v = False):
        self.v = v
        self.filepath = filepath
        if self.v:print("loading dictionary file...")
        try:
            self.raw_file = open(self.filepath, 'r').read()
        except FileNotFoundError:
            print("dictionary file not found at %s"%self.filepath)
        if self.v:print("splitting file...")
        self.lines = self.raw_file.split('\n')
        if self.filepath != 'filteredDictionary.txt':
            if self.v:print("removing extra stuff...")
            self.words = []
            for line in self.lines:
                word = True
                if self.v:print(self.lines.index(line))
                if line[0] == '#':
                    word = False
                else:
                    for i in range(0, len(line)-2):
                        if line[i] == line[i+1] == line[i+2]:
                            word = False
                            break
                if word == True:
                    self.words.append(line)
        else:
            self.words = self.lines
        print('Dictionary loaded!')



# #Reconstruct dictionary file:
# text = ''
# for word in d.words:
#     text += '%s\n'%word
# open('filteredDictionary.txt', 'w').write(text)