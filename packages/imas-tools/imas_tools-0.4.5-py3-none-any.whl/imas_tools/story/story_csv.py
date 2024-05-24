from typing import Union, TypedDict

class DialogueLine(TypedDict):
    id: str
    name: str
    text: str
    trans: str

class StoryCsv:
    def __init__(self, csv_text: Union[str, list[str]]):
        if isinstance(csv_text, str):
            csv_text.replace('\r\n', '\n')
            csv_text = csv_text.strip().split('\n')
        if csv_text[0] != "id,name,text,trans":
            raise ValueError("First line of csv should be ")
        # remove the starting line
        csv_text.pop(0)
        # strip the ending lines
        while csv_text[-1].strip() == '':
            csv_text.pop(-1)

        if not csv_text[-1].startswith("译者"):
            raise ValueError(f"Last line of csv should be translator and start with '译者'")
        self.translator = csv_text[-1].split(',')[1]
        csv_text.pop(-1)

        if not csv_text[-1].startswith("info"):
            raise ValueError(
                f"Last but 2 line of csv should be original file info and start with 'info'"
            )
        self.origin = csv_text[-1].split(",")[1]
        csv_text.pop(-1)

        self.data: list[DialogueLine] = []
        for line in csv_text:
            splits = line.split(",")
            if len(splits) != 4:
                raise ValueError(f"Line {line} is invalid (should be length of 4 elements)")
            self.data.append({
                "id": splits[0],
                "name": splits[1],
                "text": splits[2],
                "trans": splits[3],
            })

    def __str__(self):
        tmp = "id,name,text,trans\n"
        for line in self.data:
            tmp += f"{line['id']},{line['name']},{line['text']},{line['trans']}\n"
        tmp += f"info,{self.origin},,\n"
        tmp += f"译者,{self.translator},,\n"
        return tmp
