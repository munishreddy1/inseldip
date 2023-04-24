import opcua
#import time
import psycopg2


# Define OPC-UA connection parameters
url = "opc.tcp://192.168.0.1:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()

# List of nodes we want to read
node_list = ['ns=3;s="Lab_Parameter"."TestName"','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[0,1]',
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
             'ns=3;s="SS_Datatostring"."SS_String_Concat"[3,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[3,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[4,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[5,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[6,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[7,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[8,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[9,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[10,15]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,0]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,1]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,2]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,3]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,4]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,5]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,6]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,7]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,8]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,9]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,10]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,11]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,12]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,13]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,14]','ns=3;s="SS_Datatostring"."SS_String_Concat"[11,15]']


# Connection to PostgreSQL database
conn = psycopg2.connect(dbname="inseldip", port= 6543, user="postgres", password="inseldip2023", host="host.docker.internal")

#while True:
    # Read node values
values = [client.get_node(node).get_value() for node in node_list]
    
if 'ns=3;s="Lab_Parameter"."Process_Cond"' != 1:
    # Insert values into the PostgreSQL database

 cur = conn.cursor()
 cur.execute('''INSERT INTO sub_steps (testid,ss0,ss1,ss2,ss3,ss4,ss5,ss6,ss7,ss8,ss9,ss10,ss11,ss12,ss13,ss14,ss15,ss16,ss17,ss18,ss19,ss20,
ss21,ss22,ss23,ss24,ss25,ss26,ss27,ss28,ss29,ss30,ss31,ss32,ss33,ss34,ss35,ss36,ss37,ss38,ss39,ss40,ss41,ss42,ss43,ss44,ss45,ss46,ss47,ss48,
ss49,ss50,ss51,ss52,ss53,ss54,ss55,ss56,ss57,ss58,ss59,ss60,ss61,ss62,ss63,ss64,ss65,ss66,ss67,ss68,ss69,ss70,ss71,ss72,ss73,ss74,ss75,ss76,
ss77,ss78,ss79,ss80,ss81,ss82,ss83,ss84,ss85,ss86,ss87,ss88,ss89,ss90,ss91,ss92,ss93,ss94,ss95,ss96,ss97,ss98,ss99,ss100,ss101,ss102,ss103,
ss104,ss105,ss106,ss107,ss108,ss109,ss110,ss111,ss112,ss113,ss114,ss115,ss116,ss117,ss118,ss119,ss120,ss121,ss122,ss123,ss124,ss125,ss126,
ss127,ss128,ss129,ss130,ss131,ss132,ss133,ss134,ss135,ss136,ss137,ss138,ss139,ss140,ss141,ss142,ss143,ss144,ss145,ss146,ss147,ss148,ss149,
ss150,ss151,ss152,ss153,ss154,ss155,ss156,ss157,ss158,ss159,ss160,ss161,ss162,ss163,ss164,ss165,ss166,ss167,ss168,ss169,ss170,ss171,ss172,
ss173,ss174,ss175,ss176,ss177,ss178,ss179,ss180,ss181,ss182,ss183,ss184,ss185,ss186,ss187,ss188,ss189,ss190,ss191)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
                     (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], 
                      values[10], values[11], values[12], values[13],values[14], values[15], values[16], values[17], values[18], values[19],  
                      values[20], values[21], values[22], values[23], values[24], values[25], values[26], values[27], values[28], values[29], 
                      values[30], values[31], values[32], values[33], values[34], values[35], values[36], values[37], values[38], values[39], 
                      values[40], values[41], values[42], values[43], values[44], values[45], values[46], values[47], values[48], values[49],
                      values[50], values[51], values[52], values[53], values[54], values[55], values[56], values[57], values[58], values[59], 
                      values[60], values[61], values[62], values[63], values[64], values[65], values[66], values[67], values[68], values[69],  
                      values[70], values[71], values[72], values[73], values[74], values[75], values[76], values[77], values[78], values[79], 
                      values[80], values[81], values[82], values[83], values[84], values[85], values[86], values[87], values[88], values[89],
                      values[90], values[91], values[92], values[93], values[94], values[95], values[96], values[97], values[98], values[99], 
                      values[100], values[101], values[102], values[103],values[104], values[105], values[106], values[107], values[108], values[109],  
                      values[110], values[111], values[112], values[113], values[114], values[115], values[116], values[117], values[118], values[119], 
                      values[120], values[121], values[122], values[123], values[124], values[125], values[126], values[127], values[128], values[129],
                      values[130], values[131], values[132], values[133], values[134], values[135], values[136], values[137], values[138], values[139],  
                      values[140], values[141], values[142], values[143], values[144], values[145], values[146], values[147], values[148], values[149], 
                      values[150], values[151], values[152], values[153], values[154], values[155], values[156], values[157], values[158], values[159],
                      values[160], values[161], values[162], values[163], values[164], values[165], values[166], values[167], values[168], values[169],  
                      values[170], values[171], values[172], values[173], values[174], values[175], values[176], values[177], values[178], values[179], 
                      values[180], values[181], values[182], values[183], values[184], values[185], values[186], values[187], values[188], values[189],
                      values[190], values[191], values[192]))
                      

conn.commit()
    #cur.close()
    #time.sleep(10)