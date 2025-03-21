from typing import Optional

import solara
from solara.alias import rv


@solara.component
def Counter(
    text: str,
    value: solara.Reactive[int] | int,
    max_value: Optional[int] = None
):

    with solara.Card(elevation=0):
        count_text = str(value) if max_value is None else f"{value} / {max_value}"
        solara.Text(f"{text}: ")
        solara.Text(f"{count_text}", classes=["StudentResponses", "ml-1"])
