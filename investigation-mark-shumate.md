# Investigation Plan: Mark Tristan Shumate
## Automated Skip Tracing & Address Location

**Investigation ID:** `INV-2026-05-14-SHUMATE`  
**Date Initiated:** 2026-05-14  
**Primary Investigator:** PI Intelligence Platform  
**Automation Framework:** browser-harness (browser-use/browser-harness)  
**Status:** 🟡 IN PROGRESS

---

## 📋 SUBJECT INFORMATION

### Known Details
| Field | Value | Confidence | Source |
|-------|-------|------------|--------|
| **Full Legal Name** | Mark Tristan Shumate | ✅ Confirmed | Real Estate Transaction |
| **Approximate Age** | 59 years old (as of 2026) | ✅ Confirmed | Client Information |
| **Date of Birth** | ~1967 (calculated) | 🟡 Estimated | Age Calculation |
| **Last Known Address** | 3304 NE 15th Court, Fort Lauderdale, FL 33304 | ✅ Confirmed | Property Sale |
| **County** | Broward County, Florida | ✅ Confirmed | Property Records |
| **Last Known Status** | Property Seller (Former Resident) | ✅ Confirmed | Real Estate Transaction |
| **Occupation** | Likely Real Estate Broker | 🟡 Unconfirmed | Context Clue |

### Known Aliases
- Mark T. Shumate
- Mark Shumate
- M. Tristan Shumate
- M.T. Shumate

### Investigation Objective
**PRIMARY GOAL:** Locate current home address for Mark Tristan Shumate in or around Fort Lauderdale, Florida (Broward County).

**CONTEXT:** Subject sold property at 3304 NE 15th Court, Fort Lauderdale, FL. This address still appears online as his residence, but it is the property he sold. Need to find his current address post-sale.

---

## 🎯 INVESTIGATION STRATEGY

