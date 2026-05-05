from pathlib import Path


def project_root():
    """
    Returns the repository root directory.

    Parameters:
        None

    Returns:
        Path pointing to the repository root
    """

    return Path(__file__).resolve().parents[1]


def format_ateco_code(code):
    """
    Converts an ATECO code to the teaching-friendly 5-digit dotted format.

    Parameters:
        code: ATECO code as text or number

    Returns:
        code as text in the form 73.11.0
    """

    code_as_text = str(code).strip()
    compact_code = code_as_text.replace(".", "")[:5].zfill(5)

    return f"{compact_code[:2]}.{compact_code[2:4]}.{compact_code[4]}"
