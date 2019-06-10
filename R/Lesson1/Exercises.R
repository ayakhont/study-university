library(data.table)
# Created by: urfin
# Created on: 09/06/2019

# What is the chromosome with the highest number of probes?
Infinium27 = read.table("/home/urfin/PycharmProjects/study-university/R/Lesson1/Infinium27.txt",sep="\t",header=T)
probs_table = data.frame(table(Infinium27$Chr))
print(probs_table[probs_table$Freq == max(probs_table$Freq),])

# What is the chromosome with the highest number of probes with SourceStrand equal to TOP?
new_table = data.table(Infinium27)
print(new_table[, c("Chr", "SourceStrand")])