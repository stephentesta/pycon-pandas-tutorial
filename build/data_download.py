import gzip
from urllib.request import urlopen

DOWNLOAD_URLS = ['ftp://ftp.fu-berlin.de/misc/movies/database/frozendata/actors.list.gz', 
    'ftp://ftp.fu-berlin.de/misc/movies/database/frozendata/actresses.list.gz',
    'ftp://ftp.fu-berlin.de/misc/movies/database/frozendata/genres.list.gz',
    'ftp://ftp.fu-berlin.de/misc/movies/database/frozendata/release-dates.list.gz']

def download_file(url, file_name): 
    try:
        # Read the file inside the .gz archive located at url 
        with urlopen(url) as response: 
            with gzip.GzipFile(fileobj=response) as uncompressed: 
                file_content = uncompressed.read()
        
        # write to file in binary mode 'wb' 
        with gzip.open(file_name, 'wb') as f:
            f.write(file_content)
            
    except Exception as e: 
        print(e)

if __name__ == "__main__":
    for url in DOWNLOAD_URLS: 
        file_name = url.split("/")[-1]
        print(f"Downloading {file_name}")
        download_file(url, file_name)