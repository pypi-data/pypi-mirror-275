from typing import Callable, Optional, Union
from .gakuen_parser import parse_messages, encode_messages
from .story_csv import StoryCsv


def gakuen_txt_to_sc_csv(gakuen_txt: str, txt_name_without_ext: str) -> str:
    parsed = parse_messages(gakuen_txt)
    sc_csv = "id,name,text,trans\n"
    for line in parsed:
        if line["__tag__"] == "message":
            if line.get("text"):
                sc_csv += f"0000000000000,{line.get('name')},{line['text']},\n"
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    sc_csv += f"select,,{choice['text']},\n"
            elif isinstance(line["choices"], dict):
                sc_csv += f"select,,{line['choices']['text']},\n"
            else:
                raise ValueError(f"Unknown choice type: {line['choices']}")
    sc_csv += f"info,{txt_name_without_ext}.txt,,\n"
    sc_csv += f"译者,,,\n"
    return sc_csv


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
    csv_text: Union[str, list[str]], gakuen_txt: str, merger: Callable[[str, str, Optional[str]], str]
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
                line["choices"]["text"] = merger(
                    line["choices"]["text"],
                    next_csv_line["trans"],
                    next_csv_line["text"],
                )
    return encode_messages(parsed)
