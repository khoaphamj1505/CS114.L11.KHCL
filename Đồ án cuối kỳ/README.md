# Mô tả bài toán:
* Input: video từ camera hành trình của oto
* Output: Nhận dạng và phân loại các loại hình phương tiện giao thông dùng object detection
# Mô tả dữ liệu:
* Cách xây dựng dữ liệu: thu thập từ các camera hành trình trên mạng và từ mối quan hệ
* Số lượng: 100 video - 5 phút
* Độ đa dạng: nắng, mưa, tối
* Tiền xử lý: cắt tay
* Phân chia: 
	- Train: 70%
	- Dev: 20%
	- Test: 10%
# Mô tả đặc trưng:
* Các loại phương tiện:
	- Loại 1: xe 2 bánh
	- Loại 2: xe 4-7 chỗ
	- Loại 3: xe trên 7 chỗ
	- Loại 4: xe tải, xe container
