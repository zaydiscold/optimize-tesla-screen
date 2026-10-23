# Model S and Model X (2021+ refresh)

Checked 2026-10-23. The S/X browser is a different target from the Model 3/Y screen. Fewer public measurements exist, so the measure-first rule matters more here. No S/X car was connected while writing this.

## What is established

- **Panel:** the 2021+ refresh moved S/X to a **17-inch landscape** center display. The listed resolution is **2200 × 1300 (about 150 PPI)**, which is wider and taller than the 15.4-inch 3/Y panel's 1920 × 1200 ([Not a Tesla App screen comparison](https://www.notateslaapp.com/tesla-reference/1281/tesla-screen-size-comparison-for-all-tesla-models-including-size-resolution-and-aspect-ratio), dated February 2024). This is the panel, not the browser viewport.
- **DPR after the summer 2026 update:** one 2023 Model S owner reported `devicePixelRatio` **≈ 1.56** in a [Tesla Motors Club thread](https://teslamotorsclub.com/tmc/threads/the-summer-update-changed-the-in-car-browsers-pixel-density-dpr-1-0-%E2%86%92-1-53-%E2%80%94-everything-renders-50-bigger-seeing-the-same-on-your-car.357805/) (August 10, 2026). The same thread's full capture is from a 2024 Model Y: CSS screen 1920 × 1200 at DPR 1.0 before the update and 1254 × 784 at DPR 1.53 after it. No S/X owner has published CSS viewport dimensions there. Treat all of this as first-person reports, not a Tesla contract.
- **Rear screen:** S/X have an 8-inch-class rear display (1440 × 900 listed). Nothing establishes a web browser on it; do not target or promise one.
- **Pre-2021 S/X** use a 17-inch **portrait** display with an older browser stack. Treat it as a separate legacy target and only optimize for it when someone actually asks.

## What is derived, not measured

If the S/X browser applies the same ~1.53–1.56 DPR to the full panel, the CSS screen would be about **1410–1438 × 833–850**. That is arithmetic from the panel spec and one DPR reading, not a capture. The usable `innerWidth/innerHeight` will be smaller once browser chrome and Tesla's system UI are subtracted. Use these numbers as a **synthetic fixture** labeled "S/X estimate" until a real probe capture replaces them.

## How to work on S/X

1. Run [the viewport probe](../assets/viewport-probe.html) in the parked car. Record model, year, firmware, DPR, `screen`, `inner*`, `visualViewport` and the overlay box, with the browser windowed and fullscreen.
2. Test at the S/X estimate (about 1438 × 850 at DPR 1.56, coarse pointer) plus the 3/Y fixtures. The extra width matters most for layouts that switch columns or cap line length.
3. Expect a **larger physical CSS pixel** than a laptop: at DPR ~1.56 on a ~150 PPI panel, one CSS pixel is about 1 / 96 inch, like a desktop monitor, but it is read from farther away. Size type and targets for arm's length, not for the pixel count.
4. Scale fullscreen art from **both axes** of the arena (see the main skill), so the wider S/X aspect does not shrink anything relative to 3/Y.
5. Report what you could not measure. If you only ran the estimate in desktop emulation, say so.

Please contribute a real S/X probe capture back to this file. Every number here gets better with one more car.
