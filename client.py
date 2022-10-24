#CLIENTS
import socket
import threading


ip=input("Enter you PEER IP: ")
KEY = input("Enter you CYPHER KEY: ")
sport = 50001
dport = 50002

print('\ngot peer')
print('  IP ADDRESS:          {}'.format(ip))
print('  source port: {}'.format(sport))
print('  destination port:   {}\n'.format(dport))

# punch hole
# equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
print('punching hole')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', sport))
sock.sendto(b'0', (ip, dport))

print('ready to exchange messages\n')

# Vigenère cipher CODE
#################################
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     

# INITIALIZING THE 2D ARRAY
upper_cases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_cases = upper_cases.lower()
special_chars = "!#$%&()*+,-. :;<=>?@[]^_`{|}~"
digits = "0123456789"
char_set = upper_cases + lower_cases + special_chars + digits

char_set_arr = []
b = char_set
cols=[]

for x in range(len(char_set)):
  for a in b:
    cols.append(a)  
  char_set_arr.append(cols)
  b = b+b[0]
  b = b[1:]  
  cols = []


# Plain text to Cypher Text
def encrypt(key,string):
  # access cols:
  encrypted_text = ''
  iter = 0
  for s in string:
    ind_row = char_set.index(s)
    ind_col = char_set.index(key[iter])
    iter +=1
    encrypted_text += char_set_arr[ind_row][ind_col]

  return encrypted_text

# Decypt the CYPHER TEXT
def decrypt(key,encrypted_text):
  # access cols:
  decrypted_text = ''
  iter = 0
  for s in key:
    ind_row = char_set.index(s)
    ind_charset = char_set_arr[ind_row].index(encrypted_text[iter])
    iter+=1
    decrypted_text += char_set[ind_charset]


  return decrypted_text

##############################################





# RECIEVING MESSAGE
# listen for
# equiv: nc -u -l 50001
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', sport))

    while True:
        data = sock.recv(1024)
        key = generateKey(data.decode(),KEY)
        msg = decrypt(key,data.decode())
        print('\rpeer: {}\n> '.format(msg), end='')

listener = threading.Thread(target=listen, daemon=True)
listener.start()

# SENDING MESSAGE
# equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', dport))



while True:
    msg = input('> ')
    key = generateKey(msg,KEY)
    msg = encrypt(key,msg)
    print("Encypted Message ("+msg+") is sent")

    sock.sendto(msg.encode(), (ip, sport))



