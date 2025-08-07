getwd()
setwd("../Documents/Github/newgal4/data")
library(data.table)
df1<- fread("glp1_snacking_tweets_with_categorizations_and_authors.csv")
df2<- fread("glp1_snacking_tweets_with_categorizations_and_authors_reup.csv")


sort(names(df1))
sort(names(df2))
df1$author_followers<-df1$author_followers_count

#table(df2$text_x==df2$text_y)
names(df2)<-gsub( "_x", "" , names(df2))
table(names(df1)%in% names(df2))
names(df1)[! names(df1)%in% names(df2)]

sort(names(df1)[!names(df1)%in% names(df2)])
sort(names(df2)[!names(df2)%in% names(df1)])

keepvars<-names(df1)[names(df1)%in% names(df2)]

test<-(as.character(sapply(df1[,..keepvars], class))==as.character(sapply(df2[,..keepvars], class)))
table(test)
# table(as.character(sapply(df1[,..keepvars], class))==as.character(sapply(df2[,..keepvars], class)))
# diffvars<-names(df1)[test==F]
# sapply(df1[,..diffvars], class)
# sapply(df2[,..diffvars], class)


dfm<-rbindlist(list(df1[,..keepvars], df2[,..keepvars]))
dfm$count<-1
library(lubridate)
dfm$day<-day(dfm$created_at)
write.csv(dfm, "glp1_tweets_combined_w_reup01.csv")


dfc<-dfm[dfm$conversation_id==dfm$id, ]

vn<-c("count", "retweet_count", "reply_count", "like_count", "quote_count", "author_followers")
vn<-c(vn, names(dfc)[21:30])

dim(dfc)
hist(dfc$reply_count)
plot(dfc$reply_count, dfc$retweet_count)
plot(dfc$like_count, dfc$retweet_count)

dim(dfc)

colSums(dfc[,c(7:10,36)])


names(dfc
      )

library(jsonlite)


cnts<-colSums((dfc[,..vn]))[-c(1:6
                     )]

cnts_w1<-colSums((dfc[dfc$day<12,..vn]))[-c(1:6
)]
cnts_w2<-colSums((dfc[dfc$day>=12,..vn]))[-c(1:6
)]
table(dfc$day)
cnts_w1/cnts_w2

chngs<-cbind(cnts_w1, cnts_w2, xfactor=round((cnts_w2/cnts_w1-1),1))
colnames(chngs)<-c("Week of July 6", "Week of July 13", "X factor")

chngs[is.infinite(chngs)]<-NA
write.csv(chngs
      , "categories.csv")




#### CREATE TOTALS 
table(day(dfc$created_at))

tb_tot<-aggregate(dfc[,..vn], list(day=dfc$day), FUN=sum)
tb_tot$Engagement<-rowSums(tb_tot[,3:6])
tb_tot$`Reply Count`<-log(tb_tot$reply_count)
tb_tot$`Tweet Count`<-log(tb_tot$count)

tb01<-tb_tot[-c(1:2),c(1,2)]
tb02<-tb_tot[-c(1:2),c(1,3)]
tb01$id<-"Tweets"
tb02$id<-"Re-tweets"

names(tb01)<-names(tb02)<-c("x","y","id")
tb_out<-rbind(tb01, tb02)



write.csv(tb_out
          , "counts.csv"
          , row.names = F)







 #  pLOT "Total Engagement (Log)", "Tweet Count (Log)"

tb_tot$avg_follow<-tb_tot$author_followers/tb_tot$count
plot(x=tb_tot$day, y=log(tb_tot$like_count)
     , type="b"
     , ylim=c(0,10)
     , col="blue")
points(x=tb_tot$day, y=log(tb_tot$reply_count)
     , type="b"
     , ylim=c(0,7)
     , col="red")
points(x=tb_tot$day, y=log(tb_tot$count), col="black", type="b")
points(x=tb_tot$day, y=log(tb_tot$retweet_count)
       , type="b"
       , ylim=c(0,7)
       , col="green")

points(x=tb_tot$day, y=log(tb_tot$quote_count)
       , type="b"
       , ylim=c(0,7)
       , col="orange")
points(x=tb_tot$day, y=log(tb_tot$avg_follow)
       , type="b"
       , ylim=c(0,7)
       , col="purple")




##### FACTOR ANALYSIS

par(mfrow=c(2,2))

pie(chngs[,1])
pie(chngs[,2])


dfscale<-diag(1/tb_tot$author_followers)%*%as.matrix(tb_tot[,3:6])
fres<-factanal(dfscale, 1, scores = "regression")
fres$scores
round(10^5*dfscale)
f.lm<-lm(fres$scores~retweet_count+reply_count+like_count+quote_count
         , data=as.data.frame(dfscale))

summary(f.lm)
round(coef(f.lm)/sum(coef(f.lm)[-1])*10^2,2)









plot( log(dfc$author_followers)
      , log(dfc$reply_count+dfc$quote_count+dfc$retweet_count+dfc$like_count)
     )

names(dfc)[21:30]


cor(tb_tot, use="pairwise")

df1$author_followers_count
df2$author_followers


df2c<-df2[df2$id==df2$conversation_id, ]
plot(log(df2c$reply_count), log(df2c$author_followers))


vn<-c("count", "retweet_count", "reply_count", "like_count", "quote_count"
      , "author_followers")

