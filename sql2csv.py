import psycopg2


t_host = "Your Postgres database host address" # either a domain name, an IP address, or "localhost"
t_port = "5432" # This is the default postgres port
t_dbname = "postgres"
t_user = "postgres"
t_pw = "postgres"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()

def csv_export():
    s = "'"
    s += "SELECT *"
    s += " FROM "
    s += "houses"
    s += "'"

    # set up our database connection.
    conn = psycopg2.connect...
    db_cursor = conn.cursor()

    # Use the COPY function on the SQL we created above.
    SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(s)

    # Set up a variable to store our file path and name.
    t_path_n_file = ".\users.csv"

    # Trap errors for opening the file
    try:
    WITH Open(t_path_n_file, 'w') as f_output:
        db_cursor.copy_expert(SQL_for_file_output, f_output)
    except psycopg2.Error as e:
        t_message = "Error: " + e + "/n query we ran: " + s + "/n t_path_n_file: " + t_path_n_file
        return render_template("error.html", t_message = t_message)

    # Success!

    # Clean up: Close the database cursor and connection
    db_cursor.close()
    db_conn.close()

    # Send the user on to some kind of informative screen.