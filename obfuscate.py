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


exec (decrypt("955e011cf7e35ada586c677d919fc9225b8888272a33daafaada396cc064c0ceed3a0d777a3e86eaf09c4212d8c2d2366baba385579f466bd500fa013be98f89391b081cdb53eb8088f503b0ebde7aec967f40ca30739baedcaded5c678cfea17b3ecb02b355f67a5e36e204e289efa727f754913aaa5b36e204e6534424266f4c3a4ba7871310b5b4a6d98cedccfb98e8fd6b747ef4a14e883739cfb9e52376bb7cf3ae10ca6912acdf716e2120fdd5b4ff8fd324cbe96c2b7bc0afbd162ad80ee5a670b5282793b65a39e8f845270460cfd4a92e319b67b7432633095b7ac2d492b2a69fbe16f039c54fe56d5425d27f0f28337cb31a61b474842784a6d12d79a32516fd25350ef246e9ddc41a8a0d7ff117fc42018b54433f584b1935eb937c1f950ef246f0831aaa54d0d95e217a350ef2461537b2ede3092af03340ea56a6dd3e9e3fb7c9dee3c2498f5c96cec35cc14643288e5e4cbe3f37b00b34c9e0932acc368a4ba2309ad7390a68c705b13533a535263c17614f90b83cbd9fd920ba40cc6ba49960ac64cc40ae8702d1f03340ea56a6dd67bdac9042356bf039c54ec43eef93643ffb4c004128e9909364b41ddad2f235f0661e6f68b3c871a0bbd3d42ad78bc0b71ab27d450ef24695408b2e625873e6ab6f359fb13f2f6f2f78230ce9002173ce0ef9937aa3702e3b1f7031d061d871a0bbe166d8e3c6473238f0931e0b10c5d1b7da9119d9c2bf6f7998196ca8af1c9a1d3383dfb20ab77014a3a14e65b43b47c72febbe1e480d41b8b8ade15d1920cd0937b76cd11e035eefe8e17b5cd4684164a68ceb9b6fef6105f98ee2f039c544307d8eff28858efbfb046be776c070f0ff16f4443dc148f2c02f476ee5d5ae2a2a372665d120ac0cad0d7e55aa901ca924841749dc253bc832b02a91e9f8b5e6a1518c8601fa115f153e8bd8e934c71754825939dbc324defa6874aba74689391b0a7b9716c160c59135ac6bfbeb68d0e35993929ace4ec8e214ed26694dfe9b3fdc0e96a0a4758c747ef4a58aadcb8ef89c5b211d8d3bf26e0cb791ccd5a8070acb73d3e67212252fde18551c61a7c32c962089df15d06958defa6871d181c9867e76102d0e12bb8eaa4d3383df97502bb607d2eee96c2b75b55f9433daafaada396cc064c0c9ec271c5482593637344be0daa33f54f3cf981cdb860e58865eefe8e2347d4b6d2784b2a9fe268511a57dc148f2c02f476607d2eee96c2b703439fd3a9271ccb82b3036fbcebf3d6e1edb472910ddefd546c4606a6f2a3d97502bb607d2eee96c2b79c603a26be776c5a005ab3529ceca4c3759936d00561ba4a491844d7a55ed95048e897c446720d533c477f3a6ab21b0f19607d2eee96c2b7d20aecf1dc8542e7f3c88ef34c85e808456293e89af10993bcb0f7155131da1154d78cd9809a01857998517780e639c0515d06958ad612961d181c95eb782de934d2c49bc076a33e9a5072666280d41b86e8c1c0490c2eb747ef4a58aadcbf32853a3ffd4084ad2fc3fd29ab86492ba6a4a3c81ba5fff8e3ca9cd87f10039f90d9a7e1d9940c16c6f30dd1a0acc368a97502bb91864fdfcab9db2b4579b97502bb91864fd402cf7fd86a72c97502bb7d632a88504600b2df711bc2becda8633dd7dda29f1d546f75483e94f5a9069f5d173ef095c5115b2cc9f94e0614ce35e60b979667b4c86cffd19de30dd1a0acc368a97502bb91864fdfcab9db2b4579b97502bb91864fd402cf7fd86a72c97502bb7d632a88504600b2df711bc2becda8633dd7dda29fa4a3c81ba5fff8e3ca9cd87f10039f90d9a74572d207c2d7816f444324e10f1a0a18a9ba4e68430007d5f3d6e1e9981161639feabe161476dab00713458b881fed2d24455101b46298eebb5013871a0bbf090c9d490c96f6be776c34d6a55f090c9dc20e43861176fbc767dbe48f43847c9dee3981cdb88196ca84131cd7f137aa9981cdb860e58864a5866627729be1dc8542e7f3c88ef34c85977dfe7b51d6d93c3dfe14696563d95c376f7a9273cdbd9a9099f4185ed541b548afdea92da0c0a690b0bb7616b402670c3c3dfe1fb401b4a4c3759c24ca92bab1e65bb6c34b6611d389976238f892c3b3380b259faf3c4f42412ee3d25f81931b92402a3522fa820e5aee7fac0fd6f13e036e8dcaab14e866744ab94070f9354b134a27b3027612e64bf692059fdaac6ecd20084565ce4f9e023526cf5e9b7a3707632fad2a8e6e1ad88e3340210d50ef246bb3db4a7eb2191f03340e5580dbc80bad71db388f1eca53dbdd20f63e77b5083526cf5e9b7a37c29215f7255aa6cbef64197502bb43caa1df85bc88de26569ecd2f835929736313445903ce7fddea3f843bc1ac53278d4331c10fc47ab07efb64bbe438996fe11dcf1402670c7614f90e142b7ac1477bc8b1ac7e5929736c21b96bdcf9dd697502bb19244d29c8996b236caeb768b7bdb8928cdd1c457abfe0d5d3fcbd780afb6e216f444324e10f1340210db55a0731fda078a55ed959228ccc7873f08f230ab471a125bf03340e890900160119427c9dee3c6ecd20084565cdf02281042bb08108d1fc5988925e310fcc42d85e7b719ca9fdf9157191c1d5c3d98769976238b3734953e9ae151a4cc8035263c185be92861b66f571223e3afdd4bac9ee86fc0fd6f18d8669c08e95262888eba3a3e352acc368a902c264c8362ebc60f7640d4d68f71324eeccf647d1cb1aacdcf13fc4c982e08049c65c7f19c672908cf1a91c8881bf290e13dd7045ee6bf1a91c8881bf290e13dd70329dcbdebb5013871a0bbe166d8e3c6473238f0931c7cd828cebb592d32af3b461140db793229afd0e051a3905df739cfa6278034bed83b99e06b7ac4747d1cf37fac04ce4f34bec62b58fe83b34cb9cdae3a8725b90680f89cc918190a7bc0cafaa711fb4f8c8601ff8586933ee89581ec2f26c0a55b3771ae1d212413fa2bca5f7ccc2db0ac812bc4aaabd74eda374f261547e983b175cf93530c011253a6ac7e8d752a5ce3ec9aaa8df7c24ca468a710f0b9d6e741cafff37551c84e874a6868c705bb46298e3245090eae025482ca6b727f1e84ded062983e8628830a33605bb91e15c2d9689d7781b08180f310ab66f117fc47614f901f75919ce7edaf63ef66ff8c9865901d22fd80e4d64d998485c63b7275db63de42bfd158c4f1a2f7ec32e734e0659ccbd81cd23fdb1b11535e673237a3fc37af259cea29f0333d516017a3fc37e354adefb4451779f8dfd357f7568c8601fc1a55aef8ccdb67a3fc378c8601f5d03f2546c247f7a3fc37efcb2d57ffdf7433e509ace5b1a4efcb2d55d03f25c19e6f302c8cfd2b0b59cbc31abdc19e6f3095d85c8c8601f7ffdf74df4c11a406fb086b9b4fd6bfa502f8ccdb61b108672cfd580d328ac15e673238cde10d8a94c2821b053d5e673237a3fc372b0b59c372c3ed41a6e2df3abb93d4f868816f4443ce739fcd042bb78a94c28f23f05fdf4c11a0a4758c8a94c28ea8ac4f36fd5038cde10d8c8601f7ffdf745e67323348c59434b7d646683791008541c7a3fc3736054e6ca3b80fa2c82d202c8cfd2b0b59c38825f85e673237a3fc372b0b59cea8ac4fce739fc7a3fc378c8601faf672b5fcef6f5f7810bb8c8601f6bfa502f8ccdb61b1086736054e6f892c3b79f8dfd357f7568c8601fc1a55aef8ccdb61b108676b9b4fd7ffdf74bc2121f0a4758c8a94c28f23f05f5e673237a3fc372b0b59ca2083c733e509af7810bb34b7d647ffdf745e67323ab225496b2293d89d7781c19e6f3095d85c8c8601f7ffdf74575931d0a4758c8c8601f7ffdf7433e509ace5b1a42b0b59ca2083c75e673237a3fc372b0b59cca3b80fa2c82d2a0711e86b2293d7ffdf745e673231b10867e474f387ffdf74bc2121f0a4758c8c8601f7ffdf7433e509a4709b2eac47586d328ac15e673237a3fc372b0b59ca2083c733e509ace5b1a42b0b59ca2083c733e509af7810bb34b7d6489d7781fef78a2348c59434b7d647ffdf745e67323319f6416b2293d7ffdf745e673231b1086736054e6a163ce979f8dfd095d85c51ee3a4429b4ed41a6e2dd0898f878d2a37429b4ed41a6e2df3abb93f1054d316f444379f8dfd095d85cd0e87437ffdf745e673237a3fc372cfd580793944b008541c7a3fc378c8601f89d7781c19e6f3095d85c51ee3a4429b4ed41a6e2d8f7e824c0bebea4685a4b5e67323348c59434b7d647ffdf745e67323319f6418a94c28f23f05f5e673236a4fe688a94c28ea8ac4f36fd5037a3fc378c8601f6683791008541c7a3fc378c8601f89d778118c91d1095d85c78d2a37077f9d3a0c87d419b6e123f0a04db1528a45e673237a3fc37ef720e77ffdf7433e509ace5b1a48c8601f7ffdf74a6bf8bd095d85c8a94c28ea8ac4f36fd5037a3fc378c8601f89d7781fef78a27a3fc372cfd580b1528a47d1b25d49e2a028c8601f7ffdf7441a6e2df3abb932cfd58016f444336fd503ead4ef08a94c2821b053d5e673237a3fc372b0b59c6dbf8f933e509a4709b2eac47586d328ac15e673236a4fe688a94c28f23f05fd8dd40a7a3fc3736054e6ca3b80fac3c46e32edea73f0a04d4c08f7e8d891035eddfc6ab7029ede3473c3cca04254bde53371852fea8ac4ff5ba1144a7759b353b23847ce7eac0439e876418e4b5095129996855c19e6f3221a6364505d53464560bcb4db35ee516ce64b35b48f6dac58d198926f6d6673f0a04d16f444379f8dfd357f7563f0a04d5c588d5425d98c9611cb93f878a34c08f7e8d891035eddfc62b128604a7b406c0439e876418e4b5095127c5ebb5fc65387d0cd80a58d317d05745f7a0c87d419b6e123f0a04d15c90033cca04254bde53371852f2b726f4103ee201cb76dbfe7a17a4dd3317f47f4316a18704d6b47ad76bcf4481b41054a7759b353b238ea8ac4f194df14e745e44afe297068592b8f8cbc8bf35e1a64505d53464560b8dc436ef3abb932cfd58016f4443194df14e745e44afe297068592b8f8cbc8bf35e1a64505d53464560b8dc436ef7810bb5fd91ed40464b021ed2a19d0eb89e9b0a159e20dd8a0c87d4f3abb9336054e6d1af99ec494e3d357f7565fd91ed40464b021ed2a19d0eb89e9b0a159e20dd8c19e6f34774700e9b0a15474a4b4d564bb26a18704d6b47ade348b7ba0c87d46f6d6673f0a04d16f444355971c9d0cd80a58d317ddd2b6c0f9b93ff13aaa5b7854fc922491468d19892d84239e64b35b48f6dac512c63782f6df4de9b0a159e20dd8c19e6f34774700e9b0a15474a4b4d564bb213aaa5b7854fc922491468d19892f7810bb0e74f167bb6e2b4118fbfd3c0e463f878a34c08f7e8d891035eddfc62b128604a7b406e109203e63a6629b2fe084c08f7e8d891035eddfc62b128604a7b406c0439e876418e4b5095129996855e94890b6a18704d6b47ade348b7bc19e6f3d589d9464b35b48f6dac5f362bb0c33d102705ec1905b3b3db484ee3a4af2f20e74f167bb6e2b4118fbfd3c0e469e3fc2131ae60780ecfe8f3abb93b49df673bb0f58f57d6066a18704d6b47ad5a20a640472425e745e44afe297068592b8c020ff2d84239e8a114a6d2cfecd9a5dd8cbcf26829c35658540a789d302800c1c801d36054e6a163ce979f8dfd4774700e9b0a159e20dd8e94890ba763e0b185d0c74611fbab84e5e7d0898f8d91698a1fa0df64b9d54156eb7bde58311b4c08f7e8d891035eddfc62b12860ca3b80f06a1ea37eb219153a6ac7e8d752a5ce3ec9aaa8df77cf3ae177878cbe0daa33c8afcfceac15fda478e99e9a1763c17952da871d51bdf037456829f0d8e70aff19882c0359a20f1b18975e7ffc405e5cd1d654ccb85a20867eb21915feb489c6b52e18a85fa3457d0d3eb6bd9dd8a89aca1507d5fa3cf5ce67212293fda1e9908260043693598b177df31bfc35dffd76095d85c1cae63841a28135e67323afbfe4e2d24ee53ae8d35ff82a5d4d8796fc22ee36508ac8320879a378f396ce7dce5c487aef01225e876f4d140ebb50132f1add7cad7a2fd63297053a6ac7e8d752a5ce3ec9aaa8df7dcb53c886d5142458e887abcce855934bf897b1371a1d06547a56fa15fb2b6d8190a7bc0cafaa711fb4fc73b1f412dd0955df457ae87708a20795ab9389e0e1f7591955ea91159d4fdc45c2dbe0899e087872dba6be776cc96cec3249042f310ab660bef673dbba9944a191f907a28ef1cd57ac0359a2062546c9dff4f7c9cbb9a991b8ada2b708094a72adfdd7e59dca3b80fdc32ba4ef4df3489d2f9df8c9865f73614371b414b63a35ca8a20b0b5e673237a3fc37af259ceb1b11535d7f1f9095d85c2b0b59c54fffdacb51e63357f7563f0a04d16f4443ce739fc7a3fc37008364c7ffdf7441a6e2df7810bb8c8601f7ffdf747d1b25d49e2a028a94c28f23f05f5e67323d042bb76b2293d5d03f25c19e6f302c8cfd8c8601faf672b5f8ccdb6348c59434b7d647ffdf74ccdedb11b108676b9b4fd668379126ded9d7a3fc3736054e620d5f1cce739fc7a3fc372b0b59c38825f841a6e2dd0898f88c8601f7ffdf74a6bf8bd2ba401d8c8601f5d03f257f97b2e490bdfec0bebea668379157a4d6c7a3fc378c8601f5d03f2546c247ff2a0c836b2293d5d03f25a0c87d4271583fc0bebea7ffdf74a6bf8bd2e650d68a94c283ee96bfa6bf8bd095d85c2b0b59cca3b80fa0c87d419b6e123f0a04db1528a4d8dd40a7a3fc378a94c28f23f05f5e67323d042bb78c8601f7ffdf7441a6e2df3abb93c04a0bb16f4443ce739fc7a3fc372b0b59cd63b4045e673237a3fc378a94c2821b053da6bf8bd704247c2b0b59cca3b80f2527c3e357f7563f0a04d16f444336fd5037a3fc3751ee3a4429b4ed33e509ace5b1a48c8601f7ffdf7413c1d620a4758c2b0b59cea8ac4fce739fc8cde10d2b0b59cca3b80fe4b3607357f75634b7d647ffdf745e673236a4fe682b0b59cea8ac4fce739fc7a3fc372b0b59ca2083c75e673231b108676b9b4fd7ffdf74a6bf8bd2e650d68c8601f7ffdf7433e509af3abb93b31c3bdd328ac17d1b25d49e2a028c8601f7ffdf7439a20fc6d1be008c8601f7ffdf74ccdedb17a3fc378a94c28ca3b80f7f97b2e490bdfec0bebea7ffdf745e67323319f6416b2293d7ffdf745e67323348c59434b7d647ffdf74ccdedb11b1086736054e6ea8ac4f79f8dfd095d85c8c8601f6683791008541c7a3fc378a94c28f23f05f5e67323ab225496b2293d5d03f25a0c87d4740ba273f0a04d16f444379f8dfd095d85c2b0b59cd63b4045e673231b108676b9b4fd89d7781fef78a21b1086736054e67b1dfdb79f8dfd095d85c2b0b59c38825f85e673237a3fc378a94c28f23f05f5e673237a3fc3778d2a37429b4ed33e509af7810bb34b7d647ffdf74bc2121f0a4758c2b0b59cea8ac4fce739fc6a4fe688c8601f89d7781a0c87d4a6b0e063f0a04db1528a45e673237a3fc37396cdba7ffdf7441a6e2df7810bb2b0b59c6dbf8f95e673231b1086736054e6d1af99ec494e3d357f7562b0b59c38825f841a6e2df7810bb8c8601f668379157a4d6c7a3fc378a94c28f23f05f5e67323ab225496b2293d7ffdf745e67323172815836054e620d5f1c36fd503f2a0c836b2293d5d03f2546c247f7a3fc3730e799c429b4ed33e509af3abb93ebb501316f444379f8dfdd589d94a4211f4782f5c8fda23f904c73d0d73dc6031ae60780ecfe897a87860e74f1631ae60780ecfe801137ec5fd91ed40464b08ba143bf3abb93d4f868816f444355971c9d0cd80a58d317ddd2b6c0f19239e6a18704d6b47ade348b7bf47f43113aaa5b7854fc92249146f50d6bdc33d102705ec1905b3b3db484ee31728158b31c3bd15c90033cca04254bde53371852f47ce7eae109203e63a662871abc34a7b406e109203e63a66252abaffde3473c3cca04254bde53371852fca3b80fa0c87d4740ba273f0a04d9ee2d43103ee201cb76dbfe7a17af2c2873c0439e876418e4b5095129996855c19e6f377111ec705ec1905b3b3db484ee34fad60e9c35658540a789d302800c1c801db31c3bd4c08f7e8d891035eddfc6ee3de0d003fa3b85cf1765e423362cfd5809ee2d43103ee201cb76dbfe7a17a47ce7ea01227ecd0cd80a58d317d05745f7c19e6f3221a6364505d53464560bf5416089d0eb89e9b0a159e20dd8c19e6f34774700e9b0a159e20dd8e94890b13aaa5b7854fc922491468d19892f7810bb0e74f16c79cf404d97d1df6e9983da74ee35f04e0e13f9bf8db803ddfb56febc29215ff47f4316a18704d6b47ad76bcf440472425e745e44afe297068592b8c020ff24709b2eac475869ee2d43e109203e63a6629b2fe08062cff0823395fd316a03c6332fb02800f555971c9d0cd80a58d317ddd2b6c0f9b93ff13aaa5b7854fc922491468d19892f3abb93f1054d316f444379f8dfd4774700e9b0a15474a4b4d564bb2a763e0b185d0c74611fbab84e5e7f7810bbd91698a1fa0df64b9d54156eb7bde58311b4c08f7e8d891035eddfc62b12860ea8ac4ff57d606a763e0b185d0c74611fba68f76a99d0eb89e9b0a159e20dd8c19e6f3221a6364505d53464560bf54160815248d38a114a6d2cfecd9a5dd8cf3abb93b31c3bd5c588d5425d98c9611cb9e58311b062cff0823395fd316a03c6332fbea8ac4f55971c9d0cd80a58d317ddd2b6c0f9b93ffa763e0b185d0c74611fbab84e5e7f3abb93d4f868816f444355971c9d0cd80a58d317ddd2b6c0d564bb213aaa5b7854fc922491468d19892d84239e64b35b48f6dac5f50d6bdc33d102705ec1905b3b3db484ee3172815836054e67489b70907aee6692ff706b8ad1d5aee7fa77f4f5ff4e31c7c73b1f404fd8abab561ac77436325e24ee0c6b52e18a85fa3457d0d331d061dca3b80ff47ca8f71b414b63a35caf5e6b45f8bbe61043693598b177df31bfc35dffd768a5378647dddbadcaae1e38c8f63688705536f60b613ef9cd43ba2a5c5ff936984edc65ac111ab1d16a1866637b70c68b602dce20f345b5974b42bfa10af442db2e32884fee305bb91ec1c2413acdf3d934bb48c119d9c2bf6f7999e9bd5faa8231b30d47c4fe9353d3fddef2e0dd691a4a3c8137d0e2b49e5310901ca92f3d6e1eafdd4ba39a0e4d75cf935d4d0cb4f7a9273ca3b80fafacbcda83231d3112d8cca3b80ff9f6f85983fb58a5a78fd759e6760bfa7782cc54fff039c54fd4c62de0daa33613d83637c2539bdf037445180b9704247c1cae638b4f3e24373b004cdc0800dd7e59d556e3fd87a90086bf3e88561d494d600b7d5e7ee9f9c0d450d3da6254ac2b2e25552f1f8ae36851e68ed30562807885c081b3fad60726662fe5d1bf2e6fc1f8aedbe3ebb50135b80e269a5624ca179f5cc4747d1cf37fac04ce4f34bec62b58fe83b642670730007d5f3d6e1e99811617ffdf748d607bd9fd52f209f99cd174b285fbf544da91318fd842fc7245efdcf3eb7f09fd52f209f99cd174b285fbf544d9c603a26be776c82c3922f23a4feecca19d019e248a638515641f89a50d3c46088c02b62d4ac465fd3b101d5bc03285d6f75680e0cdd087a7a3fc37e354adecfebe814e1e1a8f155419c576741de6b6500ae60e674b42bf3fa50357ffdf7454c07a930d47c436054e6b271452732407df7810bb98b177df31bfc35dffd768a5378647dddbadcaae1e38c8f63688705536f60b613ef9cd43ba2a5c5ff936984edc65ac111ab1d16a1866637b70c68b602dce20f345b5974b42bfa10af442db2e32884fee305bb91ec1c2413acdf3d934bb48c119d9c2bf6f7999e9bd5f2723aa9c95a99d934b6660cca843db41eb360eab76768b7bd669a75bfcd8b016a33995511ba71405bd2228ab2b8f3abb934a5d464e7f3c88af1d03e487fe354a470b04f21ddbe22ccb8503b0ebbdebf1fed905e73554fb6a5ea4073411f9da1f34955e673235f90be6d935ae8afb61b3134c1faa4ba787cc39155adc6491af1c9a1042bb08108d1fc5988925e310fcc42d85e7c6ecd20084565c0fca07e103a99d1a4644b66ccb13a98a37c8e2f6611f9ba4649e5310180d0a45437b7636b7664a1bced44867df89ac414afcf4120871a0bbe0c5766d8b9f08181f92450ef24626fd9ed78219a61cd57acf8a425d5e7ee9fce0f0f4f03340ef927b82acd4f65881d31467cc72a700246e3cf684ce63a662747ef4a58aadcbe0c5766d8b9f08181f924e1b42b636fbcebf3d6e1e2aba5dcbc03d0ab5ed4f4329fccbe9b0a15871a0bbb9d3637f5937dd747ef4a58aadcb672e1d146a2a4fb021ac5fc6fb5c41b93b6a4ed7d4d6b47adf5a9069f5d173ea7d3620b021ac5fc6fb5c87dac033682b95981cdb860e588650dfa1ec27c829984edc67ed44c11857998c0b8dd04eebf3907b89f9185799824e10f1ea8145281bf2903d2a3b4fee7adda487472f75db60a92e109a6f2a3d1f9ba46a40314f6f52f5a102071832686e1383b74f26fd9ed78219a61cd57acf8a425d5e7ee9fce0f0f4f03340e58aadcbb9d3637f5937dd747ef4a58aadcbf5d173ec1c802466487be6fa2c0943f9ea15a87c8e5e3b6cb8f6dac516f444324e10f11f9ba468d0f4b53d2a3b4fee7addb8e9600f6a47a6c1616fc31b1e6d0bef67315aaec7baccb25c6d792e1f9ba4658aadcbb9d3637f5937dd747ef4a58aadcbf5d173edc148f2c02f476370d84af610c94ef29d1d88cf294fe624f7c16ba9c999f5a41f9ba4658aadcbe0c5766d8b9f08181f924e1b42b636fbcebf3d6e1e2aba5dcbc03d0ab5ed4f4329fccbb84497b58aadcbf5d173ec0b8dd04eebf3907b89f9185799824e10f11f9ba46529cc7e0e7fb1d17cded9902c26471706a0345c1c8135ac6b768b7bd0f7142ec1cb165059fdaa1cd57acaa727e8046bebf6005aa6747ef4a58aadcb319475a8c7f00b35263c1a597a06b9b84178706fa70497ec0e7f3c88d649e702788ee161245ef5690acf7fe8c9bacc368a97502bbcfad3e6345c1c88c7f00bcf830319227285d415352fa13634d6b47ad3b841fde673bd9a6f2a3d1f9ba468d0f4b56b9690c68148f53a9271c871a0bbf5d173ec1c802466487be04276aa9ca7f9d44399aa5eb782d63a2f5604c10ecf66da92d09223317192d31e3cf08ca3d8ab747ef4a58aadcbf5d173ec46594d8045326383b74fdbc6db4d8b9f08181f9247c4f25ece0e72772db4e1ba793fa4e26c54f301f28fd7412c3a9271c5a005abf5d173e0ff46d4a1162dff5a9069f5d173ea7d3620f95f1d3e1b42b6055d448881d31467cc72a700246e9ba13d4511ecd532df3d43c3dfe1afbac3b74b42bf5a7d7a9eeeba9a693094d999f5a4c4b76b3acbcd7029bbabb5e14215f95f1d3842be03055d448881d31467cc72af5a9069f5d173ec1c8024eca53dbacbcd701a45ce062231513227ed2b9930d716f444324e10f1c4a833c04276aabaccb25f0b8e221f9ba46ed3b9c04402872da13fafadef777b55a0731fda078a55ed952aba5dc04276aaf560c586005aa6f03340e0468618dfb5c662286b7ad5b4ff80b2f61340946c62b3185cf03340e2b9920abca9e0bedcaded33daafaada396cc064c0c9ec271c5482593637344be0daa339e9a855cc39155adc64919ebf0f915818c3b8d71a869d80055479ede0d4d68f659bd45cb4616ea4655be2127e651494381958950809a7859edcaded3593e68665a7eb183bc5d0c841cd0684ceb0e90ef80b1ef0bf60f55f61ebf62b94ac506f6dafb3186d08a939910fdaa6f802875ed38035e732f20c589279a2183bc5d0c841cdf96090a27cf11bf2d5d448361671d5453080d5e3c576330565e42509ae3fad8879fdb7183bc5d9d0ac384e5f0e6871a0bbfae0d2982c29a735263c1b0c44628e63b120355bd27597d27185a000b8adbd436cf4453acacd27dcdd5ea877473cddf497f89cc91cb4616ec611f899ec271c8f3fdac8511a579f30df5a14abc3ecd2f83d5ac4cd1970da73dfb3aa03b76ece14a5018c84af2b71fd8b2f096718c3eafc4514e9371a125bf03340e64b4d387022db97c9dee3c6ecd20084565cdeebba53f4c0d63fa503519244d2117e7a2999f5a44065450f6a47a681967c078219a657c4379a7549bdd66258faa864996d98478b2f525d5bdf1724ec502a2f096712cb1d6129df242a53ac7c23ca77be77a699a829a4aacc368aad19e961fe0266c60f76478f396c5ceb06b19ed94e892fe3a954ad9236054e6871a0bbd3d42ad71223e3f82dd9c51516a1965884904f0d68f82dd9c5e26aac55edd20d772bcc81b0c28b0c4462c37a837bd65ea809914fafc6fb5c42d671fe1d3987e59ccf65e4c5cea3feb1bca9db40c04bf0a017c47d88a343171a125bcc1bd84a40314f2e6fc1f52376bb8b6b26d19ed94e53c9b6e27aa6527a6dfb8cdfa37ba6cfe4eb2221f2777a3e8996eedf848dc7ff3abb930b9f2e78c3eafcc7f19c6d4150510ca6912b3734953529cecd35ffa0dea3f84356af9eb6ccb92503b0ebde7aec967f40ca30739ba88b6842627ca4f7c6747ed074f64b7d8c2b3acacd21215f02d7d6135adb98908b9c89b3c567a8e6cda6a9265d30e49d70849211e9f81480e8fb785be08984aa3b785291ceee8501e1c86a11111194df6b4c4595b53ee94d9685cf1ca3b80f17c1751478b4813d05f87ee2815d78c4789391e2fdcc1bd84a40314f5f73aa437f096da1162df308d01916f44432d2a9abc02f476ccf647d1cb1aacd1920cd0937b76cd11e0350dfa1e3152697da56e5e1b7e7fc38b98867508803f039c54fe56d5425d27f099e7926f739cfae35a3878822292cec42245a7d7a9f5a90697b98442da10b6fe84ead634da1c5a02f9e42fa73232160fe378edc3ee19f39be51f8a6f039c547eb62eacf992f146a2a4f0bef6735d06958ee1454fe9acc061494381041b341602759ec581f8cf03340ef927b82de66baf01d5bc03285d6f75680e0262fefbcdc0800a3b72e8eb53faa063e014dac6ddb154d78c637344b9c7165ec9d7e00984edc6c0f9e7134da52655ea91115f5b66a6ab87cf00f1a031c10fcb9abfe555f018d6a6ec23490c2ebed26694541274204c10ec0a4758c204ee1de3f4147d7d613503ce7fdb3291f5182392438dd7795e142150bef67307b89f918579985ed541b548afdea92da0c9a5624c48245be97502bbfadad2429bbabb50a1ae2777a3e86eaf09c3dff77f73a330cc04bf0a7f6d0b7a738e8236cf445aa6b07cb37349521f606e74b42bff039c54027612e44028723994d12c1bf06b48ad3db48bce8625f1e9939f5b08b271452c87e68ca54d0d9c9bb407b0c44628f99cf8999f5a4b31a61b1fe02668477ff174b42bfc86a57890716ff69450cd999f5a4b31a61b89104039aa3834d68d836b31a61b40378926138325fc3032520795ab19244d2c160c59a4dac861ec3eeca597a06e0cb87ffc2e3b5e8f84523c3dfe1796cb4774b42bff1054d3055f93c309fd2d999f5a4b31a61b1fe0266ae3a8721f119c297502bb19244d29c8996b514801889d2f9df8c98654ce35e62b3185ce08984a69d8005bdd994974b42bf69ab9080188ee11857998dc148f2c02f47618b1366e94890bcf1020b1f9ba46a40314ff84469396ea3a13458b882f222e5d8a7c38a55ed950726662ab9407056c3658b897f063b1f0d7871a0bbf5d173e685c9e0e19c7d1f94e0614ce35e60b97966ecd2f83f1cbf4c3b1f09eb6ff27aeb6bd9dff44b9d54618b2b253ddfecd2f83f1cbf4cdfe98d367477ea36054e6871a0bb3529cec288723e6b904aa871a0bbf5d173e685c9e0e19c7d1f94e0614ce35e60b97966421eb15cc04302ad6aadf010ead610085a1b37349521f606e74b42bf4f048d2ada396cc064c0c815e2806b8ad1d3fb14f1bdd994974b42bfeee7c02dd20f635da32cf0b2472fcc1bd84a40314fc5825975b55f943593e6813bd04140a4715d5b3df83f2e325caeb9188511a575ed541b548afdea92da0c1476ee174b42bf6fa33480ac812b2f849153307c3326e8e8a25600b8801befe7a56fa10497ec0b46815970685c13de4d38a965cae333ea0625552f18a5378623ca77b5716654eba2a4a4dc38a65feb489ec005be063e372042bb08684164adb02cc38eb3de0e39a14446e8c18b0c446226244e260eab765e287f2474842701bb9ca4da9f0fdc313ce91b990d0dcfda6441b8ff9e5569bfddc4f1458e8873540e6e37d0e2b3e9de153ff3bfc19f48eedb0ebd7daf0012c8a9db53145f12ef4462a50ef2462fbfba4bb7616b9976238b93d63b594da027c9dee33800c18b93d63b18fcdea042bb0868e7494fa28d482fbfba453a91da99762383f7104716a45f9a66c26f4ad2fc3fd29ab86492ba6bd5955afd21b2e74ff74348f4384be1412d59d4fdc5716654d728b92490c96f6be776c34d6a555a6b8ca4a0921facd60c5d780f1295d0ac0a342d7d5ee7bc3b7422a4158c643a342d7d35aab1d0afc3b3d8a5bae|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|7|4",raw_input("Key : ")))