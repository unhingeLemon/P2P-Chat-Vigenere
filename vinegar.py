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


# Driver code
if __name__ == "__main__":
  TEXT = "EATnaPoSige Na 1231 !*&@"
  KEY = generateKey("KEYKOTO",TEXT)
  print(encrypt(KEY,TEXT))
  #EWX
  print("DECRYPTED: " + decrypt(KEY,encrypt(KEY,TEXT)))

  pass