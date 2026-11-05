# Data policy

Ductus Research handles motor data that, in real studies, is health data under GDPR art. 9.
These rules apply to everyone working in this repository.

1. **No real participant data in Git.** Not in commits, issues, pull requests or screenshots.
2. **Development uses synthetic data** or public datasets whose licence allows it. Note the source and licence next to any fixture.
3. **Volunteer test data** (team members, healthy volunteers) is stored only in the project's Azure storage in an EU region, never on personal laptops or in this repository.
4. **Participants are identified only by pseudonymous codes.** The link between code and identity never enters the platform.
5. **Secrets** (connection strings, keys) live in Azure Key Vault or local `.env` files that are git-ignored. Commit only `.env.example` with placeholder values.
6. If something sensitive is committed by mistake, tell the team immediately. Deleting it in a new commit is not enough, because it stays in the history.
