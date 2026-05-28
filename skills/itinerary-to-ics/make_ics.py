#!/usr/bin/env python3
"""Turn a simple itinerary JSON into an Apple-Calendar-friendly .ics file.

Locations come from the library built by build_library.py. Each event names a
`place`; we look it up (case-insensitive substring) and reuse its exact
X-APPLE-STRUCTURED-LOCATION so Apple Calendar draws the map. Timezones referenced
by events are pulled from the library too. Output is folded to 75 octets with
CRLF line endings (the two things Apple's parser is strict about).

Usage:
    python3 make_ics.py itinerary.json [out.ics] [library.json]

Default out.ics:     itinerary.ics
Default library.json: ~/.itinerary-ics/library.json   (build it first)

See itinerary.example.json for the input shape.
"""
import json, os, sys

DEFAULT_LIB = os.path.expanduser("~/.itinerary-ics/library.json")


def fold(line):
    segs, seg, limit = [], "", 75
    for ch in line:
        if len((seg + ch).encode("utf-8")) > limit:
            segs.append(seg)
            seg, limit = ch, 74
        else:
            seg += ch
    segs.append(seg)
    return "\r\n ".join(segs)


def find_place(lib, name):
    places = lib["places"]
    if name in places:
        return places[name]
    low = name.lower()
    for k, v in places.items():
        if low in k.lower() or k.lower() in low:
            return v
    return None


def adhoc_structured(title, address, geo):
    addr = f';X-ADDRESS="{address}"' if address else ""
    return (f"X-APPLE-STRUCTURED-LOCATION;VALUE=URI{addr}"
            f";X-APPLE-RADIUS=100;X-APPLE-REFERENCEFRAME=1"
            f";X-TITLE={title}:geo:{geo}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    itin = json.load(open(sys.argv[1]))
    out_path = sys.argv[2] if len(sys.argv) > 2 else "itinerary.ics"
    lib_path = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_LIB
    if not os.path.exists(lib_path):
        sys.exit(f"No library at {lib_path}. Build it first:\n"
                 f"    python3 build_library.py /path/to/export.ics")
    lib = json.load(open(lib_path))

    lines = ["BEGIN:VCALENDAR", "VERSION:2.0",
             f"PRODID:{itin.get('prodid', '-//make_ics//EN')}",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH"]

    # emit only the timezones the events use
    needed = set()
    for ev in itin["events"]:
        for k in ("start", "end"):
            if isinstance(ev.get(k), dict) and ev[k].get("tz"):
                needed.add(ev[k]["tz"])
    for tz in sorted(needed):
        block = lib["timezones"].get(tz)
        if not block:
            print(f"WARNING: no VTIMEZONE for {tz} in library", file=sys.stderr)
            continue
        lines += block

    warnings = 0
    for ev in itin["events"]:
        loc_val = struct = None
        if ev.get("place"):
            p = find_place(lib, ev["place"])
            if p:
                loc_val, struct = p["location"], p["structured"]
            else:
                print(f"WARNING: place not found in library: {ev['place']!r} "
                      f"(event {ev.get('uid')})", file=sys.stderr)
                warnings += 1
        if struct is None and ev.get("geo"):
            title = ev.get("place_title") or ev.get("place") or "Location"
            loc_val = ev.get("address") or title
            struct = adhoc_structured(title, ev.get("address", ""), ev["geo"])

        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{ev['uid']}")
        lines.append(f"DTSTAMP:{itin.get('dtstamp', '20260101T000000Z')}")
        lines.append(f"SUMMARY:{ev['summary']}")
        if ev.get("description"):
            lines.append(f"DESCRIPTION:{ev['description']}")
        if ev.get("url"):
            lines.append(f"URL;VALUE=URI:{ev['url']}")
        if loc_val:
            lines.append(f"LOCATION:{loc_val}")
        if struct:
            lines.append(struct)
        lines.append(f"DTSTART;TZID={ev['start']['tz']}:{ev['start']['dt']}")
        lines.append(f"DTEND;TZID={ev['end']['tz']}:{ev['end']['dt']}")
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")

    data = "\r\n".join(fold(l) for l in lines) + "\r\n"
    open(out_path, "w", encoding="utf-8", newline="").write(data)
    bad = [l for l in data.split("\r\n") if len(l.encode()) > 75]
    print(f"wrote {out_path}: {len(itin['events'])} events, "
          f"{len(data)} bytes, {warnings} warning(s), "
          f"{'OK' if not bad else str(len(bad)) + ' overlong lines!'}")


if __name__ == "__main__":
    main()
