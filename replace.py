def replace_name():
    with open("read.csv","r")as file:
        for file2 in file:
            temp=file2
            var="the trainee of",temp,"march batch"
            print(var)
replace_name()