import opcua
import psycopg2

# Define OPC-UA connection parameters
url = "opc.tcp://10.162.80.8:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list_pre_process = ['ns=3;s="Lab_Parameter"."TestName"','ns=3;s="Lab_Parameter"."Process_Cond"', 'ns=3;s="Lab_Parameter"."Param1"', 
             'ns=3;s="Lab_Parameter"."Param2"', 'ns=3;s="Lab_Parameter"."Param3"', 'ns=3;s="Lab_Parameter"."Param4"', 
             'ns=3;s="Lab_Parameter"."Param5"', 'ns=3;s="Lab_Parameter"."Param6"', 'ns=3;s="Lab_Parameter"."Param7"', 
             'ns=3;s="Lab_Parameter"."Param8"', 'ns=3;s="Lab_Parameter"."Param9"', 'ns=3;s="Lab_Parameter"."Param10"', 
             'ns=3;s="Lab_Parameter"."Param11"', 'ns=3;s="Lab_Parameter"."Param12"', 'ns=3;s="Lab_Parameter"."Param13"', 
             'ns=3;s="Lab_Parameter"."Param14"', 'ns=3;s="Lab_Parameter"."Param15"', 'ns=3;s="Lab_Parameter"."WeatherCond"']
node_list_main_steps = ['ns=3;s="Datatostring"."MainStep_Concat"[0]', 'ns=3;s="Datatostring"."MainStep_Concat"[1]', 'ns=3;s="Datatostring"."MainStep_Concat"[2]', 
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
node_list_sub_steps = ['ns=3;s="Lab_Parameter"."TestName"','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,1]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[0,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,4]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[0,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,7]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[0,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,10]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[0,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,13]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[0,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,0]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[1,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,3]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[1,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,6]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[1,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,9]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[1,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,12]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[1,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[1,15]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[2,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,2]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[2,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,5]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[2,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,8]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[2,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,11]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[2,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[2,14]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[2,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,1]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[3,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,4]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[3,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,7]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[3,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,10]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[3,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,13]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[3,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,0]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[4,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,3]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[4,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,6]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[4,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,9]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[4,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,12]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[4,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,15]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[5,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,2]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[5,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,5]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[5,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,8]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[5,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,11]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[5,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,14]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[5,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,1]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[6,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,4]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[6,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,7]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[6,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,10]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[6,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,13]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[6,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,0]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[7,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,3]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[7,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,6]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[7,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,9]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[7,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,12]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[7,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,15]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[8,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,2]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[8,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,5]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[8,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,8]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[8,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,11]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[8,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,14]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[8,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,1]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[9,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,4]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[9,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,7]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[9,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,10]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[9,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,13]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[9,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,0]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[10,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,3]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[10,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,6]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[10,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,9]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[10,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,12]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[10,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,15]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[11,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,2]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[11,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,5]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[11,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,8]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[11,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,11]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[11,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,14]',
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[11,15]']

# Connection to PostgreSQL database
conn = psycopg2.connect(dbname="postgres", port= 5432, user="postgres", password="inseldip2023", host = "10.0.2.13")

#while True:
    # Read node values_sub_steps
values_pre_process = [client.get_node(node).get_value() for node in node_list_pre_process]
values_main_steps = [client.get_node(node).get_value() for node in node_list_main_steps]
values_sub_steps = [client.get_node(node).get_value() for node in node_list_sub_steps]
    
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

    cur = conn.cursor()
    cur.execute('''INSERT INTO pre_process(testid, process_cond, param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, 
                     param11, param12, param13, param14, param15, weathercond)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values_pre_process[0], values_pre_process[1], values_pre_process[2], values_pre_process[3], values_pre_process[4], values_pre_process[5], values_pre_process[6], values_pre_process[7], values_pre_process[8], values_pre_process[9], 
                     values_pre_process[10], values_pre_process[11], values_pre_process[12], values_pre_process[13],values_pre_process[14], values_pre_process[15], values_pre_process[16], values_pre_process[17]))
    conn.commit()
    cur.close()
#Writing values to main_steps table    
    cur = conn.cursor()
    cur.execute('''INSERT INTO main_steps (testid, ms0, ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10, ms11, ms12, ms13, ms14, ms15, ms16, 
                                        ms17, ms18, ms19, ms20, ms21, ms22, ms23, ms24, ms25, ms26, ms27, ms28, ms29, ms30, ms31)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values_main_steps[0], values_main_steps[1], values_main_steps[2], values_main_steps[3], values_main_steps[4], values_main_steps[5], values_main_steps[6], values_main_steps[7], values_main_steps[8], values_main_steps[9], 
                      values_main_steps[10], values_main_steps[11], values_main_steps[12], values_main_steps[13],values_main_steps[14], values_main_steps[15], values_main_steps[16], values_main_steps[17], values_main_steps[18], 
                      values_main_steps[19], values_main_steps[20], values_main_steps[21], values_main_steps[22], values_main_steps[23], values_main_steps[24], values_main_steps[25], values_main_steps[26], values_main_steps[27], 
                      values_main_steps[28], values_main_steps[29], values_main_steps[30], values_main_steps[31], values_main_steps[32]))
    conn.commit()
    cur.close()
#Writing values into sub_steps table    
    cur = conn.cursor()
    cur.execute('''INSERT INTO sub_steps (testid,ss0,ss1,ss2,ss3,ss4,ss5,ss6,ss7,ss8,ss9,ss10,ss11,ss12,ss13,ss14,ss15,ss16,ss17,ss18,ss19,ss20,
ss21,ss22,ss23,ss24,ss25,ss26,ss27,ss28,ss29,ss30,ss31,ss32,ss33,ss34,ss35,ss36,ss37,ss38,ss39,ss40,ss41,ss42,ss43,ss44,ss45,ss46,ss47,ss48,
ss49,ss50,ss51,ss52,ss53,ss54,ss55,ss56,ss57,ss58,ss59,ss60,ss61,ss62,ss63,ss64,ss65,ss66,ss67,ss68,ss69,ss70,ss71,ss72,ss73,ss74,ss75,ss76,
ss77,ss78,ss79,ss80,ss81,ss82,ss83,ss84,ss85,ss86,ss87,ss88,ss89,ss90,ss91,ss92,ss93,ss94,ss95,ss96,ss97,ss98,ss99,ss100,ss101,ss102,ss103,
ss104,ss105,ss106,ss107,ss108,ss109,ss110,ss111,ss112,ss113,ss114,ss115,ss116,ss117,ss118,ss119,ss120,ss121,ss122,ss123,ss124,ss125,ss126,
ss127,ss128,ss129,ss130,ss131,ss132,ss133,ss134,ss135,ss136,ss137,ss138,ss139,ss140,ss141,ss142,ss143,ss144,ss145,ss146,ss147,ss148,ss149,
ss150,ss151,ss152,ss153,ss154,ss155,ss156,ss157,ss158,ss159,ss160,ss161,ss162,ss163,ss164,ss165,ss166,ss167,ss168,ss169,ss170,ss171,ss172,
ss173,ss174,ss175,ss176,ss177,ss178,ss179,ss180,ss181,ss182,ss183,ss184,ss185,ss186,ss187,ss188,ss189,ss190,ss191)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,                 
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                             )''', 
                     (values_sub_steps[0], values_sub_steps[1], values_sub_steps[2], values_sub_steps[3], values_sub_steps[4], values_sub_steps[5], values_sub_steps[6], values_sub_steps[7], values_sub_steps[8], values_sub_steps[9], 
                      values_sub_steps[10], values_sub_steps[11], values_sub_steps[12], values_sub_steps[13],values_sub_steps[14], values_sub_steps[15], values_sub_steps[16], values_sub_steps[17], values_sub_steps[18], values_sub_steps[19],  
                      values_sub_steps[20], values_sub_steps[21], values_sub_steps[22], values_sub_steps[23], values_sub_steps[24], values_sub_steps[25], values_sub_steps[26], values_sub_steps[27], values_sub_steps[28], values_sub_steps[29], 
                      values_sub_steps[30], values_sub_steps[31], values_sub_steps[32], values_sub_steps[33], values_sub_steps[34], values_sub_steps[35], values_sub_steps[36], values_sub_steps[37], values_sub_steps[38], values_sub_steps[39], 
                      values_sub_steps[40], values_sub_steps[41], values_sub_steps[42], values_sub_steps[43], values_sub_steps[44], values_sub_steps[45], values_sub_steps[46], values_sub_steps[47], values_sub_steps[48], values_sub_steps[49],
                      values_sub_steps[50], values_sub_steps[51], values_sub_steps[52], values_sub_steps[53], values_sub_steps[54], values_sub_steps[55], values_sub_steps[56], values_sub_steps[57], values_sub_steps[58], values_sub_steps[59], 
                      values_sub_steps[60], values_sub_steps[61], values_sub_steps[62], values_sub_steps[63], values_sub_steps[64], values_sub_steps[65], values_sub_steps[66], values_sub_steps[67], values_sub_steps[68], values_sub_steps[69],  
                      values_sub_steps[70], values_sub_steps[71], values_sub_steps[72], values_sub_steps[73], values_sub_steps[74], values_sub_steps[75], values_sub_steps[76], values_sub_steps[77], values_sub_steps[78], values_sub_steps[79], 
                      values_sub_steps[80], values_sub_steps[81], values_sub_steps[82], values_sub_steps[83], values_sub_steps[84], values_sub_steps[85], values_sub_steps[86], values_sub_steps[87], values_sub_steps[88], values_sub_steps[89],
                      values_sub_steps[90], values_sub_steps[91], values_sub_steps[92], values_sub_steps[93], values_sub_steps[94], values_sub_steps[95], values_sub_steps[96], values_sub_steps[97], values_sub_steps[98], values_sub_steps[99], 
                      values_sub_steps[100], values_sub_steps[101], values_sub_steps[102], values_sub_steps[103],values_sub_steps[104], values_sub_steps[105], values_sub_steps[106], values_sub_steps[107], values_sub_steps[108], values_sub_steps[109],  
                      values_sub_steps[110], values_sub_steps[111], values_sub_steps[112], values_sub_steps[113], values_sub_steps[114], values_sub_steps[115], values_sub_steps[116], values_sub_steps[117], values_sub_steps[118], values_sub_steps[119], 
                      values_sub_steps[120], values_sub_steps[121], values_sub_steps[122], values_sub_steps[123], values_sub_steps[124], values_sub_steps[125], values_sub_steps[126], values_sub_steps[127], values_sub_steps[128], values_sub_steps[129],
                      values_sub_steps[130], values_sub_steps[131], values_sub_steps[132], values_sub_steps[133], values_sub_steps[134], values_sub_steps[135], values_sub_steps[136], values_sub_steps[137], values_sub_steps[138], values_sub_steps[139],  
                      values_sub_steps[140], values_sub_steps[141], values_sub_steps[142], values_sub_steps[143], values_sub_steps[144], values_sub_steps[145], values_sub_steps[146], values_sub_steps[147], values_sub_steps[148], values_sub_steps[149], 
                      values_sub_steps[150], values_sub_steps[151], values_sub_steps[152], values_sub_steps[153], values_sub_steps[154], values_sub_steps[155], values_sub_steps[156], values_sub_steps[157], values_sub_steps[158], values_sub_steps[159],
                      values_sub_steps[160], values_sub_steps[161], values_sub_steps[162], values_sub_steps[163], values_sub_steps[164], values_sub_steps[165], values_sub_steps[166], values_sub_steps[167], values_sub_steps[168], values_sub_steps[169],  
                      values_sub_steps[170], values_sub_steps[171], values_sub_steps[172], values_sub_steps[173], values_sub_steps[174], values_sub_steps[175], values_sub_steps[176], values_sub_steps[177], values_sub_steps[178], values_sub_steps[179], 
                      values_sub_steps[180], values_sub_steps[181], values_sub_steps[182], values_sub_steps[183], values_sub_steps[184], values_sub_steps[185], values_sub_steps[186], values_sub_steps[187], values_sub_steps[188], values_sub_steps[189],
                      values_sub_steps[190], values_sub_steps[191], values_sub_steps[192]))
    conn.commint()
    cur.close()
   
cur.close()
    
