// generatePdfPRG.js
const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('PRGExplanation.pdf'));

const content = `why the PRG gov does not "almost love it" if people would live like north koreas, but that he sure does: Perfect example of why you don’t want to use Chinese tech. Its censored, the government there would almost love it if the people would live a lie like North Koreans.`;

doc.font('Times-Roman').fontSize(12).text(content, { lineGap: 4 });

doc.end();