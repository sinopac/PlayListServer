import music_tag

def retieve_metadata(url: str):
    metadata = music_tag.load_file(url)

    return metadata
