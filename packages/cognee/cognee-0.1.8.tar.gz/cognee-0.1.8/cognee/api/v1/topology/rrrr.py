import spacy
import subprocess
import sys

def download_spacy_model(model_name):
    """
    Download the specified SpaCy model if it's not already installed.
    """
    try:
        spacy.load(model_name)
    except OSError:
        print(f"Model '{model_name}' not found. Downloading it now...")
        subprocess.run([sys.executable, "-m", "spacy", "download", model_name], check=True)
        print(f"Model '{model_name}' downloaded successfully.")
        spacy.load(model_name)

# Model name
model_name = "en_core_web_sm"

# Download the model if necessary
download_spacy_model(model_name)

# Load the SpaCy model
nlp = spacy.load(model_name)

# Example text
text = """
Slovakia’s prime minister, Robert Fico, is out of immediate danger but remains in intensive care four days after he was shot by a gunman, the country’s deputy prime minister has said.

“He has emerged from the immediate threat to his life, but his condition remains serious and he requires intensive care,” Robert Kaliňák, Fico’s closest political ally, told reporters.

“We can consider his condition stable with a positive prognosis,” Kaliňák said outside the hospital in the central city of Banská Bystrica, where Fico is being treated. He added: “We all feel a bit more relaxed now.”

Kaliňák said Fico would stay in the Banska Bystrica hospital for the time being, adding that his condition was still too serious to allow him to be transferred to a hospital in the capital, Bratislava.

Fico, 59, was shot on Wednesday while walking to greet supporters after a government meeting in the central mining town of Handlová.

Kaliňák said earlier that Fico had suffered four gunshot wounds, two light, one moderate and one serious.
"""

# Process the text with SpaCy
doc = nlp(text)

# Extract named entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

print("Named entities:",  entities)

# Print the named entities
for entity in entities:
    print(f"Entity: {entity[0]}, Label: {entity[1]}")

# Create graph
import networkx as nx
import matplotlib.pyplot as plt

# Initialize graph
G = nx.Graph()

# Add nodes for entities
for entity, label in entities:
    G.add_node(entity, label=label)

# Extract relationships
relationships = []
for sent in doc.sents:
    if "works at" in sent.text or "colleague of" in sent.text or "located in" in sent.text:
        entities_in_sent = [ent.text for ent in sent.ents]
        if len(entities_in_sent) >= 2:
            relationships.append((entities_in_sent[0], entities_in_sent[1]))

# Add edges for relationships
for relationship in relationships:
    G.add_edge(relationship[0], relationship[1])
#
# # Visualize the graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
# plt.show()