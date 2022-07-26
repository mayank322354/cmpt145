def main():
    f = open("monsters1.txt","r")
    #to make a seperate file named as a2-git.txt
    ans = open("a2-git.txt","w")
    f1 = f.readlines()

    x = y= 0
    for word in f1:
        x = 0;y= 0
        for letter in word:
            if letter == "N":
                y += 1
            elif letter == "S":
                y-=1
            elif letter == "E":
                x += 1
            elif letter == "W":
                x -= 1
        #writing the answer in the file
        ans.write(str(x)+" "+str(y))


main()