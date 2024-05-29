
import gradio as gr
from app import demo as app
import os

_docs = {'LikeableGallery': {'description': 'Used to display a list of images as a gallery that can be scrolled through.\n', 'members': {'__init__': {'value': {'type': 'list[\n        numpy.ndarray\n        | PIL.Image.Image\n        | gradio.data_classes.FileData\n        | pathlib.Path\n        | str\n        | tuple[\n            numpy.ndarray\n            | PIL.Image.Image\n            | gradio.data_classes.FileData\n            | pathlib.Path\n            | str,\n            str,\n        ]\n        | GalleryImage\n    ]\n    | Callable\n    | None', 'default': 'None', 'description': 'List of images to display in the gallery by default. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'columns': {'type': 'int | tuple | dict | None', 'default': '2', 'description': 'Represents the number of images that should be shown in one row, for each of the six standard screen sizes (<576px(xs), <768px(sm), <992px(md), <1200px(lg), <1600px(xl), >1600px(xll)). If fewer than 6 are given then the last will be used for all subsequent breakpoints. If a dict is passed in, you can represents the number of images for each size screen with [xs,sm,md,lg,xl,xll] as the key.'}, 'height': {'type': 'int | float | None', 'default': 'None', 'description': 'The height of the gallery component, specified in pixels if a number is passed, or in CSS units if a string is passed. If more images are displayed than can fit in the height, a scrollbar will appear.'}, 'allow_preview': {'type': 'bool', 'default': 'True', 'description': 'If True, images in the gallery will be enlarged when they are clicked. Default is True.'}, 'preview': {'type': 'bool | None', 'default': 'None', 'description': 'If True, Gallery will start in preview mode, which shows all of the images as thumbnails and allows the user to click on them to view them in full size. Only works if allow_preview is True.'}, 'object_fit': {'type': '"contain" | "cover" | "fill" | "none" | "scale-down" | None', 'default': 'None', 'description': 'CSS object-fit property for the thumbnail images in the gallery. Can be "contain", "cover", "fill", "none", or "scale-down".'}, 'selected_index': {'type': 'int | None', 'default': 'None', 'description': 'The index of the image that should be initially selected. If None, no image will be selected at start. If provided, will set Gallery to preview mode unless allow_preview is set to False.'}, 'show_share_button': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will show a share icon in the corner of the component that allows user to share outputs. If False, icon does not appear.'}, 'show_download_button': {'type': 'bool | None', 'default': 'True', 'description': 'If True, will show a download button in the corner of the selected image. If False, the icon does not appear. Default is True.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'If True, the gallery will be interactive, allowing the user to upload images. If False, the gallery will be static. Default is True.'}, 'type': {'type': '"numpy" | "pil" | "filepath"', 'default': '"filepath"', 'description': 'The format the image is converted to before being passed into the prediction function. "numpy" converts the image to a numpy array with shape (height, width, 3) and values from 0 to 255, "pil" converts the image to a PIL image object, "filepath" passes a str path to a temporary file containing the image. If the image is SVG, the `type` is ignored and the filepath of the SVG is returned.'}, 'action_label': {'type': 'str | None', 'default': '"Click"', 'description': 'The label for the action button. Only displayed if `clickable` is set to True.'}, 'has_more': {'type': 'bool', 'default': 'False', 'description': 'If True, will show the "Load More" button.'}, 'load_more_button_props': {'type': 'dict | None', 'default': 'None', 'description': 'gradio Button props.'}, 'gap': {'type': 'int | tuple[int, int] | None', 'default': '8', 'description': 'The gap (px) between images. If a tuple is passed, the first value is the gap for width and the second value is the gap for height.If a number is passed, the gap will be the same for width and height.'}, 'clickable': {'type': 'bool | None', 'default': 'None', 'description': 'Whether the gallery image display an action button. Set automatically by the .click method but has to be present in the signature for it to show up in the config.'}, 'likeable': {'type': 'bool | None', 'default': 'None', 'description': 'Whether the gallery image display a like or dislike button. Set automatically by the .like method but has to be present in the signature for it to show up in the config.'}}, 'postprocess': {'value': {'type': 'list[\n        numpy.ndarray\n        | PIL.Image.Image\n        | gradio.data_classes.FileData\n        | pathlib.Path\n        | str\n        | tuple[\n            numpy.ndarray\n            | PIL.Image.Image\n            | gradio.data_classes.FileData\n            | pathlib.Path\n            | str,\n            str,\n        ]\n        | GalleryImage\n        | dict\n    ]\n    | None', 'description': 'list of images, or list of (image, caption) tuples'}}, 'preprocess': {'return': {'type': 'list[GalleryImage] | None', 'description': "The preprocessed input data sent to the user's function in the backend."}, 'value': None}}, 'events': {'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the LikeableGallery. Uses event data gradio.SelectData to carry `value` referring to the label of the LikeableGallery, and `selected` to refer to state of the LikeableGallery. See EventData documentation on how to use this event data'}, 'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the LikeableGallery changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'like': {'type': None, 'default': None, 'description': 'This listener is triggered when the user likes/dislikes from within the LikeableGallery. This event has EventData of type gradio.LikeData that carries information, accessible through LikeData.index and LikeData.value. See EventData documentation on how to use this event data.'}, 'click': {'type': None, 'default': None, 'description': 'Triggered when the image action button is clicked.'}, 'load_more': {'type': None, 'default': None, 'description': ''}}}, '__meta__': {'additional_interfaces': {'GalleryImage': {'source': 'class GalleryImage(GradioModel):\n    image: Union[FileData, Path, str]\n    caption: Optional[str] = None\n    liked: Optional[bool] = None\n    # custom meta data\n    meta: Optional[Any] = None'}}, 'user_fn_refs': {'LikeableGallery': ['GalleryImage']}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_likeablegallery`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_likeablegallery
```

## Usage

```python

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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `LikeableGallery`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["LikeableGallery"]["members"]["__init__"], linkify=['GalleryImage'])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["LikeableGallery"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, the preprocessed input data sent to the user's function in the backend.
- **As output:** Should return, list of images, or list of (image, caption) tuples.

 ```python
def predict(
    value: list[GalleryImage] | None
) -> list[
        numpy.ndarray
        | PIL.Image.Image
        | gradio.data_classes.FileData
        | pathlib.Path
        | str
        | tuple[
            numpy.ndarray
            | PIL.Image.Image
            | gradio.data_classes.FileData
            | pathlib.Path
            | str,
            str,
        ]
        | GalleryImage
        | dict
    ]
    | None:
    return value
```
""", elem_classes=["md-custom", "LikeableGallery-user-fn"], header_links=True)




    code_GalleryImage = gr.Markdown("""
## `GalleryImage`
```python
class GalleryImage(GradioModel):
    image: Union[FileData, Path, str]
    caption: Optional[str] = None
    liked: Optional[bool] = None
    # custom meta data
    meta: Optional[Any] = None
```""", elem_classes=["md-custom", "GalleryImage"], header_links=True)

    demo.load(None, js=r"""function() {
    const refs = {
            GalleryImage: [], };
    const user_fn_refs = {
          LikeableGallery: ['GalleryImage'], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
