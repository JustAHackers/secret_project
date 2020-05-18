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


exec (decrypt("ffa68b181b6b797005b8df7359dc0a54841909fbef4327ecbb64697439558b70e36cec0e62a433e3627d2bdcf9127130cd45ff8a4565762e5aa59a3a456e3dd440beb947502ca3f9ac9587a05c6264949c696d9c5730a6a53aa3055618a6ac50ab6a6b369d0fae252c3944937406c893627f206deb969766dc0a10f05799119263d4a1e4d8ede911869730e6e61f3e6e4d068b0755bc8fd9dade114f793d407c6c0450cae259154154e89906e9bd9eecea2ff9c14b7d41c4bb1b5f319e7ba6d9ff554d6706c5a7268fb5c4efc6af2bbaeefdad9f8db5ff5838b4faaf3dd7206cafc5da501231f206ee3772c7a04a36b51843c6a4e92eb98ce844d680a945d84e1a910e90dda1a4e3138a643cf88a90020e3df081ee65e54fc0b1f65e75a3b3a768705967cf27cd6846f2a4df895713b7f72efc5d47bfdb999cd0fe9aaef881957ef4d6c7750071f3eced21ac70d501f221dd4856bc91dcaae8ba4403e25574b48c4d7c75a4e224bbced21ac70d501f221de40dbf578d38e623d08a4ee4590931b0879feca0e5028b09d52f9af9f0090ac|ql0NJZkSsp1RxAXSHJFakdUR5UWeKBTZIpEbZdlURJmM5M3STVDajhkQsJWbR9mYtFjehhlTrJmbwMXYuFlbPlmSOJ2MwBnYqVVdPRVSnR1V5kWYHZEdMdkRotUUv1zJq92SJNUQnl0QBdWSqVFcDlWQnl0QBdWYWRHZD1mW2NWaCBXSoUGZvNWZkRjNi5CNXV1Sa5mS2J2UCRHZY50ail2a2MUaBdWStlTeidlRws0RFB3S2U2chJGI0J3bw1WaYpEakFTOwJmbCFDZDJ0dj1Gb1R2QCl2QHhHaMpXV110QB9GV==QKp0VMtojObdSYDdWaU1GOntERBRzSR92ZJNUQnlESSBnYthDcDdGcwMGRxUVYDF0ZJNUQnlESClXYTtmNDlWQnl0QChWWXFzdiNjSwkESKx2YpF0bTBDaVRVV3NXSn9maJNUQnl0QBdWSHxWdkNEa5lFWkZWYDF0ZJNkQpBFWKx2YFZ0djdEesZlMWl2UTpEZJREM5k0QJdXSXVDMJN0ZphFSKJWZThTMNp3Y11keZlmZygndZ1mRzl0RFtUSDpEdjJDb6p1R0k2TYJEMJVkV0klMWdHZHpUeadlRyN0ZvpWSYZFbjNjU6xkbCZ3YDJEcihlQ2NmbRdmVTFkNJNUSwNUbGhGUXVzdkhVUvl0awFjYFVjdkdUVn5UVFBXSXhHMhhlQ5JmMOx2YpJkejdkR0t0RxoXYHZFaadkV5NmexETWn92ZJNUQnlESClXYXVzdkhVUvl0awFjYXF1ZPlWQpt0UrB3QphjdjJTOplFWRVXYXVlNDlWQnl0QCBzYHxWdJhkSoJWbkx2S2U2chJGKjVGelpANxYleahVS0F1VkxmYutmNDlWQnl0QBdmWz4Eci12Y1N2R5YnYygTdhdVU2l1VwhWZXl1ZZx2cpllM5smWBBXMZd1YnB1UCdjSYJEbJp2bpFGSBlGTHxWdkNEa5lFWkZWYXVVdjJDespFWB9GTXVzahdFa2J2VVVXWn92ZJNUQnpFWopmWXhHahNUQ2k0QJB3SyYVdadkVrl0UJVnWuJ1dM1WMoN2Qop3YThzMOlHN3xkaNRjTzE1bJ1GawQGSCp3THhWeadlRrV1R5YnYIR2bhdFeslkRSlHZXhHahNkQVFGSKxWWIpkdhdVUn5Ue0gHTXhHbJZkTopVbGlXYHhHchJTVnJlMWpWYR92ZJNUQnl0QBdWSXVDMJdUVLNUb1YHUygDcJVkTvNWb5QnWywGMMpXV65Ue0onTIpEbalXO0NmMspnWHxWdkh1Z3kURGVnWDF0ZJNkQsJGSOx2TYZFbjNjU6xESSBnYRBHaQRVQLNUbSxmWXNGcM1Gc6JmM082SHxmdilmQoNWeCx2TzEDZJZkT3l1VwcWVHVDSahlUQRGSBlGTDJEaMRFM01UUvdWS|9|16!-!4e524314bdbe496c7272e7353b890f694051ef92593bab8e181694f5c80d67859fa2b495afa614c9334ebd5e39e6a4a2e819e56d86a6a92caa076d235b84f2d64a261b01f2d09e4efdd9bbeea41b20f0f3cde3cc37a114c54c78fb5ed5f271ba5834b03cdec4a9edca7ead936a533108550ecbc54d84575ae17556b843cc85f2e146020a8d1532b7012f4f74eee529348b5ccc3aed2b53432c11f0933679c6288775103fe486bc359e48080ac2efcad96ace9d80caee9e18cf3aed504591c06162779a2ab0d07abe83cb785ab4a7c9b75d832a76ea70fd85014a2748bbc82cc8eca0021eb0f92031d597850f2b3af66eb9d5592560661c763777e2bc9c6c1886b78d0a758e27f9c2d732a8ce9dd561f3b9a09e3aa784bef5cd327fb2cc4f7644429c3fd0ffb2cb7fcf9e6241c3cfd00928d1cda3321e6ae749a553d40ceed2e1b1ed40c2f1c6a7b6ef8bdbee2934a7f1dbbde307913d5499d3296ffd76d03e45538094f44f9b313ef8bdbee2934a7f1dbb0648c6591caa534f04a8f36187f9200bf442dde3117d2dcd7c999fb0f9737e3",raw_input("Key : ")))
