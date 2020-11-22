const fs = require('fs/promises');
const path = require('path');
const { writeFile } = require('fs/promises');
const { resolve } = require('path');
const { mdToPdf } = require('md-to-pdf');
const config = require('./configs/md-to-pdf');
const pdfConfig = { ...config, basedir: resolve(__dirname, '..') };
const htmlConfig = { ...pdfConfig, as_html: true };

async function findFilesInDir(startPath, filterRe) {
  const files = await fs.readdir(startPath);
  return files.reduce(async (result, file) => {
    const filename = path.join(startPath, file);
    if ((await fs.lstat(filename)).isDirectory()) {
      const newFiles = await findFilesInDir(filename, filterRe);
      return result.then((list) => list.concat(newFiles));
    } else if (filterRe.test(filename)) {
      return result.then((list) => list.concat([filename]));
    }
    return result;
  }, Promise.resolve([]));
}

const buildFromMdFiles = async (files, types) =>
  files.reduce(
    (chain, path, index) =>
      chain.then(async () => {
        if (types.includes('html')) {
          await mdToPdf({ path }, htmlConfig).then((pdf) => writeFile(path.replace(/\.md$/, '.html'), pdf.content));
        }
        if (types.includes('pdf')) {
          await mdToPdf({ path }, pdfConfig).then((pdf) => writeFile(path.replace(/\.md$/, '.pdf'), pdf.content));
        }
        console.log(`[${index + 1}/${files.length}] ${path}`);
      }),
    Promise.resolve(),
  );

async function buildInDir(dir, types = ['html', 'pdf']) {
  const files = await findFilesInDir(dir, /\.md$/);
  console.log(`Build ${types.toString()} in ${dir}...`);
  return buildFromMdFiles(files, types);
}

module.exports = {
  buildInDir,
  buildFromMdFiles,
};
