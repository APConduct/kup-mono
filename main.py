import fontforge
import psMat
import math

class MonoFontGenerator:
    def __init__(self, name="KupMono"):
        self.font = fontforge.font()
        self.font.fontname = name
        self.font.familyname = name
        self.font.fullname = name

        # set up basic font metrics
        self.font.ascent = 800
        self.font.descent = 200
        self.em_size = 1000
        self.stroke_width = 60

        # Set up grid
        self.font.grid.spacing = 100
        self.font.uwidth = self.stroke_width # Set uniform stroke width

    def create_glyph(self, char):
        """Create a glyph for the given character."""
        glyph = self.font.createChar(ord(char))
        glyph.width = self.em_size # Ensure monospace

        # Start fresh
        glyph.clear()
        pen  = glyph.glyphPen()

        if char == 'a':
            # Create circular bowl
            circle = fontforge.unitShape("elipses", self.stroke_width)
            # scale and position the circle
            circle.transform(psMat.scale(0.4))
            circle.transform(psMat.translate(300, 400))
            glyph.draw(circle)

            #add stem
            stem = fontforge.unitShape("rectangle", self.stroke_width)
            stem.transform(psMat.scale(0.1, 0.5))
            glyph.draw(stem)

        elif char == 'i':
            # create dot
            dot = fontforge.unitShape("elipses", self.stroke_width)
            dot.transform(psMat.scale(0.15))
            dot.transform(psMat.translate(500, 800))
            glyph.draw(dot)

            # create stem
            stem = fontforge.unitShape("rectangle", self.stroke_width)
            stem.transform(psMat.scale(0.1, 0.5))
            stem.transform(psMat.translate(500, 400))
            glyph.draw(stem)

        # add more characters here

        glyph.removeOverlap()
        glyph.simplify()
        glyph.round()

    def generate_font(self, output_path):
        """Generate the complete font file."""
        # Basic latin alphabet and numbers
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        for char in chars:
            self.create_glyph(char)

        # Set up font features
        self.font.selection.all()
        self.font.autoHint          # Add hinting
        self.font.autoInstr()       # Add TrueType instructions

        # Generate various font formats
        self.font.generate(f"{output_path}.ttf")    # TrueType
        self.font.generate(f"{output_path}.otf")    # OpenType
        self.font.generate(f"{output_path}.woff2")  # WOFF2 for web

if __name__ == "__main__":
    font = MonoFontGenerator()
    font.generate_font("KupMono")
