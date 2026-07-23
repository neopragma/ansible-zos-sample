from pathlib import Path
import sys
from traceback import format_exc

# Make the project root importable when Ansible loads this filter plugin.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import racf.engine as engine

def racf_provision(path):
    try:
        p = Path(path)

        if p.is_file():
            return engine.generate_commands_from_file(p)

        if p.is_dir():
            return engine.generate_commands_from_directory(p)

    except Exception as exc:
        raise RuntimeError(format_exc()) from exc

class FilterModule:

    def filters(self):
        return {
            "racf_provision": racf_provision,
        }





