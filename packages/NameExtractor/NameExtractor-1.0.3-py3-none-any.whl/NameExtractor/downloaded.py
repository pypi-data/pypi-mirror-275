import nltk

def is_downloaded(r):
    """
    Check if the NLTK names corpus is already downloaded.

    Returns:
        bool: True if the names corpus is already downloaded, False otherwise.
    """
    return nltk.data.find("corpora/names.zip")