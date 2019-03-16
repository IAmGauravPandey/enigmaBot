from zulip_bots.test_lib import BotTestCase

class TestConverterBot(BotTestCase):
    bot_name = "converter"

    def test_bot(self) -> None:
        dialog = [
            ("", 'Too few arguments given. Enter `@convert help` '
                 'for help on using the converter.\n'),
            ("foo bar", 'Too few arguments given. Enter `@convert help` '
                        'for help on using the converter.\n'),
            ("2 m cm", "2 m = 200.0 cm\n"),
            ("12.0 celsius fahrenheit", "12.0 celsius = 53.600054 fahrenheit\n"),
            ("0.002 kilometer millimile", "0.002 kilometer = 1.2427424 millimile\n"),
            ("3 megabyte kilobit", "3 megabyte = 24576.0 kilobit\n"),
        ]
        self.verify_dialog(dialog)
