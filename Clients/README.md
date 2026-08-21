# Clients Folder - Active Project Workspace

**Purpose:** Discovery & evaluation phase for finding the best supplier for each client

**Duration:** Typically 2-4 weeks per project  
**Status:** Work-in-progress until supplier is selected and approved

---

## 📋 What Goes Here?

This is your **working space** where you:
- ✍️ Document client requirements
- 🔍 Research potential suppliers
- 📊 Build comparison matrices
- 💬 Gather client feedback
- ✅ Make final supplier recommendation

**Do NOT store finalized suppliers here** → Move them to `/Suppliers/` folder when complete

---

## 📁 Typical Project Structure

```
Clients/[Client Name]/
├── README.md                    ← Project overview & status
├── Client_Brief.md              ← Requirements, budget, timeline
├── Supplier_Research.md         ← Initial supplier research
├── Supplier_Comparison_Matrix.md ← Evaluation of options
├── Client_Feedback_Notes.md     ← Feedback trail & iterations
└── Final_Recommendation.md      ← Selected supplier & rationale
```

---

## 🔄 Workflow

**1. Create Folder** → `Clients/[Client Name]/`

**2. Document Requirements** → `Client_Brief.md`
```markdown
Client: [Company Name]
Product: [What they need]
Budget: [Amount]
Timeline: [When needed]
Quality Requirements: [Specs]
```

**3. Research Suppliers** → `Supplier_Research.md`
```markdown
## Potential Suppliers
1. Supplier A - [Brief info]
2. Supplier B - [Brief info]
3. Supplier C - [Brief info]
```

**4. Compare Options** → `Supplier_Comparison_Matrix.md`
```markdown
| Criteria | Supplier A | Supplier B | Supplier C |
|----------|-----------|-----------|-----------|
| Price | $X | $Y | $Z |
| Lead Time | X days | Y days | Z days |
| Certification | Yes | No | Yes |
| References | Yes | No | Yes |
```

**5. Collect Feedback** → `Client_Feedback_Notes.md`
```markdown
## Feedback from [Client Name]

### Round 1 Feedback
- Prefers [Supplier A]
- Budget concern with [Supplier C]
- Needs [specific feature]

### Round 2 Feedback
- Ready to decide
- Wants more info on [Supplier B]
```

**6. Final Recommendation** → `Final_Recommendation.md`
```markdown
## Recommendation: [Supplier Name]

**Why:** [Key reasons]
**Pros:** [Advantages]
**Risks:** [Mitigations]
**Next Steps:** [Action items]
```

---

## ✅ When Project is Complete

**Action:** Move supplier to `/Suppliers/` folder

1. Create: `Suppliers/[Supplier Name]/`
2. Copy all documentation
3. Add contracts & final docs
4. Rename this folder: `Clients/[Client Name] [ARCHIVED]`
5. Commit to git: `"Archive: Move [Supplier] - [Client] approved"`

---

## 📌 Current Projects

**(None yet - awaiting new client projects)**

---

## 💡 Tips

- **Keep it organized** — Use consistent naming
- **Document everything** — Future reference
- **Update frequently** — Commit changes to git
- **Get it in writing** — Email confirmations from client
- **Be systematic** — Use comparison matrices, don't guess

---

**Last Updated:** August 21, 2026
