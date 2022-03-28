# Climate change connections to extreme weather events in the media 2021

## Context
We want to know how often connections are being made to climate change whenever an extreme weather event happens.
To do this, we picked 3 events that happened in 2021 as a pilot for our study:
1. Marshall Wildfire in Boulder/Denver, CO (Dec 30, 2021)
2. Heat Wave in Oregon/Washington (June 28, 2021)
3. Hurricane Ida & remnants:
  - hurricane in Louisiana (August 29, 2021)
  - flash flooding in New York/New Jersey (Sept 1, 2021)
  - tornadoes in Maryland, Connecticut, Pennsylvania (Sept 1, 2021)

##  Background
wW gather news articles to answer basic questions surrounding the 3 extreme weather events (what areas were impacted/how, when were the events, how much did the event cost us - lives/financially, etc) to gather information on the events. After this, we read articles comparing climate change and the media to get a sense of what others thought so we had an idea of how to run our analysis.

We decided that we wanted our pilot project to focus on the Marshall Wildfire.

## Methodology
Marshall Wildfire pilot project:
This wildfire was first reported around 11am on Dec 30th 2021. For our pilot project, we gathered data from GrabIX (Nielsen access only) for local news that was broadcasted between 5-7pm for the DMAs that were not impacted (all DMAs but Denver and Louisville for ABC, NBS, CBS and FOX ) that mentioned `fire` in the segment blurb. The logic behind choosing which DMAs to pull data from was that affected DMAs will be in emergency mode and won't really be trying to make connections to climate change. It is important to note that information regarding the anything related to fire can be found here (ex: fire spreading, gun fire, teacher fired, etc.). These segments were pasted into word documents.

Using python via a jupyter notebook, I created CSVs for each local news (ABC, NBS, CBS and FOX) which cleaned up the data and made it into more digestible data. In order to match what words and phrases that were determined climate change related (the list given by meterologists and the one created), the segements were stripped of punctuation, stop words (ex: the, an, a, is), all characters were converted to lowercase, and duplicate text was identified (those that were 85%+ similar).

I also generated word documents that each contain:
- word cloud (just a snapshot of what words are found overall for all of the segments)
- pie chart to compare the count of words to count of climated related words
  - this was done for both my identified climate change words and the given climate change words
- bar chart to show climate change related words frequency
  - this was done for both my identified climate change words and the given climate change words
- list of climate change related words
  - this was done for both my identified climate change words and the given climate change words
- list of climate change related phrases (2 or more words)
  - this was done for both my identified climate change words and the given climate change words
- segments with identified climate change related words highlighted in yellow
  - this was done for both my identified climate change words and the given climate change words

### Misc:
Came up with my list of words that felt related to climate change, words were derived from (https://en.wikipedia.org/wiki/Glossary_of_climate_change)

