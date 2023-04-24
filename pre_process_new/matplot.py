import opcua
import psycopg2
import time
import matplotlib.pyplot as plt
url = "opc.tcp://10.162.80.8:4840"

# Connection to OPC-UA server
client = opcua.Client(url)
client.connect()
# Define the number of iterations and node list
num_iterations = 10
node_list = ['ns=3;s="Lab_Parameter"."TestName"', 'ns=3;s="Lab_Parameter"."Process_Cond"', 'ns=3;s="Lab_Parameter"."Param1"']

# Measure the read latency
start_time = time.monotonic()
latencies = []
for i in range(num_iterations):
    values = [client.get_node(node).get_value() for node in node_list]
    end_time = time.monotonic()
    read_latency = (end_time - start_time) * 1000
    latencies.append(read_latency)

# Plot the results
plt.plot(range(1, num_iterations+1), latencies)
plt.xlabel('Iteration')
plt.ylabel('Read Latency (ms)')
plt.title('Read Latency for {} Iterations'.format(num_iterations))
plt.show()
