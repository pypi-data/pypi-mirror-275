# Text Summarizer

A Python package for simple local text summarization with nltk.

## Installation

```
pip install local_text_summarizer
```


## Usage

I mostly use this for limiting token upload with expensive LLM API's. So this way I can get the gist of the text and send the condensed version to the API. 

FOR 0.1
IMPORTANT I MADE A SMALL SPELLING MISTAKE WITH THE FIRST VERSION 
TO USE 0.1
from locat_text_summarizer import condense_story
locat NOT local.

THIS HAS BEEN FIXED IN 0.2

Here is a simple example of how to use the `local_text_summarizer` package to condense a story:

```python
from local_text_summarizer import condense_story

text = """
**The Little Boat's Big Adventure**

Once upon a time, in a small marina, there was a little boat named Luna. Luna was a sturdy sailboat with a white hull and a bright blue sail. She had been sitting in the marina for a while, waiting for her next adventure.

One day, a young couple, Alex and Maddie, came to the marina looking for a boat to rent. They had always dreamed of sailing around the world, but for now, they were just looking for a day trip. As they walked down the dock, they noticed Luna, and their eyes lit up. "She's perfect!" Alex exclaimed. Maddie nodded in agreement. "Let's take her out!"

The marina owner, a grizzled old sailor named Jack, helped them prepare Luna for the trip. He showed them the ropes, literally, and gave them a quick sailing lesson. As they set off into the open water, Luna felt the wind in her sail and the sun on her deck. She was finally free!

Alex and Maddie laughed and chatted as they sailed across the bay, taking in the sights and sounds of the ocean. As they approached a small island, they decided to drop anchor and explore. Luna bobbed gently in the water as they swam ashore and discovered a hidden cove, teeming with sea life.

As the day drew to a close, Alex and Maddie reluctantly climbed back on board. As they sailed back to the marina, Luna felt grateful for the adventure she had shared with the young couple. She knew she would always be ready for the next big adventure that came her way.

From that day on, Luna became the go-to boat for many more exciting journeys, and her legend grew as the little boat with a big heart and a love for the open sea.
"""

# Summarize the text
summary = condense_story(text, ratio=0.3)
print("Summary:")
print(summary)

we go from 1622 to 678

**The Little Boat's Big Adventure**
Once upon a time, in a small marina, there was a little boat named Luna. One day, a young couple, Alex and Maddie, came to the marina looking for a boat to rent.



