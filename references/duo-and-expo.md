# iPhone Duo, the website, and Expo

Verified 2026-10-22. Keep the browser and native paths distinct when deciding what to implement.

## Current Astro website: browser improvements

[Apple's Duo Q&A](https://developer.apple.com/forums/thread/847644) explicitly recommends responsive web design rather than detecting the device type. It says **Viewport Segments and Device Posture are opt-in experimental features in iOS 27.1**, available through Safari's Feature Flags. Do not require either API for the public site's primary navigation or claim default Safari support from an enabled development flag.

Use fluid layout, container-based breakpoints, safe-area padding on all four sides, dynamic viewport units with fallbacks, usable short-window layouts, and stable form/scroll state through resizing. Avoid placing essential actions in an assumed center/fold region. Preserve a usable one-column baseline; enhance to segment-aware panes only when exposed. A stylesheet's `@supports` or parser acceptance alone does not prove working device posture/segment reporting.

[Apple's Duo preparation portal](https://developer.apple.com/iphone-duo/) provides official design sessions, including Design for iPhone Duo, and Xcode 27.1 testing resources. Native reserved-region and arrangement APIs are not automatically browser APIs. Verify the site's real Safari behavior with chrome visible/hidden, keyboard shown, open/closed/partly folded states, short/wide windows, text zoom and safe areas. Report browser tests separately from native-device tests.

## Native companion: Expo SDK 58

[Expo's SDK 58 announcement](https://expo.dev/changelog/sdk-58) covers iOS 27, Duo, native bars/safe areas, `expo-hinge`, faster builds and the experimental agent CLI. Build against the right platform SDK and test actual window changes; installing Expo alone does not make a custom UI adaptive. Prefer system navigation and current safe-area support. Hinge angle is suitable for interactions/effects; use layout geometry and system containers to drive layout.

[Expo AppIntents documentation](https://docs.expo.dev/versions/v58.0.0/sdk/app-intents/) describes an **alpha** Apple-platform package. It exposes app actions/entities through Siri, Shortcuts, Spotlight and Apple Intelligence. It needs a native development build and declared native intents; it does not run in Expo Go or add Siri capabilities to a plain Astro website. Apple App Intents and Android intents are different systems. Do not promise headless JavaScript intent execution merely from installing this package.

[Expo's October 21 upgrade guide](https://expo.dev/blog/how-to-upgrade-to-sdk-58) now says project creation recommends SDK 58, with SDK 57 as a choice for the older Expo Go. `--template default@sdk-58` remains a deterministic way to request SDK 58. The store Expo Go update is still pending. EAS's SDK 58 iOS image now uses Xcode 27.1. [Expo CLI](https://docs.expo.dev/more/expo-cli/) is included with the project's `expo` package: use project-local `npx expo`, not the obsolete global `expo-cli` package.

## Recent community leads, with limits

The [first-person Duo Safari measurement write-up](https://doesitfit.lol/blog/iphone-duo-web-developers) reports about 382 CSS px of available outer-screen width and 951×669 for an unfolded layout, measured in Apple's simulator. Use these as labeled test fixtures, not physical-device guarantees. A [first-person Framer case study](https://www.offform.design/designing-websites-for-iphone-duo-how-we-made-our-framer-sites-go-edge-to-edge/) says normal viewport/safe-area settings did not make Safari's system control strip usable page space. Do not promise that a website can remove or paint native browser chrome; do not add unverified private viewport flags or device-size heuristics to force it.

Fresh X and Reddit discovery still shows conflicting claims about fold API availability. Resolve them using Apple's experimental-feature statement and feature-test the actual browser. Short-window content, independent insets, stable state on resize and reachable controls improve the real layout without relying on those claims.

For an authorized new native app, create a separate SDK 58 project, install compatible packages with `npx expo install`, run dependency checks/Doctor/type checks and export tests. Add App Intents only when the user has chosen an actual action to expose. Native toolchain setup, signing, simulator execution, accounts and public distribution each require their own readiness checks. Do not migrate the existing website merely to improve Tesla or Safari CSS.