### Approach
1. **Start with free public records** (Property, Court, Voter)
2. **Use free people search aggregators** (TruePeopleSearch, That's Them, FastPeopleSearch)
3. **Leverage Florida's Sunshine Law** for excellent public records access
4. **Automate data collection** using browser-harness
5. **Cross-reference all findings** for verification
6. **Document everything** with timestamps and sources
7. **Escalate to paid tools** only if free resources insufficient

### Estimated Timeline
- **Phase 1-3 (Free Resources):** 45-90 minutes
- **Phase 4 (Verification):** 15-30 minutes
- **Phase 5 (Paid Upgrade if needed):** 10 minutes

---

## 🤖 AUTOMATION SETUP

### Prerequisites
```bash
# Install browser-harness
git clone https://github.com/browser-use/browser-harness.git
cd browser-harness
# Follow install.md for setup

# OR use uv for quick install
uv init && uv add browser-use && uv sync
```

### Browser-Harness Configuration
```python
# investigation_config.py
SUBJECT = {
    "full_name": "Mark Tristan Shumate",
    "age": 59,
    "last_known_address": "3304 NE 15th Court, Fort Lauderdale, FL 33304",
    "county": "Broward County",
    "state": "Florida"
}

# Search variations
SEARCH_NAMES = [
    "Mark Tristan Shumate",
    "Mark T Shumate",
    "Mark Shumate",
    "M Tristan Shumate"
]

# Free resources to query
FREE_RESOURCES = [
    "bcpa.net",  # Broward County Property Appraiser
    "browardclerk.org",  # Broward County Clerk of Courts
    "truepeoplesearch.com",
    "thatsthem.com",
    "fastpeoplesearch.com",
    "judyrecords.com"
]
```

---

## 📊 PHASE 1: PROPERTY RECORDS (FREE)

### 1.1 Broward County Property Appraiser

**Resource:** https://bcpa.net  
**Automation Priority:** 🔴 HIGH  
**Expected Data:** Current property ownership, transfer dates, mailing addresses

#### Manual Steps (Browser-Harness Automation)
```python
# Phase 1.1: Broward County Property Appraiser Search
browser-harness -c '''
new_tab("https://bcpa.net")
wait_for_load()

# Navigate to property search
# Look for "Property Search" or similar link
capture_screenshot()  # Verify page loaded

# Search by owner name: "Mark Shumate" or "Mark T Shumate"
# Fill search form and submit
# Extract results:
# - Property ownership records
# - Purchase/sale dates
# - Current mailing address (if different from property)
# - New property purchases since 3304 NE 15th sale

print(page_info())
'''
```

#### Expected Findings
- [ ] Current properties owned by Mark Shumate in Broward County
- [ ] Sale date of 3304 NE 15th Court
- [ ] New property purchases post-sale
- [ ] Mailing address on file
- [ ] Property tax records

#### Data Collection Template
```markdown
### Property Records Results
**Search Date:** [TIMESTAMP]
**Source:** Broward County Property Appraiser (bcpa.net)

#### Current Properties Owned:
1. Address: 
   - Purchase Date: 
   - Property Value: 
   - Mailing Address: 

#### Historical Records:
1. 3304 NE 15th Court, Fort Lauderdale, FL 33304
   - Sale Date: 
   - Sale Price: 
   - Buyer: 
```

---

## 📊 PHASE 2: FREE PEOPLE SEARCH TOOLS

### 2.1 TruePeopleSearch.com (Priority #1)

**Resource:** https://www.truepeoplesearch.com  
**Automation Priority:** 🔴 HIGH  
**Expected Data:** Current address, phone numbers, known relatives

#### Browser-Harness Script
```python
# Phase 2.1: TruePeopleSearch
browser-harness -c '''
new_tab("https://www.truepeoplesearch.com")
wait_for_load()
capture_screenshot()

# Search form: Name + Location
# Input: "Mark Shumate" + "Florida"
# Age filter: 55-63 range

# Extract results:
# - Current address(es)
# - Phone numbers
# - Email addresses
# - Known relatives/associates
# - Address history

# Screenshot all results
# Save to: screenshots/truepeoplesearch_[timestamp].png
'''
```

#### Data Collection Template
```markdown
### TruePeopleSearch Results
**Search Date:** [TIMESTAMP]
**Source:** truepeoplesearch.com

#### Primary Result:
- **Current Address:** 
- **Previous Addresses:** 
  - 3304 NE 15th Court, Fort Lauderdale, FL 33304 (Confirmed)
  - [Additional addresses]
- **Phone Numbers:**
  - Mobile: 
  - Landline: 
- **Email Addresses:**
- **Known Relatives:**
- **Associates:**
```

### 2.2 That's Them (Priority #2)

**Resource:** https://thatsthem.com  
**Automation Priority:** 🟡 MEDIUM  
**Expected Data:** Multiple search vectors (name, address, phone, email, VIN)

#### Browser-Harness Script
```python
# Phase 2.2: That's Them
browser-harness -c '''
new_tab("https://thatsthem.com")
wait_for_load()

# Multiple search strategies:
# 1. Name search: "Mark Shumate" + "Florida"
# 2. Reverse address search: "3304 NE 15th Court Fort Lauderdale"
#    (to verify who bought the property)
# 3. Cross-reference results

# Extract:
# - Current address
# - Forwarding address (if available)
# - Associated emails
# - Phone numbers
'''
```

#### Data Collection Template
```markdown
### That's Them Results
**Search Date:** [TIMESTAMP]
**Source:** thatsthem.com

#### Name Search Results:
- **Current Address:** 
- **Phone:** 
- **Email:** 
- **Associated People:** 

#### Reverse Address Search (3304 NE 15th):
- **Current Owner:** 
- **Move-in Date:** 
```

### 2.3 FastPeopleSearch.com (Priority #3)

**Resource:** https://www.fastpeoplesearch.com  
**Automation Priority:** 🟡 MEDIUM  
**Expected Data:** Name, address, relatives

#### Browser-Harness Script
```python
# Phase 2.3: FastPeopleSearch
browser-harness -c '''
new_tab("https://www.fastpeoplesearch.com")
wait_for_load()

# Search: "Mark Shumate" + "Florida" + Age ~59
# Cross-reference with previous findings
# Look for matching relatives/associates
'''
```

#### Data Collection Template
```markdown
### FastPeopleSearch Results
**Search Date:** [TIMESTAMP]
**Source:** fastpeoplesearch.com

#### Results:
- **Current Address:** 
- **Relatives:** 
- **Previous Addresses:** 
```

---

## 📊 PHASE 3: COURT & PUBLIC RECORDS

### 3.1 Broward County Clerk of Courts

**Resource:** https://browardclerk.org  
**Automation Priority:** 🟡 MEDIUM  
**Expected Data:** Civil/criminal records with addresses

#### Browser-Harness Script
```python
# Phase 3.1: Broward County Clerk of Courts
browser-harness -c '''
new_tab("https://browardclerk.org")
wait_for_load()

# Navigate to: Case Search or Records Search
# Search by: Name = "Mark Shumate" or "Mark Tristan Shumate"
# Date range: Last 5 years

# Extract:
# - Case filings with addresses
# - Civil judgments
# - Court records
# Note: May reveal new address from recent filings
'''
```

#### Data Collection Template
```markdown
### Court Records Results
**Search Date:** [TIMESTAMP]
**Source:** Broward County Clerk of Courts

#### Cases Found:
1. Case Number: 
   - Type: 
   - Date: 
   - Address Listed: 
   - Status: 
```

### 3.2 JudyRecords.com

**Resource:** https://www.judyrecords.com  
**Automation Priority:** 🟢 LOW  
**Expected Data:** 600M+ court records, free access

#### Browser-Harness Script
```python
# Phase 3.2: JudyRecords
browser-harness -c '''
new_tab("https://www.judyrecords.com")
wait_for_load()

# Search: "Mark Shumate" + "Florida"
# Look for recent cases with address listings
'''
```

### 3.3 Florida Voter Registration

**Resource:** Florida Division of Elections  
**Automation Priority:** 🟢 LOW  
**Expected Data:** Registered voter address (if applicable)

```markdown
### Voter Registration Results
**Search Date:** [TIMESTAMP]
**Source:** Florida Division of Elections

#### Status:
- **Registered?** 
- **Registration Address:** 
- **Registration Date:** 
```

---

## 📊 PHASE 4: VERIFICATION & CROSS-REFERENCE

### 4.1 Google Maps / Street View

**Purpose:** Verify address findings are current residential properties

#### Verification Checklist
```python
# For each address found:
browser-harness -c '''
# Visit Google Maps
new_tab("https://www.google.com/maps")
wait_for_load()

# Search each candidate address
# Verify:
# - Is it residential?
# - Street view recent?
# - Matches property records?
# - Signs of occupancy?
'''
```

```markdown
### Address Verification
**Candidate Address 1:** 
- **Google Maps Check:** ✅/❌
- **Street View Date:** 
- **Property Type:** 
- **Residential Indicators:** 
- **Confidence Level:** HIGH/MEDIUM/LOW
```

### 4.2 Cross-Reference Matrix

| Source | Address Found | Phone | Email | Relatives | Confidence |
|--------|---------------|-------|-------|-----------|------------|
| Broward Property | | | | | |
| TruePeopleSearch | | | | | |
| That's Them | | | | | |
| FastPeopleSearch | | | | | |
| Court Records | | | | | |

**Consensus Address:** [HIGHEST CONFIDENCE]

---

## 📊 PHASE 5: PAID UPGRADE PATH (IF NEEDED)

### 5.1 BeenVerified - $1 Trial

**Only proceed if free resources produce insufficient results**

**Resource:** https://www.beenverified.com  
**Cost:** $1 for 7-day trial (100 reports)  
**Cancellation:** Before 7 days to avoid $17.48/month charge

#### Browser-Harness Script
```python
# Phase 5.1: BeenVerified (PAID - USE ONLY IF NECESSARY)
browser-harness -c '''
new_tab("https://www.beenverified.com")
wait_for_load()

# Sign up for $1 trial
# Search: "Mark Tristan Shumate" + "Florida" + Age 59

# Extract FULL report:
# - Current address
# - Address history (with dates)
# - Property ownership
# - Associates/relatives
# - Criminal/court records
# - Phone numbers
# - Email addresses
# - Vehicle records
# - Social media profiles

# Screenshot entire report
# Save PDF if available ($3.99 extra)

# IMPORTANT: Set reminder to cancel before day 7
'''
```

#### Expected Comprehensive Data
```markdown
### BeenVerified Report
**Search Date:** [TIMESTAMP]
**Cost:** $1 (Trial)
**Report ID:** 

#### Current Address:
- 

#### Address History:
1. [Current]
2. 3304 NE 15th Court, Fort Lauderdale, FL 33304 (Confirmed previous)
3. [Additional historical addresses]

#### Contact Information:
- Phone: 
- Email: 
- Social Media: 

#### Associates:
- 

#### Property Ownership:
- 

#### Court/Criminal Records:
- 

#### Vehicle Records:
- 
```

---

## 📊 FINDINGS SUMMARY

### Current Address (PRIMARY TARGET)
**Status:** ⬜ NOT YET DETERMINED

```markdown
**Most Likely Current Address:**

**Address:** 
**City, State, ZIP:** 
**County:** 
**Property Type:** 
**Ownership Status:** 

**Source Verification:**
- Broward County Property Records: ✅/❌
- People Search Tools: ✅/❌ (TruePeopleSearch, That's Them, FastPeopleSearch)
- Court Records: ✅/❌
- Google Maps Verification: ✅/❌

**Confidence Level:** 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW

**Supporting Evidence:**
1. 
2. 
3. 
```

### Contact Information

```markdown
**Phone Numbers:**
- Primary: 
- Secondary: 
- Verification: 

**Email Addresses:**
- Primary: 
- Secondary: 
- Verification: 

**Social Media Profiles:**
- LinkedIn: 
- Facebook: 
- Others: 
```

### Associates & Relatives

```markdown
**Known Associates:**
1. Name: 
   - Relationship: 
   - Address: 
   - Verification: 

**Known Relatives:**
1. Name: 
   - Relationship: 
   - Address: 
   - Verification: 
```

### Property History

```markdown
**Property Timeline:**
1. [CURRENT] Address: 
   - Purchase Date: 
   - Property Value: 
   - Source: 

2. [PREVIOUS] 3304 NE 15th Court, Fort Lauderdale, FL 33304
   - Ownership Period: [Unknown] to [Sale Date]
   - Sale Price: 
   - Buyer: 
   - Source: Broward County Property Appraiser
```

---

## 🔍 AUTOMATION EXECUTION LOG

### Execution Timeline

| Phase | Resource | Status | Start Time | End Time | Duration | Results |
|-------|----------|--------|------------|----------|----------|---------|
| 1.1 | Broward Property | ⬜ Pending | | | | |
| 2.1 | TruePeopleSearch | ⬜ Pending | | | | |
| 2.2 | That's Them | ⬜ Pending | | | | |
| 2.3 | FastPeopleSearch | ⬜ Pending | | | | |
| 3.1 | Broward Courts | ⬜ Pending | | | | |
| 3.2 | JudyRecords | ⬜ Pending | | | | |
| 4.1 | Verification | ⬜ Pending | | | | |

### Automation Scripts Run

```bash
# Master automation script location:
# ./scripts/shumate_investigation.py

# Execute full investigation:
python scripts/shumate_investigation.py --subject "Mark Tristan Shumate" --age 59 --state FL

# Execute individual phases:
python scripts/shumate_investigation.py --phase 1  # Property records
python scripts/shumate_investigation.py --phase 2  # People search
python scripts/shumate_investigation.py --phase 3  # Court records
python scripts/shumate_investigation.py --phase 4  # Verification
```

---

## 📸 EVIDENCE DOCUMENTATION

### Screenshot Repository
```
./evidence/screenshots/
├── phase1_broward_property_[timestamp].png
├── phase2_truepeoplesearch_[timestamp].png
├── phase2_thatsthem_[timestamp].png
├── phase2_fastpeoplesearch_[timestamp].png
├── phase3_broward_courts_[timestamp].png
├── phase3_judyrecords_[timestamp].png
├── phase4_google_maps_[timestamp].png
└── phase5_beenverified_[timestamp].png (if used)
```

### Data Export
```
./evidence/data_exports/
├── shumate_property_records.json
├── shumate_people_search.json
├── shumate_court_records.json
├── shumate_verification.json
└── shumate_final_report.pdf
```

---

## ⚖️ LEGAL & COMPLIANCE

### FCRA Compliance Notice
**IMPORTANT:** This investigation uses only **non-FCRA compliant** data sources for informational purposes. These results:
- ❌ **CANNOT** be used for employment decisions
- ❌ **CANNOT** be used for tenant screening
- ❌ **CANNOT** be used for credit decisions
- ❌ **CANNOT** be used for insurance underwriting
- ✅ **CAN** be used for skip tracing / asset location
- ✅ **CAN** be used for due diligence (non-employment)

### Florida Sunshine Law
Florida's public records law provides excellent access to:
- ✅ Property records
- ✅ Court records
- ✅ Voter registration (limited)
- ✅ Vital records (with proper access)

This investigation operates within Florida's public records framework.

### Data Source Attribution
All data sources and timestamps are documented for:
1. Legal defensibility
2. Chain of custody
3. Distinguishing verified from unverified claims
4. Audit trail

---

## 🎯 SUCCESS CRITERIA

### Primary Objective
- ✅ **SUCCESS:** Current home address located with HIGH confidence (3+ sources)
- 🟡 **PARTIAL:** Current home address located with MEDIUM confidence (2 sources)
- ❌ **INCOMPLETE:** Unable to locate current address from free resources

### Secondary Objectives
- Current phone number(s)
- Current email address(es)
- Known associates/relatives
- Property ownership timeline
- Court records (if any)

---

## 📋 NEXT STEPS

### If Free Resources Succeed
1. ✅ Document all findings with timestamps
2. ✅ Create final PDF report
3. ✅ Provide address to client with confidence rating
4. ✅ Maintain evidence repository for 90 days

### If Free Resources Insufficient
1. ⚠️ Review data gaps
2. ⚠️ Proceed to BeenVerified $1 trial
3. ⚠️ Set cancellation reminder (Day 6)
4. ⚠️ Extract comprehensive report
5. ⚠️ Cancel before Day 7 if one-time use

### If Paid Resources Also Insufficient
1. 🔴 Escalate to:
   - Professional skip tracing service
   - Private investigator with database access
   - FCRA-compliant background check provider (if legally permitted use case)

---

## 📝 INVESTIGATION NOTES

### Investigator Comments
```
[TIMESTAMP] Investigation initiated for Mark Tristan Shumate, age 59, last known at 
3304 NE 15th Court, Fort Lauderdale, FL. Subject sold this property; current address 
unknown. Beginning with Broward County property records...

[Add timestamped notes as investigation progresses]
```

### Challenges Encountered
- [ ] Challenge 1:
- [ ] Challenge 2:

### Unexpected Findings
- [ ] Finding 1:
- [ ] Finding 2:

---

## 🔗 RESOURCE QUICK LINKS

### Property Records
- [Broward County Property Appraiser](https://bcpa.net)
- [Florida Property Records](https://www.floridalandrecords.com)

### Free People Search
- [TruePeopleSearch](https://www.truepeoplesearch.com)
- [That's Them](https://thatsthem.com)
- [FastPeopleSearch](https://www.fastpeoplesearch.com)
- [ZabaSearch](https://www.zabasearch.com)

### Court Records
- [Broward County Clerk](https://browardclerk.org)
- [JudyRecords](https://www.judyrecords.com)
- [PACER (Federal Courts)](https://pacer.uscourts.gov)

### Paid Resources (Use Only If Necessary)
- [BeenVerified](https://www.beenverified.com) - $1 Trial
- [TruthFinder](https://www.truthfinder.com) - ~$23-28/month
- [Intelius](https://www.intelius.com) - $21.13/month

### Verification
- [Google Maps](https://www.google.com/maps)
- [Zillow](https://www.zillow.com) - Property verification
- [Realtor.com](https://www.realtor.com) - Property sales history

---

## 📄 REPORT METADATA

**Investigation ID:** INV-2026-05-14-SHUMATE  
**Subject:** Mark Tristan Shumate  
**Date Created:** 2026-05-14  
**Last Updated:** [TIMESTAMP]  
**Investigation Type:** Skip Tracing / Address Location  
**Jurisdiction:** Fort Lauderdale, Broward County, Florida  
**Status:** 🟡 IN PROGRESS  
**Estimated Completion:** [TIMESTAMP]  

**Automation Framework:** browser-harness (Python)  
**Total Phases:** 5  
**Phases Completed:** 0/5  
**Free Resources Used:** 0/6  
**Paid Resources Used:** 0/1  

**Lead Investigator:** PI Intelligence Platform  
**Report Version:** 1.0  

---

## ✅ PHASE COMPLETION CHECKLIST

- [ ] **Phase 1.1:** Broward County Property Appraiser search complete
- [ ] **Phase 2.1:** TruePeopleSearch.com search complete
- [ ] **Phase 2.2:** That's Them search complete
- [ ] **Phase 2.3:** FastPeopleSearch.com search complete
- [ ] **Phase 3.1:** Broward County Clerk of Courts search complete
- [ ] **Phase 3.2:** JudyRecords.com search complete
- [ ] **Phase 3.3:** Florida voter registration check complete
- [ ] **Phase 4.1:** Google Maps verification complete
- [ ] **Phase 4.2:** Cross-reference matrix completed
- [ ] **Phase 5.1:** BeenVerified (if needed) complete

**Investigation Complete:** ❌ No / ✅ Yes  
**Primary Objective Achieved:** ❌ No / ✅ Yes  
**Final Report Generated:** ❌ No / ✅ Yes  

---

**END OF INVESTIGATION PLAN**

*This document will be updated in real-time as the browser-harness automation executes each phase and findings are documented.*
