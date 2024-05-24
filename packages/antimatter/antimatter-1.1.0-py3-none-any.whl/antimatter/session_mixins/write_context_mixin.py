from typing import Any, Callable, Dict, List

import antimatter_api as openapi_client
from antimatter.builders import WriteContextBuilder, WriteContextConfigurationBuilder, WriteContextRegexRuleBuilder
from antimatter.session_mixins.base import BaseMixin


class WriteContextMixin(BaseMixin):
    """
    Session mixin defining CRUD functionality for write contexts.
    """

    def add_write_context(
        self,
        name: str,
        builder: WriteContextBuilder,
    ) -> None:
        """
        Upserts a write context for the current domain and auth

        :param name: The name of the write context to add or update
        :param builder: The builder containing write context configuration
        """
        if builder is None:
            raise ValueError("Write context builder is required")
        openapi_client.ContextsApi(self.authz.get_client()).domain_upsert_write_context(
            domain_id=self.domain_id, context_name=name, add_write_context=builder.build(),
        )

    def list_write_context(self) -> List[Dict[str, Any]]:
        """
        Returns a list of write contexts available for the current domain and auth
        """
        return [ctx.model_dump() for ctx in openapi_client.ContextsApi(self.authz.get_client()).domain_list_write_contexts(self.domain_id).write_contexts]

    def describe_write_context(self, name: str) -> Dict[str, Any]:
        """
        Returns the write context with the given name for the current domain and auth

        :param name: The name of the write context to describe
        :return: The full details of the write context
        """
        return openapi_client.ContextsApi(self.authz.get_client()).domain_describe_write_context(self.domain_id, context_name=name).model_dump()

    def upsert_write_context_configuration(
        self,
        name: str,
        builder: WriteContextConfigurationBuilder,
    ) -> None:
        """
        Update a write context configuration. The write context must already exist.

        :param name: The name of the write context to update the configuration for
        :param builder: The builder containing write context configuration
        """
        if builder is None:
            raise ValueError("Write context configuration builder is required")
        openapi_client.ContextsApi(self.authz.get_client()).domain_upsert_write_context_configuration(
            domain_id=self.domain_id,
            context_name=name,
            write_context_config_info=builder.build(),
        )

    def delete_write_context(self, name: str) -> None:
        """
        Delete a write context. All configuration associated with this write
        context will also be deleted. Domain policy rules referencing this write
        context will be left as-is.

        :param name: The name of the write context to delete
        """
        openapi_client.ContextsApi(self.authz.get_client()).domain_delete_write_context(domain_id=self.domain_id, context_name=name)

    def list_write_context_regex_rules(self, context_name: str) -> List[Dict[str, Any]]:
        """
        List all regex rules for the write context.

        :param context_name: The name of the write context
        :return: The list of rules
        """
        return [rule.model_dump() for rule in openapi_client.ContextsApi(self.authz.get_client()).domain_get_write_context_regex_rules(
            domain_id=self.domain_id,
            context_name=context_name,
        )]

    def insert_write_context_regex_rule(
        self,
        context_name: str,
        builder: WriteContextRegexRuleBuilder,
    ) -> str:
        """
        Create a new regex rule for a write context.

        :param context_name: The name of the write context
        :param builder: The builder containing write context regex rule configuration
        """
        if builder is None:
            raise ValueError("Write context regex rule builder is required")
        return openapi_client.ContextsApi(self.authz.get_client()).domain_insert_write_context_regex_rule(
            domain_id=self.domain_id,
            context_name=context_name,
            write_context_regex_rule=builder.build(),
        ).rule_id

    def delete_write_context_regex_rule(self, context_name: str, rule_id: str) -> None:
        """
        Delete a regex classifier rule for the context.

        :param context_name: The name of the write context
        :param rule_id: The ID of the rule to delete
        """
        openapi_client.ContextsApi(self.authz.get_client()).domain_delete_write_context_regex_rule(
            domain_id=self.domain_id,
            context_name=context_name,
            rule_id=rule_id,
        )

    def delete_write_context_regex_rules(self, context_name: str) -> None:
        """
        Delete the regex classifier rules for the context.

        :param context_name: The name of the write context
        """
        for rule in self.list_write_context_regex_rules(context_name=context_name):
            openapi_client.ContextsApi(self.authz.get_client()).domain_delete_write_context_regex_rule(
                domain_id=self.domain_id,
                context_name=context_name,
                rule_id=rule["id"],
            )
