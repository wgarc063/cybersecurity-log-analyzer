import re

def analyze_logs(filename):
    with open(filename, "r") as f:
        logs = f.readlines()

    failed_attempts = {}
    for line in logs:
        match = re.search(r"Failed login from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    print("Suspicious IPs with multiple failed attempts:")
    for ip, count in failed_attempts.items():
        if count >= 3:
            print(f"{ip} - {count} failed attempts")

if __name__ == "__main__":
    analyze_logs("sample_logs.txt")
