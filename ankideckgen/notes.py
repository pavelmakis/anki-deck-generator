import logging
from difflib import Differ
from typing import Sequence, Union

from anki.collection import Collection
from anki.models import NotetypeDict
from anki.notes import Note

from ankideckgen.speech import text_to_speech
from config import AUDIO_DIR, DEFAULT_EXAMPLE_AUDIO_SPEED, DEFAULT_WORD_AUDIO_SPEED

differ = Differ()


def _highlight_plural_diff(word: str, plural: str) -> str:
    tag_offset = 0  # offset of the lenght of html tag
    missing_corr = 0  # correction for missing letters

    prev_index_diff = ""
    for index, diff in enumerate(differ.compare(word, plural)):
        if diff[0] != "+":
            if diff[0] == "-":
                missing_corr += 1

            if prev_index_diff == "+":
                plural = (
                    plural[: index - missing_corr + tag_offset]
                    + "</b>"
                    + plural[index - missing_corr + tag_offset :]
                )
                tag_offset += 4
                prev_index_diff = diff[0]
            continue

        if diff[0] == "+":
            if prev_index_diff != "+":
                plural = (
                    plural[: index - missing_corr + tag_offset]
                    + "<b>"
                    + plural[index - missing_corr + tag_offset :]
                )
                prev_index_diff = "+"
                tag_offset += 3
            continue

    if prev_index_diff == "+":
        plural += "</b>"

    return plural


def build_noun_note(
    collection: Collection,
    model: NotetypeDict,
    row: Sequence[str],
) -> Union[Note, None]:
    try:
        _, article, word, plural, tran, example, example_tran, _ = row
    except ValueError:
        logging.error(f"Skipped noun row '{row}'")
        return

    # Generating word sound
    word_sound_filename = AUDIO_DIR / f"{article}{word.lower()}_n.mp3"
    if not word_sound_filename.exists():
        input_str = word
        if article:
            input_str = article + " " + input_str
        if plural:
            input_str = input_str + ", sil<[200]> die " + plural

        text_to_speech(
            text=input_str,
            speed=DEFAULT_WORD_AUDIO_SPEED,
            filename=word_sound_filename,
        )

    word_sound = collection.media.add_file(word_sound_filename)

    # Generating example sound
    example_sound = None
    if example:
        example_sound_filename = AUDIO_DIR / f"{article}{word.lower()}_nex.mp3"
        if not example_sound_filename.exists() and example:
            text_to_speech(
                text=example,
                speed=DEFAULT_EXAMPLE_AUDIO_SPEED,
                filename=example_sound_filename,
            )

        example_sound = collection.media.add_file(example_sound_filename)

    # Adding color to article
    if article == "der":
        article = f'<span style="color: rgb(38, 75, 150);">{article}</span>'
    elif article == "die":
        article = f'<span style="color: rgb(191, 33, 47);">{article}</span>'
    else:
        article = f'<span style="color: rgb(0, 111, 60);">{article}</span>'

    # Marking plural diff with bold
    if plural:
        plural = _highlight_plural_diff(word, plural)

    # Creating note
    note = collection.new_note(notetype=model)
    note.fields = [
        article,
        word,
        # f'<font size="-0.5">die {plural}</font>',
        f"<i>die {plural}</i>" if plural else "",
        f"[sound:{word_sound}]",
        tran,
        f'<font size="-0.5">{example}</font>',
        f"[sound:{example_sound}]" if example_sound else "",
        f'<i><font size="-0.5">{example_tran}</font></i>',
        "",
    ]

    return note


def build_verb_note(
    collection: Collection,
    model: NotetypeDict,
    row: Sequence[str],
) -> Union[Note, None]:
    try:
        _, verb, verbform, tran, example, example_tran, _ = row
    except ValueError:
        logging.error(f"Skipped verb row '{row}'")
        return

    # Generating verb sound
    verb_sound_filename = AUDIO_DIR / f"{verb.lower()}_v.mp3"
    if not verb_sound_filename.exists():
        input_str = verb
        if verbform:
            input_str += ". sil<[300]> " + verbform

        text_to_speech(
            text=input_str,
            speed=DEFAULT_WORD_AUDIO_SPEED,
            filename=verb_sound_filename,
        )

    verb_sound = collection.media.add_file(verb_sound_filename)

    # Generating example sound
    example_sound = None
    if example:
        example_sound_filename = AUDIO_DIR / f"{verb.lower()}_vex.mp3"
        if not example_sound_filename.exists():
            text_to_speech(
                text=example,
                speed=DEFAULT_EXAMPLE_AUDIO_SPEED,
                filename=example_sound_filename,
            )

        example_sound = collection.media.add_file(example_sound_filename)

    # Creating note
    note = collection.new_note(notetype=model)
    note.fields = [
        verb,
        f"<i>{verbform}</i>" if verbform else "",
        f"[sound:{verb_sound}]",
        tran,
        f'<font size="-0.5">{example}</font>',
        f"[sound:{example_sound}]" if example_sound else "",
        f'<i><font size="-0.5">{example_tran}</font></i>',
        "",
    ]

    return note


