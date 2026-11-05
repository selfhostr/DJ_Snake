<div align="center">

<a href="https://djsnake.selfhostr.io"><img src=".github/assets/banner.svg" alt="djsnake: a self-hosted Discord music bot" width="100%"></a>

<h3>A self-hosted Discord music bot with a live clip page that shows the video in sync.</h3>

<a href="https://djsnake.selfhostr.io"><img src="https://raw.githubusercontent.com/selfhostr/.github/main/profile/assets/btn-site.svg" alt="Website" height="40"></a>
<a href="https://djsnake.selfhostr.io/docs/"><img src="https://raw.githubusercontent.com/selfhostr/.github/main/profile/assets/btn-docs.svg" alt="Documentation" height="40"></a>
<a href="https://djsnake.selfhostr.io/demo/"><img src="https://raw.githubusercontent.com/selfhostr/.github/main/profile/assets/btn-demo.svg" alt="Live demo" height="40"></a>
<a href="https://github.com/selfhostr/djsnake/releases"><img src="https://raw.githubusercontent.com/selfhostr/.github/main/profile/assets/btn-releases.svg" alt="Releases" height="40"></a>

<br><br>

[![CI](https://img.shields.io/github/actions/workflow/status/selfhostr/djsnake/ci.yml?branch=main&label=CI&logo=githubactions&logoColor=white)](https://github.com/selfhostr/djsnake/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/selfhostr/djsnake/badge)](https://scorecard.dev/viewer/?uri=github.com/selfhostr/djsnake)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

<br><br>

<img src="docs/screenshots/demo.webp" alt="djsnake joins a Discord voice channel and posts the clip link, then the clip page plays a synced video with a drag-and-drop queue" width="100%">

</div>

## Overview

- **Plays what you paste.** YouTube, Spotify, SoundCloud, Bandcamp, Deezer and Apple Music links, live streams and radios, or plain text searches, in your voice channel.
- **A clip page next to the chat.** The bot posts a link to a page that shows the video in sync and controls the queue.
- **Free, for good.** MIT licence, no paid edition.

djsnake is an independent project, not affiliated with or endorsed by YouTube, Spotify or Discord.

## Quick start

1. In the [Discord Developer Portal](https://discord.com/developers/applications), create an application and add a bot. Enable the **Message Content Intent** and invite the bot with the `bot` and `applications.commands` scopes.
2. Deploy the prebuilt image (`ghcr.io/selfhostr/djsnake`):

```bash
git clone https://github.com/selfhostr/djsnake.git && cd djsnake
cp .env.example .env        # set DISCORD_TOKEN
docker compose pull && docker compose up -d
```

3. Join a voice channel and send `!play https://www.youtube.com/watch?v=...`. The bot posts the clip page link.

The clip page listens on `127.0.0.1:47823` by default. Put a reverse proxy in front and set `PUBLIC_BASE_URL` to share it. Back up `./data` with `python -m djsnake.backup create`. Details: [installation](docs/source/installation.md), [configuration](docs/source/configuration.md), [backup and restore](docs/source/backup.md).

## Features

- Spotify, Deezer and Apple Music playlists, albums and tracks are matched on YouTube with no account or API key ([Spotify](docs/source/spotify.md), [more sources](docs/source/sources.md)).
- Independent queue per server, loop, shuffle, optional crossfade, autoplay and a 24/7 mode.
- Automix: SponsorBlock cuts, loudness normalised to -14 LUFS, silence trimmed, fades.
- Audio filters, volume, saved playlists, vote-to-skip and a DJ role.
- Every command works as `!name` and as a slash command ([commands](docs/source/commands.md)).
- Clip page: synced video, reorder and add tracks, lyrics from LRCLIB, listening stats, keyboard shortcuts, installable as an app, eight themes plus a custom one ([clip page](docs/source/clip-page.md)).
- Optional Last.fm scrobbling ([Last.fm](docs/source/lastfm.md)).
- English, French, Spanish and German, chosen per server with `!language`.
- Health check, optional Prometheus metrics, automatic backups.
- yt-dlp upgrades itself on start and a PO token sidecar handles YouTube's bot check ([keeping YouTube working](docs/source/youtube.md), [troubleshooting](docs/source/troubleshooting.md)).

Keyboard shortcuts, themes and more on the clip page: see [the clip page guide](docs/source/clip-page.md).

## Architecture

One Python process runs the `discord.py` bot and the clip page web server, with yt-dlp and ffmpeg for audio and video. A `pot-provider` sidecar supplies YouTube PO tokens. State lives in JSON files and SQLite databases under `DATA_DIR`. See [architecture](docs/source/architecture.md).

## Limits

- YouTube, SoundCloud and Bandcamp audio only. Spotify, Deezer and Apple Music links are matched to YouTube videos, so the match can be the wrong version of a song.
- Tracks are fully downloaded before they play, at most 720p. Playlists are capped by `MAX_PLAYLIST_SIZE` unless the requester picks the whole list.
- Age-restricted and members-only videos need YouTube cookies from a throwaway account.
- Anyone who has the control link can control the queue. Treat it as a secret.
- For personal use. Respect YouTube's Terms of Service and the rights of the people whose videos you play. The demo uses Creative Commons footage ([credits](docs/README.md#demo-footage-credits)).

## Status

Released as 1.x and used daily. YouTube breaks extractors often, so update regularly. The [changelog](CHANGELOG.md) lists every change.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, checks and translations, and [SECURITY.md](SECURITY.md) to report a vulnerability.

## License

MIT, see [LICENSE](LICENSE). Built on [discord.py](https://github.com/Rapptz/discord.py), [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [bgutil-ytdlp-pot-provider](https://github.com/Brainicism/bgutil-ytdlp-pot-provider).

djsnake is provided "as is", without warranty of any kind. The authors accept no liability for any damage or misuse.

## Support djsnake

djsnake is free and has no company behind it. If it saves you time, you can support its development:

- **GitHub Sponsors** (recurring or one-off): [github.com/sponsors/selfhostr](https://github.com/sponsors/selfhostr)
