# flux-noto-emoji-lora

This is the preprocessing/training script used for fine-tunning a custom LoRA for Flux.1-dev on Google's [noto-emoji](https://github.com/googlefonts/noto-emoji) font set.

-   Huggingface repo: https://huggingface.co/potato987/flux-noto-emoji
-   Replicate repo: https://replicate.com/that1potato/flux-noto-emoji/examples

## Model

### Example

<div align="center">

| Image                                                                                 | Prompt                                                 |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| ![bear-wearing-space-suit-emoji](example_images\bear-wearing-space-suit-emoji-2.webp) | "NOTO bear wearing space suit emoji, white background" |
| ![fire-place-emoji](example_images\fire-place-emoji.webp)                             | "NOTO fire-place emoji, white background"              |
| ![flying-horse-emoji](example_images\flying-horse-emoji.webp)                         | "NOTO flying-horse emoji, white background"            |
| ![girl-with-cat-ears-emoji](example_images\girl-with-cat-ears-emoji.webp)             | "NOTO girl with cat ears emoji, white background"      |
| ![smartphone-emoji](example_images\smartphone-emoji.webp)                             | "NOTO smartphone emoji, white background"              |

</div>

### Trigger Word

You should use `NOTO` to trigger the image generation.

### Download Model

Weights for this model are available in Safetensors format on huggingface.

[Download](https://huggingface.co/potato987/flux-noto-emoji/tree/main) them in the Files & versions tab.

### How is it trained?

1. The initial image files are downloaded from the noto-emoji repo, of size 512\*512, PNG format with transparent background.
2. White background is added to the image set via [`preprocess.py`](preprocess.py).
3. BLIP is used to generate text description for each image via [`generate_img_caption.py`](generate_img_caption.py).
4. Fine-tune the model using [Replicate's flux-lora-trainer](https://replicate.com/ostris/flux-dev-lora-trainer/train).

_Please find my training config in [`config.yaml`](config.yaml)_

## License

[FLUX.1 [dev] Non-Commercial License](LICENSE.md)

## References

-   noto-emoji GitHub repo: https://github.com/googlefonts/noto-emoji
-   BLIP: https://huggingface.co/docs/transformers/model_doc/blip
-   Flux-lora-trainer: https://replicate.com/ostris/flux-dev-lora-trainer/train
