import re
from typing import Dict, List, Literal
from .colorizer import Color, FontStyle, rgb, basic


def style(format: str, do_not_colorize: bool = False) -> List[str]:
    style_format = re.findall(
        r"(\<\w+\=[,aA-zZ0-9]+\s?\w*\=?[,aA-zZ0-9]*\s?\w*\=?[,aA-zZ0-9]*>)([ aA-zZ0-9!#$%&'*+/=?^_`{|}~.,\-;:()/\\@\"']*)",
        format,
    )
    styled: List[str] = list()
    for style, format in style_format:
        tag = Tag(style, format)
        if do_not_colorize:
            styled.append(tag.text)
            continue
        styled.append(tag.colorized)

    if not style_format:
        raise ValueError(f"Can't parse format string '{format}'")

    return styled


class Tag:
    def __init__(self, tag: str, text: str, *args, **kwargs) -> None:
        def rgb_str2int(text: str, rgb_str: str, target: Literal["font", "background"]):
            color_rgb_str = rgb_str.split(",")
            color_rgb = [int(number) for number in color_rgb_str]
            colored = rgb(
                text,
                *color_rgb,  # type: ignore
                style=getattr(FontStyle, self.style),
                target=target,
            )  # type: ignore
            return colored

        self.values: Dict[str, str] = dict()
        self.text = text
        if tag:
            splitted = tag.split(" ")
            for raw_tag in splitted:
                key_val = raw_tag.split("=")
                key = key_val[0].lstrip("<")
                self.values[key] = key_val[1].rstrip(">")

            self.font_color = self.values.get("font", "white")
            self.bg_color = self.values.get("bg", "")
            self.style = self.values.get("style", "default")

            try:
                font = rgb_str2int(self.text, self.font_color, "font")
            except ValueError:
                font = basic(
                    self.text,
                    getattr(Color, self.font_color),
                    getattr(FontStyle, self.style),
                    target="font",
                )
            if self.bg_color:
                try:
                    self.colorized = rgb_str2int(font, self.bg_color, "background")
                except ValueError:
                    self.colorized = basic(
                        font, getattr(Color, self.bg_color), target="background"
                    )
            else:
                self.colorized = font

    def __str__(self) -> str:
        return self.colorized

    def __repr__(self) -> str:
        _repr = "<"
        for key, val in self.values.items():
            _repr += f"{key}={val} "
        return _repr.rstrip(" ") + ">"
