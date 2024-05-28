"""VPN related commands."""
import logging

import click

from vss_cli.cli import pass_context
from vss_cli.config import Configuration
from vss_cli.utils.emoji import EMOJI_UNICODE

_LOGGING = logging.getLogger(__name__)
ej_rkt = EMOJI_UNICODE.get(':rocket:')
ej_warn = EMOJI_UNICODE.get(':alien:')


@click.group('vpn', short_help='Manage your VSS VPN account.')
@pass_context
def cli(ctx: Configuration):
    """Manage your VSS vpn account."""
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        ctx.load_config(spinner_cls=spinner_cls, validate=False)


@cli.group('gw', short_help='manage vpn MFA gateway')
@pass_context
def gateway(ctx: Configuration):
    """Manage vpn via mfa."""
    # TODO: check for vpn status
    pass


@gateway.command('on', short_help='enable vpn via mfa')
@click.option(
    '--otp', '-o', prompt='Provide Timed One-Time Password', help='OTP string'
)
@pass_context
def gateway_on(ctx: Configuration, otp):
    """Enable vpn via mfa."""
    click.echo(f'Attempting to enable VPN GW: {ctx.vpn_server}')
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        ctx.totp = otp
        try:
            rv = ctx.enable_vss_vpn()
            _LOGGING.debug(f'{rv=}')
            spinner_cls.stop()
            click.echo(
                f'Successfully enabled. '
                f'Ready to connect to {ctx.vpn_server} {ej_rkt}'
            )
            spinner_cls.start()
        except Exception as e:
            _LOGGING.error(f'An error occurred {ej_warn}: {e}')


@gateway.command('off', short_help='disable vpn via mfa')
@pass_context
def gateway_off(ctx: Configuration):
    """Disable vpn via mfa."""
    click.echo(f'Attempting to disable VPN GW: {ctx.vpn_server}')
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        try:
            rv = ctx.disable_vss_vpn()
            _LOGGING.debug(f'{rv=}')
            spinner_cls.stop()
            click.echo('Successfully disabled VPN GW. ')
            spinner_cls.start()
        except Exception as e:
            _LOGGING.error(f'An error occurred {ej_warn}: {e}')


@cli.command('la', short_help='launch ui')
@click.argument(
    'ui_type',
    type=click.Choice(
        ['ui', 'otp-svc', 'otp-enable', 'otp-disable', 'otp-monitor']
    ),
    required=True,
    default='ui',
)
@pass_context
def stor_launch(ctx: Configuration, ui_type):
    """Launch web ui."""
    cfg = ctx.get_vss_vpn_cfg()
    lookup = {
        'ui': cfg['endpoint'],
        'otp-svc': cfg['otp_svc'],
        'otp-enable': cfg['otp_enable'],
        'otp-disable': cfg['otp_disable'],
        'otp-monitor': cfg['otp_monitor'],
    }
    url = lookup[ui_type]
    click.echo(f'Launching {EMOJI_UNICODE[":globe_showing_Americas:"]}: {url}')
    click.launch(
        url,
    )
