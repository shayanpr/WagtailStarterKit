# 🚀 Wagtail Starter Kit

Hi! I'm Khashayar. I built this starter kit because I was tired of setting up the same things over and over again. I wanted a cleaner, faster, and more beautiful way to launch Wagtail projects that look great right from the start.

This is a high-end, production-ready boilerplate for professional portfolios and blogs, powered by **Wagtail CMS**, **Tailwind CSS**, and **Alpine.js**. I've designed it to be a "Golden Master"—clean, modular, and optimized for both human developers and AI agents.

---

## 📦 What you get out of the box

-   **🏢 Clean, Modular Component-Based Architecture:** I've separated the Business/Home logic from the Portfolio/Blog logic to keep things tidy.
-   **📰 A Professional Blog Engine:** You get full Category and Tag support with editorial card-based layouts.
-   **🎨 Cinematic UI:** I included dynamic Alpine.js slideshows with Ken Burns effects and a custom scroll-reveal animation system.
-   **🛠️ Reusable Modular Blocks:** A library of 15+ custom StreamField blocks (FAQ, Pricing, Team, Stats, CTAs) that you can drop anywhere.
-   **🌓 Built-in Dark Mode:** Full theme support managed via Alpine.js and Tailwind.
-   **📱 Speed & Responsiveness:** It's fast, mobile-friendly, and uses optimized `webp` images.
-   **🤖 AI-First Design:** The code structure is organized so that AI coding assistants can understand and help you manage it easily.

---

## 🛠️ The tools I chose

-   **Backend:** Python 3.14+ / Django 5.1+ / Wagtail 6.2+
-   **Frontend:** Tailwind CSS (with the Typography plugin) and Alpine.js for that lightweight interactivity.
-   **Packaging:** `uv` — because life is too short for slow dependency management.
-   **Database:** SQLite is the default for easy development, but it's PostgreSQL ready.

---

## 🚀 Quick Start

### 0. Prerequisites
You'll need **Python 3.14+** installed (Lower versions would probably work, but you need to change some files). If you haven't tried **uv** yet, I highly recommend it:
```bash
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1. Installation
```bash
git clone https://github.com/shayanpr/WagtailStarterKit.git
cd WagtailStarterKit
uv sync
```

### 2. Database Setup (Fresh Start)
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

### 3. Run the Server
```bash
uv run python manage.py runserver
```

### 4. Visit the Admin Panel 

Visit [http://localhost:8000/admin](http://localhost:8000/admin), login with your super user you made in step 2, and start building. 

---

## 🏗️ How I organized the code

-   **`blocks/`**: This is your UI library. All the custom components and StreamField logic live here.
-   **`home/`**: Manages the site structure, global settings (like Branding and Navigation), and your landing pages.
-   **`portfolio/`**: Specialized models for showcasing your work and case studies.
-   **`blog/`**: Modern article management with all the taxonomy you need.
-   **`config/`**: Where the Django settings and project-wide static assets live.

---

## ⚖️ License

I've released this under the **MIT License**, so feel free to use it for whatever you like! See the `LICENSE` file for the legal bits.

Built with ❤️ by **KHASHAYAR FARSHCHI**.
