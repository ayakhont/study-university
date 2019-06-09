# Install minfi and 
## try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
biocLite(c("minfi","shinyMethyl")) 

rm(list=ls())
setwd("C:/Users/mugiu/Dropbox/DRD_2019/3/Input_data")
# list the files included in the folder
list.files()
# let's have a look to the csv
SampleSheet <- read.table("SampleSheet.csv",sep=",",header=T)
SampleSheet
SampleSheet <- read.csv("SampleSheet.csv",header=T)
SampleSheet

####################################
### Import raw data
####################################

# Load idat files and the experiment samplesheet using minfi
library(minfi)
vignette("minfi")

# Set the directory in which the raw data are stored
baseDir <- ("C:/Users/mugiu/Dropbox/DRD_2019/3/Input_data")
targets <- read.metharray.sheet(baseDir)
targets

# Create an object of class RGChannelSet
?read.metharray.exp
RGset <- read.metharray.exp(targets = targets)

# Now I change the directory in which I want to save the new files
setwd("C:/Users/mugiu/Dropbox/DRD_2019/3")
save(RGset,file="RGset.RData")

load("RGset.RData")
ls()
RGset
str(RGset)
?RGChannelSet

dim(getRed(RGset))
head(getRed(RGset))
Red <- data.frame(getRed(RGset))
dim(Red)
head(Red)

dim(getGreen(RGset))
head(getGreen(RGset))
Green <- data.frame(getGreen(RGset))
dim(Green)
head(Green)

# What are rownames?
load('C:/Users/mugiu/Dropbox/DRD_2019/2/Illumina450Manifest_clean.RData')
ls()
head(Illumina450Manifest_clean)

### From Addresses to probes
Illumina450Manifest_clean[Illumina450Manifest_clean$AddressA_ID=="10600313",]
Illumina450Manifest_clean[Illumina450Manifest_clean$AddressB_ID=="10600313",]
# cg25192902, type I, Red

Illumina450Manifest_clean[Illumina450Manifest_clean$AddressA_ID=="10600322",]
# cg00226849, type II
Illumina450Manifest_clean[Illumina450Manifest_clean$AddressB_ID=="10600322",]

### From probes to Addresses
head(Illumina450Manifest_clean)
# cg00035864, type II
Red[rownames(Red)=="31729416",]
Green[rownames(Green)=="31729416",]

# cg00050873, type I red
Red[rownames(Red)=="32735311",]
Red[rownames(Red)=="31717405",]

Green[rownames(Green)=="32735311",] #Out of band signal
Green[rownames(Green)=="31717405",] #Out of band signal


####################################
### Class "IlluminaMethylationManifest"
####################################
# The RGChannelSet stores also a manifest object that contains the probe design information of the array (IlluminaMethylationManifest)

?IlluminaMethylationManifest

# Get the manifest object
?getManifest
getManifest(RGset)
getManifestInfo(RGset)

# Returns a data.frame giving the type I, type II or control probes
head(getProbeInfo(RGset))
df <- data.frame(getProbeInfo(RGset))
dim(df) #PAY ATTENTION!!!
head(getProbeInfo(RGset, type = "II"))
df_II <- data.frame(getProbeInfo(RGset, type = "II"))
dim(df_II)
350036+ 135476

####################################
### Extract methylated and unmethylated signals
####################################
MSet.raw <- preprocessRaw(RGset)
MSet.raw
save(MSet.raw,file="MSet_raw.RData")
?MethylSet
head(getMeth(MSet.raw))
head(getUnmeth(MSet.raw))

Meth <- getMeth(MSet.raw)
str(Meth)
head(Meth)
Unmeth <- getUnmeth(MSet.raw)
str(Unmeth)
head(Unmeth)

####################################
### QC plot
####################################
qc <- getQC(MSet.raw)
plotQC(qc)

