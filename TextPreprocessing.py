import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re

def remove_mentions(text, char="@"):
    import re
    pattern = re.compile(fr"{char}[A-Za-z0-9_]*")
    text = re.sub(pattern, '', text)
    return text

def remove_digits(text):
    import re
    pattern = re.compile(r"[0-9]")
    text = re.sub(pattern, '', text)
    return text

def remove_urls(text):
    import re
    url_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    text_cleaned = re.sub(url_pattern, ' ', text)

    return text_cleaned

def clean_contractions(text):
    """Text preprocessing. Converts text to lowercase. Also removes ellipses and '<unk>' when found in the text.
    Replaces contractions with their full form (e.g. "n't" becomes "not").
    """
    text = text.lower()
    text = re.sub(r'\...', '', text)
    text = re.sub(r'<unk>', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r" wo ", ' will ', text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"ma'am", "madam", text)
    text = re.sub(r"\'m", " am", text)
   
    return text

def remove_nonalphanumeric_chars(text):
    """Text preprocessing. Converts text to lowercase. Removes nonalphanumeric characters, including all punctuation.
    """
    import re
    text = text.lower()
    text = ' '.join(re.sub("[\W+]", '', t) for t in text.split())
    text = re.sub("\s+", ' ', text)

    return text
 
def remove_nonalphanumeric_chars_except_punctuation(text):
    """Text preprocessing. Converts text to lowercase. Removes nonalphanumeric characters, except specified punctuation.
    """
    import re
    text = text.lower()
    text = ' '.join(re.sub("[^A-Za-z0-9,.;]", '', t) for t in text.split())
    text = re.sub("\s+", ' ', text)
 
    return text

def remove_stopwords(text, stop_words = stopwords.words('english')):
	"""Removes stopwords from text."""
	text = text.lower()
	stop_words = set([s for s in stop_words])
	filtered_words = ' '.join(word for word in text.split(' ') if word not in stop_words)

	return filtered_words
	
def clean_tweet(text):
	text_cleaned = remove_urls(text)
	text_cleaned = ' '.join(w for w in re.split("[ ,.;:?]", text_cleaned))
	text_cleaned = remove_mentions(text_cleaned)
	text_cleaned = remove_mentions(text_cleaned, "#")
	text_cleaned = remove_digits(text_cleaned)
	text_cleaned = clean_contractions(text_cleaned)
	text_cleaned = remove_nonalphanumeric_chars(text_cleaned)
	text_cleaned = remove_stopwords(text_cleaned)
	
	return text_cleaned