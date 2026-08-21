# AI Agent Briefing Guide - Supplier Search Process

**Purpose:** Template for briefing AI agents on supplier search tasks (reusable for all projects)  
**Created:** August 21, 2026  
**Use This:** When working with Claude or other AI agents on supplier research

---

## 🎯 How to Brief an AI Agent on Supplier Search

Use this guide to provide complete context to an AI agent without repeating the workflow explanation each time.

---

## PART 1: ESTABLISH THE WORKFLOW (One-time setup)

### Tell the AI:

> "I'm using a structured supplier search workflow with these phases:
>
> **Phase 1 - Clients Folder (Active Working):**
> - Where I work with clients to find suppliers
> - Documents: Client_Brief, Supplier_Research, Comparison_Matrix, Feedback_Notes, Final_Recommendation
> - Duration: 2-4 weeks
>
> **Phase 2 - Suppliers Folder (Final/Archive):**
> - Where finalized suppliers are stored permanently
> - Complete documentation, contracts, compliance docs
> - Ready for future orders
>
> **Workflow Steps:**
> 1. Client Intake → Document requirements
> 2. Research & Discovery → Find suppliers
> 3. Build Comparison → Create evaluation matrix
> 4. Client Feedback Loop → Get client input
> 5. Narrow Down → Select top choices
> 6. Final Recommendation → Get approval
> 7. Archive → Move to Suppliers folder
>
> I have README files documenting this in `/Silky Express Business/` folder.
> Use WORKFLOW.md as your step-by-step guide."

---

## PART 2: PROVIDE CURRENT PROJECT CONTEXT

### Tell the AI:

