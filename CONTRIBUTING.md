# Contributing

Thanks for helping improve the songwriting knowledge base. The full community guide is
[SOP 08 — Contributing](.kiro/sops/08-contributing.md): what we accept, what we don't, how to
personalise the repo, and how to add an album. This page is the short version.

## Ground rules

- **One source of truth.** Methods live in `core/methodology/`. Steering, SOPs, skills and agents
  summarise them or point to them; they don't redefine them. Fix the canonical file first.
- **Label evidence.** Factual claims carry a tier: `[Tier 1]` scholarship with a primary source,
  `[Tier 2]` professional craft heuristic, `[Tier 3]` community/platform observation (unverified,
  version-dependent). Suno findings are Tier 3 until logged in `experiments/suno/` across 3+ songs.
- **Suno versions.** V6 is the default. Label v5.5-era behaviour as legacy and re-validate it on V6.
- **No personal content in universal files.** Personal preferences belong in `examples/preferences/`,
  `.kiro/steering/output-preferences.md`, or your own album folder.
- **Paraphrase sources.** Don't paste long passages from books or websites; credit them in `CREDITS.md`.

## Workflow

1. Branch from `main`: `contribution/<your-addition>` (external contributors) or a descriptive
   `feature/…`, `fix/…`, `docs/…`, `song/…` branch.
2. Make your change and run the checks:
   ```bash
   python3 -m unittest discover -s tests       # tool tests
   python3 tools/check-repo.py                 # include/resource paths, hooks, steering, skills, JSON
   python3 tools/validate-song.py examples/songs/ songs/   # no FAIL allowed
   python3 tools/lyric-lint.py songs/<file>.md # advisory prosody / rhyme readout
   ```
   Optional: `pip install -r tools/requirements-optional.txt` for dictionary-accurate lyric-lint.
3. Use conventional commit messages (`feat: …`, `fix: …`, `docs: …`, `chore: …`).
4. Open a pull request against `main`, describing what changed and why. CI runs the same checks.

## Kiro file conventions

- **Hooks:** Kiro v1 JSON in `.kiro/hooks/*.json` (`version: "v1"`, `hooks[]` with `trigger`,
  optional `matcher`, `action` of type `command` or `agent`). Kiro has no manual hooks: on-demand
  workflows are steering files with `inclusion: manual`.
- **Steering:** front matter must be the first bytes of the file. `inclusion` is `always`, `auto`
  (needs `name` + `description`), `fileMatch` (needs `fileMatchPattern`) or `manual`.
  `#[[file:path]]` includes work in steering files.
- **Agents:** load files with `resources:` (`file://…`) in the front matter, not `#[[file:]]`.
- **Skills:** `name` must match the folder; reference supporting files by plain path with an
  explicit "read X" instruction.
