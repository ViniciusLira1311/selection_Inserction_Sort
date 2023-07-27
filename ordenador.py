class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores) -> [int]:
        
        for i in range(1, len(valores)):
            key = valores[i]
            j = i-1
            while j >=0 and key < valores[j] :
                valores[j+1] = valores[j]
                j -= 1
            valores[j+1] = key

        return valores

    def ordene_insertion(self, valores) -> [int]:

        for i in range (len(valores)):
            k = i
            for j in range (i+1, len (valores)):
                if valores[k] > valores[j]:
                    k = j
            valores[i], valores[k] = valores[k], valores[i]
        
        return valores