> "I'm currently working on: **[PROJECT NAME]**
>
> **Client Details:**
> - Company: [Name]
> - Location: [City, Country]
> - Contact: [Person name, email, phone]
> - Industry: [What they do]
>
> **What They Need:**
> - Primary Product: [Specific item/equipment]
> - Secondary Products: [List]
> - Purpose: [Why they need it]
>
> **Key Requirements:**
> - Budget: [USD/ZAR amount or flexible]
> - Timeline: [When needed]
> - Quality standards: [Certifications, specs]
> - Geographic preference: [China/Europe/local?]
> - Special considerations: [Any unique needs]
>
> **Project Status:**
> - Current Phase: [Intake/Research/Comparison/Feedback/Final/Archive]
> - Documents Created: [List which docs exist]
> - Next Action: [What we're doing next]"

---

## PART 3: GIVE SPECIFIC INSTRUCTIONS

### For RESEARCH Phase:

> "I need you to help me research suppliers for [PRODUCT].
>
> **Instructions:**
> 1. Search for top suppliers of [PRODUCT] globally (focus: [REGION])
> 2. Find 5-8 potential suppliers
> 3. Look for: company info, product specs, pricing, certifications, lead times
> 4. Create Supplier_Research.md with findings
> 5. Format: Company name, location, products, price range, lead time, certifications, references
>
> **File Location:** `/Clients/[Client Name]/Supplier_Research.md`
> **Deadline:** [When you need this]"

### For COMPARISON Phase:

> "I need you to build a supplier comparison matrix.
>
> **Instructions:**
> 1. Compare suppliers on: Price, Lead Time, Quality, Certifications, References
> 2. Weight criteria: Quality (25%), Price (20%), Lead time (15%), Reliability (20%), Support (20%)
> 3. Score each supplier out of 100
> 4. Identify top 3 candidates
> 5. Create Supplier_Comparison_Matrix.md
>
> **Criteria to evaluate:**
> - Quality/certifications
> - Price per unit & MOQ
> - Lead time
> - Payment terms
> - References/track record
> - Communication/support
>
> **File Location:** `/Clients/[Client Name]/Supplier_Comparison_Matrix.md`"

### For RESEARCH & RECOMMENDATION Phase:

> "I need deep research on a specific supplier: [SUPPLIER NAME]
>
> **Instructions:**
> 1. Research company background, history, reputation
> 2. Find product specifications & datasheets
> 3. Identify certifications & standards compliance
> 4. Look for customer testimonials/references
> 5. Research pricing & payment terms
> 6. Assess reliability & financial stability
> 7. Create comprehensive report
> 8. Make recommendation: Should client use this supplier? Why/why not?
>
> **File Location:** `/Clients/[Client Name]/Final_Recommendation.md`"

---

## PART 4: PROVIDE REFERENCE MATERIALS

### Tell the AI:

> "Reference these documents in my project for context:
>
> **System Documentation:**
> - `/README.md` — Complete system overview
> - `/WORKFLOW.md` — Step-by-step workflow
> - `/Clients/README.md` — Clients folder guide
> - `/Suppliers/README.md` — Suppliers folder guide
>
> **Current Project:**
> - `/Clients/[Client Name]/README.md` — Project overview
> - `/Clients/[Client Name]/Client_Brief.md` — Client requirements
> - `/Clients/[Client Name]/Supplier_Research.md` — Research findings
> - `/Clients/[Client Name]/Supplier_Comparison_Matrix.md` — Evaluation
>
> **Example Completed Project:**
> - `/Suppliers/Bayag Resin Washed Stone/` — See how a finalized supplier is documented"

---

## PART 5: EXAMPLE COMPLETE BRIEF

Here's a complete example of how to brief an AI agent:

---

### **EXAMPLE BRIEFING MESSAGE:**

> "I'm working on a supplier search for a new client: **Sunshine Paints**
>
> **About the Project:**
> - Client: Sunshine Paints (paint mixing company, Durban, South Africa)
> - Contact: Duno
> - Industry: Paint manufacturing & accessories
>
> **What They Need:**
> - **Primary:** Automated paint mixing machine (input color codes, auto-mixes paint)
> - **Secondary:** Spray guns, masking tape, sandpaper/water papers
> - **Ideal:** One supplier for all products
>
> **Requirements:**
> - Budget: TBD (awaiting Duno's confirmation)
> - Timeline: TBD (need to confirm with Duno)
> - Quality: Color accuracy critical, commercial durability
> - Location: South Africa (Durban)
>
> **Current Status:**
> - Phase: Client Intake (Initial requirements gathered)
> - Documents Created: `/Clients/Sunshine Paints/` (README.md, Client_Brief.md)
> - Next Step: Research paint mixing machine suppliers
>
> **What I Need You To Do:**
> 1. Research top paint mixing machine suppliers globally
> 2. Look for machines with color code input capability
> 3. Find 5-8 potential suppliers
> 4. For each, gather: company info, product specs, pricing, lead times, certifications
> 5. Create `/Clients/Sunshine Paints/Supplier_Research.md` with findings
>
> **Important:**
> - Suppliers should serve South African market (or ship to Durban)
> - Paint mixer is PRIMARY focus
> - Secondary: Can they also supply spray guns, tapes, sandpaper?
> - Format your findings as structured research document
>
> Refer to `/WORKFLOW.md` Step 2 (Research & Discovery) for guidance.
> Use `/Suppliers/Bayag Resin Washed Stone/` as example of how complete research looks."

---

## PART 6: WHAT TO EXPECT BACK

### Research Phase Output:

**Supplier_Research.md should include:**
```markdown
# Paint Mixing Machine Suppliers

## Supplier A
- Company: [Name]
- Location: [City, Country]
- Years in business: [X]
- Key products: [List]
- Price range: $[X]-[Y]
- Lead time: [X] days
- Certifications: [List]
- Unique features: [List]
- Serves South Africa: Yes/No
- References available: Yes/No
- Contact: [Email/phone if available]
- Assessment: [Good/Concerns/Need more info]

## Supplier B
[Same format]

## Supplier C
[Same format]

## Initial Recommendation
Top 3 to evaluate further: [List]
```

---

## PART 7: FOLLOW-UP INSTRUCTIONS

### For Next Phase (Comparison):

> "Now that we have supplier research, I need you to:
>
> 1. Create comparison matrix comparing Suppliers A, B, C on:
>    - Price (per machine, MOQ if applicable)
>    - Lead time to delivery
>    - Features (color code input, accuracy, speed, capacity)
>    - Certifications
>    - References
>    - Payment terms
>    - Support/warranty
>
> 2. Score each 0-100 based on criteria weights
> 3. Identify top choice & why
> 4. Flag any red flags or concerns
> 5. Create `/Clients/Sunshine Paints/Supplier_Comparison_Matrix.md`
>
> Reference: WORKFLOW.md Step 3 (Build Comparison Matrix)"

---

## PART 8: COMMON INSTRUCTIONS TO GIVE AI

### "Build a Comparison Matrix"
```
Compare suppliers on: [Criteria List]
Weight by importance: [Weighting]
Score each 0-100
Identify top 3
Flag red flags
Create structured table
```

### "Research This Supplier"
```
Find: Company background, product specs, certifications
Look for: Customer reviews, case studies, references
Assess: Reliability, financial stability, support quality
Make recommendation: Yes/No and why
```

### "Help Me Prepare Client Meeting"
```
Summarize findings
Highlight pros/cons
Prepare questions for client
Create recommendation slide
```

### "Create Project Documentation"
```
File path: [Specific location]
Format: Markdown
Include: [Specific sections]
Use template: [Which template]
Reference: [Which docs to cite]
```

---

## PART 9: TIPS FOR WORKING WITH AI AGENTS

✅ **Clear, specific instructions** — Tell what doc to create, where to put it, what format

✅ **Provide context** — Send Client_Brief so AI understands requirements

✅ **Reference examples** — Point to completed projects (e.g., Bayag supplier folder)

✅ **Give file paths** — Exact locations `/Clients/[Name]/[Document].md`

✅ **Specify format** — Tables, lists, markdown structure

✅ **Set deadlines** — "Have this by [date]"

✅ **Reference workflow** — "See WORKFLOW.md Step 2-4"

❌ **Avoid vague requests** — "Find suppliers" is too vague
✅ **Instead:** "Find 5-8 paint mixing machine suppliers, create research document with company name, location, price, lead time, certifications"

---

## PART 10: QUICK CHECKLIST - BEFORE BRIEFING AN AI

- [ ] Client name & location clear
- [ ] Product/service clearly defined
- [ ] Specific deliverable identified (which document to create)
- [ ] File path specified (where to save it)
- [ ] Format/structure clear (table, markdown, etc.)
- [ ] Timeline/deadline set
- [ ] Reference materials provided (Client_Brief, workflow docs)
- [ ] Examples given (show how completed projects look)
- [ ] Success criteria clear (what makes this "done"?)

---

## 🔄 TEMPLATE FOR FUTURE AI BRIEFINGS

Copy this template when briefing a new AI agent:

---

> **Project:** [Project Name]  
> **Client:** [Client Company]  
> **Phase:** [Which workflow phase - Intake/Research/Comparison/Feedback/Final]
>
> **Current Status:**
> - Documents created: [List]
> - Next action: [What we're doing]
> - Deadline: [When needed]
>
> **What I Need:**
> [Specific task description]
>
> **Output Expected:**
> - File: `/Clients/[Client]/[Document_Name].md`
> - Format: [Markdown/Table/Structured sections]
> - Sections should include: [List specific sections]
>
> **Reference:**
> - Client requirements: `/Clients/[Client]/Client_Brief.md`
> - Workflow guide: `/WORKFLOW.md` Step [X]
> - Example completed project: `/Suppliers/[Example]/`
>
> **Success Criteria:**
> [How to know when this is done]

---

**This Guide Created:** August 21, 2026  
**Version:** 1.0  
**Last Updated:** August 21, 2026

Use this guide to streamline future AI agent briefings. Just copy, customize with project details, and send!
