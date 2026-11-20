# Clothes Rack Showroom — complete working prompt

Create an immersive, responsive clothing showroom with a real-time Three.js room, two clothing rails on perpendicular walls, scroll-controlled entry, a camera that responds to desktop pointer movement, collection navigation, selectable garments, product details and a browser-local demonstration bag.

The supplied ready-to-run implementation is the most concrete reference for this pack. Use it verbatim when the user wants the existing Ruddo example, adapt its identity and collection when they have another brand, or use the room and interaction patterns as guidelines alongside their own references. Keep the user's existing project stack when integrating it. WordPress and WooCommerce are optional choices, not prerequisites.

## 1. Source, scope and delivery

The reference began with a short supplied showroom recording, followed by the explicit correction that the racks belong on separate walls and the camera should look around with mouse movement. Preserve those decisions. Do not place two parallel rails side by side along one flat back wall. The included source independently recreates the design using procedural geometry; the original garment models and original website source were not supplied. Do not claim the procedural garments are scans, production clothing assets or exact recovered originals.

The bundled version has no build step: `index.html`, `style.css`, `app.js`, `garments.js`, a locally bundled Three.js ES module, Outfit font and their required license notices. Extract the archive and serve its directory over HTTP, for example `python -m http.server 5188`, then open `http://localhost:5188`. Preserve the relative module and font paths. For another framework, move this scene and UI into the existing application without adding an unnecessary second framework.

