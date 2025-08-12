# CHANGELOG

## [v0.15.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.15.0) - 2025-07-31 20:10:08

## Changes since v0.14.1

- v0.15.0 (930462b)
- Merge pull request #22 from JnyJny/features/kuando-keepalive-threading-fallback (a12de10)
- docs: remove unnecessary Kuando-specific section from CLAUDE.md (b6c590f)
- docs: remove keepalive mentions from user documentation (1fcfd94)
- docs: update documentation for TaskableMixin and Kuando keepalive (d552aac)
- style: ruff formatting cleanup (662176c)
- fix: add missing interval parameter for periodic keepalive (4aa03f0)
- refactor: simplify Kuando keepalive implementation (f5695ed)
- feat: add threading fallback for TaskableMixin (663ba9a)
- bug: Some serial devices have None for vendor or product IDs (665cb26)
- feat: add new device support request issue template (7778b86)
- Merge pull request #20 from JnyJny/docs/update-issue-template-version-info (25a6573)
- docs: update issue templates with correct version commands (7bfeca3)
- test: add version attribute validation tests (86c6ac1)
- Merge pull request #19 from JnyJny/docs/api-reference-navbar (b70e98e)
- docs: add Implementation links to vendor API reference navigation (d6c77a9)
- Merge pull request #18 from JnyJny/refactor/vendor-implementation-modules (61ea2b0)
- refactor: restructure vendor implementations into logical modules (25b16d7)
- Merge pull request #17 from JnyJny/docs/api-reference-updates (140ee7f)
- docs: restructure API reference documentation (603e01a)
- bug: accidently commited working file (a9a089d)
## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete release notes.


## What's Changed
* Restructure API reference documentation by @JnyJny in https://github.com/JnyJny/busylight-core/pull/17
* Refactor vendor implementations into logical modules by @JnyJny in https://github.com/JnyJny/busylight-core/pull/18
* Add Implementation links to vendor API reference navigation by @JnyJny in https://github.com/JnyJny/busylight-core/pull/19
* Update issue templates with correct version commands by @JnyJny in https://github.com/JnyJny/busylight-core/pull/20
* Threading fallback for Kuando keepalive compatibility by @JnyJny in https://github.com/JnyJny/busylight-core/pull/22


**Full Changelog**: https://github.com/JnyJny/busylight-core/compare/v0.14.1...v0.15.0

### Feature

- general:
  - add threading fallback for TaskableMixin ([663ba9a](https://github.com/JnyJny/busylight-core/commit/663ba9ad1d38a97a9e840cf883e6130fa7bd248d)) ([#22](https://github.com/JnyJny/busylight-core/pull/22))
  - add new device support request issue template ([7778b86](https://github.com/JnyJny/busylight-core/commit/7778b86dd6af4fb20fbf4a82e5b5d57adc4a9957))

### Bug Fixes

- general:
  - Some serial devices have None for vendor or product IDs ([665cb26](https://github.com/JnyJny/busylight-core/commit/665cb266c1b9968199c13a13d253054dfe763c68))
  - accidently commited working file ([a9a089d](https://github.com/JnyJny/busylight-core/commit/a9a089d45060fe2b3df342c71fd6d259b0ce0e84))

### Bug Fixes

- general:
  - add missing interval parameter for periodic keepalive ([4aa03f0](https://github.com/JnyJny/busylight-core/commit/4aa03f005173ba76d9b65860a5602a2db0c7faa0)) ([#22](https://github.com/JnyJny/busylight-core/pull/22))

### Documentation

- general:
  - remove unnecessary Kuando-specific section from CLAUDE.md ([b6c590f](https://github.com/JnyJny/busylight-core/commit/b6c590fa299ee41915412d0bf4bdfc9d2136a332)) ([#22](https://github.com/JnyJny/busylight-core/pull/22))
  - remove keepalive mentions from user documentation ([1fcfd94](https://github.com/JnyJny/busylight-core/commit/1fcfd9408d7ceb3a514830e7a11e1837392a9a53)) ([#22](https://github.com/JnyJny/busylight-core/pull/22))
  - update documentation for TaskableMixin and Kuando keepalive ([d552aac](https://github.com/JnyJny/busylight-core/commit/d552aacecdb41c1ecdbe4c763edc383fb868342d)) ([#22](https://github.com/JnyJny/busylight-core/pull/22))
  - update issue templates with correct version commands ([7bfeca3](https://github.com/JnyJny/busylight-core/commit/7bfeca37bf71b9265eb87b886eee80cf91774d22)) ([#20](https://github.com/JnyJny/busylight-core/pull/20))
  - add Implementation links to vendor API reference navigation ([d6c77a9](https://github.com/JnyJny/busylight-core/commit/d6c77a92374d39c1bab8731339eb8377739e668d)) ([#19](https://github.com/JnyJny/busylight-core/pull/19))
  - restructure API reference documentation ([603e01a](https://github.com/JnyJny/busylight-core/commit/603e01a606b1d37f55fc3a4b2e0a00da661cff40)) ([#17](https://github.com/JnyJny/busylight-core/pull/17))

### Refactor

- general:
  - simplify Kuando keepalive implementation ([f5695ed](https://github.com/JnyJny/busylight-core/commit/f5695ede2669fef298d4d28776f9f39e7c4dcdff)) ([#22](https://github.com/JnyJny/busylight-core/pull/22))
  - restructure vendor implementations into logical modules ([25b16d7](https://github.com/JnyJny/busylight-core/commit/25b16d7ee5a565146f9921f678f505dd5ef8886e)) ([#18](https://github.com/JnyJny/busylight-core/pull/18))

## [v0.14.1](https://github.com/JnyJny/busylight-core/releases/tag/v0.14.1) - 2025-07-25 03:17:53

## [v0.12.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.12.0) - 2025-07-22 20:27:29

## [v0.9.2](https://github.com/JnyJny/busylight-core/releases/tag/v0.9.2) - 2025-07-22 16:15:24

## [v0.9.1](https://github.com/JnyJny/busylight-core/releases/tag/v0.9.1) - 2025-07-22 01:20:47

## [v0.8.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.8.0) - 2025-07-20 23:20:05

## [v0.6.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.6.0) - 2025-07-20 19:54:09

## [v0.5.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.5.0) - 2025-07-19 22:47:18

## [v0.4.1](https://github.com/JnyJny/busylight-core/releases/tag/v0.4.1) - 2025-07-18 20:08:10

## [v0.4.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.4.0) - 2025-07-18 17:42:19

## [v0.3.5](https://github.com/JnyJny/busylight-core/releases/tag/v0.3.5) - 2025-07-18 15:08:53

## [v0.3.3](https://github.com/JnyJny/busylight-core/releases/tag/v0.3.3) - 2025-07-17 17:36:57

## [v0.3.2](https://github.com/JnyJny/busylight-core/releases/tag/v0.3.2) - 2025-07-17 14:56:16

## [v0.3.0](https://github.com/JnyJny/busylight-core/releases/tag/v0.3.0) - 2025-07-16 23:34:43

## [v0.2.4](https://github.com/JnyJny/busylight-core/releases/tag/v0.2.4) - 2025-07-13 20:33:04

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*
