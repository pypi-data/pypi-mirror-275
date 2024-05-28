import uuid
import json

from crewai_tools import tool

NAMESPACE = None
EMBEDDING_FUNC = None
INDEX = None


def init_toolbox(user_id, embedding_func, pinecone_client, index_name="user-facts-index"):
    global NAMESPACE
    global EMBEDDING_FUNC
    global INDEX
    index = None
    try:
        if index_name not in pinecone_client.list_indexes():
            pinecone_client.create_index(index_name, dimension=1536)  # Adjust dimension based on the model
        index = pinecone_client.Index(index_name)
    except Exception as e:
        print(e)
        pass
    NAMESPACE = user_id
    EMBEDDING_FUNC = embedding_func
    INDEX = index


def init_toolbox_with_gptembeddings(user_id, openai_client, pinecone_client):
    def embed_text_with_openai(text):
        response = openai_client.embeddings.create(
            input=[text],
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    init_toolbox(user_id, embed_text_with_openai, pinecone_client)

@tool("Long memory store")
def store_in_long_term_memory(info_to_store: str) -> str:
    """Storing information in the long term memory that can be retrived later."""
    return _store_in_long_term_memory(info_to_store)


def _store_in_long_term_memory(info_to_store: str) -> str:
    # Generate a unique identifier for the fact (e.g., UUID)
    recrod_id = str(uuid.uuid4())

    info_vector = EMBEDDING_FUNC(info_to_store)

    # Store the info with user ID in the metadata
    INDEX.upsert(vectors=[{
        "id": recrod_id, 
        "values": info_vector, 
        "metadata": {
            "namespace": NAMESPACE,
            "fact": info_to_store
        }
    }])
    return "DONE"


@tool("Long memory query/load")
def query_from_long_term_memory(question: str, count_of_best_responses: int, json_dump=True):
    """Allows to do a query to the long term memory, almost like a query to a Google but this will do query to VectorDB with long term memory."""
    return _query_from_long_term_memory(question, count_of_best_responses, json_dump)


def _query_from_long_term_memory(question: str, count_of_best_responses: int, json_dump=True):
    count = count_of_best_responses
    if count <= 0:
        count = 5
    # Assuming 'query_vector' is the vector representation of your query
    query_vector = EMBEDDING_FUNC(question)

    # Define a filter to only include keys that start with the user's ID
    query_filter = {
        "namespace": NAMESPACE
    }

    # Perform the query
    result = _extract_sorted_facts(INDEX.query(filter=query_filter, top_k=count, vector=query_vector, include_metadata=True))
    if json_dump:
        return json.dumps(result)
    else:
        return result
    

def _extract_sorted_facts(results_dict):
    # Extracting the facts and their scores
    facts_with_scores = [(match['metadata']['fact'], match['score']) for match in results_dict['matches']]

    # Sorting the facts by score in descending order
    sorted_facts = sorted(facts_with_scores, key=lambda x: x[1], reverse=True)

    # Extracting only the facts from the sorted tuples
    sorted_fact_strings = [fact for fact, score in sorted_facts]
    return sorted_fact_strings
