from hashlib import sha256
import json
from time import time


class Block:
    # Инициализация блока
    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.prevHash = None
        self.nonce = 0
        self.hash = self.getHash()

    # Формирование хэша с использованием данных, хранящихся в блоке
    def getHash(self):
        hash = sha256()
        hash.update(str(self.prevHash).encode("utf-8"))
        hash.update(str(self.timestamp).encode("utf-8"))
        hash.update(str(self.data).encode("utf-8"))
        hash.update(str(self.nonce).encode("utf-8"))
        return hash.hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.getHash()


class Blockchain:
    # Инициализация цепи блоков
    def __init__(self):
        self.chain = [Block(str(int(time())))]
        self.difficulty = 1
        self.blockTime = 30000

    # Метод получения последнего блока
    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    # Метод добавления блока в цепь
    def addBlock(self, block):
        block.prevHash = self.getLastBlock().hash
        block.hash = block.getHash()
        block.mine(self.difficulty)
        self.chain.append(block)

        self.difficulty += (-1, 1)[
            int(time()) - int(self.getLastBlock().timestamp) < self.blockTime
        ]

    # Алгоритм доказательства выполнения работы
    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            prevBlock = self.chain[i - 1]

            if (
                currentBlock.hash != currentBlock.getHash()
                or prevBlock.hash != currentBlock.prevHash
            ):
                return False

        return True

    def __repr__(self):
        return json.dumps(
            [
                {
                    "data": item.data,
                    "timestamp": item.timestamp,
                    "nonce": item.nonce,
                    "hash": item.hash,
                    "prevHash": item.prevHash,
                }
                for item in self.chain
            ],
            indent=4,
        )


chain = Blockchain()

# Добавим новый блок
chain.addBlock(
    Block(str(int(time())), ({"from": "Sasha", "to": "Vanya", "amount": 100}))
)

# Вывод обновлённого блокчейна
print(chain)
