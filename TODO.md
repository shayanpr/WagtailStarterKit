# Wagtail Starter Kit - Roadmap & Ideas

## 🚀 High Priority (Core Features)
- [x] **Contact Page Model:** Implemented `AbstractEmailForm` with custom field builder.
- [ ] **About Us Page:** Create a dedicated model for About pages, potentially including a "Team Member" Orderable or a specialized layout.
- [ ] **Blog App:** Dedicated `BlogPage` with Tags, Categories, and an RSS feed.

## 🏢 B2B / Corporate Features
- [x] **Pricing/Comparison Tables:** Created dynamic `ComparisonBlock` with featured tier support.
- [ ] **Trust & Social Proof:**
    - [ ] **Testimonials Snippet:** Manage client quotes centrally and select them via `TestimonialChooserBlock`.
    - [ ] **Partner Logo Grid:** A "Trusted By" block for displaying client logos.
    - [ ] **Team Section:** `TeamMemberBlock` with photo, role, bio, and LinkedIn link.
- [ ] **Sales & Service:**
    - [ ] **FAQ Accordion:** Collapsible questions and answers for handling customer objections.
    - [ ] **Global CTA:** A reusable "Call to Action" strip for the footer or page bottom.
- [ ] **Case Study Model:** A variation of `ProjectPage` focused on "Problem -> Solution -> ROI/Results".

## ✨ Developer Experience (DX)
- [ ] **Multi-language Support:** Integrate `wagtail-localize` for parallel translation trees.
- [x] **Migration Reset Strategy:** Clean up logic established for clean `0001_initial` releases.
- [ ] **GitHub Template Config:** Finalize the repository as a GitHub Template.
- [x] **Programmatic Seeding:** Robust `seed_data.py` script with image and settings automation.

## 🎨 Design & UI
- [ ] **Tailwind Components:** Expand the available StreamField blocks (e.g., Stats, Features with Icons).
- [ ] **Dark Mode Support:** Ensure the base templates and blocks are compatible with Tailwind's dark mode.
- [x] **Branding & Analytics:**
    - [x] Integrate `BrandingSettings` (Logo/Favicon) into `base.html`.
    - [x] Add **Google Analytics ID** field to settings and auto-inject script.

## 📦 Maintenance
- [x] **Code Reorganization:** Moved blocks to a dedicated `blocks` app for better modularity.
- [ ] **Documentation:** Update `README.md` with instructions on how to use the new Form and Comparison features.