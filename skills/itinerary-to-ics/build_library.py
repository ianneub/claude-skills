#!/usr/bin/env python3
"""Harvest map locations + timezones from an Apple Calendar .ics export.

Apple Calendar only draws a map when an event has an X-APPLE-STRUCTURED-LOCATION
property ending in a `geo:` URI. The richest version also carries an
X-APPLE-MAPKIT-HANDLE (an opaque Apple POI id) that CANNOT be generated offline.
The trick: harvest those blocks from a calendar export that already contains the
places you care about, then reuse them verbatim (see make_ics.py).

Usage:
    python3 build_library.py /path/to/export.ics [library.json]

Default library path: ~/.itinerary-ics/library.json
Re-run with more exports to grow the library; an existing entry is kept unless a
new one has a MapKit handle and the old one does not.

PRIVACY: the library contains the user's real locations (home, etc.). Keep it in
~/.itinerary-ics/ -- never commit it to a repo or share it.
"""
import json, os, sys

DEFAULT_LIB = os.path.expanduser("~/.itinerary-ics/library.json")


def unfold(path):
    raw = open(path, "r", encoding="utf-8", newline="").read()
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    out = []
    for line in raw.split("\n"):
        if line[:1] in (" ", "\t") and out:
            out[-1] += line[1:]
        else:
            out.append(line)
    return out


def title_of(struct):
    # X-TITLE may be quoted and may contain literal \n; take up to the :geo:
    if "X-TITLE=" not in struct:
        return None
    t = struct.split("X-TITLE=", 1)[1].rsplit(":geo:", 1)[0]
    if t.startswith('"') and t.endswith('"'):
        t = t[1:-1]
    return t.replace("\\n", " ").replace("\\,", ",").strip()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    lib_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_LIB
    os.makedirs(os.path.dirname(os.path.abspath(lib_path)), exist_ok=True)

    lib = {"places": {}, "timezones": {}}
    if os.path.exists(lib_path):
        lib = json.load(open(lib_path))
        lib.setdefault("places", {})
        lib.setdefault("timezones", {})

    lines = unfold(src)

    # timezones: capture whole VTIMEZONE blocks keyed by TZID
    i = 0
    while i < len(lines):
        if lines[i] == "BEGIN:VTIMEZONE":
            block, tzid = ["BEGIN:VTIMEZONE"], None
            i += 1
            while i < len(lines) and lines[i] != "END:VTIMEZONE":
                block.append(lines[i])
                if lines[i].startswith("TZID:"):
                    tzid = lines[i][5:]
                i += 1
            block.append("END:VTIMEZONE")
            if tzid:
                lib["timezones"][tzid] = block
        i += 1

    # places: every structured location, keyed by its title
    added, cur_loc = 0, None
    for l in lines:
        if l.startswith("LOCATION:"):
            cur_loc = l[len("LOCATION:"):]
        elif l.startswith("X-APPLE-STRUCTURED-LOCATION") and "geo:" in l:
            title = title_of(l)
            if not title:
                continue
            has_handle = "MAPKIT-HANDLE" in l
            old = lib["places"].get(title)
            if old and (old.get("has_handle") or not has_handle):
                continue
            lib["places"][title] = {
                "location": cur_loc or title,
                "structured": l,
                "geo": l.rsplit(":geo:", 1)[1],
                "has_handle": has_handle,
            }
            added += 1

    json.dump(lib, open(lib_path, "w"), indent=1)
    print(f"library: {lib_path}")
    print(f"  places   : {len(lib['places'])} (+{added} this run)")
    print(f"  timezones: {len(lib['timezones'])}")


if __name__ == "__main__":
    main()
