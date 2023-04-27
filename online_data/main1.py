import opcua
import time
import psycopg2

# Define OPC-UA connection parameters
url = "opc.tcp://10.162.80.8:4840"

# Connect to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list = ['ns=3;s="Lab_Parameter"."TestName3"', 'ns=3;s="RSG45_DATA"."AO_MagnetTemperature"."rAnalogSignalValue"', 
             'ns=3;s="RSG45_DATA"."AO_MixerIstFreq"."rAnalogSignalValue"', 'ns=3;s="RSG45_DATA".AO_PumpIstFre.rAnalogSignalValue', 
             'ns=3;s="FluidTemperatur"', 'ns=3;s="Conductivity"', 'ns=3;s="PH"', 'ns=3;s="Density"', 'ns=3;s="VolumeFlow"', 
             'ns=3;s="VolumeFlowAnalog"', 'ns=3;s="TempCoriolis"', 'ns=3;s="MassFlow"', 'ns=3;s="Photometer"', 'ns=3;s="PID_Setpoint"', 
             'ns=3;s="ValveCtrl".aValves[0].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[1].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[2].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[3].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[4].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[5].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[7].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[8].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[9].bMsgIsOpen', 
             'ns=3;s="ValveCtrl".aValves[10].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[11].bMsgIsOpen', 'ns=3;s="ValveCtrl".aValves[12].bMsgIsOpen', 
             'ns=3;s="DIMagnetIsOn"', 'ns=3;s="LP_Data".VISU.StepNames.sMainStep.sValue', 'ns=3;s="LP_Data".VISU.StepNames.sSubStep.sValue', 
             'ns=3;s="LP_Data".VISU.StepTime.iActStepTime', 'ns=3;s="LP_Data".VISU.StepTime.iSetSteptime', 'ns=3;s="Counter"."Output Counter"', 
             'ns=3;s="Lab_Parameter"."AutoTransferOnOff"', 'ns=3;s="Lab_Parameter"."ContTransferOnOff"', 'ns=3;s="ParameterProcess"."uWorkingSet"."uSubStepParams"[12]."Params"[4]."iPumpSpeed"', 
             'ns=3;s="VolumeFlowNew"', 'ns=3;s="DensityNew"', 'ns=3;s="MassFlowNew"', 'ns=3;s="TemperatureNew"',]
                                            
# Connect to PostgreSQL database
conn = psycopg2.connect(dbname="postgres", port= 5432, user="postgres", password="inseldip2023", host="10.0.2.13")
while True:
    # Read node values
    values = [client.get_node(node).get_value() for node in node_list]
    
    # Insert values into the PostgreSQL database
    cur = conn.cursor()

    cur.execute('''INSERT INTO online_data (testid3, magnettemp, rotorfreq, pumpfreq, fluidtemp, conductivity, ph, density, 
                   voumeflow, volumeflowanalog, "TempCoriolis", massflow, absorbance, volumeflowsetpoint, valve1, valve2, 
                   valve3, valve4, valve5, valve6, valve8, valve9, valve10, valve11, valve12, valve13, magnetstatus, mainstepname, 
                   substepname, actsubsteptime, setsubsteptime, totalprocesstime, manualtransferonoff, conttransferonoff, recipe_vf, 
                   "VolumeFlowNew", "DensityNew", "MassFlowNew", "TemperatureNew") VALUES 
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, )''', 
                   (values[0], values[1], values[2], values[3], values[4], values[5], 
                    values[6], values[7], values[8], values[9], values[10], values[11], 
                    values[12], values[13], values[14], values[15], values[16], values[17], 
                    values[18], values[19], values[20], values[21], values[22], values[23], 
                    values[24], values[25], values[26], values[27], values[28], values[29], 
                    values[30], values[31], values[32], values[33], values[34], values[35], 
                    values[36], values[37], values[38]))
    conn.commit()
    cur.close()
    time.sleep(60)
