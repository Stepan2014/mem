from PIL import Image,ImageDraw,ImageFont
print('Генератор мемов запущен!')
top_text=input( 'введиие верхний текст ')
bottom_text=input('введите нижний текст ')
print(top_text,bottom_text)


print('список картинок:')
print("1. Кот в ресторане")
print( "2. Кот в очках")
nomer=input( 'введиие номер картинки ')
nomer=int(nomer)
if nomer==1:
    kartinka='Кот в ресторане.png'
else:
    kartinka='Кот в очках.png'
print(kartinka)

image=Image.open(kartinka)
draw=ImageDraw.Draw(image)
font=ImageFont.truetype('arial.ttf',70)
draw.text((0,0),top_text,font=font,fill='black')
draw.text((0,100),bottom_text,font=font,fill='black')
image.save('mem.jpg')