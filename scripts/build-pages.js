const { buildFromMdFiles } = require('./utils');

buildFromMdFiles(['README.md', 'Plan.md', 'Exam.md', 'DEVELOPMENT.md', 'CONTRIBUTING.md'], ['html'])
  .then(() => {
    console.log('Done');
  })
  .catch((e) => {
    console.log(e.message);
    console.error(e);
  });
