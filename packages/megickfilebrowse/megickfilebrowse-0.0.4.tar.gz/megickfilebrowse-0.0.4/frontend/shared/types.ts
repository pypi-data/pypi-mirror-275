export interface FileNode {
	type: "file" | "folder";
	name: string;
	path: string[];
	valid?: boolean;
}
