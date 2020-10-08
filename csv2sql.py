import csv
import psycopg2

filename = './traincopy.csv'

under_four = []
over_four = []

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "104.198.71.239",
                                  port = "5432",
                                  database = "train")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    pg_create_table_query = "CREATE TABLE train (id serial PRIMARY KEY, label varchar, pixels varchar);"
    cursor.execute(pg_create_table_query)

    postgres_insert_query = "INSERT INTO train (label, pixels) VALUES (%s, %s)"

    with open(filename,'r') as csvfile:

        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            if int(row[0])<=4:
                pass
                # label = row[0]
                # pixels = ''.join(row[1:])
                # print(label,pixels)
                # cursor.execute(postgres_insert_query, (label, pixels))
                # print('inserted')

            else:
                label = row[0]
                pixels = ''.join(row[1:])
                cursor.execute(postgres_insert_query, (label, pixels))


    connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
