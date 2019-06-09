# Remove all the variables from the workspace
ls()
rm(list=ls())
# Set the working directory
setwd("C:/Users/mugiu/Dropbox/DRD_2019/2")


# Save options
SampleSheet <- read.table("C:/Users/mugiu/Dropbox/DRD_2019/1/SampleSheet.txt",sep="\t",header=T)
SampleSheet_W <- SampleSheet[SampleSheet$Group=="W",]
SampleSheet_W <- droplevels(SampleSheet_W)
SampleSheet_C <- SampleSheet[SampleSheet$Group=="C",]
SampleSheet_C <- droplevels(SampleSheet_C)

write.table(SampleSheet_W,file="SampleSheet_W.txt",sep="\t")
write.table(SampleSheet_W,file="SampleSheet_W.txt",sep="\t",row.names=F)

# save writes an external representation of R objects to the specified file. The objects can be read back from the file at a later date by using the function load or attach (or data in some cases).
# save.image() is just a short-cut for 'save my current workspace', i.e., save(list = ls(all.names = TRUE), file = ".RData", envir = .GlobalEnv). It is also what happens with q("yes").
save(SampleSheet_W,file="SampleSheet_W.RData")
save.image("Example_workspace.RData")

rm(list=ls())
load("SampleSheet_W.RData")
ls()
load("Example_workspace.RData")
ls()

rm(list=ls())
# The Illumina 450k manifest has been downloaded from this link
# http://support.illumina.com/array/array_kits/infinium_humanmethylation450_beadchip_kit/downloads.html
# The file is in a spreadsheet format (486428 rows and 33 columns). Let's import in R the first 20 rows of the file
Illumina450Manifest.temp <- read.table("Illumina450Manifest.txt",sep="\t",header=T, nrows=20)

head(Illumina450Manifest.temp)
str(Illumina450Manifest.temp)

# IlmnID: Unique CpG locus identifier from the Illumina CG database
# Name: Unique CpG locus identifier from the Illumina CG database
# AddressA_ID: Address of probe A
# AlleleA_ProbeSeq: Sequence for probe A
# AddressB_ID: Address of probe  B - Infinium I assays only
# AlleleB_ProbeSeq: Sequence for probe B - Infinium I assays only
# Infinium_Design_Type: Defines Assay type - Infinium I or Infinium II
# Next_Base: Base added at SBE step - Infinium I assays only
# Color_Channel: Color of the incorporated base  (Red or Green) - Infinium I assays only
# Forward_Sequence: Sequence (in 5'-3' orientation) flanking query site
# Genome_Build: Genome build on which forward sequence is based
# CHR: Chromosome - genome build 37
# MAPINFO: Coordinates - genome build 37
# SourceSeq: Unconverted design sequence
# Chromosome_36: Chromosome - genome build 36
# Coordinate_36: Coordinates - genome build 36
# Strand: Design strand
# Probe_SNPs: Assays with SNPs present within probe >10bp from query site
# Probe_SNPs_10: Assays with SNPs present within probe ≤10bp from query site (HM27 carryover or recently discovered)
# Random_Loci: Loci which were chosen randomly in the design proccess
# Methyl27_Loci: Present or absent on HumanMethylation27 array
# UCSC_RefGene_Name: Gene name (UCSC)
# UCSC_RefGene_Accession: Accession number (UCSC)
# UCSC_RefGene_Group: Gene region feature category (UCSC)
# UCSC_CpG_Islands_Name: CpG island name (UCSC)
# Relation_to_UCSC_CpG_Island: Relationship to Canonical CpG Island: Shores - 0-2 kb from CpG island; Shelves - 2-4 kb from CpG island.
# Phantom: FANTOM-derived promoter
# DMR: Differentially methylated region (experimentally determined)
# Enhancer: Enhancer element (informatically-determined)
# HMM_Island: Hidden Markov Model Island
# Regulatory_Feature_Name: Regulatory feature (informatically determined)
# Regulatory_Feature_Group: Regulatory feature category
# DHS: DNAse hypersensitive site (experimentally determined)



# Now let's go on and upload the whole manifest
# DO NOT LAUNCH ME OR I WILL CRASH! :-(
#Illumina450Manifest <- read.table("Illumina450Manifest.txt",sep="\t",header=T,quote="")
#save(Illumina450Manifest,file="Illumina450Manifest.RData")

load("Illumina450Manifest.RData")
ls()
dim(Illumina450Manifest)
head(Illumina450Manifest)
str(Illumina450Manifest)
colnames(Illumina450Manifest)

comparison <- Illumina450Manifest$IlmnID==Illumina450Manifest$Name
comparison <- Illumina450Manifest[,1]==Illumina450Manifest[,2]

