####################################
### Check the distributions of Type I and Type II probes
####################################
rm(list=ls())
setwd("/home/urfin/PycharmProjects/study-university/R/Lesson4")
load("beta.RData")
dim(beta)

# I want to subset the beta dataframe according to Type I and II
# First i want to know which probes are Type I and which are Type II
load('/home/urfin/PycharmProjects/study-university/R/Lesson2/Illumina450Manifest_clean.RData')
ls()
head(Illumina450Manifest_clean)

dfI <- Illumina450Manifest_clean[Illumina450Manifest_clean$Infinium_Design_Type=="I",]
dfI <- droplevels(dfI)
dim(dfI)
str(dfI)
dfII <- Illumina450Manifest_clean[Illumina450Manifest_clean$Infinium_Design_Type=="II",]
dfII <- droplevels(dfII)

# I subset the dataframe beta in order to retain only the rows whose name is in the first column of dfI
beta_I <- beta[rownames(beta) %in% dfI$IlmnID,]
dim(beta_I)
# I subset the dataframe beta in order to retain only the rows whose name is in the first column of dfII
beta_II <- beta[rownames(beta) %in% dfII$IlmnID,]
dim(beta_II)

# I  want to compare the density distributions of type I and type II probes
# first, I have to calculate the mean of beta for each row
mean_of_beta_I <- apply(beta_I,1,mean)
mean_of_beta_II <- apply(beta_II,1,mean)

d_mean_of_beta_I <- density(mean_of_beta_I,na.rm=T)
d_mean_of_beta_II <- density(mean_of_beta_II,na.rm=T)

plot(d_mean_of_beta_I,col="blue")
plot(d_mean_of_beta_II,col="red")

plot(d_mean_of_beta_I,col="blue")
lines(d_mean_of_beta_II,col="red")

####################################
### Normalization
####################################

# And now...let's normalize!
# For raw data and for each normalization method listed below, we will prepare the following plots:
#	- density of mean betas for type I and type II probes
#	- density of standard deviations for type I and type II probes
#	- boxplots of beta values
# Let's try the following normalization methods in minfi
#	preprocessSWAN
#	preprocessQuantile 
#	preprocessNoob
#	preprocessFunnorm

# We will need the RGset
load("C:/Users/mugiu/Dropbox/DRD_2019/3_bis/RGset.RData")

# For Raw data we have just prepared the density plot of mean betas...let's prepare the density plot of standard deviations
sd_of_beta_I <- apply(beta_I,1,sd)
sd_of_beta_II <- apply(beta_II,1,sd)
d_sd_of_beta_I <- density(sd_of_beta_I,na.rm=T)
d_sd_of_beta_II <- density(sd_of_beta_II,na.rm=T)

pdf("Raw.pdf",width=10,height=5)
par(mfrow=c(1,3))
plot(d_mean_of_beta_I,col="blue",main="raw beta")
lines(d_mean_of_beta_II,col="red")
plot(d_sd_of_beta_I,col="blue",main="raw sd")
lines(d_sd_of_beta_II,col="red")
boxplot(beta)
dev.off() #shuts down the graphical device

RGset
# preprocessNoob (minfi; input: RGset; output: MethylSet)
?preprocessNoob
preprocessNoob_results <- preprocessNoob(RGset)
preprocessNoob_results
beta_preprocessNoob <- getBeta(preprocessNoob_results)
head(beta_preprocessNoob)

beta_preprocessNoob_I <- beta_preprocessNoob[rownames(beta_preprocessNoob) %in% dfI$IlmnID,]
beta_preprocessNoob_II <- beta_preprocessNoob[rownames(beta_preprocessNoob) %in% dfII$IlmnID,]
mean_of_beta_preprocessNoob_I <- apply(beta_preprocessNoob_I,1,mean)
mean_of_beta_preprocessNoob_II <- apply(beta_preprocessNoob_II,1,mean)
d_mean_of_beta_preprocessNoob_I <- density(mean_of_beta_preprocessNoob_I,na.rm=T)
d_mean_of_beta_preprocessNoob_II <- density(mean_of_beta_preprocessNoob_II,na.rm=T)
sd_of_beta_preprocessNoob_I <- apply(beta_preprocessNoob_I,1,sd)
sd_of_beta_preprocessNoob_II <- apply(beta_preprocessNoob_II,1,sd)
d_sd_of_beta_preprocessNoob_I <- density(sd_of_beta_preprocessNoob_I,na.rm=T)
d_sd_of_beta_preprocessNoob_II <- density(sd_of_beta_preprocessNoob_II,na.rm=T)
pdf("preprocessNoob.pdf",width=10,height=5)
par(mfrow=c(1,3))
plot(d_mean_of_beta_preprocessNoob_I,col="blue",main="preprocessNoob beta")
lines(d_mean_of_beta_preprocessNoob_II,col="red")
plot(d_sd_of_beta_preprocessNoob_I,col="blue",main="preprocessNoob sd")
lines(d_sd_of_beta_preprocessNoob_II,col="red")
boxplot(beta_preprocessNoob)
dev.off() #shuts down the graphical device

# preprocessSWAN (minfi; input: RGset; output: MethylSet)
?preprocessSWAN
preprocessSWAN_results <- preprocessSWAN(RGset)
str(preprocessSWAN_results)
class(preprocessSWAN_results)
preprocessSWAN_results
beta_preprocessSWAN <- getBeta(preprocessSWAN_results)
head(beta_preprocessSWAN)

