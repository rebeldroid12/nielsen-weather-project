from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from wordcloud import STOPWORDS
from helpers.words import CLIMATE_CHANGE_RELATED_WORDS, CLIMATE_CHANGE_RELATED_PHRASES
from helpers.cc_words import CC_WORDS, CC_PHRASES
from thefuzz import fuzz
import docx
from simplify_docx import simplify


def docx_to_clean_dict(docx_as_json, first_table_index=1):
    """Takes docx_as_json and cleans it up
    return: list of dicts
      {
        "time": ___,
        "location": ____,
        "station": ____,
        "text": _____________
      }
    """
    clean_data = []

    for blob in docx_as_json['VALUE'][0]['VALUE'][first_table_index:]:
        text_end = False

        if blob['TYPE'] == 'table':
            time = blob['VALUE'][0]['VALUE'][0]['VALUE'][0]['VALUE'][0]['VALUE']
            location = blob['VALUE'][0]['VALUE'][1]['VALUE'][0]['VALUE'][0]['VALUE']
            station = blob['VALUE'][0]['VALUE'][2]['VALUE'][0]['VALUE'][0]['VALUE']

        if blob['TYPE'] == 'paragraph':
            text = blob['VALUE'][0]['VALUE']
            text_end = True

        if text_end:
            clean_data.append({
                "time": time,
                "location": location,
                "station": station,
                "text": text
            })

    return clean_data


def read_docx_to_dict(filename):

    # read in a document
    doc = docx.Document(filename)

    # coerce to JSON using the standard options
    docx_as_json = simplify(doc)

    blob_types = [blob['TYPE'] for blob in docx_as_json['VALUE'][0]['VALUE']]

    first_table_index = blob_types.index('table')

    return docx_to_clean_dict(docx_as_json, first_table_index)


def check_text_likeness(df, text, ratio=85, row_name='text'):
    """For a given dataframe (df), loop through the column (row_name),
    calculate the partial ratio between given text (text) and the text in each row,
    and return the indexes where the partial ratio is greater than or equal to the ratio
    """
    matches = df.apply(lambda row: (fuzz.partial_ratio(
        row[row_name], text) >= ratio), axis=1)
    
    return [i for i in matches.index if matches[i]]


def fetch_biggest_text(df, idx_list):
    """For the rows with similar text, fetch the biggest text's index
    """
    biggest_length = 0
    idx = None

    if len(idx_list) == 1:
        return idx_list[0]

    for i in idx_list:
        current_length = len(df['text'][i])
        if current_length > biggest_length:
            biggest_length = current_length
            idx = i
    return idx


def mark_use_row(df):
    # mark rows to use
    idxs = list(df['row_to_use'].unique())

    for index, row in df.iterrows():
        df.at[index, 'use_row'] = index in idxs

    return 'done'


# breakdown text to list of words
# lower, replace special characters
# df['words'] = df['text'].str.lower().str.replace(',', '').str.replace('>', '').str.replace('.', '').str.replace('\n', '').str.replace('’', "'").str.replace(
#     '!', '').str.replace('?', '').str.replace('%', '').str.replace(')', '').str.replace('(', '').str.replace('_', '').str.replace(':', '').str.strip().str.split(' ')


def parse_words(words, use_words=True):
    """Clean list of words"""
    clean_words = []
    
    if use_words:
        climate_change_words = CC_WORDS
    else:
        climate_change_words = CLIMATE_CHANGE_RELATED_WORDS
        
    
    hyphen_climate_words = [
        c for c in climate_change_words if '-' in c]

    for word in words:
        # remove numbers
        if word.isdigit():
            continue

        # clean up hyphenated words
        elif '-' in word:
            # only care about hyphenated climated related words
            if word in climate_change_words:
                clean_words.append(word)

            else:
                word_found = []
                word_indexes = []
                for h in hyphen_climate_words:
                    word_index = word.find(h)

                    if word_index == -1:    # hyphenated climate word not found
                        word_found.append('True')
                    else:       # hyphenated climate word not found
                        word_found.append('False')
                        word_indexes.append({'word': h, 'index': word_index})

                should_split_word = eval(' and '.join(word_found))

                if should_split_word:
                    split_words = word.split('-')
                    clean_words += split_words

                else:
                    idx = word_indexes[0]['index']
                    key = word_indexes[0]['word']
                    clean_words.append(key)

                    leftovers = word[:4] + word[len(key)+idx:]
                    leftover_list = list(filter(None, leftovers.split('-')))
                    clean_words += leftover_list

        else:
            clean_words.append(word)

    return list(filter(None, clean_words))


def fetch_climate_words_in_words(words, use_words=True):
    """Fetches climated related words in a list of words"""
    words_found = []
    
    if use_words:
        climate_change_words = CC_WORDS
    else:
        climate_change_words = CLIMATE_CHANGE_RELATED_WORDS
    
    for word in climate_change_words:
        if word in words:
            words_found.append(word)
    return words_found


def fetch_climate_phrases_in_text(text, use_phrases=True):
    """Fetches climated related phrases in a string of text"""
    phrases_found = []
    
    if use_phrases:
        climate_change_phrases = CC_PHRASES
    else:
        climate_change_phrases = CLIMATE_CHANGE_RELATED_PHRASES
    
    for phrase in climate_change_phrases:
        if phrase in text:
            phrases_found.append(phrase)
    return phrases_found


def words_found_master_list(df_clean_words):
    """Given a column of words, aggregate master list"""
    words_found = list()
    for chunk in df_clean_words:
        words_found += chunk

    return words_found


def master_stopwords_list():
    """Creates a master list of stopwords from pre-existing stopwords found in nltk and wordcloud"""
    stop_words = set(stopwords.words("english"))
    final_stopwords = list(STOPWORDS) + list(stop_words)
    return [i.lower() for i in set(final_stopwords)]


def lemmatize_words(words):
    """Given a list of words, distill to root words"""
    lem = WordNetLemmatizer()

    lemma_list = []
    for word, tag in pos_tag(words):
        wntag = tag[0].lower()
        wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
        if not wntag:
            lemma = word
        else:
            lemma = lem.lemmatize(word, pos=wntag)
        lemma_list.append(lemma)
    return lemma_list


def clean_lemmatized_words(lemma_words):
    """Removes stop words from the lemma list"""
    nonstop_lemma_words = []
    final_stopwords = master_stopwords_list()

    for word in lemma_words:
        if word not in final_stopwords:
            nonstop_lemma_words.append(word)

    return list(filter(None, nonstop_lemma_words))


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
    

from colorama import Back
def highlight_word(word, text):
    highlighted_word = Color.BOLD + Color.RED + Color.UNDERLINE + word + Color.END
    # highlighted_word = Back.CYAN + word + Back.RESET
    
    if word in text:
        return text.replace(word, highlighted_word)
    else:
        return ''
    

def highlighter(climate_words, text):
    if not climate_words:
        return ''
    
    return [highlight_word(word, text) for word in climate_words]
    
# https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
