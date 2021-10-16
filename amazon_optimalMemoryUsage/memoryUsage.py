def optimalusage(deviceCapacity,foregroundApp,backgroundApp):
    fgBgPair = []
    useage = []
    for i in range(len(foregroundApp)):
        for j in range(len(backgroundApp)):
            if foregroundApp[i][1]+ backgroundApp[j][1] <= deviceCapacity:
                fgBgPair.append([foregroundApp[i][0], backgroundApp[j][0]])
                useage.append(foregroundApp[i][1]+ backgroundApp[j][1])
    indexx = useage.index(max(useage))
    print(fgBgPair[indexx])
    
if __name__ == '__main__':
    deviceCapacity = 7
    foregroundApp = [[1,2],[2,4],[3,6]]
    backgroundApp = [[1,2]]
    optimalusage(deviceCapacity,foregroundApp,backgroundApp)