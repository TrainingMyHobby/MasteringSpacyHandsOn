from spacy import Language


def text_tokenization(input_text: str, spacy_nlp_obj: Language) -> any:
    spacy_doc = spacy_nlp_obj(input_text)
    print([token.text for token in spacy_doc])


def run_spacy_core_features_example():
    example_text = "This is my second spacy example for learning spacy core features"

    import spacy
    nlp = spacy.load('en_core_web_md')
    text_tokenization(example_text, nlp)


if __name__ == '__main__':
    run_spacy_core_features_example()
