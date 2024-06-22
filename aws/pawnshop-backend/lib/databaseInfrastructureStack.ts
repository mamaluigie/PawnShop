import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'

export class DatabaseInfrastructureStack extends cdk.Stack {

    constructor(scope: Construct, id: string, vpc: ec2.Vpc, props?: cdk.StackProps) {
        super(scope, id, props); 

        // Creating the customer dynamo database
        const customerTable = new dynamodb.TableV2(this, 'Table', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            sortKey: { name: 'TransactionId', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
          });

        // Creating the database for pawn transactions and for the buy/sell portion
        const buySellTransactionTable = new dynamodb.TableV2(this, 'Table', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            sortKey: { name: 'TransactionId', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
          });
        
          const pawnTransactionsTable = new dynamodb.TableV2(this, 'Table', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            sortKey: { name: 'TransactionId', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
          });

          // Creating the two lambdas that will be used to communicate and experiment with the databases 
          // With doing like crud operations on it and specific queries and stuff

        //   const fn = new lambda.Function(this, 'MyFunction', {
        //     runtime: lambda.Runtime.NODEJS_18_X,
        //     handler: 'index.handler',
        //     code: lambda.Code.fromAsset(path.join(__dirname, 'lambda-handler')),
        //   });
        
    }
}