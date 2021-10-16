def music(rideDuration, songDuration):
    possible_pairs = []
    duration = []
    for i in range(len(songDuration)):
        for j in range(1,len(songDuration)):
            if songDuration[i] + songDuration[j] <= rideDuration:
                possible_pairs.append([songDuration[i],songDuration[j]])
                duration.append(songDuration[i] + songDuration[j])
    indexx = duration.index(max(duration))
    s1,s2 = possible_pairs[indexx]
    print(s1,s2)
    return 0

if __name__ == '__main__':
    rideDuration = 230
    songDuration = [10,30,120,155,122,70,75]
    music(rideDuration,songDuration)
