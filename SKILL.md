---
name: optimize-tesla-screen
description: "Optimize and verify websites in Tesla in-car browsers: Model 3 and Model Y (including Highland/Juniper and 16-inch displays) and the 2021+ landscape Model S and Model X. Use for Tesla viewport, DPR, touch, font, boot-screen, animation, fullscreen and screensaver problems; preserve the site's existing identity."
---

# Optimize for Tesla Screen

Produce a usable, measured website on the requested car browser while retaining its existing visual identity. Target the front landscape screen of refreshed Model 3 and Model Y, and the 17-inch landscape screen of 2021+ Model S and Model X; identify the actual model/year, region, firmware and display when available. Do not equate display resolution, CSS viewport, browser zoom, or physical inches. Rear displays and the pre-2021 portrait S/X displays are separate targets. For S/X, read [the Model S and X reference](references/model-s-x.md): far fewer public measurements exist, so capture before you tune.

## Evidence and prior work

Read [the source ledger](references/sources.md) for hardware and browser evidence. For Zayd's site, read [the recovered project principles](references/zayd-site-principles.md) before changing boot or idle behavior. The case study separates field observations from implementation choices. Inspect the current checkout before applying it; never assume the example is already deployed.

Capture actual geometry with [the standalone viewport probe](assets/viewport-probe.html). Serve it from an authorized preview when testing in a car; it sends no telemetry. Record the model/year/firmware separately. Compare `innerWidth/Height`, root client size, `visualViewport`, DPR, all four safe-area insets, actual overlay bounds, and input capabilities before and after changing browser chrome or showing the keyboard. The historical **1307 × 747 CSS px** is one observed car viewport from the case study; it is a regression fixture, not a universal Tesla spec.

## Decisions that matter

- Use available container dimensions and content-driven breakpoints. Prefer `ResizeObserver` for overlay/canvas bounds. `visualViewport` is useful for keyboard visibility, but one observed Tesla session retained a stale reduced height; do not use it alone as a fullscreen physics arena.
- Scale fullscreen art and type from **both axes** of the measured arena, not the short side alone. A short-side-only scale made one car's 1307 × 747 viewport render smaller than a laptop, and a wider S/X arena would compound it. Size for arm's length.
- At fractional DPR (the 2026 car browsers report about 1.53–1.56), snap moving text layers to whole device pixels (`Math.round(x * dpr) / dpr`). Free sub-pixel translation resamples glyphs every frame and reads as soft or shimmering in motion.
- Make primary controls comfortably tappable; start around 48 CSS px and verify reach and legibility in the car. This is a project heuristic. WCAG's AA minimum is 24 CSS px with exceptions; 44 CSS px is the enhanced AAA target. Support taps and visible focus, not hover-only disclosure. Use capability checks, including `maxTouchPoints` and `any-pointer`, rather than UA/model guesses to choose input behavior.
- Preserve zoom. Use `width=device-width, initial-scale=1, viewport-fit=cover`, fluid widths, and four independent `env(safe-area-inset-*, 0px)` paddings on interactive foregrounds. Keep decorative fullscreen bounds separate from content safe areas.
- Check the actual loaded fonts. Measure rendered text, refit after fonts load, use appropriate licensed webfont subsets, and provide readable fallback glyphs. Build panels with CSS borders and logos with SVG geometry when glyph width is structural.
- Keep night palettes readable without large glaring fills. Check physical viewing distance and both themes; desktop screenshots cannot establish night glare or physical legibility.
- Use elapsed-time motion, preserve bounce distance, and avoid replaying a long hidden-tab interval on resume. Keep one owner for each animation, pause covered background effects, honor reduced motion, and lower decorative work if measured frame time degrades. Do not remove the visual character merely because the device is embedded.
- Test native Space/Enter activation of real controls as well as pointer clicks. Global terminal shortcuts must yield to focused buttons, and control updates must preserve focus. Reduced motion needs a static screensaver, not just a disabled entrance effect. A denied font load must release callbacks and use bounded retries.
- For controls on a fullscreen surface, reveal them on tap, pointer movement or key press, and auto-hide after a few seconds; keep them outside any `aria-hidden` art layer. On touch screens, `:hover` sticks to the last tapped element, so only honor hover when `(hover: hover)` matches. A pinned fullscreen surface must swallow taps so they never land on invisible links underneath.
- Feature-detect wake lock, fullscreen, clipboard, media and storage. Handle denials and interruptions. Never promise installation, fullscreen, hardware APIs or background survival without testing that specific browser. Keep car testing parked and respect vehicle restrictions.

## Verification and delivery

Test the observed viewport first, then continuously resize through narrower/wider and shorter/taller windows. If measurements are unavailable, use 1307×747 plus a reasonable landscape sweep such as 1024×600, 1280×720, 1440×900 and 1920×1080, and for S/X the derived ~1438×850 at DPR 1.56; label these synthetic cases, not hardware profiles. Vary DPR, coarse/fine input, both themes, reduced motion, font loading, long text, keyboard/chrome changes, hidden/resume and network interruption where relevant.

For boot: verify holding, explicit exit, scrollback, monotonically increasing timestamps and orderly async output. For idle: verify all four wall contacts, centered text morphs, one controller over the activation timeout and background rendering suspension. Add focused behavioral tests for changed mechanics. Review the visual result as well as numerical invariants.

Report separately: source evidence, local code/tests, emulated-browser behavior, actual-car observations and public deployment. Record findings in the project's `docs/` with reproduction, redacted evidence, sources, limitations and remaining hardware checks. Skill use does not itself authorize publication or merging.

For an accompanying iPhone Duo request or a proposed Expo migration, read [Duo and Expo boundaries](references/duo-and-expo.md). Browser responsiveness can be implemented in an Astro site without migrating it to Expo.
