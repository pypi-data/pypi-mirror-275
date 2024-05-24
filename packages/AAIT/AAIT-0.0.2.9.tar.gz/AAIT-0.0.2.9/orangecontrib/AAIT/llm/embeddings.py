import copy
from sentence_transformers import SentenceTransformer

from Orange.data import Domain, ContinuousVariable, Table


def create_embeddings(table):
    # Copy input Table
    data = copy.deepcopy(table)
    attr_dom = list(data.domain.attributes)
    metas_dom = list(data.domain.metas)

    # Load embeddings model
    model_path = ""
    model = SentenceTransformer(model_path)

    # Generate embeddings on column "content"
    rows = []
    for i, row in enumerate(data):
        features = list(data[i])
        metas = list(data.metas[i])
        embeddings = model.encode(row["content"].value)
        rows.append(features + embeddings + metas)

    # Generate new domains to add to data
    n_columns = len(embeddings)
    embeddings_dom = [ContinuousVariable(f"embeddings_{i}") for i in range(n_columns)]

    # Create domain and output Table
    domain = Domain(attributes=attr_dom + embeddings_dom, metas=metas_dom)
    out_data = Table.from_list(domain=domain, rows=rows)
    return out_data