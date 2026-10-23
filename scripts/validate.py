"""Check skill packaging, local references and the probe's inline JavaScript."""
from pathlib import Path
import re
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
skill = (root / "SKILL.md").read_text()
assert skill.startswith("---\n"), "Missing skill frontmatter"
frontmatter = skill.split("---", 2)[1]
assert re.search(r"^name: optimize-tesla-screen$", frontmatter, re.M)
assert re.search(r"^description: .+", frontmatter, re.M)
assert "TODO:" not in skill, "Unfinished scaffold"
for source in root.rglob("*.md"):
    if ".git" in source.parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", source.read_text()):
        if "://" in target or target.startswith("#"):
            continue
        path = (source.parent / target.split("#", 1)[0]).resolve()
        assert path.is_relative_to(root), f"Reference escapes package: {source}: {target}"
        assert path.is_file(), f"Missing reference: {source}: {target}"
probe = (root / "assets/viewport-probe.html").read_text()
scripts = re.findall(r"<script>([\s\S]*?)</script>", probe)
assert scripts, "Probe script missing"
with tempfile.TemporaryDirectory() as temp:
    for index, script in enumerate(scripts):
        path = Path(temp) / f"probe-{index}.js"
        path.write_text(script)
        subprocess.run(["node", "--check", str(path)], check=True)
print("Skill frontmatter, local references and probe JavaScript passed.")
