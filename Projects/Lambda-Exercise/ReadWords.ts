import * as fs from "fs";

function countWordsInFile(filename: string) {
  fs.readFile(filename, "utf-8", (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    const words = data.split(/\s+/);

    console.log(`There are ${words.length} words in ${filename}`);
  });
}

countWordsInFile(
  "/home/akwasi_akuoko/Projects/AWS/AWS-Restart-Course/README.md"
);
