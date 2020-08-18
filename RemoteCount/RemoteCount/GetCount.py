
def count_remotePress(word):
    keyboard=[['a','b','c','d','e','1','2','3'],
              ['f','g','h','i','j','4','5','6'],
              ['k','l','m','n','o','7','8','9'],
              ['p','q','r','s','t','.','@','0'],
              ['u','v','w','x','y','z','_','/']]
    count=0
    a=''
    for i in word:
        for j in keyboard:
            if i in j:
                if (a in j) and (j.index(i)>j.index(a)) :
                    #Check if previous character is pressed and take count
                    count+=(j.index(i)-j.index(a))+1
                else:
                    #Count press for each character+OK button
                    count+=j.index(i)+1
                print(count)
        a=i

    return count

print(count_remotePress('tech'))
