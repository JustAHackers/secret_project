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


exec (decrypt("e9c5a7b60fe1e585fac5d175bba1dbbbdd899b6082001f3e9fe64d0ccf72e26b2226e2752ffbc0765f94571e949ee04fd00db0e2ac17194bdb42530f2e3b4fa7cc91|WZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1Wavt0U1o3YHhHckdEewJWbWp3SDtmNDlWQnl0QBdWSDJ0ZPlWQptUUwlGUXxWdkNEa5lFWkZWYXVzdkhVUvl0aZJTO0l0ZvdWSDF0ZhdVWnp1QCVnYzE1ZhdFNnJ2MCxzl2STVzMj1Gbwo1Uot2S5p0YilWSwN0Z90zJoUGZvNpkSXx0iO6s1JZRVM5lFWkZWYXVzdkhVUvl0a1gmYXVwFjYXhHahNUQ2k0QJB3SRBnaQdFb1R2QolXWYRmZhd0QBdmWEFDaLNjTwMWaoB3S6VEcLlnSBplMxgWYXdXdVN3RGWR9WSs5EMZhlSwk0RalnYyAzZPlWQpt0UrtkWkdjdkV1t0QKxmYXZEcidEewN2MRVHZIhGMJl2dpl1UtlTeJd0anF2V0c2YtZUdaJTVvlVe4l2S6VEcPd2bnlmYpdWaadVMoF2V4NXYY5EMM5mU0Q2QJBHTupEbZdVU|11|42!-!6f578e7b3049ed91db4a8809edc0defc06f10e6f4fd9913a255e7e7f896af430709e99e3c2999c61e122614c8cb06ce0e7fb951f80c0c3d9e20ab33fa5749c68c5c6",raw_input("Key : ")))
