print ( "Nhập vào số N lớn hơn 1: " )
# Lấy dữ liệu
n  =  int ( đầu vào ())
cờ  =  Đúng 
# Kiểm tra SNT
nếu ( n  <  2 ):
    cờ  =  Sai
yêu tinh ( n  ==  2 ):
    cờ  =  Đúng
yêu tinh ( n  %  2  ==  0 ):
    cờ  =  Sai
khác :
    # xem qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
    cho  tôi  trong  phạm vi ( 3 , n , 2 ):
        nếu ( n  %  i  ==  0 ):
            cờ  =  Sai  
# Trong kết quả
nếu  cờ  ==  True :
    print ( n , " is a prime integer" )
khác :
    print ( n , "không phải là số nguyên tố" )