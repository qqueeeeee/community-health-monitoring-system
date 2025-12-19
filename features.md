## User-Level Features

### Active Days (7-day window)
Measures the number of distinct days a user is active within a rolling 7-day window.
This helps distinguish recurring participation from one-time or burst-driven activity.

### Return Rate
Measures how often a user returns in consecutive time windows after being active.
Lower return rates indicate higher risk of disengagement.

### Median Inter-Message Gap
Measures the typical time gap between a user’s messages.
Helps identify spam-like bursts versus conversational behavior.

### Engagement Lifespan
Time between a user’s first and most recent recorded message.
Short lifespans often indicate early disengagement or failure to integrate into the community.

### Burstiness Score
Measures whether a user’s activity is concentrated in short, high-volume bursts rather than spread over time.
High burstiness is often associated with non-sustained engagement.

## Churn Definition

A user is considered churned if they have no recorded activity for 14 consecutive days.
This threshold balances short breaks with long-term disengagement.

## Community-Level Features

### Returning User Ratio
Measures the proportion of users active in the previous time window who return in the current window.
A declining ratio indicates weakening engagement and reduced community stickiness.

### Core User Concentration
Measures the percentage of total messages contributed by the top fraction of users (e.g., top 10%).
High concentration suggests over-reliance on a small core and reduced participation diversity.

### Activity Volatility
Measures how sharply total activity changes across consecutive time windows.
High volatility often reflects unstable engagement driven by short-lived events rather than sustained participation.

