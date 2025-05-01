import * as dotenv from 'dotenv';
dotenv.config();

export const API_KEY          = process.env.API_KEY || '';
export const CLUSTER          = process.env.CLUSTER || 'mainnet-beta';
export const TOP_WALLET_COUNT = parseInt(process.env.TOP_WALLET_COUNT || '10', 10);
export const BOT_KEYPAIR_PATH = process.env.BOT_KEYPAIR_PATH || './bot-keypair.json';
export const DRY_RUN          = process.env.DRY_RUN === 'true';
