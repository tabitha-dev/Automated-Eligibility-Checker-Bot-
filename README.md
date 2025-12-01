<!-- Modern README with badges, clean layout, and full project details -->

<div align="center">

# NexGen RCM Intelligence  
AI Powered Healthcare Automation Suite

[![Live Demo](https://img.shields.io/badge/Demo-Open%20App-blue?style=for-the-badge)](https://tabitha-dev.github.io/Automated-Eligibility-Checker-Bot-/)
![Status](https://img.shields.io/badge/Project-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)
![Made With](https://img.shields.io/badge/Frontend-JavaScript-orange?style=for-the-badge)
![Health Tech](https://img.shields.io/badge/Domain-Healthcare-blue?style=for-the-badge)

**Repository**  
`tabitha-dev / Automated-Eligibility-Checker-Bot-`

</div>

---

## Contents

1. Overview  
2. Live demo  
3. Features  
4. Architecture  
5. Tech stack  
6. Getting started  
7. Python automation bot  
8. Project structure  
9. Demo walkthrough  
10. Author  

---

## Overview

NexGen RCM Intelligence is a modern simulation of a full scale Revenue Cycle Management platform. It replicates the workflows used in hospitals and medical practices for insurance eligibility checks, AI medical coding, claims adjudication, denial management, and payer communication.

The system is fully browser based, powered by Tailwind and vanilla JavaScript, and uses a self driving automation engine to simulate real backend behavior. It includes a Python Selenium bot that can automate eligibility checks like a real RPA robot.

Live demo  
https://tabitha-dev.github.io/Automated-Eligibility-Checker-Bot-/

---

## Features

### AI clinical coding and OCR simulation

- Extracts medical concepts from physician style notes  
- Auto assigns ICD diagnosis codes and CPT procedure codes  
- Shows confidence scoring meters  
- Drag and drop simulated OCR for PDF or fax extraction  
- Sends extracted data into downstream eligibility and claims flows  

### Real time eligibility bot (EDI 270 and 271)

- Multi payer support including Medicare, Aetna, Medicaid, Anthem, Cigna, UHC, Humana, Kaiser  
- Generates simulated ANSI X12 EDI traffic  
- Displays plan structure, deductible, copay, coinsurance, OOP max  
- CPT scrubber highlights risk, mismatch, missing authorization  
- Patient 360 metrics include RAF score, SDoH flags, care gaps, propensity to pay, and appeal win probability  

### Voice AI agent

- Simulated IVR payer calls  
- Real time transcript panel  
- Audio wave animation  
- Extracts benefit data and syncs into eligibility  

### Claims and denial management

- Tracks claims across adjudication stages  
- Displays denial rate and AR health  
- Generates AI powered payer appeal letters  
- Supports denial codes such as CO 16 and CO 50  

### Enterprise engineering features

- Simulated SSO login  
- HIPAA Privacy Shield masking for PHI  
- Network Monitor panel for REST and EDI events  
- NexGen Copilot floating AI widget  
- Tailwind based enterprise design system  

---

## Architecture

### Frontend portal

- Static HTML  
- Vanilla JavaScript logic  
- Tailwind CSS  
- Chart.js analytics  
- QRCode.js integration  
- Backend logic simulated via async functions, latency, retries, and structured mock data  

### Automation bot

- Python three  
- Selenium WebDriver  
- webdriver manager  
- Scrapes payer results and outputs structured JSON  

---

## Tech stack

### UI

- HTML  
- JavaScript  
- Tailwind CSS  
- Chart.js  
- Font Awesome  
- QRCode.js  

### Automation

- Python  
- Selenium  
- webdriver manager  
- JSON report export  

---

## Getting started

### Option A  hosted demo

Visit  
https://tabitha-dev.github.io/Automated-Eligibility-Checker-Bot-/

Use Sign In via SSO, Run Automation, and Developer Mode to explore.

### Option B  run locally

Clone the repo

```bash
git clone https://github.com/tabitha-dev/Automated-Eligibility-Checker-Bot-.git
cd Automated-Eligibility-Checker-Bot-
```

Serve locally

```bash
npx serve .
# or
python -m http.server 8000
```

Visit  
http://localhost:8000

---

## Python automation bot

Install dependencies

```bash
pip install selenium webdriver-manager
```

Run

```bash
python eligibility_bot.py
```

The bot will open the portal, run eligibility checks, scrape results, and save `eligibility_report.json`.

---

## Project structure

```text
Automated-Eligibility-Checker-Bot-/
  index.html
  eligibility_bot.py
  eligibility_report.json
  assets/
```

---

## Demo walkthrough

### Recommended flow for recruiters or engineering leads

1. Show SSO login  
2. Run multi patient automation batch  
3. Open Developer Mode to show API and EDI logs  
4. Demonstrate AI clinical coder  
5. Show Voice AI call transcript  
6. Walk through denial analytics and appeal generation  
7. Explain architecture and Selenium automation  

---

## Author

**Tabitha Khadse**

GitHub  
https://github.com/tabitha-dev

LinkedIn  
https://www.linkedin.com/in/tabitha-dev/

Focus areas  
health tech engineering  
revenue cycle automation  
frontend systems design  
enterprise simulation  
ai assisted medical operations
