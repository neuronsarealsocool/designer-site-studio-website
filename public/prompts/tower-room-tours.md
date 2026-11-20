# Tower and room tours

Build an immersive full-screen residential tower selector with an apartment
arrival and reversible room tours. A single-file HTML/CSS/vanilla JS implementation
is suitable for a new standalone demo; use the chosen/existing stack when needed.
Keep tower image, illuminated-window masks and floor hit zones on one registered
scene plane. Keep interface scaling independent so controls fit short screens.

Use the dawn and amber-window plates for floor feedback and the mist loop as an
optional muted atmosphere. Sequence tower-to-balcony then balcony-to-living films,
then settle onto the decoded living still. From there, provide bedroom and bathroom
entry with the matching authored return films. Preserve a useful still at every
handoff. Recompute masks, room anchors and cover transforms for any replacement
imagery; coordinates from another image are not generic architectural geometry.

- One registered scene plane holds tower imagery, lit-window masks and floor hit
  zones. A separate UI scale keeps the panel inside the viewport. Levels 4–32 are
  selected by hover, native range input or keyboard; floor feedback stays synchronized.
- Enter sequences tower-to-balcony and balcony-to-living footage, then decodes and
  settles onto a still before hiding the player. Room tags select authored forward/
  return clips. Preserve useful frames during handoffs and guard concurrent actions.
- Living-room anchors are image-relative and use the same cover/crop transform as
  the still. Clamp tags into reach on phones, retain Back/Escape, and manage focus
  according to keyboard interaction. Test short viewports and enlargement too.
- Playback speed profiles and a two-fetch queue are implementation choices to test,
  not measured performance guarantees. Bound clip waits, loading memory and retries;
  release blob URLs/resources and retain stills after errors or rejected playback.
- Reduced motion cuts between useful stills, disables entrance effects and mist/
  travel playback, and must retain every navigation path. Test initial and changed
  preferences rather than merely shortening CSS durations.

This media set reuses the same apartment media for every selected level; it does not
supply distinct tours for 29 floors. Its AED prices, unit sizes and view descriptions
are sample copy. The registration link is intentionally prevented from navigating.
Label a faithful reproduction as a demo; do not imply real availability, pricing
or a connected lead form. Connect a genuine action only within the requested scope.
The manifest has five PNGs and seven MP4s. Clips measure about 5.04 seconds at
24fps. Several are 1276x720 rather than 1280x720; use measured dimensions for crop
and handoff tests. The mist contains audio and must stay muted. This asset inventory
is not proof that every endpoint matches: inspect the actual joins in the build.

Test each selectable level, range/keyboard/pointer feedback, rapid input, Enter,
Back/Escape, both room paths, orientation, focus, reduced motion and media errors.
The registration action needs a genuine destination for a production project.
The supplied demonstration prices and repeated apartment footage do not establish
real availability or distinct tours for every level.

## Desktop framing: preserve the lake and mist

Fit the tower composition to viewport height on desktop, including ultrawide
Chrome windows. Width-driven cover scaling enlarges the tower until its base,
lake and mist are below the viewport. For the measured 1440 x 900 design plane,
use `--u: calc(100svh / 900)`, centre the 1440u x 900u plane horizontally at top 0,
and retain the imagery at top -30u, width 1440u and height 960u. Keep the floor
mask, label, hit area and selected-floor camera origin on this registered plane.
Preserve independent UI scaling and the existing phone/interior compositions.

Continuous desktop panorama: render the centre and side extensions into ONE
opaque canvas inside `.zoom`. Separate video/canvas elements and fallback
pseudo-elements can leave hairline GPU/compositing boundaries even when their
bounding boxes align and they share a transform. Do not use split DOM surfaces
or an opaque fallback pseudo-element above a moving side canvas.

The untransformed side width is `max(0px, (100vw - 1440u) / 2)`. The canvas spans
the centre plus both sides at the plate's original top and height. Draw the
undistorted centre from the exact current frame of the mist player. Fill the
sides with mirrored tower-free outer thirds of that SAME frame, compensating
for the player's centred cover crop. Round destination boundaries once into
integer backing-buffer pixels and fill adjacent regions without transparent
gaps. Use one opaque 2D context and size it from untransformed client dimensions,
not zoomed bounding rectangles. Hide the separate visual plate/player only once
the panorama is drawn; keep the player running as its video source.

