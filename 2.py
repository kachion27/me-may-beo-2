total_revenue = 0 
numberDays_achieving_goal = 0

for i in range(1, 8):
    daily_revenue = int(input(f"Nhập doanh thu ngày {i}:"))
    total_revenue += daily_revenue
    
    if daily_revenue >= 5000000:
        numberDays_achieving_goal += 1
        
revenue_avg = int(total_revenue / 7)
    
print("\n=== BÁO CÁO DOANH THU TUẦN RIKKEI STORE ===")
print(f"Tổng doanh thu cả tuần là: {total_revenue} VND")
print(f"Doanh thu trung bình mỗi ngày là: {revenue_avg} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5000000) là: {numberDays_achieving_goal}")