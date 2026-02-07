JANE_DOE_HOME = [
    (
        "hero",
        {
            "title": "Jane Doe",
            "subtitle": "Creative Developer & Architect",
            "image_url": "https://picsum.photos/1200/800",
        },
    ),
    (
        "about",
        {
            "heading": "About Me",
            "content": """
                <p>I am a creative developer with a passion for building clean, efficient, and beautiful web experiences. With a background in both architecture and software engineering, I bring a unique perspective to every project.</p>
                <p>My goal is to bridge the gap between complex functionality and elegant design, ensuring that every user interaction is meaningful and intuitive.</p>
            """,
        },
    ),
    (
        "services",
        {
            "heading": "My Specialized Services",
            "services": [
                {
                    "title": "Full-Stack Development",
                    "description": "<p>Robust backend systems powered by Django and Python, combined with dynamic React-based frontends.</p>",
                },
                {
                    "title": "Interactive 3D Environments",
                    "description": "<p>Creating immersive web experiences using Three.js and modern WebGL techniques.</p>",
                },
                {
                    "title": "Wagtail CMS Architecture",
                    "description": "<p>Custom CMS implementations that give content editors complete control over their digital presence.</p>",
                },
                {
                    "title": "Cloud Infrastructure",
                    "description": "<p>Scalable deployment strategies using Docker, AWS, and modern CI/CD pipelines.</p>",
                },
            ],
        },
    ),
    (
        "grid",
        {
            "grid_title": "My Working Process",
            "columns": [
                [
                    ("heading", "01. Discovery"),
                    (
                        "paragraph",
                        "<p>We deep-dive into your business goals, target audience, and technical requirements to build a solid foundation.</p>",
                    ),
                ],
                [
                    ("heading", "02. Strategy"),
                    (
                        "paragraph",
                        "<p>Creating a detailed roadmap, wireframes, and technical architecture to ensure the project stays on track.</p>",
                    ),
                ],
                [
                    ("heading", "03. Execution"),
                    (
                        "paragraph",
                        "<p>The build phase where design and code come together through iterative development and constant feedback.</p>",
                    ),
                ],
                [
                    ("heading", "04. Support"),
                    (
                        "paragraph",
                        "<p>Beyond launch, I provide ongoing maintenance and performance optimization to ensure long-term success.</p>",
                    ),
                ],
            ],
        },
    ),
    (
        "showcase",
        {
            "heading": "Featured Case Studies",
            "intro": "A selection of my recent work focusing on technical complexity and user-centric design.",
            "projects": [],
        },
    ),
    (
        "contact",
        {
            "heading": "Let's Build Something Together",
            "text": "Whether you have a specific project in mind or just want to explore the possibilities, I'm always open to discussing new opportunities.",
        },
    ),
    (
        "comparison",
        {
            "heading": "Standard Service Tiers",
            "tiers": [
                {
                    "name": "Starter",
                    "description": "Perfect for personal projects",
                    "price_or_label": "$499",
                    "features": ["Single Page App", "Wagtail CMS", "1 Month Support"],
                    "button_text": "Select Starter",
                    "target": "contact"
                },
                {
                    "name": "Professional",
                    "description": "Best for growing businesses",
                    "price_or_label": "$1,499",
                    "features": ["Multi-page Site", "Custom Blocks", "SEO Optimization", "3 Months Support"],
                    "is_featured": True,
                    "button_text": "Go Pro",
                    "target": "contact"
                },
                {
                    "name": "Enterprise",
                    "description": "For high-scale applications",
                    "price_or_label": "Custom",
                    "features": ["Cloud Infrastructure", "API Integrations", "Advanced Security", "Priority Support"],
                    "button_text": "Contact Sales",
                    "target": "contact"
                }
            ]
        }
    ),
]

