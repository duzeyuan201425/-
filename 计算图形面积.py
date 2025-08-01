a = '三角形'
b = '正方形'
c = '长方形'
d = '圆形'
e = '椭圆形'
print("你好，我是一个计算几何图形面积的程序。")
input_shape = input("请输入你想计算的图形类型(a-三角形,b-正方形,c-长方形,d-圆形,e-椭圆形):")
if input_shape == a:
    bace = float(input("请输入三角形的底边长度："))
    height = float(input("请输入三角形的高度："))
    print('三角形的面积为' + str(bace * height / 2))
elif input_shape == b:
    side = float(input('请输入正方形的边长：'))
    print('正方形的面积为' + str(side ** 2))
elif input_shape == c:
    length = float(input('请输入长方形的长度：'))
    width = float(input('请输入长方形的宽度：'))
    print('长方形的面积为' + str(length * width))
elif input_shape == d:
    radius = float(input('请输入圆形的半径：'))
    print('圆形的面积为' + str(3.14 * radius ** 2))
elif input_shape == e:
    major_axis = float(input('请输入椭圆的长轴长度：'))
    minor_axis = float(input('请输入椭圆的短轴长度：'))
    print('椭圆的面积为' + str(3.14 * major_axis * minor_axis))
else:
    print('error！: 输入的图形类型不正确。我们只收录了5种图形类型')
print("感谢使用计算几何图形面积的程序。")


