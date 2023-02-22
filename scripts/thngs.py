import json
import os


DATA_PATH = "data"


ThingInfoPrimitive = str | int | float
ThingInfo = ThingInfoPrimitive | list[ThingInfoPrimitive]


class Category:
    short_name: str
    display_name: str | None
    description: str | None
    things: dict[str, dict[str, ThingInfo]]

    def __init__(self, short_name: str, *, should_exist=True) -> None:
        self.short_name = short_name
        self.display_name = None
        self.description = None
        self.things = {}

        self._load(should_exist)

    def save(self) -> None:
        raw_data = {}

        if self.display_name is not None:
            raw_data["display_name"] = self.display_name

        if self.description is not None:
            raw_data["description"] = self.description

        raw_data["things"] = self.things

        with open(self._get_path(), "w") as file:
            json.dump(raw_data, file, indent=2)

    def _load(self, should_exist: bool) -> None:
        path = self._get_path()

        if not os.path.exists(path):
            if should_exist:
                raise Exception("Category does not exist")
            return

        with open(path, "r") as file:
            data = json.load(file)

        if "display_name" in data:
            self.display_name = str(data["display_name"])

        if "description" in data:
            self.description = str(data["description"])

        self.things = data["things"]

    def _get_path(self) -> str:
        return os.path.join(DATA_PATH, f"{self.short_name}.json")
