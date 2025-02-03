import sys
import telebot
import vk_api
from vk_api.upload import VkUpload

I_AM_EXECUTABLE = (True if (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')) else False)
PATH_TO_SELF = sys.executable if I_AM_EXECUTABLE else __file__

from modules.EmailAPIs import *

# ---- Quick settings [for Developers to quickly change behavior without changing all files] ----
VERSION = ['v1.5.3.3', 1533]
LOGO = f"""
███████╗███████╗███████╗████████╗   ██╗  ██╗███████╗██╗   ██╗ ██████╗ ███████╗███╗   ██╗
██╔════╝██╔════╝██╔════╝╚══██╔══╝   ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝ ██╔════╝████╗  ██║
█████╗  ███████╗█████╗     ██║      █████╔╝ █████╗   ╚████╔╝ ██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ╚════██║██╔══╝     ██║      ██╔═██╗ ██╔══╝    ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╗██║   
███████╗███████║███████╗   ██║      ██║  ██╗███████╗   ██║   ╚██████╔╝███████╗██║ ╚████║   
╚══════╝╚══════╝╚══════╝   ╚═╝      ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                      
                                                Project Version: {VERSION[0]}
                                                Project Devs: rzc0d3r, AdityaGarg8, k0re,
                                                              Fasjeit, alejanpa17, Ischunddu,
                                                              soladify, AngryBonk, Xoncia,
                                                              Anteneh13
"""
if '--no-logo' in sys.argv:
    LOGO = f"ESET KeyGen {VERSION[0]} by rzc0d3r\n"

DEFAULT_EMAIL_API = 'fakemail'
AVAILABLE_EMAIL_APIS = ('1secmail', 'guerrillamail', 'developermail', 'mailticking', 'fakemail', 'inboxes', 'incognitomail')
WEB_WRAPPER_EMAIL_APIS = ('guerrillamail', 'mailticking', 'fakemail', 'inboxes', 'incognitomail')
EMAIL_API_CLASSES = {
    'guerrillamail': GuerRillaMailAPI,
    '1secmail': OneSecEmailAPI,
    'developermail': DeveloperMailAPI,
    'mailticking': MailTickingAPI,
    'fakemail': FakeMailAPI,
    'inboxes': InboxesAPI,
    'incognitomail': IncognitoMailAPI
}
MAX_REPEATS_LIMIT = 10

args = {
    'chrome': True,
    'firefox': False,
    'edge': False,

    'key': True,
    'small_business_key': False,
    'advanced_key': False,
    'vpn_codes': False,
    'account': False,
    'protecthub_account': False,
    'only_webdriver_update': False,
    'update': False,
    'reset_eset_vpn': False,
    'install': False,
    'return_exit_code': 0,

    'skip_webdriver_menu': False,
    'no_headless': False,
    'custom_browser_location': '',
    'email_api': DEFAULT_EMAIL_API,
    'custom_email_api': False,
    'skip_update_check': False,
    'no_logo': False,
    'disable_progress_bar': False,
    'disable_output_file': False,
    'repeat': 1
}
# -----------------------------------------------------------------------------------------------

from modules.WebDriverInstaller import *

# Bypassing ESET antivirus detection
from modules.EsetTools import EsetRegister as ER
from modules.EsetTools import EsetKeygen as EK
from modules.EsetTools import EsetVPN as EV
from modules.EsetTools import EsetProtectHubRegister as EPHR
from modules.EsetTools import EsetProtectHubKeygen as EPHK
from modules.EsetTools import EsetVPNResetWindows as EVRW
from modules.EsetTools import EsetVPNResetMacOS as EVRM

from modules.SharedTools import *
from modules.MBCI import *

from modules.Updater import Updater

import traceback
import colorama
import platform
import datetime
import argparse
import time
import re

# -----------------------------------------------------------------------------------------------

def RunMenu():
    MainMenu = ViewMenu(LOGO+'\n---- Main Menu ----')

    SettingMenu = ViewMenu(LOGO+'\n---- Settings Menu ----')
    SettingMenu.add_item(
        OptionAction(
            args,
            title='Browsers',
            action='store_true',
            args_names=['chrome', 'firefox', 'edge'],
            default_value='chrome'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='Modes of operation',
            action='store_true',
            args_names=[
                'key', 'small-business-key', 'advanced-key', 'vpn-codes', 'account',
                'protecthub-account', 'only-webdriver-update', 'reset-eset-vpn', 'update', 'install'
            ],
            default_value='key')
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='Email APIs',
            action='choice',
            args_names='email-api',
            choices=AVAILABLE_EMAIL_APIS,
            default_value=DEFAULT_EMAIL_API
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--skip-webdriver-menu',
            action='bool_switch',
            args_names='skip-webdriver-menu'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--no-headless',
            action='bool_switch',
            args_names='no-headless'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--custom-browser-location',
            action='manual_input',
            args_names='custom-browser-location',
            default_value=''
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--custom-email-api',
            action='bool_switch',
            args_names='custom-email-api'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--skip-update-check',
            action='bool_switch',
            args_names='skip_update_check'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--disable-progress-bar',
            action='bool_switch',
            args_names='disable_progress_bar'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--disable-output-file',
            action='bool_switch',
            args_names='disable_output_file'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--repeat',
            action='manual_input',
            args_names='repeat',
            default_value=1,
            data_type=int,
            data_range=list(range(1, MAX_REPEATS_LIMIT))
        )
    )
    SettingMenu.add_item(MenuAction('Back', SettingMenu.close))
    MainMenu.add_item(MenuAction('Settings', SettingMenu))
    MainMenu.add_item(MenuAction('Start', MainMenu.close))
    MainMenu.add_item(MenuAction('Exit', sys.exit))
    MainMenu.view()

def parse_argv():
    if '--return-exit-code' not in sys.argv:
        print(LOGO)
    if len(sys.argv) == 1: # for MBCI mode
        RunMenu()
    else: # CLI
        args_parser = argparse.ArgumentParser()
        ENABLE_REQUIRED_ARGUMENTS = True
        GLOBAL_OVERRIDE_ARGUMENTS = ['--reset-eset-vpn', '--update',  '--install', '--return-exit-code']
        for argv in GLOBAL_OVERRIDE_ARGUMENTS:
            ENABLE_REQUIRED_ARGUMENTS = (argv not in sys.argv)
            if not ENABLE_REQUIRED_ARGUMENTS:
                break
            # Required
            ## Browsers
        args_browsers = args_parser.add_mutually_exclusive_group(required=ENABLE_REQUIRED_ARGUMENTS)
        args_browsers.add_argument('--chrome', action='store_true', help='Launching the project via Google Chrome browser')
        args_browsers.add_argument('--firefox', action='store_true', help='Launching the project via Mozilla Firefox browser')
        args_browsers.add_argument('--edge', action='store_true', help='Launching the project via Microsoft Edge browser')
        ## Modes of operation
        args_modes = args_parser.add_mutually_exclusive_group(required=ENABLE_REQUIRED_ARGUMENTS)
        args_modes.add_argument('--key', action='store_true', help='Creating a license key for ESET Smart Security Premium')
        args_modes.add_argument('--small-business-key', action='store_true', help='Creating a license key for ESET Small Business Security (1 key - 5 devices)')
        args_modes.add_argument('--advanced-key', action='store_true', help='Creating a license key for ESET PROTECT Advanced (1 key - 25 devices)')
        args_modes.add_argument('--vpn-codes', action='store_true', help='Creating 10 codes for ESET VPN + 1 ESET Small Business Security key')
        args_modes.add_argument('--account', action='store_true', help='Creating a ESET HOME Account (To activate the free trial version)')
        args_modes.add_argument('--protecthub-account', action='store_true', help='Creating a ESET ProtectHub Account (To activate the free trial version)')
        args_modes.add_argument('--only-webdriver-update', action='store_true', help='Updates/installs webdrivers and browsers without generating account and license key')
        args_modes.add_argument('--reset-eset-vpn', action='store_true', help='Trying to reset the license in the ESET VPN application (Windows & macOS only) - Overrides all arguments that are available!!!')
        args_modes.add_argument('--update', action='store_true', help='Switching to program update mode - Overrides all arguments that are available!!!')
        args_modes.add_argument('--install', action='store_true', help='Installs the program and adds it to the environment variable (Windows & macOS only) - Overrides all arguments that are available!!!')   
        args_modes.add_argument('--return-exit-code', type=int, default=0, help='[For developers] Will make the program return the exit code you requested - Overrides all arguments that are available!!!')
        # Optional
        args_parser.add_argument('--skip-webdriver-menu', action='store_true', help='Skips installation/upgrade webdrivers through the my custom wrapper (The built-in selenium-manager will be used)')
        args_parser.add_argument('--no-headless', action='store_true', help='Shows the browser at runtime (The browser is hidden by default, but on Windows 7 this option is enabled by itself)')
        args_parser.add_argument('--custom-browser-location', type=str, default='', help='Set path to the custom browser (to the binary file, useful when using non-standard releases, for example, Firefox Developer Edition)')
        args_parser.add_argument('--email-api', choices=AVAILABLE_EMAIL_APIS, default=DEFAULT_EMAIL_API, help='Specify which api to use for mail')
        args_parser.add_argument('--custom-email-api', action='store_true', help='Allows you to manually specify any email, and all work will go through it. But you will also have to manually read inbox and do what is described in the documentation for this argument')
        args_parser.add_argument('--skip-update-check', action='store_true', help='Skips checking for program updates')
        args_parser.add_argument('--no-logo', action='store_true', help='Replaces ASCII-Art with plain text')
        args_parser.add_argument('--disable-progress-bar', action='store_true', help='Disables the webdriver download progress bar')
        args_parser.add_argument('--disable-output-file', action='store_true', help='Disables the output txt file generation')
        args_parser.add_argument('--repeat', type=int, default=1, help=f'Specifies how many times to repeat generation (Accepts numbers from 1 to {MAX_REPEATS_LIMIT})')
        args_parser.add_argument('--token', help='Token value')
        args_parser.add_argument('--vktoken', type=str, default='', help='VK API Token for posting to group')
        args_parser.add_argument('--vktoken2', type=str, default='', help='VK API Token for posting to group')
        args_parser.add_argument('--vkgroupid', type=str, default='', help='VK Group ID (with minus sign)')
        try:
            global args
            args = vars(args_parser.parse_args())
            if args['repeat'] < 1 or args['repeat'] > MAX_REPEATS_LIMIT:
                print(f'--repeat argument accepts numbers only from 1 to {MAX_REPEATS_LIMIT}!!!')
                raise
        except:
            time.sleep(3)
            sys.exit(-1)

def update():
    Updater().updater_menu(I_AM_EXECUTABLE, PATH_TO_SELF)
    if len(sys.argv) == 1:
        input('\nPress Enter to exit...')
    else:
        time.sleep(3) # exit-delay
    sys.exit(0)

def main(disable_exit=False):
    if args['return_exit_code'] != 0:
        sys.exit(args['return_exit_code'])
    if len(sys.argv) == 1 and not disable_exit: # for MBCI mode
        print()
    try:
        # changing input arguments for special cases
        if not args['update'] and not args['install'] and not args['reset_eset_vpn']:
            if platform.release() == '7' and sys.platform.startswith('win'): # fix for Windows 7
                args['no_headless'] = True
            elif args['advanced_key'] or args['protecthub_account']:
                args['no_headless'] = True
                if not args['custom_email_api']:
                                    if args['email_api'] not in ['mailticking', 'fakemail', 'inboxes', 'incognitomail']:
                                        raise RuntimeError('--advanced-key, --protecthub-account works ONLY if you use the --custom-email-api argument or the following Email APIs: mailticking, fakemail, inboxes!!!')
                        # check program updates
        elif args['update']:
            print(f'{Fore.LIGHTMAGENTA_EX}-- Updater --{Fore.RESET}\n')
            update()
        elif args['reset_eset_vpn']:
            print(f'{Fore.LIGHTMAGENTA_EX}-- Reset ESET VPN --{Fore.RESET}\n')
            if sys.platform.startswith('win'):
                EVRW()
            elif sys.platform == "darwin":
                EVRM()
            else:
                console_log('This feature is for Windows and macOS only!!!', ERROR)
            if len(sys.argv) == 1:
                input('\nPress Enter to exit...')
            else:
                time.sleep(3) # exit-delay
            sys.exit(0)
        elif args['install']:
            print(f'{Fore.LIGHTMAGENTA_EX}-- Installer --{Fore.RESET}\n')
            Installer().install()
            if len(sys.argv) == 1:
                input('\nPress Enter to exit...')
            else:
                time.sleep(3) # exit-delay
            sys.exit(0)
        if not args['skip_update_check'] and not args['update']:
            try:
                print(f'{Fore.LIGHTMAGENTA_EX}-- Updater --{Fore.RESET}\n')
                updater = Updater()
                latest_cloud_version = list(updater.get_releases().keys())[0]
                latest_cloud_version_int = latest_cloud_version[1:].split('.')
                latest_cloud_version_int = int(''.join(latest_cloud_version_int[:-1])+latest_cloud_version_int[-1][0])
                if VERSION[1] > latest_cloud_version_int:
                    console_log(f'The project has an unreleased version, maybe you are using a build from the developer?\n', WARN, True)
                elif latest_cloud_version_int > VERSION[1]:
                    console_log(f'Project update is available up to version: {colorama.Fore.GREEN}{latest_cloud_version}{colorama.Fore.RESET}', WARN)
                    update_now = input(f'[  {colorama.Fore.YELLOW}INPT{colorama.Fore.RESET}  ] {colorama.Fore.CYAN}Do you want to update right now? (y/n): {colorama.Fore.RESET}').strip().lower()
                    if update_now == 'y':
                        update()
                    else:
                        console_log(f'The update has been ignored\n', INFO)
                else:   
                    console_log('Project up to date!!!\n', OK)
            except Exception as e:
                pass
        
        # initialization and configuration of everything necessary for work            
        driver = None
        please_comment = "Активировали ⁉\nПоставьте лайк ❤ и напишите в комментарии 💬"
        token_value = args['token']
        bot = telebot.TeleBot(token_value, parse_mode='MARKDOWNv2')
        webdriver_path = None
        browser_name = GOOGLE_CHROME
        vk_token_value = args['vktoken']
        vk_group_id_value = args['vkgroupid']
        vk_session = vk_api.VkApi(token=vk_token_value,api_version=5.131)
        vk = vk_session.get_api()

        vk_token_value2 = args['vktoken2']
        vk_session2 = vk_api.VkApi(token=vk_token_value2,api_version=5.131)
        vk2 = vk_session2.get_api()

      
        vk_end = "\n\n\n\nАктивировали ⁉\nПоставьте лайк ❤ и напишите в комментарии 💬\n🍺 Поблагодарить - vk.cc/cHjcEr\n\n\n\nНе успеваешь взять бесплатный ключ?\n✅ Подписывайся на наш Telegram канал t.me/mynod32\n✅ Опция \"Персональный ключ на 30 дней\" - 50 руб.\n✅ Опция \"Ключ на 90 дней для EIS, EAV\" - 120 руб."
        upload = VkUpload(vk_session)
        if args['firefox']:
            browser_name = MOZILLA_FIREFOX
        if args['edge']:
            browser_name = MICROSOFT_EDGE
        if not args['skip_webdriver_menu']: # updating or installing webdriver
            if args['custom_browser_location'] != '':
                webdriver_installer = WebDriverInstaller(browser_name, args['custom_browser_location'])
            else:
                webdriver_installer = WebDriverInstaller(browser_name)
            webdriver_path, args['custom_browser_location'] = webdriver_installer.menu(args['disable_progress_bar'])
        if not args['only_webdriver_update']:
            driver = initSeleniumWebDriver(browser_name, webdriver_path, args['custom_browser_location'], (not args['no_headless']))
            if driver is None:
                raise RuntimeError(f'{browser_name} initialization error!')
        else:
            sys.exit(0)

        # main part of the program
        console_log(f'\n{Fore.LIGHTMAGENTA_EX}-- KeyGen --{Fore.RESET}\n')
        if not args['custom_email_api']:  
            console_log(f'[{args["email_api"]}] Mail registration...', INFO)
            if args['email_api'] in WEB_WRAPPER_EMAIL_APIS: # WebWrapper API, need to pass the selenium object to the class initialization
                email_obj = EMAIL_API_CLASSES[args['email_api']](driver)
            else: # real APIs without the need for a browser
                email_obj = EMAIL_API_CLASSES[args['email_api']]()
            try:
                email_obj.init()
                if email_obj.email is not None:
                    console_log('Mail registration completed successfully!', OK)
            except:
                pass
            if email_obj.email is None:
                console_log('Mail registration was not completed, try using a different Email API!\n', ERROR)
        else:
            email_obj = CustomEmailAPI()
            while True:
                email = input(f'[  {colorama.Fore.YELLOW}INPT{colorama.Fore.RESET}  ] {colorama.Fore.CYAN}Enter the email address you have access to: {colorama.Fore.RESET}').strip()
                try:
                    matched_email = re.match(r'[-a-z0-9+.]+@[a-z]+(\.[a-z]+)+', email).group()
                    if matched_email == email:
                        email_obj.email = matched_email
                        console_log('Mail has the correct syntax!', OK)
                        break
                    else:
                        raise RuntimeError
                except:
                    console_log('Invalid email syntax!!!', ERROR)
        
        if email_obj.email is not None:
            eset_password = dataGenerator(10)
            license_key = None
            obtained_from_site = False
            # ESET HOME
            if args['account'] or args['key'] or args['small_business_key'] or args['vpn_codes']:
                ER_obj = ER(email_obj, eset_password, driver)
                ER_obj.createAccount()
                ER_obj.confirmAccount()
                output_line = '\n'.join([
                        '',
                        '-------------------------------------------------',
                        f'Account Email: {email_obj.email}',
                        f'Account Password: {eset_password}',
                        '-------------------------------------------------',
                        ''
                ])
                output_filename = 'ESET ACCOUNTS.txt'
                if args['key'] or args['small_business_key'] or args['vpn_codes']:
                    output_filename = 'ESET KEYS.txt'
                    EK_obj = EK(email_obj, driver, 'ESET HOME' if args['key'] else 'SMALL BUSINESS')
                    EK_obj.sendRequestForKey()
                    license_name, license_key, license_out_date = EK_obj.getLicenseData()
                    license_out_date = license_out_date.replace(".", "/")
                    output_line = '\n'.join([
                        '',
                        '-------------------------------------------------',
                        f'Account Email: {email_obj.email}',
                        f'Account Password: {eset_password}',
                        '',
                        f'License Name: {license_name}',
                        f'License Key: {license_key}',
                        f'License Out Date: {license_out_date}',
                        '-------------------------------------------------',
                        ''
                    ])
                    output_line = f'\n🛡 Продукт: *{license_name}*\n🕐 Срок действия: *{license_out_date}*\n🔐 Ключ активации: `{license_key}`'
                    output_line_vk = f'\n🛡 Продукт: {license_name}\n🕐 Срок действия: {license_out_date}\n🔐 Ключ активации: {license_key}'
                    if args['key']:
                      activate_products = '\n🔓 Ключ подходит для: *ESET Smart Security Premium, ESET HOME Security Premium, ESET MOBILE SECURITY*'
                      activate_products_vk = '\n🔓 Ключ подходит для: ESET Smart Security Premium, ESET HOME Security Premium, ESET MOBILE SECURITY'
                      hashtags = '\n\n\\#ESET \\#NOD32 \\#ESS \\#ESSP \\#HomeSecurity \\#SmartSecurity \\#keys \\#license'
                      photo_attachment = 'photo-203143822_457239282'
                    if args['small_business_key']:
                     activate_products = '\n🔓 Ключ подходит для: *ESET Small Business Security, ESET Cyber Security \(MacOS\), ESET Mobile Security, ESET Smart TV Security, ESET Safe Server*'
                     activate_products_vk = '\n🔓 Ключ подходит для: ESET Small Business Security, ESET Cyber Security (MacOS), ESET Mobile Security, ESET Smart TV Security, ESET Safe Server'
                     hashtags = '\n\n\\#ESET \\#NOD32 \\#ESBS \\#SmallBusiness \\#keys \\#license'
                     photo_attachment = 'photo-203143822_457239283'
                    if args['vpn_codes']:
                     activate_products = '\n🔓 Ключ подходит для: *ESET Small Business Security, ESET Cyber Security \(MacOS\), ESET Mobile Security, ESET Smart TV Security, ESET Safe Server*'
                     activate_products_vk = '\n🔓 Ключ подходит для: ESET Small Business Security, ESET Cyber Security (MacOS), ESET Mobile Security, ESET Smart TV Security, ESET Safe Server'
                     hashtags = '\n\n\\#ESET \\#NOD32 \\#ESBS \\#SmallBusiness \\#keys \\#license'
                     photo_attachment = 'photo-203143822_457239283'
                    bot.send_message(-1002475137672, output_line + activate_products +  "\n\n" + please_comment +"\n\n[⚡️Накидать бустов\!](https://t\.me/boost/mynod32) \| [\@mynod32](https://t\.me/\+wLqOncLmqAIwZGM6)" + hashtags, disable_web_page_preview=True, disable_notification=True)
                    bot.send_message(-1001233475775, output_line + activate_products +  "\n\n" + please_comment +"\n\n[⚡️Накидать бустов\!](https://t\.me/boost/mynod32) \| [\@mynod32](https://t\.me/\+wLqOncLmqAIwZGM6)" + hashtags, disable_web_page_preview=True, disable_notification=True)  
                    vk.wall.post(owner_id=vk_group_id_value, message=output_line_vk + "\n\n" + vk_end , attachments=photo_attachment, donut_paid_duration=1296000)
                    #vk.wall.post(owner_id=vk_group_id_value, message=output_line_vk + "\n\n" + vk_end , attachments=photo_attachment)
                    vk2.wall.post(owner_id=-229183047, message=activate_products_vk + output_line_vk + "\n\n" + vk_end, attachments=photo_attachment)
                    if args['vpn_codes']:
                        EV_obj = EV(email_obj, driver, ER_obj.window_handle)
                        EV_obj.sendRequestForVPNCodes()
                        vpn_codes = EV_obj.getVPNCodes()
                        if not args['custom_email_api']:
                            vpn_codes_line = ', '.join(vpn_codes)
                            output_line = '\n'.join([
                                '',
                                '-------------------------------------------------',
                                f'Account Email: {email_obj.email}',
                                f'Account Password: {eset_password}',
                                '',
                                f'License Name: {license_name}',
                                f'License Key: {license_key}',
                                f'License Out Date: {license_out_date}',
                                '',
                                f'VPN Codes: {vpn_codes_line}',
                                '-------------------------------------------------',
                                ''
                            ])
                            hashtags = '\n\n\\#ESET \\#NOD32 \\#VPN \\#proxy \\#keys \\#license'
                            photo_attachment = 'photo-203143822_457239280'
                            license_keys_formatted = "".join([f"🔐 Ключ активации: `{key}`\n\n" for key in vpn_codes_line.split(', ')])
                            license_keys_formatted_vk = "".join([f"🔐 Ключ активации: {key}\n" for key in vpn_codes_line.split(', ')])
                            output_line = f'\n🛡 Продукт: *ESET VPN*\n🕐 Срок действия: *{license_out_date}*\n\n{license_keys_formatted}\n'
                            output_line_vk = f'\n🛡 Продукт: ESET VPN\n🕐 Срок действия: {license_out_date}\n\n{license_keys_formatted_vk}\n'
                            bot.send_message(-1002475137672, output_line + please_comment +"\n\n[⚡️Накидать бустов\!](https://t\.me/boost/mynod32) \| [\@mynod32](https://t\.me/\+wLqOncLmqAIwZGM6)" + hashtags, disable_web_page_preview=True, disable_notification=True)
                            bot.send_message(-1001233475775, output_line + please_comment +"\n\n[⚡️Накидать бустов\!](https://t\.me/boost/mynod32) \| [\@mynod32](https://t\.me/\+wLqOncLmqAIwZGM6)" + hashtags, disable_web_page_preview=True, disable_notification=True)
                            vk.wall.post(owner_id=vk_group_id_value, message=output_line_vk + "\n\n" + vk_end , attachments=photo_attachment, donut_paid_duration=1296000)
                            #vk.wall.post(owner_id=vk_group_id_value, message=output_line_vk + "\n\n" + vk_end , attachments=photo_attachment)
                            vk2.wall.post(owner_id=-229183047, message=output_line_vk + "\n\n" + vk_end, attachments=photo_attachment)
            # ESET ProtectHub
            elif args['protecthub_account'] or args['advanced_key']:
                EPHR_obj = EPHR(email_obj, eset_password, driver)
                EPHR_obj.createAccount()
                EPHR_obj.confirmAccount()
                EPHR_obj.activateAccount()
                output_line = '\n'.join([
                        '',
                        '---------------------------------------------------------------------',
                        f'ESET ProtectHub Account Email: {email_obj.email}',
                        f'ESET ProtectHub Account Password: {eset_password}',
                        '---------------------------------------------------------------------',
                        ''
                ])    
                output_filename = 'ESET ACCOUNTS.txt'
                if args['advanced_key']:
                    output_filename = 'ESET KEYS.txt'
                    EPHK_obj = EPHK(email_obj, eset_password, driver)
                    license_name, license_key, license_out_date, obtained_from_site = EPHK_obj.getLicenseData()
                    license_out_date = license_out_date.replace(".", "/")
                    if license_name is not None:
                        output_line = '\n'.join([
                            '',
                            '---------------------------------------------------------------------',
                            f'ESET ProtectHub Account Email: {email_obj.email}',
                            f'ESET ProtectHub Account Password: {eset_password}',
                            '',
                            f'License Name: {license_name}',
                            f'License Key: {license_key}',
                            f'License Out Date: {license_out_date}',
                            '---------------------------------------------------------------------',
                            ''
                        ])
                    output_line = f'\n🛡 Продукт: *{license_name}*\n🕐 Срок действия: *{license_out_date}*\n🔐 Ключ активации: `{license_key}`'
                    output_line_vk = f'\n🛡 Продукт: {license_name}\n🕐 Срок действия: {license_out_date}\n🔐 Ключ активации: {license_key}'
                    if args['key']:
                      activate_products = '\n🔓 Ключ подходит для: *ESET Smart Security Premium, ESET HOME Security Premium, ESET MOBILE SECURITY*'
                      activate_products_vk = '\n🔓 Ключ подходит для: ESET Smart Security Premium, ESET HOME Security Premium, ESET MOBILE SECURITY'
                      hashtags = '\n\n\\#ESET \\#NOD32 \\#ESS \\#ESSP \\#HomeSecurity \\#SmartSecurity \\#keys \\#license'
                      photo_attachment = 'photo-203143822_457239282'
                    if args['small_business_key']:
                     activate_products = '\n🔓 Ключ подходит для: *ESET Small Business Security, ESET Cyber Security \(MacOS\), ESET Mobile Security, ESET Smart TV Security, ESET Safe Server*'
                     activate_products_vk = '\n🔓 Ключ подходит для: ESET Small Business Security, ESET Cyber Security (MacOS), ESET Mobile Security, ESET Smart TV Security, ESET Safe Server'
                     hashtags = '\n\n\\#ESET \\#NOD32 \\#ESBS \\#SmallBusiness \\#keys \\#license'
                     photo_attachment = 'photo-203143822_457239283'
                     bot.send_message(-1002475137672, output_line +  "\n\n" + please_comment +"\n\n[⚡️Накидать бустов\!](https://t\.me/boost/mynod32) \| [\@mynod32](https://t\.me/\+wLqOncLmqAIwZGM6)" + hashtags, disable_web_page_preview=True, disable_notification=True)
                     bot.send_message(-1001233475775, output_line +  "\n\n" + please_comment +"\n\n[⚡️Накидать бустов\!](https://t\.me/boost/mynod32) \| [\@mynod32](https://t\.me/\+wLqOncLmqAIwZGM6)" + hashtags, disable_web_page_preview=True, disable_notification=True)
                     vk.wall.post(owner_id=vk_group_id_value, message=output_line_vk + "\n\n" + vk_end , attachments=photo_attachment, donut_paid_duration=1296000)
                     #vk.wall.post(owner_id=vk_group_id_value, message=output_line_vk + "\n\n" + vk_end , attachments=photo_attachment)
                     vk2.wall.post(owner_id=-229183047, message=output_line_vk + "\n\n" + vk_end, attachments=photo_attachment)
            # end
            console_log(output_line)
            if not args['disable_output_file']:
                date = datetime.datetime.now()
                f = open(f"{str(date.day)}.{str(date.month)}.{str(date.year)} - "+output_filename, 'a')
                f.write(output_line)
                f.close()
            
            if license_key is not None and args['advanced_key'] and obtained_from_site:
                unbind_key = input(f'[  {colorama.Fore.YELLOW}INPT{colorama.Fore.RESET}  ] {colorama.Fore.CYAN}Do you want to unbind the key from this account? (y/n): {colorama.Fore.RESET}').strip().lower()
                if unbind_key == 'y':
                    EPHK_obj.removeLicense()
    except Exception as E:
        traceback_string = traceback.format_exc()
        if str(type(E)).find('selenium') and traceback_string.find('Stacktrace:') != -1: # disabling stacktrace output
            traceback_string = traceback_string.split('Stacktrace:', 1)[0]
        console_log(traceback_string, ERROR)
    if not disable_exit:
        if len(sys.argv) == 1:
            input('Press Enter to exit...')
        else:
            time.sleep(3) # exit-delay
    if globals().get('driver', None) is not None:
        driver.quit()
    if not disable_exit:
        sys.exit()

if __name__ == '__main__':
    parse_argv()
    if args['repeat'] == 1:
        main()
    else:
        for i in range(args['repeat']):
            try:
                print(f'\n{Fore.MAGENTA}------------ Initializing of {Fore.YELLOW}{i+1} {Fore.MAGENTA}start ------------{Fore.RESET}\n')
                if i == 0: # the first run sets up the environment for subsequent runs, speeding them up
                    main(disable_exit=True)
                    args['skip_update_check'] = True
                elif i+1 == args['repeat']:
                    main()
                else:
                    main(disable_exit=True)
            except KeyboardInterrupt:
                continue
