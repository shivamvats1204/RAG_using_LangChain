from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text="""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0,
)

chunks=splitter.split_text(text)
print(len(chunks))  # Print the number of chunks created
print(chunks[0])  # Print the chunks