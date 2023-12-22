from __future__ import annotations

from astypes import Type


class FSig:

    def __init__(self, name: str, args: str, return_type: Type, additional_imports):
        self.name = name
        self.args = args
        self.return_type = return_type
        self.imports = set(self.return_type.imports)

        if additional_imports:
            self.imports.update({additional_imports})

    @property
    def annotation(self) -> str:
        return self.return_type.annotation
