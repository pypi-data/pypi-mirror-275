
import gradio as gr
from app import demo as app
import os

_docs = {'FileBrowser': {'description': 'Creates a file explorer component that allows users to browse files passed to it. As an input component,\nit also allows users to select files to be used as input to a function, while as an output component, it displays selected files.', 'members': {'__init__': {'value': {'type': 'list[list[str]] | None', 'default': 'None', 'description': 'A list of files and selected files as a `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.'}, 'file_count': {'type': '"single" | "multiple"', 'default': '"multiple"', 'description': 'Whether to allow single or multiple files to be selected. If "single", the component will return a single absolute file path as a string. If "multiple", the component will return a list of absolute file paths as a list of strings.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise.sed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'height': {'type': 'int | float | None', 'default': 'None', 'description': 'The maximum height of the file component, specified in pixels if a number is passed, or in CSS units if a string is passed. If more files are uploaded than can fit in the height, a scrollbar will appear.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will allow users to select file(s); if False, will only display files. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}, 'root': {'type': 'None', 'default': 'None', 'description': None}}, 'postprocess': {'value': {'type': 'list[list[str]] | None', 'description': 'Expects function to return a `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.'}}, 'preprocess': {'return': {'type': 'tuple[list[str], list[str]]', 'description': 'Full list of files and selected files as `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': ''}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'FileBrowser': []}}}

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
# `megickfilebrowse`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/megickfilebrowse/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/megickfilebrowse"></a>  
</div>

An extension of Gradio's FileExplorer, with more customization.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install megickfilebrowse
```

## Usage

```python
import gradio as gr
from megickfilebrowse import FileBrowser

with gr.Blocks() as demo:
    files = [
        "foo/bar/foo.txt",
        "foo/bar/foo2.txt",
        "foo/bar/",
        "foo/fuzz/hello.py",
        "foo/fuzz/",
        "foo/",
    ]
    selected_files = ["foo/bar/foo.txt"]
    b = FileBrowser(
        value=[files, selected_files], interactive=True, file_count="single"
    )

    b.change(lambda x: print("change", x), inputs=[b])


if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `FileBrowser`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["FileBrowser"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["FileBrowser"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, full list of files and selected files as `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.
- **As output:** Should return, expects function to return a `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.

 ```python
def predict(
    value: tuple[list[str], list[str]]
) -> list[list[str]] | None:
    return value
```
""", elem_classes=["md-custom", "FileBrowser-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          FileBrowser: [], };
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
