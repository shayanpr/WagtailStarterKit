# Project: Wagtail Portfolio Starter Kit

## Overview
This is a production-ready boilerplate for building portfolio websites using **Wagtail CMS**.
It is designed to be a "Golden Master" template—clean, generic, and modular.

## Tech Stack
-   **Backend:** Python / Django / Wagtail CMS.
-   **Frontend:** Tailwind CSS (via CDN), Alpine.js (via CDN).
-   **Interactivity:** Alpine.js for Modals, Slideshows, and Dark Mode.
-   **Dependency Management:** `uv` (modern Python package manager).
-   **Database:** SQLite (default), PostgreSQL ready.

## Core Architecture

### 1. Modular Mixins (DRY Patterns)
-   **`SocialFieldsMixin`:** Unified social media fields used across `TeamMember` snippets and `SocialMediaSettings`.
-   **`BaseStreamBlockMixin`:** A centralized list of all content blocks (`hero_block`, `stats_block`, etc.) shared between `HomePage`, `FlexPage`, and `AboutPage`.

### 2. App Structure
-   **`blocks` App:** The central library for all UI components. All block templates live in `blocks/templates/blocks/`.
-   **`home` App:** Manages the core page models (`HomePage`, `FlexPage`, `AboutPage`) and global site settings.
-   **`portfolio` App:** Specialized for work showcasing. Includes `ProjectIndexPage` and `ProjectPage` with built-in Case Study support.

### 3. Global Logic
-   **Reveal System:** A project-wide animation engine using `IntersectionObserver` in `main.js`. Use classes `.reveal`, `.reveal-fast`, or `.reveal-right`.
-   **Theme Management:** Persistent Dark Mode managed by Alpine.js and Tailwind 'class' mode.
-   **Cinematic Hero:** Dynamic background slideshows with Ken Burns effects, shared across blocks and pages.

## UI & Animation Standards
-   **Roundness:** Standardize on `rounded-3xl` for cards and major containers; `rounded-full` for buttons and tags.
-   **Spacing:** Standard section padding is `py-24` (or `py-20` for smaller blocks).
-   **Grids:** Use `flex-wrap` with `justify-center` and `items-stretch` for lists (Team, Testimonials, Stats) to ensure centering and equal card heights.
-   **Images:** Always use `format-webp` and appropriate crops (`fill-800x600`, `width-1600`) for performance.

## Quick Start (For AI Agents & Developers)

1.  **Install Dependencies:** `uv sync`
2.  **Clean Slate Migration:** `uv run python manage.py makemigrations` and `migrate`.
3.  **Seeding:** Use `uv run python manage.py run_seed` (requires `seed_data.py`).
4.  **Static Assets:** Main logic lives in `config/static/css/main.css` and `config/static/js/main.js`.

## Architectural Conventions
-   **Naming:** Custom blocks must use the `_block` suffix (e.g., `hero_block`) for consistency across StreamFields.
-   **Structure:** Favor Page Fields for high-impact content (like Hero headers) and StreamFields for flexible body content.
-   **Lightbox:** Project galleries use the Alpine.js "Spotlight" modal with navigation and original-image zoom support.
