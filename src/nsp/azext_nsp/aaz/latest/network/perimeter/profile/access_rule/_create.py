# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network perimeter profile access-rule create",
)
class Create(AAZCommand):
    """Creates or updates a network access rule.

    :example: Create IP based access rule
        az network perimeter profile access-rule create -n MyAccessRule --profile-name MyProfile --perimeter-name MyPerimeter -g MyResourceGroup --address-prefixes "[10.10.0.0/16]"

    :example: Create FQDN based access rule
        az network perimeter profile access-rule create -n MyAccessRule --profile-name MyProfile --perimeter-name MyPerimeter -g MyResourceGroup --fqdn "['www.abc.com', 'www.google.com']" --direction "Outbound"

    :example: Create Subscription based access rule
        az network perimeter profile access-rule create -n MyAccessRule --profile-name MyProfile --perimeter-name MyPerimeter -g MyResourceGroup --subscriptions [0].id="<SubscriptionID1>" [1].id="<SubscriptionID2>"

    :example: Create ServiceTags based access rule
        az network perimeter profile access-rule create -n MyAccessRule --profile-name MyProfile --perimeter-name MyPerimeter -g MyResourceGroup --service-tags  "['st1'']" direction "Inbound"
    """

    _aaz_info = {
        "version": "2023-08-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networksecurityperimeters/{}/profiles/{}/accessrules/{}", "2023-08-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.access_rule_name = AAZStrArg(
            options=["-n", "--name", "--access-rule-name"],
            help="The name of the NSP access rule.",
            required=True,
        )
        _args_schema.perimeter_name = AAZStrArg(
            options=["--perimeter-name"],
            help="The name of the network security perimeter.",
            required=True,
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="The name of the NSP profile.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Resource location.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.address_prefixes = AAZListArg(
            options=["--address-prefixes"],
            arg_group="Properties",
            help="Inbound address prefixes (IPv4/IPv6)",
        )
        _args_schema.direction = AAZStrArg(
            options=["--direction"],
            arg_group="Properties",
            help="Direction that specifies whether the access rules is inbound/outbound.",
            enum={"Inbound": "Inbound", "Outbound": "Outbound"},
        )
        _args_schema.email_addresses = AAZListArg(
            options=["--email-addresses"],
            arg_group="Properties",
            help="Outbound rules email address format.",
        )
        _args_schema.fqdn = AAZListArg(
            options=["--fqdn"],
            arg_group="Properties",
            help="Outbound rules fully qualified domain name format.",
        )
        _args_schema.phone_numbers = AAZListArg(
            options=["--phone-numbers"],
            arg_group="Properties",
            help="Outbound rules phone number format.",
        )
        _args_schema.service_tags = AAZListArg(
            options=["--service-tags"],
            arg_group="Properties",
            help="Inbound rules service tag names.",
        )
        _args_schema.subscriptions = AAZListArg(
            options=["--subscriptions"],
            arg_group="Properties",
            help="Subscription id in the ARM id format.",
        )

        address_prefixes = cls._args_schema.address_prefixes
        address_prefixes.Element = AAZStrArg()

        email_addresses = cls._args_schema.email_addresses
        email_addresses.Element = AAZStrArg()

        fqdn = cls._args_schema.fqdn
        fqdn.Element = AAZStrArg()

        phone_numbers = cls._args_schema.phone_numbers
        phone_numbers.Element = AAZStrArg()

        service_tags = cls._args_schema.service_tags
        service_tags.Element = AAZStrArg()

        subscriptions = cls._args_schema.subscriptions
        subscriptions.Element = AAZObjectArg()

        _element = cls._args_schema.subscriptions.Element
        _element.id = AAZStrArg(
            options=["id"],
            help="Subscription ID in the ARM ID fromat.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NspAccessRulesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NspAccessRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityPerimeters/{networkSecurityPerimeterName}/profiles/{profileName}/accessRules/{accessRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accessRuleName", self.ctx.args.access_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkSecurityPerimeterName", self.ctx.args.perimeter_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-08-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("name", AAZStrType, ".access_rule_name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("addressPrefixes", AAZListType, ".address_prefixes")
                properties.set_prop("direction", AAZStrType, ".direction")
                properties.set_prop("emailAddresses", AAZListType, ".email_addresses")
                properties.set_prop("fullyQualifiedDomainNames", AAZListType, ".fqdn")
                properties.set_prop("phoneNumbers", AAZListType, ".phone_numbers")
                properties.set_prop("serviceTags", AAZListType, ".service_tags")
                properties.set_prop("subscriptions", AAZListType, ".subscriptions")

            address_prefixes = _builder.get(".properties.addressPrefixes")
            if address_prefixes is not None:
                address_prefixes.set_elements(AAZStrType, ".")

            email_addresses = _builder.get(".properties.emailAddresses")
            if email_addresses is not None:
                email_addresses.set_elements(AAZStrType, ".")

            fully_qualified_domain_names = _builder.get(".properties.fullyQualifiedDomainNames")
            if fully_qualified_domain_names is not None:
                fully_qualified_domain_names.set_elements(AAZStrType, ".")

            phone_numbers = _builder.get(".properties.phoneNumbers")
            if phone_numbers is not None:
                phone_numbers.set_elements(AAZStrType, ".")

            service_tags = _builder.get(".properties.serviceTags")
            if service_tags is not None:
                service_tags.set_elements(AAZStrType, ".")

            subscriptions = _builder.get(".properties.subscriptions")
            if subscriptions is not None:
                subscriptions.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.subscriptions[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType()
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )
            properties.direction = AAZStrType()
            properties.email_addresses = AAZListType(
                serialized_name="emailAddresses",
            )
            properties.fully_qualified_domain_names = AAZListType(
                serialized_name="fullyQualifiedDomainNames",
            )
            properties.network_security_perimeters = AAZListType(
                serialized_name="networkSecurityPerimeters",
                flags={"read_only": True},
            )
            properties.phone_numbers = AAZListType(
                serialized_name="phoneNumbers",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.service_tags = AAZListType(
                serialized_name="serviceTags",
            )
            properties.subscriptions = AAZListType()

            address_prefixes = cls._schema_on_200_201.properties.address_prefixes
            address_prefixes.Element = AAZStrType()

            email_addresses = cls._schema_on_200_201.properties.email_addresses
            email_addresses.Element = AAZStrType()

            fully_qualified_domain_names = cls._schema_on_200_201.properties.fully_qualified_domain_names
            fully_qualified_domain_names.Element = AAZStrType()

            network_security_perimeters = cls._schema_on_200_201.properties.network_security_perimeters
            network_security_perimeters.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.network_security_perimeters.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.perimeter_guid = AAZStrType(
                serialized_name="perimeterGuid",
                flags={"read_only": True},
            )

            phone_numbers = cls._schema_on_200_201.properties.phone_numbers
            phone_numbers.Element = AAZStrType()

            service_tags = cls._schema_on_200_201.properties.service_tags
            service_tags.Element = AAZStrType()

            subscriptions = cls._schema_on_200_201.properties.subscriptions
            subscriptions.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.subscriptions.Element
            _element.id = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
