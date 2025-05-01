import { Connection, clusterApiUrl, Keypair } from '@solana/web3.js';
import * as fs from 'fs';
import {
  fetchTopWallets
} from './walletAnalysis';
import {
  buildInstruction,
  executeTrade
} from './tradeExecution';
import {
  API_KEY,
  CLUSTER,
  TOP_WALLET_COUNT,
  BOT_KEYPAIR_PATH,
  DRY_RUN
} from './config';
import { log } from './logger';

async function loadBotKeypair(): Promise<Keypair> {
  const secret = JSON.parse(fs.readFileSync(BOT_KEYPAIR_PATH, 'utf-8'));
  return Keypair.fromSecretKey(Uint8Array.from(secret));
}

async function main() {
  const conn = new Connection(clusterApiUrl(CLUSTER));
  let botKeypair: Keypair;
  try {
    botKeypair = await loadBotKeypair();
  } catch (err) {
    log(\`Failed loading keypair: \${err}\`);
    process.exit(1);
  }

  let wallets;
  try {
    wallets = await fetchTopWallets(TOP_WALLET_COUNT);
  } catch (err) {
    log(\`fetchTopWallets error: \${err}\`);
    return;
  }

  for (const w of wallets) {
    log(\`Processing \${w.address} (PNL:\${w.pnl}, Win:\${w.winRatio})\`);
    let instr;
    try {
      instr = buildInstruction(w);
    } catch (err) {
      log(\`buildInstruction error for \${w.address}: \${err}\`);
      continue;
    }

    if (DRY_RUN) {
      log(\`Dry-run mode: skipping execution for \${w.address}\`);
      continue;
    }

    try {
      const sig = await executeTrade(conn, botKeypair, instr);
      log(\`Executed trade for \${w.address}: \${sig}\`);
    } catch (err) {
      log(\`executeTrade error for \${w.address}: \${err}\`);
    }
  }
}

main().catch(err => log(\`Unhandled error: \${err}\`));
