'''
有序表查找sequetialSeach    o（n）
无有序表查找orderSequetialSeach o（n）
'''



def sequetialSeach(alist,item):
    pos = 0
    ret = False
    while pos<len(alist): 
        if item == alist[pos]:
            return pos;
        else:
            pos = pos+1
    return ret

            




#def orderSequetialSeach(alist,item):


if __name__ == '__main__':
    alist = [1,3,2,76,23,678,45,46]
    print(sequetialSeach(alist,3))
    print(sequetialSeach(alist,37))

