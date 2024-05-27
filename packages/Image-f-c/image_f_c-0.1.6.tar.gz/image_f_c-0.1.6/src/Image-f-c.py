from PIL import Image

def convert_image_format(input_file, output_file, output_format):
    image = Image.open(input_file)
    image.save(output_file, output_format.upper())

input_file = input("変換したい画像ファイルのパスを入力してください: ")
output_file = input("出力したいファイルの名前を入力してください: ")
output_format = input("出力したい画像の形式を入力してください (例: png, jpeg, bmp): ")

convert_image_format(input_file, output_file, output_format)