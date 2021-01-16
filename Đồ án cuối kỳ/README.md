# Bài toán: Nhận diện thương hiệu - Logo trong ảnh
* ***Bài toán có ứng dụng thực tế cao, đặc biệt cho công tác quản lý và nhận diện thương hiệu.***
## Mô tả bài toán:
* **Input** : Bức ảnh có chứa logo
* **Output** : Nhận diện được các logo trong ảnh( gồm logo *UIT* , *Hội Sinh Viên* , *Khoa học máy tính* , *Công Nghệ Phầm Mềm* , *Kỹ Thuật Máy Tính* , *Khoa học và Kĩ thuật thông tin*  
	.Số lượng và độ đa dạng:
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

