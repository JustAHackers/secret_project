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


exec (decrypt("1c7aed1d351e709410fda56674e9d7661fb72d6cf933011747f459aec9082b95c563ac79a1fb0a8403477074b2c5abd5c590756c53fe265826d9d86412ebd2621cb66d1d6c9768dcac048975b354f1e7bd8543a4108bf3bdac14586ee09944b3f7ea77902309e383cfc572380e7c6cfe1306ca52058392337651b09d942390726307cb5669441fea2a7349edff1c517a9bed928918d900318156c858a96d2cf3a5f8766690c9b3e5b90c85392256dd8b2cad0413ee7b677bcf9b3bfd91101dda11725440be392291de0f73d30e38d915376039c561e63374a645816549f4c131a6e445c6f1d14c831d954c2be3e1619a809750c6eae38f690c34bdfffc4e232071b69d51f24861a5a0ba8bc810690f266266e596d328050b18d60421a6a29af786b95e298b3ada048d33012e0fa8e3e94bb5d2e97553bc84ff8c99b0a3362231cd84b29a2ca00aa299f436893e0b173534ba0eecf5cc5460f92dc47ffddd3257a7af00d583d3157f838aa3575bd01b374cde2c89d02a735f4c001f42b1d3c4b54e255d07e05b548dfda8cfa639fd13d316f73ed6088d1ead076821d9487a23f7c466b151b79dd354b3e89d3bae516a22c355baeb1b0f7161e8af9a79b2d94aabf37694ab32ee430466894b2f6688eca9d96ff2199286|JNUSwNUbGpHZUFjdjdkV1t0RGVXYtxWeLNVN5p1VGt2SDtWdjNjQzFGWSNXYXVDbjl3ZwNkbClnYzgWNQdVO3p1V08WStVmQ2JmM3dWYXFzdiNjSwkkRS92YtZFaaZkQ2JmM3tUWXVTchhVS5MWbGNDWywWdjhkVws0QKVVWYpkbahVUnR1RspHZDFkNXdHcPd2bnl0QBdmWygndZ1mRzlESClnYzgWNDlWQnl0QCBnWpJ0cadFNvNGSKZXZItGcJREM5kERBZzQpF0ZJNUQnl0QCBWSupFaidEbrJ2VGBnYDVDMlhUUpt0U1knWXZ0aLN0a1N2MCNXYYJ1chdVNsNWenB3QpF0ZJNUQnl0QBdWSDJEcalmQ0l1VUQnl0QBdWSIJUeiNDa1wkbKxmYXljMaNFa3NWb5QzYygGckN0aLl0QBdWSDF0ZJNUQnl0R5cnWXRzbJ1WNsRWM5c3YtlDNTYXFDbM5mTzp1VWd3SE1UcOpWQwNUaBdWSDF0ZJNkQ3NWb5QTZUFjdjdkV1t0QKVnWYRmZjhkS2VGSrVHZIhGMJl2a1NWbEcD5mU3xUbxg2YDhmbahlUmRWbGNXYXF1cZhlTxsUUv1zJoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1WaXl1V4BnWDlEcDlWQnl0QCxWZH5EbjhUU2MUaBdWSDF0ZJNkQwpVaCd3YtlDNjJDawR2QCBnYpJ0dj1WO0UGVvtUSDF0ZJNDlWQnl0QBdWSDJEcalmQ0l1VsNXSHxWdJdkR6RGVvtUSDF0ZJNUQnl0QBdWSHZkekNVN5p1VxYHZtV1bidlRwJ2QrtUSDF0ZJNUQnl0R5cnWXRzbZdVNxFGWJNXSuNWaLNVNzMWbsBjWTdWaYdENpxUbwZXYXRzbZhlTxs0UrtUSDF0ZJNUQnl0Rs1WSWhmWDdGcM5mT3J2RsBjYHxWdahVTvtUUvdWSDF0ZhdVWnNGSKZXZIt2ZQlWQ390ZvdWSDF0ZJNUQnNGSKZXZI50bhhVU5MkbklXYYJFbLdUMoF2V3JXSshXdJl2aLl0QBdWSDF0ZJNUQnl0QBdWSIJUehdVNwk0QnlGWIlUaLJTMoF2V3JXSpFEdQlmQsNXSHVjdkNkQwJWaCZTZq92SJNUQnl0QBdWSDF0ZJNUQnl0R5cnWXRzbJ5mWoJ2RstmYXZEciNUNwUGSRlGTDpEaLlXSwxtV2UxwmYXZEciNUN2NWbjZXYHlDdaNVOyoFWKBnWutGdZhVT0p1MWx2YzEldlNDMpxUbaZ3YtFDakNEa0l1VsN3STh3dj1HZkYJ5mSsN2MCZnYu5EbJxWMilUb4ZnW5pEZJREM5k0QKRFZX5kaahlT6lkavtUSDF0ZJNUQnl0QBdWSIBnNQdVO3p1V08lNVNwUGSRlGTDp0MJl2a1R2MKBHZHV1bJxGe1lUa1EnYywWdLhkQ5J2MoVzSTt2SD5mU3BlVS92YtZFaaZkQ2JmM39mTUFGSKZXZIxmYNZEMLl0QBdWSIJVelR1bLl0QBdWSDF0ZJdUR5MWbWhHZXZlekhUT1plMWBzSDp0bkhkU3NmevZHTzoFbj1GbpkSXx0iO6s1JhdVM3J2MKBTSIpEbjhlVsN2MSpHTHBneiJDNzN2Msp3QtpVeiJDMnJGWWNHZHx2dj1WOqpFWOpXYXVjbM5DbkFTO3NWb5QTZTVDMlhUUpt0U1knWXZ0aLN0a1N2MCNXYYJ1chdVNsNWenB3QnB3aadVWnplMWBDWzoFaidEbrt0RxgWYWO0E2VWpHUYNXahhkUwMGSNl2Tpp0bkhkU3NmevZHTzQXOJlWNtJ2MKRXWYF1bjhkS2VGSO9WYYFFcmN1a1FmbOZnYpdGc|47|94!-!2faf50293dcccc530c318c2f0fff1b4f6b28dd79edffc3f315e92efbba30dfb230c3d63a05b99452e48c9dca5f873df65b7895f6753fa213ae38f10dbe7b8fc9d993d148ec532be5f8987b2a5650f06f3bc67fdf6bf368e6de9ac2d589046e8eb96483db7efcf398d42b54e912122312a7c845c37af1c3a728fae20f567c617d464cb82926be5fd0b5e7831ef15576d5c0bbff3c0dc47fed3d94e32533876669f586bf71374aa7fd685296160404dfa9fb59447b093aa13e61e2b95a3e30a06c9a47ccf037bd8d157efa34f969410a33992ec79e7ff19e5a79e669ca4366edcfae5fd0f2713f54a1276c73213b961094512779474b1990250371eb19aa3d0b01b9a517541df32708740661920f1dd47f3ac02e32e123aeb122a49b3fde457fbf3e3d516472f698f87221cc2515b1c8b38146de414126d81f5d4b31d7c737c056bac99977edd19e823ac6eb4602dbecd6fc8103b5254bc10d9d6f011737c332ff45487e5c2a713cd2ba3cf632c7350e5e597e2b217d746926d7c9359b2d7ba90780051932b231663a5a5be1400684168dee640af833d01d1fa316a0245f53155447cefbc672a8599cfae6a49d4b4acda4ac1249b96f02707ad2550da11bdd243baa68d9965153613e3e9ff469dd6658ce9c2dd1018985",raw_input("Key : ")))
