getwd()
setwd("../Documents/Github/newgal4/data")
library(data.table)
df<- fread("glp1_tweets_combined_w_reup01.csv")


head(df)


df<-df[conversation_id==id,]
dim(df)




df[ ,table(retweet_count)]
df[ ,table(reply_count)]
df[ ,table(like_count)]
df[ ,table(quote_count)]

names(df)

table(
  rs<-rowSums(
    df[, .(retweet_count, reply_count, like_count, quote_count)
       ]
  )
)
df[, Engagement:=rs]
df[,rs:=NULL]
names(df)
df<-df[df$Engagement>0,]
df<-df[order(Engagement, decreasing=T),]

df$Engage_text<-df[, paste0("engagement=", df$Engagement
                            ," (like=", df$like_count
                            , " retw=", df$retweet_count
                            , " reply=", df$reply_count
                            , " quote=", df$quote_count
                            , ")"
                            )
                   ]


df$author_username
df$id
names(df)
df$link<-paste0("x.com/", df$author_username, "/status/", df$id)


write.csv(df[,.(text_clean, Engage_text, link)]
          , "toptweets.csv"
          , quote = TRUE
          , row.names=F)
?write.csv

read.csv("toptweets.csv")
