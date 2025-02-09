import fontforge
import psMat
import math

def create_monospace_font(font_name="MyMonoFont"):
    """Create a new monospace font with FontForge"""
    # Create a new font
    font = fontforge.font()

    # Set basic font properties
    font.fontname = font_name
    font.familyname = font_name
    font.fullname = font_name

    # Set font-wide properties for monospace
    font.em = 1000  # Standard UPM (units per em)
    font.ascent = 800
    font.descent = 200

    # Set monospace width - all characters will have this width
    mono_width = 600  # Standard for most monospace fonts

    # Define basic metrics
    x_height = 500      # Height of lowercase letters
    cap_height = 700    # Height of uppercase letters
    stroke_width = 80   # Base stroke width

    # Create basic Latin characters (A-Z, a-z)
    create_uppercase_letters(font, mono_width, cap_height, stroke_width)
    create_lowercase_letters(font, mono_width, x_height, stroke_width)
    create_numbers(font, mono_width, cap_height, stroke_width)
    create_punctuation(font, mono_width, stroke_width)

    # Set font features
    setup_font_features(font)

    return font

def create_numbers(font, width, height, stroke):
    """Create monospace numbers"""
    # Example: Create number '0'
    glyph = font.createChar(ord('0'))
    pen = glyph.glyphPen()

    # Define '0' geometry
    margin = width * 0.1
    oval_width = width - (2 * margin)
    oval_height = height - (2 * margin)

    # Draw oval
    pen.moveTo(width/2, margin)
    pen.curveTo(
        (width - margin, margin),
        (width - margin, height - margin),
        (width/2, height - margin)
    )
    pen.curveTo(
        (margin, height - margin),
        (margin, margin),
        (width/2, margin)
    )
    pen.closePath()

    # Set width for monospace
    glyph.width = width

def create_uppercase_letters(font, width, height, stroke):
    """Create uppercase letters with consistent metrics"""
    # Example: Create letter 'A'
    glyph = font.createChar(ord('A'))
    pen = glyph.glyphPen()

    # Define 'A' geometry
    left_stem = width * 0.2
    right_stem = width * 0.8
    crossbar_y = height * 0.4
    half_stroke = stroke / 2

    # Draw main triangle of 'A'
    pen.moveTo(left_stem - half_stroke, 0)
    pen.lineTo(width/2, height)
    pen.lineTo(right_stem + half_stroke, 0)
    pen.lineTo(right_stem - half_stroke, 0)
    pen.lineTo(width/2, height - stroke)
    pen.lineTo(left_stem + half_stroke, 0)
    pen.closePath()

    # Start new contour for crossbar
    pen = glyph.glyphPen()
    pen.moveTo(left_stem + stroke, crossbar_y - half_stroke)
    pen.lineTo(right_stem - stroke, crossbar_y - half_stroke)
    pen.lineTo(right_stem - stroke, crossbar_y + half_stroke)
    pen.lineTo(left_stem + stroke, crossbar_y + half_stroke)
    pen.closePath()

    # Set width for monospace
    glyph.width = width

def create_lowercase_letters(font, width, x_height, stroke):
    """Create lowercase letters with consistent metrics"""
    # Example: Create letter 'a'
    glyph = font.createChar(ord('a'))
    pen = glyph.glyphPen()

    # Define 'a' geometry
    bowl_diameter = x_height * 0.8
    stem_x = width * 0.7
    half_stroke = stroke / 2

    # Draw bowl
    pen.moveTo(width/2 - half_stroke, x_height/2)
    pen.curveTo(
        (width/2 + bowl_diameter/2 - half_stroke, x_height/2),
        (width/2 + bowl_diameter/2 - half_stroke, stroke),
        (width/2 - half_stroke, stroke)
    )
    pen.curveTo(
        (width/2 - bowl_diameter/2 - half_stroke, stroke),
        (width/2 - bowl_diameter/2 - half_stroke, x_height/2),
        (width/2 - half_stroke, x_height/2)
    )
    pen.closePath()

    # Start new contour for stem
    pen = glyph.glyphPen()
    pen.moveTo(stem_x - half_stroke, x_height)
    pen.lineTo(stem_x + half_stroke, x_height)
    pen.lineTo(stem_x + half_stroke, 0)
    pen.lineTo(stem_x - half_stroke, 0)
    pen.closePath()

    # Set width for monospace
    glyph.width = width

def create_punctuation(font, width, stroke):
    """Create punctuation marks"""
    # Example: Create period '.'
    glyph = font.createChar(ord('.'))
    pen = glyph.glyphPen()

    # Define period geometry
    dot_size = stroke
    x_pos = (width - dot_size) / 2

    # Draw dot as single filled shape
    pen.moveTo(x_pos, dot_size)
    pen.lineTo(x_pos + dot_size, dot_size)
    pen.lineTo(x_pos + dot_size, 0)
    pen.lineTo(x_pos, 0)
    pen.closePath()

    # Set width for monospace
    glyph.width = width

def setup_font_features(font):
    """Setup OpenType features for the font"""
    # Add common OpenType features
    font.addLookup("ligatures", "gsub_ligature", (), (("liga", (("latn", ("dflt")),)),))
    font.addLookupSubtable("ligatures", "ligatures-1")

    # Set font-wide properties
    font.encoding = "UnicodeFull"
    font.hasvmetrics = True
    font.os2_typoascent = font.ascent
    font.os2_typodescent = -font.descent
    font.os2_typolinegap = 100
    font.os2_winascent = font.ascent
    font.os2_windescent = font.descent
    font.os2_use_typo_metrics = True

    # Set panose values for monospace
    font.os2_panose = (2, 11, 5, 9, 2, 2, 3, 2, 2, 7)

def main():
    # Create the font
    font = create_monospace_font("MyMonoFont")

    # Generate the font files
    font.generate("MyMonoFont.otf")  # OpenType font
    font.generate("MyMonoFont.ttf")  # TrueType font

    print("Font files generated successfully!")

if __name__ == "__main__":
    main()
