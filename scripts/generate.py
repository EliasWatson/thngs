import os
import thngs


TEMPLATE_PATH = "templates"
OUTPUT_PATH = "static"


class Template:
    def __init__(self, template_name: str) -> None:
        self.path: str = os.path.join(TEMPLATE_PATH, f"{template_name}.html")
        self.text: str = ""

        with open(self.path, "r") as file:
            self.text = file.read()

    def generate(self, fields: dict[str, str]) -> str:
        out_text = self.text

        for key, value in fields.items():
            out_text = out_text.replace(f"{{{key}}}", value)

        return out_text


category_template = Template("category")
thing_template = Template("thing")


def generate_thing(thing: thngs.Thing) -> str:
    return ""


def generate_category(category_name: str) -> str:
    print(f"Generating '{category_name}.html'")

    category = thngs.Category(category_name)
    things = [generate_thing(thing) for thing in category.things.values()]

    display_name = (
        category.display_name
        if category.display_name is not None
        else category.short_name
    )

    return category_template.generate(
        {
            "name": display_name,
            "short_name": category.short_name,
            "things": "\n".join(things),
        }
    )


def generate_all_categories() -> list[tuple[str, str]]:
    return [
        (
            os.path.splitext(filename)[0],
            generate_category(os.path.splitext(filename)[0]),
        )
        for filename in os.listdir(thngs.DATA_PATH)
    ]


if __name__ == "__main__":
    generated_categories = generate_all_categories()

