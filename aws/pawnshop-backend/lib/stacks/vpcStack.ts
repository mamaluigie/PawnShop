import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { awsAccounts } from '../../bin/config/accounts'
import * as rds from 'aws-cdk-lib/aws-rds';
import * as ec2 from 'aws-cdk-lib/aws-ec2';

// This stack is to just set up the skeleton for the infrastructure like vpc and connectivity stuff
export class VpcStack extends cdk.Stack {

  public readonly vpc: ec2.Vpc;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

      // Defining a new vpc for everything to lie in
      this.vpc = new ec2.Vpc(this, 'Vpc', {
      });
      
  }
}
