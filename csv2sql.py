import csv
import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    create_table_query = '''CREATE TABLE houses
          (ID INT PRIMARY KEY     NOT NULL,
          LONGITUDE REAL    NOT NULL,
          LATITUDE  REAL    NOT NULL,          
          HOUSING_MEDIAN_AGE REAL    NOT NULL, 
          TOTAL_ROOMS REAL, 
          TOTAL_BEDROOMS REAL, 
          POPULATION REAL    NOT NULL, 
          HOUSEHOLDS REAL    NOT NULL, 
          MEDIAN_INCOME REAL    NOT NULL, 
          MEDIAN_HOUSE_VALUE REAL    NOT NULL, 
          OCEAN_PROXIMITY TEXT    NOT NULL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

   postgres_insert_query = '''INSERT INTO houses(ID, LONGITUDE, LATITUDE, HOUSING_MEDIAN_AGE,TOTAL_ROOMS,TOTAL_BEDROOMS,POPULATION,HOUSEHOLDS,MEDIAN_INCOME,MEDIAN_HOUSE_VALUE, OCEAN_PROXIMITY ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
   

   f = open('housing.csv','r')
   row  = 0 
   for line in f:
       l = line.rstrip().split(',')
       record_to_insert = (row, l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10])
       row += 1
       cursor.execute(postgres_insert_query, record_to_insert)
   
       connection.commit()
       count = cursor.rowcount
       print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

