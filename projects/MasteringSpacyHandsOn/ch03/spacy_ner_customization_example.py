def run_spacy_ner_customization_example():
    import spacy
    from spacy.tokens import Span
    nlp = spacy.load("en_core_web_md")

    example_text = "What customizations I can do for this text that has my YouTube channel name TrainingMyHobby " \
                   "and owner of this channel who is a SolutionArchitect at large enterprises like banks"
    doc = nlp(example_text)
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    print('Before', ents)

    # Create a NER span for the YouTube channel name in the above example text
    # Below are the list of NERs we like to consider in the input text and let Spacy consider them as NER's
    ner_to_look_for = ["TrainingMyHobby", "SolutionArchitect"]

    # Step 1: Iterate through doc and obtain the start and end index of the tokens that matches with the NER's
    # that we need to consider and are delcared in the list ner_to_look_for

    # Iterate through the tokenized input text and if the token text matches with an element in the ner_to_look_for
    # then do the customization of Spacy NER's
    custom_ner_entities = []
    for a_token in doc:
        token_text = a_token.text
        for an_ner in ner_to_look_for:
            if an_ner == token_text:
                print(f"{a_token} a_token.i, {a_token.i} {len(a_token)}")
                custom_ner_entities.append(Span(doc, a_token.i, a_token.i + 1, label="PERSON"))

    if len(custom_ner_entities) > 0:
        doc.set_ents(custom_ner_entities, default="unmodified")

    # Step 2: Now print all the entities that should identify entities configured through the above step customization
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    print('After', ents)


if __name__ == '__main__':
    run_spacy_ner_customization_example()
