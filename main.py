# This bot is designed to give learn links to users of BeInCrypto

import logging
import os

# import custom assets for the bot
from assets import *

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# get basedir for token file
BASEDIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = BASEDIR + os.sep + "token"

with open(TOKEN_FILE) as token_file:
    token = token_file.read()
    token = token.strip()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# MENUES
def display_start_menu(update, context):
    """Show learning journey articles"""
    update.message.reply_text(
        lernen_menu_message(), reply_markup=lernen_menu(), parse_mode="HTML",
    )


def display_overview_menu(update, context):
    """Show a menu to select categories and get more articles as a nested menu"""
    update.message.reply_text(
        overview_menu_message(), reply_markup=overview_menu(), parse_mode="HTML",
    )


def display_main_menu(update, context):
    """Show Beginner articles"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=overview_menu_message(), reply_markup=overview_menu(), parse_mode="HTML"
    )


def display_lernen_menu(update, context):
    """Show Beginner articles"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=lernen_menu_message(), reply_markup=lernen_menu(), parse_mode="HTML"
    )


def display_beginner_menu(update, context):
    """Show Beginner articles"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=beginner_menu_message(), reply_markup=beginner_menu(), parse_mode="HTML"
    )


def display_advanced_menu(update, context):
    """Show Advanced articles"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=advanced_menu_message(), reply_markup=advanced_menu(), parse_mode="HTML",
    )


def display_pro_menu(update, context):
    """Show pro articles"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=pro_menu_message(), reply_markup=pro_menu(), parse_mode="HTML"
    )


def help_message(update, context):
    """Return a help message to the user"""
    html_string = "<b>Der BeInCrypto Lernen Bot</b>\n\nDie Welt der Kryptowährungen ist oft genau das: kryptisch. Deswegen bieten wir dir hier Inhalte zu den unterschiedlichsten Themen. Für Anfänger und Profis!\n\n<b>So benutzen:</b>\n\n"
    html_string += "<b>/start</b> - Starte deine Lernreise\n\n<b>/menu</b> - Rufe das Hauptmenü auf\n\n<b>/help</b> - Rufe die Hilfenachricht auf\n\n"
    html_string += "Mehr von BeInCrypto findest du auf unserer <a href='https://beincrypto.de'>Website</a>\n& in unserer <a href='https://t.me/BiCDECommunity'> Telegram Gruppe</a>."
    update.message.reply_text(text=html_string, parse_mode="HTML")


def error(update, context):
    """Log warnings"""
    logging.warning(f"Update {update} caused error {context.error}")


# printing out article card to user
def print_article_card(update, context):
    """Function to display the first presentation in telegram"""
    query = update.callback_query
    if query:
        article = query.data
    else:
        article = update.message.text[1:]

    # get logic what card is needed
    html_string = ""
    if article == "wasistbitcoin":
        html_string = wasistbitcoin()
    elif article == "wieentstehenbitcoin":
        html_string = wieentstehenbitcoin()
    elif article == "wasistdefi":
        html_string = wasistdefi()
    elif article == "bitcoinkreditkarte":
        html_string = bitcoinkreditkarte()
    elif article == "stablecoins":
        html_string = stablecoins()
    elif article == "wasistdefi":
        html_string = wasistdefi()
    elif article == "bitcoinboerse":
        html_string = bitcoinboerse()
    elif article == "appstrading":
        html_string = tradingapps()
    elif article == "telegramtop10":
        html_string = telegramtop10()
    elif article == "cloudmining":
        html_string = cloudmining()
    elif article == "investmentapps":
        html_string = investmentapps()
    elif article == "xrpkaufen":
        html_string = xrpkaufen()
    elif article == "kryptotools":
        html_string = kryptotools()
    elif article == "einfachbitcoin":
        html_string = einfachbitcoin()
    elif article == "leveragetrading":
        html_string = leveragetrading()
    elif article == "steuerbitcoin":
        html_string = steuerbitcoin()
    elif article == "bitcoinderivate":
        html_string = bitcoinderivate()
    elif article == "blockchainonline":
        html_string = blockchainonline()
    elif article == "bottrading":
        html_string = bottrading()
    elif article == "scamerkennen":
        html_string = scamerkennen()
    elif article == "dapps2020":
        html_string = dapps2020()
    elif article == "p2pboersen":
        html_string = p2pboersen()
    elif article == "blockchainfirmen":
        html_string = blockchainfirmen()

    # send out article card
    if query:
        query.answer()
        query.edit_message_text(
            text=html_string, parse_mode="HTML",
        )
    else:
        update.message.reply_text(text=html_string, parse_mode="HTML")


def main():
    """Run the telegram bot with commands"""
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("wasistbitcoin", print_article_card))
    dp.add_handler(CommandHandler("wieentstehenbitcoin", print_article_card))
    dp.add_handler(CommandHandler("wasistdefi", print_article_card))
    dp.add_handler(CommandHandler("help", help_message))

    # display menues
    dp.add_handler(CommandHandler("menu", display_overview_menu))
    dp.add_handler(CommandHandler("start", display_start_menu))

    # callback for menus
    dp.add_handler(CallbackQueryHandler(display_advanced_menu, pattern="advanced_menu"))
    dp.add_handler(CallbackQueryHandler(display_beginner_menu, pattern="beginner_menu"))
    dp.add_handler(CallbackQueryHandler(display_pro_menu, pattern="pro_menu"))
    dp.add_handler(CallbackQueryHandler(display_lernen_menu, pattern="lernen_menu"))
    dp.add_handler(CallbackQueryHandler(display_main_menu, pattern="overview"))

    # callback for article cards
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="wasistbitcoin"))
    dp.add_handler(
        CallbackQueryHandler(print_article_card, pattern="wieentstehenbitcoin")
    )
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="wasistdefi"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="stablecoins"))
    dp.add_handler(
        CallbackQueryHandler(print_article_card, pattern="bitcoinkreditkarte")
    )
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="bitcoinboerse"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="appstrading"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="telegramtop10"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="cloudmining"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="investmentapps"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="xrpkaufen"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="kryptotools"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="einfachbitcoin"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="leveragetrading"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="steuerbitcoin"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="bitcoinderivate"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="blockchainonline"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="bottrading"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="scamerkennen"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="dapps2020"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="p2pboersen"))
    dp.add_handler(CallbackQueryHandler(print_article_card, pattern="blockchainfirmen"))

    # Error
    dp.add_error_handler(error)

    # Start Bot and run
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
