import os
import networkx as nx
import pandas as pd

import cellmaps_ppi_embedding
from cellmaps_ppi_embedding.runner import Node2VecEmbeddingGenerator, EmbeddingGenerator
from cellmaps_ppi_embedding.runner import CellMapsPPIEmbedder


input_base_path = "data/raw"
embedding_base_path = "data/embedding"
input_path = os.path.join(input_base_path, "apms.tsv")


df = pd.read_csv(os.path.join(input_base_path, "apms.tsv"), sep='\t')
nx_graph = nx.from_pandas_edgelist(df, source = 'Bait', target = 'Prey')
gen = Node2VecEmbeddingGenerator(nx_network = nx_graph)

embedder = CellMapsPPIEmbedder(
    outdir=embedding_base_path,
    inputdir=input_base_path,
    embedding_generator=gen,
    name=f"AP-MS Embedding",
    organization_name="CM4AI",
    project_name="CM4AI AP-MS Embedding Tutorial"
)
embedder.run()