Use requestVideoFrameCallback where available. Pause/cancel updates with the
mist player and when the page is hidden. Decode the dawn plate and draw it through
the exact same panorama compositor for reduced motion or playback failure. On
phones retain the original plate/player composition. This is video compositing,
not procedurally animated mist or a newly generated scene. All source media and
floor geometry stay unchanged. Keep the floor highlight and tag above the canvas.

Transition integrity: the entire panorama shares `.zoom` and its selected-floor
origin, opening animation, entry scale and return scale. Keep the UI outside it.
Inspect entry and return in Chrome, including intermediate frames and the opening
zoom. Look specifically for thin vertical lines against the smooth sky, not just
large crop errors or misaligned horizons. Matching rectangles alone is not proof
of a seamless render. Never conceal joins with a blur, dark wash or restored
width-driven crop.

Acceptance: retain the full tower crown/base, waterfront, boats and a clear lake
band with moving mist at 1920 x 1080, 2560 x 1080, 3440 x 1215 and extreme ultrawide
ratios. Resize without floor drift or growing zoom. Verify high/low floors,
slider feedback, Enter and return. At 390px preserve the phone layout and reachable
room tags. Reduced motion shows the decoded still panorama with no video/camera
motion. Do not call a stopped loop or offscreen fog verified moving mist.

## Project rules

Use this working prompt as written, adapt it, or lock selected elements and combine
the rest with the user's other ideas. Establish the real brand, audience, purpose,
primary action and required functionality. Keep the existing or chosen stack; for
a new project choose a suitable responsive frontend. WordPress and WooCommerce
are optional. Motion is optional unless required by this selected experience.

Default to Replicate for new media, using the bundled media workflow. Confirm the
model inputs and authorized budget before paid jobs. Show newly selected/generated
media in chat and obtain approval before putting it on any public site, preview,
CDN or repository. Reuse explicit approval for unchanged assets. The library host
is asset storage, not automatic approval for every future project's use.

Use real HTML text and semantic controls. Keep content useful before media loads.
Implement keyboard access, visible focus, touch controls, reduced motion, loading
and failure recovery. Test desktop, mobile, short screens and resize. Verify real
actions and label demonstration data. Do not claim a connected backend or measured
performance without testing it. Preserve applicable license notices; hosting a
copy does not grant new rights to brands, fonts or media.

## Hosted asset map

Use these direct URLs in the implementation. [Machine-readable manifest](https://lapis-slate-xvar.here.now/library/tower-room-tours/assets.json)
includes file sizes and SHA-256 hashes. Local manifest: `assets/manifests/tower-room-tours.json`.

| ID | Role | File |
| --- | --- | --- |
| asset-01 | tower dawn plate | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/d69f7a7c265c41.png) |
| asset-02 | amber window plate | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/9028729d570e46.png) |
| asset-03 | mist loop | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/d9260005fe8640.mp4) |
| asset-04 | bathroom still | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/83ad657818844d.png) |
| asset-05 | living room still | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/f71ee0cb96244b.png) |
| asset-06 | bedroom still | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/990133c719be4d.png) |
| asset-07 | bathroom return film | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/df4fe4a4d75043.mp4) |
| asset-08 | bedroom return film | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/2f4d338b38ed44.mp4) |
| asset-09 | tower to balcony film | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/0d6494f865f246.mp4) |
| asset-10 | living to bathroom film | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/1163d1658c8843.mp4) |
| asset-11 | living to bedroom film | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/0a4bef8f0bb142.mp4) |
| asset-12 | balcony to living room film | [Open asset](https://lapis-slate-xvar.here.now/library/tower-room-tours/media/c57d43b5697248.mp4) |

## Live website reference

[View live website](https://choose-your-floor.neuronsarealsocool.chatgpt.site)
