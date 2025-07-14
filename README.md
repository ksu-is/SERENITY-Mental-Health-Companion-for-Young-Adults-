# SERENITY-Mental-Health-Companion-for-Young-Adults-
# Project Title: Serenity

**Author:** Victoria Ewoigbokhan  
**Course:** IS 3020 Application Development  
**Semester:** Summer 2025  

## Description

Young adulthood brings big life changes—moving out, starting college or a career, new relationships—and with them stress, anxiety, and sometimes depression. Many 18–25 year-olds hesitate to pursue traditional therapy due to stigma, cost, or scheduling conflicts. **Serenity** fills that gap with a confidential, on-demand mental health companion that:

- Listens empathetically via free-text or symptom selection.
- Offers evidence-based coping strategies (CBT exercises, guided breathing, grounding, mindfulness “mini-games”).
- Visualizes mood trends over time to help users spot triggers and celebrate progress.
- Connects users to professional resources (therapists, campus counseling, hotlines) via geolocation.
- Enables optional peer support through “Check-In Circles”: small groups share mood emojis and encouragement badges without exposing private journals.

By blending AI-driven conversation, self-guided tools, peer encouragement, and local referrals, Serenity empowers young adults to take charge of their mental well-being on their own terms.

## Target Audience

- **Primary:** Individuals aged 18–25 — college students, recent grads, early-career professionals seeking discreet, flexible support.  
- **Secondary:** Campus counselors & peer mentors looking to supplement in-person sessions; family members seeking tools for loved ones.

## Features

- **Conversational AI Chatbot:** Built on Rasa NLU & Core to understand free-form input and guide dialogue flows.
- **Mood Logging & Visualization:** Five-point mood scale + free-text journaling, plotted on an interactive timeline.
- **Coping Toolkit:** Save favorite exercises—breathing, grounding, guided imagery, quick mindfulness games—for one-tap access.
- **Check-In Circles:** Invite up to 4 friends to share mood emojis and send private “encouragement” badges.
- **Resource Hub:** Geolocated listings of licensed therapists, campus counseling centers, crisis hotlines with booking links.
- **Gamification & Reminders:** Streak tracking, customizable push notifications to encourage consistent check-ins.

## Technical Stack

- **Backend:** Python Flask REST API  
- **Database:** Encrypted SQLite for secure mood & journal storage  
- **Auth:** JWT-based authentication  
- **Chatbot Framework:** Rasa NLU & Core (runs on-device or via secure backend)  
- **Frontend:** React Native (iOS & Android support)
    

## How to Run

1. **Clone repo**  
   ```bash
   git clone https://github.com/yourusername/serenity.git
   cd serenity
