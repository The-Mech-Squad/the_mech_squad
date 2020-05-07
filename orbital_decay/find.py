import tle2czml
import psycopg2
import re

def find_sat(sat_id):
    connection = psycopg2.connect(host="127.0.0.1",
                                    port="5432",
                                    database="sat_data")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select TLE_LINE0, TLE_LINE1, TLE_LINE2 from orbits WHERE object_name='{}';".format(sat_id)

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

    cursor.close()
    connection.close()


    print("Creating CZML File.....")
    # pass txt file to tle2czml

    with open('input.txt', 'r') as f, open('sats.txt', 'w') as fo:
        for line in f:
            fo.write(line.replace('"', '').replace("'", ""))

    tle2czml.create_czml("sats.txt")

    print("Completed")
