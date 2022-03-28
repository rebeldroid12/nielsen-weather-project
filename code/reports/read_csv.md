# How to read generated CSVs:

### Data:
The Marshall Fire happened on December 30th 2021 near Denver, CO. Data was collected by GrabIX with search word `fire` for 2021-12-30 between 5 and 7pm for the major local news stations -- CBS, ABC, NBC and FOX. Using Python, various data science libraries (including Pandas) and a Jupyter notebook 4 CSVs were generated for each local news station (`CBS.csv`, `ABC.csv`, `NBC.csv` and `FOX.csv`) and each has the following columns:

- time: timestamp of segment capture
- location: location of segment airing
- station: station that aired the segment
- text: segment snippet
- dup: True if text in row matches 100% with another another row's text, False is not 100% match
- matches: Using the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) found in [TheFuzz](https://github.com/seatgeek/thefuzz) library, list the rows of text that have a match greater than or equal to 85% to the row's text
- row_to_use: the row to use -- calculate which row to use given a text's uniqueness or if multiple matches find the longest text
- words: text broken up into a list of words
- cc_clean_words: a clean list of words similar to `words` column however this is cleaning up hyphenated words that can be found in the given list of climate change words (if it's not a hyphenated word found in the list of climate change words then break up the hyphenated word into individual words)
- my_clean_words: a clean list of words similar to `words` column however this is cleaning up hyphenated words that can be found in my generated list of climate change words (if it's not a hyphenated word found in my list of climate change words then break up the hyphenated word into individual words)
- cc_climate_words_found: list of words found in the text that match the given list of climate change single words
- my_climate_words_found: list of words found in the text that match my list of climate change single words
- cc_climate_phrases_found: list of phrases found in the text that match the given list of climate change phrases
- my_climate_phrases_found: list of phrases found in the text that match my list of climate change phrases


### Notes:
- Rows are in no particular order

