# Serverless Tryout

This is a try-out project using the [serverless](https://serverless.com) framework to create a serverless python application on AWS.

## Deploy
You need to [install serverless](https://serverless.com/framework/docs/getting-started/) locally.

Before you can deploy the code to AWS you need to set up your AWS profile locally so that it can be used by serverless. See [this](https://serverless.com/framework/docs/providers/aws/guide/credentials/) for more information.

In the `serverless.yml` file you can change the parameters according to the profile you set and the region you would like to deploy your serverless function.

You should set up the `serverless.env.yml` file to contain the following:
```yaml
TELEGRAM_TOKEN: <your token here>
SENTRY_DSN: https://<your dsn entry here>
```

Once set up you can deploy the function to AWS by running:
```bash
serverless deploy
```

## Acknowledgements
- [serverless/examples](https://github.com/serverless/examples/tree/master/aws-python-telegram-bot) for the telegram bot example.
