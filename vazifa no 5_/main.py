from PIL import Image, ImageDraw, ImageFont

# Set up the image size and background color
image_size = (400, 400)
background_color = (255, 255, 255)

# Set up the font and text
font_path = "arial.ttf"
font_size = 128
font_color = (0, 0, 0)
text = "Python"

# Create a new image and get the drawing context
image = Image.new("RGB", image_size, background_color)
draw = ImageDraw.Draw(image)

# Load the font and get the size of the text
font = ImageFont.truetype(font_path, font_size)
text_size = draw.textsize(text, font)

# Calculate the x and y coordinates of the text
x = (image_size[0] - text_size[0]) / 2
y = (image_size[1] - text_size[1]) / 2

# Draw the text onto the image
draw.text((x, y), text, font=font, fill=font_color)

# Draw a heart shape onto the image
heart_size = (int(image_size[0] * 0.6), int(image_size[1] * 0.6))
heart_image = Image.new("RGBA", heart_size, (0, 0, 0, 0))
heart_draw = ImageDraw.Draw(heart_image)
heart_draw.polygon([
    (heart_size[0] / 2, 0),
    (heart_size[0], heart_size[1] / 3),
    (heart_size[0], heart_size[1]),
    (heart_size[0] / 2, heart_size[1] * 2 / 3),
    (0, heart_size[1]),
    (0, heart_size[1] / 3)
], fill=(255, 0, 0, 255))
heart_position = (int(image_size[0] * 0.2), int(image_size[1] * 0.5) - heart_size[1] // 2)
image.paste(heart_image, heart_position, heart_image)

# Save the image as a PNG file
image.save("python_logo_love.png")
