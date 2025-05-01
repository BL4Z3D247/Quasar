import {
  Connection,
  Transaction,
  TransactionInstruction,
  sendAndConfirmTransaction,
  Keypair
} from '@solana/web3.js';

export function buildInstruction(tradeData: any): TransactionInstruction {
  // TODO: parse tradeData into a Solana instruction
  throw new Error('buildInstruction() not implemented');
}

export async function executeTrade(
  conn: Connection,
  botKeypair: Keypair,
  instruction: TransactionInstruction
) {
  const tx = new Transaction().add(instruction);
  return sendAndConfirmTransaction(conn, tx, [botKeypair]);
}
