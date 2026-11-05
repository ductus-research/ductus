# Architecture

## Data flow

```
Tablet (capture app, browser)
  -> Azure Functions (session intake, study rules)
  -> Blob Storage (raw stylus traces, per study) + Cosmos DB (studies, sessions, metrics)
  -> Container Apps (signal processing with packages/metrics)
  -> Azure Machine Learning (session quality model)
  -> Researcher portal -> CSV export
```

## Azure services

| Service | Role |
|---|---|
| Static Web Apps | Capture app, researcher portal, presentation site |
| Functions | Session intake and study logic |
| Container Apps | Signal processing service |
| Blob Storage | Raw stylus traces, separated per study |
| Cosmos DB | Studies, sites, sessions, metrics |
| Entra External ID | Researcher accounts and roles |
| Machine Learning | Quality-control model, versioned metric runs |
| Key Vault | Keys and secrets |
| Application Insights | Monitoring and alerts |
| Log Analytics | Audit trail and incident investigation |

All resources are deployed in an EU region.

## Capture

The capture app uses the browser Pointer Events API, including `getCoalescedEvents()` where the
browser provides it, and records position, pressure, tilt and timestamp for every stylus sample.
Every tablet model must pass the device certification test (sampling rate, timing jitter, ruler
calibration) before it can be used in a study.
