# MyPowerHouse

Read-only energy insight integration for Home Assistant, designed for a Powerwall/Teslemetry and Octopus setup.

## Version 0.1.0

* Live solar, home, grid and battery measurements
* Import and export tariff display
* A safety-first recommendation that never controls equipment
* A starter Lovelace dashboard

## Install through HACS

1. Create a GitHub repository from this folder and name it `mypowerhouse`.
2. In Home Assistant, open HACS → Integrations → the three-dot menu → Custom repositories.
3. Add the GitHub repository URL, choosing **Integration** as the category.
4. Search HACS for **MyPowerHouse**, install it, then restart Home Assistant.
5. Go to Settings → Devices & services → Add integration → **MyPowerHouse**.
6. Select the existing sensor entities that represent solar power, home consumption, grid power, battery power, battery percentage, and your current Octopus import/export rates.
7. Copy `dashboards/mypowerhouse.yaml` into a new YAML dashboard, or recreate the included cards in your preferred dashboard editor.

## Important setup note

Powerwall and tariff integrations vary in their sign conventions. In this first release, positive grid power means import and positive battery power means discharge. Verify those readings against your existing Energy dashboard before relying on recommendations.

## Roadmap

The next release will add hourly cost and export-income calculations, Octopus price forecasts and EV-aware recommendations. Automatic control remains disabled until an explicit opt-in release.