####################################
### Control probes
####################################
# getProbeInfo returns the types and the numbers of control probes of each type. It can act both on RGChannelSet and on MethylSet classes.
getProbeInfo(RGset, type = "Control")

df_TypeControl <- data.frame(getProbeInfo(RGset, type = "Control"))
str(df_TypeControl)
table(df_TypeControl$Type)

controlStripPlot(RGset, controls="NEGATIVE")
controlStripPlot(RGset, controls="EXTENSION")
controlStripPlot(RGset, controls="STAINING")
controlStripPlot(RGset, controls="BISULFITE CONVERSION I")
controlStripPlot(RGset, controls="BISULFITE CONVERSION II")
controlStripPlot(RGset, controls="SPECIFICITY I")
controlStripPlot(RGset, controls="SPECIFICITY II")

library(shinyMethyl)
vignette("shinyMethyl")
# summary <- shinySummarize(RGset) # do not launch it now, it takes some minutes
# save(summary,file="summary_shinyMethyl.RData")
load('summary_shinyMethyl.RData')
runShinyMethyl(summary)


####################################
### Detection p-value
####################################

?detectionP
detP <- detectionP(RGset) # do not launch it now, it takes some minutes
save(detP,file="detP.RData")
str(detP)
dim(detP)
head(detP)

failed <- detP>0.05
head(failed)
dim(failed)
table(failed)
summary(failed)

# Note well: minfi does not provide any function that performs filtering of samples/probes on the basis of detection p-value! Other packages, like wateRmelon, allow to perform this action

####################################
### Filtering of the bad samples
####################################
# Fraction of failed postions per sample
head(colMeans(failed)) #each value corresponds to the ratio (number of TRUE)/(number of TRUE+FALSE) for each column (that is, for each sample)
# We can decide, for example, to identify the samples in which >5 % of sites have a detection p-value greater than 0.05
means_of_columns <- colMeans(failed) 
means_of_columns
# In this example, all the samples have < 5% of probes with a bad detection pValue --> I can retain all the samples

####################################
### Filtering of the bad probes
####################################
# Fraction of samples with failed postions per probe
head(rowMeans(failed)) #each value corresponds to the ratio (number of TRUE)/(number of TRUE+FALSE) for each row (that is, for each probe)
# cfr with head(failed)
head(failed)
head(detP)
6/8 # probe cg00050873 has a bad detection pValue in 6 samples
7/8 # probe cg00212031 has a bad detection pValue in 7 samples

# We can decide, for example, to remove the probes having > 1 % of samples with a detection p-value greater than 0.05
means_of_rows <- rowMeans(failed)
head(means_of_rows)
str(means_of_rows)
probes_to_retain <- means_of_rows<0.01
head(probes_to_retain)
table(probes_to_retain)
names_probes_to_remove <- names(probes_to_retain)[probes_to_retain==FALSE]
names_probes_to_remove

MSet.raw_filtered <- MSet.raw[probes_to_retain,]
MSet.raw
MSet.raw_filtered

# Now we can check that the probes we have removed are no more in the MSet.raw_filtered object
Unmeth_filtered <- getUnmeth(MSet.raw_filtered)
Meth_filtered <- getMeth(MSet.raw_filtered)
intersect(rownames(Unmeth_filtered), names_probes_to_remove)
intersect(rownames(Meth_filtered), names_probes_to_remove)
# :-)
save(MSet.raw_filtered,file="MSet.raw_filtered.RData")


# BUT...As we will see in the next lesson, most of the normalization procedures implemented in minfi work on RGset and do not like missing probes.
# How to behave?
# Our suggestion:
# check how many probes have a detection p-value < 0.05 or <0.01 by subsetting the MethylSet object 
# if they are few (for example, less than 10000), leave them...they will not affect normalization procedures
# if they are several (for example, 10000 or more), use normalization procedures that work with filtered MethylSet objects (preprocessQuantile, dasen, etc)
# You can always remove the bad probes from the beta or M value matrix obtained after the normalization procedures

