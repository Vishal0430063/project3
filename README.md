# project3
# Students enter daily attendance, calculate percentages, and create graphs showing  departmental performance. 
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

# Calculate Attendance Percentage
df['Attendance %'] = (df['Present'] / df['Total']) * 100

# Save to CSV (optional)
df.to_csv('attendance_summary.csv', index=False)

# 📊 Line Chart: Date-wise Attendance Trends
for dept in df['Department'].unique():
    dept_data = df[df['Department'] == dept]
    plt.plot(dept_data['Date'], dept_data['Attendance %'], marker='o', label=dept)

plt.title('Department-wise Attendance Trend')
plt.xlabel('Date')
plt.ylabel('Attendance %')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
https://bing.com/th/id/BCEI.af7b8725-039b-4925-b452-e4c466b35a18.png

# 🥧 Pie Chart: Average Attendance by Department
avg_attendance = df.groupby('Department')['Attendance %'].mean()
avg_attendance.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Average Attendance by Department')
plt.ylabel('')
plt.tight_layout()
plt.show()
