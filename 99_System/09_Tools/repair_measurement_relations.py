from pathlib import Path

root = Path(".")

def p(*parts):
    return root.joinpath(*parts)

def read(path):
    return path.read_text()

def write(path, text):
    path.write_text(text)

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

def remove_list(text, field, value):
    end = text.find("\n---", 4)
    front, rest = text[:end], text[end:]
    lines = front.splitlines()
    target = "[[" + value + "]]"
    try:
        i = lines.index(field + ":")
    except ValueError:
        return text
    j = i + 1
    while j < len(lines) and lines[j].startswith("  - "):
        if target in lines[j]:
            lines.pop(j)
            break
        j += 1
    if i + 1 >= len(lines) or not lines[i + 1].startswith("  - "):
        lines.pop(i)
    return "\n".join(lines) + rest

fn_name = "Measure Battery " + "Current"
design_name = "Current Sensing " + "Design"
firmware_name = "Battery Current Acquisition " + "Firmware"
circuit_name = "Battery Current Measurement " + "Circuit"

# Function inverse links.
path = p("30_Product Capabilities","Product Functions",fn_name + ".md")
text = read(path)
text = add_list(text, "realizedBy", design_name)
text = add_list(text, "performedBy", firmware_name)
text = add_list(text, "performedBy", circuit_name)
write(path, text)

# Generic circuit performer.
path = p("20_Product Architecture", circuit_name + ".md")
text = read(path)
text = add_list(text, "performs", fn_name)
write(path, text)

# Shared control dependency inverses.
path = p("20_Product Architecture","Control Circuit.md")
text = read(path)
text = add_list(text, "dependencyOf", firmware_name)
text = add_list(text, "dependencyOf", circuit_name)
write(path, text)

# Product composition inverses.
path = p("10_Products","Battery Accessories","Identification and Charge Interface Devices","PosiCharge PosiGuard.md")
text = read(path)
text = add_list(text, "hasPart", firmware_name)
text = add_list(text, "hasPart", circuit_name)
write(path, text)

# Evidence inverse.
source_name = "Document - PosiCharge PosiGuard Product Page"
path = p("70_Research and Evidence","Source Documents",source_name + ".md")
text = read(path)
text = add_list(text, "supports", design_name)
write(path, text)

# Repair the Hall sensor partial relationship without inventing an assembly.
hall_sensor = "Hall-Effect Current " + "Sensor"
hall_design = "Hall-Effect Current " + "Sensing"
path = p("20_Product Architecture",hall_sensor + ".md")
text = read(path)
text = remove_list(text, "partOf", "Hall-Effect Current Measurement Assembly")
text = add_list(text, "dependencyOf", hall_design)
write(path, text)

path = p("30_Product Capabilities","Product Designs",hall_design + ".md")
text = read(path)
text = add_list(text, "dependsOn", hall_sensor)
write(path, text)
