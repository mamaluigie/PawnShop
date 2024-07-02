import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';

import * as path from 'path';

export class DatabaseInfrastructureStack extends cdk.Stack {

    constructor(scope: Construct, id: string, vpc?: ec2.Vpc, props?: cdk.StackProps) {
        super(scope, id, props); 

        // Creating the two lambdas that will be used to communicate and experiment with the databases 
        // With doing like crud operations on it and specific queries and stuff
        // This function will be used to send various commands/flags to the lambda function with 
        // data attatched in order to interact with the database.

        // Creating the customer dynamo database
        const customerTable = new dynamodb.TableV2(this, 'CustomerTable', {
            partitionKey: { name: 'StoreIdNumber', type: dynamodb.AttributeType.STRING },
            pointInTimeRecovery: true,
        });

        const crudFunction = new lambda.Function(this, 'CrudLambdaFunction', {
          runtime: lambda.Runtime.PYTHON_3_12,
          handler: 'CrudHandler.handler',
          code: lambda.Code.fromAsset(path.join(__dirname, '../../assets/CrudHandler/')),
          environment: {
            'DATABASE_NAME':customerTable.tableArn,
          }
        });

        // Grant permission for read and write for the crud lambda function
        customerTable.grantReadWriteData(crudFunction);

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

        // Setting the permissions for being able to read and write for the lambda function
        buySellTransactionTable.grantReadWriteData(crudFunction);
        pawnTransactionsTable.grantReadWriteData(crudFunction);

        // Creating the s3 buckets containing the pictures of the customers and their items
        const customerPortraitBucket = new s3.Bucket(this, 'CustomerPortraitBucket',{
          blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
          publicReadAccess: false,
          removalPolicy: cdk.RemovalPolicy.RETAIN,
        });
        const customerBuySellItemBucket = new s3.Bucket(this, 'CustomerBuySellItemBucket',{
          blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
          publicReadAccess: false,
          removalPolicy: cdk.RemovalPolicy.RETAIN,
        });
        const customerPawnItemBucket = new s3.Bucket(this, 'CustomerPawnItemBucket',{
          blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
          publicReadAccess: false,
          removalPolicy: cdk.RemovalPolicy.RETAIN,
        });

        // Setting the permissions for the crud function to upload to the s3 buckets also
        customerPortraitBucket.grantReadWrite(crudFunction);
        customerBuySellItemBucket.grantReadWrite(crudFunction);
        customerPawnItemBucket.grantReadWrite(crudFunction);
    }
}