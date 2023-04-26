import opcua
import psycopg2

# Define OPC-UA connection parameters
url = "opc.tcp://10.162.80.8:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list_pre_process = ['ns=3;s="Lab_Parameter"."TestName"','ns=3;s="Lab_Parameter"."Operation"','ns=3;s="Lab_Parameter"."pre_ParticleSizes"',
                         'ns=3;s="Lab_Parameter"."pre_ParticleSizeDistribution"','ns=3;s="Lab_Parameter"."AbsorptionModel"',
                         'ns=3;s="Lab_Parameter"."AbsorptionModelParameters"','ns=3;s="Lab_Parameter"."Initial_BIONS_concentration"',
                         'ns=3;s="Lab_Parameter"."InitialVolume"','ns=3;s="Lab_Parameter"."Param1"','ns=3;s="Lab_Parameter"."Param2"',
                         'ns=3;s="Lab_Parameter"."Param3"','ns=3;s="Lab_Parameter"."Param4"','ns=3;s="Lab_Parameter"."Param5"']

# Connection to PostgreSQL database
conn = psycopg2.connect(dbname="postgres", port= 5432, user="postgres", password="inseldip2023", host = "10.0.2.13")

#while True:
    # Read node values_sub_steps
values_pre_process = [client.get_node(node).get_value() for node in node_list_pre_process]

if ('"Lab_Parameter"."Recipe_Reset"' != 'Reset_post') and ('"Lab_Parameter"."Recipe_Reset"' != 'Reset_steps') and ('"Lab_Parameter"."Recipe_Reset"' != 'Reset'):
    # Insert values into the pre_process PostgreSQL database
    cur = conn.cursor()
    cur.execute('''INSERT INTO pre_process(testid, operation, particle_sizes, particle_size_distribution, absorption_model,
                absorption_model_params, initial_BIONs_concentration, initial_volume, param1, param2, param3, param4, param5)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values_pre_process[0], values_pre_process[1], values_pre_process[2], values_pre_process[3], 
                     values_pre_process[4], values_pre_process[5], values_pre_process[6], values_pre_process[7], values_pre_process[8], 
                     values_pre_process[9], values_pre_process[10], values_pre_process[11], values_pre_process[12]))
    cur.commit()
    cur.close()
    
