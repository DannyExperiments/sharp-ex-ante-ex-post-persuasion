"""Render a rotating perspective view of the four-state witness.

Pillow is used only for rendering. Run from the repository root.
"""

import argparse
from itertools import combinations
from math import cos, pi, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


VERTICES = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
BACKGROUND = "#101d33"
INK = "#f5f7fd"
MUTED = "#cad7ed"
TEAL = "#77e8dc"
GOLD = "#ffca79"


def project(point, angle):
    x, y, z = point
    rotated_x = x * cos(angle) + z * sin(angle)
    turned_depth = z * cos(angle) - x * sin(angle)
    tilt = 0.24 + 0.16 * sin(angle + pi / 3)
    rotated_y = y * cos(tilt) - turned_depth * sin(tilt)
    depth = y * sin(tilt) + turned_depth * cos(tilt)
    scale = 575 / (5.2 - depth)
    return 226 + scale * rotated_x, 262 - scale * rotated_y, depth


def build_frame(angle, fonts):
    title, label, value, body, state = fonts
    canvas = Image.new("RGB", (800, 570), BACKGROUND)
    draw = ImageDraw.Draw(canvas)
    draw.text((26, 20), "Four states, two constraint rules", fill=INK, font=title)
    draw.line((28, 77, 772, 77), fill="#385371", width=2)
    draw.rounded_rectangle((459, 106, 772, 437), radius=15, fill="#1a2b47")
    draw.text((484, 124), "M = 3", fill=INK, font=value)
    draw.text((485, 195), "Ex ante", fill=MUTED, font=label)
    draw.text((743, 183), "1", fill=TEAL, font=value, anchor="ra")
    draw.text((485, 265), "Ex post", fill=MUTED, font=label)
    draw.text((743, 253), "7/54", fill=GOLD, font=value, anchor="ra")
    draw.line((484, 321, 745, 321), fill="#385371", width=2)
    draw.text((485, 362), "Gap", fill=INK, font=label)
    draw.text((743, 346), "54/7", fill=INK, font=value, anchor="ra")

    nodes = [project(point, angle) for point in VERTICES]
    center = project((0, 0, 0), angle)
    edges = sorted(combinations(nodes, 2), key=lambda pair: sum(point[2] for point in pair))
    for first, second in edges:
        far = first[2] + second[2] < 0
        draw.line((*first[:2], *second[:2]), fill="#41677b" if far else "#6caeb3", width=3 if far else 4)

    entries = [(x, y, z, f"e{index}", TEAL)
               for index, (x, y, z) in enumerate(nodes, 1)]
    entries.append((*center, "", GOLD))
    for x, y, _, name, color in sorted(entries, key=lambda item: item[2]):
        radius = 14 if name else 12
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color, outline=BACKGROUND, width=3)
        if name:
            side = 1 if x >= center[0] else -1
            draw.text((x + 18 * side, y + 1), name, font=state, fill=INK,
                      stroke_width=3, stroke_fill=BACKGROUND, anchor="lm" if side == 1 else "rm")

    draw.text((28, 469), "●", fill=TEAL, font=body)
    draw.text((57, 469), "Ex ante can reveal all four states.", fill=MUTED, font=body)
    draw.text((28, 513), "●", fill=GOLD, font=body)
    draw.text((57, 513), "Caps and the fixed mean force the uniform prior.", fill=MUTED, font=body)
    return canvas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font", default="DejaVuSans.ttf")
    parser.add_argument("--bold-font", default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output", type=Path, default=Path("visualization/persuasion-gap.gif"))
    args = parser.parse_args()
    fonts = tuple(
        ImageFont.truetype(font, size)
        for font, size in [
            (args.bold_font, 39), (args.regular_font, 28), (args.bold_font, 45),
            (args.regular_font, 28), (args.bold_font, 24)
        ]
    )
    frames = [
        build_frame(0.58 + tau * index / 64, fonts).quantize(colors=120, method=2)
        for index in range(64)
    ]
    frames[0].save(args.output, save_all=True, append_images=frames[1:],
                   duration=92, loop=0, disposal=2, optimize=True)


if __name__ == "__main__":
    main()
