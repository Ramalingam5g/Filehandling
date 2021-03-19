def check_name_age():
    with open("file.csv","r")as f1:
        word=[]
        for line in f1:
            for line2 in line:
                print(line2[1])
                
                

check_name_age()