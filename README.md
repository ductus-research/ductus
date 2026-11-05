# Ductus Research

Pen-kinematics measurement platform for clinical research teams in psychiatry and neurology.
Standardized drawing tasks run in the browser on ordinary stylus tablets and produce comparable
motor measures across sites, devices and visits.

> **Research use only.** Not a medical device. Not intended for diagnosis or treatment decisions.

## Repository structure

| Folder | What lives here | Owner (role) |
|---|---|---|
| `apps/capture` | Browser capture app (PWA): tasks, stylus capture, device certification | Pen capture and tablet app |
| `apps/portal` | Researcher portal: studies, sessions, replay, CSV export | Portal and partners |
| `services/api` | Azure Functions: session intake, study logic | Cloud and backend |
| `services/dsp` | Signal processing service (Container Apps), uses `packages/metrics` | Data and signal processing |
| `packages/metrics` | Open-source metric library (Python), versioned definitions | Data and signal processing |
| `infra` | Azure infrastructure as code (Bicep) | Cloud and backend |
| `site` | Public presentation website (ductus-research.com) | Portal and partners |
| `docs` | Architecture, decisions, data policy, protocol notes | Everyone |

## Getting started

```bash
git clone https://github.com/ductus-research/ductus.git
cd ductus
```

Each folder has its own `README.md` with setup steps once that component exists.

### Metric library (Python)

```bash
cd packages/metrics
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

## How we work

- `main` is protected: every change goes through a pull request reviewed by another team member.
- Branch names: `feat/<short-name>`, `fix/<short-name>`, `docs/<short-name>`.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.
- **Never commit real participant data.** See [docs/data-policy.md](docs/data-policy.md).

## Links

- Website: https://www.ductus-research.com
- Contact: see the website

## License

[MIT](LICENSE)
