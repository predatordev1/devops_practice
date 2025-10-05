import psutil
cpu_usage_threshold = float(input("Enter the value of threshold CPU usage :"))
print("Monitoring CPU usage...")
while True:
    cpu_usage = psutil.cpu_percent()
    if (cpu_usage>=cpu_usage_threshold):
        print(F"Alert! CPU usage exceeds threshold: {cpu_usage}\n")