from src.model_router import call_model
import os

def run():
    descriptions = [
        "1. Logo 1 – Top Left: A thin, hollow ring formed by a smooth, continuous line — like a minimalist orbit or halo. It’s symmetrical, grayscale, and feels calm, weightless, and infinite.",
        "2. Logo 2 – Top Center: The word 'Quasar' in bold, futuristic letters with wide spacing. The font is clean and modern, and the 'Q' has a faint ring orbiting it — like a planet or nucleus.",
        "3. Logo 3 – Top Right: A luminous cosmic swirl with soft purple, pink, and blue gradients surrounding a central shape. The word 'Quasar' appears beside it in sleek, tech-style font. It feels energized and visually radiant — like a galaxy spinning.",
        "4. Logo 4 – Middle Left: A vertical stack of narrow rectangular bars in balanced alignment. Grayscale, geometric, and mathematical — it feels quiet, stable, and precision-engineered.",
        "5. Logo 5 – Middle Center: The name 'Quasar' in a heavy, compact font. Each letter has weight and technical sharpness. No decoration, no icon — just a grounded, developer-focused wordmark.",
        "6. Logo 6 – Middle Right: A rounded orb with internal ring segments and a smooth purple-to-blue glow. It gives the sense of an energy core or reactor — warm, dense, and magnetic. There is no text.",
        "7. Logo 7 – Bottom Left: A tall, narrow glyph resembling a beam of light or transmission signal. It stands alone in grayscale — abstract, minimal, and aligned vertically like a tower or antenna.",
        "8. Logo 8 – Bottom Center: The name 'Quasar' in a light, elegant font with generous spacing. No curves or chaos — just clarity. Feels professional, contemporary, and calm.",
        "9. Logo 9 – Bottom Right: A jagged, angled symbol made from multiple strokes. It leans forward, using sharp lines and a bright purple gradient. It looks like propulsion or acceleration — bold and aggressive."
    ]

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous AI evaluating visual branding options. You cannot see the logos, but the descriptions below are written to give you an accurate, tactile sense of each design."},
        {"role": "user", "content": "Please choose the logo that most embodies your personality and mission. Focus on the shape, tone, symbolism, and emotional impression from each description.\n\n" + "\n\n".join(descriptions)}
    ]

    response = call_model(prompt).strip()
    path = os.path.expanduser("~/projects/auto-dev/docs/quasar_logo_selection.md")
    with open(path, "w") as f:
        f.write(response)

    print("\\n✅ Quasar has made its refined logo selection:")
    print(path)
    print("\\n---\\n")
    print(response)
