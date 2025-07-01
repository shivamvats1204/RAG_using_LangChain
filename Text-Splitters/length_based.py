from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Example usage of CharacterTextSplitter
text = """He stood on the crowded train, swaying gently with the rhythm of the city’s pulse. The skyline blurred outside the window, tall and gleaming, but distant—like a life being lived somewhere just out of reach. He was 22 now. Days bled into one another, measured in client meetings, black coffee, and the click of elevator doors. He smiled when expected, nodded politely, laughed at the right cues. But deep inside, there was a silence. A hollow that never quite echoed. He didn’t know what he was searching for. Only that he had been looking for something… or someone… for as long as he could remember. Sometimes he would catch a glimpse—a fleeting scent, a voice in a crowd, a silhouette on the opposite train platform—and his chest would tighten. The feeling would rush in like a forgotten melody. Familiar. Precious. Gone before he could grasp it. He had drawn places he didn’t remember visiting. Climbed hills he felt he’d stood on in another life. He chalked it up to nostalgia, maybe a dream. Maybe a lie his heart told him just to keep beating. But one thing he knew for certain. He was missing something. Or someone."""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)
print(result)
