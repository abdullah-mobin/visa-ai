import os
import subprocess

# List of folders to search in
SEARCH_DIRECTORIES = [
    "/home/idk/Documents",
    "/home/idk/Downloads",
]

def search_and_open_file(query: str):
    try:
        query = query.lower().replace("open", "").strip()
        query_words = query.split()

        matched_files = []

        for directory in SEARCH_DIRECTORIES:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file).lower()
                    if all(word in file_path for word in query_words):
                        matched_files.append(os.path.join(root, file))

        if matched_files:
            file_to_open = matched_files[0]
            subprocess.run(["xdg-open", file_to_open])
            return f"Opening: {os.path.basename(file_to_open)}"
        else:
            return f"No file found matching: '{query}'"

    except Exception as e:
        return f"File open error: {e}"