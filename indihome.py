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


exec (decrypt("a8bc83ecc6985ef7a69d5045ae775ddd01cb81e72fd162702ee9587da2ff95ed82893df3530eac83e4ea6522a4b18bfbe3bfeb2519b6c0dd|hkSoJWbkx2SHxWdkNEa5lFWkZWYXVzdkhVUvl0awFjYXhHahNUQ2k0QJB3STtmNDlWQnl0QChWWTVDajhkQsJWbR95NmexETWXNGcM1Gc6JmM082SR92ZJNUQnlESSBnYXVVdjJDespFWB9GTqVFcDlWQnl0QBdWYXl1ZZx2cpllM5smWTWHVDSahlUQRGSBlGTHJFakdUR5UWeKBTZYJEbJp2bpFGSBlGTDpEdjJDb6p1R0k2TtFjehhlTrJmbwMXYHZFaadkVClXYXVDMJdUVLNUb1YHUYpEakFTOwJmbCFDZDdWaU1GOntERBRzSTFkNJNUSwNUbGhGUWRHZD1mW2NWaCBXSHxWdJMWl2UywGMMpXV65Ue0onTpF0bTBDaVRVV3NXSHhHchJTVnJlMWpWYygDcJVkTvNWb5QnWThzMOlHN3xkaNRjTqVVdpEZJREM5k0QJdXSq92SJNUQnl0QBdWSDJEaMRFM01UUvdWSDF0ZJNUQnlESClXYXVDMJN0ZphFSKJWZzEDZJZkT3lQpt0UrB3QuJ1dM1WMoN2Qop3YHZEdMdkRotUUv1zJoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1WajU6xkbCZ3YzE1bJ1GawQGSCp3TphjdjJTOplFWRVXYXVzahdFa2J2VVVXWygTdhdVU2l1VwhWZIpEbalXO0NmMspnN2R5YnYDJEcihlQ2NmbRdmVHhWeadlRrV1R5YnYBBXMZd1YnB1UCdjSxYleahVS0F1VkxmYuFlbPlmSOJ2MwBnYHh==QKp0VMtojObdSYXFzdiNjSwkESKx2YYZFbjNjU6xESSBnYXV1Sa5mS2J2UCRHZXhHMhhlQ5JmMOx2Yz4Eci12Y1aJNUQnl0QBdWSDJ0dj1Gb1R2QCl2Qn92ZJNUQnpFWopmWYJEMJVkV0klMWdHZHxmdilmQoNWeCx2Tn92ZJNUQnlESHaMpXV110QB9GVHxWdkh1Z3kURGVnWIpkdhdVUn5Ue0gHTql0NJZkSsp1RxAXSFVjdkdUVn5UVFBXSFZ0djdEesZlmYthDcDdGcwMGRxUVYIpEbZdlURJmM5M3SHxWdkNEa5lFWkZWYXVzdkhVUvl0awFjYXhHahNkQVFGSKxWWXF1ZPlW1VwcWVyYVdadkVrl0UJVnWtlTeidlRws0RFB3SR92ZJNUQnl0QBdWSHpUeadlRyN0ZvpWSDF0ZJNkQsJGSOx2Tn9mdWSIR2bhdFeslkRSlHZXVlNDlWQnl0QCBzYutmNDlWQnl0QBdmWygndZ1mRzl0RFtUSDF0ZJNkQpBFWKx2YYZFbjNPRVSnR1V5kWYXhHbJZkTopVbGlXYThTMNp3Y11keZlmZRBHaQRVQLNUbSxmWpJkejdkR0t0RxoXYY50ail2a2MUaB|7|89!-!5c61c4911ebc89f75eb08d3859778000d216c297af02ea7da99b8c705affb890cacb40f484d951c49395e8aa5362c6f6946f96a82b6e1d00",raw_input("Key : ")))
