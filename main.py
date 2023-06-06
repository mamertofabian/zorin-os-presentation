import tiktoken


def init_env_vars():
    from dotenv import load_dotenv
    load_dotenv()


if __name__ == '__main__':
    init_env_vars()


def estimate_token_cost(docs):
    enc = tiktoken.encoding_for_model("gpt-4")

    total_word_count = sum(len(doc.page_content.split()) for doc in docs)
    total_token_count = sum(len(enc.encode(doc.page_content)) for doc in docs)
    est_cost = total_token_count * 0.0004 / 1000

    # print(f"\nTotal word count: {total_word_count}")
    # print(f"Estimated tokens: {total_token_count}")
    # print(f"Estimated cost of embedding: ${est_cost}\n")

    return total_word_count, total_token_count, est_cost
