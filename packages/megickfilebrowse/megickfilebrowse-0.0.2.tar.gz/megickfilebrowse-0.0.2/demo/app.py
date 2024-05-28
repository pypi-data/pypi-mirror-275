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
