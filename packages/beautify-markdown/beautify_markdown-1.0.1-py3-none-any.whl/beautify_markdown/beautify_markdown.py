from rich import traceback
from rich.console import Console
from rich.prompt import Prompt
import pyperclip

traceback.install()

console = Console()


def beautify_markdown(md_to_beautify):
    md_beautified = md_to_beautify
    md_beautified = md_beautified.replace(r"\n\n", "\n\n")
    md_beautified = md_beautified.replace(r"```bash\n", "```bash\n    ")
    md_beautified = md_beautified.replace(r"```bash\n    ```", "```bash\n```")
    md_beautified = md_beautified.replace(r"\n- ", "\n**")
    md_beautified = md_beautified.replace(r"**: ", "**: ")
    md_beautified = md_beautified.replace(r"\n- **", "\n\n**")
    return md_beautified


def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)


def main():
    filename = Prompt.ask(
        "Enter the full path to the markdown file you want to output",
        default="README.md",
    )

    console.log(
        "Copy the contents you want to beautify to the clipboard and then press enter"
    )
    Prompt.ask("Press enter when you have copied the contents")

    md_to_beautify = pyperclip.paste()

    beautified_md = beautify_markdown(md_to_beautify)
    save_to_file(beautified_md, filename)

    console.log(f"Beautified markdown has been saved to {filename}")


if __name__ == "__main__":
    main()
