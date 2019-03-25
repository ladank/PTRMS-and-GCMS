library(gdata)
library(tidyverse)
library(readxl)
library(ggplot2)

setwd("C:/Users/allen/ownCloud/Full scale chamber test/Small chamber test") # win7

load_data <- function(sheet_name){
  std <-read_excel("New_std_calibration_20190323.xlsx",
                   sheet=sheet_name)
  std <- std[-(1:2),]
  names(std)[1] <-"No of Peak"
  names(std)[2] <-"RT"
  names(std)[5] <-"Area"
  return(std)
}

find_peak <- function(min,max){
   out <- as.numeric(std1[which((std1$RT>min)&std1$RT<max),5])
   out <- append(out,as.numeric(std2[which((std2$RT>min)&std2$RT<max),5]))
   out <- append(out,as.numeric(std3[which((std3$RT>min)&std3$RT<max),5]))
   out <- append(out,as.numeric(std4[which((std4$RT>min)&std4$RT<max),5]))
   out <- append(out,as.numeric(std5[which((std5$RT>min)&std5$RT<max),5]))
   return(out)
}
find_cf <- function(std_con,tar_con){
  df <- data.frame(std_con,tar_con)
  data_lm <- lm(tar_con~std_con,data=df)
  summary(data_lm)
  return(data_lm)
}


plot_data <- function(std_con,tar_con,data_lm,compound_name,xloc,yloc){
  df <- data.frame(std_con,tar_con)
  #data_lm <- lm(tar_con~std_con,data=df)
  #summary(data_lm)

  formula <- sprintf("italic(y) == %.2f %+.2f * italic(x)",round(coef(data_lm)[1],2),round(coef(data_lm)[2],2))
  r2 <- sprintf("italic(R^2) == %.4f",summary(data_lm)$r.squared)
  labels <- data.frame(formula=formula,r2=r2,stringsAsFactors = FALSE)
  
  plot_tar <- ggplot(df,aes(x=std_con,y=tar_con)) + geom_point()+xlab("standard solution concentration")+ylab(paste(compound_name,"Area"))
  plot_tar <- plot_tar+geom_abline(intercept = coef(data_lm)[1],slope = coef(data_lm)[2],color="red")
  plot_tar <- plot_tar+geom_text(data=labels,mapping=aes(x = xloc,y=yloc,label=formula),parse = TRUE,inherit.aes = FALSE,size = 3)
  plot_tar <- plot_tar+geom_text(data=labels,mapping=aes(x = xloc,y=0.9*yloc,label=r2),parse = TRUE,inherit.aes = FALSE,size = 3)
  plot_tar <- plot_tar+ggtitle(compound_name)
  plot_tar

}

std1 <- load_data("Sheet1")
std2 <- load_data("Sheet2")
std3 <- load_data("Sheet3")
std4 <- load_data("Sheet4")
std5 <- load_data("Sheet5")

std_con <- c(0.3,0.2,0.12,0.04,0.01)
tol_con <- find_peak(9,9.1)
hex_con <- find_peak(10,11)
dec_con <- find_peak(15.5,16)

tol_lm <- find_cf(std_con,tol_con)
hex_lm <- find_cf(std_con,hex_con)
dec_lm <- find_cf(std_con,dec_con)

plot_data(std_con,tol_con,tol_lm,"Toluene",xloc=0.1,yloc=1e+9)
plot_data(std_con,hex_con,hex_lm,"Hexanal",xloc=0.1,yloc=5e+8)
plot_data(std_con,dec_con,dec_lm,"Decane",xloc=0.1,yloc=1e+9)

summary(tol_lm)
summary(hex_lm)

