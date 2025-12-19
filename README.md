# Community Health Monitoring System

A data-driven system for monitoring the health of an online community using real Discord message metadata. The project models **engagement quality over time** rather than raw activity volume, focusing on user retention, recurring participation, and early warning signals of disengagement.

---

## Project Overview

Most community analytics focus on message counts or daily activity, which can be misleading. A server can appear active while slowly losing its core users. This project addresses that gap by tracking **weekly retention behavior** and translating it into interpretable health states.

---

## Data Source

* Real Discord server data (admin-authorized)
* ~6 months of message metadata (~8,000 messages)
* Data collected via a Discord bot using the official Discord API

### Stored Fields (Metadata Only)

* Message timestamp (UTC)
* User ID (anonymized during analysis)
* Channel ID
* Message length
* Presence of embeds or attachments

**No message content, DMs, or private data are stored.**

---

## Methodology

### 1. Weekly Aggregation

All analysis is performed at a **weekly resolution** to reduce noise and reflect realistic engagement cycles in low-to-medium activity communities.

Computed metrics:

* Weekly message count
* Weekly active users
* Weekly returning users

---

### 2. Returning User Ratio (Core Metric)

The primary health signal is the **Returning User Ratio**:

> Returning users this week ÷ Active users last week

This measures how many community members come back consistently, rather than how loud the server is.

---

### 3. Health Classification

Each week is classified into one of three health states based on retention:

* **Healthy**: Returning User Ratio ≥ 0.40
* **Warning**: 0.25 ≤ Ratio < 0.40
* **Critical**: Ratio < 0.25

These thresholds are intentionally simple, interpretable, and adjustable.

---

## Example Insights

* Early growth phase showed increasing retention as the community formed
* Middle period stabilized around a consistent returning user base
* Later weeks revealed **retention collapse despite activity**, indicating engagement driven by short-lived events rather than sustained participation

This distinction would not be visible using message counts alone.

---

## Project Structure

```
community-health-monitoring/
├── data/
│   └── discord_messages.csv
├── notebooks/
│   └── analysis.ipynb
├── scripts/
│   └── discord_collector.py
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* pandas
* matplotlib
* Discord API (discord.py)

---

## Why This Project Matters

This project demonstrates:

* Working with messy, real-world data
* Time-based behavioral analysis
* Retention-focused thinking
* Tradeoff-aware system design
* Avoidance of unnecessary overengineering

It is designed to reflect how engagement analytics are handled in real communities, products, and platforms.

---

## Future Extensions (Optional)

* User-level churn risk flags
* Drift detection on retention trends
* Moderator-facing alerts
* Cross-channel engagement analysis

---

## Ethical Considerations

* No message content stored or analyzed
* No private channels or DMs collected
* Analysis performed at an aggregate level
* Data used strictly for community health insights

---

## Author

Built as an applied data science project focused on real-world behavioral analysis and interpretability.
