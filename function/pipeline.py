def compose(*functions):
    #() tuple
    """
    A higher-order function that takes multiple functions and
    returns a single function applying them in sequence.
    """
    def composed_function(x):
        for f in functions:
            x = f(x)
        return x
    return composed_function

# Some complex transformation functions
def clean_text(text):
    # Remove unwanted characters
    return ''.join(c for c in text if c.isalnum() or c.isspace())

def to_lower(text):
    return text.lower()

def remove_stopwords(text):
    stopwords = {'the', 'is', 'at', 'on'}
    return ' '.join(word for word in text.split() if word not in stopwords)

def stem_words(text):
    # Dummy stemmer (just chopping last character for demo)
    return ' '.join(word[:-1] if len(word) > 4 else word for word in text.split())

# Build a processing pipeline
process_text = compose(
    clean_text,
    to_lower,
    remove_stopwords,
    stem_words
)

# Use it
input_data = "The  cats are sitting on the mat at home."
output_data = process_text(input_data)
print(output_data)
