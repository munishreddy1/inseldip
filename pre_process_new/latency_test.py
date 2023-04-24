import time
import opcua
import psycopg2
# Define OPC-UA connection parameters
url = "opc.tcp://10.162.80.8:4840"

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
conn = psycopg2.connect(dbname="postgres", port= 5432, user="postgres", password="inseldip2023", host="172.20.0.35")

# Set the number of iterations
num_iterations = 10
while True:
     values = [client.get_node(node).get_value() for node in node_list]
# Measure the time it takes to read from OPC-UA server
     start_time = time.monotonic()
     for i in range(num_iterations):
      values = [client.get_node(node).get_value() for node in node_list]
     end_time = time.monotonic()
     read_latency = (end_time - start_time) / num_iterations
     print("Average read latency: {:.2f} ms".format(read_latency * 1000))

# Measure the time it takes to write to PostgreSQL database
     start_time = time.monotonic()
     for i in range(num_iterations):
      cur = conn.cursor()
     cur.execute('''INSERT INTO pre_process(testid, process_cond, param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, 
                     param11, param12, param13, param14, param15, weathercond)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], 
                     values[10], values[11], values[12], values[13],values[14], values[15], values[16], values[17]))
     conn.commit()
     end_time = time.monotonic()
     write_latency = (end_time - start_time) / num_iterations
     print("Average write latency: {:.2f} ms".format(write_latency * 1000))
