class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None


class Lista:
    def __init__(self):
        self.prim = None


'''
crearea unei liste din valori citite pana la 0
'''


def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista


def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod



'''
tiparirea elementelor unei liste
'''


def tipar(lista):
    tipar_rec(lista.prim)


def tipar_rec(nod):
    if nod != None:
        print(nod.e)
        tipar_rec(nod.urm)


'''
program pentru test
'''

def length(list):
    lung = 0
    node = list.prim
    while node != None:
        lung += 1
        node = node.urm
    return lung

def invert_a_list(head):
    if head is None or head.urm is None:
        return head
    rest = invert_a_list(head.urm) # reverse the rest of list
    head.urm.urm = head # put the first elem at the end
    head.urm = None
    return rest # header pointer


def maximum_number_of_a_numerical_list_first_implementation(maximum_number,node):
    if node is None:
        return maximum_number
    else:
        if node.e > maximum_number:
            maximum_number = node.e
        return maximum_number_of_a_numerical_list_first_implementation(maximum_number, node.urm)


def maximum_number_of_a_numerical_list(node):
    if node is None:
        return -1
    if node.urm is None:
        return node.e
    return max(node.e,maximum_number_of_a_numerical_list(node.urm))


def main():
    list1 = creareLista()
    print(maximum_number_of_a_numerical_list(list1.prim))
    print(maximum_number_of_a_numerical_list(-1,list1.prim))
    a = invert_a_list(list1.prim)

    while a is not None:
        print(a.e)
        a = a.urm

main()


"""
                                            { empty set, if len(list) == 0
    Model matematic pt a) invers(l1...ln) = {
                                            { invers(l2...ln) U l1, otherwise
                                            
                                                                            
                                                                                { -1, if list is empty ( node == NULL )
    Model matematic pt b) maximum_number_of_a_numerical_list(max_number, l1...ln) = { l1, if list has only an element
                                                                                { maximum_number_of_a_numberical_list(l1,max(l2...ln)), otherwise

"""

