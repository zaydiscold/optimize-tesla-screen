# Source ledger: modern Tesla web optimization

Checked 2026-10-22. Recheck hardware and browser-specific claims when using this skill, especially after firmware updates. No real car was connected during research.

## Official hardware and vehicle UI

- [Tesla Model Y](https://www.tesla.com/modely): the October 17 retrieved Performance specifications listed a **16-inch center touchscreen** and **8-inch rear screen**; the October 22 direct retrieval returned promotional footnotes only. Confirm current regional specifications and the actual car. This evidence does not establish its web viewport or every region/trim's hardware.
- [Tesla Model 3](https://www.tesla.com/model3): the search-indexed current specifications listed a **16-inch center touchscreen**; direct retrieval returned only promotional footnotes. Treat the current model-page search excerpt as weaker evidence than a fully retrieved spec. Confirm the exact car, region and build. Refreshed 15.4-inch cars remain relevant; avoid treating “Highland” or “Juniper” as an exact resolution/DPR identifier.
- [Tesla Model Y touchscreen manual](https://www.tesla.com/ownersmanual/modely/en_us/GUID-518C51C1-E9AC-4A68-AE12-07F4FF8C881E.html): UI details vary with software, options and region; apps appear over the map, and system UI includes persistent controls and popups. Consequently measure the actual browser content area, not the whole panel. The manual describes separate rear-screen capabilities; do not infer a rear web browser exists.
- [Tesla entertainment manual](https://www.tesla.com/ownersmanual/modely/en_au/GUID-79A49D40-A028-435B-A7F6-8E48846AB9E9.html): entertainment availability depends on configuration/region, and video behavior changes outside Park. Do not infer that an arbitrary website can control vehicle UI, bypass restrictions or use CarPlay/Android Auto/native-app APIs.

## Browser observations: useful but not universal

- [Developer's August 2026 DPR report](https://www.reddit.com/r/TeslaBrowserApps/comments/1vk5trz/the_summer_update_changed_the_incar_browsers/): first-person report of a summer firmware change from DPR 1 to about 1.53 and changed touch/viewport assumptions. This is a discovery lead, not an official contract. It motivates recording DPR and input capabilities rather than hard-coding a model-to-resolution table.
- [Tesla Motors Club DPR thread](https://teslamotorsclub.com/tmc/threads/the-summer-update-changed-the-in-car-browsers-pixel-density-dpr-1-0-%E2%86%92-1-53-%E2%80%94-everything-renders-50-bigger-seeing-the-same-on-your-car.357805/): the fullest public capture (a 2024 Model Y: CSS screen 1920 × 1200 at DPR 1.0 before the summer 2026 update, 1254 × 784 at DPR 1.53 after) plus the only public Model S reading (a 2023 Model S at DPR ≈ 1.56, no dimensions). First-person reports; checked 2026-10-23.
- [Not a Tesla App screen comparison](https://www.notateslaapp.com/tesla-reference/1281/tesla-screen-size-comparison-for-all-tesla-models-including-size-resolution-and-aspect-ratio) (February 2024): panel specs per model, including 2021+ S/X at 17 inches and 2200 × 1300. Panel resolution only, never a browser viewport. See [the Model S and X reference](model-s-x.md).
- [2026.26.6.1 update report](https://www.notateslaapp.com/software-updates/version/2026.26.6.1/release-notes): an explicitly undocumented browser scaling change was reported to make sites larger and trigger different layouts. Corroboration only. Do not assert all cars have it or derive exact CSS dimensions from it.
- X research used `bird search 'Tesla browser (viewport OR developer OR resolution OR zoom)' -n 12 --plain`; results were mostly unrelated and did not establish reliable geometry. Do not elevate unrelated social posts into engineering evidence. The useful project-specific evidence is the first-person case study in [project principles](zayd-site-principles.md).

## Primary web platform guidance

- [W3C CSS Environment Variables](https://www.w3.org/TR/css-env-1/): independent safe-area variables and viewport-segment geometry. Use per-edge padding where content needs protection; feature support must still be checked in the actual browser.
- [W3C Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/): segment queries describe logical regions. Query available geometry/capabilities, not a speculative model name. Unsupported queries must leave a usable base layout.
- [WCAG 2.2 target minimum, AA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum): 24×24 CSS px minimum with defined exceptions. [Enhanced target size, AAA](https://www.w3.org/WAI/WCAG21/Understanding/target-size): 44×44 CSS px with exceptions. A 48px primary-control target is this skill's practical starting heuristic, not a Tesla requirement or a WCAG AA mandate.
- [Apple Responsive Design Mode](https://developer.apple.com/documentation/safari-developer-tools/responsive-design-mode): viewport/DPR presets approximate layout; actual keyboard, chrome and device behavior need simulator/device checks. The same evidence distinction applies to desktop Chromium emulating a Tesla viewport.

## Reproduction and acceptance

Open the supplied standalone probe on an authorized preview in the parked car, record the model/year/firmware, and capture its geometry before/after chrome and keyboard changes. Reproduce the affected route with that CSS size/input/DPR locally. Check both themes, text/font loading, all edge contacts, wake-lock denial and long-running lifecycle behavior as applicable. Finish with an actual-car rerun. A synthetic 16-inch or 1920px desktop profile alone cannot establish car compatibility.
