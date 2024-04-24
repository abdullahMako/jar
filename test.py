import jaydebeapi
conn = jaydebeapi.connect("com.ibm.db2.jcc.DB2Driver",
                           "jdbc:db2://{host}:{port}/db",
                           ["SA", ""],
                           "/path/to/hsqldb.jar",)
curs = conn.cursor()
curs.execute("select * from CUSTOMER")
curs.fetchall()

curs.close()
conn.close()
