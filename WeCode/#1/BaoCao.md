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
# Bài 2: Độ đo áp suất SI/PSI
Đề: Tìm ra áp suất chất lỏng/khí và cách đo đạt chúng là một vấn đề nghiên cứu vật lý thực nghiệm từng làm đau đầu nhiều nhà khoa học thời trung cổ. Đã có nhiều nhà khoa học khác nhau đề xuất các thang đo khác nhau. Tuy nhiên ngày nay một đơn vị đo áp suất phổ thông mà dễ hiểu là tính lực tác động (theo khối lượng) chia cho diện tích. Khổ nổi trong hệ đo lường quốc tế (SI) và hệ đo Imperial phổ biến ở Mỹ người ta đo khối lượng và áp suất bằng cách đơn vị khác nhau. Bạn Bình vừa mua một con mô-tô phân khối lớn hàng nhập nguyên chiếc từ Mỹ về, tài liệu hướng dẫn của xe ghi áp suất phù hợp khi bơm xe bằng đơn vị PSI (Pound / square inches - 1 pound lực trên một inch vuông). Còn ống bơm của Bình tích hợp đồng hồ đo áp suất bằng đơn vị kg/cm2 (1 kilogram lực trên một centimét vuông).

Biết: 1 pound = 0.453592 kg

và 1 inch = 2,54 cm

Viết công thức giúp Bình đổi PSI sang kg/cm2
* Code:

      from decimal import*
      getcontext().prec=6
      a=float(input())
      print(Decimal((a*0.453592)/(2.54*2.54)).normalize())
* Bình luận: 
Sử dụng công thức toán để tính
* Chú thích:
Tương tự bài 1 sử dụng Decimal để output gồm 6 chữ số.
