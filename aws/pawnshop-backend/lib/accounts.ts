// This file will be for keeping track of config information about accounts
// Example of account
// {
//  accountNumber: 1234567890,
//  region: "us-east-1",
//  
// }

export interface AwsAccount {
    accountName: string;
    accountId: string;
    roleName: string; 
    region: string;
    devAccount: boolean;
  }
  
  export const awsAccounts: AwsAccount[] = [
    {
      accountName: 'kaneDevAccount',
      accountId: '615130240771',
      roleName: 'devRole',
      region: 'us-east-1',
      devAccount: true,
      // Add more details as needed
    },
  ];