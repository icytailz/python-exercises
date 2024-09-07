import re

log_file_path = "extract-ip-using-regex.log"

ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')  # regex to match IPv4

# process log file
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        ips = ip_pattern.findall(line)
        if ips:
            print(f"IP address found: {', '.join(ips)}")
