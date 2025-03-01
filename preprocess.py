import dotenv
import os

from PIL import Image


IMAGE_FOLDER_PATH = dotenv.get_key('.env', 'IMAGE_FOLDER_PATH')


def add_white_bg(image_path) -> None:
    '''Adds a white background to PNG images.
    
    Args: image_path (str): Path to the image, expects a PNG.
    '''
    img = Image.open(image_path).convert("RGBA")
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    
    composite = Image.alpha_composite(white_bg, img)
    composite.save(image_path, 'PNG')
    
    print(f'Added white background for {image_path}')


def main():
    for file_name in os.listdir(IMAGE_FOLDER_PATH):
        if file_name.lower().endswith('.png'):
            image_path = os.path.join(IMAGE_FOLDER_PATH, file_name)
            
            add_white_bg(image_path)
    

if __name__ == '__main__':
    main()
