from enum import Enum, auto


class Browsers(Enum):
    CHROME = auto()

    @classmethod
    def get_browser(cls, name: str) -> 'Browsers':
        try:
            return cls[name.upper()]
        except KeyError as exc:
            raise KeyError(f"[{name.upper()}] browser isn't supported "
                           f"- choose one of {[browser.name for browser in cls]}") from exc
