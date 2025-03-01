import dotenv
import replicate


REPLICATE_API_TOKEN = dotenv.get_key('.env', 'REPLICATE_API_TOKEN')
HG_TOKEN = dotenv.get_key('.env', 'HG_TOKEN')
IMAGE_FOLDER_PATH = dotenv.get_key('.env', 'IMAGE_FOLDER_PATH')
ZIP_PATH = 'noto_emoji.zip'


def train():
    '''
    https://replicate.com/blog/fine-tune-flux#create-a-training-via-an-api
    '''
    model = replicate.models.create(
        owner="that1potato",
        name="flux-noto-emoji-lora",
        visibility="private",  # or "private" if you prefer
        hardware="gpu-t4",  # Replicate will override this for fine-tuned models
        description="FLUX.1 fine-tuned on noto emoji."
    )
    
    print(f"Model created: {model.name}")
    print(f"Model URL: https://replicate.com/{model.owner}/{model.name}")
    
    # Now use this model as the destination for your training
    training = replicate.trainings.create(
        version="ostris/flux-dev-lora-trainer:4ffd32160efd92e956d39c5338a9b8fbafca58e03f791f6d8011f3e20e8ea6fa",
        input={
            "input_images": open(ZIP_PATH, "rb"),
            "steps": 1000,
            # "hf_token": HG_TOKEN,  # optional
            # "hf_repo_id": HG_REPO_ID,  # optional
        },
        destination=f"{model.owner}/{model.name}"
    )
    
    print(f"Training started: {training.status}")
    print(f"Training URL: https://replicate.com/p/{training.id}")


def main():
    train()

if __name__ == "__main__":
    main()
