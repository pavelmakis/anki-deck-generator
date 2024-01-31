from anki.models import ModelManager, NotetypeDict


def create_noun_notetype(manager: ModelManager) -> NotetypeDict:
    """Creates notetype (model) for noun with templates"""

    noun = manager.new(name="Substantiv (reversed)")

    # Notes will be sorted by second field (Substantiv)
    noun["sortf"] = 1

    # Adding card fields
    manager.add_field(notetype=noun, field=manager.new_field("Artikel"))
    manager.add_field(notetype=noun, field=manager.new_field("Substantiv"))
    manager.add_field(notetype=noun, field=manager.new_field("Plural"))
    manager.add_field(notetype=noun, field=manager.new_field("Audio"))
    manager.add_field(notetype=noun, field=manager.new_field("Übersetzung"))
    manager.add_field(notetype=noun, field=manager.new_field("Beispiel"))
    manager.add_field(notetype=noun, field=manager.new_field("Audio des Beispiels"))
    manager.add_field(
        notetype=noun, field=manager.new_field("Übersetzung des Beispiels")
    )
    manager.add_field(notetype=noun, field=manager.new_field("Kommentar"))

    # Adding card templates
    card_1 = manager.new_template(name="de -> ru")
    card_1["qfmt"] = "{{Artikel}} {{Substantiv}}<br>{{Plural}}<br>{{Audio}}"
    card_1["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Übersetzung}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_2 = manager.new_template(name="ru -> de")
    card_2["qfmt"] = "{{Übersetzung}}"
    card_2["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Artikel}} {{Substantiv}}<br>"
        "{{Plural}}<br>"
        "{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_3 = manager.new_template(name="ru -> de (with typing)")
    card_3["qfmt"] = "{{Übersetzung}}<br><br>{{type:Substantiv}}"
    card_3["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Artikel}} {{Substantiv}}<br>"
        "{{Plural}}<br>"
        "{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    manager.add_template(notetype=noun, template=card_1)
    manager.add_template(notetype=noun, template=card_2)
    manager.add_template(notetype=noun, template=card_3)

    manager.save(notetype=noun)

    return noun


def create_verb_notetype(manager: ModelManager) -> NotetypeDict:
    """Creates notetype (model) for verb with templates"""

    verb = manager.new(name="Verb (reversed)")

    # Adding card fields
    manager.add_field(notetype=verb, field=manager.new_field("Verb"))
    manager.add_field(notetype=verb, field=manager.new_field("Verbformen"))
    manager.add_field(notetype=verb, field=manager.new_field("Audio"))
    manager.add_field(notetype=verb, field=manager.new_field("Übersetzung"))
    manager.add_field(notetype=verb, field=manager.new_field("Beispiel"))
    manager.add_field(notetype=verb, field=manager.new_field("Audio des Beispiels"))
    manager.add_field(
        notetype=verb, field=manager.new_field("Übersetzung des Beispiels")
    )
    manager.add_field(notetype=verb, field=manager.new_field("Kommentar"))

    # Adding card templates
    card_1 = manager.new_template(name="de -> ru")
    card_1["qfmt"] = "{{Verb}}<br>{{Verbformen}}<br>{{Audio}}"
    card_1["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Übersetzung}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_2 = manager.new_template(name="ru -> de")
    card_2["qfmt"] = "{{Übersetzung}}"
    card_2["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Verb}}<br>{{Verbformen}}<br>{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_3 = manager.new_template(name="ru -> de (with typing)")
    card_3["qfmt"] = "{{Übersetzung}}<br><br>{{type:Verb}}"
    card_3["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Verb}}<br>{{Verbformen}}<br>{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    manager.add_template(notetype=verb, template=card_1)
    manager.add_template(notetype=verb, template=card_2)
    manager.add_template(notetype=verb, template=card_3)

    manager.save(notetype=verb)

    return verb


def create_adjective_notetype(manager: ModelManager) -> NotetypeDict:
    """Creates notetype (model) for adjective with templates"""

    adjective = manager.new(name="Adjektiv (reversed)")

    # Adding card fields
    manager.add_field(notetype=adjective, field=manager.new_field("Adjektiv"))
    manager.add_field(
        notetype=adjective, field=manager.new_field("Steigerung der Adjektive")
    )
    manager.add_field(notetype=adjective, field=manager.new_field("Audio"))
    manager.add_field(notetype=adjective, field=manager.new_field("Übersetzung"))
    manager.add_field(notetype=adjective, field=manager.new_field("Beispiel"))
    manager.add_field(
        notetype=adjective, field=manager.new_field("Audio des Beispiels")
    )
    manager.add_field(
        notetype=adjective, field=manager.new_field("Übersetzung des Beispiels")
    )
    manager.add_field(notetype=adjective, field=manager.new_field("Kommentar"))

    # Adding card templates
    card_1 = manager.new_template(name="de -> ru")
    card_1["qfmt"] = "{{Adjektiv}}<br>{{Steigerung der Adjektive}}<br>{{Audio}}"
    card_1["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Übersetzung}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_2 = manager.new_template(name="ru -> de")
    card_2["qfmt"] = "{{Übersetzung}}"
    card_2["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Adjektiv}}<br>{{Steigerung der Adjektive}}<br>"
        "{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_3 = manager.new_template(name="ru -> de (with typing)")
    card_3["qfmt"] = "{{Übersetzung}}<br><br>{{type:Adjektiv}}"
    card_3["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Adjektiv}}<br>{{Steigerung der Adjektive}}<br>"
        "{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    manager.add_template(notetype=adjective, template=card_1)
    manager.add_template(notetype=adjective, template=card_2)
    manager.add_template(notetype=adjective, template=card_3)

    manager.save(notetype=adjective)

    return adjective


def create_word_notetype(manager: ModelManager) -> NotetypeDict:
    """Creates notetype (model) for any other word with templates.

    This model is used for words with basic 'word' and 'translation' fileds."""

    word = manager.new(name="Wort (reversed)")

    # Adding card fields
    manager.add_field(notetype=word, field=manager.new_field("Wort"))
    manager.add_field(notetype=word, field=manager.new_field("Audio"))
    manager.add_field(notetype=word, field=manager.new_field("Übersetzung"))
    manager.add_field(notetype=word, field=manager.new_field("Beispiel"))
    manager.add_field(notetype=word, field=manager.new_field("Audio des Beispiels"))
    manager.add_field(
        notetype=word, field=manager.new_field("Übersetzung des Beispiels")
    )
    manager.add_field(notetype=word, field=manager.new_field("Kommentar"))

    # Adding card templates
    card_1 = manager.new_template(name="de -> ru")
    card_1["qfmt"] = "{{Wort}}<br>{{Audio}}"
    card_1["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Übersetzung}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_2 = manager.new_template(name="ru -> de")
    card_2["qfmt"] = "{{Übersetzung}}"
    card_2["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Wort}}<br>{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    card_3 = manager.new_template(name="ru -> de (with typing)")
    card_3["qfmt"] = "{{Übersetzung}}<br><br>{{type:Wort}}"
    card_3["afmt"] = (
        "{{FrontSide}}<hr id=answer>"
        "{{Wort}}<br>{{Audio}}<br><br><br>"
        "{{Beispiel}}<br>"
        "{{Übersetzung des Beispiels}}<br>"
        "{{Audio des Beispiels}}<br><br>"
        "{{Kommentar}}"
    )

    manager.add_template(notetype=word, template=card_1)
    manager.add_template(notetype=word, template=card_2)
    manager.add_template(notetype=word, template=card_3)

    manager.save(notetype=word)

    return word


def create_phrase_notetype(manager: ModelManager) -> NotetypeDict:
    phrase = manager.new("Phrase (reversed)")

    # Adding card fields
    manager.add_field(notetype=phrase, field=manager.new_field("Phrase"))
    manager.add_field(notetype=phrase, field=manager.new_field("Audio"))
    manager.add_field(notetype=phrase, field=manager.new_field("Übersetzung"))
    manager.add_field(notetype=phrase, field=manager.new_field("Kommentar"))

    # Adding card templates
    card_1 = manager.new_template(name="de -> ru")
    card_1["qfmt"] = "{{Phrase}}<br>{{Audio}}"
    card_1["afmt"] = "{{FrontSide}}<hr id=answer>{{Übersetzung}}<br><br>{{Kommentar}}"

    card_2 = manager.new_template(name="ru -> de")
    card_2["qfmt"] = "{{Übersetzung}}"
    card_2[
        "afmt"
    ] = "{{FrontSide}}<hr id=answer>{{Phrase}}<br>{{Audio}}<br><br>{{Kommentar}}"

    manager.add_template(notetype=phrase, template=card_1)
    manager.add_template(notetype=phrase, template=card_2)

    manager.save(notetype=phrase)

    return phrase
