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


exec (decrypt("bf639bfe8f01cd5d25ada1b7c067114a9eb55354fdc26adaed6b3c2579620eba5d073c9daa6cfb7323f4f2ee97acc549e9cb2cf96cc89704e726a87e936ddb83adf120651cdea7bc93585430139bae0581a38ebde0b758647fcc356812b609713172|zplV5w2YYZFcklGaVNmbWx2SRBXajlWN6pFWSZWYHZUdadEeshlMkZTYYF0bWhkSxo1UrtUlUONN0aLllbJVnWtlTeiZ1cpplbKZnYXVDaidVVph1UBlTSIpEakFTOwJmbCFDZDdWaU1mREesh1MKxmWtZVeahVSvZFSKFjWTt2SZ5WS1NmMWBDWygGai1mUzplV5knYyokdkhUTvJVbGbkhkU3NmevZHTyAXMjNjUoNmMWlHZtZVejJjT5FGWCBDTqF0dNhEZslVboZ3YzIFajhUQ1llM5QHTyEDahd1d2NmMWVnWHFDahd1d1N2RodXSpt2SZ5WS1NmMWNnWX5EMYJjW2NWbw8mYuSd3TphjdjhkVuF2V1sWYXVUdiNjSuxkMxgWYXhHbjlWN3FGSBl2SRBXajlWN2N2RWV3SDp0WulUdjJjVwglMohmYtJ1caZVO5p1VSB3YtZlakNEaVNmbWx2SRBXajlWN6pFWSZWYHZUdadt0U142YtlTMjN0Z4tUUvt0JoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1Wa0l1UCFVWXhnekNVQ2k0QJB3QtpUeM1mW2NWbxIWStpVeiJTMsJ2VGBnYDpEZJREMnNWbGNDJDdsVGWOxmYXtWdZJTO0x0MOxmYtJFdZdFbzxkbC92YDlEcDlmTpNWa1Y3YHZVdLNkSvRGSkNDlWQnlESk9WYXhHbJZkU5R2VVZzQpF0ZJNUQnl1VFlzYtZ0MYJDb1NGSWBzSDlUaLF1bnXRTdZhlQ3p1V1s2SHZEaLF1bnl0QCdnWY5EailWQ5k0QKNmYplUdh1WOwJWaodnWY5Eail2=kSKdFTL6ozWnE2VxcnYzoEMJdUMsllMohmYtxmNaNFeqJmM5IXYXZ1chdVSzNWbWhHZXZlM0AXSE92ZJl2aLN2RWpXWXRTOXFDMLF2VZdGZHZUdldVR1J2R5MjWYl0bLNVQ5A1UBlWZTlbwcGUTFUaNRVQ310QJt0YIpEci5WUnNWbVV3YyYFaj1mTvt0QjhTYE10ZZdFewplM0kTSt5DdGcwk1V1UTWTFUOJhkSoRWM5AnYuJUMkN0ZpFVbWlnWtlTeidlRwkURoBjYXd3LJNEa1wkWaBlTSH5kdiJDdwp1V4BXWpVTTWFjQEJmM5IXYXZ1SZhVSvtUUwl2YpVjeahlUmllM5YXYylWYtZlakNkSklERwc2YtZ0MYJDb1NGSWBzSDpEVkdlSxp1VOBTSE92ZJl2aLllbJVnWtlTeEbi5mUsNWaJtSSDF0bMl2bvs0UBhDTycmeQl2YzllbJV3YzYVaidFbws0QrV3YtZFaaN0Zw1dph1UBlTSIpEakFTOwJmbCFDZDdWaWdkR5plMWBTSE92ZJl2aLllbJVnWtlTeiZ1cpN2MWl0QBdWSHxWbJdkRolERwkTSDlUaPd2bnl0QBdWSDF0ZJdkS5p1VGJ3QpF0ZJNUQnN2RWpXWXWYRmZhdVN3RGWR9WSsJEbjJjR1lERvdWSpt2SDlmTpNWa1Y3YHZVdLNkSvRGSSd3Y69mdMN3YyUFcD1mS5xUbGtmWHhGbZdlUsNmbNdGUTJkYLNkSWNmMWlHTXZkbadVNwkUa3lWSpxGZiZ1cpJ2VWp3YyYkbaNlSklERwc2YHZleZdFNLllbJVnWtlTeiZ1cpRGWOx2YsljaiJjUslEwGbh1mR5t0ROF3SR92SJlnQDNWb5MzYyYVeJdUO3R2RsZnYu10SZ5WS1NmMWBDWygGai1mUaLp1V4BnWpJEMZdVN1k1U1MnYzQGbjl2ZwlERwkTSDpUdJp2bLl0QBd2YHZleZdFNnB1UClWywWdjhkVws0QKhkYXZEciNkQRl1V4pHZTFkNJNUSwNUbKlHTtpldj1WMilkbSZnWXFDahdekhUTzNWbGVnWHlDdMhkSsNUbKlXSEBzZidlVqF2RGVXYYBHbMtmS5J2MkpnWYl0bLFFcqF|7|71",raw_input("Key : ")))
