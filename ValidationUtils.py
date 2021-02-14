def KFoldCrossValidation(dataset, k):
    lista1 = []
    lista2 = []
    temp = []

    n = len(dataset[0])
    nT = int(n/k)
    a = 0
    b = nT

    lista2.append(dataset[0][a : b])
    lista2.append(dataset[0][nT :])
    lista1.append(lista2)
    a = a + nT
    b = b + nT
    temp.extend(dataset[0][0 : a])
    temp.extend(dataset[0][b :])
    # print(lista1)
    # print("\n\n\n\n")
    
    for i in range(4):
        lista2 = []
        lista2.append(dataset[0][a : b])
        lista2.append(temp)
        lista1.append(lista2)
        temp = []
        a = a + nT
        b = b + nT
        temp.extend(dataset[0][0 : a])
        temp.extend(dataset[0][b :])
        # print(lista1)
        # print("\n\n\n\n")
    # print(lista1)

    return lista1