####################################
### Accessing annotation for Illumina methylation objects
####################################
?getAnnotation
getAnnotation(RGset)
df_Annotation <- getAnnotation(RGset)
str(df_Annotation)
df_Annotation <- data.frame(getAnnotation(RGset))
str(df_Annotation)


####################################
### Filtering of SNPs  
####################################
?dropLociWithSnps
dropLociWithSnps(MSet.raw)

# First, we have to convert the MethylSet Object in a GenomiMethylSet object
#GenomicMSet.raw_filtered <- mapToGenome(MSet.raw_filtered)
#save(GenomicMSet.raw_filtered,file="GenomicMSet.raw_filtered.RData")
load("GenomicMSet.raw_filtered.RData")
GenomicMSet.raw_filtered
dropSNPs_CpG <- dropLociWithSnps(GenomicMSet.raw_filtered,snps="CpG")
dropSNPs_CpG
dropSNPs_SBE <- dropLociWithSnps(GenomicMSet.raw_filtered,snps="SBE")
dropSNPs_SBE


####################################
### beta-values and M-values
####################################
# In this example we proceed with filtered data, but it is exactly the same with not filtered data, just replace Unmeth_filtered and Meth_filtered with Unmeth e Meth

head(Unmeth_filtered)
head(Meth_filtered)

?getBeta
beta <- getBeta(MSet.raw_filtered)
str(beta)
summary(beta)
head(beta)
579/(579+458)

?getM
M <- getM(MSet.raw_filtered)
str(M)
summary(M)
head(M)
log2(579/458)

####################################
### Density plots of Beta and M values
####################################

?density
density(beta)
plot(density(beta))
plot(density(beta),main="Density of Beta Values")
plot(density(beta),main="Density of Beta Values",col="blue")

density(M)
plot(density(M))
plot(density(M),main="Density of M Values")

# We can put several plots in the same panel:
# http://www.statmethods.net/advgraphs/layout.html
# (in general, you can find a quick guide to plots here: http://www.statmethods.net/graphs/index.html)
par(mfrow=c(1,2))
plot(density(beta),main="Density of Beta Values")
plot(density(M),main="Density of M Values")


####################################
### Boxplots
####################################

boxplot(beta)

par(mfrow=c(1,2))
plot(density(beta),main="Density of Beta Values",col="blue")
boxplot(beta)

par(mfrow=c(2,1))
plot(density(beta),main="Density of Beta Values",col="blue")
boxplot(beta)

# You can save the graph in a variety of formats from the menu File -> Save As.
# You can also save the graph via code using one of the following functions:

# Function 						Output to
# pdf("mygraph.pdf") 			pdf file
# win.metafile("mygraph.wmf") 	windows metafile
# png("mygraph.png") 			png file
# jpeg("mygraph.jpg") 			jpeg file
# bmp("mygraph.bmp") 			bmp file
# postscript("mygraph.ps") 		postscript file

# For example:
pdf("Picture1.pdf",width=10,height=5)
par(mfrow=c(1,2))
plot(density(beta),main="Density of Beta Values",col="blue")
boxplot(beta)
dev.off() #shuts down the graphical device


# Exercise: let's consider the probe cg02004872:
# Is it a type I or type II probe?
# What is/are its addresses?
# What are the associated red and green fluorescence?

# If we have time
barplot(colMeans(Red))
barplot(colMeans(Green))
barplot(colMeans(Red),colMeans(Green))
df <- data.frame(colMeans(Red),colMeans(Green))
df
barplot(df)
df <- as.matrix(df)
df
barplot(df)
barplot(t(df))
barplot(t(df),col=c("red","green"))

# Check the CRC_Lesson3_RGset.RData file for quality controls!
RGset_CRC
summary <- shinySummarize(RGset_CRC) # do not launch it now, it takes some minutes
save(summary,file="summary_shinyMethyl_CRC_Lesson3.RData")