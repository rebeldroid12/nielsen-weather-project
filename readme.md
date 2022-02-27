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

## Methodology
First, we gather news articles to answer basic questions surrounding the 3 extreme weather events (what areas were impacted/how, when were the events, how much did the event cost us - lives/financially, etc) to gather information on the events. After this, we read articles comparing climate change and the media to get a sense of what others thought so we had an idea of how to run our analysis.

Marshall Wildfire analysis:
This wildfire was first reported around 11am on Dec 30th so for an initial sample we gathered local news data that was broadcasted between 5-7pm for the DMAs that were not impacted (all DMAs but Denver and Louisville for ABC) and mentioned `fire`.

We grabbed 137 segements - it is important to note that information regarding the anything related to fire can be found here (ex: fire spreading, gun fire, teacher fired, etc.)

First run of data:
I was curious to see what words were coming up as an initial view of the data: word cloud & word frequency

1. Data was pulled into a text file.
2. Used python/pandas/juptyer notebook to clean data
  - remove punctuations
  - removing stopwords (the, city, tonight, etc)
3. Came up with a list of words that felt related to climate change (https://en.wikipedia.org/wiki/Glossary_of_climate_change)

List:
- adaptation
- all-time
- arctic shrinkage
- carbon
- carbon dioxide
- carbon footprint
- carbon offset
- carbon tax
- celsius
- climate
- climate change
- climate crisis
- climate justice
- crisis
- degree
- ecosystem
- energy
- environmental
- extreme weather event
- fossil fuel
- glacial
- global
- global climate
- global cooling
- global warming
- global warming controversy
- global warming denial
- greenhouse
- greenhouse debt
- greenhouse effect
- greenhouse gas
- greenland ice sheet
- historic
- historical temperature record
- history
- ice sheet
- megadrought
- meteorologist
- meteorology
- mitigation
- natural
- nitrous oxide
- ozone
- planet
- policies
- policy
- pollution
- record
- record-breaking
- renewable resource
- report
- reversable
- reverse
- science
- scientist
- sea ice
- sea level
- sea-level
- sea-level rise
- solar
- warm
- warming
4. Ran percents of how often those words came up if at all
- Found that of the words selected for the climate change related words they appear 2.5% of the time. View breakdown below:


