import pyshark
import sys
print("Using Python from:", sys.executable)
def capture_packets():
    capture = pyshark.LiveCapture(interface='Wi-Fi', output_file='results/capture.pcap')
    capture.sniff(timeout=10)  # Captures for 10 seconds

if __name__ == "__main__":
    capture_packets()