beta_preprocessSWAN_I <- beta_preprocessSWAN[rownames(beta_preprocessSWAN) %in% dfI$IlmnID,]
beta_preprocessSWAN_II <- beta_preprocessSWAN[rownames(beta_preprocessSWAN) %in% dfII$IlmnID,]
mean_of_beta_preprocessSWAN_I <- apply(beta_preprocessSWAN_I,1,mean)
mean_of_beta_preprocessSWAN_II <- apply(beta_preprocessSWAN_II,1,mean)
d_mean_of_beta_preprocessSWAN_I <- density(mean_of_beta_preprocessSWAN_I,na.rm=T)
d_mean_of_beta_preprocessSWAN_II <- density(mean_of_beta_preprocessSWAN_II,na.rm=T)
sd_of_beta_preprocessSWAN_I <- apply(beta_preprocessSWAN_I,1,sd)
sd_of_beta_preprocessSWAN_II <- apply(beta_preprocessSWAN_II,1,sd)
d_sd_of_beta_preprocessSWAN_I <- density(sd_of_beta_preprocessSWAN_I,na.rm=T)
d_sd_of_beta_preprocessSWAN_II <- density(sd_of_beta_preprocessSWAN_II,na.rm=T)
pdf("preprocessSWAN.pdf",width=10,height=5)
par(mfrow=c(1,3))
plot(d_mean_of_beta_preprocessSWAN_I,col="blue",main="preprocessSWAN beta")
lines(d_mean_of_beta_preprocessSWAN_II,col="red")
plot(d_sd_of_beta_preprocessSWAN_I,col="blue",main="preprocessSWAN sd")
lines(d_sd_of_beta_preprocessSWAN_II,col="red")
boxplot(beta_preprocessSWAN)
dev.off() #shuts down the graphical device

# preprocessQuantile (minfi; input: RGset or Mset; output: GenomicRatioSet)
?preprocessQuantile
preprocessQuantile_results <- preprocessQuantile(RGset)
str(preprocessQuantile_results)
class(preprocessQuantile_results)
preprocessQuantile_results
beta_preprocessQuantile <- getBeta(preprocessQuantile_results)
head(beta_preprocessQuantile)

preprocessQuantile_results <- preprocessQuantile(MSet.raw)
str(preprocessQuantile_results)
class(preprocessQuantile_results)
preprocessQuantile_results
beta_preprocessQuantile <- getBeta(preprocessQuantile_results)
head(beta_preprocessQuantile)

beta_preprocessQuantile_I <- beta_preprocessQuantile[rownames(beta_preprocessQuantile) %in% dfI$IlmnID,]
beta_preprocessQuantile_II <- beta_preprocessQuantile[rownames(beta_preprocessQuantile) %in% dfII$IlmnID,]
mean_of_beta_preprocessQuantile_I <- apply(beta_preprocessQuantile_I,1,mean)
mean_of_beta_preprocessQuantile_II <- apply(beta_preprocessQuantile_II,1,mean)
d_mean_of_beta_preprocessQuantile_I <- density(mean_of_beta_preprocessQuantile_I,na.rm=T)
d_mean_of_beta_preprocessQuantile_II <- density(mean_of_beta_preprocessQuantile_II,na.rm=T)
sd_of_beta_preprocessQuantile_I <- apply(beta_preprocessQuantile_I,1,sd)
sd_of_beta_preprocessQuantile_II <- apply(beta_preprocessQuantile_II,1,sd)
d_sd_of_beta_preprocessQuantile_I <- density(sd_of_beta_preprocessQuantile_I,na.rm=T)
d_sd_of_beta_preprocessQuantile_II <- density(sd_of_beta_preprocessQuantile_II,na.rm=T)
pdf("preprocessQuantile.pdf",width=10,height=5)
par(mfrow=c(1,3))
plot(d_mean_of_beta_preprocessQuantile_I,col="blue",main="preprocessQuantile beta")
lines(d_mean_of_beta_preprocessQuantile_II,col="red")
plot(d_sd_of_beta_preprocessQuantile_I,col="blue",main="preprocessQuantile sd")
lines(d_sd_of_beta_preprocessQuantile_II,col="red")
boxplot(beta_preprocessQuantile)
dev.off() #shuts down the graphical device

# Try by yourself preprocessFunnorm (minfi; input: RGset; output: MethylSet)


# If we have time: let's plot the beta densitiy distribution in islands before and after preprocessQuantile and preprocessFunnorm normalization
####
islands <- Illumina450Manifest_clean[Illumina450Manifest_clean$Relation_to_UCSC_CpG_Island=="Island",]
islands <- droplevels(islands)
beta_islands <- beta[rownames(beta) %in% islands$IlmnID,]
dim(beta_islands)
beta_preprocessQuantile_islands <- beta_preprocessQuantile[rownames(beta_preprocessQuantile) %in% islands$IlmnID,]
dim(beta_preprocessQuantile_islands)
beta_preprocessFunnorm_islands <- beta_preprocessFunnorm[rownames(beta_preprocessFunnorm) %in% islands$IlmnID,]
dim(beta_preprocessFunnorm_islands)

mean_beta_islands <- apply(beta_islands,1,mean)
mean_beta_preprocessQuantile_islands <- apply(beta_preprocessQuantile,1,mean)
mean_beta_preprocessFunnorm_islands <- apply(beta_preprocessFunnorm,1,mean)

plot(density(mean_beta_islands,na.rm=T),xlim=c(0,1),col="brown")
lines(density(mean_beta_preprocessQuantile_islands,na.rm=T),xlim=c(0,1),col="pink")
lines(density(mean_beta_preprocessFunnorm_islands,na.rm=T),xlim=c(0,1),col="orange")

