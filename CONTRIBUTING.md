# Contributing

## Workflow

1. Pick or create an issue on the project board and assign yourself.
2. Create a branch from an up-to-date `main`:
   ```bash
   git switch main
   git pull
   git switch -c feat/short-name
   ```
3. Commit small, focused changes:
   ```bash
   git add <files>
   git commit -m "capture: record coalesced pointer events"
   ```
   Message format: `<area>: <what changed>` where area is `capture`, `portal`, `api`, `dsp`, `metrics`, `infra`, `site` or `docs`.
4. Push and open a pull request:
   ```bash
   git push -u origin feat/short-name
   ```
5. At least one other team member reviews and approves. The author merges (squash merge).
6. Delete the branch after merging.

## Rules

- No direct pushes to `main`.
- No real participant data, secrets or keys in the repository, ever. Use synthetic data or public datasets with their licence noted.
- Any change to a metric definition in `packages/metrics` bumps its version and is noted in the changelog.
- Keep each folder's `README.md` up to date with how to run that component.
