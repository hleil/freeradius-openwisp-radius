# Generated by Django 4.0.3 on 2022-04-13 12:53

from django.db import migrations

import openwisp_radius.base.fields

from .. import settings as app_settings


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_radius', '0030_remove_radiuscheck_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='allowed_mobile_prefixes',
            field=openwisp_radius.base.fields.FallbackTextField(
                blank=True,
                default=','.join(app_settings.ALLOWED_MOBILE_PREFIXES),
                fallback=','.join(app_settings.ALLOWED_MOBILE_PREFIXES),
                help_text=(
                    'Comma separated list of international mobile'
                    ' prefixes allowed to register via the user registration API.'
                ),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='birth_date',
            field=openwisp_radius.base.fields.FallbackCharChoiceField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Whether this field should be disabled, allowed or'
                    ' mandatory in the user registration API.'
                ),
                max_length=12,
                null=True,
                verbose_name='birth date',
                fallback=app_settings.OPTIONAL_REGISTRATION_FIELDS.get(
                    'birth_date', None
                ),
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='first_name',
            field=openwisp_radius.base.fields.FallbackCharChoiceField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Whether this field should be disabled, allowed or'
                    ' mandatory in the user registration API.'
                ),
                max_length=12,
                null=True,
                verbose_name='first name',
                fallback=app_settings.OPTIONAL_REGISTRATION_FIELDS.get(
                    'first_name', None
                ),
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='freeradius_allowed_hosts',
            field=openwisp_radius.base.fields.FallbackTextField(
                blank=True,
                default=','.join(app_settings.FREERADIUS_ALLOWED_HOSTS),
                fallback=','.join(app_settings.FREERADIUS_ALLOWED_HOSTS),
                help_text=(
                    'Comma separated list of IP addresses allowed to'
                    ' access freeradius API'
                ),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='last_name',
            field=openwisp_radius.base.fields.FallbackCharChoiceField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Whether this field should be disabled, allowed or'
                    ' mandatory in the user registration API.'
                ),
                max_length=12,
                null=True,
                verbose_name='last name',
                fallback=app_settings.OPTIONAL_REGISTRATION_FIELDS.get(
                    'last_name', None
                ),
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='location',
            field=openwisp_radius.base.fields.FallbackCharChoiceField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Whether this field should be disabled, allowed or'
                    ' mandatory in the user registration API.'
                ),
                max_length=12,
                null=True,
                verbose_name='location',
                fallback=app_settings.OPTIONAL_REGISTRATION_FIELDS.get(
                    'location', None
                ),
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='needs_identity_verification',
            field=openwisp_radius.base.fields.FallbackBooleanChoiceField(
                blank=True,
                default=None,
                help_text=(
                    'Whether identity verification is required at the'
                    ' time of user registration'
                ),
                null=True,
                fallback=app_settings.NEEDS_IDENTITY_VERIFICATION,
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='password_reset_url',
            field=openwisp_radius.base.fields.FallbackURLField(
                blank=True,
                default=app_settings.PASSWORD_RESET_URLS.get('__all__', ''),
                fallback=app_settings.PASSWORD_RESET_URLS.get('__all__', ''),
                help_text='Enter the URL where users can reset their password',
                null=True,
                verbose_name='Password reset URL',
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='registration_enabled',
            field=openwisp_radius.base.fields.FallbackBooleanChoiceField(
                blank=True,
                default=None,
                help_text=(
                    'Whether the registration API endpoint should be enabled or not'
                ),
                null=True,
                fallback=app_settings.REGISTRATION_API_ENABLED,
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='saml_registration_enabled',
            field=openwisp_radius.base.fields.FallbackBooleanChoiceField(
                blank=True,
                default=None,
                help_text=(
                    'Whether the registration using SAML should be enabled or not'
                ),
                null=True,
                verbose_name='SAML registration enabled',
                fallback=app_settings.SAML_REGISTRATION_ENABLED,
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='sms_verification',
            field=openwisp_radius.base.fields.FallbackBooleanChoiceField(
                blank=True,
                default=None,
                help_text=(
                    'Whether users who sign up should be required to'
                    ' verify their mobile phone number via SMS'
                ),
                null=True,
                fallback=app_settings.SMS_VERIFICATION_ENABLED,
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='social_registration_enabled',
            field=openwisp_radius.base.fields.FallbackBooleanChoiceField(
                blank=True,
                default=None,
                help_text=(
                    'Whether the registration using social'
                    ' applications should be enabled or not'
                ),
                null=True,
                fallback=app_settings.SOCIAL_REGISTRATION_ENABLED,
            ),
        ),
    ]
