#!/usr/bin/env python3
"""
validate-song.py - Validate song files against Suno formatting rules.

Enhanced version of Brian's count-suno-fields.py concept.
Checks character counts, required elements, tag compliance, and formatting rules.

Usage:
    python3 tools/validate-song.py songs/my_song.md
    python3 tools/validate-song.py --json songs/*.md
"""

import argparse
import json
import re
import sys


def parse_song_file(filepath):
    """Parse a song file and extract Style Prompt and Lyrics sections."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (IOError, OSError) as e:
        return None, None, str(e)

    # Extract Style Prompt section
    style_match = re.search(
        r"## STYLE PROMPT:\s*\n(.*?)(?=\n##|\n---|\Z)", content, re.DOTALL
    )
    style_prompt = style_match.group(1).strip() if style_match else None

    # Extract Lyrics section
    lyrics_match = re.search(
        r"## LYRICS:\s*\n(.*?)(?=\n## PRODUCTION NOTES:|\Z)", content, re.DOTALL
    )
    lyrics_text = lyrics_match.group(1).strip() if lyrics_match else None

    return style_prompt, lyrics_text, None


def get_exclusions_text(style_prompt):
    """Extract the [Exclusions:] line from the style prompt area."""
    if not style_prompt:
        return ""
    match = re.search(r"\[Exclusions?:.*?\]", style_prompt, re.IGNORECASE)
    return match.group(0) if match else ""


def get_style_prompt_without_exclusions(style_prompt):
    """Get the style prompt text without the [Exclusions:] line."""
    if not style_prompt:
        return ""
    # Remove the exclusions line
    cleaned = re.sub(r"\n?\[Exclusions?:.*?\]\n?", "", style_prompt, flags=re.IGNORECASE)
    return cleaned.strip()


def get_lyrics_without_exclusions(lyrics_text):
    """Get lyrics text (exclusions are in style prompt area, not lyrics)."""
    if not lyrics_text:
        return ""
    return lyrics_text


def check_style_prompt_chars(style_prompt):
    """Check Style Prompt character count (<=1000, WARN at 900)."""
    text = get_style_prompt_without_exclusions(style_prompt)
    count = len(text)
    if count > 1000:
        return "FAIL", count, 1000
    elif count > 900:
        return "WARN", count, 1000
    else:
        return "PASS", count, 1000


def check_lyrics_chars(lyrics_text, style_prompt):
    """Check Lyrics field character count (<=5000, WARN at 4500).
    Exclusions are subtracted since they go in the Exclude field."""
    text = get_lyrics_without_exclusions(lyrics_text)
    # If exclusions appear in lyrics area (some formats), remove them
    text = re.sub(r"\[Exclusions?:.*?\]", "", text, flags=re.IGNORECASE).strip()
    count = len(text)
    if count > 5000:
        return "FAIL", count, 5000
    elif count > 4500:
        return "WARN", count, 5000
    else:
        return "PASS", count, 5000


def check_required_elements(lyrics_text):
    """Check for required elements in lyrics."""
    if not lyrics_text:
        return {}

    elements = {
        "[Title:": bool(re.search(r"\[Title:", lyrics_text)),
        "[Production Direction:": bool(
            re.search(r"\[Production Direction:", lyrics_text)
        ),
        "[Vocal Direction:": bool(re.search(r"\[Vocal Direction:", lyrics_text)),
        "[end]": bool(re.search(r"\[end\]", lyrics_text)),
    }
    return elements


def check_genre_first(style_prompt):
    """Check that genre is first in Style Prompt (first phrase before first comma)."""
    text = get_style_prompt_without_exclusions(style_prompt)
    if not text:
        return "FAIL", ""

    # Get the first item (before first comma)
    first_item = text.split(",")[0].strip()

    # Genre descriptors typically contain genre-related words or are short descriptive phrases
    # We check that it looks like a genre descriptor (not a technical parameter)
    technical_patterns = [
        r"^(tempo|key|bpm|\d+\s*bpm|vocal range)",
    ]
    for pattern in technical_patterns:
        if re.match(pattern, first_item, re.IGNORECASE):
            return "FAIL", first_item

    # If it's a short phrase that could be a genre, PASS
    if first_item and len(first_item) < 100:
        return "PASS", first_item
    else:
        return "FAIL", first_item


def check_tag_count(style_prompt):
    """Check tag count in Style Prompt (comma-separated items, optimal 5-8)."""
    text = get_style_prompt_without_exclusions(style_prompt)
    if not text:
        return "FAIL", 0

    tags = [t.strip() for t in text.split(",") if t.strip()]
    count = len(tags)

    if count > 10:
        return "FAIL", count
    elif count > 8:
        return "WARN", count
    elif count < 5:
        return "WARN", count
    else:
        return "PASS", count


def check_layer_declarations(style_prompt, lyrics_text):
    """Check that named parenthetical layers are declared in Style Prompt."""
    if not lyrics_text or not style_prompt:
        return "PASS", []

    style_text = get_style_prompt_without_exclusions(style_prompt)

    # Find named layers in lyrics: (X layer: text)
    layer_pattern = r"\((\w+)\s+layer:"
    layers_used = re.findall(layer_pattern, lyrics_text, re.IGNORECASE)

    undeclared = []
    for layer in layers_used:
        # Check if the layer keyword appears in the style prompt
        if not re.search(re.escape(layer), style_text, re.IGNORECASE):
            undeclared.append(layer)

    if undeclared:
        return "FAIL", undeclared
    else:
        return "PASS", undeclared


def check_section_tag_isolation(lyrics_text):
    """Check that section tags are on their own line (no lyrics on same line)."""
    if not lyrics_text:
        return "PASS", []

    violations = []
    lines = lyrics_text.split("\n")

    # Section tag pattern: [Verse ...], [Chorus ...], [Bridge ...], [Pre-Chorus ...],
    # [Outro ...], [Intro ...], [Hook ...], etc.
    section_pattern = r"^\[(?:Verse|Chorus|Bridge|Pre-Chorus|Outro|Intro|Hook|Interlude|Post-Chorus|Break|Instrumental|Solo)[^\]]*\]"

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue
        # Check if line starts with a section tag but has more content after
        match = re.match(section_pattern, stripped, re.IGNORECASE)
        if match:
            # Get the text after the section tag
            remaining = stripped[match.end():].strip()
            # If there's non-tag text after the section tag, it's a violation
            if remaining and not re.match(r"^\[", remaining):
                violations.append(f"Line {i}: {stripped[:60]}")

    if violations:
        return "FAIL", violations
    else:
        return "PASS", violations


def validate_file(filepath):
    """Run all validation checks on a file."""
    style_prompt, lyrics_text, error = parse_song_file(filepath)

    if error:
        return {
            "file": filepath,
            "error": f"Could not read file: {error}",
            "checks": [],
            "result": "ERROR",
            "failures": 1,
            "warnings": 0,
        }

    if style_prompt is None and lyrics_text is None:
        return {
            "file": filepath,
            "error": "Format not recognized - no ## STYLE PROMPT: or ## LYRICS: sections found",
            "checks": [],
            "result": "ERROR",
            "failures": 1,
            "warnings": 0,
        }

    checks = []
    failures = 0
    warnings = 0

    # 1. Style Prompt character count
    if style_prompt is not None:
        status, count, limit = check_style_prompt_chars(style_prompt)
        checks.append({
            "name": "Style Prompt Characters",
            "status": status,
            "detail": f"{count}/{limit} chars",
        })
        if status == "FAIL":
            failures += 1
        elif status == "WARN":
            warnings += 1
    else:
        checks.append({
            "name": "Style Prompt Characters",
            "status": "FAIL",
            "detail": "No Style Prompt section found",
        })
        failures += 1

    # 2. Lyrics character count
    if lyrics_text is not None:
        status, count, limit = check_lyrics_chars(lyrics_text, style_prompt)
        checks.append({
            "name": "Lyrics Field Characters",
            "status": status,
            "detail": f"{count}/{limit} chars",
        })
        if status == "FAIL":
            failures += 1
        elif status == "WARN":
            warnings += 1
    else:
        checks.append({
            "name": "Lyrics Field Characters",
            "status": "FAIL",
            "detail": "No Lyrics section found",
        })
        failures += 1

    # 3. Required elements
    if lyrics_text is not None:
        elements = check_required_elements(lyrics_text)
        for elem, present in elements.items():
            display_name = f"{elem}]" if not elem.endswith("]") else elem
            checks.append({
                "name": f"Required Element: {display_name}",
                "status": "PASS" if present else "FAIL",
                "detail": "PRESENT" if present else "MISSING",
            })
            if not present:
                failures += 1
    else:
        for elem in ["[Title:", "[Production Direction:", "[Vocal Direction:", "[end]"]:
            display_name = f"{elem}]" if not elem.endswith("]") else elem
            checks.append({
                "name": f"Required Element: {display_name}",
                "status": "FAIL",
                "detail": "MISSING (no lyrics section)",
            })
            failures += 1

    # 4. Genre first in Style Prompt
    if style_prompt is not None:
        status, genre_text = check_genre_first(style_prompt)
        checks.append({
            "name": "Genre First",
            "status": status,
            "detail": genre_text[:50] if genre_text else "empty",
        })
        if status == "FAIL":
            failures += 1
    else:
        checks.append({
            "name": "Genre First",
            "status": "FAIL",
            "detail": "No Style Prompt section found",
        })
        failures += 1

    # 5. Tag count in Style Prompt
    if style_prompt is not None:
        status, count = check_tag_count(style_prompt)
        checks.append({
            "name": "Tag Count",
            "status": status,
            "detail": f"{count} tags",
        })
        if status == "FAIL":
            failures += 1
        elif status == "WARN":
            warnings += 1
    else:
        checks.append({
            "name": "Tag Count",
            "status": "FAIL",
            "detail": "No Style Prompt section found",
        })
        failures += 1

    # 6. Layer declarations
    if style_prompt is not None and lyrics_text is not None:
        status, undeclared = check_layer_declarations(style_prompt, lyrics_text)
        detail = "no undeclared layers" if not undeclared else f"undeclared: {', '.join(undeclared)}"
        checks.append({
            "name": "Layer Declarations",
            "status": status,
            "detail": detail,
        })
        if status == "FAIL":
            failures += 1
    else:
        checks.append({
            "name": "Layer Declarations",
            "status": "PASS",
            "detail": "skipped (missing sections)",
        })

    # 7. Section tag isolation
    if lyrics_text is not None:
        status, violations = check_section_tag_isolation(lyrics_text)
        detail = "all section tags on own line" if not violations else f"{len(violations)} violation(s)"
        checks.append({
            "name": "Section Tag Isolation",
            "status": status,
            "detail": detail,
        })
        if status == "FAIL":
            failures += 1
    else:
        checks.append({
            "name": "Section Tag Isolation",
            "status": "PASS",
            "detail": "skipped (no lyrics section)",
        })

    # Determine overall result
    if failures > 0:
        result = "FAIL"
    elif warnings > 0:
        result = "WARN"
    else:
        result = "PASS"

    return {
        "file": filepath,
        "error": None,
        "checks": checks,
        "result": result,
        "failures": failures,
        "warnings": warnings,
    }


def format_text_output(results):
    """Format results as human-readable text."""
    output_lines = []

    for res in results:
        output_lines.append(f"=== FILE: {res['file']} ===")

        if res["error"]:
            output_lines.append(f"  ERROR: {res['error']}")
            output_lines.append("")
            continue

        for check in res["checks"]:
            status_str = f"[{check['status']}]"
            name = check["name"]
            detail = check["detail"]

            if name.startswith("Required Element:"):
                # Format required elements with dot leaders
                elem_name = name.replace("Required Element: ", "")
                padding = "." * max(1, 30 - len(elem_name))
                output_lines.append(f"  {elem_name} {padding} {detail}")
            elif name == "Style Prompt Characters":
                output_lines.append(f"  Style Prompt: {detail} {status_str}")
            elif name == "Lyrics Field Characters":
                output_lines.append(f"  Lyrics Field: {detail} {status_str}")
            elif name == "Genre First":
                output_lines.append(f"  Genre First: {check['status']} ({detail})")
            elif name == "Tag Count":
                output_lines.append(f"  Tag Count: {detail} {status_str}")
            elif name == "Layer Declarations":
                output_lines.append(f"  Layer Declarations: {check['status']} ({detail})")
            elif name == "Section Tag Isolation":
                output_lines.append(f"  Section Tag Isolation: {check['status']} ({detail})")
            else:
                output_lines.append(f"  {name}: {detail} {status_str}")

        output_lines.append("")
        output_lines.append(
            f"  RESULT: {res['result']} ({res['failures']} failures, {res['warnings']} warnings)"
        )
        output_lines.append("")

    return "\n".join(output_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Validate song files against Suno formatting rules.",
        epilog="Checks character counts, required elements, tag compliance, and formatting rules.",
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="One or more song file paths to validate",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON",
    )

    args = parser.parse_args()

    results = []
    for filepath in args.files:
        results.append(validate_file(filepath))

    if args.json_output:
        print(json.dumps(results, indent=2))
    else:
        print(format_text_output(results))

    # Exit code 1 if any failure
    if any(r["result"] == "FAIL" or r["result"] == "ERROR" for r in results):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
