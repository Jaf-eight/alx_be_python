import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="lyrics_app"
)

mycursor=mydb.cursor()

mycursor.execute("select * from artists where country = 'Ethiopia';")
myresult = mycursor.fetchall()
for row in myresult:
  print(row)

#mycursor.execute("update artists set artist_name = 'Betty Tezera' where artist_id = 4;")
#mydb.commit()


#for row in myresult:
  #print(row)

# Close connection to the databasse  
# mycursor.close()
# mydb.close()