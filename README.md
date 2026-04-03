# GitHub Copilot CLI vs Claude Code CLI — Benchmark for Business Users

> **Hypothesis:** Both tools produce functionally equivalent results. The meaningful difference for enterprise users is GitHub Copilot's built-in security, identity management, and organizational controls — not AI coding capability.

---

## Who This Test Is For

This benchmark is designed for **business users and decision-makers** — people who want to build things with AI tools but don't have a coding background. Every task here is something a real non-technical person would ask an AI assistant to do.

The goal is to answer one honest question:

> *"Is the hype real or is there an incredible marketing cycle happening and Github Copilot functions just as good as Claude Code in the CLI?"*

---

## The 5 Tests

| # | What You're Testing | Seed Files Needed |
|---|---|---|
| 1 | Build a website from scratch | None — prompt only |
| 2 | Turn sales data into a visual dashboard | `seeds/02-sales-data/sales_data.csv` |
| 3 | Fix a broken website | `seeds/01-broken-coffee-shop/` (3 seeded bugs) |
| 4 | Deploy a web app to Azure | `seeds/04-task-tracker-app/` + your Azure details |
| 5 | Add a login page to an existing website | `seeds/03-existing-site/` |

---

## How to Run the Tests

### What you need
- GitHub Copilot CLI installed (`gh copilot` — requires GitHub Copilot subscription)
- Claude Code CLI installed (`claude` — requires Anthropic account)
- Python 3.10+ (for Test 4 seed app)
- An Azure account (for Test 4)

### Before you start
1. Open **two terminal windows** — one for each tool
2. Make sure both tools are logged in and ready
3. Have the `prompts/` folder open so you can copy-paste identically

### Running each test

**Step 1:** Copy the prompt text from `prompts/0X-test-name.txt` exactly as written.

**Step 2:** Paste the identical prompt into each tool, one at a time.

**Step 3:** If a seed file is required, attach or reference it the same way in both tools.

**Step 4:** Let each tool complete without additional guidance. Only re-prompt if the tool asks you a clarifying question — and ask the same clarifying response to both.

**Step 5:** Score the result using `scoring/rubric.md`.

---

## Test 4 — Azure Setup

Before running Test 4, update `prompts/04-deploy-to-azure.txt`:

1. Replace `[REPLACE_WITH_YOUR_SUBSCRIPTION_ID]` with your Azure Subscription ID
2. Replace `[REPLACE_WITH_YOUR_RESOURCE_GROUP]` with an existing or new resource group name

Both tools receive the **same updated prompt** with your real Azure details.

**Cost:** The prompt specifies Azure App Service **Free tier (F1)**, which costs $0. Your Azure credits will not be charged.

> ⚠️ **After the test:** Delete the App Service instances from the Azure Portal when done. Even on the free tier, it's good hygiene.

---

## Bonus Round — Azure Setup

**Prompt file:** `prompts/bonus-online-ordering-azure.txt`

**Before you run:**
1. Update your Azure Subscription ID and Resource Group in the prompt file if you haven't already
2. Make sure your resource group exists and is empty (no running App Service instances)
3. Switch both tools to **Claude Opus 4.6** before pasting the prompt:
   - GitHub Copilot CLI: `/model claude-opus-4.6`
   - Claude Code CLI: `/model claude-opus-4-6`

**What this test asks each tool to build — in a single prompt:**

> *"My coffee shop is called Morning Brew and business is booming. I want to take orders online so customers don't have to wait in line."*

| Component | What's required |
|---|---|
| Customer ordering page | Menu display, add to cart, place order with name |
| Order confirmation | Shown to customer after placing order |
| Owner dashboard | Separate page showing all incoming orders with timestamps |
| Mark as ready | Owner can update order status |
| Azure deployment | Full app live at a real URL — provisioned from scratch |

**This is the hardest test in the benchmark.** It requires building a multi-page app with connected state and deploying it to Azure — all from one prompt, with no existing infrastructure running.

**Scoring (100 pts):**
- Customer ordering page works: 30 pts
- Order confirmation shown: 10 pts
- Owner dashboard shows orders: 20 pts
- Mark as ready works: 10 pts
- Design quality: 15 pts
- Live at an Azure URL: 15 pts

**Cost:** Free tier (F1) is specified in the prompt. No charges expected.

> ⚠️ **After the bonus round:** Delete the App Service from the Azure Portal to stop all resources.

---

## Folder Structure

```
copilot-vs-claudecode-benchmark/
│
├── README.md                          ← You are here
│
├── prompts/                           ← Identical prompts for both tools
│   ├── 01-build-website.txt
│   ├── 02-sales-dashboard.txt
│   ├── 03-fix-broken-site.txt
│   ├── 04-deploy-to-azure.txt
│   ├── 05-add-login.txt
│   └── bonus-online-ordering-azure.txt  ← Bonus round (Opus 4.6, hardest test)
│
├── seeds/                             ← Starting files both tools receive
│   ├── 01-broken-coffee-shop/         ← Test 3: has 3 intentional bugs
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   ├── 02-sales-data/                 ← Test 2: 48 rows of sales data
│   │   └── sales_data.csv
│   ├── 03-existing-site/              ← Test 5: clean site to extend
│   │   ├── index.html
│   │   └── style.css
│   └── 04-task-tracker-app/           ← Test 4: Flask app to deploy
│       ├── app.py
│       ├── requirements.txt
│       └── templates/
│           └── index.html
│
├── scoring/
    ├── rubric.md                      ← Plain-English scoring guide
    └── judge-prompt.txt               ← Prompt for AI judge scoring
```

