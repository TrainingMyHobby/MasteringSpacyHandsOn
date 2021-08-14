
def run_spacy_pos_example():
    import spacy
    nlp = spacy.load("en_core_web_md")

    example_text = "I am learning Spacy Part of Speech feature with my hands-on examples"
    doc = nlp(example_text)

    for a_token in doc:
        print(f"[TOKEN IS {a_token} ]")
        print(f"POS explanation -> {spacy.explain(a_token.pos_)}")
        print(f"TAG explanation -> {spacy.explain(a_token.tag_)}")


if __name__ == '__main__':
    run_spacy_pos_example()
