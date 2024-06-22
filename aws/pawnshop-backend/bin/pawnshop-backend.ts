#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { VpcStack } from '../lib/vpcStack';
import { DatabaseInfrastructureStack } from '../lib/databaseInfrastructureStack';

const app = new cdk.App();
const vpcStack = new VpcStack(app, 'VpcStack', {});
new DatabaseInfrastructureStack(app, 'DatabaseInfrastructureStack', vpcStack.vpc, {});

// new NewStack can go here(app, '<new stack>', {});