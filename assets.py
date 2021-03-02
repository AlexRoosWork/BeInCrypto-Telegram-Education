# hold the assets for the bic lernen bot
# article cards
# menues
# menu messages

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ARTICLE Cards
def wasistbitcoin():
    html_string = "<b>Was ist Bitcoin?\nDie Anleitung für Anfänger</b>"
    html_string += "\n\n<a href='https://bit.ly/32mNq5E'><b>+ Exklusive Slides</b></a>\n<a href='https://bit.ly/3fASxTI'><b>+ Vollständiger Artikel</b></a>"
    html_string += "\n\nIn dieser Lektion bekommst du nicht nur den Überblick über Bitcoin, sondern auch noch eine <b>einfache Anleitung zur ersten Bitcoin Wallet</b>. Damit hast du den perfekten Start in die Krypto-Welt."
    return html_string


def wieentstehenbitcoin():
    html_string = (
        "<b>Wie entstehen neue Bitcoin?\nEinführung in Blockchain und Mining</b>"
    )
    html_string += "\n\n<a href='https://bit.ly/3hDMizd'><b>+ Exklusive Slides</b></a>\n<a href='https://bit.ly/39llErF'><b>+ Vollständiger Artikel</b></a>"
    html_string += "\n\n<b>Empfohlenes Vorwissen:\n/wasistbitcoin </b>"
    html_string += "\n\nWir blicken auf die Bitcoin Blockchain und klären die Frage 'Wo leben Bitcoins?' Außerdem: 'Wie entstehen neue Bitcoin?' und 'Warum haben Bitcoin einen Wert?'"
    return html_string


def wasistdefi():
    html_string = "<b>Was ist DeFi?</b>"
    html_string += "\n\n<a href='https://bit.ly/33me67p'><b>+ Exklusive Slides</b></a>\n<a href='https://bit.ly/2EzAwaM'><b>+ Vollständiger Artikel</b></a>"
    html_string += (
        "\n\n<b>Empfohlenes Vorwissen:\n/wasistbitcoin\n/wieentstehenbitcoin</b>"
    )
    html_string += "\n\nHier bekommst du einen Überblick über die DeFi Industrie. Im Jahr 2020 ist DeFi <i>der</i> Trend und deswegen betrachten wir die größten Anwendungsfelder und die erfolgreichsten Projekte"
    return html_string


def stablecoins():
    html_string = "<b>Die besten Stablecoins im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2DbHhPy'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += (
        "\n\n<b>Empfohlenes Vorwissen:\n/wasistbitcoin\n/wieentstehenbitcoin</b>"
    )
    html_string += "\n\nWas ist ein Stablecoin und was sind die populärsten Projekte?"
    return html_string


def bitcoinkreditkarte():
    html_string = "<b>Wie kann ich Bitcoin mit Kreditkarte kaufen?</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/3i08zqR'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += (
        "\n\n<b>Empfohlenes Vorwissen:\n/wasistbitcoin\n/wieentstehenbitcoin</b>"
    )
    html_string += "\n\nKreditkarten zählen zu den beliebtesten Zahlungsmethoden. In diesem Artikel schauen wir uns an, wie man Bitcoin mit Kreditkarte kaufen kann."
    return html_string


def bitcoinboerse():
    html_string = "<b>Die besten Krypto-Börsen für Bitcoin im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2Xi7naw'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\n<b>Empfohlenes Vorwissen:\n/wasistbitcoin</b>"
    html_string += "\n\nEs gibt zahlreiche Börsen, die den Verkauf von Bitcoin anbieten. Wir schauen uns einige der besten Krypto-Börsen an."
    return html_string


def tradingapps():
    html_string = "<b>Die 7 besten Trading Apps im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2PjSSyx'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nWenn Du dich für das Trading interessierst, findest du hier eine Übersicht der 7 besten Trading Apps.\n<b>Vorsicht beim Traden!</b>"
    return html_string


