import wikipedia
import re
import csv

def getText(topic):
    """
    Get the text content from a Wikipedia page on a given topic.

    Args:
        topic (str): The topic for which to retrieve Wikipedia content.

    Returns:
        str: The text content of the Wikipedia page on the specified topic, or None if the topic is not found.
    """
    try:
        page = wikipedia.page(topic)
        content = page.content
        text = re.sub(r'\s+', ' ', content).strip()
        return text
    except:
        return None

def splitTextIntoChunks(text, max_chunk_length):
    """
    Split a long text into smaller chunks based on a maximum chunk length.

    Args:
        text (str): The input text to be split into chunks.
        max_chunk_length (int): The maximum length of each chunk in characters.

    Returns:
        list of str: A list of text chunks, where each chunk is no longer than the specified maximum length.
    """
    chunks = []
    current_chunk = ""

    for sentence in re.split(r'(?<=[.!?])\s+', text):
        if len(current_chunk) + len(sentence) <= max_chunk_length:
            current_chunk += sentence
        else:
            chunks.append(current_chunk)
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

topics = ["cricket", "science", "math", "history", "politics", "agnostic", "nihilism", "cosmos", "quantum computing", "string theory", "chess", "alphazero"]
ans = []
max_chunk_length = 500

for topic in topics:
    text = getText(topic)
    if text:
        chunks = splitTextIntoChunks(text, max_chunk_length)
        ans.extend(chunks)

output_file_path = '../data/humanGenerated.csv'

with open(output_file_path, 'w', newline='') as file:
    """
    Write text chunks to a CSV file.

    Args:
        output_file_path (str): The path to the CSV file where the text chunks will be saved.
    """
    writer = csv.writer(file)
    writer.writerow(["text"])
    for row in ans:
        writer.writerow([row])


# This file is used for generating data from Wikipedia, which is mostly human-generated. 
# Moving forward, our plan is to use the Wayback Machine to access snapshots from the years 2010-2015, as these are likely to contain human-generated content.