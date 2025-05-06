import json
import os

EXT_DIR = "Extensions"
index = {}

for folder in os.listdir(EXT_DIR):
    subdir = os.path.join(EXT_DIR, folder)
    json_path = os.path.join(subdir, "extensions.json")
    zip_path = os.path.join(subdir, "extensions.zip")

    if os.path.isfile(json_path):
        entry = {
            "json": os.path.relpath(json_path).replace("\\", "/")
        }

        if os.path.isfile(zip_path):
            entry["zip"] = os.path.relpath(zip_path).replace("\\", "/")

        index[folder] = entry

with open("Index.json", "w") as f:
    json.dump(index, f, indent=2)

print("✅ Index.json обновлён.")
