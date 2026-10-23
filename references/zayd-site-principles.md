# Field notes: boot and screensaver

A worked example from Zayd's personal site. Observations and design choices below are case-specific; they are not Tesla platform guarantees. Updated 2026-10-22.

Provenance: author-provided historical field notes and implementation records. The source videos and development repository are not public, so those historical observations cannot be independently reproduced from this package. The public routes show current behavior and may change. Reproduce any relevant finding on the actual target before relying on it.

## Boot: readability and deliberate pacing

Field notes from the boot sequence on [zayd.wtf](https://zayd.wtf/boot/).

Prior car observation: `/boot/`, October 12; viewport **1307×747 CSS px with touch**. Exact car model, year, display hardware, firmware and DPR were not supplied in the evidence recovered here.

- Let people read. `/boot/` starts held. Hold can be entered through a visible control, `h`, a command, or scrolling back. Stray taps do not dismiss a held boot; provide a deliberate enter/exit action. Remove the former five-second touch auto-close.
- Take timestamps when lines actually print. Keep them strictly increasing; precomputed and asynchronously interleaved stamps had run backward.
- Buffer asynchronous readings and drain in order at the display cadence rather than printing several resolved readings in one frame. Use instant tail following, with per-line entrance motion; preserve intentional scrollback.
- Box-drawing glyphs had produced rules roughly 1.6 times too wide. Use CSS boxes for panels, grids for labels/values with wrapping, and SVG geometry for the logo.
- Provide supported decorative glyphs and readable language fallbacks when fonts lack a script. Cap simultaneous decorative scrambles and reduce them when frame rate deteriorates. Deduplicate repeated prose across a run.

The initial implementation was checked in desktop Chromium at the recorded viewport and at desktop and phone widths. These were emulated checks, not new physical-car measurements.

## Idle: physical continuity and crisp detail

Field notes from the screensaver on [zayd.wtf](https://zayd.wtf/idle/).

Prior problems from car clips: bounce happened about 150px above the bottom, resize expanded from one side, motion felt slow/uneven, thin glowing accents disappeared, the dark-theme parchment inversion glared, and font spacing varied. Another controller could appear after 90 seconds.

- Measure the actual visible overlay with `clientWidth/Height` and `ResizeObserver`. The reported `visualViewport` height remained reduced after dock changes. Treat this as one observed browser behavior, not a fact about every Tesla firmware.
- Place the outer ring flush at contact and preserve mirrored overshoot in the physics. Remove accidental arena margins; keep content padding separate.
- Proposed tuning: speed 10% of overlay diagonal per second, clamped to 120–340px/s, launch angle 36–54 degrees; one rAF loop at available refresh. A frame over 100ms is treated as a pause in this design. These are site choices, not Tesla platform requirements.
- Resize new quotes about the center; defer growth near a wall until there is room. Proposed morph: 460ms easeOutExpo. Pin final line width during the transition to avoid rewrapping jumps.
- Use two crisp contrasting orange/purple rings, about 2–3px depending on scale, without glow. Keep the quiet center and softened stone tan. The proposed `--idle-tan` mixed 70% ink into paper; recheck rendered contrast rather than inheriting the historical ~6.5:1 claim.
- Proposed font: self-hosted IBM Plex Mono 500 Latin subset with OFL license. Fit actual DOM dimensions with an attached hidden twin, include font readiness in cached measurements, and refit after loading. Do not infer width from character count or measure `display:none` elements.
- Allow one idle controller. Pause background ash/meteor painting while the opaque overlay is active, using the existing lifecycle contract rather than adding competing owners.
- Wake lock was requested as an enhancement, not established as granted in the car.

The initial implementation included physics and desktop-browser checks. Actual-car bottom-edge behavior and wake-lock acceptance still need device verification.

## Preserve the design

Retain the bespoke, restrained visual identity: warm paper, hard ink, crisp accent detail, personal typography and intentional motion. Optimize the engineering under the visual treatment. Do not replace the site with a generic automotive dashboard. These principles do not authorize replacing artwork or rewriting an existing site in React Native.
