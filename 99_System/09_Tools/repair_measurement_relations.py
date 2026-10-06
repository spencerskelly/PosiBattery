from pathlib import Path

root = Path(".")
fn = root / "30_Product Capabilities" / "Product Functions" / ("Measure Battery " + "Current.md")
text = fn.read_text()

def add_list(text, field, value):
    end = text.find("\n---", 4)
    front, rest = text[:end], text[end:]
    lines = front.splitlines()
    target = "[[" + value + "]]"
    try:
        i = lines.index(field + ":")
    except ValueError:
        lines += [field + ":", '  - "' + target + '"']
        return "\n".join(lines) + rest
    j = i + 1
    while j < len(lines) and lines[j].startswith("  - "):
        if target in lines[j]:
            return text
        j += 1
    lines.insert(j, '  - "' + target + '"')
    return "\n".join(lines) + rest

text = add_list(text, "realizedBy", "Current Sensing " + "Design")
text = add_list(text, "performedBy", "Battery Current Acquisition " + "Firmware")
fn.write_text(text)
