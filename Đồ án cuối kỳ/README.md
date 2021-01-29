# Bài toán: Nhận diện thương hiệu - Logo trong ảnh
* ***Bài toán có ứng dụng thực tế cao, đặc biệt cho công tác quản lý và nhận diện thương hiệu.***
> [Model_YOLOv4](https://github.com/khoaphamj1505/CS114.L11.KHCL/blob/master/%C4%90%E1%BB%93%20%C3%A1n%20cu%E1%BB%91i%20k%E1%BB%B3/Train_model.ipynb)

> [Dự đoán hình ảnh](https://github.com/khoaphamj1505/CS114.L11.KHCL/blob/master/%C4%90%E1%BB%93%20%C3%A1n%20cu%E1%BB%91i%20k%E1%BB%B3/img_detect.py)

> [Dự đoán bằng camera (Realtime_detection)](https://github.com/khoaphamj1505/CS114.L11.KHCL/blob/master/%C4%90%E1%BB%93%20%C3%A1n%20cu%E1%BB%91i%20k%E1%BB%B3/realtime_detect.py)

## Mô tả bài toán:
* **Input** : Bức ảnh có chứa logo

![image](https://user-images.githubusercontent.com/63738324/104817010-2b7ade80-5851-11eb-8695-14087312330b.png)
* **Output** : Nhận diện được các logo trong ảnh( gồm logo *UIT* , *Hội Sinh Viên* , *Khoa học máy tính* , *Công Nghệ Phầm Mềm* , *Kỹ Thuật Máy Tính* , *Khoa học và Kĩ thuật thông tin*  

![image](https://user-images.githubusercontent.com/63738324/104817036-506f5180-5851-11eb-9579-52cca3cdcd47.png)


* Số lượng và độ đa dạng:
	
	- 3000 bức hình gồm ảnh chứa logo và ảnh nhiễu
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

- Dữ liệu sau khi được dán nhãn sẽ trộn lên ngẫu nhiên để mang đi train. Đồng thời tạo chọn ngẫu nhiên 20% dữ liệu dùng để kiểm tra độ chính xác của model trong quá trình training

## Thuật toán máy học: 
- Sử dụng mô hình YOLOv4 (You Only Look Once)
- YOLO là một trong những mô hình phát hiện, nhận dạng vật thể được coi là tốt nhất. 
	* Tài liệu tham khảo: 
		- https://github.com/AlexeyAB/darknet
		- [Cách train mô hình YOLOv4](https://www.miai.vn/2020/05/25/yolo-series-train-yolo-v4-train-tren-colab-chi-tiet-va-day-du-a-z/)
## Các bước cài đặt chương trình:
- Cài đặt tổng quát:
	- Ngôn ngữ sử dụng: Python
	- Công cụ thực hiện: VScode, Google Colab
	- Thư viện sử dụng: math, os, numpy, glob2
- Cài đặt Yolov4:
	* Bước 1: Tải mã nguồn Yolov4 về drive
	* Bước 2: Tải file pre-trained
	* Bước 3: Tạo file obj.names và obj.data
	* Bước 4: Chỉnh sửa tệp MAKEFILE
	* Bước 5: Chỉnh sửa tệp config trong darknet

## Demo
- Dự đoán logo bằng camera laptop
<img src="https://raw.githubusercontent.com/khoaphamj1505/CS114.L11.KHCL/master/%C4%90%E1%BB%93%20%C3%A1n%20cu%E1%BB%91i%20k%E1%BB%B3/Laptop_cam.gif" width="400" height="400" />
- Dự đoán logo bằng camera điện thoại
<img src="https://github.com/khoaphamj1505/CS114.L11.KHCL/blob/master/%C4%90%E1%BB%93%20%C3%A1n%20cu%E1%BB%91i%20k%E1%BB%B3/Mobile_cam.gif?raw=true" width="400" height="400" />

## Khó khăn:
- Mô hình chưa giải quyết được các logo quá nhỏ.
- Thời gian predict còn hơi chậm.
## Hướng giải quyết:
- Nhóm đang train lại model khác là yolov4-custom để khắc phục các lỗi không nhận dạng được logo quá nhỏ. Có thể cải thiện dataset nhiều hơn, tiền xử lý hình ảnh…
- Xử lý các trường hợp khó hơn: dạng logo mất một nửa

