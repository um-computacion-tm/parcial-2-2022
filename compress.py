class Compress:

    def compress(self, text: str):
        values = {}
        compressed = []
        words = text.split(' ')
        counter = 0
        for word in words:
            if not word in values:
                counter += 1
                values[word] = counter
            compressed.append(values[word])
        return compressed, values

    def uncompress(self, compressed: list, values: dict):
        unvalues = {}
        for value in values:
            unvalues[values[value]] = value
        text = ""
        for value in compressed:
            text += unvalues[value] + " "
        return text[:-1]