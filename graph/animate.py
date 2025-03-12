#!/bin/python3
import json
import os
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("animation", help="Path to the animation file")
parser.add_argument("output_dir", help="Directory to save the PDF files")
args = parser.parse_args()

animation_steps = json.load(open(args.animation))

# Read the base Mermaid diagram from the file
with open("ptraced.mermaid", "r") as file:
    base_diagram = file.read()


# Function to generate Mermaid diagram with classes for a specific step
def generate_mermaid_diagram(step):
    diagram = base_diagram
    for cls, nodes in step.items():
        for node in nodes:
            diagram += f"\n    class {node} {cls}"
    return diagram


# Directory to store temporary files
temp_dir = "/tmp/mermaid_animation"
os.makedirs(temp_dir, exist_ok=True)
# Directory to store PDF files
os.makedirs(args.output_dir, exist_ok=True)

# Generate PDFs for each animation step
for i, step in enumerate(animation_steps):
    diagram = generate_mermaid_diagram(step)
    temp_mermaid_file = os.path.join(temp_dir, f"step-{i}.mermaid")
    output_pdf_file = os.path.join(args.output_dir, f"step-{i}.pdf")

    with open(temp_mermaid_file, "w") as file:
        file.write(diagram)

    subprocess.run(
        [
            "mmdc",
            "-i",
            temp_mermaid_file,
            "-o",
            output_pdf_file,
            "-b",
            "transparent",
            "--pdfFit",
        ]
    )

print(f"PDFs saved to {args.output_dir}")
