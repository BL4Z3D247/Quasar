import * as fs from 'fs';
import * as path from 'path';

const logFile = path.resolve(__dirname, '../logs/scout.log');
export function log(msg: string) {
  const line = \`[\${new Date().toISOString()}] \${msg}\n\`;
  fs.appendFileSync(logFile, line);
  console.log(line.trim());
}
