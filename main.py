import random

class RSAEncryption():
  def __init__(self, bin_key, bits, load_key):
    self.bin_key = bin_key
    self.bits = bits
    if load_key == True:
      self.load_key()
    if self.bin_key == None:
      self.regenerate_key()

  def save_key(self):
    with open("key.txt", 'w') as f:
      f.write(self.bin_key)
    print("Successfully Saved Key")

  def load_key(self):
    with open("key.txt", 'r') as f:
      self.bin_key = f.readlines()[0]
    print("Successfully Loaded Key")

  def regenerate_key(self):
    bin_num = []
    for x in range(0, self.bits):
      if random.choice([0, 1]) == 1:
        bin_num.append('1')
        print('\b|')
      else:
        bin_num.append('0')
        print('\b.')
    self.bin_key = ''.join(bin_num)
    print("Verifying Key has Specified Bit-Length...")
    print(len(self.bin_key) == self.bits)
    print("Key Regen Successful. New %s-bit Key:\n%s" % (self.bits, self.bin_key))

  def encrypt(self, a):
    return int(self.bin_key, 2) * random.randint(2, 100) + a

  def decrypt(self, a):
    return a % int(self.bin_key, 2)

  def encrypt_string(self, a):
    a_list = [*a]
    e_list = []
    for bit in a_list:
      e_list.append(self.encrypt(ord(bit)))
    return ','.join(str(item) for item in e_list)

  def decrypt_string(self, a):
    a_list = [int(item) for item in a.split(',')]
    d_list = []
    for bit in a_list:
      d_list.append(chr(self.decrypt(bit)))
    return ''.join(d_list)

rsa = RSAEncryption(None, 128, False)
encrypted = rsa.encrypt_string("Typing that and calling it brazilian is an insult to real brazilians.")
decrypted = rsa.decrypt_string(encrypted)
print("'hello there' Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
with open("decrypted.txt", 'w') as f:
  f.write(encrypted)
