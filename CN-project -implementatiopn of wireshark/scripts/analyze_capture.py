import pyshark

cap = pyshark.FileCapture('results/capture.pcap')
print("\n--- Packet Summary ---\n")
packet_count = 0

for i, packet in enumerate(cap):
    try:
        src = packet.ip.src
        dst = packet.ip.dst
        proto = packet.transport_layer or packet.highest_layer

        print(f"Packet {i+1}:")
        print(f"Source: {src}")
        print(f"Destination: {dst}")
        print(f"Protocol: {proto}\n")

        packet_count += 1
    except AttributeError:
        continue

print(f"[+] Total Packets Analyzed: {packet_count}")
