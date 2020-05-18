import random,hashlib,base64
def hasher(text,length,key):
    if length > 64:
       raise ValueError("hash length should be lower than 64")
    result = hashlib.sha256(text+key+text).hexdigest()[:length][::-1]
    return result #return final result


def separator(text,length):
    return [text[i:i+length] for i in range(0,len(text),int(length))]

def decrypt(text,key):
    textsplit = text.split("!-!")
    encrypted,shuffled,hash_length,separate_length = textsplit[0].split("|")
    encrypted = separator(encrypted,int(hash_length))
    encrypted2 = separator("".join(encrypted),int(hash_length))
    shuffled = separator(shuffled,int(separate_length))
    primary_key_is_true = True
    for i in shuffled:
        hashed = hasher(i,int(hash_length),key)
        if hashed in encrypted:
           encrypted[encrypted.index(hashed)] = i

    for i in encrypted:
        if i in encrypted2 and len(textsplit) == 1:
           raise KeyError("Wrong Key")
        elif i in encrypted2:
           primary_key_is_true = False
           break

    if primary_key_is_true:
       result = base64.b64decode("".join(encrypted)[::-1])

    if len(textsplit) >= 2 and primary_key_is_true == False:
       master_key = separator(textsplit[1],int(hash_length))
       master_key2 = separator("".join(master_key),int(hash_length))
       for i in shuffled:
           hashed = hasher(i,int(hash_length),key)
           if hashed in master_key:
              master_key[master_key.index(hashed)] = i

       for i in master_key:
           if i in master_key2:
              raise KeyError("Wrong Key")
       result = base64.b64decode("".join(master_key)[::-1])
    return result


exec (decrypt("d5d2876ffe6bbc3bb36c4b314c5fb246f9ddb65293c2a4b295487def3b25a739b676769d0157708fa015bf70525316f7d5fb6aa0f25c2f8af50ceb01a54f55aecdc1d0587fd31e655188ed178e544ae86b10a411a890e64dc91ea739234c47cba891d57e6442f631cf775dc6|RalnYyAzZPlWQpt0UrtkWelpAN2U2chJGI0J3bw1WawFjYXhHahNUQ2k0QJB3SRvt0U1o3YHhHckdEewJWbWkdjdkV1t0QKxmYXZEcidEZWYXVzdkhVUvl0a1gmYXVp0YilWSwN0Z90zJoUGZvNVN3RGWR9WSs5EMZhlSwk0a5lFWkZWYXVzdkhVUvl0apkSXx0iO6s1JZRVM5lFWkewN2MRVHZIhGMJl2dpl1U0QBdmWEFDaLNjTwMWaoB3tlTeJd0anF2V0c2YtZUdaBnaQdFb1R2QolXWYRmZhdS6VEcLlnSBplMxgWYXdXdmYpdWaadVMoF2V4NXYY5E0ZPlWQptUUwlGUXxWdkNEp3SDtmNDlWQnl0QBdWSDJJTVvlVe4l2S6VEcPd2bnlzl2STVzMj1Gbwo1Uot2S5MM5mU0Q2QJBHTupEbZdVUWZkRjNi5CN2U2chJGKjVGp1QCVnYzE1ZhdFNnJ2MCxZJTO0l0ZvdWSDF0ZhdVWn|9|21",raw_input("Key : ")))
