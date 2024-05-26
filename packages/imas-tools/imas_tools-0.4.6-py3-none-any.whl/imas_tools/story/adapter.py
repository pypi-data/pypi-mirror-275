from typing import Callable, Optional, Union
from .gakuen_parser import parse_messages, encode_messages
from .story_csv import StoryCsv


def gakuen_txt_to_sc_csv(gakuen_txt: str, txt_name_without_ext: str) -> str:
    parsed = parse_messages(gakuen_txt)
    sc_csv = StoryCsv.new_empty_csv(f"{txt_name_without_ext}.txt")
    for line in parsed:
        if line["__tag__"] == "message":
            if line.get("text") is not None and line.get("name") is not None:
                sc_csv.append_line(
                    {
                        "id": "0000000000000",
                        "name": line.get("name"),
                        "text": line.get("text"),
                        "trans": "",
                    } # type: ignore
                )
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    sc_csv.append_line(
                        {
                            "id": "select",
                            "name": "",
                            "text": choice["text"],
                            "trans": "",
                        }
                    )
            elif isinstance(line["choices"], dict):
                sc_csv.append_line(
                    {
                        "id": "select",
                        "name": "",
                        "text": line["choices"]["text"],
                        "trans": "",
                    }
                )
            else:
                raise ValueError(f"Unknown choice type: {line['choices']}")

    return str(sc_csv)


def trivial_translation_merger(
    original_text: str,
    translated_text: str,
    validation_original_text: Optional[str] = None,
):
    if (
        validation_original_text is not None
        and validation_original_text != original_text
    ):
        raise ValueError(
            f"Original text does not match validation text: {validation_original_text} != {original_text}"
        )
    return translated_text


# eg <r\=はなみさき>花海咲季</r>
def line_level_dual_lang_translation_merger_in(
    original_text: str,
    translated_text: str,
    validation_original_text: Optional[str] = None,
):
    raise NotImplementedError


def merge_translated_csv_into_txt(
    csv_text: Union[str, list[str]],
    gakuen_txt: str,
    merger: Callable[[str, str, Optional[str]], str],
) -> str:
    story_csv = StoryCsv(csv_text)
    parsed = parse_messages(gakuen_txt)
    iterator = iter(story_csv.data)

    for line in parsed:
        if line["__tag__"] == "message":
            if line.get("text"):
                next_csv_line = next(iterator)
                line["text"] = merger(
                    line["text"], next_csv_line["trans"], next_csv_line["text"]
                )
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    next_csv_line = next(iterator)
                    choice["text"] = merger(
                        choice["text"], next_csv_line["trans"], next_csv_line["text"]
                    )
            elif isinstance(line["choices"], dict):
                next_csv_line = next(iterator)
                line["choices"]["text"] = merger(
                    line["choices"]["text"],
                    next_csv_line["trans"],
                    next_csv_line["text"],
                )
    return encode_messages(parsed)
