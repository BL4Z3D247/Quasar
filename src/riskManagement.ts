import { Connection, PublicKey } from '@solana/web3.js';

/** Calculate how much SOL to allocate, based on available balance and risk% */
export async function calculatePositionSize(
  conn: Connection,
  botPubkey: PublicKey,
  riskPercent: number
): Promise<number> {
  const lamports = await conn.getBalance(botPubkey);
  const sol = lamports / 1e9;
  return sol * riskPercent;
}

/** Given an entry price, compute stop-loss price */
export function computeStopLoss(entryPrice: number, stopLossPercent: number): number {
  return entryPrice * (1 - stopLossPercent);
}

/** Given an entry price, compute take-profit price */
export function computeTakeProfit(entryPrice: number, takeProfitPercent: number): number {
  return entryPrice * (1 + takeProfitPercent);
}
