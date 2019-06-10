# First thing (always!): remove all the variables from the workspace.
# You can do this in 2 ways:
# 1) Go to Workspace --> Erase workspace
# or 2) digit
rm(list=ls())

getwd() # To know the current working directory
setwd("/home/urfin/PycharmProjects/study-university/R/Lesson1") # To set the new working directory
getwd()

#################################################
# VECTORS
#################################################

# Create a vector named V1 which contains the integer numbers from 1 to 5
V1 <- c(1,2,3,4,5)
V1
# or you can use
V1 <- c(1:5)
V1
V1 <- c(1:500)
V1

# Remember! You cannot create an object called "1"
# 1 <- c(1,2,3,4,5)

length(V1)
str(V1)
summary(V1)

# Create a vector named V2 which contains decimal numbers from 0 to 2
?seq
V2 <- seq(from=0,to=2,by=0.1)
V2
length(V2)
summary(V2)
str(V2)

# Create a vector named V3 which contains the names of the numbers from "one" to "ten". 
V3 <- c("one","two","three","four","five","six","seven","eight","nine","ten")
V3
length(V3)
str(V3)
summary(V3)
table(V3)

one <- 1
two <- 2
three <- 3
V3 <- c(one,two,three)
V3
length(V3)
str(V3)
summary(V3)
table(V3)

# Create a vector named V4 
V4 <- c("one","two","three","one","one","two")
V4
length(V4)
str(V4)
summary(V4)
table(V4)

# Create a vector named V5 by converting V4 from datatype=carachter to datatype=factor
V4
V5 <- as.factor(V4)
V5
length(V5)
str(V5)
summary(V5)
table(V5)
levels(V5)
length(levels(V5))
nlevels(V5)

# Back from factors to numbers
V6 <- as.numeric(V5)
V6
V5
V4
V6
# Back from factors to characters
V7 <- as.character(V5)
V7
V4

# Indexing a vector
V1
V1[20]
V2
V2[30]

V5
V5[6]
V5[20]

# Using operators on vectors
V1
V1 <- V1[V1>31]

V1_greater31 <- V1[V1>31]
V1_greater31
summary(V1_greater31)

V8 <- c(1:10)
V9 <- c(1:10)
V8==V9
V10 <- V8==V9 
V10
str(V10)
summary(V10)
table(V10)

V11 <- c("A","B","D","F","L")
V12 <- c("Q","B","D","A","L")

V11==V12
V13 <- V11==V12
table(V13)
V13bis <- V11[V11==V12]
V13bis

V11!=V12
V14 <- V11!=V12
table(V14)
V14bis<- V11[V11!=V12]
V14bis

V11 %in% V12
V15 <- V11[V11 %in% V12]
V15

#################################################
# DATAFRAMES
#################################################
SampleSheet <- read.table("/home/urfin/PycharmProjects/study-university/R/Lesson1/SampleSheet.txt",sep="\t",header=T)
SampleSheet
length(SampleSheet)
dim(SampleSheet)
str(SampleSheet)
#read.table automatically convert character variables to factors. 

SampleSheet$Sex <- as.factor(SampleSheet$Sex)
str(SampleSheet)

head(SampleSheet)
levels(SampleSheet$Sample_Name)
levels(SampleSheet$Group)
table(SampleSheet$Group)
summary(SampleSheet$Group)
summary(SampleSheet$CD8.naive)
summary(SampleSheet)

# Indexing a dataframe
SampleSheet[,1]
SampleSheet$Sample_Name
SampleSheet[,"Sample_Name"]
SampleSheet[,]$Sample_Name


SampleSheet[1,]

SampleSheet[1:3,1]
SampleSheet[1:3,"Sample_Name"]
SampleSheet[1:3,]$Sample_Name

SampleSheet[1:3,3:5]

# Subsetting a dataframe
SampleSheet[SampleSheet$Group=="W",]
SampleSheet_W <- SampleSheet[SampleSheet$Group=="W",]
SampleSheet_W
dim(SampleSheet_W)

condition <- SampleSheet$Group=="W"
condition
SampleSheet_W <- SampleSheet[condition,]
SampleSheet_W
dim(SampleSheet_W)


SampleSheet_W <- SampleSheet[SampleSheet$Group=="W",1:3]
SampleSheet_W
dim(SampleSheet_W)

SampleSheet_W <- SampleSheet[SampleSheet$Group=="W",c(1,2,5)]
SampleSheet_W
dim(SampleSheet_W)


str(SampleSheet_W)

SampleSheet_W <- droplevels(SampleSheet_W)
dim(SampleSheet_W)
str(SampleSheet_W)

