import json
import telegram
import os

from logger import setup_logger
from responses import OK_RESPONSE, ERROR_RESPONSE
from sentry import setup_sentry


logger = setup_logger()
SENTRY_DSN = os.environ.get('SENTRY_DSN')
if not SENTRY_DSN:
    logger.warning('Error tracking disabled due to missing SENTRY_DSN.')
else:
    setup_sentry(SENTRY_DSN)


def configure_telegram():
    """Configures the telegram bot"""
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM TOKEN must be set.')
        raise NotImplementedError
    return telegram.Bot(TELEGRAM_TOKEN)


def webhook(event, context):
    bot = configure_telegram()
    logger.info('Event: {}'.format(event))

    if event.get('httpMethod') == 'POST' and event.get('body'):
        logger.info('Message received')
        update = telegram.Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat.id
        text = update.message.text
        msg = text

        if text == '/health' or text == '/status':
            msg = "I'm alive!"
        elif text == '/whoami':
            f_name = update.message.chat.first_name
            l_name = update.message.chat.last_name
            u_name = update.message.chat.username
            msg = "You are {} {} (@{})".format(f_name, l_name, u_name)
        elif text == '/chatId':
            msg = update.message.chat.id
        elif text == '/error':
            logger.error("Oops, something went wrong!")
            msg = "Oops, something went wrong!"

        bot.sendMessage(chat_id=chat_id, text=msg)
        logger.info('Message sent')

        return OK_RESPONSE
    return ERROR_RESPONSE


def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}/'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage'),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        return OK_RESPONSE
    return ERROR_RESPONSE