# Why an error? :'(
length(Illumina450Manifest$IlmnID)
length(Illumina450Manifest$Name)
str(Illumina450Manifest$IlmnID)
str(Illumina450Manifest$Name)
# the 2 columns have a different number of levels...
# to compare them, I have to convert both to character vectors
comparison <- as.character(Illumina450Manifest[,1])== as.character(Illumina450Manifest[,2])
head(comparison)
dim(comparison)
# Remember, for vectors, dim() does not work, use length()
length(comparison)
table(comparison)

# We can use logical operators on one R object and apply the results to index another R object
Matching <- Illumina450Manifest[comparison==TRUE,]
dim(Matching)
# R by default subsets for the TRUE values, so in alternative we can write
Matching <- Illumina450Manifest[comparison,]
dim(Matching)

NotMatching <- Illumina450Manifest[comparison==FALSE,]
dim(NotMatching)
# in alternative
NotMatching <- Illumina450Manifest[!comparison,]
dim(NotMatching)

head(NotMatching)
NotMatching <- NotMatching[-1,]
head(NotMatching)

# Drop the unused levels!
NotMatching <- droplevels(NotMatching)
str(NotMatching)

# Distribution of probes across the chromosomes
str(Illumina450Manifest)
table(Illumina450Manifest$CHR)

notMappedToCHR <- Illumina450Manifest[Illumina450Manifest$CHR=="",]
dim(notMappedToCHR)
notMappedToCHR <- droplevels(notMappedToCHR)

dim(notMappedToCHR)
dim(NotMatching)
916-851

# Who are these 65 probes?
# We can use the %in% operator

notMappedToCHR$IlmnID %in% NotMatching$IlmnID
notMappedToCHR$IlmnID !%in% NotMatching$IlmnID
!notMappedToCHR$IlmnID %in% NotMatching$IlmnID

notMappedToCHR_NotMatching <- notMappedToCHR[!notMappedToCHR$IlmnID %in% NotMatching$IlmnID,]
dim(notMappedToCHR_NotMatching)
notMappedToCHR_NotMatching <- droplevels(notMappedToCHR_NotMatching)
str(notMappedToCHR_NotMatching)
head(notMappedToCHR_NotMatching)
notMappedToCHR_NotMatching$IlmnID

Illumina450Manifest_clean <- Illumina450Manifest[!Illumina450Manifest$IlmnID %in% notMappedToCHR$IlmnID,]
dim(Illumina450Manifest_clean)
Illumina450Manifest_clean <- droplevels(Illumina450Manifest_clean)
str(Illumina450Manifest_clean)
save(Illumina450Manifest_clean,file="Illumina450Manifest_clean.RData")

############# ISLANDS, SHORES AND SHELVES
table(Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island)
# How many probes in Islands?
ProbesIslands <- Illumina450Manifest_clean[Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island=="Island",]
dim(ProbesIslands)
# How many probes in Islands map also in a gene?
ProbesIslands_Gene <- Illumina450Manifest_clean[Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island=="Island" & Illumina450Manifest_clean$UCSC_RefGene_Name!="",]
dim(ProbesIslands_Gene)

############# GENES
levels(Illumina450Manifest_clean$UCSC_RefGene_Name)[1:20]
# A1CF http://genome-euro.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr10%3A52472902-52731702&hgsid=213618992_FWAq8vB3Gv9iJTJYY7xyDqECVmFA
Illumina450Manifest_clean[Illumina450Manifest_clean$IlmnID=="cg12848457",]
Illumina450Manifest_clean[Illumina450Manifest_clean$IlmnID=="cg27394794",]
Illumina450Manifest_clean[Illumina450Manifest_clean$IlmnID=="cg10222734",]
Illumina450Manifest_clean[Illumina450Manifest_clean$IlmnID=="cg03817621",]


# Have a look at this:
Illumina450Manifest_clean[Illumina450Manifest_clean$Name=="cg00048759",]
#http://genome-euro.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr7%3A99773884-99776433&hgsid=228211450_jK6pt7GD6xw8kdT4sfPebiyQiI2f

############# WHAT IS THE ISLAND (considering also its shores and shelves) WITH THE HIGHEST NUMBER OF PROBES?
table(Illumina450Manifest_clean$UCSC_CpG_Islands_Name)
nlevels(Illumina450Manifest_clean$UCSC_CpG_Islands_Name)
head(table(Illumina450Manifest_clean$UCSC_CpG_Islands_Name))
island_table <- data.frame(table(Illumina450Manifest_clean$UCSC_CpG_Islands_Name))
head(island_table)
island_table <- island_table[order(island_table[,2]),]
head(island_table)
island_table <- island_table[order(-island_table[,2]),]
head(island_table)

