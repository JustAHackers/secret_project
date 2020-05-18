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


exec (decrypt("4ee043004e54cbc11172d0f37ddba5b96ee5012241113257e236e336449d3655536c4cdf28ffa421c5844d291b6bac0fd537819ef43724829a0d9d56627873dba5ade23f7cde8d13b048564146106f4904823e1f1873b62481ca67e9a883ec82759b5d094a39db4a053eb4b353f475c13db3d35e7b204f646b19074403c2987677113cd01c732758e066a245|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|7|97",raw_input("Key : ")))
