# CHANGELOG

## [v0.14.1](https://github.com/JnyJny/busylight-core/releases/tag/v0.14.1) - 2025-07-25 03:17:53

## Changes since v0.12.0

- v0.14.1 (d5daa4c)
- v0.14.0 (459b4f6)
- v0.13.0 (f9bac30)
- docs(CHANGELOG): update release notes (5e64ef0)
- Merge pull request #16 from JnyJny/features/vendor-lights-classes (4aa867d)
- docs: update all documentation for vendor Lights classes (b676a52)
- test: add comprehensive tests for vendor Lights classes (ee27c3c)
- feat: add vendor-specific Lights classes for direct access (90177e7)
- feat: Updated busylight_core package with version information string. (9fdfde3)
- docs: Broken link in README.md (c693c38)
- docs: Consolidated development info in CONTRIBUTING.md (3054ab3)
- docs: Removed mute from Kuando in vendor/device table. (86ea9e0)
- docs: Wordsmithing the README (b6ae056)
- docs: Fixed doc URLs in README. s/advanced-features/features/ (c5fa708)
- docs: fix documentation links in README (41703a6)
- Merge pull request #15 from JnyJny/doc/comprehensive-documentation-improvements (0254345)
- docs: comprehensive documentation improvements and API reference enhancement (652ce8a)
- feature: added release method to busylight_core.light.Light (6bce0de)
- docs: removed nonfunctional fix for footnote rendering. (444f36c)
- Merge pull request #14 from JnyJny/ci/extract-python-versions-from-pyproject (8833e57)
- ci: Added toml tool dev dependency for extract python version testing matrix. (d90a202)
- docs: Update CONTRIBUTING.md for optimized release workflow (b0bcf28)
- docs: Document optimized release workflow in CLAUDE.md (0ad1067)
- docs: Document Python version configuration in workflows README (21b5aeb)
- feat: Add error handling for missing Python version config (aebb765)
- simplify: Remove unnecessary JSON conversion for Python versions (6866a0f)
- fix: Use consistent busylight_core naming in tool section (83b21b2)
- ci: Extract Python test matrix from pyproject.toml (3a89224)
- docs: Document workflow communication mechanism in README (fa02ff6)
- ci: Improve GitHub Actions workflow performance and reliability (47293bb)
- ci: Use pyproject.toml as source of truth for docs Python version (da17b4b)
- ci: Improve error handling in GitHub Pages auto-enablement (f3af74b)
- ci: Auto-enable GitHub Pages in docs workflow (5df171f)
- docs: Add GitHub Pages setup link to workflows README (e3ae0d4)
- docs: Remove irrelevant Jinja formatting section from workflows README (840d11b)
- ci: Use pyproject.toml as source of truth for build Python version (e66363a)
- Merge pull request #13 from JnyJny/ci/optimize-github-actions-workflow (e493911)
- docs: Update workflows README to reflect optimized architecture (ca8c844)
- ci: Optimize GitHub Actions workflow architecture (c5aa73f)
- docs: Optimize CLAUDE.md for token efficiency and objectivity (98f0627)
- Merge pull request #12 from JnyJny/refactor/standardize-exception-variable-names (f12098c)
- docs: Standardize exception variable names from 'e' to 'error' (5d6ff49)
- refactor: Standardize Light class caching to @cache decorator (e7fe6e3)
- docs(CHANGELOG): update release notes (5b5fced)
## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete release notes.


## What's Changed
* docs: Standardize exception variable names from 'e' to 'error' by @JnyJny in https://github.com/JnyJny/busylight-core/pull/12
* ci: Optimize GitHub Actions workflow architecture by @JnyJny in https://github.com/JnyJny/busylight-core/pull/13
* ci: Extract Python test matrix from pyproject.toml by @JnyJny in https://github.com/JnyJny/busylight-core/pull/14
* Comprehensive Documentation Improvements and API Reference Enhancement by @JnyJny in https://github.com/JnyJny/busylight-core/pull/15
* feat: add vendor-specific Lights classes for direct access by @JnyJny in https://github.com/JnyJny/busylight-core/pull/16


**Full Changelog**: https://github.com/JnyJny/busylight-core/compare/v0.12.0...v0.14.1

### Feature

