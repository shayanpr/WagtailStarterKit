# Project: Wagtail Portfolio Starter Kit

## Overview
This is a production-ready boilerplate for building portfolio websites using **Wagtail CMS**.
It is designed to be a "Golden Master" template—clean, generic, and modular.

## Tech Stack
-   **Backend:** Python / Django / Wagtail CMS.
-   **Frontend:** Tailwind CSS (via CDN for simplicity, extendable via Node).
-   **Dependency Management:** `uv` (modern Python package manager).
-   **Database:** SQLite (default), PostgreSQL ready.

## Core Architecture
1.  **Home App (`home`):**
    -   StreamField-based Page Layouts.
    -   Blocks: Hero, About (RichText), Services (Grid), Featured Projects (Chooser), Contact.
    -   Global Settings: Social Media links, Navigation Menu.
2.  **Portfolio App (`portfolio`):**
    -   `ProjectIndexPage`: A grid-based gallery of work.
    -   `ProjectPage`: A comprehensive case study view with full-screen hero and gallery support (Orderables).
3.  **Global Logic:**
    -   Generic `base.html` using `{% wagtail_site %}` for dynamic branding.
    -   Dynamic Navbar pulling from `NavigationSettings`.

## Quick Start (For AI Agents & Developers)

1.  **Install Dependencies:**
    ```bash
    uv sync
    ```

2.  **Initialize Database (Fresh Start):**
    ```bash
    uv run python manage.py makemigrations
    uv run python manage.py migrate
    ```

3.  **Create Admin User:**
    ```bash
    uv run python manage.py createsuperuser
    ```

4.  **Run Server:**
    ```bash
    uv run python manage.py runserver
    ```

5.  **Mandatory Admin Setup:**
    -   Log in to `/admin`.
    -   Go to **Settings -> Sites** and set the "Site Name" (this acts as your logo).
    -   Create a **Project Index Page** under the Home Page to enable the portfolio.
    -   Populate **Navigation Settings** to see the Navbar links.

## Architectural Conventions
-   **Structure over Hardcoding:** Never hardcode text or URLs in templates; use Wagtail Settings or Page Fields.
-   **Atomic Design:** Keep block templates simple and focused.
-   **Tailwind:** Use utility classes for all styling.
