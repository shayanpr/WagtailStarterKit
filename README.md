# Wagtail Portfolio Starter Kit

A professional, production-ready boilerplate for building portfolio websites with **Wagtail CMS** and **Tailwind CSS**.

AI was used in the making of this project.

## Features
*   **Modular Architecture:** Separate apps for Landing Page (`home`) and Portfolio (`portfolio`).
*   **Dynamic Layouts:** StreamField-based page construction.
*   **Built-in Gallery:** Dedicated project management with Orderable image galleries.
*   **SEO Optimized:** Pre-configured metadata and reusable templates.
*   **Modern Stack:** Python 3.14+, Django 6+, Wagtail 7+, Tailwind CSS (via CDN).

## Quick Start

1.  **Install:**
    ```bash
    git clone https://github.com/shayanpr/WagtailStarterKit.git
    uv sync
    ```

2.  **Initialize:**
    ```bash
    uv run python manage.py makemigrations
    uv run python manage.py migrate
    uv run python manage.py createsuperuser
    ```

3.  **Run:**
    ```bash
    uv run python manage.py runserver
    ```

## Post-Install Setup
*   Log in to `/admin`.
*   Go to **Settings > Sites** and update the Site Name (this updates the logo).
*   Create your **HomePage** and **Project Index Page**.
*   Configure **Navigation** and **Social Media** in Settings.

Built with ❤️ using `uv`.
