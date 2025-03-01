import os

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


IMAGE_FOLDER_PATH = 'noto_emoji_dataset/512/'


def generate_image_caption(image_path: str, model: BlipForConditionalGeneration, processor: BlipProcessor) -> str:
    '''Generates a descriptive caption for the input image.
    
    Args:
        image_path (str): The path of the image file

    Returns:
        caption (str): A description of the image
    '''
    
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors='pt')
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption

def generate_caption_file(file_name: str, caption: str) -> None:
    '''Generates a .txt file with the same image file name containing the image caption.
    
    Args:
        file_name (str): The name of the image file you wish to generate a caption for
        caption (str): A description of the image
    '''
    # generate .txt file containing the caption
    base_name, _ = os.path.splitext(file_name)
    file_path = os.path.join(IMAGE_FOLDER_PATH, base_name + '.txt')
    
    with open(file_path, 'w') as file:
        file.write(caption)
    
    print(f'File created: {file_path}, caption: {caption}')


def main():
    # initialise BLIP
    blip_processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base', cache_dir='blip_weights')
    blip = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base', cache_dir='blip_weights')
    
    for file_name in os.listdir(IMAGE_FOLDER_PATH):
        if file_name.lower().endswith('.png'):
            image_path = os.path.join(IMAGE_FOLDER_PATH, file_name)
            
            caption = generate_image_caption(image_path, blip, blip_processor)
            
            generate_caption_file(file_name, caption)
    

if __name__ == "__main__":
    main()
