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


exec (decrypt("27f6f8d1d165fe8a4b0bda51131133861e4502590ee58e13c52ab1195a27316554c585fb38399d827d79ae9b07e34f49fef0cb568c542d160ae2d2c1204937eac698246f271658e89cf20eecb29cfc05fb6a7f9a406c168529ebb8e238a07eba9e0be8d18a7bf6bd31c9dad64eed30a373de916718e3ef68922d209b5cf41b21d28ef7dbe6e20da73e1e127a0d6a14d574eee4bb6973ee79161a7e26ddc2a5f3d0386abbd2580fb28c518255cfe3e038552afe02a1d034e8e1ca47b231a31165c864f27576a7fe2cd0d6fd51a164daae84628af91a401235085470a26d6d4eb86730b81c86e3d32d00cec0d79f0f3c2d98aa2d98e216380a58753441bfff20a884145825ffafcb2834760500d1349ecc943e634d378cfced884145825ffafc1c2278230d099a05d59d96a4e8a46fbed517ccbd390809629|RBHaQRVQLNUbSxmWXV1Sa5mS2J2UCRHZz4Eci12Y1N2R5YnYXVzdkhVUvl0awFjYXhHbJZkTopVbGlXYXhHMhhlQ5JmMOx2YDJEcihlQ2NmbRdmVpJkejdkR0t0RxoXYDF0ZJNkQsJGSOx2T2U2chJGKjVGelpANyYVdadkVrl0UJVnWygndZ1mRzl0RFtUSYJEbJp2bpFGSBlGTR92ZJNUQnlESSBnYYpEakFTOwJmbCFDZDJ0dj1Gb1R2QCl2QywGMMpXV65Ue0onTTpEZJREM5k0QJdXS2U2chJGI0J3bw1WatFjehhlTrJmbwMXYHxWdkNEa5lFWkZWYTFkNJNUSwNUbGhGUY50ail2a2MUaBdWSoUGZvNWZkRjNi5CNThTMNp3Y11keZlmZHVDSahlUQRGSBlGTDF0ZJNkQpBFWKx2YutmNDlWQnl0QBdmWuFlbPlmSOJ2MwBnYn9maJNUQnl0QBdWSzE1bJ1GawQGSCp3TWRHZD1mW2NWaCBXSYJEMJVkV0klMWdHZXF1ZPlWQpt0UrB3Qn92ZJNUQnlESClXYHZEdMdkRotUUv1zJIpEbalXO0NmMspnWXNGcM1Gc6JmM082SuJ1dM1WMoN2Qop3YqVFcDlWQnl0QBdWYzEDZJZkT3l1VwcWVpF0bTBDaVRVV3NXSHhWeadlRrV1R5YnYygTdhdVU2l1VwhWZXVDMJdUVLNUb1YHUBBXMZd1YnB1UCdjSHxWdkNEa5lFWkZWYXVDMJN0ZphFSKJWZtlTeidlRws0RFB3SXVzdkhVUvl0awFjYYZFbjNjU6xkbCZ3YHxWdJhkSoJWbkx2SXVlNDlWQnl0QCBzYqVVdPRVSnR1V5kWYHpUeadlRyN0ZvpWSR92ZJNUQnl0QBdWSDJEaMRFM01UUvdWSHxmdilmQoNWeCx2TThzMOlHN3xkaNRjTHJFakdUR5UWeKBTZql0NJZkSsp1RxAXSFZ0djdEesZlMWl2UHZFaadkV5NmexETWDpEdjJDb6p1R0k2TXl1ZZx2cpllM5smWq92SJNUQnl0QBdWSFVjdkdUVn5UVFBXS==QKp0VMtojObdSYHxWdkh1Z3kURGVnWn92ZJNUQnpFWopmWIpEbZdlURJmM5M3SYZFbjNjU6xESSBnYHhHchJTVnJlMWpWYTVDajhkQsJWbR9mYHhHaMpXV110QB9GVDdWaU1GOntERBRzSIR2bhdFeslkRSlHZXVVdjJDespFWB9GTXhHahNkQVFGSKxWWxYleahVS0F1VkxmYTtmNDlWQnl0QChWWXVzahdFa2J2VVVXWIpkdhdVUn5Ue0gHTDF0ZJNUQnlESClXYygDcJVkTvNWb5QnWXFzdiNjSwkESKx2YphjdjJTOplFWRVXYthDcDdGcwMGRxUVYXhHahNUQ2k0QJB3S|7|16!-!a7fefc0202e8f9c536d60582242244ce2938da8bd998c92418a5622b85a742e88318c8f64c4bb0ca707b59b6d7943f3bf9fd168ec183a02ed59a0a12ad3b47951ebca3efa72e8c9cb1fad9916ab1f1d8f6e57fb53de12ec8ab966c9a4c5d7965b9d69c02c576fe60421b050e39904d547409b2e72c949fecbaa0adb681f326a20ac9f7069e9ad05749292a75d0e5230873999366eb74997b2e2579ae001a58f40d4ce5660a8cdf6ac182ca881f949d4c88a5f9da520d439c9215376a425422e81ce3fa787e57f9a10d0ef08252e30559c3eac5fb253d2a48dc837d5ae0e0396ce74d6c21ce9404a0dd191d07bfdf41a0bc55a0bc9a2e4cd58c7843326fffad5cc3238ca8ff5f16ac437ed8dd0243b911b349e43047c1f190cc3238ca8ff5f121aa7ca4d0dbb5d808b0be539c53ef69082711604bdcdbeab",raw_input("Key : ")))