The reference live example is [the Clothes Rack showroom](https://ruddo-clay-showroom.neuronsarealsocool.chatgpt.site/). The preview is a still of the corrected showroom, not a new product photograph or a separately generated video. The original supplied reference recording is not redistributed in this pack.

## 2. Visitor journey and composition

Begin outside the room, with the clothing rails intentionally soft behind the title. Present a sparse fixed header: the small overlapping double-disc mark at upper left, and `menu` plus `// cart` at upper right. The introduction centers `Clay-dyed / Workwear`, a very large, translucent `ruddo` wordmark with a registered mark, an offset orange label reading `Kiln-dyed`, `Slow-cut`, `SS27`, and a separate loose stack reading `Mended`, `Small runs`, `Monthly`.

The title should feel like typography placed in a physical space, with warm cloth, shadows and distance visible behind it. Use a restrained brown-to-sand room, off-white type and a sharp orange accent. Do not turn the opening into a conventional product-card grid. Keep the direct `ruddo.store` entry and the `scroll to walk in` cue near the lower center. The double-disc home control and the wordmark are different scales of the same simple identity.

Scrolling moves the camera forward. After entry, dissolve the introduction and sharpen the room. Show the back control, a subdued collection title when appropriate, an exploration hint and the fixed bottom Store/Men/Women navigation. Store frames both walls; Men and Women move toward the corresponding rack, turning the camera with the wall. Pointer movement adds a measured yaw/pitch response rather than moving all the content as one flat parallax layer.

## 3. Color, typography and layout values

Use Outfit, locally hosted from the included font, with Arial/sans-serif fallback and `font-display: swap`. The source palette is orange `#ff5c24`, ink `#241d16`, paper `#e7dfd1`, warm off-white `#fffdf4` and a dark room base around `#21170f`. Keep the supplied font's OFL notice.

The desktop header sits roughly 27px from the top and 32px from the sides. Its double disc is about 46×26px and the header links are approximately 16px. The desktop intro composition has a 560px-wide reference frame, its top around 30.5% of the screen, scaled by `min(1, viewportWidth / 1920)`. The reference display heading is 52px with close tracking; the oversized wordmark settles near 185px with strong negative tracking and a slight negative top margin. The orange label stack and manifesto should remain deliberately offset rather than mechanically centered underneath each other.

Keep the title translucent enough to see the room through it, while the main descriptive heading stays readable. The orange labels use dark text with tightly fitted rectangular fills. Panel surfaces are warm paper, with ink text, fine separators and clear controls. Match the supplied source for exact reuse; adjust typography and spacing coherently when adapting a longer brand name instead of retaining inappropriate fixed widths.

## 4. Three-dimensional room and lighting

Use a `PerspectiveCamera` with a 49° field of view, near plane 0.1 and far plane 180 as the reference baseline. The renderer uses antialiasing and alpha, an sRGB output color space, ACES filmic tone mapping, exposure around 1.16 and a device-pixel-ratio cap of 1.7. Share geometry and textures where possible so the showroom remains responsive.

The floor is a broad plane around 160×160 scene units, rotated horizontally just below y=0. Give it a warm sand shader that changes with distance from the two walls. Build two large wall planes meeting behind the racks, with rotations of +45° and −45°. In the supplied coordinate layout, wall centers are at x=−20/+20, y=23, z=11; each plane spans about `sqrt(2)×40` by 60 units. Shade one wall slightly darker, around 0.97 of the other, so the corner reads clearly. The wall shader transitions from light sand at floor level through brown into a nearly black ceiling region.

The men’s rail group is positioned near (−6.7, 0, −1.5) with a +π/4 rotation; the women’s group is near (6.7, 0, −1.5) with a −π/4 rotation. Store all garment, hit-target and contact-shadow positions relative to their own rotated rail group. Provide one helper that converts a rail-local point into a room/world point, and use it consistently for camera positions, look targets and projected product labels. Mixing local coordinates with unrotated world coordinates will break collection framing and hit testing.

Start with a warm hemisphere light (sky `#ece4d3`, ground `#55412b`, intensity about 2.4), a key directional light from (−8,12,8) around intensity 3.3, a fill from (10,8,5) around 1.8, and a rim from (2,7,−5) around 1.4. Use soft ambient contact shadows under the garments and each rail foot. The source draws a small radial canvas texture for these shadows; they should ground the objects without hard black ovals.

## 5. Clothing rails and procedural garments

Each rail is approximately 11.6 units wide and 5.96 units high. Model a thin, lightly imperfect metal tube with rounded upper corners and two tapered weighted feet. The source uses a curved tube radius near 0.031, warm metallic material `#bcb5a7`, and rough concrete-colored bases. Hang garments with visible wooden shoulders and small curved metal hooks; do not float clothing directly beneath an invisible rail.

Include 22 demonstration pieces, eleven in each collection. The color sequence is Coal `#242724`, Chalk `#e5e3d8`, Umber `#5e4d3a`, Ecru `#d0d0b8`, Indigo `#536c8b`, Mist `#a7bab9`, Terracotta `#b9583b`, Rose clay `#b88482`, Ochre `#b59b41`, Sage `#8d9d7d` and Ink `#222b2c`.

The men’s type sequence is shirt, hoodie, shirt, tee, pants, knit, tee, hoodie, shirt, knit, pants. The women’s sequence is shirt, hoodie, pants, tee, knit, pants, hoodie, tee, knit, shirt, shirt. Place them at rail-local x positions `−4.95 + index×0.99`, y near 5.19 and z near 0.02, scaled around 1.4. Give resting pieces an edge-on angle near 1.33 radians, with a small index-based variation. This lets hover turn a piece toward the visitor and makes the rail feel densely stocked.

Use garment silhouettes with sleeves, shoulders, neck openings, hems and separated trouser legs. The supplied geometry starts with 2D outlines, subdivides the triangles, displaces front and back panels into soft cloth folds, joins their edges and computes normals. Cotton should look matte: roughness around 0.94, zero metalness, double-sided panels and a subtle, repeating procedural fabric normal. Preserve the slightly uneven seam and fold structure rather than substituting glossy capsules or rigid boxes.

Differentiate garments with shirt plackets, small buttons, folded collars and pockets; hoodie hoods, drawstrings and kangaroo-pocket seams; knit ribs; sleeve cuffs; and trouser fly, belt loops, pockets and hems. Use the included `garments.js` as the authoritative implementation when exact reuse is requested. If the user supplies licensed production garment models, those may replace the approximations while retaining the interaction model. Model changes need visual review before publication.

## 6. Entry, camera states and mouse response

Normalize scroll progression as `clamp(scrollY / (viewportHeight×1.2), 0, 1)` and pass it through `t²(3−2t)`. The document runway is about 260vh. The reference enters Store when normalized scroll exceeds 0.42 and returns to the introduction below 0.08, provided a dialog is not open and a short programmatic-navigation suppression window has expired. Direct entry scrolls to roughly 1.2 viewport heights. Avoid smooth-scroll feedback that immediately returns a just-entered showroom to its initial state.

Initial camera reference: x=0, y≈3.9−0.4p, z≈22−4p on desktop, looking toward y≈5.3−2.4p. Narrow screens begin farther back, near z=31−3p. Store frames both rails from around (0,3.65,17.5), or z=29 on narrow screens, looking toward (0,2.9,−2).

A collection camera is computed in that rail’s local coordinates: y≈3.35, z≈9.8 on desktop or 10.7 on narrow screens, looking toward y=3.0. On phones, the x position tracks the selected piece. Selecting a product moves closer, near z=7 on desktop or 8 on narrow screens, and offsets desktop framing to leave room for the product panel.

Use time-based exponential easing with a factor near `1−exp(−dt×4.2)` and cap unusually long dt values around 0.05 seconds. Interpolate the camera position and look target separately. Normalize pointer position to −1…1, ease it, rotate the view direction around the world up axis and add a small vertical look offset. Approximate yaw limits are 0.14 radians in the intro, 0.38 in Store and 0.14 for a collection; vertical influence is smaller. Let Store have the widest look range.

Disable mouse-look for touch input, reduced motion, selected products and open dialogs. Clear or neutralize the pointer when it leaves the canvas, the window loses focus or collection navigation changes the view. UI controls must remain stable under the pointer. Scrolling should move the camera through the scene; pointer movement should look around within it.

## 7. Hover, selection and product labels

Use raycasting against simple, invisible pick volumes associated with the actual garment groups. A baseline pick box is around 0.78×3.4×0.95 units, offset below its hanger. Limit collection hit testing to that collection, and suppress it while a product or another dialog is open. The canvas cursor may indicate a selectable garment; essential navigation must also be available by keyboard and touch.

On hover or selection, ease the chosen garment toward a nearly frontal local rotation, around −0.025 radians, and draw it forward to local z≈1.25. Other pieces settle toward their own resting angles. An extremely small idle sway, about 0.008 radians, gives the rail life without turning it into a waving animation. Reduced motion removes this sway.

Project the active garment’s position to a small orange name label near its lower edge. Clamp the label into useful screen bounds and hide it when its projected position falls outside the safe area. Recalculate against the actual rotated wall, camera and viewport; a hard-coded label position will drift. Clicking a piece opens its details and focuses that garment.

## 8. Product panel and demonstration bag

Use an accessible native dialog sliding visually from the right, with warm paper fill and a subtly blurred backdrop. Desktop product panels are around 450px wide and full viewport height, with a close control, collection/season eyebrow, product name, price, a short description, color, XS/S/M/L/XL size choices, Add to bag, feedback and a fabric/care disclosure. Default to M and expose the selected size with `aria-pressed` as well as visual styling.

Demonstration prices in the source are tee $65, shirt $125, knit $135, hoodie $145 and trousers $155. Keep them clearly illustrative until an owner supplies genuine catalog data. Adding the same product and size increments quantity. A bag item is keyed by product ID and size; another size is a separate item. Bag rendering shows a color chip, item name, size, quantity, line total, an accessible Remove action, subtotal and Continue exploring.

Store bag state in local storage, validating recovered product IDs, sizes and positive integer quantities before using it. The included reference uses the compatibility key `ruddo-bag`. Handle malformed or unavailable browser storage without breaking the scene. Build item text using safe DOM text APIs rather than inserting untrusted catalog values as HTML.

This is a frontend showroom demo. Keep the visible statements that checkout is not connected and no payment is taken. Do not show an order-success state or pretend a bag operation is a completed purchase. If production commerce is requested, connect the user’s chosen real catalog, inventory, tax/shipping, checkout and order backend as separate work; WordPress/WooCommerce is one optional choice.

## 9. Navigation, dialogs and smaller screens

Store/Men/Women controls remain fixed along the bottom, with the active item orange and the others near-black. The desktop baseline is about 610×34px; the narrow layout is the viewport width minus 40px, 38px high and around 18px from the bottom. Collection selection updates camera orientation, active state, accessible pressed state and the faint collection heading. Back returns a collection to Store and Store to the introduction. Home resets the intro immediately without leaving a partially scrolled title.

The menu dialog contains The store, Men and Women navigation and a short brand note. Selecting a destination closes the menu, moves the camera and restores usable page controls. Synchronize `aria-expanded` with the menu’s actual open state. Native Escape behavior, visible close controls, sensible focus return and body scroll handling are required for every dialog. Avoid keyboard traps outside a correctly open modal.

At widths below about 700px, recompose the header and intro, move the camera back and show Previous garment, Explore a piece and Next garment controls for collection views. The intro reference is roughly 340px wide, with a 29px heading, 118px wordmark and smaller staggered label stacks. Ensure that any longer adapted brand fits instead of overflowing this reference frame. Product and bag panels must stay within screen bounds and retain internal scrolling for their content.

Touch users can move along the chosen rack with the arrow controls or a horizontal swipe exceeding roughly 40px. Keep vertical scrolling available for entering and leaving the room. Wrap the selected index within the collection. Keyboard users must be able to reach collection navigation and explicit product exploration without a mouse; the supplied desktop exploration controls become visible on focus. Never make hover the only path to product information.

## 10. Motion, failure and performance

Respect reduced motion for the camera, garment sway, blur and transitions. Keep the scene’s final readable states, controls and actual product information available. Avoid autoplay sound. The included source has a useful reduced-motion baseline; production refinements should also react to a changed preference during a session and avoid wasting rendering work while hidden or idle.

If WebGL cannot initialize, show an honest fallback with a reachable way to browse product details. A production adaptation should make the full collection reachable in that fallback, rather than only a single demonstration item. Do not remove the normal document and leave a blank canvas. Loading, module/font failure and missing assets should have understandable outcomes.

Cap rendering resolution, reuse geometry/materials, avoid rebuilding clothing on every frame and dispose of GPU resources if this scene mounts/unmounts inside an application. Test high-DPI phones and short viewports as well as wide monitors. The runnable source is an independently authored example with procedural approximations and a demonstration bag, not a connected production shop.

## 11. Hosted asset map

| ID | Role | Direct asset URL |
|---|---|---|
| showroom-preview | Approved screenshot of the corrected two-wall showroom | [Showroom preview](https://lapis-slate-xvar.here.now/library/clothes-rack-showroom/media/b89477202a0c6f.jpg) |
| showroom-source | Ready-to-run HTML/CSS/JavaScript source, Three.js, Outfit and notices | [Download the source bundle](https://lapis-slate-xvar.here.now/library/clothes-rack-showroom/media/763513fcde284d.zip) |

Keep the [required source, Three.js and font notices](https://lapis-slate-xvar.here.now/library/clothes-rack-showroom/notices.txt) with distributed copies. The source archive also contains the original component license files. These URLs are part of the complete prompt and should remain in copied and downloaded versions. Public access does not grant additional rights to another brand’s identity, reference material or third-party assets.

## 12. Acceptance and adaptation

Verify the opening composition and its responsive title scale; visible separation of the two perpendicular walls; scroll-in and reverse-scroll behavior; direct Store entry without a bounce back to the intro; collection camera turns; mouse yaw/pitch; hover orientation and projected labels; keyboard/touch exploration; size selection; duplicate-item quantity; separate sizes; remove/subtotal; local-storage recovery; menu, home, back and Escape; reduced motion; WebGL failure; and both desktop and narrow layouts.

For verbatim reuse, preserve the supplied materials, source proportions, interactions and stated limitations. For adaptation, establish the brand, audience, garment catalog, palette, type, pricing, room dimensions and product-detail content first. Keep the two-wall showroom and understandable camera states unless the user chooses another spatial idea. Replace the procedural clothing with owner-supplied assets when appropriate, and review any new composition or media before publication.

Use Replicate by default for genuinely new generated imagery or video, after agreeing the model and budget. No paid generation is needed to run this pack. Show any newly generated or selected media in chat and obtain approval before hosting it. Use the working prompt as written, as a detailed guide or in combination with the user's other ideas; do not force every build into an identical brand or platform.
