####    How To Open This Script?    ####
###     Use unlock Function         ####
import getpass,hashlib,base64
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

def unlock(key):
    exec (decrypt("f71ac2e2122310ca2bbd2c486d048f4c8304bc74b82240cddc02e033497e8d2842be370f1391a815a00f2d4328c463281be10d4f97be015d38fbd26b3bf12feec191bfa3ef2ba293ef37c579476878093a985950d4649f9007568766bea45037f68dc444b0c57e087c30d7fe5e7ce9ded42a70fe1f8babb94a6b6052fbdf9156ef0b4c437b8507de0d9e7db6baeebc1d0f61b478e9a05126b8bf1c58b3c5c2e702d6225b8b4b988cdc9973da7c86f1347123d4aa07c755562648ed4f781a1a91884997fb6522f1090f808d29b73ed050d4b5f6fcc1110b13be8b226585b02ce39bbc5087259ac89eb968eafadd39b8ef87f3d115bad8ba30a4fd4c6af51756df1dca07b3dbb90af3043076abf06b3847223846b4a97db9d4f9baca33abc0666f|Gl3STt2SiNjQsJWaoZHZYJ1dkhVUzlkbjl2STVzMj1Gbwo1Uoh2YzUFcD1WM1kVbW1mYzoEbQZFdkNUbxUjYHZkekdkWyBlV0R2YtZUdadUO0xkbOhmYYJ0caNFazFGWOBzSHFTNidkR6R2RaJ3STh3cadFNvJGWsNXWY5EMa12cwt0UrtUSDF0ZJdkR1FWbGVTSWWXVTcZhFbiNWbGVnWHlDdM5mSoJWbSBnYuF1bNNEezp1V08WWXVTcZh1awxEVFBHWR92ZJNUQnl0QBdWSHZUdh1mR1wkbKxmYWaadlW2NWbVZzQpF0ZJNUQnl0QBdWSDF0ZaJjVwkVbW1GTtZ0djdkV1p1QoB3SR92ZJNUQnl0QBdWYXl1ZidkV1t0RxUjYHZkezoEdZhVUvlFWkJDTIpEbjhUSvlFWjB3STt2SJNUQnl0Rs1WSHhXMjNUQoB1UBd3Tn92ZJNUQnl0QBdmWtlTeJd0anF2V0cmYYx1ZjNjU5t0R4FzYDtmcJlWQnx0UwIHTTBzZJNUSyN2MSl3SHhHbilGaoJWbwhWZTtGcDlWQnl0QCh2YzU1ZQNVQpF2VxcnYzoEMzIVMk5GZ0UGWv52STNnbKlXNxJmMsV3SIpEai1mU2J2U1oXWXFzdidUVvJ2VGd3SH50bjl2dnNWbGVnWyU1bOR0ZzlERVNzSTFwFWb0NnYXVjdjhkR5N2MSFDZuRGNlh1but0Uz5mS5VTciJDb1tESKhmYtJldiNVN6l1VxcnYHV1bidlR3t0RO92Ypd3Zj1mR1p3QuJUehdVNwk0QoNnWXRzbZN1awNkbah2YqFjYj1mR1p1R5QHTt50biJDbqp1Un5WWXpkaadkVtplMoBXYtR3cidVN2NGSGl3YM5mSoJWbSBnYuF1bNNEezp1V08WWXVTcZh1awxEVFBHWR92ZJNUQnl0QBdWSHZUdh1mR1wkbKxmYXljMaNFaupFWSh2SR92ZJNws0UrZzQpF0ZJNUQnl0QBdWSDF0ZihFbtRGVxkXWXVzaiJDM1llMoZXYX5EbLdUM1I2RGpHZHplcLF1bnl0QBdWSDF0ZJNUQnl0Rxg2Yu50bZd1d1J2R5gmWI10bl1GewlVa1smWX5kdihlQ5pFWOp3SIRXOLN1awlUa10mYzoEdZhVUvlUazlGTtBndhdFNvRWblMV9mTEd2cJRUVzs0UBJXSIpEai1GZstERZFDTDFUNNN0antUeClXWXVjbaN1Z14Ue3dWTUlUeLN1azlESKhmYtJldiNVN5l1VnllM5smWYl0ZZNjSxMmMoNmYuRXOYdUNsV2RWp2SHFDaj5mTvl1V3VnYHlDaahUTvVWb4BXWpVzaadlT2JGWClnWY5keLhEd5svdWSptGcD1WOxQGSCFDZEFTeZhFZmF2V1cHZYF1bJtWOxQGSCFDZDFkNJNUSwNUbFlzYzI0chhlUwoFWJ9mWtd3cidkR3FGWNBTtmNDlWQnl0QCh2YzUVOiNjQsJWaoZHZYJ1dkhVUwxkbKxWWXF1bLF1bnl0QBdWWXVTcZh1anB1UCJWSuRXOQhFd5kUa10mYzokQpRGWOxGZDFUOJRUR3NUaBdWSDF0ZJNkQtJ2MJdWYTJEcilmQ5l1V14mWThWeZdVNrJmMwU3YtZUdadEb1R2QnFDTHpUMjJjVnlWSDl0cJlWSwtUUvdWSDF0ZiNjQsJWaoZHZYJ1dkhVUzlkbjl2STVzMj1Gbwo1Uoh2YzUFcDlWQnl0QCNHZYF0ZLpHMn1UUwZkhlTwE1UClUWX5kcahVSrkUa3lmWYhGbZlXSwt0Urt0QtJFbalmQ6N2R4BHZIJFbjlGaqJmMSxGTI50didEbwI2RWVnWzI1bLRjhUUvlFWOFzSR92ZJNUQnlFWkBnYtN2ZQNlQ6N2R4BHZIJFbjlGaoRmMsVnW5h3cadFNvlFWkBnYtNGcJNEOnNWbGVnWHlDdM5EdZhVUvRWbGl3Y5hXeahlQ5t0ROZnWHVFcLZFMLl0QBdWSHRGbkdkSspVaBlTSGRHZDlWQnl0QChGZywWdalXQ5k0RWVXWzoUNWYXRzZl1Gb3t0RGNTYXVjbk1mR5x0RGNTYXVjbLR1bLl0QBdWSDF0ZJNkQoJWbwhWZTVDajhkQsJWbR9WSuRXOQhFd5kUa10mY3YHZVdLdUOxQGSCFDZDdXaklXSwxkbklXYYJFbLdkR6R2Urt0JoUGZvNWZkRjNi5CN2U2chJGKjVGelpAN2U2chJGI0J3bw1Wa2ZJNUQnNWbWBDZYpUdJhEczF2VJVXWykDdjhkSsN2MN9mYXZUejJDaoJ2Q1sGZXFzdjlHaqJmMxcXYXhHbLdkT2p1RVNXSqh3SkcJhkSoJWbkx2SElVMMNUQ100Qrd2S5JUeZdVNup1UnVjT5d3ZNRVS5t0UrNXSIpEai1mU2J2U1kXWXVzahdVNwsERNNnT5tGc==QKp0VMtojObdSYXFzdiNjSwk0Rxg2Yu50bZd1dzNWbGVnWHlDdMhEczF2VJt0QtJFbalmQsJWbOlXZYJEMLdkT2p1RVB3Tn91sWYXVDMLRUTz5UerB3STJUbiNTSnF2UCBnYpJUeZdVNup1UoNnWXRzbZhFZwJWbjB3SWBzSJNUQnl0RaZ3YpJEakNTWzlFWjdJdUMoNmbO9WWXd3cl1GewlVa4pXZY50Yi5mT1MWe1onWYJVeadlTxMmbOBnYyUzchdVMwR2QnVzTUtWNPR1awh1R0omUXVjaJV0UrBXSpVTbiNjS0lFWR9WSshXdJlWNxJmMsV3SHZUdh1mR1s0U3l2S5lUdh1WOwJWaohGZywWdaNjWoNWarV3YtZ1didkRqp1U0RxUjYHZkekdkWyxkbKxmYXljMaNFa0V2VaFzSR92ZJNUQnl0QBdWSDF0ZJdEZsR2RKxmWpVDajhkQsJWbR9mYYxWbkN1aLl0Qnl0RGVXYtZUNM1mR3N2RWVnWDhGcLF1bnl0QBdWYXl1ZihkV3lERwkTSHhHbilGaot0Uwg3Tn92ZJNUQnl0QBdmWtlTeJd0anFBdWSHFTNZ1mVtJ2MKxWSEBzZXFDMLl0QBdWSHpldjlmQwl0RsVXSIpEai1GZstERFFzSU92SJNUQnl0QBdWSDJkbahlUolERwcUdaJTVvNWbGVnWHlDdM5mSoJWbSBnYuF1bNRVQz1EVVB3SU92SJNUQnl0QBdWSDJkbahlUolERwcWWXVTcZhFbiNWbGVnWHlDd1t0ROZnWHVFcMhkT3J2RsBjYHZVdaNjUvtkVws0Qtp1cQdlV1l1MKVzYIF1biNjQsJWaolXWYRmZhdVN3RGWR9WSrpFcidUVn9CRXZXhHajNjUtFmevtUSDF0ZJNUQnl0QBdWSDJEai1GcoV2U1g2YIJEbi1WUvF2UrtUSDF0ZJdUM1I2RGpHZHplcQdFewN2MR9XljMaNFaupFWSh2SR92ZJNUQnl0QBdWSHFTNZ1mVtJ2MKxGTtZ0djdkV1p1Qo5mWYJFaLF1bnl0QBdmWtlTeJd0anF2V0c2YtZwk0Rxg2Yu50bZd1dzVWb4BXWphnelhlTjJmbOVzY5VjeahlU5p1VOFzYu5EciJTNzF2VxAHZDdWNPR1a18EVrBHWHVDbldkVqt2V0cmYYxWaadlW2NWbVZzQpF0ZJNUQnl0QBdWSDF0ZZdVNxlFWrVXWYJ0dadVNrt0RrB3QpF0ZJNUQnl0QC1mYzk0ZhNlQwJWaEBzZidEb6R2QolXWXVzaiJDM1NmMGR3YHhHbLdEewN2MR9WWXVTcZh1awx0R4xmYphGai1GcoV2UrB3SR92ZJNUQnNGSKBnYuF2QthXMjREM3NUbaZ3YpJkMZhlS6x0ROZnWHV1ZhdFNnNWbGVnWHlDdM5mToJGWCNnWThmNhhVQvRWbGlHTHVEcMdEesJWaoh2SUaBl2STtWdj1mVop1QnB3SRB3cZhlQwNmexMnWXRzba12dwl0Q4cWYXVDMLhkSoRWM5AnYuJUMkN0ZpR1RGdXYY10ZSdVNqlERVOxQGSWlmWTFkNJVEcxM2MSJUSFhGaZJDdsNGb4VXSxIFbZdFMn9UaCNkYHZkahlnQqJmMSx2YpJkaj5mV6FmR4VXYXFzdiNjSmSoJWbSBnYuF1bNpXQz5ERVB3SR92ZJNUQnlFWkBnYtRmMZhVSnB1UCJ2YtZUdadUO0xUbO9mYywmaaN1Zul1VKpmWHZVbaJDa1bLl0QBdWSIpEbkhkV5JWaCJWWykzaaZFdw9UbrJ3YzI0chhlUzp1V14GZHhGZJdkW2NWaCBXSHxWdJhkSoJWbkx2SEF0cidkVLNlQtJ2MJdWYTJEcilmQ5l1V14mWTh2cadFNvl1UrBHWRBHajNTV5kUaOZkYt10ZR52anNlbWpHZFV0ZTdkRqFmMWlHWHRjaXdkS1kURwFzYzIlQJVEaollM0x2YshXdJFDb2RGWSFTWtV1ZPlmQLRGWOBTUTJUSZdlTypFWKNmYp5UVadlR0lERvdWUthHaZJzcUQnl0QBdWSHFTNidkR6R2RaJHTtZ0djdkV1p1Qo5mWYJFaLF1bnl0QBdmWtlTeJd0anF2V0cmWyYFMZ1mVt90ZvdWSDF0ZJNUQkdkWyt0UBtSSEl0dNR0bLl0QBdWSDF0ZJNUQnl0RKFzYyYFMJREMn5keBtUSDF0ZJNUQnl0RWN3YyUlNDlWQnl0QBdWSDF0ZJN|12|98",key))

if "__main__" == __name__:
   unlock(getpass.getpass("Key : "))
