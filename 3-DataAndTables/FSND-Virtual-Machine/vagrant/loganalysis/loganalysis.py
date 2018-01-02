#!/usr/bin/env python3
import psycopg2


#1. What are the most popular three articles of all time?
title1 = "What are the most popular three articles of all time?"
pop3artquery = (
    "select a.title, count(*) as article_view from articles a, log l where l.path like concat('%',a.slug) "
    "and status like '200%' group by a.title order by count(*) desc limit 3 ;")

#2. Who are the most popular article authors of all time?
title2 = "Who are the most popular article authors of all time?"
mostpopartquery =(
    "select au.name, count(*) as author_view from articles a, log l, authors au where l.path like concat('%',a.slug) "
    "and a.author = au.id and status like '200%' group by au.name order by count(*) desc;")

#3. On which days did more than 1% of requests lead to errors?
title3 = "On which days did more than 1% of requests lead to errors?"
errdaysquery ="select mosterrday,Errorperc from (select date(time) as mosterrday, round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) as Errorperc from log group by date(time) order by Errorperc desc) as result where Errorperc > 1 ;"

#DB Connection Function
def dbconnect():
        db = psycopg2.connect(database="news")
        cursor = db.cursor()
        return db, cursor

#Query Function
def query_db(query):
    db, cursor = dbconnect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

#Print results Function
def print_query_results(query_result,title):
    print(' ')
    print (title)
    for result in query_result:
        print(result[0] + ' --> ' + str(result[1]) + ' views')

#Print Error results function
def print_error_results(query_result,title):
    print(' ')
    print (title)
    for result in query_result:
        print("On %s with %s%s"% (result[0], result[1],"%"))

#Main code for function calls
pop3artquery_result = query_db(pop3artquery)
mostpopartquery_result = query_db(mostpopartquery)
errdaysquery_result = query_db(errdaysquery)
print_query_results(pop3artquery_result,title1)
print_query_results(mostpopartquery_result,title2)
print_error_results(errdaysquery_result,title3)