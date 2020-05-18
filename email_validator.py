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


exec (decrypt("b99d498584402bc07d0c8d4f5076705c3f26c50878d6a43e740e0345925548c9577c269d972c33cfcef2cb921c5e623100b7ab84fced668db355b1552685aaa72a868e57e32a6cbc1e95347fb9be7121bee5ca42fafd2419492edff75db74749a78a7885585e15840c1df38569742650118e71a489531823546c0a006abadd9756e2378c28bf48801c8b622075b27986c527fa9ba975ede82eaf01740573414ff35e98e265a10bbf7419ec9a4aac212088d3a161368a3f087e725a3682d2e71ab18bb45a85e9ca3200e7c704680f6f58b3f7cac1cc067aa534df93e47d186249eb8e7c485683c11935acdcbbebc6ee840cd53ecfd0c39f2c7cd0509239159a7338c27f10d24d6c70712bda990590c0b6285f68a8ee93fc710661b6778bff99d1d40786d5d2e126480e4daef855d8ac33c863c9daf15c110547aa10c9930582216b956722f6ff5dda0129718d6872c165021faaa045c4ffc993058fc9696fe2131eec425408bf4880198ac29155e31846bad3c1a4f702936beaa05672c90acc182aedd951e98ac2912604b11b5465856446d34a0ef6a46dcdb4fe8e5b80f3b448ef7328eb4416d6b8f56d7c109159f6d5d2e1da69a2889e0ff32b697c90a468aeb0876510c0b6283e0a789a4e1943f8f8924153501d9720f736d7e7bbac1de24719438ce1dfa57502ff6bb0cbbaf0b9dc0bbc02ab12c4822ce67f4419531b377705729|khEawkUarV3Y2lVbGNXSIJUe=kSKdFTL6ozW3J2MKBTSGJ1b2V2Rsx2Y6FzNwR2R4BnYtZleiNDa1wkbSRDZDp0MJl2a1R2MjNjU6xUbkxGZtZFaaN0ZwxkbpF0ZJNUQnl0QJ1GawQGSCpXSJNUQnl0QBdWSj1mVoplRCZnY0U2U1knWXFjd1QXWYF0baJjVadlRrt0QrV3YCZnYyc3ZhdVM5JmMwcmYYZ1cHFDahd1dw90Zpt2SJNUQnlESWV3SDpkMZdFehJGI0J3bw1WaDJkNlpWM2N2RjNTV1NWbWRnYwAFWClnYzgWNnl0QCZ3YHZVd1pFWN92SR92ZDlEcD1mR6RGVvFGWRdWYXRzZDJEMj52a2MUawp1RxgWYXdXdLdkR1FWbslHTjVGelpAN2U2cNZDT5ljMahlSDdWahhkUwMGSZ1Gb6l0UFhWSMdkR6R2Urt0JVlFWK5mWYF1ZnE2VxcnYzoEMwg1MahmYHx2aoBTSpdXaklXS1FWbsl3STVTetlDcilGa3NWbhdVWnJ2VGBnYXpnQkNUaBdWSWlXYXpVNMdlRnl0QBdWSDF0ZsV3YIZFMLNkSDJkelhVT1pFW1MzYtxGMaNFaJlGd0l1VsN3SDF0ZhdVWnJ2VClnYzgmehdEbLhkQ5J2MopXYhd1d1J2MK5GT0M3YzwmeD1mW5pFWOdnYyUje1R2QB9WSshXerljYzIEbil2Zk1WVvNGSKZXZDlWQnl0QBdWSVZzQpF0ZJNUQ0l1VsN3S5p0YIpkdlh0a1RGSDlEcM5mSsl1VZdlURJmM5M3S6x0VkFjWY5EMBdWSDJ0dj1WODJEcilmQoN2MR92STVjejdEeyMWaYNVQ5A1UDF0ZJNUQnl0QoBFWKx2YYZFbyk1V4BnWHFDaEV1dLFFcwM2QnF2V0cWZu9mNDF0ZJNUQnl0Qyc3SjhkS2VGSzI0chhlUzF2VHxGMLhFMwxUbaNlSkdVeKNnYwplbrRnWXFDawxkbklXYYJFbCBnWpJEaXlnSq9WahhkUwMGSrp1VZdmWyYFMLN0aLl1V1EXYZd2YIpkdlhkTBdWSDJ0dj1GbKBHZHV1bJxGeLNkSjJWaJVXYCZ3YHZVdLNkSGBnYDt2cjhkSygmdidVV2RWbnl0QCZ3YHZVdahlQw80ZvdWSjhkS2VGSrZzQnl0QBdmWYhmaoUGZvNWZkRjNJNUQnl0QBdWS5l0ZMRFNnZVbzoEdZhVUvJ2Vi5CN2U2chJGK5QTZTtGcDdGcwlERwkTSEFkN1w2Y5dGcDdGcilWSwNUaBdWShd1d1RGSoBTSYlUOj1mRzglMwpnYyQzbLF1bJhkSsNGWWx2YBlWVzYlaZJjVNZDT5lzNmNVSMNDd5kUa10mYBdWSDF0ZJNUQwMGRxUVYIpEbpdXaZN1cpt0UoBHZDF0bJxmQkdEb3NWb5omW1lUa1EnYywWdGNXYXFVaLF1bDlWQnl0QBdWSDF0ZJNUQnF2VzIleMdEc6JmM6NWeJZzQpF0Z3B3QpF0ZJNUQGBnYDJUdiNTU082YIpkdlh0aY5kehdVNuxkbvdWSDF0ZaJDezoFbLdUMoF2ViNDa1MUaBdWSpF0ZJNUQnl0Qnl0QBdWSDJEaBdWSDF0ZJNkQLdkR6R2UrB3QI50bhhVUwNUaLNkS1pFWkZ2YxY3YHZVdLdkRDJEcalmQzp1VYNjWoJ2Rst2S1pVb5knYXZEMOdnYHxGMidEbUdEb6R2QBZTS5J2MoVTSFhGapJWbWNDWzIUe|7|12",raw_input("Key : ")))
