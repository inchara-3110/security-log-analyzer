
from collections import Counter

LOG_FILE = "sample_logs.txt"
FAILURE_THRESHOLD = 3


def analyze_logs():
    total_events = 0
    successful_logins = 0
    failed_logins = 0
    failed_ips = Counter()

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            total_events += 1

            if "LOGIN_SUCCESS" in line:
                successful_logins += 1

            elif "LOGIN_FAILED" in line:
                failed_logins += 1

                for item in line.split():
                    if item.startswith("ip="):
                        ip_address = item.split("=", 1)[1]
                        failed_ips[ip_address] += 1

    print("===== SECURITY LOG ANALYZER =====")
    print(f"Total events: {total_events}")
    print(f"Successful logins: {successful_logins}")
    print(f"Failed logins: {failed_logins}")
    print("\n===== SUSPICIOUS IP ADDRESSES =====")

    found_suspicious_ip = False

    for ip_address, count in failed_ips.items():
        if count >= FAILURE_THRESHOLD:
            print(f"WARNING: {ip_address} had {count} failed logins")
            found_suspicious_ip = True

    if not found_suspicious_ip:
        print("No IP addresses reached the failure threshold.")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    analyze_logs()
