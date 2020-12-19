# Bài toán: Dự đoán tên của trái cây có trong ảnh
## Mô tả bài toán:
	* Input: Bức hình chứa đúng một quả, trái cây trên nền màu trắng hoặc màu sáng
	* Output: Tên của loại trái cây (VD: 'chuoi')
## Mô tả dữ liệu:
	-Phân loại những loại trái cây phổ biến tại Việt Nam (10 loại)
	-Số lượng và độ đa dạng:
	. 2000-2500 bức hình
	. Độ đa dạng: 10% bức hình lấy từ trên mạng, 90% bức hình chụp thực tế (chụp hình trái cây từ siêu thị, chợ)
	. Chụp hình trong các điều kiện khác nhau: sáng, tối mờ.

	* Phân chia: 
		- Train: 70%
		- Dev: 20%
		- Test: 10%
## 3.	Các thao tác tiền xử lí:
	.Đưa các tấm hình về size cố định (300x300)
	.Đưa các tấm hình về ảnh flatten.

