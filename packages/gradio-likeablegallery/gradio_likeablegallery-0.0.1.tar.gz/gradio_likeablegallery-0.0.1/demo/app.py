
import gradio as gr
from gradio_likeablegallery import LikeableGallery
from PIL import Image

all_images = [Image.new("RGB", (200, 200)) for _ in range(10)]


with gr.Blocks() as demo:
    with gr.Row():
        LikeableGallery(value=all_images, label="Blank", likeable=True,
                        allow_preview=True, preview=True),  # blank component
        LikeableGallery(label="Populated"),  # populated component


if __name__ == "__main__":
    demo.launch()
