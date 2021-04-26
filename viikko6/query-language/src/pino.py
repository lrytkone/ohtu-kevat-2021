class Pino:
    def __init__(self):
        self._alkiot = []

    def push(self, alkio):
        self._alkiot.append(alkio)

    def pop(self):
        return self._alkiot.pop()

    def empty(self):
        return len(self._alkiot) == 0

def main():
    pino = Pino()

    print("Pinotaan, tyhjä lopettaa:")

    while True:
        pinoon = input()

        if not pinoon:
            break

        pino.push(pinoon)

    while not pino.empty():
        print(pino.pop())

if __name__ == "__main__":
    main()