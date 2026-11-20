# Rainy harbour penthouse

Build a single-screen cinematic landing page for Auralis, a fictional harbour-front penthouse firm. The visitor starts outside a pair of black lacquer doors. When they part, the view looks straight down on an illuminated rooftop pool. A fast camera tilt opens the harbour out to the horizon. The film dissolves into a live composition where the skyline crosses the foot of “Harbour” and a man rises into the foreground. At rest, the weather continues moving behind the buildings.

## Hosted media

Load the five 2000px WebP stills in one shared frame. Preserve the transparency of the skyline and balcony cutouts. Stream both videos directly from the linked MP4 files and preload the linked variable font.

| Role | Resource |
| --- | --- |
| doors | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/doors.webp |
| aerial | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/aerial.webp |
| back | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/back.webp |
| mid | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/mid.webp |
| front | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/front.webp |
| tilt | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/tilt.mp4 |
| rain | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/rain.mp4 |
| font | https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/media/font.woff2 |

Keep the [Inter font license](https://lapis-slate-xvar.here.now/library/rainy-harbour-penthouse/inter-OFL.txt) with redistributed copies of the font.

## Compose the final frame first

Use Inter throughout, with the supplied variable Latin font preloaded and displayed with swap. Set the tab title to “Auralis — Above the Harbour” and the description to “Auralis: harbour-view penthouses above a city that never sleeps. Above the harbour.”

Fill the viewport with an isolated, clipped hero on #0D0A22. Use a 100svh composition with a 520px minimum in ordinary orientations. Fit short landscape screens to their available height. Centre a 16:9 stage sized to cover the viewport. At 1440 × 900 the stage is 1600 × 900 and extends 80px past either side.

Stack these planes in paint order:

1. Storm sky and harbour water, two interchangeable rain videos, then a top shade from rgba(13,8,40,.45) to transparent across the upper 45%. Pivot the back plane at 50% 40%.
2. White live typography. Make “Harbour” the h1 with accessible name “Above the Harbour”. Give each of the seven letters an inline block, 700 weight, −.045em tracking and unit line-height. Set “Above the” in weight 300 with −.01em tracking.
3. The cutout skyline. Pivot at 50% 45%. Its highest towers reach about 33% of stage height, with the main skyline at 45%.
4. The balcony and figure, pivoting at bottom centre. Behind the cutout, fit glass between the posts at left 5.2%, right 4.1%, top 57.9%, height 25.4%. Blend rgba(190,200,255,.10), rgba(150,160,230,.05) at 60%, and rgba(120,130,210,.08) down the glass. Add a 1px white highlight at 18% opacity, 1.2px backdrop blur and 1.05 saturation. The figure’s crown is at 35.9%.

Centre the headline in the visible viewport. Measure the tracked word at 100px in its actual font. Calculate a font size that fits 62.5% of the stage width, 92% of the viewport width and the vertical clearance above its baseline. For the height limit, reserve 3.5vh beneath the nav and divide the remaining distance to the baseline by .88. Use the smallest limit. Measure “Harbour” after the font loads and fit the full word at 1440 × 900. Place the actual text baseline at 43% of the stage height, or 36.2% where height exceeds width × 1.2. Put the kicker at baseline minus .88em, set its font to .118 of the headline size, and shift it .1 kicker-em left of centre. On desktop the figure interrupts the lower middle of the word. In portrait its head just meets the base of the word.

## Viewport navigation

Use u = min(viewport width / 1440, viewport height / 900). Place the desktop bar 52u from the top, with 125u side insets, height 48u and 15u text. Set the home wordmark AURALIS at 17u, weight 600 and .28em tracking. Centre a pill group independently of both side groups. Use 5u padding, 6u gaps, 14% white fill, 12px backdrop blur and a 1px 12%-white inner edge. The links are Home, The Firm, Skyline Homes and Talk To Us, each 38u high with 22u horizontal padding. Home gets a white fill and #180F3C text at weight 600. Give other links 88% white text and a 250ms transition to a 14%-white hover fill.

At right, group a 20u outlined globe and “Eng” with a 9u gap. Leave 30u before the 44u-high Enquire pill. Give it 27u horizontal padding, #F2B8C0 fill, ink text and weight 600. Lift it 1px on hover and lighten to #F7C9D0. Keep navigation keyboard operable. Use compact in-page panels for destinations in this standalone concept. Make the enquiry action truthful about its outcome.

## Run one timed reveal

Cover the hero with a viewport-filling aerial still and a matching tilt video, then place the split doors above both. Each door uses half the same image, background-size 200% 100%, aligned to its outer edge. Use one master requestAnimationFrame clock driving paused Web Animations with 7400ms duration, fill both and offsets in milliseconds divided by 7400. Hold initial CSS states before playback. Wait for all five images and canplaythrough on the tilt, plus 120ms. Start after five seconds even on a slow connection.

| Interval in seconds | Action |
| --- | --- |
| .02–1.13 / .02–1.24 | Slide the left door to −101% with cubic-bezier(.1,.2,.8,1), and the right to +101% with cubic-bezier(.4,.6,.9,1). |
| 1.19–1.47 | Dissolve from the pool still into its matching tilt video, ease-in-out. |
| 1.25–2.85 | Play the full 5.04s silent tilt in 1.6s. Use clip duration / 1.6 as base rate. Correct drift towards the timeline target each frame, within .85–1.2 times that rate. Pause at the final frame. |
| 2.40 onward | Start the rain behind the city. |
| 2.45–2.95 | Dissolve the entire opening into the aligned skyline with cubic-bezier(.45,0,.55,1). |
| 2.45–2.75 | Fade the nav up from −6px, ease-out. |
| 2.45–3.10 | Fade the kicker upward from .5em with cubic-bezier(.2,.65,.3,1). |
| 2.45 + .054 × letter index | Reveal each letter from .14em below, fading to full white over .70s with the kicker easing. Index the seven letters from 0 to 6, so the final reveal ends at 3.474s. |
| 2.90–3.70 | Ease the top shade to full opacity. |
| 2.90–4.30 | Lift the sky 1.5% with cubic-bezier(.45,0,.35,1) and hold. |
| 2.90–4.30 / 4.60–6.90 | Lift the city 4% with cubic-bezier(.45,0,.3,1), hold, then ease back with cubic-bezier(.45,0,.55,1). |
| 3.00–4.80 | Move the headline block from 6% below its rest position to rest with cubic-bezier(.3,0,.4,1). |
| 3.35–6.00 / 6.00–7.30 | Bring the balcony up from 66% below to −2.5% with cubic-bezier(.2,.5,.2,1). Settle to zero with cubic-bezier(.45,0,.55,1). |
| 7.40 | Hide the opening and doors and leave the final scene interactive. |

Keep both rain players muted and inline over the sky still. Only use the colour-matched first 3.6s. As the active player crosses 2.85s, restart its partner at zero. Crossfade for .7s and pause the outgoing player .8s after the swap. Keep the still visible if playback fails. With reduced motion, show the composed final frame immediately and leave every video paused.

## Responsive acceptance

Below 820px use 18px side insets and a 16px top inset. Place the 14px wordmark (.22em tracking) opposite the 13px language label, 16px globe and 36px Enquire pill with 16px horizontal padding. Move the links to a full-width 40px second row 12px lower. Use 4px group padding, equal-width 32px links, 12px text and 10px horizontal padding. At 360px and below, use 11px type and 6px padding. In landscape at heights up to 500px, fit a single 34px nav row 12px from the top with 24px side insets. Use a 13px wordmark, 12px controls, 32px Enquire and 28px nav links.

Check 1440×900, 1536×686, 390×844, 360×640, 844×390 and 768×1024. Inspect the pool-to-film match, skyline dissolve, letter stagger, temporary tower overlap, late balcony rise, rain swaps and reduced-motion still. Verify the nav and enquiry flow with keyboard and touch-sized viewports. Keep each composition inside the viewport and the console clear.

## Live example

[Open the Auralis penthouse scene](https://auralis-harbour.neuronsarealsocool.chatgpt.site).
