import os
import json


class TextWriter:
    def __init__(self) -> None:
        with open(os.path.join(base_dir, "storage.json"), "r") as file:
            self.data = json.load(file)

    def print_names(self) -> None:
        print([i for i in self.data])

    def print_file(self, name) -> str:
        print(self.data[name])
        return self.data[name]

    def write_file(self, name: str) -> None:
        with open("main.py", "w") as f:
            f.write(self.data[name])


class TextStore:
    def read_python_files(directory: str) -> None:
        python_files = [
            file
            for file in os.listdir(directory)
            if file.endswith(".py") or file.endswith(".ipynb")
        ]
        files_data = {}

        for file_name in python_files:
            file_path = os.path.join(directory, file_name)
            with open(file_path, "r") as file:
                content = file.read()
                files_data[file_name] = content

        return files_data

    def save_to_json(data, output_file):
        with open(output_file, "w") as json_file:
            json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    directory_path = os.path.join(base_dir, "programs")
    json_output_file = os.path.join(base_dir, "storage.json")

    files_data = TextStore.read_python_files(directory_path)
    TextStore.save_to_json(files_data, json_output_file)
    print("Data successfully stored in", json_output_file)
