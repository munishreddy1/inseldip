import opcua
#import time
import psycopg2


# Define OPC-UA connection parameters
url = "opc.tcp://192.168.0.1:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list = ['ns=3;s="Lab_Parameter"."TestName"','ns=3;s="Lab_Parameter"."Process_Cond"', 'ns=3;s="Lab_Parameter"."Param1"', 
             'ns=3;s="Lab_Parameter"."Param2"', 'ns=3;s="Lab_Parameter"."Param3"', 'ns=3;s="Lab_Parameter"."Param4"', 
             'ns=3;s="Lab_Parameter"."Param5"', 'ns=3;s="Lab_Parameter"."Param6"', 'ns=3;s="Lab_Parameter"."Param7"', 
             'ns=3;s="Lab_Parameter"."Param8"', 'ns=3;s="Lab_Parameter"."Param9"', 'ns=3;s="Lab_Parameter"."Param10"', 
             'ns=3;s="Lab_Parameter"."Param11"', 'ns=3;s="Lab_Parameter"."Param12"', 'ns=3;s="Lab_Parameter"."Param13"', 
             'ns=3;s="Lab_Parameter"."Param14"', 'ns=3;s="Lab_Parameter"."Param15"', 'ns=3;s="Lab_Parameter"."WeatherCond"']

# Connection to PostgreSQL database
conn = psycopg2.connect(dbname="inseldip", port= 6543, user="postgres", password="inseldip2023")

#while True:
    # Read node values
values = [client.get_node(node).get_value() for node in node_list]
    
if 'ns=3;s="Lab_Parameter"."Process_Cond"' != 1:
    # Insert values into the PostgreSQL database

    cur = conn.cursor()
    cur.execute('''INSERT INTO pre_process(testid, process_cond, param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, 
                     param11, param12, param13, param14, param15, weathercond)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], 
                     values[10], values[11], values[12], values[13],values[14], values[15], values[16], values[17]))

    conn.commit()
    #cur.close()
    #time.sleep(10)