CLOUD_SERVICES_PAGE_DATA = {
    "title": "Cloud Infrastructure Services",
    "slug": "cloud-services",
    "body": [
        (
            "hero",
            {
                "title": "Scalable Cloud Architecture",
                "subtitle": "High-performance infrastructure for modern web applications.",
                "image_url": "https://picsum.photos/1200/800?random=10"
            }
        ),
        (
            "grid",
            {
                "grid_title": "Our Infrastructure Stack",
                "columns": [
                    [
                        ("heading", "Docker & Kubernetes"),
                        ("paragraph", "<p>Containerized workflows for consistent development and deployment across all environments.</p>")
                    ],
                    [
                        ("heading", "AWS & Azure"),
                        ("paragraph", "<p>Leveraging the power of global cloud providers to ensure 99.9% uptime and global reach.</p>")
                    ]
                ]
            }
        ),
        (
            "comparison",
            {
                "heading": "Cloud Hosting Plans",
                "tiers": [
                    {
                        "name": "Basic VPS",
                        "price_or_label": "$10/mo",
                        "features": ["2GB RAM", "1 vCPU", "50GB SSD"],
                        "target": "contact"
                    },
                    {
                        "name": "Pro Cluster",
                        "price_or_label": "$150/mo",
                        "features": ["16GB RAM", "8 vCPU", "500GB SSD", "Auto-scaling"],
                        "is_featured": True,
                        "target": "contact"
                    }
                ]
            }
        )
    ]
}

PROJECT_INDEX_DATA = {
    "title": "Selected Work",
    "slug": "work",
    "intro": "Explore my latest development and design projects.",
}

PROJECTS_DATA = [
    {
        "title": "Eco-Friendly Dashboard",
        "slug": "eco-dashboard",
        "client": "GreenFuture Inc.",
        "image_url": "https://picsum.photos/800/600?random=1",
        "body": "<p>An interactive dashboard designed to track carbon footprints in real-time using IoT sensors and data visualization.</p>",
    },
    {
        "title": "Virtual Museum Tour",
        "slug": "museum-vr",
        "client": "National Arts Foundation",
        "image_url": "https://picsum.photos/800/600?random=2",
        "body": "<p>A high-performance WebGL experience allowing users to explore historical artifacts in a 360-degree digital environment.</p>",
    },
    {
        "title": "Secure Fintech API",
        "slug": "fintech-api",
        "client": "SwiftPay Systems",
        "image_url": "https://picsum.photos/800/600?random=3",
        "body": "<p>A robust and secure RESTful API built to handle high-volume financial transactions with multi-layered encryption.</p>",
    },
]

SOCIAL_DATA = {
    "email": "jane@doe.com",
    "linkedin": "https://linkedin.com/in/janedoe",
    "github": "https://github.com/janedoe",
    "twitter": "https://twitter.com/janedoe",
}

# Generic external links for testing the extra_links StreamField
EXTRA_SOCIAL_DATA = [
    {"platform_name": "Google", "url": "https://google.com"},
    {"platform_name": "YouTube", "url": "https://youtube.com"},
]
# For navigation, we provide the titles. The script will link them to the correct pages.
NAV_DATA = [
    {"title": "Home", "target": "home"},
    {"title": "Cloud", "target": "cloud"},
    {"title": "Work", "target": "work"},
    {"title": "Contact", "target": "contact"},
]
CONTACT_PAGE_DATA = {
    "title": "Contact Me",
    "slug": "contact",
    "intro": "<p>Have a project in mind? I'd love to hear from you. Fill out the form below and I'll get back to you as soon as possible.</p>",
    "thank_you_text": "<p>Thanks for your message! I usually respond within 24 hours.</p>",
    "from_address": "no-reply@janedoe.com",
    "to_address": "jane@doe.com",
    "subject": "New Portfolio Inquiry",
}

CONTACT_FORM_FIELDS = [
    {"label": "Full Name", "field_type": "singleline", "required": True},
    {"label": "Email Address", "field_type": "email", "required": True},
    {"label": "Subject", "field_type": "singleline", "required": False},
    {"label": "Message", "field_type": "multiline", "required": True},
]
