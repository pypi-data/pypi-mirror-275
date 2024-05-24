from my_data_preprocessor_mz.text_cleaner import TextCleaner

text = ("Hello world! This is a test running for the TextCleaner class. It's designed to remove stopwords, "
        "punctuation, and to perform lemmatization.")

cleaner = TextCleaner()

lowercase_text = cleaner.to_lowercase(text)
print("Lowercase text:")
print(lowercase_text)

no_punctuation_text = cleaner.remove_punctuation(lowercase_text)
print("\nText without punctuation:")
print(no_punctuation_text)

no_stopwords_text = cleaner.remove_stopwords(no_punctuation_text)
print("\nText without stopwords:")
print(no_stopwords_text)

lemmatized_text = cleaner.lemmatize_text(no_stopwords_text)
print("\nLemmatized text:")
print(lemmatized_text)

cleaned_text = cleaner.clean_text(text)
print("\nFully cleaned text:")
print(cleaned_text)