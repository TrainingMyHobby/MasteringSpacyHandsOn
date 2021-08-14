def run_spacy_tokenization_customization_example():
    example_text = "I am checking spacy tokenizer customization feature of a text javaprogram"
    import spacy
    from spacy.attrs import ORTH, NORM
    nlp = spacy.load("en_core_web_md")

    special_case = [{ORTH: "java"}, {"ORTH": "program"}]
    nlp.tokenizer.add_special_case("javaprogram", special_case)

    doc = nlp(example_text)
    print([w.text for w in doc])
    print([token for token in doc])


if __name__ == "__main__":
    run_spacy_tokenization_customization_example()
