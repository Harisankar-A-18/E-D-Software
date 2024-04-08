import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class HybridEncryption(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Hybrid Encryption'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.key1Label = QLabel('Enter Key 1:', self)
        self.key1Label.move(20, 20)
        self.key1Input = QLineEdit(self)
        self.key1Input.move(120, 20)

        self.key2Label = QLabel('Enter Key 2:', self)
        self.key2Label.move(20, 60)
        self.key2Input = QLineEdit(self)
        self.key2Input.move(120, 60)

        self.encryptLabel = QLabel('Enter Text to Encrypt:', self)
        self.encryptLabel.move(20, 100)
        self.encryptInput = QLineEdit(self)
        self.encryptInput.move(150, 100)

        self.encryptButton = QPushButton('Encrypt', self)
        self.encryptButton.move(20, 140)
        self.encryptButton.clicked.connect(self.encrypt)

        self.decryptLabel = QLabel('Enter Text to Decrypt:', self)
        self.decryptLabel.move(20, 180)
        self.decryptInput = QLineEdit(self)
        self.decryptInput.move(150, 180)

        self.decryptButton = QPushButton('Decrypt', self)
        self.decryptButton.move(20, 220)
        self.decryptButton.clicked.connect(self.decrypt)

        self.show()

    def encrypt(self):
        key1 = self.key1Input.text()
        key2 = self.key2Input.text()
        plaintext = self.encryptInput.text()
        ciphertext = ''

        for i in range(len(plaintext)):
            xored = ord(plaintext[i]) ^ int(key1[i % len(key1)])
            lucas = self.lucas(int(key2), i)
            encrypted_char = (xored + lucas) % 256
            ciphertext += chr(encrypted_char)

        QMessageBox.about(self, 'Encrypted Text', ciphertext)

    def decrypt(self):
        key1 = self.key1Input.text()
        key2 = self.key2Input.text()
        ciphertext = self.decryptInput.text()
        plaintext = ''

        for i in range(len(ciphertext)):
            lucas = self.lucas(int(key2), i)
            decrypted_char = (ord(ciphertext[i]) - lucas) % 256
            xored = decrypted_char ^ int(key1[i % len(key1)])
            plaintext += chr(xored)

        QMessageBox.about(self, 'Decrypted Text', plaintext)

    def lucas(self, n, k):
        if k == 0:
            return 2 % n
        elif k == 1:
            return 1 % n
        else:
            return (self.lucas(n, k - 1) + self.lucas(n, k - 2)) % n

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HybridEncryption()
    sys.exit(app.exec_())