- general:
  - add vendor-specific Lights classes for direct access ([90177e7](https://github.com/JnyJny/busylight-core/commit/90177e7065df833d231e07e506331885632ef968)) ([#16](https://github.com/JnyJny/busylight-core/pull/16))
  - Updated busylight_core package with version information string. ([9fdfde3](https://github.com/JnyJny/busylight-core/commit/9fdfde3706bc3ab53d90fca9eebfed99e72e8190))
  - feature: added release method to busylight_core.light.Light ([6bce0de](https://github.com/JnyJny/busylight-core/commit/6bce0de67a0ad5a63e510bf02494f2a95a97ebd2)) ([#15](https://github.com/JnyJny/busylight-core/pull/15))
  - Add error handling for missing Python version config ([aebb765](https://github.com/JnyJny/busylight-core/commit/aebb765ad6a660f6ea8fa90dd3eba9a333318208)) ([#14](https://github.com/JnyJny/busylight-core/pull/14))

### Bug Fixes

- general:
  - Use consistent busylight_core naming in tool section ([83b21b2](https://github.com/JnyJny/busylight-core/commit/83b21b295bb0f511780043013bb5dc5ec01d863c)) ([#14](https://github.com/JnyJny/busylight-core/pull/14))

### Documentation

- general:
  - update all documentation for vendor Lights classes ([b676a52](https://github.com/JnyJny/busylight-core/commit/b676a52e13d399e3f42eab25fb8b7fcf53a915b1)) ([#16](https://github.com/JnyJny/busylight-core/pull/16))
  - Broken link in README.md ([c693c38](https://github.com/JnyJny/busylight-core/commit/c693c38a2b9981df399a725f11af15cdad487952))
  - Consolidated development info in CONTRIBUTING.md ([3054ab3](https://github.com/JnyJny/busylight-core/commit/3054ab34d50b53ffbf2efb1d0eaae99fe02c0129))
  - Removed mute from Kuando in vendor/device table. ([86ea9e0](https://github.com/JnyJny/busylight-core/commit/86ea9e0c0246823c30f1655d145231b9dae93d12))
  - Wordsmithing the README ([b6ae056](https://github.com/JnyJny/busylight-core/commit/b6ae0563174fd41dc30b2cc02040f774eef0a049))
  - Fixed doc URLs in README. s/advanced-features/features/ ([c5fa708](https://github.com/JnyJny/busylight-core/commit/c5fa708fb596990620503a008f5af78b9c5ae8ff))
  - fix documentation links in README ([41703a6](https://github.com/JnyJny/busylight-core/commit/41703a65ac75a85f79b61845c4ec52b1974eb8da))
  - comprehensive documentation improvements and API reference enhancement ([652ce8a](https://github.com/JnyJny/busylight-core/commit/652ce8a522e0b29ce4e687a1de26a3c5991d7d84)) ([#15](https://github.com/JnyJny/busylight-core/pull/15))
  - removed nonfunctional fix for footnote rendering. ([444f36c](https://github.com/JnyJny/busylight-core/commit/444f36c5e662666148bcb18a1a57ddafb3cbfcc0)) ([#15](https://github.com/JnyJny/busylight-core/pull/15))
  - Update CONTRIBUTING.md for optimized release workflow ([b0bcf28](https://github.com/JnyJny/busylight-core/commit/b0bcf28b96ce93673dc6aafd33cbdd503ef85b36)) ([#14](https://github.com/JnyJny/busylight-core/pull/14))
  - Document optimized release workflow in CLAUDE.md ([0ad1067](https://github.com/JnyJny/busylight-core/commit/0ad1067b01204e66f69c357f6eb3861f0a45730a)) ([#14](https://github.com/JnyJny/busylight-core/pull/14))
  - Document Python version configuration in workflows README ([21b5aeb](https://github.com/JnyJny/busylight-core/commit/21b5aeb24402e6dacdfb472463cf3523a7ef9231)) ([#14](https://github.com/JnyJny/busylight-core/pull/14))
  - Document workflow communication mechanism in README ([fa02ff6](https://github.com/JnyJny/busylight-core/commit/fa02ff63d33133a9d7a8ed4f12b393c54f524b83))
  - Add GitHub Pages setup link to workflows README ([e3ae0d4](https://github.com/JnyJny/busylight-core/commit/e3ae0d468f64342b9ad70d565d9e1d05f5973127))
  - Remove irrelevant Jinja formatting section from workflows README ([840d11b](https://github.com/JnyJny/busylight-core/commit/840d11b929cef7996dcee53d4b33f69f7ebbdd15))
  - Update workflows README to reflect optimized architecture ([ca8c844](https://github.com/JnyJny/busylight-core/commit/ca8c84485d3cc1742e496a436dbb1b9089d6165d)) ([#13](https://github.com/JnyJny/busylight-core/pull/13))
  - Optimize CLAUDE.md for token efficiency and objectivity ([98f0627](https://github.com/JnyJny/busylight-core/commit/98f06275c5a954b088e3765a917c140a0b08cfca))
  - Standardize exception variable names from 'e' to 'error' ([5d6ff49](https://github.com/JnyJny/busylight-core/commit/5d6ff49f3c3263d10bd32e49f61e625152c06ff3)) ([#12](https://github.com/JnyJny/busylight-core/pull/12))

### Refactor

- general:
  - Standardize Light class caching to @cache decorator ([e7fe6e3](https://github.com/JnyJny/busylight-core/commit/e7fe6e33a6641649d16a0d2bb663733e103f3b01))

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
