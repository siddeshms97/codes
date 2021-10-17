def amazon_primeAir(maxTravelDist,fRL,rRL):
    pair = []
    maxdis = []
    for i in range(len(fRL)):
        for j in range(len(rRL)):
            if fRL[i][1] + rRL[j][1] <= maxTravelDist:
                pair.append([fRL[i][0],rRL[j][0]])
                maxdis.append(fRL[i][1] + rRL[j][1])
    #print(pair)
    #print(maxdis)
    indexx = maxdis.index(max(maxdis))
    #print(indexx)
    print(pair[indexx])

if __name__ == '__main__':
    maxTravelDist = 7000
    fRL = [[1,2000],[2,4000],[3,6000]]
    rRL = [[1,2000]]
    amazon_primeAir(maxTravelDist,fRL,rRL)