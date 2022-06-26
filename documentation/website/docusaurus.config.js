// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "PyZNN Docs",
  tagline: "Python SDK for interacting with the Zenon network and ecosystem.",
  url: "https://your-docusaurus-test-site.com",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "millerships", // Usually your GitHub org/user name.
  projectName: "pyznn", // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: "PyZNN",
        logo: {
          alt: "PyZNN Logo",
          src: "img/logo.svg",
        },
        items: [
          {
            type: "doc",
            docId: "installation",
            position: "left",
            label: "Documentation",
          },
          {
            href: "https://github.com/facebook/docusaurus",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "Install",
                to: "/docs/installation",
              },
              {
                label: "JSON-RPC client",
                to: "/docs/json-rpc-client",
              },
              {
                label: "Wallet",
                to: "/docs/wallet",
              },
            ],
          },
          {
            title: "Community",
            items: [
              {
                label: "Forum",
                href: "https://forum.zenon.org/",
              },
              {
                label: "Website",
                href: "https://zenon.network/",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/Zenon_Network",
              },
            ],
          },
        ],
        copyright: "Built with Docusaurus",
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
