from simfaas.ServerlessSimulator import ServerlessSimulator as Sim

sim = Sim(arrival_rate=0.9, warm_service_rate=1/1.991, cold_service_rate=1/2.244,
            expiration_threshold=600, max_time=1400, azure_trace='trace.csv')
print('done')
sim.generate_trace_azure(debug_print=False, progress=True)
sim.print_trace_results()
