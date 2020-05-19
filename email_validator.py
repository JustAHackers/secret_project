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


exec (decrypt("8903eaceeb20aa6708046835b76a813610cc72ddc2d195143b006c7f18fd440e2201cb64318d0c791db1915a3ddedb23339f5cf337f4750bb391f10643519a8f9a2b|VXSpVTciJDb1tESClnYzgWNLN1aLNkbSdHUWJ1bj1mVoplRCZnYyc3bkhkQ6N2RWxmWDt2SkhUQ1J2VGd3SHRGbkZUOyk1V4BnWDhHajNTVwN0Z90zJoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1WaxGMaN1Zph1R0kGTtBndhdFNvlFWOFzSTt2SJNUQnl0QBdWSHxWbJdkRilkbKx2YzIkdi5mTslEbxIWSthndalnSklERwkTSDpEVkdlTqpFWOpXSq92SJNUQnl0QBdWSDF0ZJhEc2A1V5cnWXRzbJ5mWoJ2RstmYXZEcbs1WZTFDbidlRwJ2Q1Y3YtNmdhdUO0p1U5IjWYpEca52a0lFWNRnWzYFbjNTU2V2MwkGTtpldj1WMoR2QoRXWXx2cLNFe3NWb5QTYXZleQh1cpFGSSBzYI1UaPlmSvRGSSd3Y69mdMNDd5kUa10mYzoEdZhVUvNGSKZ=kSKdFTL6ozWnE2VxcnYzoEMJhkSsNGWWx2YzIleMdEc6JmM0M3YzwmeD1mW5JmMwcmYYZ1ckdEb3NWb5omWY5kehdVNuxkbCZnYyc3ZhdVM3J2MKBTSGJ1bj1mVoplRCZnYyc3SZdVNxFGWJlzYtZ0MYJDb1NGSWBzSDpUVZhlSupFWRdGVHxmekNUQ2k0QJB3QtZkekRVM2N2RWV3SHZUdh1Gb5t0U1knWXZ0aLN0a1N2MCNXYYJ1chdVNsNWenB3QuJUeiNDa1A1V5cnWXRzbJ1WNsRWM5c3YtlDNlNVNwUGSRl2STVTeadlRrt0QrV3YzImMoBHZDJEcilmQ3NWb5QTZU92SJNUQnl0QBdWSDF0ZJhkQ5J2MoVDTupEbidVOyo1Uod3YtlDNjJDawR2QrtUSDF0ZJNUQnl0QBdWSHlzdadFNvlUb1wGZxkzdj1WO0U2U1ATZIFVaMNkSzkUarVHZzoEckdUVvlEb40chhlUzF2V1w2Y5dGcD5mU3N2MCxmWXFVOhdVNwsESKhGZxkDci5mQxQ2QnlmVHhWeadlRrlERvdWSptGcDdGcrp1VZdmWyYFMYNjWoJ2Rst2SHFDahd1dw90ZvdWSDF0ZaJDe2lVbGNXSIJUeiNDa1MUaBdWSDJEcaSotUeJBHTuRWehhlUst0RxgWYXdncJxGe1lUartUSDF0ZJNUQnl0QBdWSDF0ZJhkQ5F2V1ATSDdWaYhUSptkMxgWYXdncJlWQ0BVaCdVWXhHcaNUSwNUaBdWSDJEbldkTsNGSRZzQpF0ZJNUQnl0QCBnWpJ0dj1WO0MlmQzp1V082YIpkdlh0awlERwkTSEFkNDlWQnl0QBdWSDJEMhdVMsxkbONnWXZ1dLRUTx5kaBB3QpF0ZJNUQnl0QCd3YtlDNlRVM2N2RWV3SDpUdahFZmNGSKZXZItWdkhEawkUarV3YtZFaaN0ZwxkbOdnYHxGMidEbiNUNwUGSRl2STVTeadlRrt0QrV3YzI0chhlUzF2V1w2Y5dGcDlWQnl0QBdWSDF0ZJNkQwpVaCRXWXx2cJdUN2R2QCBnYpJkNlp2bLl0QBdWSDF0ZJNUQnl0QBdWSHlzdadFNvlkbahmYHx2aidlRwJ2Q1ATZIFVaMNk1pFWN92SR92ZJNUQnF2VZd2YIpkdlh0anBVaBd3Tn92ZJNUQnl0QBd2YIpkdlhkTvFGWRlzYIpkdlhEbi1kRwsUSDF0ZJhkU5VGVvtUSDF0ZJNUQnl0RFlzYtZFekdlV6RGSNVnWyYFMLNkSvRGSSd3Y69mdMNjWsNWXZI50bhhVUwZ2UrVXYu5kdil2ZwNUaBdWSDF0ZJNkQwpVaCRXWXx2cJdEb1l0RGpHZU92SJNUQnl0QBdWSDF0ZJdkR6R2U1knWXFjdk1WVvJ2VGBnYDt2SJNUQnl0QBdWSHlzdadFNvl1V1EXYYl0cJ52Ypt0U1MzYt|11|163!-!80db3ef18931ce6e6decfeefc212dc5723891df885403d903367247ae3d277c6e3135850eaa1b7733b5b3889008afa0d0f8774868e2ab1df45e276ef5eae835cc46c",raw_input("Key : ")))
