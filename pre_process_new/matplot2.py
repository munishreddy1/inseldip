latencies = []
for i in range(num_iterations):
    start_time = time.monotonic()
    values = [client.get_node(node).get_value() for node in node_list]
    end_time = time.monotonic()
    read_latency = (end_time - start_time) * 1000
    latencies.append(read_latency)
