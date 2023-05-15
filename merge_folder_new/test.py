import opcua
import psycopg2

# Define OPC-UA connection parameters
url = "opc.tcp://10.162.80.8:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()

node_list_pre_process = ['ns=3;s="Lab_Parameter"."TestName"','ns=3;s="Lab_Parameter"."Operation"','ns=3;s="Lab_Parameter"."pre_ParticleSizes"',
                         'ns=3;s="Lab_Parameter"."pre_ParticleSizeDistribution"','ns=3;s="Lab_Parameter"."AdsorptionModel"',
                         'ns=3;s="Lab_Parameter"."AdsorptionModelParameters"','ns=3;s="Lab_Parameter"."Initial_BIONS_concentration"',
                         'ns=3;s="Lab_Parameter"."InitialVolume"','ns=3;s="Lab_Parameter"."Param1"','ns=3;s="Lab_Parameter"."Param2"',
                         'ns=3;s="Lab_Parameter"."Param3"','ns=3;s="Lab_Parameter"."Param4"','ns=3;s="Lab_Parameter"."Param5"']

node_list_post_process = ['ns=3;s="Lab_Parameter"."TestName2"','ns=3;s="Lab_Parameter"."post_ParticleSizes"',
                          'ns=3;s="Lab_Parameter"."post_ParticleSizeDistribution"','ns=3;s="Lab_Parameter"."Yield"',
                          'ns=3;s="Lab_Parameter"."Recovery"','ns=3;s="Lab_Parameter"."PurificationFactor"','ns=3;s="Lab_Parameter"."Param6"',
                          'ns=3;s="Lab_Parameter"."Param7"','ns=3;s="Lab_Parameter"."Param8"','ns=3;s="Lab_Parameter"."Param9"',
                          'ns=3;s="Lab_Parameter"."Param10"','ns=3;s="Lab_Parameter"."Param11"','ns=3;s="Lab_Parameter"."Param12"']
# Connection to PostgreSQL database
conn = psycopg2.connect(dbname="postgres", port= 5432, user="postgres", password="inseldip2023", host = "172.20.0.35")

#while True:
    # Read node values_sub_steps
values_pre_process = [client.get_node(node).get_value() for node in node_list_pre_process]
values_post_process = [client.get_node(node).get_value() for node in node_list_post_process]

if ('"Lab_Parameter"."Recipe_Reset"' != 'Reset_post') and ('"Lab_Parameter"."Recipe_Reset"' != 'Reset_steps') and ('"Lab_Parameter"."Recipe_Reset"' != 'Reset'):
            # Change values if necessary
    for i in range(len(values_pre_process)):
        if node_list_pre_process[i] == 'ns=3;s="Lab_Parameter"."Operation"':
           if values_pre_process[i] == 1:
                    values_pre_process[i] = 'Washing BIONs'
           elif values_pre_process[i] == 2:
                    values_pre_process[i] = 'Protein purification'
           elif values_pre_process[i] == 4:
                    values_pre_process[i] = 'Test'
        elif "AdsorptionModel" in node_list_pre_process[i]:
            if values_pre_process[i] == 1:
                values_pre_process[i] = "Langmuir"
            elif values_pre_process[i] == 2:
                values_pre_process[i] = "Freundlich"
            elif values_pre_process[i] == 4:
                values_pre_process[i] = "test"
    # Insert values into the pre_process PostgreSQL database
    cur = conn.cursor()
    cur.execute('''INSERT INTO pre_process(testid, operation, particle_sizes, particle_size_distribution, adsorption_model,
                adsorption_model_params, "initial_BIONs_concentration", initial_volume, param1, param2, param3, param4, param5)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values_pre_process[0], values_pre_process[1], values_pre_process[2], values_pre_process[3], 
                     values_pre_process[4], values_pre_process[5], values_pre_process[6], values_pre_process[7], values_pre_process[8], 
                     values_pre_process[9], values_pre_process[10], values_pre_process[11], values_pre_process[12]))
    conn.commit()
    cur.close()
    cur = conn.cursor()
    cur.execute('''INSERT INTO post_process(testid, particle_sizes, particle_size_distribution, yield,recovery,
                   purification_factor, param6, param7, param8, param9, param10, param11, param12)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values_post_process[0], values_post_process[1], values_post_process[2], values_post_process[3], 
                     values_post_process[4], values_post_process[5], values_post_process[6], values_post_process[7], values_post_process[8], 
                     values_post_process[9], values_post_process[10], values_post_process[11], values_post_process[12]))
    conn.commit()
    cur.close()