def build_adjective_note(
    collection: Collection,
    model: NotetypeDict,
    row: Sequence[str],
) -> Union[Note, None]:
    try:
        _, adjective, comparisons, tran, example, example_tran, _ = row
    except ValueError:
        logging.error(f"Skipped adjective row '{row}'")
        return

    # Generating adjective sound
    adj_sound_filename = AUDIO_DIR / f"{adjective.lower()}_a.mp3"
    if not adj_sound_filename.exists():
        input_str = adjective
        if comparisons:
            input_str += ". sil<[300]> " + comparisons

        text_to_speech(
            text=input_str,
            speed=DEFAULT_WORD_AUDIO_SPEED,
            filename=adj_sound_filename,
        )

    adjective_sound = collection.media.add_file(adj_sound_filename)

    # Generating example sound
    example_sound = None
    if example:
        example_sound_filename = AUDIO_DIR / f"{adjective.lower()}_aex.mp3"
        if not example_sound_filename.exists():
            text_to_speech(
                text=example,
                speed=DEFAULT_EXAMPLE_AUDIO_SPEED,
                filename=example_sound_filename,
            )

        example_sound = collection.media.add_file(example_sound_filename)

    # Creating note
    note = collection.new_note(notetype=model)
    note.fields = [
        adjective,
        f"<i>{comparisons}</i>" if comparisons else "",
        f"[sound:{adjective_sound}]",
        tran,
        f'<font size="-0.5">{example}</font>',
        f"[sound:{example_sound}]" if example_sound else "",
        f'<i><font size="-0.5">{example_tran}</font></i>',
        "",
    ]

    return note


def build_word_note(
    collection: Collection,
    model: NotetypeDict,
    row: Sequence[str],
) -> Union[Note, None]:
    try:
        _, word, tran, example, example_tran, _ = row
    except ValueError:
        logging.error(f"Skipped word row '{row}'")
        return

    # Generating word sound
    word_sound_filename = AUDIO_DIR / f"{word.lower()}_w.mp3"
    if not word_sound_filename.exists():
        text_to_speech(
            text=word, speed=DEFAULT_WORD_AUDIO_SPEED, filename=word_sound_filename
        )

    word_sound = collection.media.add_file(word_sound_filename)

    # Generating example sound
    example_sound = None
    if example:
        example_sound_filename = AUDIO_DIR / f"{word.lower()}_wex.mp3"
        if not example_sound_filename.exists():
            text_to_speech(
                text=example,
                speed=DEFAULT_EXAMPLE_AUDIO_SPEED,
                filename=example_sound_filename,
            )

        example_sound = collection.media.add_file(example_sound_filename)

    # Creating note
    note = collection.new_note(notetype=model)
    note.fields = [
        word,
        f"[sound:{word_sound}]",
        tran,
        f'<font size="-0.5">{example}</font>',
        f"[sound:{example_sound}]" if example_sound else None,
        f'<i><font size="-0.5">{example_tran}</font></i>',
        "",
    ]

    return note


def build_phrase_note(
    collection: Collection,
    model: NotetypeDict,
    row: Sequence[str],
) -> Union[Note, None]:
    try:
        _, phrase, tran, _ = row
    except ValueError:
        logging.error(f"Skipped row '{row}'")
        return

    # Generating phrase sound
    phrase_sound_filename = AUDIO_DIR / f"{phrase.strip()[:10].lower()}_ph.mp3"
    if not phrase_sound_filename.exists():
        text_to_speech(
            text=phrase,
            speed=DEFAULT_EXAMPLE_AUDIO_SPEED,
            filename=phrase_sound_filename,
        )

    # Adding generated sounds to collection
    phrase_sound = collection.media.add_file(phrase_sound_filename)

    # Creating note
    note = collection.new_note(notetype=model)
    note.fields = [
        phrase,
        f"[sound:{phrase_sound}]",
        tran,
        "",
    ]

    return note
