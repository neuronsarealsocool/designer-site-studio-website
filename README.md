# Designer Site Studio

A responsive, open website library for high-end design prompts, reference packs and
linked assets. Search and filter the collection, save favorites in your browser,
inspect full prompts and asset maps, and copy/download prompts for your coding agent.

[Live website](https://studio-prompt-library.neuronsarealsocool.chatgpt.site/)
· [Agentic AI skill](https://github.com/neuronsarealsocool/designer-site-studio-agentic-ai-skill)
· [Prompt packs](https://github.com/neuronsarealsocool/designer-site-studio-prompt-packs)

## Make your own copy

Click **Use this template** on GitHub, choose **Create a new repository**, and give
your copy a name. You can also fork this repository or download its ZIP.

For a local copy, install Node.js 22.13 or newer and npm, then run:

```sh
git clone https://github.com/neuronsarealsocool/designer-site-studio-website.git
cd designer-site-studio-website
npm ci
npm run dev
```

Open the local address printed by Next.js, normally http://127.0.0.1:3000.
The included collection works without API keys or a publishing account.

## Build and host

```sh
npm run typecheck
npm run build
npm start
```

The build creates `out/`, a static website that can be served by any ordinary static
host at the root of a domain. `npm start` serves that build locally. Set the `PORT`
environment variable to change its default port of 3000.

To publish your own copy, use your host's Node build environment with `npm ci` and
`npm run build`, then publish the `out/` directory. Hosting beneath a URL subdirectory
needs additional base-path and root-relative asset-link configuration.

Set `NEXT_PUBLIC_SITE_URL` to your own HTTPS origin before building if you want the
metadata origin to match your domain. The fallback for local development is localhost.

## Customize it

| File | What to change |
| --- | --- |
| `app/page.tsx` | Brand, page sections, repository links and interactions |
| `app/globals.css` | Colors, typography, layout and responsive styles |
| `app/layout.tsx` | Browser title and social/search metadata |
| `app/library-data.json` | Pack titles, full prompts, media maps and previews |
| `app/site-examples.json` | Live website and repository references |
| `public/favicon.svg` | Browser icon |
| `public/prompts/`, `public/manifests/`, `public/downloads/` | Downloadable pack content |
| `public/thumbs/` | Optimized gallery previews |

Saved favorites use browser-local storage. There is no login, payment processing,
server database or paid generation in this website. The included examples may link
to external sites and media. Replace those links and media with authorized material
when adapting the collection to your own project.

The website uses the existing `studio-library-saved-v1` storage key and download
filenames for compatibility with earlier versions.

## Refresh from the skill library (optional)

The current packs and thumbnails are already included. For a later collection update,
Python 3.10+, Pillow and FFmpeg are optional maintenance tools:

```sh
python scripts/sync-library.py --skill-root /path/to/scroll-site-studio
python scripts/prepare-thumbnails.py
npm run typecheck
npm run build
```

`sync-library.py` refreshes the public data and downloadable prompt/manifest bundles.
`prepare-thumbnails.py` downloads linked, already approved media to an ignored local
cache and creates display copies; it does not generate paid media. Keep the pack
catalog, full prompts and asset maps consistent. Existing examples are references,
not guarantees that their business forms or services have working backends.

The creative workflow defaults to Replicate for new generated media. Agree any paid
model and budget first, and approve new or selected media in chat before publication.
WordPress is optional; this website itself is a Next.js static export.

## License and media rights

Original website code is MIT licensed; see [LICENSE](LICENSE).
Third-party prompts, media and models retain their applicable rights. Keep required
notices and review [THIRD_PARTY.md](THIRD_PARTY.md) before reusing those materials.
The repository contains the public collection and frontend, rather than a copy of
the owner's account settings or hosting identity.
