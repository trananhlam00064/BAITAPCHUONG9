# bài 9.9
nhập  toán 
r  =  int ( input ( "nhập bán kính: " ))
a  =  int ( input ( "nhập chiều dài hcn: " ))
b =  int ( input ( "nhập chiều rộng hcn: " ))

S_hinh_tron  =  lambda  r : ( r ** 2 ) * ( math . pi )
S_hinh_chu_nhat  =  lambda  a , b : ( a * b )
P_hinh_tron  =  lambda  r : ( r * 2 ) * ( math . pi )
P_hinh_chu_nhat  =  lambda  a , b : ( a + b ) * 2
print ( "Diện tích hình tròn là: " , S_hinh_tron ( r ))
print ( "Diện tích hình chữ nhật là: " , S_hinh_chu_nhat ( a , b ))
print ( "chu vi hinh dang la: " , P_hinh_tron ( r ))
print ( "chu vi hinh chữ nhật là: " , P_hinh_chu_nhat ( a , b ))