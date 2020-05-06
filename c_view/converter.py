import tle2czml



# Need to pull in 3le data from the database 
# For each row
# TLE_LINE0
# TLE_LINE1
# TLE_LINE2

# Pull row from db by column name
import psycopg2
import re

try:
    connection = psycopg2.connect(host="127.0.0.1",
                                  port="5432",
                                  database="sat_data")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select TLE_LINE0, TLE_LINE1, TLE_LINE2 from orbits"

    cursor.execute("TRUNCATE orbits")
    cursor.execute(postgreSQL_select_Query)
    print("Fetching TLE Data from Database")
    orbits = cursor.fetchall() 
   
    print("Writing TLE Data to Text File")

    sats = open("input.txt","w") 
    for row in orbits:
        sats.writelines(row[0] + "\n")
        sats.writelines(row[1] + "\n")
        sats.writelines(row[2] + "\n")
    sats.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


print("Creating CZML File.....")
# pass txt file to tle2czml

with open('input.txt', 'r') as f, open('sats.txt', 'w') as fo:
    for line in f:
        fo.write(line.replace('"', '').replace("'", ""))

tle2czml.create_czml("sats.txt")

print("Completed")
