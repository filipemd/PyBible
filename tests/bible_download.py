import os
import pybible
import json

books = [
    "gn", "ex", "lv", "nm", "dt", "js", "jz", "rt", "1sm", "2sm", "1rs", "2rs", "1cr", "2cr", "ed", "ne", "et",
    "jó", "sl", "pv", "ec", "ct", "is", "jr", "lm", "ez", "dn", "os", "jl", "am", "ob", "jn", "mq", "na", "hc",
    "sf", "ag", "zc", "ml", "mt", "mc", "lc", "jo", "atos", "rm", "1co", "2co", "gl", "ef", "fp", "cl", "1ts",
    "2ts", "1tm", "2tm", "tt", "fm", "hb", "tg", "1pe", "2pe", "1jo", "2jo", "3jo", "jd", "ap"
]

def download_version(version):
    directory = f"bible/{version}/"
    try:
        os.makedirs(directory, exist_ok=True)  # Ensure directory exists or create it
    except Exception as e:
        print(f"Error creating directory: {e}")
        return
    
    for book in books:
        i = 0
        data = []
        while i < pybible.chapter_amount(version, book):
            print(f"Livro: {book} Capítulo: {i+1}")

            try:
                chapter_data = pybible.bible(version, book, i+1)
                data.append(chapter_data)
            except Exception as e:
                print(f"Error downloading {book} chapter {i+1}: {e}")
            
            i += 1
            
        with open(f"{directory}/{book}.json", "w") as write_file:
            json.dump(data, write_file)

download_version("nvi")
download_version("niv")
