# API (Azure Functions)

Receives sessions from the capture app, checks them against the study configuration,
stores raw traces in Blob Storage and session records in Cosmos DB, and triggers metric computation.

Local settings go in `local.settings.json`, which is git-ignored.