SampleSheet[SampleSheet$CD8.naive>300,]
SampleSheet_CD8.naive_300 <- SampleSheet[SampleSheet$CD8.naive>300,]
str(SampleSheet_CD8.naive_300)
SampleSheet_CD8.naive_300 <- droplevels(SampleSheet_CD8.naive_300)
str(SampleSheet_CD8.naive_300)

V_A_C_D <- c("A","C","D")
SampleSheet
SampleSheet$Sample_Name %in% V_A_C_D
SampleSheet_A_C_D <- SampleSheet[SampleSheet$Sample_Name %in% V_A_C_D,]
SampleSheet_A_C_D
str(SampleSheet_A_C_D)
SampleSheet_A_C_D <- droplevels(SampleSheet_A_C_D)
str(SampleSheet_A_C_D)

#################################################
# INFINIUM 27
#################################################
# The file is in a spreadsheet format . Let's import in R the first 20 rows of the file
Infinium27 <- read.table("/home/urfin/PycharmProjects/study-university/R/Lesson1/Infinium27.txt",sep="\t",header=T,nrow=20)
dim(Infinium27)
head(Infinium27)
Infinium27
Infinium27  <- read.table("/home/urfin/PycharmProjects/study-university/R/Lesson1/Infinium27.txt",sep="\t",header=T)
dim(Infinium27)
head(Infinium27)
str(Infinium27)


# How many probes are there in each chromosome?
# We can proceed in two ways:
# 1) We subset the dataframe for each chromosome
chr1 <- Infinium27[Infinium27$Chr=="1",]
dim(chr1)
chr2 <- Infinium27[Infinium27$Chr=="2",]
dim(chr2)
# etc
# 2) We use the table function
table(Infinium27$Chr)

summary(Infinium27)

# Missing values
str(Infinium27)
TSS_NA <- Infinium27[is.na(Infinium27$TSS_Coordinate),]
dim(TSS_NA)
head(TSS_NA)
TSS_NA_2 <- Infinium27[Infinium27$TSS_Coordinate=="NA",]
dim(TSS_NA_2)

# How many probes are not associated to a gene?
Infinium27_No_gene <- Infinium27[Infinium27$Symbol=="",]
dim(Infinium27_No_gene)
str(Infinium27_No_gene)
Infinium27_No_gene <- droplevels(Infinium27_No_gene)
str(Infinium27_No_gene)

# How many genes there are on each chromosome?
str(Infinium27$Gene_ID)
Infinium27_gene <- Infinium27[Infinium27$Gene_ID!="",]
str(Infinium27_gene)
Infinium27_gene <- droplevels(Infinium27_gene)
dim(Infinium27_gene)
str(Infinium27_gene)
summary(Infinium27_gene)
table(Infinium27_gene$Chr)
table(Infinium27_gene$Chr, Infinium27_gene$Gene_Strand)
df_table <- data.frame(table(Infinium27_gene$Chr))
df_table
colnames(df_table) <- c("chr","number of genes")
df_table

# What is the gene with the highest number of probes?
gene_table <- table(Infinium27$Symbol)
head(gene_table)
str(gene_table)
gene_table <- data.frame(gene_table)
str(gene_table)
colnames(gene_table) <- c("Gene","Freq")
head(gene_table)
gene_table <- gene_table[order(gene_table$Freq),]
head(gene_table)
tail(gene_table)
gene_table <- gene_table[order(-gene_table$Freq),]
head(gene_table)
gene_table[gene_table$Freq == max(gene_table$Freq),]
gene_table <- gene_table[!is.na(gene_table$Gene),]
head(gene_table)
gene_table <- gene_table[gene_table$Gene !="",]
head(gene_table)
gene_table <- droplevels(gene_table)
gene_table[gene_table$Freq == max(gene_table$Freq),]


# Save options

write.table(gene_table,file="gene_table.txt",sep="\t")
write.table(gene_table,file="gene_table.txt",sep="\t",row.names=F)

# save writes an external representation of R objects to the specified file. The objects can be read back from the file
# at a later date by using the function load or attach (or data in some cases).
# save.image() is just a short-cut for 'save my current workspace', i.e., save(list = ls(all.names = TRUE),
# file = ".RData", envir = .GlobalEnv). It is also what happens with q("yes").
save(gene_table,file="gene_table.RData")
save.image("Lesson_1.RData")

rm(list=ls())
load("gene_table.RData")
ls()
load("Lesson_1.RData")
ls()

# Exercises:
# What is the chromosome with the highest number of probes?
# What is the chromosome with the highest number of probes with SourceStrand equal to TOP?
# On which chromosomes are the probes not associated to a gene?
# What is the maximum distance of a probe from TSS? And the smallest?
# How many CpG islands are on chromosome 7? 	

  