# Bài toán: Nhận diện thương hiệu - Logo trong ảnh
* ***Bài toán có ứng dụng thực tế cao, đặc biệt cho công tác quản lý và nhận diện thương hiệu.***
## Mô tả bài toán:
* **Input** : Bức ảnh có chứa logo
* **Output** : Nhận diện được các logo trong ảnh( gồm logo *UIT* , *Hội Sinh Viên* , *Khoa học máy tính* , *Công Nghệ Phầm Mềm* , *Kỹ Thuật Máy Tính* , *Khoa học và Kĩ thuật thông tin*  
	* Số lượng và độ đa dạng:
	
		- 6000 bức hình gồm ảnh chứa logo và ảnh nhiễu
		- Độ đa dạng: 90% bức hình lấy từ trên mạng, 10% bức hình chụp thực tế.
		- Chụp hình trong các điều kiện khác nhau: sáng, tối mờ, đổi màu ảnh

	* Phân chia: 
		- Train: 80%
		- Valid: 20%
## Các thao tác tiền xử lí:
	- Với bộ data train: Lọc tất cả các ảnh gây nhiễu(không chứa logo trường) bằng tay do nhóm chưa biết cách lọc bằng code nên thời gian lọc data có hơi mất thời gian. Sau khi lọc sử dụng tool LabelImg để gán nhãn dữ liệu(bounding boxes). Cuối cùng bộ data Train sẽ gồm các tấm ảnh chứa logo trường và các file .txt chứa các thông số của nhãn
	.Đưa các tấm hình về ảnh flatten.

