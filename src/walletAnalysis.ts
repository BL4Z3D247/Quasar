import axios from 'axios';
import { API_KEY } from './config';

export interface WalletPerformance {
  address: string;
  pnl: number;
  winRatio: number;
}

export const fetchTopWallets = async (count = 10): Promise<WalletPerformance[]> => {
  const { data } = await axios.get('https://api.example.com/top-wallets', {
    headers: { Authorization: \`Bearer \${API_KEY}\` }
  });
  return data.slice(0, count).map((w: any) => ({
    address: w.address,
    pnl: w.pnl,
    winRatio: w.win_ratio
  }));
};
