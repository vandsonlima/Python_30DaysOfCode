

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lista_x = [i for i in range(x+1)]
    lista_y = [i for i in range(y+1)]
    lista_z = [i for i in range(z+1)]

    result = []

    # for x1 in range(len(lista_x)):
    #     for y1 in range(len(lista_y)):
    #         for z1 in range(len(lista_z)):
    #             combin = [lista_x[x1], lista_y[y1], lista_z[z1]]
    #             if(sum(combin) != n):
    #                 result.append(combin)
    #print(result)
    print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])