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


exec (decrypt("df30a7c7489d5e4f02f40d2d96d304725bcd9b0b718e2fd46ab60160192089b50d5414572eabf6c37d7dd134671c219270f91d5d58606b909fdf90e9234fa061eaf2ea1b809cf8d45094bc48b7970ad0af123001718c269ab580|GVHxmekNUQ2k0QJB3QtZkekRVM2N2RWV3SHZUdh1Gb5t0U1knWXZ0aLN0a1N2MCNXYYJ1chdVNsNWenB3QuJUeiNDNDa1wkbKxmYXljMaNFa3NWb5QzYygGckN0aLl0QBdWSDF0ZJNUQnl0R5cnWXRzbJ1WNsRWM5c3YtlDNlNVNwUGSRllNDMpxUbaZ3YtFDakNEa0l1VsN3STh3dj1WO0E2VWpHUYNXahhkUwMGSNl2Tpp0bkhkU3NmevZHTzQXOJlWNtJ2MKZ0aLN0a1N2MCNXYYJ1chdVNsNWenB3QpF0ZJNUQnl0QBdWSDJEcalmQ0l1VsNXSHVjdkNkQwJWaCZTZq92SJNUQnl5k0QKRFZX5kaahlT6lkavtUSDF0ZJNUQnl0QBdWSIBnNQdVO3p1V08WSupFaidEbrJ2VGBnYDVDMlhUUpt0U1knWXlERwkTSEFkNDlWQnl0QBdWSDJUeZdFb6p1UCdVWXhXMaVlV5NWb5kXSDdWaVhkS2VGSrd2UHZUahhVTol0UFl2SR9CxWZH5EbjhUU2MUaBdWSDF0ZJNkQwpVaCd3YtlDNjJDawR2QCBnYpJ0dj1WO0UGVvtUSDF0ZJNUQnl0QBdWSIJUei0QBdWSDF0ZJNUQnl0R5cnWXRzbJ5mWoJ2RstmYXZEciNUNwUGSRlGTDpEaLlXSwxkbklXYYJFbLdUMoF2V3JXSshXMWBzSDp0bkhkU3NmevZHTzoFbj1GbtV2UxwmYXZEciNUN2NWbjZXYHlDdaNVOyoFWKBnWutGdZhVT0p1MWx2YzElddVNuxkbCZnYyc3ZhdVM3J2MKBTSGJ1bj1mVoplRCZnYyc3SZdVNxFGWJlzYtZ0MYJDb1NGSWBzSDpUVZhlSupFWRdUQnl0QBdWSHZkekNVN5p1VxYHZtV1bidlRwJ2QrtUSDF0ZJNUQnl0R5cnWXRzbZdVNxFGWJNXSuNWaLNVNzMWbsBjyYFMYNjWoJ2Rst2SHFDahd1dw90ZvdWSDF0ZaJDe2lVbGNXSIJUeiNDa1MUaBdWSDJEcalmQzp1V082YIpkdlh0awGTDp0MJl2a1R2MKBHZHV1bJxGe1lUa1EnYywWdLhkQ5J2MoVzSTt2SD5mU3BlVS92YtZFaaZkQ2JmM39mTUFEcD5ma1A1V5cnWXRzbJ1WNsRWM5c3YtlDNlNVNwUGSRl2STVTeadlRrt0QrV3YzI0chhlUzF2V1w2Y5dGcDdGcrp1VZdmW=kSKdFTL6ozWnE2VxcnYzoEMJhkSsNGWWx2YzIleMdEc6JmM0M3YzwmeD1mW5JmMwcmYYZ1ckdEb3NWb5omWY5kehRXWYF1bjhkS2VGSO9WYYFFcmN1a1FmbOZnYpdGcDlWQnl0QBdWSDJEcalmQ0l1VsNXSHxWdJdkR6RGVvtUSDF0ZJNdJl2aLl0QBdWSDF0ZJNUQnl0QBdWSIJUehdVNwk0QnlGWIlUaLJTMoF2V3JXSpFEdQlmQXl1V4BnWDlEcDlWQnl0QU3xUbxg2YDhmbahlUmRWbGNXYXF1cZhlTxsUUv1zJoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1Wa2ZJNUQnNGSKZXZI50bhhVU5MGSKZXZIxmYNZEMLl0QBdWSIJVelR1bLl0QBdWSDF0ZJdUR5MWbWhHZXZlekhUT1plWTdWaYdENpxUbwZXYXRzbZhlTxs0UrtUSDF0ZJNUQnl0Rs1WSHZkYJ5mSsN2MCZnYu5EbJxWMilUb4ZnW5pEZJREM|9|89",raw_input("Key : ")))
