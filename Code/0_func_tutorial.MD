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

- Xác định đa thức theo biến t và đạo hàm đa thức -> tính giá trị đạo hàm đó
- Input: t,h,X,Y
- Output: mảng hệ số ứng với số mũ giảm dần của biến t ( từ trái -> phải)

# Tính tích phân

1. Tính tính phân bằng pp Newton Cotet (N7_TichPhan_NTCT.py)
   function H(n) tính vecto H chứa các Hi ,với i=0,1,...,n ứng với số mốc
   function I(Y,a,b) tính giá trị tích phân của tích phân xác định hàm y(x) từ a -> b
   <!-- 2+3 trong N7_TichPhan_HinhThang_XimSon.py -->
2. Tính tích phân bằng pp Hình thang ( số mốc là chẵn, min mốc là 2, n=1 ở pp Cotet)
   function HT(Y,h) với Y là vecto giá trị y , h là khoảng cách nghiệm
   Lưu ý: pp HT khi cho giá trị 2 đầu tích phân là a,b thì chia đoạn thành n phần bằng nhau (ứng với n+1 mốc, x0=a,xn = b) khi đó h = (b-a)/n
3. Tính tích phân bằng pp XimSonXí ( số mốc là lẻ, min mốc là 3, n=2 ở pp Cotet)
   function XimSon(Y,h) với Y là vecto giá trị y , h là khoảng cách nghiệm
   Lưu ý: pp XimSon khi cho giá trị 2 đầu tích phân là a,b thì chia đoạn thành 2m phần bằng nhau (ứng với 2m+1 mốc, x0=a,x2m = b) khi đó h = (b-a)/(2m)
   3.1. Tính sai số XimSon

- function Er_XS(F,a,b,name,h):
  - F là dạng symbol
  - a,b là 2 đầu mốc tích phân
  - name là tên biến
  - h là khoảng cách nghiệm đã tính theo ct: h=(b-a)/(2\*m)a
- Khi làm bài có yêu cầu về sai số thì ta phải xác định 4 điều trc khi run:
  - Kiểm tra xem hàm nhập đúng chưa ?
  - Chọn m
  - Xác định các mốc của x trong excel theo m
  - Rút ra mảng x trong code để run

# Tính tích phân 2 lớp bằng XimSon

- function XimSon2Lop(F,X,Y,a,b,d,c,n,m)
  - F là hàm symbol
  - X,Y là data của tập xác định D1
  - a,b và d,c là giới hạn các cạnh hcn ứng với trục x,y
  - n,m ứng việc chia trục x,y thành 2n và 2m đoạn
- Bảng giá trị Z ở dạng:
  -\-y--|-----|---|-----|---|------|
  ---\--| y*0 |---|-y_i-|---|y_(2m)|
  x----\|_____|___|_____|___|______|
  --x_0-|-----|---|-----|---|------|
  ------|-----|---|-----|---|------|
  --x_i-|-----|---|-----|---|------|
  ------|-----|---|-----|---|------|
  x_(2n)|-----|---|-----|---|------|
