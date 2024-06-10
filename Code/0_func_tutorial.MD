#Lagrange
#Noi suy Newt #n

<!--  -->

5_BinhPhuongToiThieu #Dùng bình phương tối thiểu để tìm dạng đa thức bậc n của dữ liệu đã cho.

1. Bình phương tối thiểu với tìm đa thức
   Sử dụng hàm BPTT_DaiSo(n,X,Y)là:
   n là bậc tìm được khi ta nhìn vào đồ thị dữ liệu
   X,Y là data mảng X,Y
2. BPTT tìm biểu thức E mũ dạng Y=a\*e^{bx} và giá trị y=Y hoặc y=Y-D (nếu y có gtri âm)
   tìm trong N5_BinhPhuongToiThieu_Emu.py
3. BPTT tìm biểu thức x mũ dạng Y=a\*x^{b}
tìm trong N5_BinhPhuongToiThieu_Xmu.py
<!--  -->

#Bessel
2n+2 mốc
run:
Nhập vị trí giới hạn của X và Y trong excel
VD:
x0=40 #index = 8
h=5
X1=X1[7:11] #index =7->10
Y1=Y1[7:11]

<!--  -->

#Steclinh
2n+1 mốc
run:
Nhập vị trí giới hạn của X và Y trong excel
VD:
x0=40 #index = 8
h=5
X1=X1[7:10] #index =7->9
Y1=Y1[7:10]

<!--  -->

#Tinh dao ham (N6_DaoHam.py)
Xác định đa thức theo biến t và đạo hàm đa thức -> tính giá trị đạo hàm đó
Input: t,h,X,Y
output: mảng hệ số ứng với số mũ giảm dần của biến t ( từ trái -> phải)

# Tính tích phân
1. Tính tính phân bằng pp Newton Cotet (N7_TichPhan_NTCT.py)
function H(n) tính vecto H chứa các Hi ,với i=0,1,...,n ứng với số mốc
function I(Y,a,b) tính giá trị tích phân của tích phân xác định hàm y(x) từ a -> b

