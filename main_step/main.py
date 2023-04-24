import opcua
import psycopg2


# Define OPC-UA connection parameters
url = "opc.tcp://192.168.0.1:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list = ['ns=3;s="Datatostring"."MainStep_Concat"[0]', 'ns=3;s="Datatostring"."MainStep_Concat"[1]', 'ns=3;s="Datatostring"."MainStep_Concat"[2]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[3]', 'ns=3;s="Datatostring"."MainStep_Concat"[4]', 'ns=3;s="Datatostring"."MainStep_Concat"[5]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[6]', 'ns=3;s="Datatostring"."MainStep_Concat"[7]', 'ns=3;s="Datatostring"."MainStep_Concat"[8]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[9]', 'ns=3;s="Datatostring"."MainStep_Concat"[10]', 'ns=3;s="Datatostring"."MainStep_Concat"[11]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[12]', 'ns=3;s="Datatostring"."MainStep_Concat"[13]', 'ns=3;s="Datatostring"."MainStep_Concat"[14]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[15]', 'ns=3;s="Datatostring"."MainStep_Concat"[16]', 'ns=3;s="Datatostring"."MainStep_Concat"[17]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[18]', 'ns=3;s="Datatostring"."MainStep_Concat"[19]', 'ns=3;s="Datatostring"."MainStep_Concat"[20]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[21]', 'ns=3;s="Datatostring"."MainStep_Concat"[22]', 'ns=3;s="Datatostring"."MainStep_Concat"[23]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[24]', 'ns=3;s="Datatostring"."MainStep_Concat"[25]', 'ns=3;s="Datatostring"."MainStep_Concat"[26]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[27]', 'ns=3;s="Datatostring"."MainStep_Concat"[28]', 'ns=3;s="Datatostring"."MainStep_Concat"[29]', 
             'ns=3;s="Datatostring"."MainStep_Concat"[30]', 'ns=3;s="Datatostring"."MainStep_Concat"[31]', 'ns=3;s="Lab_Parameter"."TestName"']


# Connection to PostgreSQL database
conn = psycopg2.connect(dbname="postgres", port= 6543, user="postgres", password="inseldip2023", host="172.20.0.35")

#while True:
    # Read node values
values = [client.get_node(node).get_value() for node in node_list]
    
if 'ns=3;s="Lab_Parameter"."Process_Cond"' != 1:
    # Insert values into the PostgreSQL database

 cur = conn.cursor()
 cur.execute('DROP TABLE IF EXISTS main_steps')
cur.execute('''CREATE TABLE main_steps (ms0	text, ms1	text, ms2	text, ms3	text, ms4	text, ms5	text, ms6	text, ms7	text, 
                                        ms8	text, ms9	text, ms10	text, ms11	text, ms12	text, ms13	text, ms14	text, ms15	text, 
                                        ms16	text, ms17	text, ms18	text, ms19	text, ms20	text, ms21	text, ms22	text, ms23	text, 
                                        ms24	text, ms25	text, ms26	text, ms27	text, ms28	text, ms29	text, ms30	text, ms31	text, testid text)''')
cur.execute('''INSERT INTO main_steps (ms0, ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10, ms11, ms12, ms13, ms14, ms15, ms16, 
                                        ms17, ms18, ms19, ms20, ms21, ms22, ms23, ms24, ms25, ms26, ms27, ms28, ms29, ms30, ms31, testid)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], 
                      values[10], values[11], values[12], values[13],values[14], values[15], values[16], values[17], values[18], 
                      values[19], values[20], values[21], values[22], values[23], values[24], values[25], values[26], values[27], 
                      values[28], values[29], values[30], values[31], values[32]))

conn.commit()
 