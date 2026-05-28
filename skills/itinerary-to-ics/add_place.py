#!/usr/bin/env python3
"""Add a place to the library by coordinates (handle-less pin).

Use this when an airport (or any location) is NOT in the library and you don't
have a calendar export that contains it. You CANNOT fabricate an
X-APPLE-MAPKIT-HANDLE offline, but a `geo:` URI + title is enough for a working
map pin in Apple Calendar -- it just won't be a rich POI card.

The entry persists in the library, so future trips through this place reuse it.
If you LATER get an export that contains this place, re-run build_library.py:
the richer handle-bearing entry will upgrade this one automatically.

Usage:
    python3 add_place.py "Title" "LAT,LON" ["Full, Address, Here"] [library.json]

Example:
    python3 add_place.py "Boise Airport" "43.564386,-116.222861" \\
        "3201 W Airport Way, Boise, ID 83705, United States"

Getting coordinates (decimal degrees, latitude first):
  - Google Maps: right-click the spot -> the top of the menu is "lat, lon"
    (click it to copy).
  - Apple Maps: drop a pin / search, then Share -> the URL contains ll=lat,lon.
  - Wikipedia: most airports list "Coordinates" in the infobox.
"""
import json, os, re, sys

DEFAULT_LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "library.json")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    title = sys.argv[1].strip()
    geo = sys.argv[2].strip().replace(" ", "")
    address = sys.argv[3].strip() if len(sys.argv) > 3 else ""
    lib_path = sys.argv[4] if len(sys.argv) > 4 else DEFAULT_LIB

    if not re.fullmatch(r"-?\d+\.?\d*,-?\d+\.?\d*", geo):
        sys.exit(f"geo must be 'LAT,LON' decimal degrees, got {geo!r}")

    os.makedirs(os.path.dirname(os.path.abspath(lib_path)), exist_ok=True)
    if os.path.exists(lib_path):
        lib = json.load(open(lib_path))
    else:
        print(f"NOTE: no library at {lib_path}; creating one with no timezones. "
              f"Build from an export first so events get VTIMEZONE blocks.",
              file=sys.stderr)
        lib = {"places": {}, "timezones": {}}
    lib.setdefault("places", {})
    lib.setdefault("timezones", {})

    existing = lib["places"].get(title)
    if existing and existing.get("has_handle"):
        print(f"REFUSING: {title!r} already exists WITH a MapKit handle "
              f"(richer than coordinates). Leaving it untouched.", file=sys.stderr)
        return

    addr = f';X-ADDRESS="{address}"' if address else ""
    structured = (f"X-APPLE-STRUCTURED-LOCATION;VALUE=URI{addr}"
                  f";X-APPLE-RADIUS=100;X-APPLE-REFERENCEFRAME=1"
                  f";X-TITLE={title}:geo:{geo}")
    lib["places"][title] = {
        "location": address or title,
        "structured": structured,
        "geo": geo,
        "has_handle": False,
    }
    json.dump(lib, open(lib_path, "w"), indent=1)
    print(f"{'updated' if existing else 'added'}: {title!r} -> geo:{geo}")
    print(f"library now has {len(lib['places'])} places")


if __name__ == "__main__":
    main()
