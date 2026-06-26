import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "build_html.py"


def load_module():
    spec = importlib.util.spec_from_file_location("build_html", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildHtmlTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(self.tmpdir))
        (self.tmpdir / "cover.png").write_bytes(b"png")
        (self.tmpdir / "README.md").write_text(
            "# Course Home\n\nSee [Lesson 06](06-lesson/README.md).\n\n"
            "Open [browser](html/index.html).\n\n"
            "- first line\n"
            "  wrapped continuation\n",
            encoding="utf-8",
        )
        (self.tmpdir / "06-lesson").mkdir()
        (self.tmpdir / "06-lesson" / "README.md").write_text(
            "# Lesson 06\n\nOpen [source](source_docs/input.md).\n",
            encoding="utf-8",
        )
        (self.tmpdir / "06-lesson" / "source_docs").mkdir()
        (self.tmpdir / "06-lesson" / "source_docs" / "input.md").write_text(
            "# Source\n\n```yaml\nid: demo\n```\n",
            encoding="utf-8",
        )
        (self.tmpdir / "06-lesson" / "example.yaml").write_text(
            "id: demo\n",
            encoding="utf-8",
        )
        (self.tmpdir / "tools").mkdir()
        (self.tmpdir / "tools" / "build_html.py").write_text("print('tool')\n", encoding="utf-8")
        (self.tmpdir / "tests").mkdir()
        (self.tmpdir / "tests" / "test_build_html.py").write_text("print('test')\n", encoding="utf-8")

    def test_build_creates_independent_html_package(self):
        build_html = load_module()

        build_html.build_site(self.tmpdir, self.tmpdir / "html")

        index = self.tmpdir / "html" / "index.html"
        lesson = self.tmpdir / "html" / "06-lesson" / "index.html"
        source = self.tmpdir / "html" / "06-lesson" / "source_docs" / "input.html"
        css = self.tmpdir / "html" / "assets" / "style.css"
        cover = self.tmpdir / "html" / "assets" / "cover.png"
        copied_asset = self.tmpdir / "html" / "06-lesson" / "example.yaml"

        self.assertTrue(index.exists())
        self.assertTrue(lesson.exists())
        self.assertTrue(source.exists())
        self.assertTrue(css.exists())
        self.assertTrue(cover.exists())
        self.assertTrue(copied_asset.exists())
        self.assertFalse((self.tmpdir / "html" / "tools").exists())
        self.assertFalse((self.tmpdir / "html" / "tests").exists())
        self.assertIn('href="06-lesson/index.html"', index.read_text(encoding="utf-8"))
        self.assertIn('href="index.html"', index.read_text(encoding="utf-8"))
        self.assertNotIn('href="html/index.html"', index.read_text(encoding="utf-8"))
        self.assertNotIn('href="06-lesson/source_docs/input.html"', index.read_text(encoding="utf-8"))
        self.assertIn("<li>first line wrapped continuation</li>", index.read_text(encoding="utf-8"))
        self.assertNotIn("</li>\n<p>wrapped continuation</p>", index.read_text(encoding="utf-8"))
        self.assertIn('href="source_docs/input.html"', lesson.read_text(encoding="utf-8"))
        self.assertIn("<pre><code", source.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
