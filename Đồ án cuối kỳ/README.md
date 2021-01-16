# Bài toán: Nhận diện thương hiệu - Logo trong ảnh
* ***Bài toán có ứng dụng thực tế cao, đặc biệt cho công tác quản lý và nhận diện thương hiệu.***
## Mô tả bài toán:
* **Input** : Bức ảnh có chứa logo

![image](https://user-images.githubusercontent.com/63738324/104817010-2b7ade80-5851-11eb-8695-14087312330b.png)
* **Output** : Nhận diện được các logo trong ảnh( gồm logo *UIT* , *Hội Sinh Viên* , *Khoa học máy tính* , *Công Nghệ Phầm Mềm* , *Kỹ Thuật Máy Tính* , *Khoa học và Kĩ thuật thông tin*  

![image](https://user-images.githubusercontent.com/63738324/104817036-506f5180-5851-11eb-9579-52cca3cdcd47.png)


* Số lượng và độ đa dạng:
	
	- 3000 bức hình gồm ảnh chứa logo và ảnh nhiễu
	- Độ đa dạng: 85% bức hình lấy từ trên mạng, 15% bức hình chụp thực tế.
	- Chụp hình trong các điều kiện khác nhau: sáng, tối mờ, đổi màu ảnh

* Phân chia: 
	- Train: 80%
	- Valid: 20%
## Các thao tác tiền xử lí:
- Với bộ data train: Lọc tất cả các ảnh gây nhiễu(không chứa logo trường) bằng tay do nhóm chưa biết cách lọc bằng code nên thời gian lọc data có hơi mất thời gian. 
- Sau khi lọc sử dụng tool LabelImg để gán nhãn dữ liệu(bounding boxes).

	* Tham khảo ở link: [Hướng dẫn sử dụng LabelImg](https://github.com/tzutalin/labelImg)
- Cuối cùng bộ data Train sẽ gồm các tấm ảnh chứa logo trường và các file .txt chứa các thông số của nhãn

![image](https://user-images.githubusercontent.com/63738324/104817151-02a71900-5852-11eb-9dcf-29d4a97f32b7.png)

## Thuật toán máy học: 
- Sử dụng mô hình YOLOv4 (You Only Look Once)
- YOLO là một trong những mô hình phát hiện, nhận dạng vật thể được coi là tốt nhất. 
	* Tài liệu tham khảo: 
		- https://github.com/AlexeyAB/darknet
		- [Cách train mô hình YOLOv4](https://www.miai.vn/2020/05/25/yolo-series-train-yolo-v4-train-tren-colab-chi-tiet-va-day-du-a-z/)
## Báo cáo sơ bộ từng vòng và gặp trở ngại gì, điều gì chưa tốt ????
## Cần làm gì để giải quyết ??
## WORD PP 

