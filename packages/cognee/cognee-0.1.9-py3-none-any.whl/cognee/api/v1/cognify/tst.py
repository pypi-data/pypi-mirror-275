# from cognee.shared.data_models import GraphDBType
#
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# import asyncio
# from cognee.shared.data_models import KnowledgeGraph, DefaultCognitiveLayer, TextContent, TextSubclass, DefaultContentPrediction
# from cognee.modules.cognify.llm.generate_graph import generate_graph
#
# required_layers_one = DefaultContentPrediction(
#     label=TextContent(
#         type='TEXT',
#         subclass=[TextSubclass.ARTICLES]
#     )
# )
#
# print(required_layers_one.dict())
#
#
# #
# #
# #
# # if __name__ == "__main__":
# #     async def main():
# #         logging.info("Hello")
# #         from cognee.infrastructure.databases.graph.get_graph_client import get_graph_client
# #
# #         client = await get_graph_client(graph_type=GraphDBType.NEO4J)
# #
# #         print(client)
# #
# #         await client.add_node("1", name="Alice")
# #
# #
# #         from cognee.utils import render_graph
# #         # graph_url = await render_graph(graph)
# #         # print(graph_url)
# #
# #
# #     asyncio.run(main())
import duckdb
# import networkx as nx
#
# # Create a new graph
# G = nx.Graph()
#
# # Add some nodes to the graph
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
#
# # Node ID you're looking for
# node_id = 2
#
# # Check if the node exists in the graph
# if G.has_node(node_id):
#     print(f"Node with ID {node_id} exists in the graph.")
# else:
#     print(f"Node with ID {node_id} does not exist in the graph.")

from nltk.parse.generate import generate, demo_grammar

from cognee.infrastructure import infrastructure_config

# from nltk import CFG
# grammar = CFG.fromstring("Utilizes the quantum superposition.")
# print(grammar)
# import nltk
# from nltk import CFG
# from nltk.tokenize import word_tokenize
# from nltk.parse import RecursiveDescentParser
#
# nltk.download('wordnet')
# from nltk.corpus import wordnet as wn
#
# # Define a CFG with parts of speech tags and catch-all rules for unknown words
# grammar = CFG.fromstring("""
#   S -> NP VP
#   NP -> Det N | Det N PP | N
#   VP -> V | V NP | V NP PP | V Adv
#   PP -> P NP
#   Det -> 'a' | 'the'
#   N -> 'dog' | 'park' | UNKNOWN_NOUN
#   V -> 'saw' | 'walked' | UNKNOWN_VERB
#   P -> 'in' | 'on'
#   Adv -> 'quickly' | UNKNOWN_ADV
#   """)
#
# # Initialize a recursive descent parser with the grammar
# parser = RecursiveDescentParser(grammar)
#
# def get_wordnet_pos(treebank_tag):
#     """Converts treebank POS tags to WordNet POS tags."""
#     if treebank_tag.startswith('J'):
#         return wn.ADJ
#     elif treebank_tag.startswith('V'):
#         return wn.VERB
#     elif treebank_tag.startswith('N'):
#         return wn.NOUN
#     elif treebank_tag.startswith('R'):
#         return wn.ADV
#     else:
#         return None
#
# def get_unknown_pos(word):
#     """Finds the most likely POS tag for an unknown word using WordNet."""
#     synsets = wn.synsets(word)
#     if not synsets:
#         return 'UNKNOWN_NOUN'  # Default to NOUN if word not found
#     pos_counts = [get_wordnet_pos(s.pos()) for s in synsets]
#     most_common_pos = max(set(pos_counts), key=pos_counts.count)
#     if most_common_pos == wn.NOUN:
#         return 'UNKNOWN_NOUN'
#     elif most_common_pos == wn.VERB:
#         return 'UNKNOWN_VERB'
#     elif most_common_pos == wn.ADJ:
#         return 'UNKNOWN_ADJ'
#     elif most_common_pos == wn.ADV:
#         return 'UNKNOWN_ADV'
#     else:
#         return 'UNKNOWN_NOUN'
#
# def preprocess_sentence(sentence, original_grammar):
#     """Dynamically adjusts the grammar for unknown words in the sentence."""
#     tokens = word_tokenize(sentence)
#     new_productions = original_grammar.productions()
#
#     for word in tokens:
#         if not any(word in str(prod) for prod in original_grammar.productions()):
#             unknown_pos = get_unknown_pos(word)
#             # Create a new production for the unknown word and add it to the list of productions
#             new_production = CFG.fromstring(f"{unknown_pos} -> '{word}'").productions()[0]
#             new_productions.append(new_production)
#
#     # Create a new grammar with the adjusted set of productions
#     adjusted_grammar = CFG(original_grammar.start(), new_productions)
#     return tokens, adjusted_grammar
#
#
# # Example sentence
# sentence = "Alice utilizes quantum superposition"
#
# # Preprocess the sentence and adjust the grammar for unknown words
# tokens, adjusted_grammar = preprocess_sentence(sentence, grammar)
#
# print(tokens)
# print(adjusted_grammar)

# Parse the preprocessed sentence using the adjusted grammar
# parser = RecursiveDescentParser(adjusted_grammar)
#
# for tree in parser.parse(tokens):
#     print(tree)
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# from nltk.chunk import ne_chunk
#
# # Ensure that the necessary NLTK resources are downloaded
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
#
# # The sentence you want to tag and recognize entities in
# sentence = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California."
#
# # Tokenize the sentence into words
# tokens = word_tokenize(sentence)
#
# # Perform POS tagging on the tokenized sentence
# tagged = pos_tag(tokens)
# print(tagged)
#
# # Perform Named Entity Recognition (NER) on the tagged tokens
# entities = ne_chunk(tagged)
#
# # Print the named entities
# print(entities)
#
# # Alternatively, to display the entities more clearly, you can use:
# entities.pprint()
#
# infra_config = infrastructure_config.get_config()
# # db = duckdb.connect(infra_config["database_path"])
#
# db_engine = infra_config["database_engine"]
#
# data = [
#     {
#         'document_id': 'doc1',
#         'layer_id': 'layer1',
#         'created_at': '2022-01-01 00:00:00',
#         'updated_at': '2022-01-01 00:00:00'
#     },
#     {
#         'document_id': 'doc2',
#         'layer_id': 'layer2',
#         'created_at': '2022-01-02 00:00:00',
#         'updated_at': '2022-01-02 00:00:00'
#     }
# ]
#
# # Call the load_cognify_data method
# db_engine.load_cognify_data(data)
#
# # Call the get_cognify_data method and print the results
# cognify_data = db_engine.get_cognify_data()
# print(cognify_data)



import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes with parameters as dictionaries
G.add_node(1, params={'color': 'red', 'size': 10, 'nested_params': {'shape': 'circle', 'opacity': 0.5}})
G.add_node(2, params={'color': 'blue', 'size': 15})
G.add_node(3, params={'color': 'green', 'size': 20})

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)

# Print nodes with parameters
for node, params in G.nodes(data='params'):
    print("Node:", node)
    print("Parameters:", params)

# Print edges
print("Edges:", G.edges())


