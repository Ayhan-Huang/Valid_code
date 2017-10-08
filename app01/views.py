from django.shortcuts import render, HttpResponse, redirect


def test(request):
    if request.method == 'GET':
        return render(request, 'test.html')

    code1 = request.session['valid_code']
    code2 = request.POST.get('valid_code')
    if code1 == code2:
        return HttpResponse('OK')
    else:
        return redirect('/test/')


# def valid_code(request):
#     with open('bilibili.jpg', 'rb')as f:
#         res = f.read()
#
#     valid_code = 'bilibili'
#     request.session["valid_code"] = valid_code
#
#     return HttpResponse(res)

def valid_code(request):
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO  # 内存管理，优化速度
    import random

    img = Image.new(mode='RGB', size=(120, 30),
                    color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # 创建图像对象（模式，大小，颜色）

    draw = ImageDraw.Draw(img, mode='RGB')  # 创建画笔（图像对象，模式）
    font = ImageFont.truetype("app01/static/fonts/kumo.ttf", 28)  # 读取字体（字体路径，字体大小）

    code_list = []
    for i in range(5):
        char = random.choice([chr(random.randint(65, 90)), str(random.randint(1, 9))])
        code_list.append(char)
        draw.text([i * 24, 0], char, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                  font=font)
        # 通过画笔的text方法，为图像绘制字符串（位置，文本，颜色，字体）
        # [i * 24, 0] 字体坐标，i*24设置水平偏移，让每个字符分开显示

    f = BytesIO()  # 拿到一个内存文件句柄f
    img.save(f, "png")  # 保存图像对象到f
    
    valid_code = ''.join(code_list)
    request.session["valid_code"] = valid_code  # 验证码写入session
    
    return HttpResponse(f.getvalue())  # `getvalue()`方法拿到内存文件句柄的内容

# 注意，Django的session信息默认存在数据库，使用session前先执行数据库迁移，以生成django_session表