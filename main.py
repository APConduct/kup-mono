import fontforge
import psMat
import os
import math

def create_rounded_corner(pen, x1, y1, x2, y2, x3, y3, radius):
    """Create a rounded corner between three points using a quadratic curve."""
    # Calculate vectors
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x3 - x2, y3 - y2

    # Normalize vectors
    len1 = math.sqrt(dx1*dx1 + dy1*dy1)
    len2 = math.sqrt(dx2*dx2 + dy2*dy2)

    dx1, dy1 = dx1/len1, dy1/len1
    dx2, dy2 = dx2/len2, dy2/len2

    # Calculate rounded corner points
    p1x = x2 - dx1 * radius
    p1y = y2 - dy1 * radius
    p2x = x2 + dx2 * radius
    p2y = y2 + dy2 * radius

    # Draw the rounded corner
    pen.lineTo((p1x, p1y))
    pen.curveTo((x2, y2), (x2, y2), (p2x, p2y))

def create_monospace_font(font_name="KupMono"):
    # Create a new font
    font = fontforge.font()

    # Set basic font properties
    font.fontname = font_name
    font.familyname = font_name
    font.fullname = font_name
    font.encoding = 'UnicodeFull'

    # Set font parameters inspired by brass-mono and zed-mono
    font.ascent = 800
    font.descent = 200
    font.em = 1000  # Standard em square size
    font.design_size = 10

    # Set consistent dimensions for monospace
    glyph_width = 600  # Standard width for all glyphs

    corner_radius = 30 # Radius for rounded corners
    stroke_width = 80 # Width of main strokes

    # Function to create basic glyph with monospace metrics
    def setup_glyph(glyph):
        glyph.width = glyph_width
        glyph.vwidth = font.ascent + font.descent
        # Clear any existing contours
        glyph.clear()
        return glyph

    # Create basic Latin alphabet (a-z, A-Z)
    for unicode_val in range(65, 91):  # Uppercase A-Z
        char = chr(unicode_val)
        glyph = font.createChar(unicode_val, char)
        setup_glyph(glyph)

    for unicode_val in range(97, 123):  # Lowercase a-z
        char = chr(unicode_val)
        glyph = font.createChar(unicode_val, char)
        setup_glyph(glyph)

    # Create digits (0-9)
    for unicode_val in range(48, 58):
        char = chr(unicode_val)
        glyph = font.createChar(unicode_val, char)
        setup_glyph(glyph)

    # Add common punctuation marks
    punctuation = "!@#$%^&*()_+-=[]{}\\|;:'\",.<>/?"
    for char in punctuation:
        glyph = font.createChar(ord(char), char)
        setup_glyph(glyph)

    # Example of creating 'A' glyph with brass-mono inspired geometry
    glyph_A = font[ord('A')]
    pen = glyph_A.glyphPen()

    # Define 'A' contours
    pen.moveTo((50, 0))

    pen.lineTo((250, 800))

    pen.lineTo((450, 0))
    pen.lineTo((400, 0))
    pen.lineTo((250, 600))
    pen.lineTo((100, 0))
    pen.closePath()

    # Add crossbar
    pen.moveTo((150, 250))
    pen.lineTo((350, 250))
    pen.lineTo((350, 300))
    pen.lineTo((150, 300))
    pen.closePath()

    glyph_B = font[ord('B')]
    pen = glyph_B.glyphPen()


    # Generate font files
    def generate_font_files(font, name):
        # Generate OTF
        otf_path = f"{name}.otf"
        font.generate(otf_path)
        print(f"Generated {otf_path}")

        # Generate TTF
        ttf_path = f"{name}.ttf"
        font.generate(ttf_path)
        print(f"Generated {ttf_path}")

        # Generate WOFF
        woff_path = f"{name}.woff"
        font.generate(woff_path)
        print(f"Generated {woff_path}")

        # Generate WOFF2
        woff_path = f"{name}.woff2"
        font.generate(woff_path)
        print(f"Generated {woff_path}")

    return font, generate_font_files

# Create and generate the font
font, generate_files = create_monospace_font()
generate_files(font, "KupMono")
