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



except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")