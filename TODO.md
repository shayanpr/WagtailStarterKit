# Wagtail Starter Kit - Roadmap & Ideas

## 🚀 High Priority (Core Features)
- [x] **Contact Page Model:** Implemented `AbstractEmailForm` with custom field builder.
- [x] **Project Tagging:** Integrated `django-taggit` with smart filtering on `ProjectIndexPage`.
- [ ] **About Us Page:** Create a dedicated model for About pages.
    - [ ] **Team Members:** Implement `TeamMember` snippet and a `TeamGridBlock`.
- [ ] **Blog / News App:** Dedicated app for articles, updates, and tutorials.
    - [ ] **Models:** `BlogIndexPage` (Listing) and `BlogPage` (Article).
    - [ ] **Taxonomy:** Categories and Tags support.
    - [ ] **Feeds:** RSS/Atom feed support.

## 🏢 B2B / Corporate Features
- [x] **Pricing/Comparison Tables:** Created dynamic `ComparisonBlock` with featured tier support.
- [x] **FAQ Accordion:** Collapsible questions and answers using pure HTML/Tailwind.
- [x] **Trust & Social Proof:**
    - [x] **Testimonials Snippet:** Manage client quotes centrally and select them via `TestimonialBlock`.
    - [x] **Partner Logo Grid:** A "Trusted By" block for displaying client logos using `Partner` snippets.
- [ ] **Sales & Service:**
    - [ ] **Global CTA:** A reusable "Call to Action" strip for the footer or page bottom.
    - [ ] **Stats Block:** A grid of animated numbers (e.g., "99.9% Uptime", "10k Users").
- [ ] **Case Study Model:** A variation of `ProjectPage` focused on "Problem -> Solution -> ROI/Results".

## 💼 Agency Operations (Public vs. Private)
- [ ] **Public Repo Cleanup:**
    - [ ] Add `gemini.md` to `.git/info/exclude`.
    - [ ] Run `git filter-repo` to purge `seed_data.py`, `content_data.py`, and `gemini.md` history.
    - [ ] Force-push cleaned history to public origin.
- [ ] **Private Mirror Setup:**
    - [ ] Create a dedicated private repository for full agency automation.
    - [ ] Document the `git pull public main` workflow for syncing features.
- [ ] **Public Documentation:**
    - [ ] Add "Built with AI" statement to `README.md` without exposing internal prompts.

## ✨ Developer Experience (DX)
- [ ] **Multi-language Support:** Integrate `wagtail-localize` for parallel translation trees.
- [x] **Migration Reset Strategy:** Clean up logic established for clean `0001_initial` releases.
- [ ] **GitHub Template Config:** Finalize the repository as a GitHub Template.
- [x] **Programmatic Seeding:** Robust `seed_data.py` script with image, settings, and recursive cleaning automation.

## 🎨 Design & UI
- [x] **Tailwind Components:** Expanded blocks with Grids, FAQs, Pricing, and Partners.
- [ ] **Dark Mode Support:** Ensure the base templates and blocks are compatible with Tailwind's dark mode.
- [x] **Branding & Analytics:**
    - [x] Integrate `BrandingSettings` (Logo/Favicon) into `base.html`.
    - [x] Add **Google Analytics ID** field to settings and auto-inject script.

## 📦 Maintenance
- [x] **Code Reorganization:** Moved blocks to a dedicated `blocks` app for better modularity.
- [x] **Image Optimization:** Implemented WebP format and specific crops (fill/width) across all templates.
- [ ] **Documentation:** Update `README.md` with instructions on how to use the new Form, Tagging, and Comparison features.
- [ ] **Search:** Implement a working search results page template.
