import pandas as pd
import matplotlib.pyplot as plt

# Sample attendance data
data = {
    'Date': ['2025-07-01', '2025-07-01', '2025-07-02', '2025-07-02'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE'],
    'Present': [40, 35, 45, 38],
    'Total': [50, 50, 50, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Attendance Percentage
df['Attendance %'] = (df['Present'] / df['Total']) * 100

# Save to CSV (optional)
df.to_csv('attendance_summary.csv', index=False)

# 📊 Line Chart: Date-wise Attendance Trends
plt.figure(figsize=(8, 5))
for dept in df['Department'].unique():
    dept_data = df[df['Department'] == dept].sort_values('Date')
    plt.plot(dept_data['Date'], dept_data['Attendance %'], marker='o', label=dept)

plt.title('Department-wise Attendance Trend')
plt.xlabel('Date')
plt.ylabel('Attendance %')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 🥧 Pie Chart: Average Attendance by Department
avg_attendance = df.groupby('Department')['Attendance %'].mean()

plt.figure(figsize=(6, 6))
avg_attendance.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=False)
plt.title('Average Attendance by Department')
plt.ylabel('')
plt.tight_layout()
plt.show()
