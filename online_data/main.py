import sys
import opcua
import time
import psycopg2

sys.path
sys.executable

# Define OPC-UA connection parameters
url = "opc.tcp://10.162.80.8:4840"

# Connect to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list = ['ns=3;s="VolumeFlowNew"', 'ns=3;s="DensityNew"', 'ns=3;s="TemperatureNew"', 'ns=3;s="MassFlowNew"', 'ns=3;s="PID_Setpoint"', 
             'ns=3;s="RSG45_DATA"."AO_MagnetTemperature"."rAnalogSignalValue"', 'ns=3;s="RSG45_DATA"."AO_MixerIstFreq"."rAnalogSignalValue"', 
             'ns=3;s="RSG45_DATA".AO_PumpIstFre.rAnalogSignalValue', 'ns=3;s="PH"', 'ns=3;s="Conductivity"', 'ns=3;s="FluidTemperatur"', 
             'ns=3;s="Density"', 'ns=3;s="VolumeFlow"', 'ns=3;s="VolumeFlowAnalog"', 'ns=3;s="VolumeFlowCorr"', 'ns=3;s="MassFlow"', 
             'ns=3;s="Photometer"', 'ns=3;s="ValveCtrl".aValves[0].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[1].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[2].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[3].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[4].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[5].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[7].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[8].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[9].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[10].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[11].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[12].bMsgIsOpen', 'ns=3;s="DIMagnetIsOn"', 
             'ns=3;s="LP_Data".VISU.StepNames.sMainStep.sValue', 'ns=3;s="LP_Data".VISU.StepNames.sSubStep.sValue', 'ns=3;s="LP_Data".VISU.StepTime.iActStepTime', 
             'ns=3;s="LP_Data".VISU.StepTime.iSetSteptime', 'ns=3;s="Counter"."Output Counter"', 'ns=3;s="LP_Data".VISU.ButtonState.bManuValvesAllowed', 
             'ns=3;s="LP_Data".VISU.ButtonState.iProductionStart', 'ns=3;s="LP_Data".VISU.ButtonState.iProductionStop', 'ns=3;s="LP_Data".VISU.ButtonState.iStandby', 
             'ns=3;s="Lab_Parameter"."ManualTransferOnOff"', 'ns=3;s="Lab_Parameter"."ContTransferOnOff"', 'ns=3;s="Lab_Parameter"."Recipe_Reset"', 
             'ns=3;s="Lab_Parameter"."Process_Cond"', 'ns=3;s="ParameterProcess"."uWorkingSet"."uSubStepParams"[12]."Params"[4]."iPumpSpeed"']
                                            
# Connect to PostgreSQL database
#conn = psycopg2.connect(dbname="suppliers", port= 6543, user="postgres", password="inseldip2023")
# Connect to PostgreSQL database docker file
conn = psycopg2.connect(dbname="inseldip", port= 6543, user="postgres", password="inseldip2023", host="host.docker.internal")
while True:
    # Read node values
    values = [client.get_node(node).get_value() for node in node_list]
    
    # Insert values into the PostgreSQL database
    cur = conn.cursor()

    cur.execute('''INSERT INTO online_data (volumeflownew, densitynew, temperaturenew, massflownew, volumeflowsetpoint, magnettemp, rotorfreq, 
                   pumpfreq, ph, conductivity, fluidtemperature, density, volumeflow, volumeflowanalog, volumeflowcorr, massflow, absorbance, 
                   valve1, valve2, valve3, valve4, valve5, valve6, valve8, valve9, valve10, valve11, valve12, valve13, magnetison, mainstepname, 
                   substepname, actsubsteptime, setsubsteptime, totalprocesstime, buttonmanualvalves, buttonproductionstart, buttonproductionstop, 
                   buttonstandby, manualtransferonoff, conttransferonoff, recipe_reset, process_cond, recipe_volume_flow) VALUES 
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  
                    %s, %s, %s, %s)''', 
                   (values[0], values[1], values[2], values[3], values[4], values[5], 
                    values[6], values[7], values[8], values[9], values[10], values[11], 
                    values[12], values[13], values[14], values[15], values[16], values[17], 
                    values[18], values[19], values[20], values[21], values[22], values[23], 
                    values[24], values[25], values[26], values[27], values[28], values[29], 
                    values[30], values[31], values[32], values[33], values[34], values[35], 
                    values[36], values[37], values[38], values[39], values[40], values[41], 
                    values[42], values[43]))
    conn.commit()
    cur.close()
    time.sleep(60)


import opcua
#import time
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
conn = psycopg2.connect(dbname="postgres", port= 5432, user="postgres", password="inseldip2023", host = "172.20.0.35")

#while True:
    # Read node values
values = [client.get_node(node).get_value() for node in node_list]
#Lab_Parameter.PreprocessTransferOnOff    
#Lab_Parameter.PostprocessTransferOnOff
if ('"Lab_Parameter"."Recipe_Reset"' != 'Reset_post') and ('"Lab_Parameter"."Recipe_Reset"' != 'Reset_steps') and ('"Lab_Parameter"."Recipe_Reset"' != 'Reset'):

    # Insert values into the PostgreSQL database

    cur = conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS pre_process1')
    #cur.execute('''CREATE TABLE pre_process1 (process_cond	int8, param1	text, param2	text, param3	text, param4	text, param5	text, 
    #                                   param6	text, param7	text, param8	text, param9	text, param10	text, param11	text, 
    #                                   param12	text, param13	text, param14	text, param15	text, testid	text, weathercond	text
    #                                   )''')
    cur.execute('''INSERT INTO pre_process1(testid, process_cond, param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, 
                     param11, param12, param13, param14, param15, weathercond)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                     (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], 
                     values[10], values[11], values[12], values[13],values[14], values[15], values[16], values[17]))

    conn.commit()   
