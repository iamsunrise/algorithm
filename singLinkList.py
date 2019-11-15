class Node(object):
    def __init__(self,item):
        self.next = None
        self.item = item

class SingLinkList(object):
    def __init__(self,item=None):
        if item != None:
            node = Node(item)
            self.__head = node
        else:
            self.__head = item

    def isEmpty(self):
        """是否为空"""
        return self.__head == None


    def length(self):
        """是否为空"""
        count = 0
        cur = self.__head
        while cur != None:
            count = count+1
            cur = cur.next
        return count

    def travel(self):
        """遍历节点"""
        cur = self.__head
        while cur != None:
            print(cur.item,end="")
            cur = cur.next

    def append(self,item):
        """尾部添加"""
        node = Node(item)
        if self.__head == None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        
    def add(self):
        """头部添加"""
        pass

    def insert(self,pos,item):
        """是否为空"""
        pass

    def delete(self,pos):
        """删除指定元素"""
        pass

    def search(self,item):
        """检查节点是否存在"""
        pass
        
    def remove(self,item):
        """删除节点"""
        pass

if __name__ == '__main__':
    ss = SingLinkList(1)
    ss.travel()
    ss.append(3)
    ss.travel()
    print(ss.length())
#    print(ss.isEmpty())
#    ss.append(2)
#    print(ss.isEmpty())
#    print(ss.length())
#    ss.append(3)
#    ss.append(4)
#    ss.travel()
#    print(ss.length())

