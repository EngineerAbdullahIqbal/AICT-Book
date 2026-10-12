// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AICT Course Guide',
  tagline: 'A teaching book for the 1-year AICT computer course',
  favicon: 'img/aict-logo.svg',

  // Fonts for the site design (specs/site-design/spec.md §4): Ubuntu for headings,
  // Inter for text, JetBrains Mono for small labels.
  stylesheets: [
    'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&family=Ubuntu:wght@500;700&display=swap',
  ],

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // GitHub Pages: https://engineerabdullahiqbal.github.io/AICT-Book/
  // The deploy workflow sets BASE_URL=/AICT-Book/. Local builds and tests use '/'.
  url: 'https://engineerabdullahiqbal.github.io',
  baseUrl: process.env.BASE_URL ?? '/',
  organizationName: 'EngineerAbdullahIqbal',
  projectName: 'AICT-Book',
  // GitHub Pages adds trailing slashes unless this is set (Docusaurus deployment docs).
  trailingSlash: false,

  // Any broken link, anchor or Markdown link fails the build (research R2).
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  markdown: {
    // Draw ```mermaid code blocks as diagrams (research R3).
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        // Docs-only mode: the book is served at the site root (research R1).
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Dark by default, like the reference design; the switch stays for bright classrooms.
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'AICT Course Guide',
        logo: {
          alt: 'AICT Course Guide logo',
          src: 'img/aict-logo.svg',
          width: 32,
          height: 32,
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'bookSidebar',
            position: 'left',
            label: 'Book',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Learn',
            items: [
              {label: 'Start Reading', to: '/start'},
              {label: 'Module 1: Computer Basics', to: '/module-01-computer-basics'},
              {label: 'Module 4: MS Word', to: '/module-04-ms-word'},
              {label: 'Module 7: MS Excel', to: '/module-07-ms-excel'},
            ],
          },
          {
            title: 'Global Coaching Center',
            items: [
              {label: 'All 16 Modules', to: '/#modules'},
              {label: 'How Every Lesson Works', to: '/#how-it-works'},
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} Global Coaching Center · AICT Course Guide`,
      },
      // neutral prints well and is calm on a projector; dark suits dark mode (research R3).
      mermaid: {
        theme: {light: 'neutral', dark: 'dark'},
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
