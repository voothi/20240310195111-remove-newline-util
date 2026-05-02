import unittest
import re
from remove_newline_util import clean_text

class TestRemoveNewlineUtil(unittest.TestCase):

    def test_hyphen_newline(self):
        """Tests standard hyphen followed by a newline."""
        self.assertEqual(clean_text("betre-\nten"), "betreten")
        self.assertEqual(clean_text("betre-\n ten"), "betreten")
        self.assertEqual(clean_text("betre- \n ten"), "betreten")

    def test_negation_symbol_hyphen(self):
        """Tests the logical negation symbol (¬) as a hyphen."""
        # Case from user: "leuch¬ tet" (same line)
        self.assertEqual(clean_text("leuch¬ tet"), "leuchtet")
        # Case with newline
        self.assertEqual(clean_text("leuch¬\ntet"), "leuchtet")
        self.assertEqual(clean_text("leuch¬ \ntet"), "leuchtet")
        # Multiple occurrences
        text = "leuch¬ tet and Ent¬ fernung"
        self.assertEqual(clean_text(text), "leuchtet and Entfernung")

    def test_newline_removal(self):
        """Tests that remaining newlines are replaced with spaces."""
        self.assertEqual(clean_text("line1\nline2"), "line1 line2")

    def test_html_tag_removal(self):
        """Tests removal of HTML tags."""
        self.assertEqual(clean_text("Hello <b>World</b>"), "Hello World")
        self.assertEqual(clean_text("Hello<br>World"), "Hello World")

    def test_multiple_spaces(self):
        """Tests that multiple spaces are collapsed into one."""
        self.assertEqual(clean_text("Hello   World"), "Hello World")

    def test_punctuation_spacing(self):
        """Tests that spaces before punctuation are removed."""
        self.assertEqual(clean_text("Hello ."), "Hello.")
        self.assertEqual(clean_text("Hello ! "), "Hello!")

    def test_full_sample(self):
        """Tests the full sample text provided by the user."""
        test_text = (
            "Weit draußen in den unerforschten Einöden eines total aus der Mode "
            "gekommenen Ausläufers des westlichen Spiralarms der Galaxis leuch¬ tet "
            "unbeachtet eine kleine gelbe Sonne. Um sie kreist in einer Ent¬ fernung "
            "von ungefähr achtundneunzig Millionen Meilen ein absolut unbedeutender, "
            "kleiner blaugrüner Planet, dessen vom Affen stam¬ mende Bioformen so "
            "erstaunlich primitiv sind, dass sie Digitaluhren noch immer für eine "
            "unwahrscheinlich tolle Erfindung halten."
        )
        cleaned = clean_text(test_text)
        self.assertIn("leuchtet", cleaned)
        self.assertIn("Entfernung", cleaned)
        self.assertIn("stammende", cleaned)
        self.assertNotIn("¬", cleaned)

    def test_custom_hyphenation_mark(self):
        """Tests that custom hyphenation marks from config are respected."""
        config = {
            'hyphenation_marks': '*',
            'join_same_line_hyphens': True,
            'collapse_multiple_spaces': True
        }
        # Same line
        self.assertEqual(clean_text("word* test", config), "wordtest")
        # Newline
        self.assertEqual(clean_text("word*\ntest", config), "wordtest")
        # Ensure default marks don't work if overridden
        self.assertIn("-", clean_text("word- test", config))

    def test_toggle_features(self):
        """Tests toggling space collapse and same-line joining."""
        config = {
            'hyphenation_marks': '-',
            'join_same_line_hyphens': False,
            'collapse_multiple_spaces': False
        }
        # Should NOT join on same line
        self.assertEqual(clean_text("word- test", config), "word- test")
        # Should join on newline (this is always done by Rule 1, just using marks)
        self.assertEqual(clean_text("word-\ntest", config), "wordtest")
        # Should NOT collapse spaces
        self.assertEqual(clean_text("extra   space", config), "extra   space")

    def test_german_compositional_hyphens(self):
        """Tests that German compositional hyphens (e.g. 'Luft- und') are preserved."""
        # Same line
        self.assertEqual(clean_text("Luft- und Seefracht"), "Luft- und Seefracht")
        self.assertEqual(clean_text("Ein- oder Ausstieg"), "Ein- oder Ausstieg")
        self.assertEqual(clean_text("See-, Luft- sowie Landfracht"), "See-, Luft- sowie Landfracht")
        self.assertEqual(clean_text("Hin- bzw. Rückfahrt"), "Hin- bzw. Rückfahrt")
        
        # Newline
        self.assertEqual(clean_text("Luft-\nund Seefracht"), "Luft- und Seefracht")
        self.assertEqual(clean_text("Ein-\noder Ausstieg"), "Ein- oder Ausstieg")
        self.assertEqual(clean_text("See-, Luft-\nsowie Landfracht"), "See-, Luft- sowie Landfracht")

    def test_dash_and_range_preservation(self):
        """Tests that standalone dashes and certain ranges are not collapsed."""
        # Standalone dash (preceded by space)
        self.assertEqual(clean_text("Value - Test"), "Value - Test")
        
        # Range with 'bis' (German for 'to')
        self.assertEqual(clean_text("10- bis 20 Uhr"), "10- bis 20 Uhr")
        self.assertEqual(clean_text("10-\nbis 20 Uhr"), "10- bis 20 Uhr")

    def test_mixed_hyphenation(self):
        """Tests a mix of word splitting and compositional hyphens."""
        text = "See-, Luft- und Land- \n transport sowie Hy- \n phenation."
        # See-, Luft- und -> preserved (compositional)
        # Land- \n transport -> joined (word split)
        # Hy- \n phenation -> joined (word split)
        # Note: clean_text removes space before punctuation like '.'
        result = clean_text(text)
        self.assertEqual(result, "See-, Luft- und Landtransport sowie Hyphenation.")

if __name__ == '__main__':
    unittest.main()
