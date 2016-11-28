import sqlite3
conn = sqlite3.connect('GREYC-KeyStroke-Dataset.db')

c = conn.cursor()

keymap = {
  'a': int('0x00', 16),
  's': int('0x01', 16),
  'd': int('0x02', 16),
  'f': int('0x03', 16),
  'h': int('0x04', 16),
  'g': int('0x05', 16),
  'z': int('0x06', 16),
  'x': int('0x07', 16),
  'c': int('0x08', 16),
  'v': int('0x09', 16),
  'b': int('0x0B', 16),
  'q': int('0x0C', 16),
  'w': int('0x0D', 16),
  'e': int('0x0E', 16),
  'r': int('0x0F', 16),
  'y': int('0x10', 16),
  't': int('0x11', 16),
  '1': int('0x12', 16),
  '2': int('0x13', 16),
  '3': int('0x14', 16),
  '4': int('0x15', 16),
  '6': int('0x16', 16),
  '5': int('0x17', 16),
  '=': int('0x18', 16),
  '9': int('0x19', 16),
  '7': int('0x1A', 16),
  '-': int('0x1B', 16),
  '8': int('0x1C', 16),
  '0': int('0x1D', 16),
  ']': int('0x1E', 16),
  'o': int('0x1F', 16),
  'u': int('0x20', 16),
  '[': int('0x21', 16),
  'i': int('0x22', 16),
  'p': int('0x23', 16),
  'l': int('0x25', 16),
  'j': int('0x26', 16),
  '\'': int('0x27', 16),
  'k': int('0x28', 16),
  ';': int('0x29', 16),
  '\\': int('0x2A', 16),
  ',': int('0x2B', 16),
  '/': int('0x2C', 16),
  'n': int('0x2D', 16),
  'm': int('0x2E', 16),
  '.': int('0x2F', 16),
  '`': int('0x32', 16),
  ' ': int('0x31', 16)
}

c.execute("SELECT rawPress, password FROM keystroke_datas")
data = []
for ps, password in c:
    
    ps = [[int(i) for i in p.split(' ')] for p in ps.split('\n') if p != '']

    for p1, p2 in zip(ps, ps[1:]):
        key_code, p1t = p1
        key_code, p2t = p2
        char = str(chr(key_code).lower())
        assert char in keymap
        data.append(((p2t - p1t) / 10000, keymap[char]))
        
data = [d for d in data if d[0] > 0]

for t, k in data:
    print('{}, {}'.format(int(t), k))
        
conn.close()
