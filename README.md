# Improve Engine

A modern, responsive, and accessible website built with MkDocs and Material theme. Features gradient color themes, light/dark mode, and is optimized for deployment to GitHub Pages and Azure Static Web Apps.

## Features

- ✨ **Beautiful Gradient Design** - Modern gradient color themes throughout the site
- 🌓 **Light/Dark Mode** - Seamless theme switching with system preference support
- 📱 **Fully Responsive** - Optimized for desktop, tablet, and mobile devices
- ♿ **Accessible** - Built with WCAG accessibility guidelines in mind
- 🖼️ **Hero Images** - Eye-catching hero sections on each major page
- 📝 **Blog** - Built-in blog functionality with post categorization and authors
- 🔍 **Search** - Fast, built-in search functionality
- ⚡ **Fast Performance** - Static site generation for lightning-fast load times

## Quick Start

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/itrahulit/improve-engine.git
cd improve-engine
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run local development server:
```bash
mkdocs serve
```

4. Open your browser and navigate to `http://127.0.0.1:8000`

## Building the Site

To build the static site:

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## Deployment

### GitHub Pages

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch via GitHub Actions.

### Azure Static Web Apps

To deploy to Azure Static Web Apps:

1. Create a new Static Web App in Azure Portal
2. Configure the following build settings:
   - App location: `/`
   - Output location: `site`
   - Build command: `pip install -r requirements.txt && mkdocs build`

## Adding Blog Posts

1. Create a new Markdown file in `docs/blog/posts/`
2. Add frontmatter with date, categories, and authors:
```yaml
---
date: 2026-01-30
categories:
  - Category Name
authors:
  - admin
---
```
3. Write your post content
4. Commit and push - the post will automatically appear on the blog page

## Customization

### Colors and Gradients

Edit `docs/stylesheets/extra.css` to customize the gradient color schemes:
- `--gradient-primary`: Main gradient used in header and buttons
- `--gradient-secondary`: Secondary gradient for accents
- `--gradient-accent`: Accent gradient for hover effects

### Theme Settings

Edit `mkdocs.yml` to customize:
- Site name and metadata
- Navigation structure
- Theme colors (primary/accent)
- Plugins and extensions

## Structure

```
improve-engine/
├── docs/
│   ├── assets/
│   │   └── images/          # Images and assets
│   ├── blog/
│   │   ├── .authors.yml     # Blog authors
│   │   ├── index.md         # Blog index page
│   │   └── posts/           # Blog posts
│   ├── stylesheets/
│   │   └── extra.css        # Custom CSS
│   ├── index.md             # Home page
│   └── contact.md           # Contact page
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions workflow
├── mkdocs.yml               # MkDocs configuration
└── requirements.txt         # Python dependencies
```

## License

See [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
