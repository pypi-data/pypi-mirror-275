import os
import json

base_dir = os.path.dirname(__file__)
directory_path = os.path.join(base_dir, "programs")
json_output_file = os.path.join(base_dir, "storage.json")


class Writer:
    def __init__(self) -> None:
        with open(os.path.join(base_dir, "storage.json"), "r") as file:
            self.data = json.load(file)

    def names(self) -> None:
        print([i for i in self.data])

    def get(self, name: str):
        cells = json.loads(self.data[name])["cells"]
        text = ""
        sources = [cell["source"] for cell in cells]
        for i in sources:
            text += "".join(i)
        return text

    def write(self, name: str) -> None:
        with open("main.ipynb", "w") as f:
            f.write(self.data[name])


class Store:
    def read(directory: str) -> None:
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

    def save(data, output_file):
        with open(output_file, "w") as json_file:
            json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    files_data = Store.read(directory_path)
    Store.save(files_data, json_output_file)
    print("Data successfully stored in", json_output_file)
