module.exports = {
    stylesheet: [
        'https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/2.10.0/github-markdown.min.css',
    ],
    css: `body { max-width: 186mm; margin: 0 auto; }
          .page-break { page-break-after: always; }
          /* .markdown-body { font-size: 11px; } */
          .markdown-body pre > code { white-space: pre-wrap; }`,
    body_class: ['markdown-body'],
    pdf_options: {
        format: "A4",
        margin: "12mm",
        printBackground: true,
        footerTemplate: ' ',
        headerTemplate: `<header style="margin: 0 auto; font-size: 8pt; color: #CCC;">Курс "Web-программирование" 2020 / ПГНИУ</header>`,
    },
    // stylesheet_encoding: "utf-8",
};
