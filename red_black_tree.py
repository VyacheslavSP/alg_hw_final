
class Node():
    def __init__(self,val):
        self.val = val                                  
        self.parent = None                             
        self.left = None                                 #  левый ребенок Node
        self.right = None                                # правй ребенок Node
        self.color = 1                                   


class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # вставка
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Условие -новая нода всегда красная

        y = None
        x = self.root

        while x != self.NULL :                           # Поиск позиции для вставки (левый или правый ребенок)
            y = x
            if node.val < x.val :
                x = x.left
            else :
                x = x.right

        node.parent = y                                  # Родитель- у
        if y == None :                                   # если без родителеля то корень
            self.root = node
        elif node.val < y.val :                          # проверка по значению
            y.left = node
        else :
            y.right = node

        if node.parent == None :                         # Условие- корень всегда черный
            node.color = 0
            return

        if node.parent.parent == None :                  # если нет родителя родителя-т.е. крень 
            return

        self.fixInsert ( node )                          # запуск балансировки

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node


    #  левый малый поворот
    def LR ( self , x ) :
        y = x.right                                      # У правый ребенок х
        x.right = y.left                                 
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                              # смена родителей
        if x.parent == None :                            # если без родителя то корень
            self.root = y                                
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # правый малый поворот 
    def RR ( self , x ) :
        y = x.left                                       # У левый ребенок х. аналогично левому повороту
        x.left = y.right                                
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                              
        if x.parent == None :                           
            self.root = y                                
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y


    # балансировка про вставке
    def fixInsert(self, k):
        while k.parent.color == 1:                        # пока родитель красный
            if k.parent == k.parent.parent.right:         
                u = k.parent.parent.left                  # левый ребенок родителя родителя
                if u.color == 1:                          # если его цвет красный-перекрась в черный
                    u.color = 0                           
                    k.parent.color = 0
                    k.parent.parent.color = 1             # перекоась родителя родителя в красный
                    k = k.parent.parent                   
                else:
                    if k == k.parent.left:                # если к левый ребенок
                        k = k.parent
                        self.RR(k)                        # оверни направо
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:                                         # если левый ребенок
                u = k.parent.parent.right                 # проверь правого ребенка родителя родителя (u)
                if u.color == 1:                          
                    u.color = 0                           # перекрась u в черный,если был красным
                    k.parent.color = 0
                    k.parent.parent.color = 1             # перекрась родителя родителя в красный
                    k = k.parent.parent                   
                else:
                    if k == k.parent.right:               # если к правый ребенок
                        k = k.parent
                        self.LR(k)                        # поверн налево к
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)              
            if k == self.root:                            
                break
        self.root.color = 0                               # принудительно окрась корень в черный




if __name__ == "__main__":
    bst = RBTree()

    bst.insertNode(8)
    bst.insertNode(3)
    bst.insertNode(4)
   