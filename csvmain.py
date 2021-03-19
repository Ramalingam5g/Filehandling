import csv

with open("read.csv","r")as file1:
    reader_file=csv.reader(file1)
    with open("write.csv","w")as file2:
        writer_file=csv.writer(file2,delimiter="#")
        for line in reader_file:
            writer_file.writerow(line)

