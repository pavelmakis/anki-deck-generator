from csv import reader

import click
from anki.collection import Collection
from anki.exporting import AnkiPackageExporter
from speechkit import configure_credentials, creds

from ankideckgen.notes import (
    build_adjective_note,
    build_noun_note,
    build_phrase_note,
    build_verb_note,
    build_word_note,
)
from ankideckgen.notetypes import (
    create_adjective_notetype,
    create_noun_notetype,
    create_phrase_notetype,
    create_verb_notetype,
    create_word_notetype,
)
from config import BASE_DIR, YANDEX_API_KEY


def _clean_deck(collection: Collection) -> None:
    # Removing all models (notetypes)
    collection.models.remove_all_notetypes()

    # Removing all decks
    deck_ids = (i["id"] for i in collection.decks.all())
    collection.decks.remove(deck_ids)


@click.command()
@click.argument("input_collection_path", type=click.Path(exists=True))
@click.argument("words_csv_path", type=click.Path(exists=True))
@click.option(
    "-n",
    "--name",
    "deck_name",
    required=True,
    type=str,
    help="Name of the created deck in collection",
)
@click.option(
    "-o",
    "--output",
    "output",
    default="output",
    help="Filename to export new Anki collection to",
)
def build_deck(
    input_collection_path: str,
    words_csv_path: str,
    deck_name: str,
    output: str,
) -> None:
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(api_key=YANDEX_API_KEY)
    )

    # Openning collection and cleaning it
    collection = Collection(input_collection_path)
    _clean_deck(collection=collection)

    # Creating new deck
    deck = collection.decks.add_normal_deck_with_name(name=deck_name)
    deck = collection.decks.get(did=deck.id)

    # Creating models (note types)
    noun_model = create_noun_notetype(manager=collection.models)
    verb_model = create_verb_notetype(manager=collection.models)
    adjective_model = create_adjective_notetype(manager=collection.models)
    word_model = create_word_notetype(manager=collection.models)
    phrase_model = create_phrase_notetype(manager=collection.models)

    with open(words_csv_path) as words_csv:
        file_reader = reader(words_csv, delimiter=";")
        for row in file_reader:
            if len(row) <= 1:
                continue
            elif row[0] == "noun":
                note = build_noun_note(
                    collection=collection,
                    model=noun_model,
                    row=row,
                )
            elif row[0] == "verb":
                note = build_verb_note(
                    collection=collection,
                    model=verb_model,
                    row=row,
                )
            elif row[0] == "adjective":
                note = build_adjective_note(
                    collection=collection,
                    model=adjective_model,
                    row=row,
                )
            elif row[0] == "word":
                note = build_word_note(
                    collection=collection,
                    model=word_model,
                    row=row,
                )
            elif row[0] == "phrase":
                note = build_phrase_note(
                    collection=collection,
                    model=phrase_model,
                    row=row,
                )

            if note is not None:
                collection.add_note(note=note, deck_id=deck["id"])

    # Exporting to Anki package
    exporter = AnkiPackageExporter(col=collection)
    exporter.exportInto(f"{BASE_DIR}/{output}.apkg")


if __name__ == "__main__":
    build_deck()
