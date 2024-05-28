<script lang="ts">
	import FileTree from "./FileTree.svelte";
	import type { FileNode } from "./types";

	export let interactive: boolean;
	export let file_count: "single" | "multiple" = "multiple";
	export let value: string[][] = [];
	// export let ls_fn: (path: string[]) => Promise<FileNode[]>;
	let selected_folders: string[][] = [];
	let selected_files: string[][] = [];

	const paths_equal = (path: string[], path_2: string[]): boolean => {
		return path.join("/") === path_2.join("/");
	};

	const path_in_set = (path: string[], set: string[][]): boolean => {
		return set.some((x) => paths_equal(x, path));
	};

	const path_inside = (path: string[], path_2: string[]): boolean => {
		return path.join("/").startsWith(path_2.join("/"));
	};

	function map_file_path(path: string): FileNode {
		const path_parts = path.split("/").filter((x) => x.trim().length > 0);
		const is_file = !path.endsWith("/");
		return {
			name: path_parts[path_parts.length - 1],
			type: is_file ? "file" : "folder",
			path: path_parts,
			valid: is_file, // allow selection
		};
	}

	function get_all_files(value: string[][]) {
		const all_files_in = value[0];
		const all_files_mapped = all_files_in.map((file) =>
			map_file_path(file),
		);
		return all_files_mapped;
	}

	function get_selected_files(value: string[]) {
		const select_files_in = value;
		const select_files_mapped = select_files_in.map((file) =>
			file.split("/").filter((x) => x.trim().length > 0),
		);
		return select_files_mapped;
	}

	function set_selected_files(selection: string[][]) {
		const select_files = selection.map((file) => file.join("/"));
		const all_files_in = value[0];
		value = [all_files_in, select_files];
	}

	$: selected_files = get_selected_files(value[1]);
	$: all_files = get_all_files(value);
</script>

<div class="file-wrap">
	<FileTree
		path={[]}
		{all_files}
		{selected_files}
		{selected_folders}
		{interactive}
		{file_count}
		valid_for_selection={false}
		on:check={(e) => {
			const { path, checked, type } = e.detail;
			if (checked) {
				if (file_count === "single") {
					// value = [path];
					set_selected_files([path]);
				} else if (type === "folder") {
					if (!path_in_set(path, selected_folders)) {
						selected_folders = [...selected_folders, path];
					}
				} else {
					if (!path_in_set(path, selected_files)) {
						// value = [...value, path];
						set_selected_files([...selected_files, path]);
					}
				}
			} else {
				selected_folders = selected_folders.filter(
					(folder) => !path_inside(path, folder),
				); // deselect all parent folders
				if (type === "folder") {
					selected_folders = selected_folders.filter(
						(folder) => !path_inside(folder, path),
					); // deselect all children folders
					// value = value.filter((file) => !path_inside(file, path)); // deselect all children files
					set_selected_files(
						selected_files.filter(
							(file) => !path_inside(file, path),
						),
					); // deselect all children files
				} else {
					// value = value.filter((x) => !paths_equal(x, path));
					set_selected_files(
						selected_files.filter((x) => !paths_equal(x, path)),
					);
				}
			}
		}}
	/>
</div>

<style>
	.file-wrap {
		height: calc(100% - 25px);
		overflow-y: scroll;
	}
</style>
