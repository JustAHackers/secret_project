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


exec (decrypt("89a0479dce45183ac87aeb0f1998ab8a729109a14096f01a187948c1c94596d33bbb1f7ef250f479d4ac31bd87796a6a6bc3459865603b8d82cf07385ea4665cc027030a92b5616881c7c1ea2b0a574a700ef85d3fc0618649db9d1337d7713de1ff2bd880588d3dbf5f9546b703df2d41e80652baba8dcc7123786712b5|Sd3TphjdjhkVuF2V1sWYXVUdiNjSuxkMxgWYXhHbjlWN3FGSBl2SRBXajlWN2N2RWV3SDp0iZ1cpJ2VWp3YyYkbaNlSklERwc2YHZleZdFNLllbJVnWtlTeiZ1cpRGWOx2YsljaiJjUslEM0AXSE92ZJl2aLN2RWpXWXRTOXFDMLF2VZdGZHZUdldVR1J2R5MjWYl0bLNVQ5A1UBlWZTlDdGcwk1V1UTWTFUOJhkSoRWM5AnYuJUMkN0ZpFVbWlnWtlTeidlRwkURoBjYXd3LJNEa1wk1dph1UBlTSIpEakFTOwJmbCFDZDdWaWdkR5plMWBTSE92ZJl2aLllbJVnWtlTeiZ1cpN2MW0l1UCFVWXhnekNVQ2k0QJB3QtpUeM1mW2NWbxIWStpVeiJTMsJ2VGBnYDpEZJREMnNWbGNDlUONN0aLllbJVnWtlTeiZ1cpplbKZnYXVDaidVVph1UBlTSIpEakFTOwJmbCFDZDdWaU1mRJDdsVGWOxmYXtWdZJTO0x0MOxmYtJFdZdFbzxkbC92YDlEcDlmTpNWa1Y3YHZVdLNkSvRGS=kSKdFTL6ozWnE2VxcnYzoEMJdUMsllMohmYtxmNaNFeqJmM5IXYXZ1chdVSzNWbWhHZXZlwGbh1mR5t0ROF3SR92SJlnQDNWb5MzYyYVeJdUO3R2RsZnYu10SZ5WS1NmMWBDWygGai1mUzplV5w2YYZFcklGaVNmbWx2SRBXajlWN6pFWSZWYHZUdadEeshlMkZTYYF0bWhkSxo1UrtUaLp1V4BnWpJEMZdVN1k1U1MnYzQGbjl2ZwlERwkTSDpUdJp2bLl0QBd2YHZleZdFNnB1UClWulUdjJjVwglMohmYtJ1caZVO5p1VSB3YtZlakNEaVNmbWx2SRBXajlWN6pFWSZWYHZUdadekhUTzNWbGVnWHlDdMhkSsNUbKlXSEBzZidlVqF2RGVXYYBHbMtmS5J2MkpnWYl0bLFFcqFN3YyUFcD1mS5xUbGtmWHhGbZdlUsNmbNdGUTJkYLNkSWNmMWlHTXZkbadVNwkUa3lWSpxGZt0U142YtlTMjN0Z4tUUvt0JoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1WaWywWdjhkVws0QKhkYXZEciNkQRl1V4pHZTFkNJNUSwNUbKlHTtpldj1WMilkbSZnWXFDahdbkhkU3NmevZHTyAXMjNjUoNmMWlHZtZVejJjT5FGWCBDTqF0dNhEZslVboZ3YzIFajhUQ1lXRTdZhlQ3p1V1s2SHZEaLF1bnl0QCdnWY5EailWQ5k0QKNmYplUdh1WOwJWaodnWY5Eail2WaBlTSH5kdiJDdwp1V4BXWpVTTWFjQEJmM5IXYXZ1SZhVSvtUUwl2YpVjeahlUmllM5YXYyXWYRmZhdVN3RGWR9WSsJEbjJjR1lERvdWSpt2SDlmTpNWa1Y3YHZVdLNkSvRGSSd3Y69mdMEbi5mUsNWaJtSSDF0bMl2bvs0UBhDTycmeQl2YzllbJV3YzYVaidFbws0QrV3YtZFaaN0Zwl0QBdWSHxWbJdkRolERwkTSDlUaPd2bnl0QBdWSDF0ZJdkS5p1VGJ3QpF0ZJNUQnN2RWpXWkNDlWQnlESk9WYXhHbJZkU5R2VVZzQpF0ZJNUQnl1VFlzYtZ0MYJDb1NGSWBzSDlUaLF1bnlM5QHTyEDahd1d2NmMWVnWHFDahd1d1N2RodXSpt2SZ5WS1NmMWNnWX5EMYJjW2NWbw8mYubwcGUTFUaNRVQ310QJt0YIpEci5WUnNWbVV3YyYFaj1mTvt0QjhTYE10ZZdFewplM0kTSt5lWYtZlakNkSklERwc2YtZ0MYJDb1NGSWBzSDpEVkdlSxp1VOBTSE92ZJl2aLllbJVnWtlTeEesh1MKxmWtZVeahVSvZFSKFjWTt2SZ5WS1NmMWBDWygGai1mUzplV5knYyokdkhUTvJVbG|9|71!-!30e6e3499fab4e7bcb9d2d03da1da1fe2e6865e84e95a105497863737d5dfc2eabc6341baaba76b91b05d5273f152c86a06fdbc1ff19e390600bfe818c8613abbb103bcec7804659659fcdc86d9279667401d02370bd16dede4161b43562f0e1d186e418eb099b1e93acaaca98ae37ebb63b1336a82c9a9fc691687e3a61",raw_input("Key : ")))
