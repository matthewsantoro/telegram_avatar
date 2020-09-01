from PIL import Image, ImageDraw, ImageFont


def create_empty_background():
    return Image.new('RGBA', (512, 512), (0, 0, 0, 255))


def choose_icon(filename):
    return Image.open(f'images/{filename}.png')


def generate_image(data):
    background = create_empty_background()
    icon = choose_icon(data['icon'])
    background_w, background_h = background.size
    icon_w, icon_h = icon.size
    area = (
        int((background_w - icon_w) / 2),
        int((background_h - icon_h) / 2),
        int((background_w - icon_w) / 2 + icon_w),
        int((background_h - icon_h) / 2 + icon_h)
    )
    background.paste(icon, area, icon)
    font = ImageFont.truetype("font/YanoneKaffeesatz-VariableFont_wght.ttf", 100)

    img_text = Image.new("RGBA", background.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img_text)

    text = data['dt']
    text_w, text_h = font.getsize(text)
    print(text_h)
    text_area = (int((background_w - text_w) / 2),
                 int(area[1] / 2 - text_h / 2))

    d.text(text_area, text, font=font, fill=(255, 255, 255, 255))

    text = f'{data["temp"]}°C'
    text_w, text_h = font.getsize(text)
    print(text_h)
    text_area = (int((background_w - text_w) / 2),
                 int(background_h - (area[1] / 2 + text_h / 2)))
    d.text(text_area, text, font=font, fill=(255, 255, 255, 255))

    result = Image.alpha_composite(background, img_text)
    result.show()
    result.save('images/result.png', 'PNG')


data = {'dt': '22:00',
        'temp': '17',
        'icon': '04d'}

generate_image(data)

