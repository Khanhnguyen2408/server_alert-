import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu mới
data = {
"time_window": [
    "31/12/2025 00:00",
    "31/12/2025 00:30",
    "31/12/2025 01:00",
    "31/12/2025 01:30",
    "31/12/2025 02:00",
    "31/12/2025 02:30",
    "31/12/2025 03:00",
    "31/12/2025 03:30",
    "31/12/2025 05:30",
    "31/12/2025 06:00",
    "31/12/2025 09:00",
    "31/12/2025 09:30",
    "31/12/2025 11:30",
    "31/12/2025 12:00",
    "31/12/2025 12:30",
    "31/12/2025 13:00",
    "31/12/2025 14:00",
    "31/12/2025 17:00"
],
"p_20_delayup": [
    260.0,
    257.0,
    257.4,
    298.2,
    254.0,
    250.0,
    355.0,
    281.2,
    347.0,
    266.0,
    276.0,
    354.0,
    263.0,
    272.2,
    281.4,
    148.0,
    111.0,
    115.0
]




}

# Tạo DataFrame
df = pd.DataFrame(data)

# Chuyển time_window sang datetime
df["time_window"] = pd.to_datetime(df["time_window"], format="%d/%m/%Y %H:%M")

# Vẽ đồ thị
plt.figure()
plt.plot(df["time_window"], df["p_20_delayup"], marker='o')
plt.xlabel("Time Window")
plt.ylabel("p_20_delayup (ms)")
plt.title("p20 Delay Up theo thời gian (Server 158.247.7.204)")
plt.xticks(rotation=45)
plt.tight_layout()

# Hiển thị
plt.show()
