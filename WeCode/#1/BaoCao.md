# Bài 1: Thang đo nhiệt độ KFC
Đề: Bình vừa mua xách tay một cái nhiệt kế hồng ngoại cực xịn cực chính xác chỉ mỗi tội nó hiển thị nhiệt độ theo thang đo độ F - Farenheit. Hãy giúp Bình đổi qua độ C - Celsius và độ K - Kelvin
* Code:

      from decimal import*
      F=float(input())
      getcontext().prec=6
      C=(F-32)/1.8
      K=C+273.15
      print(Decimal(C).normalize(),Decimal(K).normalize())
      
* Bình Luận:
Sử dụng các công thức để đổi từ F sang C và K
* Chú thích: 
Để Output gồm 6 chữ số nên dùng Thư viên Decimal. Có thể xem chi tiết tại link sau: https://docs.python.org/2/library/decimal.html
