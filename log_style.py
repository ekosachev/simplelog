from color import Color
from modifier import Modifier


class LogStyle(object):
    color: Color
    bg: Color
    modifiers: list[Modifier]

    def __init__(
            self,
            color: Color = Color.white,
            bg: Color | None = None,
            modifiers: list[Modifier] | Modifier | None = None
    ):
        self.color = color
        self.bg = bg

        if modifiers is None:
            self.modifiers = []
        elif modifiers is Modifier:
            self.modifiers = [modifiers]
        else:
            self.modifiers = modifiers

    def _produce_tag(self) -> str:
        if self.bg is not None:
            tag: str = f"{self.color.value} on {self.bg.value}"
        else:
            tag: str = self.color.value
        if self.modifiers:
            tag += f" {' '.join(m for m in self.modifiers)}"

        return tag

    def format(self, text: str) -> str:
        tag: str = self._produce_tag()
        return f"[{tag}]{text}[/{tag}]"
