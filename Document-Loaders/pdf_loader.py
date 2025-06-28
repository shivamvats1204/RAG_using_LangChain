from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
docs=loader.load()

print("No. of pages are: ",len(docs))

print("\nPage 1 content is:",docs[1].page_content,sep="\n")

print("\nPage 1 metadata is:",docs[1].metadata,sep="\n")
