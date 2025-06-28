from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="./sample_dir",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

docs = loader.load()

print("No. of documents loaded:", len(docs))

print("\nLast document content is:", docs[-1].page_content, sep="\n")