def telegramtop10():
    html_string = "<b>Die Top 10 der besten Telegram Kanäle für Preissignale</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2DvDFHW'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nFalls Du deine Trading Signale von einer Telegram Gruppe bekommen möchtest, findest Du hier die Top 10 der Telegram Kanäle für Krypto-Signale.\n<b>Vorsicht beim Traden!</b>"
    return html_string


def cloudmining():
    html_string = "<b>Die besten Cloud Mining Dienste in 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2Ph2h9Z'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\n<b>Empfohlenes Vorwissen:\n/wieentstehenbitcoin</b>"
    html_string += "\n\nWer sich im Mining ausprobieren will, allerdings keine Tausenden Euro für Hardware bereit hat, kann sich beim Cloud Mining umschauen."
    return html_string


def investmentapps():
    html_string = "<b>Die besten Investment- und Trading Apps in 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/33kOQyj'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nInvestieren ist dank dem Internet so einfach wie nie zuvor. Hier eine Übersicht über die besten Apps im Jahr 2020."
    return html_string


def xrpkaufen():
    html_string = "<b>Wie kann ich Ripple XRP kaufen?</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/3fpr9XK'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nDie digitale Währung Ripple XRP zu kaufen ist einfach. Hier ein kleiner Guide."
    return html_string


def kryptotools():
    html_string = "<b>Die 30 besten Krypto-Tools im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2PlqWdA'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nEine Übersicht über viele verschiedene Tools in der Kryptowelt. Von Wallet bis Blockexplorer."
    return html_string


def einfachbitcoin():
    html_string = "<b>In wenigen Schritten die ersten Bitcoin kaufen</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/38ZPfXJ'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\n<b>Empfohlenes Vorwissen: /wasistbitcoin</b>"
    html_string += "\n\nFür ein bisschen Starthilfe, wenn Du dir unsicher bist, wie man Bitcoins kauft."
    return html_string


