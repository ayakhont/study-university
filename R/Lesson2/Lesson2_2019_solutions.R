# Exercises:
#1 How many probes in the array are in the open sea?
table(Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island)

#2 Create a barplot representing the number of Islands, shores, shelves in each chromosome
Illumina450Manifest_clean_islands <- Illumina450Manifest_clean[Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island!="",]
Illumina450Manifest_clean_islands <- droplevels(Illumina450Manifest_clean_islands)
table(Illumina450Manifest_clean_islands$Relation_to_UCSC_CpG_Island, Illumina450Manifest_clean_islands$CHR)
barplot(table(Illumina450Manifest_clean_islands$Relation_to_UCSC_CpG_Island, Illumina450Manifest_clean_islands$CHR))
levels(Illumina450Manifest_clean_islands$Relation_to_UCSC_CpG_Island)
barplot(table(Illumina450Manifest_clean_islands$Relation_to_UCSC_CpG_Island, Illumina450Manifest_clean_islands$CHR),col=c("grey","green","yellow","cyan","orange"))

#3 How many probes map in genic sequences but not in CpG island, shores and shelves?
Genic <- Illumina450Manifest_clean[Illumina450Manifest_clean$UCSC_RefGene_Name!="",]
dim(Genic)
Genic <- droplevels(Genic)
table(Genic$Relation_to_UCSC_CpG_Island)

#4 For each chromosome, how many probes map in genic sequences?
table(Genic$CHR)
#5 Load the Infinium27k manifest: how many probes are in common between 27k and 450k? And where do the common probes map (Island, shore, shelves, genic or not genic)
Infinium27 <- read.table("C:/Users/mugiu/Dropbox/DRD_2019/1/Infinium27.txt",sep="\t",header=T)
dim(Infinium27)
colnames(Illumina450Manifest_clean)
colnames(Infinium27)
Infinium450_in_27 <- Illumina450Manifest_clean$IlmnID %in% Infinium27$IlmnID
length(Infinium450_in_27)
table(Infinium450_in_27)
Infinium450_in_27 <- Illumina450Manifest_clean[Illumina450Manifest_clean$IlmnID %in% Infinium27$IlmnID,]
Infinium450_in_27 <- droplevels(Infinium450_in_27)
dim(Infinium450_in_27)
table(Infinium450_in_27$Relation_to_UCSC_CpG_Island)
