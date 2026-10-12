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
  favicon: 'img/favicon.ico',

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
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'AICT Course Guide',
        logo: {
          alt: 'AICT Course Guide',
          src: 'img/logo.svg',
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
        copyright: `Copyright © ${new Date().getFullYear()} AICT Course Guide. Built with Docusaurus.`,
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
