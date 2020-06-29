import json

import requests
from Crypto.Cipher import AES

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
url = "http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?complexname=%E5%BC%A0%E5%AE%B6%E6%B8%AF%E5%B8%82%E5%8D%97%E6%B2%99%E5%BB%BA%E7%AD%91%E5%AE%89%E8%A3%85%E5%B7%A5%E7%A8%8B%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&pg=0&pgsz=15&total=0"
resp = requests.get(url, headers=headers)
print(resp.text)

class AESDecrypt:
    iv = '0123456789ABCDEF'
    k = 'jo8j9wGw%6HbxfFn'

    @classmethod
    def PKCS7Padding(cls, text):
        """
        默认即为Pkcs7填充
        """
        length = len(text)
        unpadding = ord(text[length - 1])
        return text[0:length - unpadding]

    @classmethod
    def decrypt(cls, content):
        key = bytes(cls.k, encoding='utf-8')
        iv = bytes(cls.iv, encoding='utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypt_bytes = cipher.decrypt(bytes.fromhex(content))
        result = str(decrypt_bytes, encoding='utf-8')
        result = cls.PKCS7Padding(result)
        return result


enc_str = "95780ba0943730051dccb5fe3918f9fe0b265875366ec51d2bbc4ecc85d8dc5a07266f919782fa6c4b95644825dbbaba8ae3de673dc4684431d3bb96a9afb87aabddcf189375f1ce633cd074880a0a05a51dd7ee10d492a5874ec2f3879639de"

data = json.loads(AESDecrypt.decrypt(resp.text))
print(data)
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome
# 需要在python目录里面把Python27\Lib\site-packages下的crypto文件改名，没错，就是直接改成Crypto
# C改为大写
