#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { VpcStack } from '../lib/stacks/vpcStack';
import { DatabaseInfrastructureStack } from '../lib/stacks/databaseInfrastructureStack';
import { awsAccounts } from './config/accounts'

// Create the new app
const app = new cdk.App();

// Get the account information and loop through to create all of the stacks
awsAccounts.forEach(account => {


  const vpcStack = new VpcStack(app, 'VpcStack', {});
  const databaseInfrastructureStack = new DatabaseInfrastructureStack(app, 'DatabaseInfrastructureStack'.concat(account.accountName), vpcStack.vpc, {});
  // Check to see if account needs vpc or not
  if(account.vpc){
    databaseInfrastructureStack.addDependency(vpcStack);
  } 

});
