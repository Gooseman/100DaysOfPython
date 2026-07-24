import sys
from pathlib import Path

# Ensure the project's `src/` directory is on sys.path so tests can import `quiz_master`.
project_root = Path(__file__).resolve().parent
src_path = project_root / ".." / "src"
sys.path.insert(0, str(src_path.resolve()))
