# Wagtail Starter Kit - Roadmap & Ideas

## 🚀 High Priority (Core Features)
- [ ] **Contact Page Model:** Implement `AbstractEmailForm` to allow users to build custom forms, save submissions to the database, and send email notifications.
- [ ] **About Us Page:** Create a dedicated model for About pages, potentially including a "Team Member" Orderable or a specialized layout.

## 🏢 B2B / Corporate Features
- [ ] **Trust & Social Proof:**
    - [ ] **Testimonials Snippet:** Manage client quotes centrally and select them via `TestimonialChooserBlock`.
    - [ ] **Partner Logo Grid:** A "Trusted By" block for displaying client logos (grayscale/opacity filters).
    - [ ] **Team Section:** `TeamMemberBlock` with photo, role, bio, and LinkedIn link.
- [ ] **Sales & Service:**
    - [ ] **Pricing Tables:** Structured block for Service Tiers (Starter/Pro/Enterprise) with feature checklists.
    - [ ] **FAQ Accordion:** Collapsible questions and answers for handling customer objections.
    - [ ] **Global CTA:** A reusable "Call to Action" strip (e.g., "Book a Demo") for the footer or page bottom.
- [ ] **Content Marketing:**
    - [ ] **Blog App:** Dedicated `BlogPage` with Tags, Categories, and an RSS feed.
    - [ ] **Case Study Model:** A variation of `ProjectPage` focused on "Problem -> Solution -> ROI/Results".

## ✨ Developer Experience (DX)
- [ ] **Template Switcher:** Add a `choices` field to `FlexPage` (and others) to allow users to select from multiple layout templates in the Wagtail Admin.
- [ ] **Migration Reset:** Clean up the migration history before finalizing the v1.0 release (Squash into `0001_initial`).
- [ ] **GitHub Template Config:** Finalize the repository as a GitHub Template for easy project scaffolding.

## 🎨 Design & UI
- [ ] **Tailwind Components:** Expand the available StreamField blocks (e.g., Pricing Tables, FAQs, Testimonials).
- [ ] **Dark Mode Support:** Ensure the base templates and blocks are compatible with Tailwind's dark mode.
- [ ] **Branding & Analytics:**
    - [ ] Integrate `BrandingSettings` (Logo/Favicon) into `base.html`.
    - [ ] Add **Google Analytics ID** field to settings and auto-inject the tracking script if present.

## 📦 Maintenance
- [ ] **Cleanup Imports:** Remove unused imports in `models.py` (e.g., `tempfile`).
- [ ] **Documentation:** Update `README.md` with instructions on how to use the new Form and Template features once implemented.
