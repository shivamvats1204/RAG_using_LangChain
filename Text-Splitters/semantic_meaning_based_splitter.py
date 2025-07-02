from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

# uncomment the following lines to use OpenAI embeddings 
# splitter = SemanticChunker(
#     OpenAIEmbeddings(),
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=1
# )


# using huggingface embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.45
)

text = """
The sun rose over the mountains, painting the sky in hues of orange and gold. Quantum computing is poised to revolutionize encryption by making classical cryptography obsolete. In ancient mythology, the phoenix symbolizes rebirth, emerging from ashes stronger than before. Global markets reacted sharply to the unexpected shift in interest rates announced this morning.

Meanwhile, in fields like healthcare and finance, AI is being used to analyze complex datasets and provide insights that would take humans much longer to derive. Machine learning models can now predict patient diagnoses, automate fraud detection, and even assist in drug discovery. Yet these advancements also raise concerns—about data privacy, bias in decision-making algorithms, and over-reliance on automated systems.
"""

docs = splitter.create_documents([text]) # Create documents from the text
print(len(docs))  # Print the number of documents created
print(docs)  # Print the content of the first document