highest_probes <- Illumina450Manifest_clean[Illumina450Manifest_clean$UCSC_CpG_Islands_Name=="chr6:31830299-31830948"|Illumina450Manifest_clean$UCSC_CpG_Islands_Name=="chr6:31939730-31940559",]
dim(highest_probes) 
highest_probes <- droplevels(highest_probes)
str(highest_probes)
highest_probes$UCSC_RefGene_Name


####################################
### Infinium I and Infinium II
####################################
str(Illumina450Manifest_clean)
table(Illumina450Manifest_clean$Infinium_Design_Type)
table(Illumina450Manifest_clean$Color_Channel)


# What is the number of Infinium I and Infinium II probes in Islands, shores, shelves and not CpG rich regions??
TypeI <- Illumina450Manifest_clean[Illumina450Manifest_clean$Infinium_Design_Type=="I",]
dim(TypeI)
TypeI <- droplevels(TypeI)
TypeII <- Illumina450Manifest_clean[Illumina450Manifest_clean$Infinium_Design_Type=="II",]
dim(TypeII)
TypeII <- droplevels(TypeII)
table(TypeI$Relation_to_UCSC_CpG_Island)
#         Island N_Shelf N_Shore S_Shelf S_Shore 
#  28518   77674    3666   12064    3247   10307 
table(TypeII$Relation_to_UCSC_CpG_Island)
#         Island N_Shelf N_Shore S_Shelf S_Shore 
# 147569   72580   21178   50806   19053   38890 

# OR, very quickly:
table(Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island, Illumina450Manifest_clean$Infinium_Design_Type)

###################################
# Barplots
###################################
# http://www.statmethods.net/graphs/bar.html
# Barplots of probes in each chromosome
barplot(table(Illumina450Manifest_clean$CHR))
levels(Illumina450Manifest_clean$CHR)
# reorder the levels
Illumina450Manifest_clean$CHR <- factor(Illumina450Manifest_clean$CHR,levels=c("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","Y"))
levels(Illumina450Manifest_clean$CHR)
barplot(table(Illumina450Manifest_clean$CHR))
barplot(table(Illumina450Manifest_clean$CHR),main="Probes per chromosome",xlab="Chromosome",ylab="Counts")
barplot(table(Illumina450Manifest_clean$CHR),main="Probes per chromosome",xlab="Chromosome",ylab="Counts",col="red")
barplot(table(Illumina450Manifest_clean$CHR),main="Probes per chromosome",xlab="Chromosome",ylab="Counts",col=rainbow(24))
barplot(table(Illumina450Manifest_clean$CHR),main="Probes per chromosome",xlab="Chromosome",ylab="Counts",col=rainbow(12))

barplot(table(Illumina450Manifest_clean$CHR, Illumina450Manifest_clean$Infinium_Design_Type))
barplot(table(Illumina450Manifest_clean$Infinium_Design_Type, Illumina450Manifest_clean$CHR))
barplot(table(Illumina450Manifest_clean$Infinium_Design_Type, Illumina450Manifest_clean$CHR), legend=levels(Illumina450Manifest_clean$Infinium_Design_Type))
barplot(table(Illumina450Manifest_clean$Infinium_Design_Type, Illumina450Manifest_clean$CHR),beside=T,legend=levels(Illumina450Manifest_clean$Infinium_Design_Type))

# Is the ratio between typeI and typeII constant between the chromosomes?
df_table <- data.frame(table(Illumina450Manifest_clean$Infinium_Design_Type, Illumina450Manifest_clean$CHR))
df_table
df_table_I <- df_table[df_table$Var1=="I",]
df_table_I <- droplevels(df_table_I)
df_table_II <- df_table[df_table$Var1=="II",]
df_table_II <- droplevels(df_table_II)
head(df_table_I)
head(df_table_II)
df_table_I[,2]==df_table_II[,2]
table(df_table_I[,2]==df_table_II[,2])
ratio_I_II <- df_table_I[,3]/df_table_II[,3]
barplot(ratio_I_II)
barplot(ratio_I_II,names.arg=levels(df_table_I$Var2))

# Barplots of type I and II probes in each region
barplot(table(Illumina450Manifest_clean$Infinium_Design_Type, Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island),beside=T,legend=levels(Illumina450Manifest_clean$Infinium_Design_Type))
barplot(table(Illumina450Manifest_clean$Infinium_Design_Type, Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island),beside=T,legend=levels(Illumina450Manifest_clean$Infinium_Design_Type),col=c("blue","red"))

# Exercises:
#1 How many probes in the array are in the open sea?
#2 Create a barplot representing the number of Islands, shores, shelves in each chromosome
#3 How many probes map in genic sequences but not in CpG island, shores and shelves?
#4 For each chromosome, how many probes map in genic sequences?
#5 Load the Infinium27k manifest: how many probes are in common between 27k and 450k? And where do the common probes map (Island, shore, shelves, genic or not genic)

