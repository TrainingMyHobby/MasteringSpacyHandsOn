from pathlib import Path


def run_first_spacy_example():
    import spacy
    from spacy import displacy

    nlp = spacy.load('en_core_web_md')
    doc = nlp("My first Spacy example")
    for a_sent in doc.sents:
        print(f"A sentence {a_sent}")

    # displacy.serve(doc,style="ent")
    render_svg_image = displacy.render(doc,style="dep", jupyter=False)

    Path("/tmp/first_spach_example_render_svg_image.svg").open("w", encoding="utf-8").write(render_svg_image)


if __name__ == '__main__':
    run_first_spacy_example()