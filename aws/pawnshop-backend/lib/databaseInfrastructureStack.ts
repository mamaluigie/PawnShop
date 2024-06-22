import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import * as s3 from 'aws-cdk-lib/aws-s3'

export class DatabaseInfrastructureStack extends cdk.Stack {

    constructor(scope: Construct, id: string, vpc: ec2.Vpc, props?: cdk.StackProps) {
        super(scope, id, props); 

        // Creating the customer dynamo database
        const customerTable = new dynamodb.TableV2(this, 'CustomerTable', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
          });

        // Creating the database for pawn transactions and for the buy/sell portion
        const buySellTransactionTable = new dynamodb.TableV2(this, 'BuySellTransactionTable', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            sortKey: { name: 'TransactionId', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
          });
        
          const pawnTransactionsTable = new dynamodb.TableV2(this, 'PawnTransactionTable', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            sortKey: { name: 'TransactionId', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
          });

        // Creating the s3 buckets containing the pictures of the customers and their items
        const customerPortraitBucket = new s3.Bucket(this, 'CustomerPortraitBucket');
        const customerBuySellItemBucket = new s3.Bucket(this, 'CustomerBuySellItemBucket');
        const customerPawnItemBucket = new s3.Bucket(this, 'CustomerPawnItemBucket');

          // Creating the two lambdas that will be used to communicate and experiment with the databases 
          // With doing like crud operations on it and specific queries and stuff

        //   const fn = new lambda.Function(this, 'MyFunction', {
        //     runtime: lambda.Runtime.NODEJS_18_X,
        //     handler: 'index.handler',
        //     code: lambda.Code.fromAsset(path.join(__dirname, 'lambda-handler')),
        //   });

    }
}