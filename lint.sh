#!/bin/bash
set -euo pipefail

# Check if pylint is installed
if ! command -v pylint &> /dev/null
then
    echo "Pylint could not be found. Please install it first."
    exit
fi

# lint.sh — recursively run pylint on project Python files only.
# Usage:
#   ./lint.sh          # lint current directory recursively
#   ./lint.sh /path/to/dir

START_DIR="${1:-.}"

if [ ! -d "$START_DIR" ]; then
  echo "Error: '$START_DIR' is not a directory." >&2
  exit 2
fi

# Resolve absolute path of start dir
START_DIR="$(cd "$START_DIR" && pwd)"

# Build a find command that excludes common virtualenv and site-packages locations.
# Excluded directory names (relative basenames):
EXCLUDES=(
  "venv" "env" ".venv" ".env"        # common virtualenv dirs
  "site-packages" "dist-packages"   # pip-installed packages
  "__pycache__" "build" "dist"      # build artifacts
  ".eggs"                          # eggs
)

# Convert excludes into -path arguments for find
find_exclude_args=()
for e in "${EXCLUDES[@]}"; do
  # exclude any directory named X at any depth
  find_exclude_args+=( -path "*/$e" -prune -o )
done

# Also exclude hidden .venv names like .tox and .mypy_cache
find_exclude_args+=( -path "*/.tox" -prune -o -path "*/.mypy_cache" -prune -o )

# Find Python files under START_DIR while honoring excludes
# Use -type f and case-insensitive extensions .py and .pyw
mapfile -t files < <(find "$START_DIR" "${find_exclude_args[@]}" -type f \( -iname "*.py" -o -iname "*.pyw" \) -print)

if [ "${#files[@]}" -eq 0 ]; then
  echo "No Python files found under '$START_DIR' (after excluding venv/site-packages)." 
  exit 0
fi

# Optionally filter out files that live under a site-packages path resolved via python (best-effort)
# Get possible site-packages paths from the active Python (if any) to avoid linting those.
site_paths=()
if command -v python >/dev/null 2>&1; then
  while IFS= read -r p; do
    [ -n "$p" ] && site_paths+=("$p")
  done < <(python - <<'PY'
import sysconfig, sys
paths = set()
for k in ("purelib","platlib"):
    try:
        paths.add(sysconfig.get_path(k))
    except Exception:
        pass
# also include site.getsitepackages() if available
try:
    import site
    for p in getattr(site, "getsitepackages", lambda: [])():
        paths.add(p)
except Exception:
    pass
for p in sorted(p for p in paths if p):
    print(p)
PY
)
fi

# Remove any files that are located under detected site-packages paths (defensive)
if [ "${#site_paths[@]}" -gt 0 ]; then
  filtered=()
  for f in "${files[@]}"; do
    skip=false
    for sp in "${site_paths[@]}"; do
      # normalize
      sp="$(cd "$sp" 2>/dev/null && pwd || printf '%s' "$sp")"
      case "$f" in
        "$sp"/*) skip=true; break ;;
      esac
    done
    $skip || filtered+=("$f")
  done
  files=("${filtered[@]}")
fi

if [ "${#files[@]}" -eq 0 ]; then
  echo "No Python files remain after excluding site-packages/venvs."
  exit 0
fi

# Run pylint in batches to avoid argument length limits
BATCH_SIZE=200
i=0
exit_code=0
while [ $i -lt "${#files[@]}" ]; do
  batch=( "${files[@]:$i:$BATCH_SIZE}" )
  if ! pylint --rcfile=.pylintrc "${batch[@]}"; then
    exit_code=1
  fi
  i=$((i + BATCH_SIZE))
done

exit $exit_code
