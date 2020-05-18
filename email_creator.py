import random,base64
def hasher(text,length,key):
    random.seed(key) #setting seed for the digest value
    digest_value=random.sample("abcdef1234567890",16) #shuffling the digest value
    random.seed(text) #setting seed for digest result
    result="".join([random.choice(digest_value) for i in range(length)])
    random.seed() #turning back random to normal
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


exec (decrypt("59cdab518c562588a1476495ba58ca0c6a1f8e3f5dc96000e7d04ac5bbd3817077daf1de5489a0be9adc672088b0c7578bdcd1e241dcdf48b68e98efd0816deae301e2f091fb022f385a95fe01b454f7341b8e15|MM5mU0Q2QJBHTupEbZdVUS6VEcLlnSBplMxgWYXdXdzl2STVzMj1Gbwo1Uot2S5a5lFWkZWYXVzdkhVUvl0aRalnYyAzZPlWQpt0UrtkW0ZPlWQptUUwlGUXxWdkNEmYpdWaadVMoF2V4NXYY5Ep1QCVnYzE1ZhdFNnJ2MCxewN2MRVHZIhGMJl2dpl1UkdjdkV1t0QKxmYXZEcidEelpAN2U2chJGI0J3bw1Wap0YilWSwN0Z90zJoUGZvNwFjYXhHahNUQ2k0QJB3SRVN3RGWR9WSs5EMZhlSwk0tlTeJd0anF2V0c2YtZUda0QBdmWEFDaLNjTwMWaoB3pkSXx0iO6s1JZRVM5lFWkZJTO0l0ZvdWSDF0ZhdVWnWZkRjNi5CN2U2chJGKjVGBnaQdFb1R2QolXWYRmZhdZWYXVzdkhVUvl0a1gmYXVJTVvlVe4l2S6VEcPd2bnlp3SDtmNDlWQnl0QBdWSDJvt0U1o3YHhHckdEewJWbW|7|21",raw_input("Key : ")))
