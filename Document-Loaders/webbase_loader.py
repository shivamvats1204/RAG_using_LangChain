from langchain_community.document_loaders import WebBaseLoader

url="https://shivamvats.netlify.app/"
loader = WebBaseLoader(url)

docs = loader.load()
print(len(docs))
print("\n Website's content is:", docs[0].page_content, sep="\n")

