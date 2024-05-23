"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query GlitchtipProjectsWithAlerts {
  glitchtip_projects: glitchtip_projects_v1 {
    name
    projectId
    organization {
      name
      instance {
        name
      }
    }
    alerts {
      name
      description
      quantity
      timespanMinutes
      recipients {
        provider
        ... on GlitchtipProjectAlertRecipientWebhook_v1 {
          url
          urlSecret {
            ...VaultSecret
          }
        }
        ... on GlitchtipProjectAlertRecipientEmail_v1 {
          provider
        }
      }
    }
    jira {
      project
      board {
        name
        disable {
          integrations
        }
      }
      labels
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class GlitchtipInstanceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class GlitchtipOrganizationV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    instance: GlitchtipInstanceV1 = Field(..., alias="instance")


class GlitchtipProjectAlertRecipientV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")


class GlitchtipProjectAlertRecipientWebhookV1(GlitchtipProjectAlertRecipientV1):
    url: Optional[str] = Field(..., alias="url")
    url_secret: Optional[VaultSecret] = Field(..., alias="urlSecret")


class GlitchtipProjectAlertRecipientEmailV1(GlitchtipProjectAlertRecipientV1):
    provider: str = Field(..., alias="provider")


class GlitchtipProjectAlertV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    description: str = Field(..., alias="description")
    quantity: int = Field(..., alias="quantity")
    timespan_minutes: int = Field(..., alias="timespanMinutes")
    recipients: list[Union[GlitchtipProjectAlertRecipientWebhookV1, GlitchtipProjectAlertRecipientEmailV1, GlitchtipProjectAlertRecipientV1]] = Field(..., alias="recipients")


class DisableJiraBoardAutomationsV1(ConfiguredBaseModel):
    integrations: Optional[list[str]] = Field(..., alias="integrations")


class JiraBoardV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    disable: Optional[DisableJiraBoardAutomationsV1] = Field(..., alias="disable")


class GlitchtipProjectJiraV1(ConfiguredBaseModel):
    project: Optional[str] = Field(..., alias="project")
    board: Optional[JiraBoardV1] = Field(..., alias="board")
    labels: Optional[list[str]] = Field(..., alias="labels")


class GlitchtipProjectsV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    project_id: Optional[str] = Field(..., alias="projectId")
    organization: GlitchtipOrganizationV1 = Field(..., alias="organization")
    alerts: Optional[list[GlitchtipProjectAlertV1]] = Field(..., alias="alerts")
    jira: Optional[GlitchtipProjectJiraV1] = Field(..., alias="jira")


class GlitchtipProjectsWithAlertsQueryData(ConfiguredBaseModel):
    glitchtip_projects: Optional[list[GlitchtipProjectsV1]] = Field(..., alias="glitchtip_projects")


def query(query_func: Callable, **kwargs: Any) -> GlitchtipProjectsWithAlertsQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        GlitchtipProjectsWithAlertsQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return GlitchtipProjectsWithAlertsQueryData(**raw_data)
