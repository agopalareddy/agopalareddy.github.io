---
date: 2025-08-11
title: "Google Calendar Availability Sync"
collection: projects
permalink: /projects/2025-08-google-calendar-sync
excerpt: "A Google Apps Script that automatically syncs events from multiple source calendars to a single 'Availability' calendar, creating customizable availability blocks while preserving privacy."
venue: "Personal Project"
last_modified_at: 2026-02-10 00:00:00
---

A Google Apps Script to automatically sync events from multiple source calendars to a single "Availability" calendar. This script creates customizable availability blocks (e.g., "Personal", "Work", "Class") based on the source calendar, allowing you to share your availability without revealing the private details of your appointments.

### Features

- **One-Way Sync**: Copies events from multiple source calendars to one destination calendar
- **Privacy-Focused**: Creates customizable events, hiding original titles, descriptions, and guest lists while showing relevant availability context
- **Per-Calendar Event Naming**: Assigns custom event titles based on the source calendar (e.g., "Personal", "Work", "Class") instead of generic "Busy" titles
- **Automatic Title Updates**: Gradually updates existing event titles to match new naming configurations without hitting API rate limits
- **Robust Reconciliation**: Accurately creates and deletes events, preventing duplicate or orphaned entries
- **Automatic Deletion**: Removes availability blocks when the original event is deleted or rescheduled
- **Manual Event Protection**: Allows manually added events on the destination calendar without script interference
- **Automatic Nightly Reset**: Sync cursor resets every morning, ensuring long-term accuracy

### How It Works

1. Configure your source calendars (personal, work, school, etc.)
2. Create a destination "Availability" calendar
3. The script syncs events every 15-30 minutes via Google Apps Script triggers
4. Share the public URL or iCal address of your availability calendar with others

### Technologies Used

- Google Apps Script
- JavaScript
- Google Calendar API

### GitHub Repository

[View the project on GitHub](https://github.com/agopalareddy/GoogleCalendarSync)
