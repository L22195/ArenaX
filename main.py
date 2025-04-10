
from qr_scanner import scan_qr_code
import pandas as pd

# تحميل البيانات
attendance_df = pd.read_csv('data/premier_league_attendance.csv')
stadiums_df = pd.read_csv('data/football_stadiums.csv')

# تحليل الحضور
def analyze_attendance(data):
    avg_attendance = data['Attendance'].mean()
    print(f"متوسط الحضور: {avg_attendance:.2f}")

# تشغيل النظام
if __name__ == '__main__':
    analyze_attendance(attendance_df)
    scan_qr_code()
