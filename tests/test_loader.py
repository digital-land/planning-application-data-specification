from bin import loader


class FakePost(dict):
    def __init__(self, metadata, content=""):
        super().__init__(metadata)
        self.content = content


def test_load_content_returns_fresh_tables(monkeypatch):
    fake_paths = ["specification/field/example.md"]

    def fake_glob(pattern):
        if pattern == "specification/field/*.md":
            return fake_paths
        return []

    def fake_frontmatter_load(path):
        return FakePost({"field": "example", "name": "Example"})

    monkeypatch.setattr(loader, "glob", fake_glob)
    monkeypatch.setattr(loader.frontmatter, "load", fake_frontmatter_load)

    first = loader.load_content()
    first["field"]["changed"] = FakePost({"field": "changed"})

    second = loader.load_content()

    assert "changed" not in second["field"]
    assert list(second["field"].keys()) == ["example"]


def test_load_needs_returns_fresh_tables(monkeypatch):
    need_paths = {
        "user-needs/need/*.md": ["user-needs/need/need-1.md"],
        "user-needs/justification/*.md": ["user-needs/justification/just-1.md"],
    }

    def fake_glob(pattern):
        return need_paths.get(pattern, [])

    def fake_frontmatter_load(path):
        if path.endswith("need-1.md"):
            return FakePost({"need": "need-1", "name": "Need 1"}, content="Need body")
        return FakePost({"id": "just-1"}, content="Justification body")

    monkeypatch.setattr(loader, "glob", fake_glob)
    monkeypatch.setattr(loader.frontmatter, "load", fake_frontmatter_load)

    first = loader.load_needs()
    first["need"]["changed"] = FakePost({"need": "changed"}, content="Changed")

    second = loader.load_needs()

    assert "changed" not in second["need"]
    assert second["need"]["need-1"]["__body__"] == "Need body"
    assert second["justification"]["just-1"]["__body__"] == "Justification body"
