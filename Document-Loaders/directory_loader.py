from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="./sample_dir",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

# uncomment the following lines to use the loader (eager loading)
# docs = loader.load()
# for document in docs:
#     print(document.metadata)
# print("\n The last document content is:", document.page_content, sep="\n")


# following lines for lazy loading
docs = loader.lazy_load()
for document in docs:
    print(document.metadata)
print("\n The last document content is:", document.page_content, sep="\n")