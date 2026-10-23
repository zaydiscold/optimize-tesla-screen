# Optimize for Tesla Screen

A reusable agent skill for making websites work well in Tesla in-car browsers: modern Model 3 and Model Y, and the 2021+ landscape Model S and Model X. Includes source-backed guidance, a real-site case study, a private-by-default measurement page, and notes on iPhone Duo Safari and Expo.

This is a website optimization workflow. It does not install software on a vehicle or expose vehicle controls.

## Install

With an agent that supports the Skills CLI:

```sh
npx skills add zaydiscold/optimize-tesla-screen
```

Or clone this repository into your agent's skills directory:

```sh
git clone https://github.com/zaydiscold/optimize-tesla-screen.git ~/.codex/skills/optimize-tesla-screen
```

Use a different destination if that directory already contains a skill you want to preserve. Start a new agent session after installation.

## Use

```text
Use $optimize-tesla-screen to audit this site for a modern Model 3, Model Y,
Model S or Model X browser. Preserve the visual identity, measure the actual viewport,
fix the relevant issues, and distinguish emulation from real-car results.
```

Open [SKILL.md](SKILL.md) for the workflow and [the source ledger](references/sources.md) for evidence and caveats. The [Duo and Expo reference](references/duo-and-expo.md) explains when responsive CSS is sufficient and when a native app is relevant.

## Measure the browser

The standalone [viewport probe](assets/viewport-probe.html) reports CSS viewport size, DPR, safe areas, input capabilities, fixed-overlay bounds and recent resize events. It can also sample frame scheduling. It makes no network requests and writes no persistent data. Copying the report is a deliberate button action; keyboard-test text is excluded.

Serve the file on an authorized preview to open it in a parked car. Record model, year, firmware and display separately. Do not treat a 16-inch panel, a panel's physical resolution, a desktop emulation preset and the browser's usable CSS area as equivalent.

## What this release covers

- Actual overlay measurement and resize handling, including a previously observed stale `visualViewport` height.
- Readable fonts and glyph fallbacks, CSS panel geometry and deliberate boot hold/exit controls.
- Consistent animation timing, centered resizing, one animation owner, reduced-motion behavior and bounded font-load failure handling.
- Independent safe areas, short landscape windows, touch targets and native keyboard activation.
- Model S and Model X (2021+): panel facts, the one public DPR reading, a clearly labeled derived test fixture, and a capture checklist. See [the S/X reference](references/model-s-x.md).
- Both-axis scaling for fullscreen art, device-pixel snapping for moving text at fractional DPR, and tap-to-reveal fullscreen controls.
- A source-labeled case study from [zayd.wtf](https://zayd.wtf/).
- Duo Safari's experimental fold APIs and the boundary between an existing website and an Expo native companion.

Research refreshed October 23, 2026. Device behavior can change with firmware. The bundled probe was tested in desktop Chromium emulation; this release does not claim physical-car or Duo hardware certification.

## Validate

Requires Python 3.9 or newer and Node.js (CI uses Node 22).

```sh
python3 scripts/validate.py
```

MIT licensed. Copyright 2026 Zayd Khan.
