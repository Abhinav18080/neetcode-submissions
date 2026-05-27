class PrefixTree:

    def __init__(self):
        self.storewords = []
        

    def insert(self, word: str) -> None:
        if word not in self.storewords:
            self.storewords.append(word)

    def search(self, word: str) -> bool:
        if word in self.storewords:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for i in self.storewords:
            if i.startswith(prefix):
                return True
        return False
        