---

## What the Seeded Bugs Are (Test 3)

The `01-broken-coffee-shop` folder has three intentional problems. Do not fix them before the test — let each tool find them:

| Bug | What's Wrong |
|---|---|
| Bug 1 | CSS file is linked as `styles.css` but the actual file is named `style.css` — so no styling loads |
| Bug 2 | The menu button calls `openMenu()` but the JavaScript function is named `showMenu()` — so the button crashes |
| Bug 3 | The hero image points to `images/hero-photo.jpg` but no `images/` folder exists — broken image |

A perfect score = finding and fixing all three without being told what they are.

---

## Model Configuration

Both tools are pinned to the **same model** to eliminate AI capability as a variable. The only difference between the two tools is the product wrapper and enterprise features.

### Model & Mode Settings

| Setting | GitHub Copilot CLI | Claude Code CLI |
|---|---|---|
| Model — main tests | Claude Sonnet 4.6 | Claude Sonnet 4.6 |
| Model — bonus round | Claude Opus 4.6 | Claude Opus 4.6 |
| Reasoning effort | Medium | Default (automatic) |
| Autonomy mode | **Autopilot** | **Standard** |

**Why Sonnet for the main benchmark?**
Sonnet 4.6 is the model most real users run day-to-day. It handles all five tasks comfortably, keeps costs manageable for anyone reproducing the test, and is supported by both tools.

**Why Opus for the bonus round?**
To close off the counter-argument that "Opus would have changed things." One test, both tools on maximum capability, scored the same way. If the result is still equivalent, that's the final word.

**Why different autonomy modes?**
Each tool is run in its recommended default configuration for a business user — the way a non-technical person would actually use it out of the box. GitHub Copilot's autopilot executes actions without asking for confirmation at each step. Claude Code's standard mode surfaces key actions for approval before proceeding. This difference is intentional and transparent — it reflects the real-world experience of each tool, not a lab condition. Any impact on the result is noted in the findings.

**Why not use `--dangerously-skip-permissions` for Claude Code?**

Claude Code has a flag called `--dangerously-skip-permissions` that suppresses all approval prompts, making it behave more like GitHub Copilot's autopilot. This flag is **not used** in this benchmark for two reasons:

1. **It's not a fair comparison.** GitHub Copilot's autopilot is a designed, supported product mode with built-in guardrails — it is how the tool is meant to be used. `--dangerously-skip-permissions` is an override flag that bypasses Claude Code's own safety checks. The name itself signals it is not intended for everyday use. Running Claude Code with a flag that says "dangerous" in the name would not be a legitimate like-for-like comparison.

2. **It does not reflect how a business user would actually run the tool.** The goal of this benchmark is to simulate a real non-technical user's experience with each product out of the box. A business user would not — and should not — run any software tool in a mode explicitly labelled "dangerous." Claude Code's standard mode, with its approval prompts, is the correct and honest representation of the product.

The autonomy difference is a real product difference and is noted transparently throughout the results. It is not a disadvantage engineered against either tool — it is the reality of how each tool works for the audience this benchmark is designed to serve.

### Which GitHub Copilot CLI to use

> ⚠️ **Important:** There are two tools that share the name "GitHub Copilot CLI." Use the **new Copilot CLI** — not the old `gh copilot suggest/explain` extension, which is now archived and only handles shell command suggestions.

| Tool | Install command |
|---|---|
| ✅ New Copilot CLI (use this) | `npm install -g @github/copilot` or `brew install github/copilot-cli/copilot` |
| ❌ Old gh extension (do not use) | `gh extension install github/gh-copilot` — archived, limited to shell suggestions only |

Launch the new Copilot CLI by running `copilot` in your terminal.

### How to set the model on each tool

Both tools use the same `/model` slash command **inside** the interactive session.

**Claude Code CLI:**
```bash
claude                  # launch the session
/model claude-sonnet-4-6   # main tests
/model claude-opus-4-6     # bonus round
/status                 # verify current model
```
Alternatively, launch with the model pre-set:
```bash
claude --model claude-sonnet-4-6
claude --model claude-opus-4-6
```

**GitHub Copilot CLI:**
```bash
copilot                 # launch the session
/model claude-sonnet-4.6   # main tests
/model claude-opus-4.6     # bonus round
```
The selected model is displayed above the input box so you can always confirm it at a glance.

> ⚠️ **Verify before each test:** Confirm the model name shown in each session matches the required model before pasting any prompt. A wrong model quietly invalidates the comparison.

> ⚠️ **Minimum version requirement:** GitHub Copilot CLI **v1.0.17 or later** is required for Claude Sonnet 4.6 and Opus 4.6 model support. Run `copilot --version` to confirm before starting. If outdated, run `npm install -g @github/copilot` to update.

---

## Reproducing This Test

This benchmark is fully self-contained. Everything needed is in this repository:
- All seed files are provided
- All prompts are static text files
- No internet access required except for Test 4 (Azure)
- No proprietary data — all content is fictional

Fork the repo, run the tests, and publish your own results.

---

## The Honest Bottom Line

| What's Being Tested | Expected Finding |
|---|---|
| AI output quality | Equivalent |
| Ability to build a website | Both work |
| Ability to read and fix bugs | Both work |
| Ability to deploy to Azure | Both work |


