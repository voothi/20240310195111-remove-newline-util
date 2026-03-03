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

if __name__ == '__main__':
    unittest.main()