def leveragetrading():
    html_string = "<b>Bitcoin Margin Trading:</b> Profite mit Leverage maximieren"
    html_string += (
        "\n\n<a href='https://bit.ly/30pv2bb'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nWie funktioniert Trading mit Leverage? Wir geben einen kurzen Überblick über die Margin Trading bei Bitcoin und einige der möglichen Exchanges.\n\n<b>Vorsicht beim Trading mit Leverage!</b>"
    return html_string


def steuerbitcoin():
    html_string = "<b>Wie muss ich Bitcoin Gewinne versteuern?</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/30pv2bb'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nWer Gewinne aus dem Kauf- und Verkauf von Bitcoin erzielt, muss diese versteuern. Doch war da nicht noch etwas mit einer einjährigen Haltefrist?\n\n"
    return html_string


def steuerbitcoin():
    html_string = "<b>Wie muss ich Bitcoin Gewinne versteuern?</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/30pv2bb'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nWer Gewinne aus dem Kauf- und Verkauf von Bitcoin erzielt, muss diese versteuern. Doch war da nicht noch etwas mit einer einjährigen Haltefrist?\n\n"
    return html_string


def bitcoinderivate():
    html_string = "<b>Die besten Bitcoin Derivate Exchanges im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/3k4FU5P'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nDer Handel von Bitcoin geht weit über den Spot-Market hinaus. Hier siehst Du wo man Bitcoin Derivate handeln kann.\n\n"
    return html_string


def blockchainonline():
    html_string = "<b>Die besten Blockchain Online Kurse im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2DcEo12'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\n<b>Empfohlenes Vorwissen:\nEnglisch</b>"
    html_string += "\n\nWenn Du eine Karriere in der Blockchain Industrie anstrebst, findest du hier weiterführende Blockchain Online Kurse.\n\n"
    return html_string


def bottrading():
    html_string = "<b>Die besten Krypto Bots für automatisches Trading</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/3k489Sg'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nDas Trading im 21sten Jahrhundert lässt sich größtenteils automatisieren. Hier findest Du einige der populärsten Trading Bots für die Aufgabe.\n<b>Wie immer: Vorsicht beim Traden</b>\n"
    return html_string


def scamerkennen():
    html_string = "<b>Wie erkenne ich einen Scam?</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/39OfaBU'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nIm Wilde Westen der Kryptowährungen tummeln sich die Scams und Betrugsmaschen.\n<b>Wir zeigen dir, wie Du einen Scam spotten kannst</b> und besprechen einige der größten Scams der Vergangenheit.\n"
    return html_string


def dapps2020():
    html_string = "<b>Die populärsten dApps im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/2PmO5ME'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nEine Übersicht der beliebtesten dApps im Jahr 2020."
    return html_string


def p2pboersen():
    html_string = "<b>Die besten Peer to Peer Börsen im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/30kKIMM'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nDie gleichen Prinzipien der Dezentralität Bitcoins, lassen sich auch auf Krypto-Börsen selbst anwenden. Eine Übersicht der Peer to Peer Börsen."
    return html_string


def blockchainfirmen():
    html_string = "<b>Die besten Blockchain Unternehmen im Jahr 2020</b>"
    html_string += (
        "\n\n<a href='https://bit.ly/3i61Bkp'><b>+ Vollständiger Artikel</b></a>"
    )
    html_string += "\n\nHier findest Du eine Liste der größten Blockchain Unternehmen. Neben ConsenSys spielen nämlich auch Giganten wie IBM, Amazon und Microsoft mit."
    return html_string


# KEYBOARDS
def lernen_menu():
    """Guided Learning Experience Menu"""
    keyboard = [
        [
            InlineKeyboardButton(
                "Lektion 1: Was ist Bitcoin?", callback_data="wasistbitcoin",
            )
        ],
        [
            InlineKeyboardButton(
                "Lektion 2: Wie entstehen Bitcoin?",
                callback_data="wieentstehenbitcoin",
            )
        ],
        [InlineKeyboardButton("Lektion 3: Was ist DeFi?", callback_data="wasistdefi",)],
    ]
    keyboard.append(back_button())
    return InlineKeyboardMarkup(keyboard)


def overview_menu():
    """Category Menu"""
    keyboard = [
        [InlineKeyboardButton("Der erste Anfang", callback_data="lernen_menu")],
        [InlineKeyboardButton("Einsteiger", callback_data="beginner_menu")],
        [InlineKeyboardButton("Advanced", callback_data="advanced_menu")],
        [InlineKeyboardButton("Profi", callback_data="pro_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)


def beginner_menu():
    """Beginner Menu"""
    keyboard = [
        [
            InlineKeyboardButton(
                "Wie kann ich Bitcoin mit Kreditkarte kaufen?",
                callback_data="bitcoinkreditkarte",
            )
        ],
        [
            InlineKeyboardButton(
                "Bitcoin bei XCOEX kaufen", callback_data="einfachbitcoin"
            )
        ],
        [
            InlineKeyboardButton(
                "Wie kann ich Ripple XRP kaufen?", callback_data="xrpkaufen",
            )
        ],
        [
            InlineKeyboardButton(
                "Wie erkenne ich einen Scam?", callback_data="scamerkennen"
            )
        ],
        # [InlineKeyboardButton("", callback_data="")],
        # [InlineKeyboardButton("", callback_data="")],
        # [InlineKeyboardButton("", callback_data="")],
    ]
    keyboard.append(back_button())
    return InlineKeyboardMarkup(keyboard)


def advanced_menu():
    """Advanced Menu"""
    keyboard = [
        [
            InlineKeyboardButton(
                "Die 30 besten Krypto-Tools", callback_data="kryptotools"
            )
        ],
        [
            InlineKeyboardButton(
                "Die besten Krypto-Börsen für Bitcoin", callback_data="bitcoinboerse",
            )
        ],
        [
            InlineKeyboardButton(
                "Wie muss ich Bitcoin Gewinne versteuern?",
                callback_data="steuerbitcoin",
            )
        ],
        [
            InlineKeyboardButton(
                "Die besten Blockchain Online Kurse", callback_data="blockchainonline"
            )
        ],
        [InlineKeyboardButton("Die populärsten dApps", callback_data="dapps2020")],
        [
            InlineKeyboardButton(
                "Die besten Peer to Peer Börsen", callback_data="p2pboersen",
            )
        ],
        [
            InlineKeyboardButton(
                "Die besten Blockchain Unternehmen", callback_data="blockchainfirmen",
            )
        ],
        # [InlineKeyboardButton("", callback_data="")],
        # [InlineKeyboardButton("", callback_data="")],
        # [InlineKeyboardButton("", callback_data="")],
        # [InlineKeyboardButton("", callback_data="")],
    ]
    keyboard.append(back_button())
    return InlineKeyboardMarkup(keyboard)


def pro_menu():
    """Pro Menu"""
    keyboard = [
        [
            InlineKeyboardButton(
                "Die besten Cloud Mining Dienste", callback_data="cloudmining"
            )
        ],
        [InlineKeyboardButton("Die besten Stablecoins", callback_data="stablecoins",)],
        [
            InlineKeyboardButton(
                "Die 7 besten Trading Apps", callback_data="appstrading",
            )
        ],
        [
            InlineKeyboardButton(
                "Die Top 10 Telegram Kanäle für Preissignale",
                callback_data="telegramtop10",
            )
        ],
        [
            InlineKeyboardButton(
                "Die besten Investment-Apps", callback_data="investmentapps",
            )
        ],
        [
            InlineKeyboardButton(
                "Bitcoin Margin Trading", callback_data="leveragetrading"
            )
        ],
        [
            InlineKeyboardButton(
                "Die besten Bitcoin Derivate Exchanges",
                callback_data="bitcoinderivate",
            )
        ],
        [
            InlineKeyboardButton(
                "Die besten Krypto Bots für automatisches Trading",
                callback_data="bottrading",
            )
        ],
        # [InlineKeyboardButton("", callback_data="")],
    ]
    keyboard.append(back_button())
    return InlineKeyboardMarkup(keyboard)


# MESSAGES
def lernen_menu_message():
    """Message for users that enter /start"""
    return "<b>Deine Lernreise mit BeInCrypto:</b>\n\nSuch dir ein Thema aus und steige mit uns in den Krypto-Hasenbau hinab.\n\n<b>Hinweis:</b> Die Themen bauen aufeinander auf. Beginne mit der ersten Lektion, wenn du komplett neu bist."


def overview_menu_message():
    """Message for users that enter /menu"""
    return "<b>Hier findest Du all unsere Lerninhalte.</b>\n\nAm besten suchst Du nach Artikeln, die etwas über deinem aktuellen Wissenstand sind."


def beginner_menu_message():
    return "<b>Einsteiger Menü</b>\n\nHier findest Du einsteigerfreundliche Artikel zum Thema Bitcoin, Blockchain und Kryptowährungen.\n\n<b>Falls Du komplett neu bist, empfehlen wir unsere Lernreise unter /start</b>"


def advanced_menu_message():
    return "<b>Advanced Menü</b>\n\nDu weißt bereits was Bitcoin ist und kennst unterschiedliche Kryptowährungen. Am besten besitzt du sogar schon einen kleinen Betrag und hast bereits eine Transaktion getätigt.\nJetzt bist du bereit noch tiefer in einzelne Themen abzusteigen."


def pro_menu_message():
    return "<b>Pro Menü</b>\n\nDu bist ein Pro in Sachen Krypto und interssierst dich für Nischenthemen."


# HELPER
def back_button():
    """Return a backbutton to be appended to the menu. backbutton leads to overview menu"""
    return [InlineKeyboardButton("<-- Zurück", callback_data="overview")]
