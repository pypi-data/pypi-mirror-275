"""megickfilebrowse component"""

from __future__ import annotations

import fnmatch
import os
from pathlib import Path
from typing import Any, Callable, List, Literal, Tuple, TypedDict

from pathlib import Path

from gradio_client.documentation import document

from gradio.components.base import Component, server
from gradio.data_classes import GradioRootModel


class FileExplorerData(GradioRootModel):
    root: list[list[str]]


class ListFileResult(TypedDict):
    name: str
    type: str
    valid: bool


class FileBrowser(Component):
    """
    Creates a file explorer component that allows users to browse files passed to it. As an input component,
    it also allows users to select files to be used as input to a function, while as an output component, it displays selected files.
    """

    EVENTS = ["change"]
    data_model = FileExplorerData

    def __init__(
        self,
        *,
        value: list[list[str]] | None = None,
        file_count: Literal["single", "multiple"] = "multiple",
        label: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        height: int | float | None = None,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | None = None,
        root: None = None,
    ):
        """
        Parameters:
            value: A list of files and selected files as a `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.
            file_count: Whether to allow single or multiple files to be selected. If "single", the component will return a single absolute file path as a string. If "multiple", the component will return a list of absolute file paths as a list of strings.
            label: The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise.sed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            height: The maximum height of the file component, specified in pixels if a number is passed, or in CSS units if a string is passed. If more files are uploaded than can fit in the height, a scrollbar will appear.
            interactive: if True, will allow users to select file(s); if False, will only display files. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            key: if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.
        """
        valid_file_count = ["single", "multiple"]
        if file_count not in valid_file_count:
            raise ValueError(
                f"Invalid value for parameter `file_count`: {file_count}. Please choose from one of: {valid_file_count}"
            )
        self.file_count = file_count
        self.height = height

        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            key=key,
            value=value,
        )

    def example_payload(self) -> Any:
        return [["Users", "gradio", "app.py"]]

    def example_value(self) -> Any:
        return ["Users", "gradio", "app.py"]

    def preprocess(
        self, payload: FileExplorerData | None
    ) -> Tuple[list[str], list[str]]:
        """
        Parameters:
            payload: List of files and selected files as a FileExplorerData object.
        Returns:
            Full list of files and selected files as `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.
        """
        if payload is None:
            return FileExplorerData(root=[[], []])

        if self.file_count == "single":
            if len(payload.root[1]) > 1:
                raise ValueError(
                    f"Expected only one file, but {len(payload.root)} were selected."
                )
        try:
            for f in payload.root[0]:
                Path(f)
            for f in payload.root[1]:
                Path(f)
        except Exception as e:
            raise ValueError(f"Expected all paths to be valid, but got an error: {e}")
        return payload.root[0], payload.root[1]

    def postprocess(self, value: list[list[str]] | None) -> FileExplorerData:
        """
        Parameters:
            value: Expects function to return a `list[list[str]]`, the first list is a list of files and the second list is a list of selected files.
        Returns:
            A FileExplorerData object containing the full list of files and selected files.
        """
        if value is None:
            return FileExplorerData(root=[[], []])

        assert isinstance(value, list)

        if len(value) > 2:
            raise ValueError(
                f"Expected only two lists, but {len(value)} were returned."
            )
        assert all(isinstance(param, list) for param in value)

        try:
            for f in value[0]:
                Path(f)
            for f in value[1]:
                Path(f)
        except Exception as e:
            raise ValueError(f"Expected all paths to be valid, but got an error: {e}")
        return FileExplorerData(root=value)
