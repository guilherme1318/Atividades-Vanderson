def copiarArq(First, second):
    f1 = open("First.txt", "r")
    f2 = open("second.txt", "w")


    for text in f1:
        f2.write(text)
    f1.close()
    f2.close()

copiarArq("First.txt","second.txt")


#Guilherme Ribeiro 1700546   BD
#Nicolas Alves 1700012       BD
