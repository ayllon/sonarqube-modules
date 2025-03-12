#!/bin/bash

mmdc -i ptraced.mermaid -b transparent -o ptraced.pdf --pdfFit
./animate.py changed.json changed
./animate.py building.json building
