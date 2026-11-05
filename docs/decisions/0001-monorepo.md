# 0001. One repository for the whole project

- Status: accepted
- Date: 2026-11-06

## Context

The project has a capture app, a researcher portal, backend services, a metric library,
infrastructure and a presentation site, built by a team of four.

## Decision

Keep everything in one repository (`ductus-research/ductus`), one top-level folder per component.

## Consequences

- One place for issues, the project board and reviews.
- Changes that touch several components (for example the session JSON format) land in one pull request.
- Each component keeps its own README and, where needed, its own CI workflow filtered by path.
