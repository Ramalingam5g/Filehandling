def trainee_names():
    with open("read.txt","r")as file:
        word=[]
        for content in file:
            temp=content.split()
            for line in temp:
                word.append(line)
    word.sort()       
    with open("write.txt","w")as line:
        for i in word:
            
            line.writelines("\nthe trainee of march batch is:")  
            line.writelines(i)      
trainee_names()
