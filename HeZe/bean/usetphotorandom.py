# -*- coding:utf-8 -*-
import random, hashlib


def getuserphotorandom():
    str2=random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','0'], 36)
    str3 = ''
    for i in str2:
        str3 = str3 + i
    str4 = str3.encode('utf-8')
    m = hashlib.md5()
    m.update(str4)
    psw = m.hexdigest()
    return psw