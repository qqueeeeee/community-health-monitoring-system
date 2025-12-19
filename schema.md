# Event Schema

This document describes the event-level data schema used in the Community Behavior Intelligence System.
The schema is designed to store raw behavioral events in a format that supports time-series analysis,
feature engineering, drift detection, and predictive modeling.

## Design Principles

- All data is stored as immutable events
- Events are timestamped in UTC
- Raw events are stored without aggregation
- Personally identifiable or sensitive data is intentionally excluded

## Universal Event Structure

Each event in the system follows a common structure:

| Field Name | Description |
|----------|-------------|
| event_id | Unique identifier for the event |
| event_type | Type of event (e.g. message_sent) |
| event_time | Timestamp when the event occurred (UTC) |
| user_id | Hashed identifier of the user who triggered the event |
| channel_id | Identifier of the channel where the event occurred (nullable) |
| target_user_id | Identifier of the affected user, if applicable (nullable) |
| metadata | JSON object containing event-specific attributes |

## Event Types

### message_sent
**event_type:** message_sent
Represents a user sending a message in a public channel.

**Key characteristics:**
- One event per message
- Message content is not stored
- Used as the primary signal for engagement analysis

**Metadata fields:**
These fields capture behavioral characteristics of messages without storing content.
- content_length
- has_embed
- has_attachment
- is_interaction_command

## Source Data Mapping

The following table shows how raw dataset fields map to the event schema.

| Schema Field | Source Column | Notes |
|-------------|---------------|------|
| event_id | _id | Unique MongoDB document ID |
| user_id | author | Will be hashed before use |
| channel_id | channelId | Public channels only |
| event_time | createTimestamp | Epoch milliseconds |

## Explicit Exclusions

The following data is intentionally not collected or stored:
- Message text or content
- Private messages or DMs
- Usernames or profile information
- IP addresses or location data

## Notes and Assumptions

- Additional event types (e.g. reactions, joins, leaves) will follow the same universal schema
- All timestamps are stored in UTC
- User identifiers are anonymized before analysis
- Deleted or edited messages are preserved as metadata and may be expanded into separate events later
