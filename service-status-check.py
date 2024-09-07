import subprocess


def check_service_status(service_name):
    try:
        # Run systemctl status command to check the service statusus
        result = subprocess.run(['systemctl', 'is-active', service_name],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout.strip() == "active":
            print(f"The service '{service_name}' is running.")
        else:
            print(f"The service '{service_name}' is not running.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main
if __name__ == "__main__":
    service_name = input("Enter the service name: ")
    check_service_status(service_name)
