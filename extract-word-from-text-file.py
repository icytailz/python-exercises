log_file_path = "example.log"

with open(log_file_path, 'r') as log_file:
    for line in log_file:
        if "ERROR" in line or "WARNING" in line:
            print(line.strip())
