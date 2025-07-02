from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """He looked down at the sketchpad beside his drink—open to a page filled with landscapes he couldn’t name
Mountain ridges, lakes, a torii gate perched on a cliff
None of it came from memory, and yet none of it was unfamiliar
He had drawn them on instinct, as if his hand remembered what his mind had lost

Lately, he felt like he was always searching. Not for a job, or a direction—he had those, technically—but for something far more elusive
Or… someone
A person whose name he couldn't recall, whose face danced on the edge of memory like a dream just before waking"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(len(chunks))  # Print the number of chunks created
print(chunks)