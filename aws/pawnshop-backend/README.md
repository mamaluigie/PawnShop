# Welcome to your CDK TypeScript project

This is a blank project for CDK development with TypeScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template


How to update the aws account stacks
First you will have to bootstrap the aws account.
- Make sure that you verify with the command line in the .aws/config file your user credentials. 
  You can also do this through a command to update that instead of manually doing it.
- Next make sure that the application is built and bootstrapped propperly<br>
  ```aws bootstrap```
- Now list all of the stacks that you would like to deploy or work with <br>
  ```aws list```<br>

  ```
     Stack1
     Stack2
     Stack3
     ```
- Deploy the chosen stack that you want <br>
  ```aws deploy <stack name>```



The entry point for the application is in the bin directory in the app ts file

To define multiple stacks we must do it in there


Dynamodb will store the account information and in dynamodb there will be a link to the rds database instance that will contain each of the items that person has either bought, sold, or pawned to me.

The dynamodb instance will have only account information so this is the attributes each item will have

partition key = hash(first name, last name, <identifying number or drivers license number>)
- the logic behind this is that they can have a card that has their number/barcode on it. I can scan this and it will pull up their account instantly. If they dont have this I can still look it up super quick with their first name, last name, and govt issued id number.

First name
Last name
Race
Age
Address
Eye color
Height
Weight
phone number
email
link to items to the rds instance for bought, sold, or pawned items

The RDS instance will contain these values for representing the pawn shop items
Item category
Item condition 1-5




