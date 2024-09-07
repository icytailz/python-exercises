import psutil

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

# Function to check cpu usage


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print(f"Alert: High CPU usage, above {CPU_THRESHOLD}%")


def check_memory_usage():
    mem_info = psutil.virtual_memory()
    mem_usage = mem_info.percent
    print(f"Current Memory Usage: {mem_usage}%")
    if mem_usage > MEM_THRESHOLD:
        print(f"Alert: High Memory usage, above {MEM_THRESHOLD}%")

# Main function


def monitor_system():
    print("Monitoring system resource usage...")
    check_cpu_usage()
    check_memory_usage()


if __name__ == "__main__":
    monitor_system()
