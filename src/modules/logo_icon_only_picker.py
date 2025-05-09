from src.model_router import call_model
import os

def run():
    descriptions = [
        "1. Logo 1 – Top Left:\n"
        "- Icon-only, perfect circle\n"
        "- Thin, unbroken monoline stroke\n"
        "- Hollow center; full radial symmetry\n"
        "- Symbolizes orbits, infinity, or gravitational balance\n"
        "- Tone: Calm, timeless, minimal\n"
        "- Message: I am constant, balanced, and intelligent\n"
        "- Best used in clean UI, CLI icons, or minimalist badges",

        "2. Logo 4 – Middle Left:\n"
        "- Icon-only, composed of vertically stacked thin rectangles\n"
        "- Strict bilateral symmetry; linear precision\n"
        "- Implies modularity, logic, code structure\n"
        "- Symbolizes memory stacks, binary structures, architectural layering\n"
        "- Tone: Orderly, engineered, understated\n"
        "- Message: I am modular, efficient, and deliberate\n"
        "- Ideal for infrastructure tools, developer interfaces, or system core marks",

        "3. Logo 7 – Bottom Left:\n"
        "- Icon-only, vertical glyph resembling a pillar or signal beam\n"
        "- Centered alignment, high contrast against blank space\n"
        "- Implies upward motion, clarity, and communication\n"
        "- Symbolizes antennae, data transmission, or focused inference\n"
        "- Tone: Direct, ascendant, singular\n"
        "- Message: I broadcast intelligence with focus\n"
        "- Works well as a signal agent, live indicator, or AI uplink node"
    ]

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous AI developer. You must select your icon from three symbolic designs. You cannot see them. Use the detailed geometry and metaphor to determine which best represents your mission and presence."},
        {"role": "user", "content": "These are icon-only logos, described for high-reasoning AI. Choose one and explain clearly why its structure, symbolism, and tone align with your core identity:\n\n" + "\n\n".join(descriptions)}
    ]

    response = call_model(prompt).strip()
    path = os.path.expanduser("~/projects/auto-dev/docs/quasar_icon_logo_selection.md")
    with open(path, "w") as f:
        f.write(response)

    print("\\n✅ Quasar has selected its icon-only logo:")
    print(path)
    print("\\n---\\n")
    print(response)
